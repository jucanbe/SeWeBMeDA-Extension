#!/usr/bin/env python3
"""Validate sub-agent outputs, align them with the study code and compute micro-F1 against gold."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = HERE.parent
sys.path.insert(0, str(PKG / "src"))
from experiments.llm import ner  # noqa: E402
from experiments.schemas import get_schema  # noqa: E402

man = {m["batch"]: m for m in json.loads((HERE / "batches/manifest.json").read_text())}


def gold_index(cond, ds):
    d = next((PKG / "results/runs").glob(f"test-{cond}-large-{ds}__*"))
    return {json.loads(l)["sid"]: json.loads(l) for l in open(d / "predictions.jsonl")}


def check(batch):
    m = man[batch]; out = HERE / "outputs" / f"{batch}.jsonl"
    if not out.exists():
        return {"batch": batch, "status": "missing"}
    rows, bad = {}, 0
    for l in out.read_text().splitlines():
        if not l.strip():
            continue
        try:
            r = json.loads(l); rows[r["id"]] = r
        except Exception:
            bad += 1
    miss = [i for i in m["ids"] if i not in rows]
    return {"batch": batch, "status": "ok" if not miss and not bad else "incomplete", "n": len(rows),
            "missing": len(miss), "bad_lines": bad}


def f1(batches):
    tp = fp = fn = 0
    q = {"tp": 0, "fp": 0, "fn": 0}
    for b in batches:
        m = man[b]; schema = get_schema(m["dataset"]); g = gold_index(m["condition"], m["dataset"])
        rows = {json.loads(l)["id"]: json.loads(l) for l in (HERE / "outputs" / f"{b}.jsonl").read_text().splitlines() if l.strip()}
        for sid in m["ids"]:
            rec = g[sid]; gold = {tuple(x) for x in rec["gold"]}
            spans, _ = ner.align(rec["tokens"], rows.get(sid, {}).get("entities", []), schema.type_names)
            pred = {tuple(x) for x in spans}
            tp += len(pred & gold); fp += len(pred - gold); fn += len(gold - pred)
            qp = {tuple(x) for x in rec["pred"]}
            q["tp"] += len(qp & gold); q["fp"] += len(qp - gold); q["fn"] += len(gold - qp)
    f = lambda a, b, c: 2 * a / (2 * a + b + c) if a else 0.0
    return {"opus_f1": round(f(tp, fp, fn), 3), "qwen27b_f1_same_items": round(f(q["tp"], q["fp"], q["fn"]), 3), "tp": tp, "fp": fp, "fn": fn}


if __name__ == "__main__":
    bs = sys.argv[1:] or sorted(man)
    st = [check(b) for b in bs]
    for s in st:
        if s["status"] != "ok":
            print(s)
    okb = [s["batch"] for s in st if s["status"] == "ok"]
    print(len(okb), "complete batches of", len(bs))
    if okb:
        print(f1(okb))
