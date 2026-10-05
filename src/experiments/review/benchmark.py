"""EntityClass reviewer configured for the benchmark datasets.

The reviewer itself (services/entity_reviewer.EntityReviewService) is used
unchanged. This module supplies what the application normally provides:

  * the dataset's own entity types instead of the 14 clinical types;
  * the TRAIN-derived classification KG (KnowledgeGraph/experiments/<ds>/development_v1)
    behind the application's KG matching semantics;
  * the dataset-specific BERT model for the Consistency cross-check;
  * a fixed configuration (default weights, thresholds, settings) instead of
    the application's database row.

`BenchmarkKG.find_matches` returns the same similarity scores as
KnowledgeGraphService.find_matches (difflib ratio / containment); candidates
that cannot reach `min_score` are pruned with length bounds first, results are
memoised per (text, type), and ties are ordered by URI for determinism.
"""
import json
from difflib import SequenceMatcher
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from experiments.bert_validator import select_benchmark_bert, type_normalizer
from experiments.kg.build import KG_ROOT
from experiments.schemas import DatasetSchema, get_schema
from models.entities import KGMatch
from models.review_defaults import ENTITY_SETTINGS, ENTITY_WEIGHTS, THRESHOLDS
from services.entity_reviewer import EntityReviewService
from services.knowledge_graph import KnowledgeGraphService

# Schema types to which the application's type-specific Constraint heuristics
# (written for its "disease", "finding" and "substance" types) apply.
CONSTRAINT_TYPE_MAP = {
    "Disease": "disease", "DiseaseOrPhenotypicFeature": "disease",
    "Chemical": "substance", "ChemicalEntity": "substance",
    "Finding": "finding",
}


def default_config() -> Dict:
    return {"weights": dict(ENTITY_WEIGHTS), "thresholds": dict(THRESHOLDS), "settings": dict(ENTITY_SETTINGS)}


class BenchmarkKG(KnowledgeGraphService):
    def __init__(self, schema: DatasetSchema, kg_dir: Optional[Path] = None):
        from rdflib import Graph
        self.kg_directory = Path(kg_dir) if kg_dir else KG_ROOT / schema.folder / "development_v1"
        self.type_map = {t: [t] for t in schema.types}
        self.graph = Graph()
        self.graph.parse(str(self.kg_directory / "kg.nt"), format="nt")
        self._entities_cache = {}
        self._loaded_files = [str(self.kg_directory / "kg.nt")]
        self._build_entity_cache()
        # (norm_label, label, uri, index of label in entity) per KG class, sorted by label length
        self._by_type: Dict[str, List[Tuple[int, str, str, str]]] = {}
        for uri in sorted(self._entities_cache):
            e = self._entities_cache[uri]
            classes = {self._kg_type_local(t) for t in e["types"]}
            for label, norm in zip(e["labels"], e["normalized_labels"]):
                for c in classes:
                    self._by_type.setdefault(c, []).append((len(norm), norm, label, uri))
        self._memo: Dict[Tuple[str, Optional[str], int, float], List[KGMatch]] = {}

    def find_matches(self, entity_text: str, max_matches: int = 5, min_score: float = None,
                     entity_type: Optional[str] = None) -> List[KGMatch]:
        if min_score is None:
            min_score = self.SIMILAR_MATCH_THRESHOLD
        key = (entity_text, entity_type, max_matches, min_score)
        if key in self._memo:
            return self._memo[key]
        query = self._normalize_text(entity_text)
        classes = self.type_map.get(entity_type) if entity_type is not None else None
        if not classes:                      # same as the parent: unknown type = no type filter
            classes = list(self._by_type)
        lq = len(query)
        best: Dict[str, Tuple[float, str]] = {}
        for c in classes:
            for ll, norm, label, uri in self._by_type.get(c, ()):
                current = best.get(uri, (0.0, ""))[0]
                if current >= 1.0:
                    continue
                if query == norm:
                    best[uri] = (1.0, label)
                    continue
                # upper bound of both difflib ratio and containment score
                bound = 2.0 * min(lq, ll) / (lq + ll) if (lq + ll) else 0.0
                if bound < min_score or bound <= current:
                    continue
                score = SequenceMatcher(None, query, norm).ratio()
                if query in norm or norm in query:
                    score = max(score, min(lq, ll) / max(lq, ll))
                if score > current:
                    best[uri] = (score, label)
        matches = [KGMatch(kg_uri=uri, kg_label=label,
                           kg_type=self._kg_type_local(self._entities_cache[uri]["types"][0])
                           if self._entities_cache[uri]["types"] else None, similarity_score=score)
                   for uri, (score, label) in best.items() if score >= min_score]
        matches.sort(key=lambda m: (-m.similarity_score, m.kg_uri))
        self._memo[key] = matches[:max_matches]
        return self._memo[key]

    async def find_matches_async(self, entity_text: str, max_matches: int = 5, min_score: float = None,
                                 entity_type: Optional[str] = None, kg_backend: str = "internal") -> List[KGMatch]:
        return self.find_matches(entity_text, max_matches=max_matches, min_score=min_score, entity_type=entity_type)


class CachedBert:
    """Memoises BERT inference per entity text (the reviewer classifies the entity text alone)."""

    def __init__(self, service):
        self.service = service
        self._memo = {}

    def get_available_models(self, model_type=None):
        return self.service.get_available_models(model_type)

    def classify(self, text, model_name=None):
        key = (text, model_name)
        if key not in self._memo:
            self._memo[key] = self.service.classify(text, model_name)
        return self._memo[key]


def build_reviewer(dataset: str, bert_service=None, kg: Optional[BenchmarkKG] = None,
                   config: Optional[Dict] = None) -> EntityReviewService:
    """The real reviewer on a benchmark schema. bert_service=None gives the no-BERT reviewer."""
    schema = get_schema(dataset)
    kg = kg or BenchmarkKG(schema)
    bert_model = select_benchmark_bert(schema.name, bert_service) if bert_service is not None else None
    return EntityReviewService(
        kg_service=kg, bert_service=bert_service, bert_model=bert_model,
        type_normalizer=type_normalizer(schema), numeric_types=frozenset(),
        constraint_type_map=CONSTRAINT_TYPE_MAP, config=config or default_config())
