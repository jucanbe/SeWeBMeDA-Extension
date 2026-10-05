#!/usr/bin/env python3
"""Execution 1: silver annotation with gpt-oss-20b on vLLM (reasoning effort low).

    python3 execution1.py

Annotates the TRAIN control samples (3 x 500) and the original synthetic corpora
(SyntheticDataset/, exact duplicates once). Rerunning the same command resumes:
completed sentences are never redone; failed ones are retried (max 5 attempts).
"""
import argparse
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from pipeline.paths import configure_environment  # noqa: E402

configure_environment()

from experiments import annotation  # noqa: E402
from experiments.data.model import Sentence  # noqa: E402
from experiments.llm.ner import ChatClient, build_messages, parse_response, response_schema  # noqa: E402
from experiments.schemas import get_schema  # noqa: E402
from pipeline.journal import journal  # noqa: E402
from pipeline.orchestrate import (banner, prepare_model, print_estimate, smoke_chat, start_logging,  # noqa: E402
                                  with_recovery)
from pipeline.registry import MODELS  # noqa: E402
from pipeline.server import ExecutionLock, LockBusy, ServerError, VLLMServer, environment  # noqa: E402

BENCHMARK_N = 100                   # first-run benchmark requests, kept as real annotations


def required_inputs():
    files = [ROOT / "SyntheticDataset" / get_schema(d).s_full_file for d in annotation.DATASETS]
    files += [ROOT / "Datasets" / get_schema(d).folder / "train.csv" for d in annotation.DATASETS]
    missing = [str(f.relative_to(ROOT)) for f in files if not f.exists()]
    if missing:
        raise SystemExit(f"missing input files: {missing}")


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--datasets", default=",".join(annotation.DATASETS))
    p.add_argument("--kill-stale", action="store_true", help="stop a stale vLLM server left by an earlier crash")
    p.add_argument("--limit", type=int, default=0, help="debug only: annotate the first N sentences per job")
    a = p.parse_args()
    datasets = [get_schema(d).name for d in a.datasets.split(",")]

    log_dir = start_logging("execution1")
    spec = MODELS["gpt-oss-20b"]
    try:
        with ExecutionLock("execution1"):
            required_inputs()
            jobs = [(d, "control") for d in datasets] + [(d, "original") for d in datasets]
            pending = [j for j in jobs if not annotation.is_complete(*j)]
            banner("EXECUTION 1: gpt-oss-20b silver annotation (reasoning effort low)")
            for d, k in jobs:
                print(f"  {d:<12} {k:<9} {'complete' if (d, k) not in pending else 'to do / resume'}")
            if not pending:
                print("Nothing to do: all annotation jobs are complete.")
                return 0
            prov = prepare_model(spec)
            server = VLLMServer(spec, log_dir, kill_stale=a.kill_stale)
            with server:
                runtime = dict(server.runtime(), local_path=prov["local_path"])
                env = environment({"execution": "execution1"})
                client = ChatClient(spec.hf_id, server.base_url, max_tokens=spec.max_tokens,
                                    extra_body=spec.request_extra)

                mode = {"structured": True}

                def smoke():
                    schema = get_schema(datasets[0])
                    _, items, _, demos, _ = annotation.plan(schema.name, "control")
                    msgs = [build_messages(schema, Sentence(schema.name, "synthetic", "q", s.tokens), demos)
                            for s in items[:5]]
                    sch = [response_schema(schema) if mode["structured"] else None] * 5
                    smoke_chat(client, msgs, sch, min_ok=4, parse=parse_response)

                banner("SMOKE TEST")
                try:
                    smoke()
                except ServerError as e:
                    # gpt-oss + JSON-schema decoding is version dependent in vLLM; fall back to parsing JSON text
                    print(f"[SMOKE] structured output failed ({e}); retrying without response_format")
                    mode["structured"] = False
                    smoke()
                    print("[SMOKE] using unconstrained JSON (recorded in the annotation manifests)")
                journal("annotation_mode", structured=mode["structured"])

                def run(d, k, limit):
                    return with_recovery(server, lambda: annotation.annotate(
                        d, k, client, spec.concurrency, health_check=server.healthy, limit=limit,
                        runtime=runtime, environment=env, structured=mode["structured"]), smoke, f"{d}/{k}")

                if not a.limit and all(not (annotation.out_dir("control", get_schema(d)) / "annotations.jsonl").exists()
                                       for d in datasets):
                    banner(f"FIRST-RUN BENCHMARK ({BENCHMARK_N} {datasets[0]} control sentences, kept as annotations)")
                    t0 = time.time()
                    n0 = run(datasets[0], "control", BENCHMARK_N).completed
                    rate = n0 / (time.time() - t0)
                    remaining = []
                    for d, k in jobs:
                        _, items, _, _, _ = annotation.plan(d, k)
                        done = len(annotation.silver_records(d, k))
                        remaining.append((f"{d} {k}", len(items) - done, rate))
                    print_estimate("Estimated remaining H100 time (gpt-oss annotation)", remaining)

                banner("EXPERIMENT EXECUTION")
                summary = {}
                for d, k in jobs:
                    if annotation.is_complete(d, k) and not a.limit:
                        continue
                    r = run(d, k, a.limit)
                    summary[f"{d}/{k}"] = {"total": r.total, "completed": r.completed, "abandoned": len(r.abandoned)}
            banner("SUMMARY")
            for k, v in summary.items():
                print(f"  {k:<26} {v['completed']}/{v['total']} annotated, {v['abandoned']} abandoned")
            journal("execution_end", summary=summary)
            return 0
    except LockBusy as e:
        print(f"[LOCK] {e}")
        return 3
    except ServerError as e:
        print(f"[SERVER] giving up: {e}\nAll completed annotations are kept; rerun the same command to resume.")
        journal("execution_failed", error=str(e))
        return 2


if __name__ == "__main__":
    sys.exit(main())
