#!/usr/bin/env python3
"""Tiny embedding-model check (no experiment): download/verify nomic-embed and its remote code,
start it in vLLM, send one embedding request, stop; restart offline and repeat; report where caches went.

    python3 smoke_embedding.py
"""
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from pipeline.paths import configure_environment  # noqa: E402

configure_environment()

import httpx  # noqa: E402

from pipeline.model_store import ensure_model, modules_cache_files, status  # noqa: E402
from pipeline.orchestrate import banner, start_logging  # noqa: E402
from pipeline.registry import MODELS  # noqa: E402
from pipeline.server import ExecutionLock, LockBusy, ServerError, VLLMServer  # noqa: E402

OUTSIDE = [Path.home() / ".cache" / "huggingface", Path.home() / ".cache" / "vllm", Path.home() / ".triton",
           Path.home() / ".cache" / "torch", Path.home() / ".cache" / "flashinfer"]


def new_files_outside(since: float):
    hits = []
    for d in OUTSIDE:
        if d.exists():
            hits += [str(p) for p in d.rglob("*") if p.is_file() and p.stat().st_mtime >= since]
    return hits


def one_request(srv) -> int:
    r = httpx.post(f"{srv.base_url}/embeddings", json={"model": srv.spec.hf_id,
                                                       "input": ["search_query: aspirin-induced asthma"]}, timeout=120)
    r.raise_for_status()
    return len(r.json()["data"][0]["embedding"])


def main():
    log_dir = start_logging("smoke_embedding")
    spec = MODELS["nomic-embed"]
    t_start = time.time()
    report = {}
    try:
        with ExecutionLock("smoke_embedding"):
            banner("1. MODEL FILES AND REMOTE CODE")
            prov = ensure_model(spec)
            report["status"] = status(spec)
            report["offline_probe_ok"] = prov["offline_ok"]
            for offline in ([prov["offline_ok"], True] if not prov["offline_ok"] else [True, True]):
                banner(f"2. vLLM START ({'offline' if offline else 'online (first start)'})")
                try:
                    with VLLMServer(spec, log_dir, offline=offline) as srv:
                        dim = one_request(srv)
                        print(f"[SMOKE] embedding request OK, dimension {dim}")
                        report.setdefault("vllm_starts", []).append({"offline": offline, "ok": True, "dim": dim,
                                                                     "vllm": srv.version, "args": srv.args_used})
                except (ServerError, httpx.HTTPError) as e:
                    print(f"[SMOKE] vLLM failed: {e}")
                    report.setdefault("vllm_starts", []).append({"offline": offline, "ok": False, "error": str(e)})
                    break
            if not all(s["ok"] for s in report["vllm_starts"]):
                banner("3. IN-PROCESS FALLBACK")
                from pipeline.local_embed import LocalNomic
                with LocalNomic(prov, spec) as m:
                    v = m.embed(["search_query: aspirin-induced asthma"])
                    report["fallback"] = {"ok": True, "dim": int(v.shape[1]), **m.provenance()}
                    print(f"[SMOKE] fallback embedding OK, dimension {v.shape[1]}")
    except LockBusy as e:
        print(f"[LOCK] {e}")
        return 3
    banner("REPORT")
    report["modules_cached_in_VLLM_Paper"] = modules_cache_files()
    report["new_files_outside_VLLM_Paper"] = new_files_outside(t_start)
    for k, v in report.items():
        print(f"  {k}: {v}")
    ok = all(s["ok"] for s in report.get("vllm_starts", [])) and not report["new_files_outside_VLLM_Paper"]
    print("\nRESULT:", "vLLM nomic-embed works online and offline, caches inside VLLM_Paper" if ok else
          "see details above (log: " + str(log_dir) + ")")
    return 0 if ok or report.get("fallback", {}).get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
