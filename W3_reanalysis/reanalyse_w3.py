#!/usr/bin/env python3
"""Re-analysis of the final H100 study with W3 (DEV-calibrated weights) as the default reviewer.

Read-only with respect to the study outputs: it loads the frozen design, the stored per-span EntityClass
criterion scores of the TEST runs and the DEV validity rows, and recomputes every statistic that the
original analysis reported for the default weights W0, now with the frozen W3 weights in its place.
No model is run, no span is rescored, and nothing is written outside W3_reanalysis/results.

    python3 reanalyse_w3.py [--n-boot 2000]

Output: W3_reanalysis/results/w3_results.json
"""
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = HERE.parent  # repository root
sys.path.insert(0, str(PKG / "src"))

from experiments.review import analysis as an  # noqa: E402
from experiments.review.report import block  # noqa: E402
from experiments.eval.stats import holm  # noqa: E402
from pipeline import design  # noqa: E402
from pipeline import final  # noqa: E402
from pipeline.durable import read_jsonl  # noqa: E402
from pipeline.freeze import DEV_ROWS, verify_freeze  # noqa: E402
from pipeline.registry import QWEN_ORDER  # noqa: E402

OUT = HERE / "results"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-boot", type=int, default=final.N_BOOT_AUROC)
    n_boot = ap.parse_args().n_boot

    fz = verify_freeze()
    w3 = dict(fz["weights"]["W3"])
    w1 = dict(fz["weights"]["W1"])
    # The original code uses an.W0 as "the default reviewer"; W3 takes that role here.
    an.W0 = w3
    schemes = {"W0": w3, "W1": w1}          # reference key "W0" now holds the W3 weights

    runs = final.test_runs(fz)
    dev_rows = read_jsonl(DEV_ROWS)
    primary = [e for (key, ds, cond), e in runs.items() if cond in design.PRIMARY_VALIDITY_CONDITIONS]
    rows = an.load_rows([e.dir for e in primary])
    rows_unaligned = an.load_rows([e.dir for e in primary], include_unaligned=True)

    def gold(sel):
        names = {x["run"] for x in sel}
        return sum(len(r["gold"]) for e in primary if e.dir.name in names for r in e.records_for_evaluation())

    out = {"weights": {"W3": w3, "W1": w1}, "n_boot": n_boot,
           "note": "key 'W0' inside blocks is the reference reviewer, here the W3 weights",
           "pooled": block(rows, dev_rows, schemes, gold(rows), n_boot)}
    print("pooled done", flush=True)
    for key in QWEN_ORDER:
        sub = [r for r in rows if r["model"] == {"4b": "small", "9b": "medium", "27b": "large"}[key]]
        out.setdefault("by_model", {})[key] = block(sub, dev_rows, schemes, gold(sub), n_boot)
        print("model", key, "done", flush=True)
    for ds in design.DATASETS:
        sub = [r for r in rows if r["dataset"] == ds]
        out.setdefault("by_dataset", {})[ds] = block(sub, dev_rows, schemes, gold(sub), 0)
    out["sensitivity_including_unaligned"] = block(rows_unaligned, dev_rows, schemes, gold(rows_unaligned), 0)

    # paired comparisons against W3, Holm within family (same families as the pre-registration)
    x, y, g = an.criterion_matrix(rows), an.labels(rows), an.groups(rows)
    sc = out["pooled"]["scorers_with_bert"]["scorers"]
    # paired differences exist only with bootstrap resamples (n_boot > 0)
    rq_base = {f"W3_vs_{b}": sc[b].get("auroc_minus_W0") for b in ("B0_confidence", "B1_bert_agreement",
                                                                  "B2_seen_in_train", "B3_logistic", "B4_gbt")}
    rq_w = {"W3_vs_W1": sc["W1"].get("auroc_minus_W0"),
            "W3_vs_B3_logistic": sc["B3_logistic"].get("auroc_minus_W0"),
            "W3_vs_B4_gbt": sc["B4_gbt"].get("auroc_minus_W0")}
    for fam, res in (("baselines", rq_base), ("weightings", rq_w)) if n_boot else ():
        adj = holm({k: v["p"] for k, v in res.items()})
        for k in res:
            res[k]["p_holm"], res[k]["reject_holm_0.05"] = adj[k]["p_holm"], adj[k]["reject"]
        out[f"paired_auroc_{fam}"] = res
    out["sentence_level"] = final.sentence_correlations(rows, {e.dir.name: e for e in primary})
    print("validity done", flush=True)

    out["rq5_scorecard"] = final.rq5(runs, n_boot)   # uses an.W0, i.e. W3
    print("rq5 done", flush=True)

    # silver entities: only per-criterion means were stored, so the mean W3 score is their weighted mean
    orig = json.loads((PKG / "results/analysis/final_results.json").read_text())
    silver = {}
    for ds, cell in orig["entityclass_on_silver"].items():
        m = cell["mean"]
        silver[ds] = {"entities": cell["entities"],
                      "mean_W3_from_criterion_means": sum(w3[c] * m[c] for c in an.CRITERIA if w3[c] > 0)}
    out["silver_entities"] = silver

    OUT.mkdir(exist_ok=True)
    (OUT / "w3_results.json").write_text(json.dumps(out, indent=1, default=float))
    print(f"wrote {OUT / 'w3_results.json'}")


if __name__ == "__main__":
    main()
