"""Silver annotation (gpt-oss-20b on vLLM) of the TRAIN control sample and of the original synthetic corpora.

Layers per sentence, recorded in `sources`:
  annotator  gpt-oss-20b with the dataset schema and 5 fixed TRAIN demonstrations
  gazetteer  TRAIN gold surface forms with >= 2 mentions, type purity >= 0.9 and
             non-entity ratio < 0.5 (longest match); fills only unannotated tokens
Merge priority: annotator > gazetteer. The requested `domain` of a synthetic row
is only checked (domain_satisfied), never used as a label.

Control sample: 500 TRAIN sentences per dataset (fixed seed, stratified); the
gazetteer excludes the control sentences. It measures silver quality against
gold and provides the E2c demonstration pool.

Outputs (only VALID annotations; failed attempts go to failures.jsonl):
  synthetic/silver_control/<ds>/{annotations.jsonl, failures.jsonl, manifest.json}
  synthetic/s_full_silver/<ds>/{annotations.jsonl, failures.jsonl, manifest.json}
"""
import os
import random
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Dict, List, Optional, Sequence, Tuple

from experiments.data.adapters import BIOCsvAdapter, SFullAdapter
from experiments.data.model import Sentence, Span, normalize_mention, sha256_file
from experiments.kg.build import build_index
from experiments.llm.ner import (PROMPT_VERSION, ChatClient, align, build_messages, parse_response,
                                 prompt_hash, response_schema, schema_hash)
from experiments.schemas import SYNTHETIC_DIR, get_schema
from experiments.subsets import select
from pipeline.durable import atomic_write_json, read_jsonl
from pipeline.workqueue import Outcome, QueueResult, run_resumable

ANNOTATOR_VERSION = "silver-2.0-vllm"
N_DEMOS = 5
DEMO_SEED = 7
CONTROL_N = 500
CONTROL_SEED = 20261002
DATASETS = ["BC5CDR", "BioRED", "MedMentions"]
TEST_SCALE = int(os.environ.get("VLLM_PAPER_TEST_SCALE", "0"))     # end-to-end tests with a fake server only
if TEST_SCALE:
    CONTROL_N = TEST_SCALE


def gazetteer_spans(tokens: List[str], index: Dict[str, Dict], min_count=2, purity=0.9, max_o_ratio=0.5,
                    max_len=6) -> List[Span]:
    norm = [normalize_mention(t) for t in tokens]
    cands = []
    for i in range(len(tokens)):
        for n in range(max_len, 0, -1):
            if i + n > len(tokens):
                continue
            e = index.get(" ".join(norm[i:i + n]))
            if not e or not e["types"]:
                continue
            total = sum(e["types"].values())
            t, c = max(e["types"].items(), key=lambda kv: kv[1])
            if total >= min_count and c / total >= purity and e["o"] / (e["o"] + total) < max_o_ratio:
                cands.append((i, i + n, t))
    return _non_overlapping(sorted(cands, key=lambda s: (-(s[1] - s[0]), s[0])))


def _non_overlapping(spans: Sequence[Span], taken: Optional[set] = None) -> List[Span]:
    taken = set(taken or ())
    out = []
    for s, e, t in spans:
        if any(i in taken for i in range(s, e)):
            continue
        out.append((s, e, t))
        taken.update(range(s, e))
    return out


def merge(annotator: List[Span], gazetteer: List[Span]) -> Tuple[List[Span], Dict]:
    final, sources, taken = [], {}, set()
    for layer, spans in (("annotator", annotator), ("gazetteer", gazetteer)):
        for s in _non_overlapping(sorted(set(spans), key=lambda x: (-(x[1] - x[0]), x[0])), taken):
            final.append(s)
            sources[f"{s[0]}:{s[1]}:{s[2]}"] = layer
            taken.update(range(s[0], s[1]))
    agree = {"annotator_spans": len(annotator), "gazetteer_spans": len(gazetteer),
             "annotator_found_gazetteer": sum(1 for s in gazetteer if s in annotator)}
    return sorted(final), {"sources": sources, "agreement": agree}


