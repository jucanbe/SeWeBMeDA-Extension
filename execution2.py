#!/usr/bin/env python3
"""Execution 2: Qwen experiments on vLLM, one model at a time.

    python3 execution2.py --stage dev       DEV grid for Qwen 4B -> 9B -> 27B (resumable)
    python3 execution2.py --stage freeze    score DEV, select k/m/validator, fit W3/B3/B4, freeze TEST design
    python3 execution2.py --stage test      TEST with the frozen design only (after approval)
    python3 execution2.py --stage analyze   all tables and statistics for the paper

Rerunning a stage resumes it. --models 4b,9b,27b restricts the dev/test stages.
"""
import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from pipeline.paths import configure_environment  # noqa: E402

configure_environment()

from experiments.runner import Experiment, derive_validator  # noqa: E402
from pipeline import design  # noqa: E402
from pipeline.journal import journal  # noqa: E402
from pipeline.orchestrate import banner, start_logging, startup_cleanup  # noqa: E402
from pipeline.registry import QWEN_ORDER  # noqa: E402
from pipeline.server import ExecutionLock, LockBusy, ServerError  # noqa: E402


def parse_models(s: str):
    keys = [k.strip().lower() for k in s.split(",") if k.strip()]
    bad = [k for k in keys if k not in QWEN_ORDER]
    if bad:
        raise SystemExit(f"unknown model(s) {bad}; use {','.join(QWEN_ORDER)}")
    return [k for k in QWEN_ORDER if k in keys]       # always small -> large


def stage_dev(models, log_dir, kill_stale):
    from pipeline import qwen
    configs, waiting = {}, []
    for key in models:
        ok, w = qwen.split_runnable(design.dev_configs(key))
        configs[key] = ok
        waiting += w
    if waiting:
        print(f"[DEV] {len(waiting)} runs need the silver annotations of execution1.py and are postponed "
              f"(rerun this stage after execution1.py): e.g. {waiting[:3]}")
    exps = [Experiment(c) for cfgs in configs.values() for c in cfgs]
    qwen.embedding_phase(exps, log_dir, kill_stale)
    summary = qwen.run_llm_stage("dev", configs, log_dir, kill_stale)
    states = [s for per in summary.values() for s in per.values()]
    banner("DEV SUMMARY")
    print(f"  runs complete: {sum(s.startswith('complete') for s in states)}/{len(states)}"
          f"   postponed (waiting for execution1): {len(waiting)}")
    if not waiting and all(s.startswith("complete") for s in states) and models == QWEN_ORDER:
        print("  DEV is complete. Next: python3 execution2.py --stage freeze")
    return 0


def stage_test(models, log_dir, kill_stale):
    from pipeline import qwen
    from pipeline.freeze import verify_freeze
    fz = verify_freeze()
    print(f"[TEST] frozen design verified (frozen at {fz['frozen_at']})")
    configs = {}
    for key in models:
        base = [c for c in fz["test_configs"][key] if not c.get("validator", {}).get("enabled")]
        configs[key] = base
    exps = [Experiment(c) for cfgs in configs.values() for c in cfgs]
    qwen.embedding_phase(exps, log_dir, kill_stale)

    def derive(key):
        for c in fz["test_configs"][key]:
            if not c.get("validator", {}).get("enabled"):
                continue
            src_cond = design.TEST_DERIVED[key][c["condition"]]
            src = next(x for x in configs[key] if x["dataset"] == c["dataset"] and x["condition"] == src_cond)
            src_exp = Experiment(src)
            target = Experiment(c)
            if src_exp.status()["state"].startswith("complete") and not target.status()["state"].startswith("complete"):
                d = derive_validator(src_exp.dir, c["name"], {k: v for k, v in c["validator"].items() if k != "enabled"})
                if d != target.dir:
                    raise ServerError(f"derived run {d.name} does not match the frozen configuration")
                print(f"[TEST] derived {c['name']} (validator, no LLM calls)")

    summary = qwen.run_llm_stage("test", configs, log_dir, kill_stale, frozen_runtime=fz["runtime"],
                                 after_model=derive)
    states = [s for per in summary.values() for s in per.values()]
    banner("TEST SUMMARY")
    print(f"  runs complete: {sum(s.startswith('complete') for s in states)}/{len(states)} (+ derived validator runs)")
    print("  Next: python3 execution2.py --stage analyze")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0],
                                formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    p.add_argument("--stage", required=True, choices=["dev", "freeze", "test", "analyze"])
    p.add_argument("--models", default=",".join(QWEN_ORDER), help="dev/test only, e.g. 4b or 4b,9b")
    p.add_argument("--kill-stale", action="store_true", help="kept for compatibility; stale servers of this package "
                   "are now always cleaned up automatically")
    p.add_argument("--note", default="", help="freeze only: note stored in the frozen design")
    a = p.parse_args()
    models = parse_models(a.models)
    log_dir = start_logging(f"execution2_{a.stage}")
    try:
        with ExecutionLock(f"execution2 --stage {a.stage}"):
            os.environ["VLLM_PAPER_STAGE"] = f"execution2 --stage {a.stage}"
            if a.stage in ("dev", "test"):
                startup_cleanup()
            if a.stage == "dev":
                return stage_dev(models, log_dir, a.kill_stale)
            if a.stage == "freeze":
                from pipeline.freeze import FreezeError, freeze_stage
                try:
                    fz = freeze_stage(a.note)
                except FreezeError as e:
                    print(f"[FREEZE] {e}")
                    return 1
                print(f"[FREEZE] design frozen at {fz['frozen_at']}; report: results/frozen/FREEZE_REPORT.md")
                print("[FREEZE] TEST is NOT started automatically. After approval: python3 execution2.py --stage test")
                return 0
            if a.stage == "test":
                from pipeline.freeze import FreezeError
                try:
                    return stage_test(models, log_dir, a.kill_stale)
                except FreezeError as e:
                    print(f"[TEST] refused: {e}")
                    return 1
            if a.stage == "analyze":
                from pipeline.final import AnalysisError, analyze_stage
                from pipeline.freeze import FreezeError
                try:
                    analyze_stage()
                except (AnalysisError, FreezeError) as e:
                    print(f"[ANALYZE] refused: {e}")
                    return 1
                return 0
    except LockBusy as e:
        print(f"[LOCK] {e}")
        return 3
    except ServerError as e:
        print(f"[SERVER] giving up: {e}\nAll completed results are kept; rerun the same command to resume.")
        journal("execution_failed", error=str(e))
        return 2


if __name__ == "__main__":
    sys.exit(main())
