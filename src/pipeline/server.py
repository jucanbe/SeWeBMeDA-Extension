"""One-model-at-a-time vLLM lifecycle: lock, pre-start checks, start, readiness, smoke test, stop, restart.

Defence in depth against two models on the GPU:
  1. flock on VLLM_Paper/.execution.lock for the whole execution (execution1 and execution2 share it);
  2. PID file logs/vllm.pid.json of the server this package started (stale ones are reported);
  3. the port must be closed before a start;
  4. no 'vllm serve' / vllm entrypoint process may exist;
  5. nvidia-smi: no compute processes and memory released (waits after a stop);
  6. after a start, /v1/models must list exactly the expected model.
"""
import fcntl
import json
import os
import platform
import shutil
import signal
import socket
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

import httpx

from pipeline.durable import atomic_write_json
from pipeline.journal import journal
from pipeline import procs
from pipeline.paths import HF_HOME, LOCK_FILE, LOGS_DIR, ROOT
from pipeline.registry import COMMON_ARGS, ModelSpec

TEST_MODE = os.environ.get("VLLM_PAPER_TEST_MODE") == "1"     # unit tests only: fake server, no GPU checks
READY_TIMEOUT_S = int(os.environ.get("VLLM_PAPER_READY_TIMEOUT", "1800"))
GPU_FREE_MB = 2048
MAX_RESTARTS = 3
RESTART_BACKOFF_S = [30, 120, 300]


class LockBusy(RuntimeError):
    pass


class ServerError(RuntimeError):
    pass


class ExecutionLock:
    """Host-wide exclusive lock for all executions of this package (released by the kernel on death)."""

    def __init__(self, name: str):
        self.name = name
        self._f = None

    def __enter__(self):
        LOCK_FILE.parent.mkdir(parents=True, exist_ok=True)
        self._f = open(LOCK_FILE, "a+")
        try:
            fcntl.flock(self._f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            self._f.seek(0)
            holder = self._f.read().strip()
            raise LockBusy(f"another execution holds {LOCK_FILE.name}: {holder or 'unknown'}")
        self._f.seek(0)
        self._f.truncate()
        self._f.write(json.dumps({"execution": self.name, "pid": os.getpid(), "host": platform.node(),
                                  "since": datetime.now(timezone.utc).isoformat()}))
        self._f.flush()
        return self

    def __exit__(self, *exc):
        if self._f:
            self._f.seek(0)
            self._f.truncate()
            fcntl.flock(self._f, fcntl.LOCK_UN)
            self._f.close()


# ---------------------------------------------------------------------------
# environment and GPU

def _run(cmd: List[str], timeout: int = 30) -> str:
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout).stdout.strip()
    except Exception:
        return ""


def gpu_status() -> Dict:
    if not shutil.which("nvidia-smi"):
        return {"available": False}
    sel = []
    vis = os.environ.get("CUDA_VISIBLE_DEVICES", "").strip()
    if vis and vis not in ("all", "NoDevFiles"):
        sel = ["-i", vis]                                   # only the GPU(s) this job was given
    gpus = _run(["nvidia-smi", *sel, "--query-gpu=index,name,memory.used,memory.total,driver_version",
                 "--format=csv,noheader,nounits"])
    procs_ = _run(["nvidia-smi", *sel, "--query-compute-apps=pid,process_name,used_memory",
                   "--format=csv,noheader,nounits"])
    rows = [dict(zip(["index", "name", "memory_used_mb", "memory_total_mb", "driver"],
                     [x.strip() for x in line.split(",")])) for line in gpus.splitlines() if line.strip()]
    return {"available": bool(rows), "gpus": rows,
            "compute_processes": [p.strip() for p in procs_.splitlines() if p.strip()]}


def environment(extra: Optional[Dict] = None) -> Dict:
    env = {"hostname": platform.node(), "platform": platform.platform(), "python": sys.version.split()[0],
           "executable": sys.executable, "root": str(ROOT), "hf_home": str(HF_HOME),
           "recorded_at": datetime.now(timezone.utc).isoformat()}
    g = gpu_status()
    env["gpu"] = g
    env["gpu_count"] = len(g.get("gpus", []))
    for mod in ("torch", "vllm", "transformers", "huggingface_hub", "sklearn", "numpy"):
        try:
            m = __import__(mod)
            env[f"{mod}_version"] = getattr(m, "__version__", "?")
        except Exception:
            env[f"{mod}_version"] = None
    try:
        import torch
        env["cuda_version"] = torch.version.cuda
    except Exception:
        env["cuda_version"] = None
    env.update(extra or {})
    return env


