"""Readers for the benchmark BIO files and the synthetic corpora."""
import csv
import json
import logging
from collections import OrderedDict
from pathlib import Path
from typing import Dict, Iterable, List, Optional

from experiments.data.model import (
    Sentence, bio_to_spans, tokenize, ORIGINAL, SYNTHETIC, S_FULL,
)
from experiments.schemas import DatasetSchema, DATASETS_DIR, SYNTHETIC_FULL_DIR

logger = logging.getLogger(__name__)

SPLITS = ("train", "dev", "test")


class BIOCsvAdapter:
    """Token-per-row CSV with columns words, sentence_id, labels."""

    def __init__(self, schema: DatasetSchema, root: Path = DATASETS_DIR):
        self.schema = schema
        self.root = Path(root) / schema.folder
        self.stats: Dict[str, Dict] = {}

    def path(self, split: str) -> Path:
        if split not in SPLITS:
            raise ValueError(f"Unknown split '{split}'")
        return self.root / f"{split}.csv"

    def load(self, split: str) -> List[Sentence]:
        rows: "OrderedDict[str, list]" = OrderedDict()
        with open(self.path(split), newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            missing = {"words", "sentence_id", "labels"} - set(reader.fieldnames or [])
            if missing:
                raise ValueError(f"{self.path(split)} lacks columns {missing}")
            for row in reader:
                rows.setdefault(row["sentence_id"], []).append(row)

        sentences, repaired, unknown = [], 0, set()
        for sid, group in rows.items():
            tokens = [r["words"] for r in group]
            labels = [r["labels"].strip() or "O" for r in group]
            spans, rep = bio_to_spans(labels)
            repaired += rep
            unknown |= {t for _, _, t in spans if t not in self.schema.types}
            sentences.append(Sentence(
                dataset=self.schema.name, split=split,
                sid=f"{self.schema.folder}:{split}:{sid}",
                tokens=tokens, spans=spans, origin=ORIGINAL, label_source="gold",
                provenance={"file": str(self.path(split).name), "sentence_id": sid},
            ))
        if unknown:
            raise ValueError(f"{self.schema.name}/{split}: labels outside schema: {sorted(unknown)}")
        self.stats[split] = {"sentences": len(sentences), "repaired_I_tags": repaired,
                             "mentions": sum(len(s.spans) for s in sentences)}
        if repaired:
            logger.info(f"{self.schema.name}/{split}: {repaired} I- tags without a matching B- started new spans")
        return sentences


class SFullAdapter:
    """Original-paper synthetic corpora (S-full): sentence, value, temperature, domain."""

    def __init__(self, schema: DatasetSchema, path: Optional[Path] = None):
        self.schema = schema
        self.path = Path(path) if path else SYNTHETIC_FULL_DIR / schema.s_full_file

    def load(self) -> List[Sentence]:
        out = []
        with open(self.path, newline="", encoding="utf-8") as f:
            for i, row in enumerate(csv.DictReader(f)):
                domain_type = self.schema.normalize_domain(row["domain"])
                if domain_type is None:
                    raise ValueError(f"Unknown domain '{row['domain']}' in {self.path}")
                out.append(Sentence(
                    dataset=self.schema.name, split="synthetic",
                    sid=f"{self.schema.folder}:s_full:{i}",
                    tokens=tokenize(row["sentence"]), spans=[],
                    origin=SYNTHETIC, track=S_FULL, label_source="none",
                    provenance={"raw_sentence": row["sentence"], "value": float(row["value"]),
                                "temperature": float(row["temperature"]), "requested_domain": row["domain"],
                                "requested_type": domain_type, "file": self.path.name},
                ))
        return out


def load_jsonl(path: Path) -> Iterable[Dict]:
    """Records of a JSONL file; an interrupted last line is repaired (pipeline.durable)."""
    from pipeline.durable import read_jsonl
    yield from read_jsonl(path)


class SFullSilverAdapter:
    """Original synthetic corpus (S-full) with silver labels from generation/annotate.py --original.

    One sentence per unique text (exact duplicates were annotated once).
    """

    def __init__(self, schema: DatasetSchema, directory: Path):
        self.schema = schema
        self.directory = Path(directory)

    def load(self) -> List[Sentence]:
        path = self.directory / "annotations.jsonl"
        if not path.exists():
            raise FileNotFoundError(f"{path} missing; run generation/annotate.py --original first")
        return [Sentence(dataset=self.schema.name, split="synthetic", sid=r["sid"], tokens=r["tokens"],
                         spans=[tuple(x) for x in r["spans"]], origin=SYNTHETIC, track=S_FULL,
                         label_source=r["label_source"],
                         provenance={"requested_type": r["requested_type"], "copies": r["copies"],
                                     "domain_satisfied": r["domain_satisfied"]})
                for r in load_jsonl(path)]


