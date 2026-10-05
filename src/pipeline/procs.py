"""Ownership of vLLM servers launched by this package, and automatic cleanup of stale ones.

Every server is launched
  * in its own process group (start_new_session),
  * with VLLM_PAPER_OWNER=<package root>|<launch id> in its environment (inherited by the
    engine-core workers), and cwd = the package root,
and a record logs/vllm_owned/<pgid>.json holds: pid, pgid, model, stage, launch id, launch time,
command line, controller pid, host and SLURM job id.

A process is OWNED by this package if its environment carries our marker (current launches) or,
for servers started before markers existed, if it is a vLLM process whose cwd is this package root.
Everything else is UNRELATED and is never signalled.

Stale = owned and its controller is gone. Every execution holds the package-wide flock, so while we hold
it no other controller of this package can be alive; owned groups that are not ours are therefore stale.
They are terminated (SIGTERM, wait, SIGKILL), and their records are removed only after the group is gone.
"""
import json
import os
import platform
import signal
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

from pipeline.durable import atomic_write_json
from pipeline.journal import journal
from pipeline.paths import LOGS_DIR, PID_FILE, ROOT

OWNER_ENV = "VLLM_PAPER_OWNER"
OWNED_DIR = LOGS_DIR / "vllm_owned"
ROOT_REAL = os.path.realpath(ROOT)


def owner_marker(launch_id: str) -> str:
    return f"{ROOT_REAL}|{launch_id}"


# ---------------------------------------------------------------------------
# process inspection (Linux /proc; ps/lsof fallback elsewhere)

def _run(cmd: List[str]) -> str:
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=30).stdout
    except Exception:
        return ""


def list_processes() -> List[Dict]:
    out = []
    if Path("/proc").is_dir() and Path("/proc/self/stat").exists():
        uid = os.getuid()
        for d in Path("/proc").iterdir():
            if not d.name.isdigit():
                continue
            try:
                if d.stat().st_uid != uid:
                    continue
                raw = (d / "cmdline").read_bytes()
                argv = [x.decode(errors="replace") for x in raw.split(b"\0") if x]
                cmd = " ".join(argv)
                comm = (d / "comm").read_text().strip()
                stat = (d / "stat").read_text()
                pgid = int(stat[stat.rindex(")") + 2:].split()[2])
                out.append({"pid": int(d.name), "pgid": pgid, "cmd": cmd or comm, "comm": comm, "argv": argv})
            except (OSError, ValueError):
                continue
        return out
    for line in _run(["ps", "-U", str(os.getuid()), "-o", "pid=,pgid=,comm=,command="]).splitlines():
        parts = line.split(None, 3)
        if len(parts) >= 3 and parts[0].isdigit():
            cmd = parts[3] if len(parts) > 3 else parts[2]
            out.append({"pid": int(parts[0]), "pgid": int(parts[1]), "comm": parts[2], "cmd": cmd,
                        "argv": cmd.split()})
    return out


def _environ(pid: int) -> str:
    p = Path(f"/proc/{pid}/environ")
    if p.exists():
        try:
            return p.read_bytes().replace(b"\0", b"\n").decode(errors="replace")
        except OSError:
            return ""
    return _run(["ps", "eww", "-p", str(pid), "-o", "command="])


def _cwd(pid: int) -> str:
    p = Path(f"/proc/{pid}/cwd")
    if p.exists():
        try:
            return os.path.realpath(p)
        except OSError:
            return ""
    out = _run(["lsof", "-a", "-p", str(pid), "-d", "cwd", "-Fn"])
    for line in out.splitlines():
        if line.startswith("n"):
            return os.path.realpath(line[1:])
    return ""


def is_vllm(p: Dict) -> bool:
    """A vLLM server process by its program, not by any text in its arguments (a shell or grep whose
    command line merely mentions vLLM is never matched)."""
    argv = p.get("argv") or []
    if p.get("comm", "").startswith("VLLM::") or p["cmd"].startswith("VLLM::"):
        return True                                            # engine-core / worker processes
    if not argv:
        return False
    prog = os.path.basename(argv[0]).lower()
    if prog == "vllm" and len(argv) > 1 and argv[1] == "serve":
        return True
    if prog.startswith("python") and len(argv) > 1:
        if argv[1] == "-m" and len(argv) > 2 and argv[2].startswith("vllm.entrypoints"):
            return True
        if "serve" in argv[2:]:
            script = " ".join(argv[1:argv.index("serve", 2)])  # ps fallback splits paths containing spaces
            if os.path.basename(script) in ("vllm", "fake_vllm_server.py"):
                return True                                    # python <venv>/bin/vllm serve / test fake
    return False


def classify() -> Dict[str, List[Dict]]:
    """{'owned': [...], 'unrelated': [...]} vLLM processes of this user (never our own process)."""
    owned, unrelated = [], []
    me, my_group, parent = os.getpid(), os.getpgid(0), os.getppid()
    for p in list_processes():
        if p["pid"] in (me, parent) or p["pgid"] == my_group or not is_vllm(p):
            continue
        env = _environ(p["pid"])
        if f"{OWNER_ENV}={ROOT_REAL}|" in env or f"{OWNER_ENV}={ROOT_REAL}%7C" in env:
            p["ownership"] = "marker"
            owned.append(p)
        elif _cwd(p["pid"]) == ROOT_REAL:
            p["ownership"] = "cwd (launched before ownership markers)"
            owned.append(p)
        else:
            unrelated.append(p)
    return {"owned": owned, "unrelated": unrelated}


