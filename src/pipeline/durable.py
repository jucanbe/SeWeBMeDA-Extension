"""Crash-safe files: durable JSONL appends, tolerant resume reading, atomic JSON writes."""
import json
import os
import threading
from pathlib import Path
from typing import Dict, Iterator, List


class CorruptJSONL(RuntimeError):
    pass


def read_jsonl(path: Path, repair: bool = True) -> List[Dict]:
    """All records of a JSONL file.

    An incomplete or unparsable LAST line (interrupted write) is removed from the
    file when repair=True and reported; an unparsable line anywhere else means
    real corruption and raises CorruptJSONL.
    """
    path = Path(path)
    if not path.exists():
        return []
    raw = path.read_bytes()
    if not raw:
        return []
    lines = raw.split(b"\n")
    trailing_newline = raw.endswith(b"\n")
    body = lines[:-1] if trailing_newline else lines
    out = []
    for i, line in enumerate(body):
        if not line.strip():
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            last = i == len(body) - 1
            if not last:
                raise CorruptJSONL(f"{path}: line {i + 1} is not valid JSON (not the last line)")
            if repair:
                keep = b"\n".join(body[:i])
                keep = keep + b"\n" if keep else b""
                with open(path, "r+b") as f:
                    f.truncate(len(keep))
                    f.flush()
                    os.fsync(f.fileno())
                print(f"[RESUME] {path.name}: removed an incomplete last line from an interrupted write")
            break
    else:
        if not trailing_newline and body and body[-1].strip() and repair:
            # last record complete but without newline: add it so the next append starts a new line
            with open(path, "ab") as f:
                f.write(b"\n")
                f.flush()
                os.fsync(f.fileno())
    return out


class DurableAppender:
    """Thread-safe JSONL appender; every record is flushed and fsync'ed before returning."""

    def __init__(self, path: Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()
        self._f = open(self.path, "a", encoding="utf-8")

    def write(self, record: Dict):
        line = json.dumps(record, ensure_ascii=False) + "\n"
        with self._lock:
            self._f.write(line)
            self._f.flush()
            os.fsync(self._f.fileno())

    def close(self):
        with self._lock:
            if not self._f.closed:
                self._f.close()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()


def atomic_write_json(path: Path, data, indent: int = 1):
    """Write to a temporary file, fsync, then os.replace: readers never see a half-written file."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.tmp.{os.getpid()}")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, indent=indent, ensure_ascii=False, default=str))
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)
    try:
        dfd = os.open(path.parent, os.O_RDONLY)
        os.fsync(dfd)
        os.close(dfd)
    except OSError:
        pass


def iter_jsonl(path: Path) -> Iterator[Dict]:
    yield from read_jsonl(path)
