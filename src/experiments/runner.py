"""Experiment runner: reproducible, resumable at sentence level, TEST-protected.

A config (JSON) contains:
    name, dataset, split (dev|test), subset {n, seed}, condition,
    model {key, id, revision, label, base_url, extra_body}, runtime {...vLLM launch settings...},
    fewshot {strategy, k}, rag {enabled, max_facts, fuzzy}, validator {enabled, ...},
    synthetic {track: S-full, dir}, temperature, max_tokens, seed, frozen (required for TEST).

The run directory is results/runs/<name>__<run_id>/ where run_id hashes the
resolved config and all input fingerprints. Files:
    predictions.jsonl  one VALID result per sentence (fsync'ed); the only completion record
    failures.jsonl     every failed attempt; a sentence is abandoned after 5 failed attempts
    metrics.json       written when the run is complete
    manifest.json      atomic; status running | partial | complete | complete_with_failures
"""
import hashlib
import json
import logging
import platform
import sys
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Dict, List, Optional

from experiments.data.adapters import BIOCsvAdapter, SFullSilverAdapter
from experiments.data.model import Sentence, normalize_mention, sha256_file
from experiments.eval.metrics import evaluate
from experiments.fewshot.retrieve import DemoPool, Embedder, select_demos
from experiments.kg.build import KG_ROOT, PROTOCOLS
from experiments.kg.retrieve import KGIndex, ValidatorConfig, retrieve_facts, validate
from experiments.llm.ner import (PROMPT_VERSION, ChatClient, align, build_messages, parse_response,
                                 prompt_hash, response_schema, schema_hash)
from experiments.schemas import RESULTS_DIR, SYNTHETIC_DIR, get_schema
from experiments.subsets import get_subset, load_subset
from pipeline.durable import atomic_write_json, read_jsonl
from pipeline.workqueue import MAX_ATTEMPTS, Outcome, QueueResult, failure_counts, run_resumable

logger = logging.getLogger("runner")
RUNS_DIR = RESULTS_DIR / "runs"
FROZEN_DIR = RESULTS_DIR / "frozen"


class ProtocolError(RuntimeError):
    pass


DEFAULTS = {
    "split": "dev", "subset": {"n": 200, "seed": 20261001}, "protocol": "development",
    "fewshot": {"strategy": "none", "k": 0}, "rag": {"enabled": False, "max_facts": 10, "fuzzy": True},
    "validator": {"enabled": False}, "synthetic": {"track": "S-full"},
    "temperature": 0.0, "max_tokens": 2048, "seed": 0, "frozen": False,
}


def resolve(config: Dict) -> Dict:
    cfg = json.loads(json.dumps(DEFAULTS))
    for k, v in config.items():
        if isinstance(v, dict) and isinstance(cfg.get(k), dict):
            cfg[k].update(v)
        else:
            cfg[k] = v
    return cfg


def frozen_hash(cfg: Dict) -> str:
    """Hash of everything that defines a condition except the split/subset it is evaluated on
    (and the local endpoint URL, which is not part of the method)."""
    keep = {k: v for k, v in cfg.items() if k not in ("split", "subset", "frozen", "protocol")}
    keep = json.loads(json.dumps(keep))
    keep.get("model", {}).pop("base_url", None)
    return hashlib.sha256(json.dumps(keep, sort_keys=True).encode()).hexdigest()[:16]


def check_protocol(cfg: Dict):
    if cfg["split"] not in ("dev", "test"):
        raise ProtocolError("evaluation split must be dev or test")
    if cfg["protocol"] != "development":
        raise ProtocolError("only the development protocol is used (TRAIN resources, no final refit)")
    if cfg["split"] == "test":
        if not cfg.get("frozen"):
            raise ProtocolError("TEST can only be evaluated with a frozen configuration (frozen: true)")
        registry = FROZEN_DIR / f"{frozen_hash(cfg)}.json"
        if not registry.exists():
            raise ProtocolError(f"configuration is not registered as frozen ({registry.name}); run the freeze stage")
    if cfg["fewshot"]["strategy"] in ("synthetic", "mixed") and cfg["synthetic"]["track"] != "S-full":
        raise ProtocolError("this package evaluates the original synthetic corpora (S-full) only")


def resource_splits(cfg: Dict) -> tuple:
    return PROTOCOLS[cfg["protocol"]]


def kg_dir(cfg: Dict, schema) -> Path:
    return KG_ROOT / schema.folder / f"{cfg['protocol']}_{cfg.get('kg_version', 'v1')}"


def synthetic_dir(cfg: Dict, schema) -> Path:
    return Path(cfg["synthetic"].get("dir") or SYNTHETIC_DIR / "s_full_silver" / schema.folder)


