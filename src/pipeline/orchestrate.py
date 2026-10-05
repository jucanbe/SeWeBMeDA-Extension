"""Shared orchestration: console logging, model lifecycle with bounded recovery, smoke tests, estimates."""
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Dict, List, Optional

from pipeline.journal import journal, set_journal
from pipeline.model_store import ensure_model
from pipeline.paths import LOGS_DIR, configure_environment
from pipeline.progress import fmt_s
from pipeline.registry import ModelSpec
from pipeline.server import ServerError, VLLMServer, environment
from pipeline.workqueue import ServerDown


class Tee:
    def __init__(self, stream, path: Path):
        self.stream = stream
        self.f = open(path, "a", encoding="utf-8")

    def write(self, s):
        self.stream.write(s)
        self.f.write(s.replace("\r", "\n") if "\r" in s else s)
        self.f.flush()

    def flush(self):
        self.stream.flush()
        self.f.flush()

    def isatty(self):
        return self.stream.isatty()


def start_logging(name: str) -> Path:
    configure_environment()
    set_journal(name)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    log_dir = LOGS_DIR / f"{name}_{stamp}"
    log_dir.mkdir(parents=True, exist_ok=True)
    sys.stdout = Tee(sys.stdout, log_dir / "console.log")
    sys.stderr = Tee(sys.stderr, log_dir / "console.log")
    journal("execution_start", argv=sys.argv, log_dir=str(log_dir))
    return log_dir


def banner(text: str):
    print("\n" + "=" * 78 + f"\n{text}\n" + "=" * 78, flush=True)


def prepare_model(spec: ModelSpec) -> Dict:
    banner(f"MODEL DOWNLOAD CHECK: {spec.hf_id}")
    return ensure_model(spec)


def with_recovery(server: VLLMServer, work: Callable[[], object], smoke: Callable[[], None], what: str):
    """Run work(); on ServerDown restart the same model (bounded), smoke-test, and resume."""
    while True:
        try:
            return work()
        except ServerDown as e:
            journal("server_down", model=server.spec.hf_id, what=what, error=str(e))
            print(f"\n[SERVER] {e}; completed results are kept")
            server.restart(str(e))          # raises ServerError after MAX_RESTARTS
            smoke()


def smoke_chat(client, messages_list: List[List[Dict]], json_schema_list: List[Optional[Dict]], min_ok: int,
               parse: Callable[[str], object]) -> Dict:
    """A few production-shaped requests; abort if fewer than min_ok give usable JSON."""
    ok, lat, toks = 0, [], []
    for msgs, sch in zip(messages_list, json_schema_list):
        r = client.chat(msgs, sch)
        lat.append(r.latency_s)
        toks.append((r.usage or {}).get("completion_tokens", 0))
        if not r.error and r.finish_reason != "length":
            _, err = parse(r.content)
            ok += err is None
    res = {"requests": len(messages_list), "usable": ok, "mean_latency_s": sum(lat) / max(len(lat), 1),
           "completion_tokens": toks}
    print(f"[SMOKE] {ok}/{len(messages_list)} usable JSON answers, mean latency {res['mean_latency_s']:.1f} s")
    journal("smoke", **res)
    if ok < min_ok:
        raise ServerError(f"smoke test failed: {ok}/{len(messages_list)} usable answers")
    return res


def print_estimate(title: str, rows: List[tuple]):
    """rows: (label, remaining units, rate units/s or None)."""
    banner(title)
    total = 0.0
    for label, remaining, rate in rows:
        if rate:
            t = remaining / rate
            total += t
            print(f"  {label:<34} {remaining:>7} left at {rate:5.1f}/s  ~ {fmt_s(t)}")
        else:
            print(f"  {label:<34} {remaining:>7} left  (rate not measured yet)")
    print(f"  {'Total (measured parts)':<34} {'':>7}               ~ {fmt_s(total)}")
    journal("estimate", title=title, rows=rows, total_s=round(total))


def startup_cleanup():
    """At the start of every stage (lock held): terminate stale servers left by an earlier crashed job."""
    from pipeline import procs
    try:
        res = procs.cleanup_stale()
    except RuntimeError as e:
        raise ServerError(str(e)) from e
    if res["killed"]:
        print(f"[CLEANUP] terminated {len(res['killed'])} stale server group(s) from an earlier run")
    return res