def _port_open(port: int) -> bool:
    with socket.socket() as s:
        s.settimeout(1)
        return s.connect_ex(("127.0.0.1", port)) == 0


def preflight(port: int, kill_stale: bool = True):
    """Before any start: terminate stale servers of this package, then refuse while the port or GPU is busy.

    Unrelated vLLM processes of the same user are never signalled; they only matter if they hold our
    port or our GPU, which the checks below detect.
    """
    try:
        procs.cleanup_stale()
    except RuntimeError as e:
        raise ServerError(str(e)) from e
    t0 = time.time()
    while _port_open(port) and time.time() - t0 < 60:
        time.sleep(2)
    if _port_open(port):
        raise ServerError(f"port {port} is in use by a process that is not a server of this package")
    if not TEST_MODE:
        wait_gpu_free()


def wait_gpu_free(timeout_s: int = 180):
    g = gpu_status()
    if not g["available"]:
        raise ServerError("no NVIDIA GPU visible (nvidia-smi)")
    t0 = time.time()
    while True:
        g = gpu_status()
        used = max(int(float(x["memory_used_mb"])) for x in g["gpus"])
        if not g["compute_processes"] and used < GPU_FREE_MB:
            return
        if time.time() - t0 > timeout_s:
            raise ServerError(f"GPU not free: {used} MB used, processes: {g['compute_processes']}")
        time.sleep(5)


def _group_alive(pgid: int) -> bool:
    return procs.group_alive(pgid)


def _kill_group(pgid: int, grace_s: int = 60, proc: Optional[subprocess.Popen] = None) -> bool:
    return procs.terminate_group(pgid, grace_s, proc)


# ---------------------------------------------------------------------------
# server

