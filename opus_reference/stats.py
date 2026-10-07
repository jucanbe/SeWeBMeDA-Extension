#!/usr/bin/env python3
"""Paired statistics for the Opus reference: F1 differences to Qwen 27B (paired sentence bootstrap),
AUROC of W_cal against baselines on the Opus spans, and W_cal AUROC Opus vs Qwen 27B (joint sentence bootstrap)."""
import json, sys
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent
PKG = HERE.parent
sys.path.insert(0, str(PKG / "src"))
from experiments.review import analysis as an  # noqa: E402
from experiments.data.adapters import load_jsonl  # noqa: E402
N = 2000
fz = json.loads((PKG / "results/frozen/freeze.json").read_text())
WC, WE = fz["weights"]["W3"], fz["weights"]["W1"]
rng = np.random.default_rng(0)
out = {"f1_diff": {}}
cells = sorted((HERE / "runs").glob("opus-*"))
qruns = {d.name: next((PKG / "results/runs").glob(f"test-{d.name.split('-')[1]}-large-{d.name.split('-', 2)[2]}__*")) for d in cells}
tot = np.zeros((2, 3))
for d in cells:
    o = {r["sid"]: r for r in load_jsonl(d / "predictions.jsonl")}
    q = {r["sid"]: r for r in load_jsonl(qruns[d.name] / "predictions.jsonl")}
    sids = list(o)
    def cnt(r): return [len({tuple(p) for p in r["pred"]} & {tuple(g) for g in r["gold"]}), len(r["pred"]), len(r["gold"])]
    a = np.array([cnt(o[s]) for s in sids], float); b = np.array([cnt(q[s]) for s in sids], float)
    f = lambda m, ix: 2 * m[ix, 0].sum() / (m[ix, 1].sum() + m[ix, 2].sum())
    allix = np.arange(len(sids))
    diffs = [f(a, ix) - f(b, ix) for ix in (rng.integers(0, len(sids), len(sids)) for _ in range(N))]
    out["f1_diff"][d.name] = {"delta": f(a, allix) - f(b, allix), "ci": [float(np.quantile(diffs, .025)), float(np.quantile(diffs, .975))]}
    print(d.name, {k: round(v, 3) if isinstance(v, float) else [round(x, 3) for x in v] for k, v in out["f1_diff"][d.name].items()})

ro = an.load_rows(cells); rq = an.load_rows(list(qruns.values()))
def scores(rows):
    x = an.criterion_matrix(rows)
    return {"W_cal": an.overall(x, WC), "W_eq": an.overall(x, WE), "B0": an.b0_confidence(rows),
            "B1": an.b1_bert(rows), "B2": an.b2_seen(rows).astype(float),
            "W_cal_no_bert": an.overall(an.criterion_matrix(rows, bert=False), WC)}
so, sq = scores(ro), scores(rq)
yo, go = an.labels(ro), an.groups(ro)
out["opus_vs_baselines"] = {k: an.paired_auroc_difference(so[k], so["W_cal"], yo, go, N) for k in ("W_eq", "B0", "B1", "B2", "W_cal_no_bert")}
out["opus_auroc"] = {k: an.auroc(v, yo) for k, v in so.items()}
yq = an.labels(rq)
out["qwen27b_auroc"] = {k: an.auroc(v, yq) for k, v in sq.items()}
for k, v in out["opus_vs_baselines"].items():
    print("opus W_cal minus", k, {a: round(b, 3) for a, b in v.items()})
print("opus auroc", {k: round(v, 3) for k, v in out["opus_auroc"].items()})
print("qwen auroc", {k: round(v, 3) for k, v in out["qwen27b_auroc"].items()})
# W_cal AUROC Opus minus Qwen 27B, resampling sentences jointly (same sentences in both)
key = lambda r: (r["run"].replace("opus-", "").split("__")[0], r["sid"])
sent = sorted({(r["dataset"], r["condition"], r["sid"]) for r in ro} | {(r["dataset"], r["condition"], r["sid"]) for r in rq})
pos = {s: i for i, s in enumerate(sent)}
io = np.array([pos[(r["dataset"], r["condition"], r["sid"])] for r in ro]); iq = np.array([pos[(r["dataset"], r["condition"], r["sid"])] for r in rq])
bo = [np.where(io == i)[0] for i in range(len(sent))]; bq = [np.where(iq == i)[0] for i in range(len(sent))]
diffs = []
for _ in range(N):
    pick = rng.integers(0, len(sent), len(sent))
    a = np.concatenate([bo[i] for i in pick]); b = np.concatenate([bq[i] for i in pick])
    diffs.append(an.auroc(so["W_cal"][a], yo[a]) - an.auroc(sq["W_cal"][b], yq[b]))
out["wcal_auroc_opus_minus_qwen27b"] = {"delta": out["opus_auroc"]["W_cal"] - out["qwen27b_auroc"]["W_cal"],
                                        "ci": [float(np.quantile(diffs, .025)), float(np.quantile(diffs, .975))]}
print("W_cal opus-qwen", out["wcal_auroc_opus_minus_qwen27b"])
(HERE / "results/opus_stats.json").write_text(json.dumps(out, indent=1, default=float))
