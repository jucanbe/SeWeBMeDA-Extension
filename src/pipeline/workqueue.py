"""Resumable, crash-safe execution of many independent LLM requests.

* An item is complete only when a VALID result is in the output JSONL (fsync'ed).
* Every failed attempt is appended to a separate failure log and retried; after
  MAX_ATTEMPTS failed attempts (counted across reruns) the item is abandoned and
  reported, so a run never loops forever on one sentence.
* If the server looks dead (connection errors, 5xx, failed health check), no new
  work is submitted, completed results are kept, and ServerDown is raised so the
  orchestrator can restart the model and call again (resume).
"""
import threading
import time
from collections import Counter
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Optional

from pipeline.durable import DurableAppender, read_jsonl
from pipeline.progress import Progress

MAX_ATTEMPTS = 5


class ServerDown(RuntimeError):
    pass


@dataclass
class Outcome:
    ok: bool
    record: Optional[Dict] = None
    reason: str = ""
    error_kind: Optional[str] = None
    detail: Dict = field(default_factory=dict)


@dataclass
class QueueResult:
    total: int
    completed: int
    abandoned: List[str]
    attempts: Dict[str, int]


def failure_counts(fail_path: Path) -> Counter:
    return Counter(r["key"] for r in read_jsonl(fail_path))


def run_resumable(items: List, key: Callable[[object], str], process: Callable[[object], Outcome],
                  out_path: Path, fail_path: Path, concurrency: int, tag: str,
                  health_check: Optional[Callable[[], bool]] = None, unit: str = "req",
                  max_attempts: int = MAX_ATTEMPTS, on_benchmark: Optional[Callable] = None) -> QueueResult:
    keys = [key(it) for it in items]
    if len(set(keys)) != len(keys):
        raise ValueError("duplicate item keys")
    done = {r["_key"] for r in read_jsonl(out_path)}
    attempts = failure_counts(fail_path)
    progress = Progress(tag, len(items), done=len(done), unit=unit)

    def pending():
        return [it for it in items if key(it) not in done and attempts[key(it)] < max_attempts]

    todo = pending()
    lock = threading.Lock()
    with DurableAppender(out_path) as out, DurableAppender(fail_path) as fail, ThreadPoolExecutor(concurrency) as pool:
        while todo:
            server_down = False
            inflight = {}
            queue = list(todo)
            while queue or inflight:
                while queue and not server_down and len(inflight) < 2 * concurrency:
                    it = queue.pop(0)
                    inflight[pool.submit(process, it)] = it
                if not inflight:
                    break
                finished, _ = wait(list(inflight), return_when=FIRST_COMPLETED)
                for f in finished:
                    it = inflight.pop(f)
                    k = key(it)
                    try:
                        oc = f.result()
                    except Exception as e:                       # a bug in processing: record, never swallow
                        oc = Outcome(False, reason=f"exception: {type(e).__name__}: {e}", error_kind="exception")
                    with lock:
                        if oc.ok:
                            out.write(dict(oc.record, _key=k))
                            done.add(k)
                            progress.update(1)
                        else:
                            attempts[k] += 1
                            fail.write({"key": k, "attempt": attempts[k], "reason": oc.reason,
                                        "error_kind": oc.error_kind, "detail": oc.detail,
                                        "abandoned": attempts[k] >= max_attempts,
                                        "time": datetime.now(timezone.utc).isoformat()})
                            progress.update(0, failed=1)
                            if oc.error_kind in ("connection", "server", "timeout") and not server_down:
                                if health_check is None or not health_check():
                                    server_down = True
                if on_benchmark is not None and on_benchmark(progress):
                    on_benchmark = None
            if server_down:
                progress.close()
                raise ServerDown(f"{tag}: server unavailable")
            todo = pending()
            if todo:
                time.sleep(1)
    progress.close()
    abandoned = sorted(k for k in keys if k not in done and attempts[k] >= max_attempts)
    return QueueResult(len(items), len(done & set(keys)), abandoned, dict(attempts))


def completed_records(out_path: Path) -> Dict[str, Dict]:
    return {r["_key"]: r for r in read_jsonl(out_path)}