class VLLMServer:
    def __init__(self, spec: ModelSpec, log_dir: Path, kill_stale: bool = True, offline: bool = True):
        self.spec = spec
        self.offline = offline                       # HF_HUB_OFFLINE for vLLM (False only if remote code needs it)
        self.log_dir = Path(log_dir)
        self.kill_stale = kill_stale
        self.proc: Optional[subprocess.Popen] = None
        self.args_used: Optional[List[str]] = None
        self.restarts = 0
        self.base_url = f"http://127.0.0.1:{spec.port}/v1"
        self.version: Optional[str] = None

    # -- lifecycle --------------------------------------------------------
    def _command(self, extra: List[str]) -> List[str]:
        binary = os.environ.get("VLLM_PAPER_VLLM_BIN")
        if binary:                                   # tests: fake server script
            base = [sys.executable, binary]
        else:
            vllm = Path(sys.executable).with_name("vllm")
            base = [str(vllm) if vllm.exists() else "vllm"]
        return base + ["serve", self.spec.hf_id, "--revision", self.spec.revision,
                       "--served-model-name", self.spec.hf_id, "--host", "127.0.0.1",
                       "--port", str(self.spec.port), *COMMON_ARGS, *extra]

    def start(self):
        preflight(self.spec.port, self.kill_stale)
        attempts = [self.spec.serve_args] + list(self.spec.alt_serve_args)
        last_err = None
        for i, extra in enumerate(attempts):
            try:
                self._start_once(extra)
                return
            except ServerError as e:
                last_err = e
                log = (self.log_dir / f"vllm_{self.spec.key}.log").read_text(errors="replace")[-4000:]
                if "unrecognized arguments" in log or "invalid choice" in log or "no such option" in log.lower():
                    if i + 1 < len(attempts):
                        print(f"[SERVER] vLLM rejected {extra}; trying the documented alternative flags")
                        continue
                raise
        raise last_err

    def _start_once(self, extra: List[str]):
        self.log_dir.mkdir(parents=True, exist_ok=True)
        cmd = self._command(extra)
        env = dict(os.environ)
        self.launch_id = f"{os.getpid()}-{int(time.time() * 1000)}"
        env[procs.OWNER_ENV] = procs.owner_marker(self.launch_id)
        if self.offline:
            env.update(HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1")
        else:
            env.pop("HF_HUB_OFFLINE", None)
            env.pop("TRANSFORMERS_OFFLINE", None)
        log = open(self.log_dir / f"vllm_{self.spec.key}.log", "a")
        log.write(f"\n===== {datetime.now(timezone.utc).isoformat()} START {' '.join(cmd)}\n")
        log.flush()
        print(f"[SERVER] MODEL STARTUP {self.spec.hf_id} (port {self.spec.port}); loading can take minutes")
        self.proc = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT, env=env, start_new_session=True,
                                     cwd=str(ROOT))
        self.pgid = self.proc.pid                     # start_new_session: pid == process group id
        procs.write_record(self.proc.pid, self.pgid, self.spec.hf_id, self.launch_id, cmd,
                           stage=os.environ.get("VLLM_PAPER_STAGE", "") or " ".join(sys.argv[1:]))
        journal("server_start", model=self.spec.hf_id, pid=self.proc.pid, cmd=cmd, hf_offline=self.offline)
        t0 = time.time()
        while time.time() - t0 < READY_TIMEOUT_S:
            if self.proc.poll() is not None:
                _kill_group(self.pgid, grace_s=30, proc=self.proc)     # engine workers may outlive the parent
                self._cleanup()
                raise ServerError(f"vLLM exited during startup (code {self.proc.returncode}); "
                                  f"see logs/{self.log_dir.name}/vllm_{self.spec.key}.log")
            if self.healthy():
                break
            time.sleep(3)
        else:
            self.stop()
            raise ServerError(f"vLLM not ready after {READY_TIMEOUT_S} s")
        served = self.served_models()
        if served != [self.spec.hf_id]:
            self.stop()
            raise ServerError(f"/v1/models lists {served}, expected exactly [{self.spec.hf_id}]")
        self.args_used = extra
        self.version = self._version()
        journal("server_ready", model=self.spec.hf_id, seconds=round(time.time() - t0), vllm_version=self.version)
        print(f"[SERVER] ready after {time.time() - t0:.0f} s (vLLM {self.version})")

    def healthy(self) -> bool:
        try:
            return httpx.get(f"http://127.0.0.1:{self.spec.port}/health", timeout=5).status_code == 200
        except Exception:
            return False

    def alive(self) -> bool:
        return self.proc is not None and self.proc.poll() is None

    def served_models(self) -> List[str]:
        try:
            return [m["id"] for m in httpx.get(f"{self.base_url}/models", timeout=10).json()["data"]]
        except Exception:
            return []

    def _version(self) -> Optional[str]:
        try:
            return httpx.get(f"http://127.0.0.1:{self.spec.port}/version", timeout=5).json().get("version")
        except Exception:
            return None

    def stop(self):
        if self.proc is not None:
            pgid = self.proc.pid                     # start_new_session=True: the PID is the group id
            print(f"[SERVER] stopping {self.spec.hf_id}")
            if not _kill_group(pgid, proc=self.proc):
                print(f"[SERVER] WARNING: process group {pgid} did not exit; it will be cleaned up as stale")
            try:
                self.proc.wait(timeout=30)
            except Exception:
                pass
            journal("server_stop", model=self.spec.hf_id)
        self._cleanup()
        t0 = time.time()
        while _port_open(self.spec.port) and time.time() - t0 < 60:
            time.sleep(1)
        if not TEST_MODE:
            wait_gpu_free()
        self.proc = None

    def _cleanup(self):
        """Remove the ownership record only once the process group is really gone."""
        pgid = getattr(self, "pgid", None)
        if pgid is not None and not procs.group_alive(pgid):
            procs.remove_record(pgid)

    def restart(self, reason: str):
        """Bounded restart of the same model with the same flags."""
        if self.restarts >= MAX_RESTARTS:
            raise ServerError(f"giving up after {MAX_RESTARTS} restarts ({reason})")
        wait = RESTART_BACKOFF_S[min(self.restarts, len(RESTART_BACKOFF_S) - 1)]
        self.restarts += 1
        journal("server_restart", model=self.spec.hf_id, attempt=self.restarts, reason=reason, backoff_s=wait)
        print(f"[SERVER] restart {self.restarts}/{MAX_RESTARTS} of {self.spec.hf_id} in {wait} s: {reason}")
        self.stop()
        time.sleep(wait if not TEST_MODE else 0)
        self._start_once(self.args_used or self.spec.serve_args)

    def runtime(self) -> Dict:
        """Everything that must be identical between DEV and TEST."""
        return {"hf_id": self.spec.hf_id, "revision": self.spec.revision, "vllm_version": self.version,
                "serve_args": COMMON_ARGS + list(self.args_used or []), "request_extra": self.spec.request_extra,
                "tensor_parallel_size": int(COMMON_ARGS[1]), "max_num_seqs": self.spec.max_num_seqs or None}

    # -- context manager: always stop ---------------------------------------
    def __enter__(self):
        self._install_signal_handlers()
        self.start()
        return self

    def __exit__(self, *exc):
        self.stop()

    def _install_signal_handlers(self):
        def handler(signum, frame):
            print(f"\n[SERVER] signal {signum}: stopping vLLM before exit")
            journal("signal", signum=signum)
            try:
                self.stop()
            finally:
                sys.exit(128 + signum)
        for sig in (signal.SIGINT, signal.SIGTERM, signal.SIGHUP):
            signal.signal(sig, handler)
