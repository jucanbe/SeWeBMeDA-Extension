#!/usr/bin/env python3
"""Exploratory Opus 5.5 reference: F1 against gold and LAVA reviewer validity on the Opus predictions.

Compares with the Qwen3.5 TEST runs of the same condition and dataset (same sentences). Reads VLLM_Paper,
writes only Opus_reference/results/opus_results.json.
"""
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
PKG = HERE.parent
sys.path.insert(0, str(PKG / "src"))
from experiments.review import analysis as an  # noqa: E402
from experiments.data.adapters import load_jsonl  # noqa: E402

N_BOOT = 2000
fz = json.loads((PKG / "results/frozen/freeze.json").read_text())
W = {"W_cal": fz["weights"]["W3"], "W_eq": fz["weights"]["W1"]}


def f1_block(pred_file):
    recs = list(load_jsonl(pred_file))
    per = np.array([[len({tuple(p) for p in r["pred"]} & {tuple(g) for g in r["gold"]}),
                     len(r["pred"]), len(r["gold"])] for r in recs], dtype=float)

    def f(ix):
        tp, npred, ngold = per[ix].sum(0)
        return 2 * tp / (npred + ngold) if npred + ngold else 0.0
    ci = an.bootstrap_ci(f, np.arange(len(recs)), N_BOOT)
    tp, npred, ngold = per.sum(0)
    return {"f1": f(np.arange(len(recs))), "precision": tp / npred if npred else 0.0, "recall": tp / ngold,
            "ci": [ci["ci_low"], ci["ci_high"]], "sentences": len(recs), "pred": int(npred), "gold": int(ngold)}


def validity(rows, gold_n):
    x, y, g = an.criterion_matrix(rows), an.labels(rows), an.groups(rows)
    out = {"n_spans": len(rows), "share_correct": float(y.mean())}
    cons = np.array([r["scores"]["constraint"] for r in rows], dtype=float)
    tv = np.array([bool(r["type_valid"]) for r in rows])
    for k, w in W.items():
        s = an.overall(x, w)
        dec = an.decide(s, cons, tv)
        out[k] = {"auroc": an.discrimination(s, y, g, N_BOOT), "decisions": an.decision_metrics(dec, y),
                  "filtering": an.filtering(dec == "passed", y, gold_n)}
    out["B0_confidence"] = an.discrimination(an.b0_confidence(rows), y, g, N_BOOT)
    out["B2_seen_in_train"] = an.discrimination(an.b2_seen(rows), y, g, N_BOOT)
    return out


res = {"weights": W, "cells": {}}
for d in sorted((HERE / "runs").glob("opus-*")):
    _, cond, ds = d.name.split("-", 2)
    cell = {}
    for label, run in [("opus", d)] + [(k, next((PKG / "results/runs").glob(f"test-{cond}-{k}-{ds}__*"), None))
                                       for k in ("small", "medium", "large")]:
        if run is None:
            continue
        b = {"f1": f1_block(run / "predictions.jsonl")}
        if (run / "entityclass.jsonl").exists():
            rows = an.load_rows([run])
            b["reviewer"] = validity(rows, b["f1"]["gold"]) if rows else None
        cell[label] = b
    res["cells"][f"{cond}-{ds}"] = cell
    print(cond, ds, {k: round(v["f1"]["f1"], 3) for k, v in cell.items()},
          {k: round(v["reviewer"]["W_cal"]["auroc"]["auroc"], 3) for k, v in cell.items() if v.get("reviewer")}, flush=True)

# pooled reviewer validity on all Opus spans vs all Qwen 27B spans of the same cells
for label, runs in (("opus", sorted((HERE / "runs").glob("opus-*"))),
                    ("large", [next((PKG / "results/runs").glob(f"test-{c}-large-{ds}__*"))
                               for c, ds in (x.name.split("-", 2)[1:] for x in sorted((HERE / "runs").glob("opus-*")))])):
    runs = [r for r in runs if (r / "entityclass.jsonl").exists()]
    if runs:
        rows = an.load_rows(runs)
        gold_n = sum(len(r["gold"]) for x in runs for r in load_jsonl(x / "predictions.jsonl"))
        res.setdefault("pooled", {})[label] = validity(rows, gold_n)
        p = res["pooled"][label]
        print("pooled", label, {k: round(p[k]["auroc"]["auroc"], 3) for k in W},
              {k: {m: round(v, 3) for m, v in p[k]["decisions"].items() if isinstance(v, float)} for k in ("W_cal",)})
(HERE / "results").mkdir(exist_ok=True)
(HERE / "results/opus_results.json").write_text(json.dumps(res, indent=1, default=float))