def demos_for(train: List[Sentence], exclude: set) -> List[Sentence]:
    pool = [s for s in train if s.sid not in exclude and s.spans and 8 <= len(s.tokens) <= 40]
    return random.Random(DEMO_SEED).sample(pool, N_DEMOS)


class Annotator:
    def __init__(self, schema, client: ChatClient, demos: List[Sentence], structured: bool = True):
        self.schema = schema
        self.client = client
        self.demos = demos
        self.json_schema = response_schema(schema) if structured else None

    def __call__(self, tokens: List[str]) -> Tuple[Optional[List[Span]], Dict, Optional[str], Optional[str]]:
        """(spans or None, meta, failure reason, error kind)."""
        q = Sentence(self.schema.name, "synthetic", "q", tokens)
        messages = build_messages(self.schema, q, self.demos)
        res = self.client.chat(messages, self.json_schema)
        meta = {"raw": res.content, "finish_reason": res.finish_reason, "latency_s": round(res.latency_s, 3),
                "usage": res.usage, "served_model": res.model, "reasoning_chars": len(res.reasoning),
                "prompt_hash": prompt_hash(messages)}
        if res.error:
            return None, meta, res.error, res.error_kind
        ents, err = parse_response(res.content)
        if err or res.finish_reason == "length":
            return None, meta, f"unusable response: {err or 'truncated (finish_reason=length)'}", "response"
        spans, unaligned = align(tokens, ents, self.schema.type_names)
        meta.update(entities=ents, unaligned=unaligned)
        return spans, meta, None, None


def control_ids(train: List[Sentence]) -> List[str]:
    return select(train, CONTROL_N, CONTROL_SEED)


def out_dir(kind: str, schema) -> Path:
    return SYNTHETIC_DIR / {"control": "silver_control", "original": "s_full_silver"}[kind] / schema.folder


def plan(dataset: str, kind: str):
    """(schema, items, gazetteer index, demos, extra manifest fields) for one annotation job."""
    schema = get_schema(dataset)
    train = BIOCsvAdapter(schema).load("train")
    if kind == "control":
        cids = control_ids(train)
        cset = set(cids)
        index = build_index([s for s in train if s.sid not in cset], origin="original")
        demos = demos_for(train, exclude=cset)
        by_id = {s.sid: s for s in train}
        items = [by_id[i] for i in cids]
        extra = {"control_n": CONTROL_N, "control_seed": CONTROL_SEED, "control_ids": cids}
    else:
        index = build_index(train, origin="original")
        demos = demos_for(train, exclude=set())
        source = SFullAdapter(schema)
        unique, copies = {}, Counter()
        for s in source.load():
            key = " ".join(s.provenance["raw_sentence"].split())
            copies[key] += 1
            unique.setdefault(key, s)
        items = list(unique.values())
        if TEST_SCALE:
            items = items[:3 * TEST_SCALE]
        for s in items:
            s.provenance["copies"] = copies[" ".join(s.provenance["raw_sentence"].split())]
        extra = {"source_file": f"SyntheticDataset/{source.path.name}", "source_sha256": sha256_file(source.path),
                 "rows": sum(copies.values()), "unique_sentences": len(unique),
                 "duplicates_policy": "exact duplicate sentences annotated once (first occurrence)"}
    return schema, items, index, demos, extra