def silver_control_path(schema) -> Path:
    return SYNTHETIC_DIR / "silver_control" / schema.folder / "annotations.jsonl"


def needs_embeddings(cfg: Dict) -> bool:
    return cfg["fewshot"]["strategy"] in ("original", "synthetic", "mixed", "silver_original")


class Experiment:
    def __init__(self, config: Dict):
        self.cfg = resolve(config)
        check_protocol(self.cfg)
        self.schema = get_schema(self.cfg["dataset"])
        self.adapter = BIOCsvAdapter(self.schema)
        n = self.cfg["subset"]["n"]
        self.subset_path = get_subset(self.schema.name, self.cfg["split"], n, self.cfg["subset"]["seed"])
        self.inputs = self._fingerprints()
        rid = hashlib.sha256(json.dumps({"cfg": self.cfg, "inputs": self.inputs, "prompt": PROMPT_VERSION},
                                        sort_keys=True).encode()).hexdigest()[:12]
        self.run_id = rid
        self.dir = RUNS_DIR / f"{self.cfg['name']}__{rid}"

    # ------------------------------------------------------------------
    def _fingerprints(self) -> Dict:
        fp = {"eval_split": sha256_file(self.adapter.path(self.cfg["split"])),
              "subset": sha256_file(self.subset_path)}
        for s in resource_splits(self.cfg):
            fp[f"resource_{s}"] = sha256_file(self.adapter.path(s))
        if self.cfg["rag"]["enabled"] or self.cfg["validator"]["enabled"]:
            fp["kg_index"] = sha256_file(kg_dir(self.cfg, self.schema) / "index.json")
        if self.cfg["fewshot"]["strategy"] in ("synthetic", "mixed"):
            fp["synthetic_annotations"] = sha256_file(synthetic_dir(self.cfg, self.schema) / "annotations.jsonl")
        if self.cfg["fewshot"]["strategy"] == "silver_original":
            fp["silver_original"] = sha256_file(silver_control_path(self.schema))
        return fp

    def subset_ids(self) -> List[str]:
        return load_subset(self.subset_path)

    def query_texts(self) -> List[str]:
        sents = {s.sid: s for s in self.adapter.load(self.cfg["split"])}
        return [sents[i].text for i in self.subset_ids()]

    def pools(self, embedder) -> Dict[str, DemoPool]:
        strat = self.cfg["fewshot"]["strategy"]
        pools = {}
        eval_texts = {" ".join(s.text.split()).lower() for s in self.adapter.load(self.cfg["split"])}
        if strat in ("original", "mixed", "random_original"):
            original = [s for sp in resource_splits(self.cfg) for s in self.adapter.load(sp)]
            pools["original"] = DemoPool("original", original, embedder, exclude_texts=eval_texts)
        if strat in ("synthetic", "mixed"):
            syn = SFullSilverAdapter(self.schema, synthetic_dir(self.cfg, self.schema)).load()
            pools["synthetic"] = DemoPool("synthetic", syn, embedder, exclude_texts=eval_texts)
        if strat == "silver_original":
            recs = read_jsonl(silver_control_path(self.schema))
            sil = [Sentence(self.schema.name, "train", r["sid"], r["tokens"], [tuple(x) for x in r["spans"]],
                            label_source=r["label_source"]) for r in recs]
            pools["silver_original"] = DemoPool("silver_original", sil, embedder, exclude_texts=eval_texts)
        return pools

    # ------------------------------------------------------------------
    def status(self) -> Dict:
        """Derived from the outputs only."""
        ids = set(self.subset_ids())
        done = {r["sid"] for r in read_jsonl(self.dir / "predictions.jsonl")} & ids
        att = failure_counts(self.dir / "failures.jsonl")
        abandoned = {k for k in ids - done if att[k] >= MAX_ATTEMPTS}
        remaining = ids - done - abandoned
        state = "not_started" if not done and not abandoned else (
            "partial" if remaining else ("complete_with_failures" if abandoned else "complete"))
        return {"total": len(ids), "completed": len(done), "abandoned": sorted(abandoned),
                "remaining": len(remaining), "state": state}

    def run(self, client: ChatClient, concurrency: int, embedder: Optional[Embedder] = None,
            health_check: Optional[Callable[[], bool]] = None, limit: Optional[int] = None,
            runtime: Optional[Dict] = None, environment: Optional[Dict] = None, tag: str = "") -> Dict:
        cfg = self.cfg
        self.dir.mkdir(parents=True, exist_ok=True)
        ids = self.subset_ids()
        if limit:
            ids = ids[:limit]
        sentences = {s.sid: s for s in self.adapter.load(cfg["split"])}
        pools = self.pools(embedder) if cfg["fewshot"]["strategy"] != "none" else {}
        if needs_embeddings(cfg):
            for p in pools.values():          # load every embedding before the worker threads start
                _ = p.matrix
            embedder.embed([sentences[i].text for i in ids], "query")
        kg = KGIndex.load(kg_dir(cfg, self.schema)) if (cfg["rag"]["enabled"] or cfg["validator"]["enabled"]) else None
        vcfg = ValidatorConfig(**{k: v for k, v in cfg["validator"].items() if k != "enabled"})
        schema_json = response_schema(self.schema)
        started = self._read_manifest().get("started_at") or datetime.now(timezone.utc).isoformat()
        self._write_manifest("running", runtime, environment, started_at=started)

        def process(sid: str) -> Outcome:
            s = sentences[sid]
            demos = select_demos(s, pools, cfg["fewshot"]["strategy"], cfg["fewshot"]["k"], embedder,
                                 seed=cfg["seed"]) if pools else []
            facts = retrieve_facts(s.tokens, kg, cfg["rag"]["max_facts"], use_fuzzy=cfg["rag"]["fuzzy"]) \
                if cfg["rag"]["enabled"] else []
            demo_facts = [[f.render() for f in retrieve_facts(d.tokens, kg, cfg["rag"]["max_facts"],
                                                               use_fuzzy=cfg["rag"]["fuzzy"])] for d in demos] \
                if cfg["rag"]["enabled"] and demos else None
            messages = build_messages(self.schema, s, demos, [f.render() for f in facts] or None, demo_facts)
            res = client.chat(messages, schema_json)
            detail = {"finish_reason": res.finish_reason, "usage": res.usage, "latency_s": round(res.latency_s, 3)}
            if res.error:
                return Outcome(False, reason=res.error, error_kind=res.error_kind, detail=detail)
            ents, perr = parse_response(res.content)
            if perr or res.finish_reason == "length":
                return Outcome(False, reason=f"unusable response: {perr or 'truncated (finish_reason=length)'}",
                               error_kind="response", detail=dict(detail, raw=res.content[:2000]))
            spans, unaligned = align(s.tokens, ents, self.schema.type_names)
            actions = []
            if cfg["validator"]["enabled"]:
                spans, actions = validate(s.tokens, spans, kg, vcfg)
            return Outcome(True, record={
                "sid": s.sid, "tokens": s.tokens, "gold": [list(x) for x in s.spans], "pred": [list(x) for x in spans],
                "raw_response": res.content, "reasoning_chars": len(res.reasoning), "finish_reason": res.finish_reason,
                "unaligned": unaligned, "entities": ents, "demos": [d.sid for d in demos],
                "kg_facts": [asdict(f) | {"rendered": f.render()} for f in facts],
                "validator_actions": actions, "prompt_hash": prompt_hash(messages),
                "prompt_chars": sum(len(x["content"]) for x in messages), "usage": res.usage,
                "latency_s": round(res.latency_s, 3), "served_model": res.model,
                "completed_at": datetime.now(timezone.utc).isoformat()})

        result: QueueResult = run_resumable(
            ids, key=lambda x: x, process=process, out_path=self.dir / "predictions.jsonl",
            fail_path=self.dir / "failures.jsonl", concurrency=concurrency, tag=tag or f"[{self.dir.name}]",
            health_check=health_check)
        st = self.status()
        if limit:
            self._write_manifest("partial", runtime, environment, started_at=started)
            return st
        if st["state"] in ("complete", "complete_with_failures"):
            self.evaluate()
        self._write_manifest(st["state"], runtime, environment, started_at=started,
                             finished_at=datetime.now(timezone.utc).isoformat()
                             if st["state"].startswith("complete") else None,
                             extra={"abandoned_sentences": st["abandoned"]})
        return st

    def train_lexicon(self) -> set:
        return {normalize_mention(t) for sp in resource_splits(self.cfg) for s in self.adapter.load(sp)
                for t, _ in s.mentions()}

    def records_for_evaluation(self) -> List[Dict]:
        """Completed records plus abandoned sentences as empty predictions (counted, never dropped)."""
        recs = {r["sid"]: r for r in read_jsonl(self.dir / "predictions.jsonl")}
        sentences = {s.sid: s for s in self.adapter.load(self.cfg["split"])}
        out = []
        for sid in self.subset_ids():
            if sid in recs:
                out.append(recs[sid])
            else:
                s = sentences[sid]
                out.append({"sid": sid, "tokens": s.tokens, "gold": [list(x) for x in s.spans], "pred": [],
                            "abandoned": True})
        return out

    def evaluate(self) -> Dict:
        recs = self.records_for_evaluation()
        metrics = evaluate(recs, self.schema.type_names, train_lexicon=self.train_lexicon())
        done = [r for r in recs if not r.get("abandoned")]
        lat = [r["latency_s"] for r in done if r.get("latency_s")]
        metrics["run"] = {
            "n_sentences": len(recs), "n_abandoned_as_empty": sum(1 for r in recs if r.get("abandoned")),
            "unaligned": sum(len(r.get("unaligned", [])) for r in done),
            "mean_latency_s": sum(lat) / len(lat) if lat else None,
            "prompt_tokens": sum((r.get("usage") or {}).get("prompt_tokens", 0) for r in done),
            "completion_tokens": sum((r.get("usage") or {}).get("completion_tokens", 0) for r in done),
            "failed_attempts": sum(failure_counts(self.dir / "failures.jsonl").values()),
            "validator_actions": sum(len(r.get("validator_actions", [])) for r in done),
        }
        atomic_write_json(self.dir / "metrics.json", metrics)
        return metrics

    def _read_manifest(self) -> Dict:
        p = self.dir / "manifest.json"
        return json.loads(p.read_text()) if p.exists() else {}

    def _write_manifest(self, status: str, runtime: Optional[Dict] = None, environment: Optional[Dict] = None,
                        started_at: Optional[str] = None, finished_at: Optional[str] = None,
                        extra: Optional[Dict] = None):
        old = self._read_manifest()
        man = {
            "run_id": self.run_id, "name": self.cfg["name"], "status": status, "config": self.cfg,
            "frozen_hash": frozen_hash(self.cfg), "prompt_version": PROMPT_VERSION,
            "response_schema_sha256": schema_hash(self.schema),
            "inputs": self.inputs, "subset_manifest": self.subset_path.name,
            "resource_splits": list(resource_splits(self.cfg)),
            "runtime": runtime or old.get("runtime"),
            "environment": environment or old.get("environment") or
            {"python": sys.version.split()[0], "platform": platform.platform()},
            "started_at": started_at or old.get("started_at"), "finished_at": finished_at,
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }
        if extra:
            man.update(extra)
        atomic_write_json(self.dir / "manifest.json", man)


