"""Append-only execution journal for diagnosis (never used to decide what is complete)."""
import json
import os
from datetime import datetime, timezone

from pipeline.paths import LOGS_DIR

_NAME = {"value": "execution"}


def set_journal(name: str):
    _NAME["value"] = name


def journal(event: str, **fields):
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    rec = {"time": datetime.now(timezone.utc).isoformat(), "pid": os.getpid(), "event": event, **fields}
    with open(LOGS_DIR / f"{_NAME['value']}_journal.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False, default=str) + "\n")
        f.flush()
        os.fsync(f.fileno())