def annotate(dataset: str, kind: str, client: ChatClient, concurrency: int,
             health_check: Optional[Callable[[], bool]] = None, limit: int = 0,
             runtime: Optional[Dict] = None, environment: Optional[Dict] = None,
             tag: str = "", structured: bool = True) -> QueueResult:
    schema, items, index, demos, extra = plan(dataset, kind)
    if limit:
        items = items[:limit]
    ann = Annotator(schema, client, demos, structured)
    extra = dict(extra, structured_output="json_schema" if structured else "none (JSON parsed from text)")
    d = out_dir(kind, schema)
    d.mkdir(parents=True, exist_ok=True)

    def process(s: Sentence) -> Outcome:
        spans_a, meta, reason, kind_ = ann(s.tokens)
        if spans_a is None:
            return Outcome(False, reason=reason, error_kind=kind_,
                           detail={k: meta[k] for k in ("finish_reason", "usage", "latency_s")} | {"raw": meta["raw"][:2000]})
        g = gazetteer_spans(s.tokens, index)
        spans, info = merge(spans_a, g)
        rec = {"sid": s.sid, "tokens": s.tokens, "spans": [list(x) for x in spans],
               "label_source": f"silver:{client.model}", "annotator_spans": [list(x) for x in spans_a],
               "gazetteer_spans": [list(x) for x in g], **info, "annotator": meta,
               "annotator_version": ANNOTATOR_VERSION,
               "completed_at": datetime.now(timezone.utc).isoformat()}
        if kind == "control":
            rec["gold"] = [list(x) for x in s.spans]
        else:
            requested = s.provenance["requested_type"]
            rec.update(requested_type=requested, requested_domain=s.provenance["requested_domain"],
                       domain_satisfied=any(x[2] == requested for x in spans), copies=s.provenance["copies"],
                       value=s.provenance["value"], temperature=s.provenance["temperature"])
        return Outcome(True, record=rec)

    started = datetime.now(timezone.utc).isoformat()
    result = run_resumable(items, key=lambda s: s.sid, process=process, out_path=d / "annotations.jsonl",
                           fail_path=d / "failures.jsonl", concurrency=concurrency,
                           tag=tag or f"[GPT-OSS][{schema.name}][{kind}]", health_check=health_check, unit="sent")
    write_manifest(d, schema, kind, client, demos, extra, result, runtime, environment, started, partial=bool(limit))
    return result


def write_manifest(d: Path, schema, kind, client, demos, extra, result, runtime, environment, started, partial):
    old = d / "manifest.json"
    prev = __import__("json").loads(old.read_text()) if old.exists() else {}
    status = "partial" if partial or result.completed + len(result.abandoned) < result.total else (
        "complete_with_failures" if result.abandoned else "complete")
    m = {"dataset": schema.name, "kind": kind, "status": status, "annotator_model": client.model,
         "request_extra": client.extra_body, "max_tokens": client.max_tokens, "temperature": client.temperature,
         "seed": client.seed, "annotator_version": ANNOTATOR_VERSION, "prompt_version": PROMPT_VERSION,
         "response_schema_sha256": schema_hash(schema), "demos": [x.sid for x in demos], "n_demos": N_DEMOS,
         "demo_seed": DEMO_SEED,
         "gazetteer": {"min_count": 2, "purity": 0.9, "max_non_entity_ratio": 0.5, "source": "TRAIN gold"
                       + (" without the control sentences" if kind == "control" else "")},
         "merge_priority": ["annotator", "gazetteer"],
         "items": result.total, "completed": result.completed, "abandoned": result.abandoned,
         "output": {"path": str((d / "annotations.jsonl").relative_to(d.parents[2])),
                    "sha256": sha256_file(d / "annotations.jsonl")},
         "runtime": runtime, "environment": environment,
         "started_at": prev.get("started_at") or started,
         "finished_at": datetime.now(timezone.utc).isoformat() if status.startswith("complete") else None,
         **extra}
    atomic_write_json(d / "manifest.json", m)


def is_complete(dataset: str, kind: str) -> bool:
    d = out_dir(kind, get_schema(dataset))
    p = d / "manifest.json"
    if not p.exists():
        return False
    return __import__("json").loads(p.read_text())["status"].startswith("complete")


def silver_records(dataset: str, kind: str) -> List[Dict]:
    return read_jsonl(out_dir(kind, get_schema(dataset)) / "annotations.jsonl")
