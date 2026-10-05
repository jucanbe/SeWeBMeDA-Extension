"""Compact progress line: [TAG] done/total | rate | elapsed | ETA."""
import sys
import time


def fmt_s(s: float) -> str:
    s = int(max(0, s))
    return f"{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}"


class Progress:
    def __init__(self, tag: str, total: int, done: int = 0, unit: str = "req", every_s: float = 2.0):
        self.tag, self.total, self.start_done, self.done = tag, total, done, done
        self.unit, self.every_s = unit, every_s
        self.t0 = time.time()
        self._last = 0.0
        self.tty = sys.stdout.isatty()
        self.failed = 0

    def update(self, n: int = 1, failed: int = 0):
        self.done += n
        self.failed += failed
        now = time.time()
        if now - self._last >= (self.every_s if self.tty else 30) or self.done >= self.total:
            self._last = now
            self._print(final=False)

    def rate(self) -> float:
        dt = time.time() - self.t0
        return (self.done - self.start_done) / dt if dt > 0 else 0.0

    def _print(self, final: bool):
        r = self.rate()
        eta = (self.total - self.done) / r if r > 0 else 0
        line = (f"{self.tag} {self.done}/{self.total} | {r:.1f} {self.unit}/s | elapsed {fmt_s(time.time() - self.t0)}"
                f" | ETA {fmt_s(eta)}" + (f" | failed {self.failed}" if self.failed else ""))
        if self.tty and not final:
            sys.stdout.write("\r" + line[:200].ljust(120))
        else:
            sys.stdout.write(line + "\n")
        sys.stdout.flush()

    def close(self):
        if self.tty:
            sys.stdout.write("\n")
        self._print(final=True)
