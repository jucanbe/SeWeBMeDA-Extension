"""Build the downstream (TRAIN-derived) experiment KG and its lookup index.

Output: VLLM_Paper/KnowledgeGraph/experiments/<dataset>/<version>/
    kg.nt           RDF graph (N-Triples): one node per normalised surface form with type counts,
                    O-count, provenance
    index.json      label index used by KG-RAG retrieval and the validator
    manifest.json   input fingerprints, allowed splits, protocol, counts

Protocols:
    development   splits = {train}          (all tuning happens against DEV)
    final_refit   splits = {train, dev}     (rebuilt once, after freezing configs)
TEST is never accepted.
"""
import argparse
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List

from rdflib import Graph, Literal, Namespace, RDF, RDFS, URIRef
from rdflib.namespace import SKOS, XSD

from experiments.data.adapters import BIOCsvAdapter
from experiments.data.model import Sentence, normalize_mention, sha256_file
from experiments.schemas import get_schema

KG_ROOT = Path(__file__).resolve().parents[3] / "KnowledgeGraph" / "experiments"   # VLLM_Paper/KnowledgeGraph
EC = Namespace("http://example.org/entityclass/experiments#")
MAX_NGRAM = 6

PROTOCOLS = {"development": ("train",), "final_refit": ("train", "dev")}


class LeakageError(RuntimeError):
    pass


def check_splits(splits: Iterable[str], protocol: str):
    splits = tuple(sorted(set(splits)))
    if "test" in splits:
        raise LeakageError("TEST data may never be used to build a KG")
    allowed = tuple(sorted(PROTOCOLS[protocol]))
    if splits != allowed:
        raise LeakageError(f"protocol '{protocol}' requires splits {allowed}, got {splits}")


def build_index(sentences: List[Sentence], origin: str) -> Dict[str, Dict]:
    """norm label -> {label, types{type: count}, o, origin}."""
    index: Dict[str, Dict] = {}
    for s in sentences:
        for start, end, etype in s.spans:
            if end - start > MAX_NGRAM * 3:
                continue
            label = " ".join(s.tokens[start:end])
            key = normalize_mention(label)
            entry = index.setdefault(key, {"label": label, "types": Counter(), "o": 0, "origin": origin})
            entry["types"][etype] += 1
    # O-count: occurrences of an indexed string that are not an entity of exactly that extent
    for s in sentences:
        gold_extents = {(a, b) for a, b, _ in s.spans}
        norm_tokens = [normalize_mention(t) for t in s.tokens]
        for i in range(len(s.tokens)):
            for n in range(1, MAX_NGRAM + 1):
                j = i + n
                if j > len(s.tokens):
                    break
                key = " ".join(norm_tokens[i:j])
                if key in index and (i, j) not in gold_extents:
                    index[key]["o"] += 1
    for entry in index.values():
        entry["types"] = dict(entry["types"])
    return index


def to_graph(index: Dict[str, Dict], schema, provenance: Dict) -> Graph:
    g = Graph()
    g.bind("ec", EC)
    g.bind("skos", SKOS)
    for t, definition in schema.types.items():
        g.add((EC[t], RDF.type, RDFS.Class))
        g.add((EC[t], RDFS.label, Literal(t)))
        g.add((EC[t], SKOS.definition, Literal(definition)))
    for i, (key, e) in enumerate(sorted(index.items())):
        node = URIRef(f"{EC}{schema.folder}/e{i}")
        g.add((node, RDFS.label, Literal(e["label"])))
        g.add((node, EC.normalizedLabel, Literal(key)))
        g.add((node, EC.nonEntityCount, Literal(e["o"], datatype=XSD.integer)))
        g.add((node, EC.origin, Literal(e["origin"])))
        g.add((node, EC.sourceDataset, Literal(schema.name)))
        g.add((node, EC.sourceSplits, Literal(",".join(provenance["splits"]))))
        for t, n in e["types"].items():
            g.add((node, RDF.type, EC[t]))
            ann = URIRef(f"{node}/{t}")
            g.add((node, EC.annotatedAs, ann))
            g.add((ann, EC.entityType, EC[t]))
            g.add((ann, EC.frequency, Literal(n, datatype=XSD.integer)))
    return g


def build(dataset: str, protocol: str = "development", version: str = "v1", out_root: Path = KG_ROOT,
          splits: Iterable[str] = None) -> Path:
    schema = get_schema(dataset)
    splits = tuple(splits) if splits else PROTOCOLS[protocol]
    check_splits(splits, protocol)
    adapter = BIOCsvAdapter(schema)
    sentences = [s for split in splits for s in adapter.load(split)]
    index = build_index(sentences, origin="original")
    out = Path(out_root) / schema.folder / f"{protocol}_{version}"
    out.mkdir(parents=True, exist_ok=True)
    provenance = {"splits": list(splits)}
    to_graph(index, schema, provenance).serialize(destination=str(out / "kg.nt"), format="nt", encoding="utf-8")
    (out / "index.json").write_text(json.dumps(index, ensure_ascii=False))
    manifest = {
        "dataset": schema.name, "protocol": protocol, "version": version, "splits": list(splits),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "inputs": {f"{schema.folder}/{s}.csv": sha256_file(adapter.path(s)) for s in splits},
        "entries": len(index), "mentions": sum(sum(e["types"].values()) for e in index.values()),
        "max_ngram": MAX_NGRAM, "normalisation": "lower-case, whitespace-collapsed, unicode dashes -> '-'",
        "kg_sha256": sha256_file(out / "kg.nt"), "index_sha256": sha256_file(out / "index.json"),
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2))
    return out


def add_synthetic_graph(kg_dir: Path, synthetic_sentences: List[Sentence], annotator: str) -> Path:
    """Write silver S-train knowledge as a separate graph next to an existing KG (E5s only)."""
    for s in synthetic_sentences:
        if s.track != "S-train":
            raise LeakageError("only S-train sentences may enter an experiment KG")
    index = build_index(synthetic_sentences, origin=f"synthetic-silver:{annotator}")
    (Path(kg_dir) / "index_synthetic.json").write_text(json.dumps(index, ensure_ascii=False))
    return Path(kg_dir) / "index_synthetic.json"


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--dataset", required=True)
    p.add_argument("--protocol", choices=list(PROTOCOLS), default="development")
    p.add_argument("--version", default="v1")
    a = p.parse_args()
    print(build(a.dataset, a.protocol, a.version))