# ---------------------------------------------------------------------------
# records

def write_record(pid: int, pgid: int, model: str, launch_id: str, cmd: List[str], stage: str) -> Path:
    rec = {"pid": pid, "pgid": pgid, "model": model, "launch_id": launch_id, "stage": stage, "cmd": cmd,
           "launched_at": datetime.now(timezone.utc).isoformat(), "controller_pid": os.getpid(),
           "host": platform.node(), "slurm_job_id": os.environ.get("SLURM_JOB_ID"), "root": ROOT_REAL}
    OWNED_DIR.mkdir(parents=True, exist_ok=True)
    path = OWNED_DIR / f"{pgid}.json"
    atomic_write_json(path, rec)
    return path


def read_records() -> List[Dict]:
    recs = []
    for p in sorted(OWNED_DIR.glob("*.json")) if OWNED_DIR.exists() else []:
        try:
            recs.append(dict(json.loads(p.read_text()), _path=str(p)))
        except (OSError, ValueError):
            recs.append({"_path": str(p), "pgid": int(p.stem) if p.stem.isdigit() else -1})
    if PID_FILE.exists():                                   # legacy single-file record
        try:
            recs.append(dict(json.loads(PID_FILE.read_text()), _path=str(PID_FILE)))
        except (OSError, ValueError):
            recs.append({"_path": str(PID_FILE), "pgid": -1})
    return recs


def group_alive(pgid: int) -> bool:
    if pgid <= 0:
        return False
    try:
        os.killpg(pgid, 0)
        return True
    except (ProcessLookupError, PermissionError):
        return False


def _pid_alive(pid: Optional[int]) -> bool:
    if not pid:
        return False
    try:
        os.kill(pid, 0)
        return True
    except (ProcessLookupError, PermissionError):
        return False


def terminate_group(pgid: int, grace_s: int = 60, proc=None) -> bool:
    """SIGTERM the group, wait up to grace_s, then SIGKILL; True when the group is gone."""
    if not group_alive(pgid):
        return True
    try:
        os.killpg(pgid, signal.SIGTERM)
    except (ProcessLookupError, PermissionError):
        return not group_alive(pgid)
    t0 = time.time()
    while time.time() - t0 < grace_s:
        if proc is not None:
            proc.poll()
        if not group_alive(pgid):
            return True
        time.sleep(1)
    try:
        os.killpg(pgid, signal.SIGKILL)
    except (ProcessLookupError, PermissionError):
        pass
    for _ in range(30):
        if proc is not None:
            proc.poll()
        if not group_alive(pgid):
            return True
        time.sleep(1)
    return False


def remove_record(pgid: int):
    (OWNED_DIR / f"{pgid}.json").unlink(missing_ok=True)


def cleanup_stale(keep_pgids=()) -> Dict:
    """Terminate stale servers owned by this package; never touch unrelated processes.

    Must be called while holding the package flock. Returns {'killed': [...], 'unrelated': [...]}.
    Raises RuntimeError if a stale group cannot be terminated.
    """
    keep = set(keep_pgids)
    found = classify()
    records = read_records()
    groups: Dict[int, Dict] = {}
    for p in found["owned"]:
        if p["pgid"] not in keep:
            groups.setdefault(p["pgid"], {"processes": [], "record": None})["processes"].append(p)
    for r in records:
        g = r.get("pgid", -1)
        if g in keep:
            continue
        if g in groups:
            groups[g]["record"] = r
        elif group_alive(g):
            # a recorded group is alive but none of its processes looked like ours: verify by marker/cwd
            members = [p for p in list_processes() if p["pgid"] == g]
            if members and all(_cwd(p["pid"]) == ROOT_REAL or f"{OWNER_ENV}={ROOT_REAL}|" in _environ(p["pid"])
                               for p in members):
                groups[g] = {"processes": members, "record": r}
    killed = []
    for pgid, info in groups.items():
        rec = info["record"] or {}
        ctrl = rec.get("controller_pid")
        if ctrl and ctrl != os.getpid() and _pid_alive(ctrl) and rec.get("host") == platform.node() \
                and "execution" in _run(["ps", "-p", str(ctrl), "-o", "command="]):
            raise RuntimeError(f"vLLM group {pgid} belongs to a live controller (pid {ctrl}); not touching it")
        desc = ", ".join(f"{p['pid']} {p['cmd'][:60]}" for p in info["processes"])
        print(f"[CLEANUP] stale vLLM server from an earlier run (pgid {pgid}, model {rec.get('model', '?')}, "
              f"ownership {info['processes'][0]['ownership'] if info['processes'] and 'ownership' in info['processes'][0] else 'record'}): "
              f"{desc}")
        if not terminate_group(pgid):
            raise RuntimeError(f"could not terminate stale vLLM group {pgid}")
        killed.append({"pgid": pgid, "model": rec.get("model"), "processes": [p["pid"] for p in info["processes"]]})
        journal("stale_server_killed", pgid=pgid, model=rec.get("model"), record=rec, processes=info["processes"])
    for r in records:                                       # records are removed only once their group is gone
        g = r.get("pgid", -1)
        if g not in keep and not group_alive(g):
            Path(r["_path"]).unlink(missing_ok=True)
    unrelated = classify()["unrelated"]
    if unrelated:
        print("[CLEANUP] vLLM processes not owned by this package are left untouched: "
              + "; ".join(f"{p['pid']} {p['cmd'][:60]}" for p in unrelated))
    return {"killed": killed, "unrelated": [p["pid"] for p in unrelated]}
