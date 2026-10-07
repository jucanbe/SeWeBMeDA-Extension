#!/usr/bin/env python3
"""Turn the sub-agent outputs into run directories in the study format (predictions.jsonl + manifest.json).

Each Opus run mirrors the Qwen3.5 27B TEST run of the same condition and dataset: same sentences, tokens,
gold and demonstrations; only pred/entities/unaligned come from Opus, aligned with the study code (ner.align).
Repair batches (<batch>_rN) fill items missing from their original batch. Items with no output are kept as
empty predictions and listed in the manifest as missing. Nothing is written inside VLLM_Paper.
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = HERE.parent
sys.path.insert(0, str(PKG / "src"))
from experiments.llm import ner  # noqa: E402
from experiments.schemas import get_schema  # noqa: E402

man = json.loads((HERE / "batches/manifest.json").read_text())
outs = {}
for m in man:  # originals first, then repairs (manifest order)
    f = HERE / "outputs" / f"{m['batch']}.jsonl"
    if f.exists():
        for l in f.read_text().splitlines():
            try:
                r = json.loads(l)
            except Exception:
                continue
            if r.get("id") in m["ids"]:
                outs.setdefault((m["condition"], m["dataset"]), {}).setdefault(r["id"], r)

cells = defaultdict(list)
for m in man:
    if "repair_of" not in m:
        cells[(m["condition"], m["dataset"])] += m["ids"]

for (cond, ds), ids in sorted(cells.items()):
    src = next((PKG / "results/runs").glob(f"test-{cond}-large-{ds}__*"))
    q = {json.loads(l)["sid"]: json.loads(l) for l in open(src / "predictions.jsonl")}
    schema = get_schema(ds)
    got = outs.get((cond, ds), {})
    d = HERE / "runs" / f"opus-{cond}-{ds}"
    d.mkdir(parents=True, exist_ok=True)
    missing = []
    with open(d / "predictions.jsonl", "w", encoding="utf-8") as fh:
        for sid in q:  # keep the order of the Qwen run
            rec = dict(q[sid])
            if sid not in ids:
                continue
            ents = got.get(sid, {}).get("entities")
            if ents is None:
                missing.append(sid); ents = []
            ents = [e for e in ents if isinstance(e, dict)]
            spans, unal = ner.align(rec["tokens"], ents, schema.type_names)
            rec.update(pred=[list(s) for s in spans], entities=ents, unaligned=unal,
                       raw_response=json.dumps({"entities": ents}, ensure_ascii=False),
                       served_model="claude-opus-5-5 (Claude Code sub-agent)", usage=None, latency_s=None,
                       reasoning_chars=None, finish_reason=None, completed_at=None, _key=sid)
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    mf = json.loads((src / "manifest.json").read_text())
    cfg = mf["config"]
    cfg["model"] = {"key": "opus", "id": "claude-opus-5-5", "label": "opus"}
    cfg["name"] = d.name
    json.dump({"name": d.name, "status": "complete", "config": cfg, "mirrors_run": src.name,
               "harness": "Claude Code sub-agents, batches of up to 40 sentences, demonstrations as text",
               "items": len(ids), "missing_outputs": missing},
              open(d / "manifest.json", "w"), indent=1)
    print(d.name, len(ids), "items,", len(missing), "missing")
