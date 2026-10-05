"""Validity report for a set of scored runs.

    python -m experiments.review.report --eval <run dirs> [--fit <DEV run dirs>] --out results/analysis/<name>.json
                                        [--weights results/frozen/weights.json] [--boot 2000]

--fit    DEV runs on which W3, B3, B4 and the isotonic maps are fitted (required when --eval is TEST).
         Without it the learned scorers are estimated out-of-fold on --eval: a DEV dry run.
The script refuses TEST rows unless --fit is given and contains DEV rows only.
"""
import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np

from experiments.review import analysis as an


def _split_of(rows) -> set:
    return {r["split"] for r in rows}


def block(rows: List[Dict], fit_rows: Optional[List[Dict]], schemes: Dict, gold_n: int, n_boot: int) -> Dict:
    y = an.labels(rows)
    if len(rows) == 0 or y.sum() == 0 or y.sum() == len(y):
        return {"n": len(rows), "note": "no rows or a single class"}
    x = an.criterion_matrix(rows, bert=True)
    constraint = x[:, an.CRITERIA.index("constraint")]
    type_valid = np.array([r["type_valid"] for r in rows], dtype=bool)
    w0 = an.overall(x, an.W0)
    out = {
        "n": len(rows), "n_correct": int(y.sum()), "labels": {l: int(sum(r["label"] == l for r in rows))
                                                               for l in an.ERROR_LABELS},
        "criteria_with_bert": an.criterion_analysis(rows, bert=True, n_boot=n_boot),
        "criteria_without_bert": {"consistency": an.criterion_analysis(rows, bert=False)["consistency"]},
        "scorers_with_bert": an.compare_scorers(rows, fit_rows, schemes, gold_n, bert=True, n_boot=n_boot),
        "scorers_without_bert": an.compare_scorers(rows, fit_rows, schemes, gold_n, bert=False),
        "ablation_W0": an.ablation(rows, an.W0, gold_n, bert=True),
        "strata_W0": an.stratified(w0, rows, an.decide(w0, constraint, type_valid)),
        "strata_criteria": {c: an.stratified(x[:, j], rows) for j, c in enumerate(an.CRITERIA)},
        "score_summary_W0": an.score_summary(rows),
    }
    x_nb = an.criterion_matrix(rows, bert=False)
    out["bert_effect_on_W0"] = an.paired_auroc_difference(an.overall(x_nb, an.W0), w0, y, an.groups(rows),
                                                          n=max(n_boot, 200))
    return out


def build(eval_dirs: List[Path], fit_dirs: Optional[List[Path]], weights_file: Optional[Path], n_boot: int,
          include_unaligned: bool = False) -> Dict:
    rows = an.load_rows(eval_dirs, include_unaligned)
    fit_rows = an.load_rows(fit_dirs, include_unaligned) if fit_dirs else None
    if "test" in _split_of(rows) and (fit_rows is None or _split_of(fit_rows) != {"dev"}):
        raise SystemExit("TEST rows need --fit with DEV runs only (nothing may be fitted on TEST)")
    schemes = an.weight_schemes(json.loads(Path(weights_file).read_text())["schemes"] if weights_file else None)
    gold_by_run = {Path(d).name: an.total_gold([d]) for d in eval_dirs}
    meta = {Path(d).name: json.loads((Path(d) / "manifest.json").read_text())["config"] for d in eval_dirs}

    def gold_for(sel):
        return sum(gold_by_run[r] for r in {x["run"] for x in sel})

    report = {"runs": sorted(gold_by_run), "splits": sorted(_split_of(rows)),
              "fit_runs": sorted(Path(d).name for d in fit_dirs) if fit_dirs else None,
              "weight_schemes": schemes, "include_unaligned": include_unaligned, "bootstrap": n_boot,
              "pooled": block(rows, fit_rows, schemes, gold_for(rows), n_boot)}
    for key, label in (("model", "by_model"), ("dataset", "by_dataset"), ("condition", "by_condition")):
        parts = defaultdict(list)
        for r in rows:
            parts[r[key]].append(r)
        fit_parts = defaultdict(list)
        for r in fit_rows or []:
            fit_parts[r[key]].append(r)
        report[label] = {k: block(v, (fit_parts.get(k) or fit_rows) if fit_rows is not None else None, schemes,
                                  gold_for(v), n_boot if key == "model" else 0) for k, v in sorted(parts.items())}
    if fit_rows is not None:
        # cross-model transfer: learned scorers fitted on one classifier's DEV rows, applied to another's rows
        transfer = {}
        for src in sorted({r["model"] for r in fit_rows}):
            fx = [r for r in fit_rows if r["model"] == src]
            for dst in sorted({r["model"] for r in rows}):
                ev = [r for r in rows if r["model"] == dst]
                res = an.compare_scorers(ev, fx, schemes, gold_for(ev))
                transfer[f"{src}->{dst}"] = {k: res["scorers"][k]["auroc"] for k in ("B3_logistic", "B4_gbt")}
        report["cross_model_transfer_auroc"] = transfer
    report["run_configs"] = meta
    return report


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--eval", nargs="+", required=True)
    p.add_argument("--fit", nargs="*")
    p.add_argument("--weights")
    p.add_argument("--out", required=True)
    p.add_argument("--boot", type=int, default=0)
    p.add_argument("--include-unaligned", action="store_true")
    a = p.parse_args()
    rep = build([Path(x) for x in a.eval], [Path(x) for x in a.fit] if a.fit else None, a.weights, a.boot,
                a.include_unaligned)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(rep, indent=1))
    pooled = rep["pooled"]
    print(json.dumps({"n": pooled["n"], "criteria_auroc": {c: round(v["auroc"], 3) for c, v in
                                                            pooled["criteria_with_bert"].items()},
                      "scorers_auroc": {k: round(v["auroc"], 3) for k, v in
                                        pooled["scorers_with_bert"]["scorers"].items()}}, indent=1))