def derived_config(source_cfg: Dict, name: str, validator: Dict) -> Dict:
    """Config of a validator-derived condition (E4 from E0, E6 from E5); used by derive and by freeze."""
    cfg = json.loads(json.dumps(resolve(source_cfg)))
    cfg["name"] = name
    cfg["validator"] = {"enabled": True, **validator}
    cfg["condition"] = {"E0": "E4", "E5": "E6"}.get(cfg.get("condition"), cfg.get("condition"))
    return cfg


def derive_validator(source_dir: Path, name: str, validator: Dict) -> Path:
    """Apply the post-hoc validator to an existing complete run's predictions (no LLM calls)."""
    source_dir = Path(source_dir)
    src_man = json.loads((source_dir / "manifest.json").read_text())
    if not src_man["status"].startswith("complete"):
        raise ProtocolError("source run is not complete")
    exp = Experiment(derived_config(src_man["config"], name, validator))
    exp.dir.mkdir(parents=True, exist_ok=True)
    kg = KGIndex.load(kg_dir(exp.cfg, exp.schema))
    vcfg = ValidatorConfig(**validator)
    out = []
    for r in read_jsonl(source_dir / "predictions.jsonl"):
        spans, actions = validate(r["tokens"], [tuple(x) for x in r["pred"]], kg, vcfg)
        out.append(dict(r, pred=[list(x) for x in spans], validator_actions=actions, derived_from=src_man["run_id"]))
    tmp = exp.dir / ".predictions.jsonl.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        for r in out:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    tmp.replace(exp.dir / "predictions.jsonl")
    for name_ in ("failures.jsonl",):
        if (source_dir / name_).exists():
            (exp.dir / name_).write_bytes((source_dir / name_).read_bytes())
    exp.evaluate()
    exp._write_manifest(src_man["status"], src_man.get("runtime"), src_man.get("environment"),
                        started_at=src_man.get("started_at"), finished_at=src_man.get("finished_at"),
                        extra={"derived_from": {"run_id": src_man["run_id"], "dir": source_dir.name}})
    return exp.dir


def freeze(config: Dict, note: str = "") -> Path:
    cfg = resolve(config)
    FROZEN_DIR.mkdir(parents=True, exist_ok=True)
    h = frozen_hash(cfg)
    path = FROZEN_DIR / f"{h}.json"
    if not path.exists():
        atomic_write_json(path, {"frozen_hash": h, "config": cfg, "note": note,
                                 "frozen_at": datetime.now(timezone.utc).isoformat()})
    return path
