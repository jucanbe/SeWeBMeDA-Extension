"""Score every predicted entity of a run with EntityClass and label it against gold.

    python -m experiments.review.score --run results/runs/<run dir> [--no-bert]

Unit of analysis: a predicted span (one occurrence of a predicted entity,
after alignment to tokens). Entities the classifier returned that could not
be aligned to the sentence are kept as rows with label "unaligned"; they are
not part of P/R/F1 and are reported separately.

EntityClass sees: entity text, type, classifier confidence, normalised form
and the sentence as context. It never sees gold. Gold labels and TRAIN strata
are attached afterwards.

Output: <run>/entityclass.jsonl (one row per predicted span) and
<run>/entityclass_manifest.json.
"""
import argparse
import asyncio
import functools
import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from experiments.data.adapters import load_jsonl
from experiments.data.model import normalize_mention, sha256_file, tokenize
from experiments.review.benchmark import BenchmarkKG, CachedBert, build_reviewer, default_config
from experiments.schemas import get_schema
from models.review_defaults import SCORING_VERSION
from pipeline.durable import atomic_write_json

logger = logging.getLogger("review.score")
CRITERIA = ("congruence", "coverage", "constraint", "completeness", "consistency")
LABELS = ("correct", "type_error", "boundary_error", "boundary_type_error", "spurious", "unaligned")


def gold_label(span: Tuple[int, int, str], gold: List[Tuple[int, int, str]]) -> str:
    """Error category of one predicted span against the gold spans of its sentence."""
    s, e, t = span
    if (s, e, t) in gold:
        return "correct"
    if any(gs == s and ge == e for gs, ge, _ in gold):
        return "type_error"
    overlapping = [g for g in gold if g[0] < e and s < g[1]]
    if not overlapping:
        return "spurious"
    return "boundary_error" if any(g[2] == t for g in overlapping) else "boundary_type_error"


def train_stratum(text: str, etype: str, index: Dict[str, Dict]) -> str:
    """A: surface seen in TRAIN with this type; B: seen only with other types; C: unseen as an entity."""
    entry = index.get(normalize_mention(text))
    if not entry or not entry["types"]:
        return "C_unseen"
    return "A_seen_same_type" if etype in entry["types"] else "B_seen_other_type"


def entity_for_span(tokens: List[str], span, entities: List[Dict]) -> Optional[Dict]:
    """The classifier output that produced this span (same matching as llm.ner.align)."""
    s, e, t = span
    target = [x.lower() for x in tokens[s:e]]
    for ent in entities:
        if ent.get("type") != t:
            continue
        text = str(ent.get("text", "")).strip()
        if [x.lower() for x in text.split()] == target or [x.lower() for x in tokenize(text)] == target:
            return ent
    return None


def _confidence(ent: Dict) -> Optional[float]:
    c = ent.get("confidence")
    if isinstance(c, (int, float)) and not isinstance(c, bool):
        return max(0.0, min(1.0, float(c)))
    return None


BERT_ROOT = Path(__file__).resolve().parents[3] / "BERT_models"          # VLLM_Paper/BERT_models


@functools.lru_cache(maxsize=None)
def _bert_checkpoint(name: Optional[str]) -> Optional[Dict]:
    """Path and hashes of the BERT checkpoint used for the Consistency cross-check."""
    if name is None:
        return None
    d = BERT_ROOT / "Entities" / name
    meta = json.loads((d / "training_metadata.json").read_text())
    return {"path": str(d), "weights_sha256": sha256_file(d / "model.safetensors"),
            "config_sha256": sha256_file(d / "config.json"),
            "tokenizer_sha256": sha256_file(d / "tokenizer.json"),
            "trained_on": meta["dataset"], "train_sha256": meta["train_sha256"], "test_used": meta["test_used"],
            "base_model": meta["base_model"], "base_model_revision": meta["base_model_revision"],
            "dev_f1": meta["dev_f1"]}


