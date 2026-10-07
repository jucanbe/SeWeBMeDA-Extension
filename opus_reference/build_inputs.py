#!/usr/bin/env python3
"""Build the batch inputs for the exploratory Claude Opus 5.5 reference (E0 and E1 on the frozen TEST subsets).

Read-only with respect to VLLM_Paper. The TEST sentences and the E1 demonstrations are taken from the
Qwen3.5-27B TEST runs (same subsets; E1 retrieval does not depend on the classifier, k = 10). Prompts are
built with the study prompt (ner-v2) and rendered as plain text, because the classifier here is a Claude
Code sub-agent and not a chat endpoint.

    python3 build_inputs.py        -> batches/<cond>_<dataset>_<nn>.md and batches/manifest.json
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = HERE.parent
sys.path.insert(0, str(PKG / "src"))
from experiments.data.adapters import BIOCsvAdapter  # noqa: E402
from experiments.data.model import Sentence  # noqa: E402
from experiments.llm import ner  # noqa: E402
from experiments.schemas import get_schema  # noqa: E402

DATASETS = ["BC5CDR", "BioRED", "MedMentions"]
BATCH = {"E0": 100, "E1": 40}
OUT = HERE / "batches"
OUT.mkdir(exist_ok=True)


def run_dir(cond, ds):
    return next((PKG / "results/runs").glob(f"test-{cond}-large-{ds}__*"))


def render(messages):
    """Plain-text rendering of the chat messages (demonstrations as example pairs)."""
    parts = []
    for m in messages[1:-1]:
        parts.append(("Example input:\n" if m["role"] == "user" else "Example answer:\n") + m["content"])
    parts.append("Input:\n" + messages[-1]["content"])
    return "\n\n".join(parts)


manifest = []
for ds in DATASETS:
    schema = get_schema(ds)
    train = {s.sid: s for s in BIOCsvAdapter(schema).load("train")}
    for cond in ("E0", "E1"):
        recs = [json.loads(l) for l in open(run_dir(cond, ds) / "predictions.jsonl")]
        items = []
        for r in recs:
            q = Sentence(dataset=schema.name, split="test", sid=r["sid"], tokens=r["tokens"])
            demos = [train[d] for d in r["demos"]] if cond == "E1" else []
            msgs = ner.build_messages(schema, q, demos)
            items.append({"id": r["sid"], "text": render(msgs)})
        sysp = ner.system_prompt(schema)
        for b in range(0, len(items), BATCH[cond]):
            chunk = items[b:b + BATCH[cond]]
            name = f"{cond}_{schema.folder}_{b // BATCH[cond]:02d}"
            body = ["# Task", sysp, "", "# Items",
                    "Each item below is independent. Answer every item.", ""]
            for it in chunk:
                body += [f"## Item {it['id']}", it["text"], ""]
            (OUT / f"{name}.md").write_text("\n".join(body))
            manifest.append({"batch": name, "condition": cond, "dataset": ds, "ids": [it["id"] for it in chunk]})
(OUT / "manifest.json").write_text(json.dumps(manifest, indent=1))
print(len(manifest), "batches;", sum(len(m["ids"]) for m in manifest), "items")
