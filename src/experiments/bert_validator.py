"""Dataset-specific BERT models for the benchmark EntityClass Consistency check.

The benchmark reviewer uses the BERT model trained on the same dataset's TRAIN
split (train_benchmark_bert_models.py): BC5CDR -> bc5cdr_biomedbert, etc. The
application keeps its own automatic selection over the project entity types;
nothing here changes it.
"""
import json
from pathlib import Path
from typing import Callable, Dict, Optional

from experiments.schemas import DatasetSchema, get_schema

BENCHMARK_BERT_MODELS: Dict[str, str] = {
    "BC5CDR": "bc5cdr_biomedbert",
    "BioRED": "biored_biomedbert",
    "MedMentions": "medmentions_biomedbert",
}


class IncompatibleBertModel(ValueError):
    pass


def type_normalizer(schema: DatasetSchema) -> Callable[[str], Optional[str]]:
    """Case-insensitive mapping onto the dataset's own type names (None if unknown)."""
    lookup = {t.lower(): t for t in schema.types}

    def normalize(label: Optional[str]) -> Optional[str]:
        if not label:
            return None
        return lookup.get(label.strip().lower())
    return normalize


def select_benchmark_bert(dataset: str, bert_service) -> str:
    """Name of the dataset's BERT model, after checking it really belongs to that dataset.

    Raises IncompatibleBertModel when the model is missing, was trained on another
    dataset, used TEST, or predicts labels outside the dataset schema.
    """
    schema = get_schema(dataset)
    name = BENCHMARK_BERT_MODELS[schema.name]
    info = next((m for m in bert_service.get_available_models("entity") if m["name"] == name), None)
    if info is None:
        raise IncompatibleBertModel(f"{schema.name}: BERT model '{name}' not found")
    meta_path = Path(info["path"]) / "training_metadata.json"
    if not meta_path.exists():
        raise IncompatibleBertModel(f"{name}: training_metadata.json missing")
    meta = json.loads(meta_path.read_text())
    if meta.get("dataset") != schema.name:
        raise IncompatibleBertModel(f"{name} was trained on {meta.get('dataset')}, not {schema.name}")
    if meta.get("test_used") is not False:
        raise IncompatibleBertModel(f"{name}: training metadata does not certify test_used=false")
    types = {label[2:] for label in info.get("labels") or [] if label[:2] in ("B-", "I-")}
    outside = types - set(schema.types)
    if not types or outside:
        raise IncompatibleBertModel(f"{name}: labels outside the {schema.name} schema: {sorted(outside)}")
    return name