async def score_run(run_dir: Path, bert_service=None, kg: Optional[BenchmarkKG] = None) -> Path:
    run_dir = Path(run_dir)
    manifest = json.loads((run_dir / "manifest.json").read_text())
    cfg = manifest["config"]
    schema = get_schema(cfg["dataset"])
    kg = kg or BenchmarkKG(schema)
    index = json.loads((kg.kg_directory / "index.json").read_text())
    reviewer = build_reviewer(schema.name, bert_service=bert_service, kg=kg)
    config = default_config()

    out_path = run_dir / "entityclass.jsonl"
    tmp_path = run_dir / ".entityclass.jsonl.tmp"
    rows = 0
    with open(tmp_path, "w", encoding="utf-8") as out:
        for rec in load_jsonl(run_dir / "predictions.jsonl"):
            tokens = rec["tokens"]
            sentence = " ".join(tokens)
            gold = [tuple(g) for g in rec["gold"]]
            items = []
            for span in (tuple(p) for p in rec["pred"]):
                ent = entity_for_span(tokens, span, rec.get("entities", []))
                text = " ".join(tokens[span[0]:span[1]])
                items.append((span, text, span[2], ent or {}, gold_label(span, gold)))
            for u in rec.get("unaligned", []):
                src = next((x for x in rec.get("entities", [])
                            if str(x.get("text", "")).strip() == u["text"] and x.get("type") == u["type"]), {})
                items.append((None, u["text"], u["type"] or "", src, "unaligned"))
            for span, text, etype, ent, label in items:
                conf = _confidence(ent)
                norm = ent.get("normalized_form") or None
                res = await reviewer.evaluate_entity(text, etype, norm, sentence, conf, "llm",
                                                     run_bert_validation=bert_service is not None)
                scores = {c: (res[c].score if res[c] is not None else None) for c in CRITERIA}
                row = {
                    "run": run_dir.name, "dataset": schema.name, "model": cfg["model"]["label"],
                    "condition": cfg.get("condition"), "split": cfg["split"], "sid": rec["sid"],
                    "span": list(span) if span else None, "text": text, "type": etype,
                    "confidence": conf, "has_normalized_form": norm is not None,
                    "label": label, "correct": label == "correct",
                    "stratum": train_stratum(text, etype, index),
                    "scores": scores, "overall_W0": res["overall_score"], "decision_W0": res["review_status"],
                    "recommendation_W0": res["recommendation"],
                    "type_valid": res["constraint"].type_valid, "violations": res["constraint"].violations,
                    "kg_nearest": res["congruence"].nearest_entity if res["congruence"] else None,
                    "kg_similar_count": res["coverage"].similar_entities_count if res["coverage"] else None,
                    "kg_is_novel": res["coverage"].is_novel if res["coverage"] else None,
                    "missing_fields": res["completeness"].missing_fields,
                    "bert_status": res["consistency"].bert_status,
                    "bert_agreement": res["consistency"].bert_agreement,
                    "bert_alternate": res["consistency"].alternate_types,
                }
                if bert_service is not None:
                    # BERT's own prediction for the entity text (memoised; the call the reviewer made)
                    ents, _ = bert_service.classify(text, reviewer.bert_model)
                    top = max(ents, key=lambda e: e["confidence"]) if ents else None
                    row.update(bert_type=top["type"] if top else None,
                               bert_p=float(top["confidence"]) if top else None)
                    # the same entity without the BERT cross-check (only Consistency changes)
                    nb = await reviewer._evaluate_consistency(text, etype, "llm", conf, False, False,
                                                              config["settings"])
                    s2 = dict(scores, consistency=nb.score)
                    overall = reviewer._calculate_overall_score(s2, config["weights"])
                    status, _ = reviewer._determine_status_and_recommendation(
                        overall, res["congruence"], res["constraint"], nb, config["thresholds"])
                    row.update(consistency_no_bert=nb.score, overall_W0_no_bert=overall, decision_W0_no_bert=status)
                out.write(json.dumps(row, ensure_ascii=False) + "\n")
                rows += 1
    tmp_path.replace(out_path)
    atomic_write_json(run_dir / "entityclass_manifest.json", {
        "scoring_version": SCORING_VERSION, "config": config, "bert": bert_service is not None,
        "bert_model": reviewer.bert_model, "bert_checkpoint": _bert_checkpoint(reviewer.bert_model),
        "kg": str(kg.kg_directory),
        "kg_sha256": sha256_file(kg.kg_directory / "kg.nt"), "rows": rows,
        "predictions_sha256": sha256_file(run_dir / "predictions.jsonl"),
        "created_at": datetime.now(timezone.utc).isoformat()})
    return out_path


def is_scored(run_dir: Path) -> bool:
    """Scores exist and belong to the current predictions (resume: never rescore)."""
    m = Path(run_dir) / "entityclass_manifest.json"
    if not m.exists() or not (Path(run_dir) / "entityclass.jsonl").exists():
        return False
    return json.loads(m.read_text()).get("predictions_sha256") == sha256_file(Path(run_dir) / "predictions.jsonl")


def best_device() -> str:
    import torch
    if torch.cuda.is_available():
        return "cuda"
    if getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def score_runs(run_dirs: List[Path], use_bert: bool = True, force: bool = False):
    from services.bert_ner import BERTNERService
    todo = [Path(d) for d in run_dirs if force or not is_scored(Path(d))]
    print(f"[ENTITYCLASS] {len(run_dirs) - len(todo)} runs already scored, {len(todo)} to score")
    if not todo:
        return
    bert = CachedBert(BERTNERService(models_dir=str(BERT_ROOT), device=best_device())) if use_bert else None
    kgs: Dict[str, BenchmarkKG] = {}
    for n, d in enumerate(todo, 1):
        ds = json.loads((Path(d) / "manifest.json").read_text())["config"]["dataset"]
        if ds not in kgs:
            kgs[ds] = BenchmarkKG(get_schema(ds))
        asyncio.run(score_run(Path(d), bert, kgs[ds]))
        print(f"[ENTITYCLASS] {n}/{len(todo)} scored {Path(d).name}", flush=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING, format="%(asctime)s %(levelname)s %(message)s")
    logger.setLevel(logging.INFO)
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--run", nargs="+", required=True)
    p.add_argument("--no-bert", action="store_true")
    a = p.parse_args()
    score_runs([Path(r) for r in a.run], use_bert=not a.no_bert)
