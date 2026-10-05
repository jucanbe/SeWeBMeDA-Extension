"""KG-RAG fact retrieval and the post-hoc KG validator.

RAG: facts are retrieved from the TRAIN-derived index and put into the prompt
BEFORE prediction. The validator only acts AFTER prediction, may retype or drop
predicted spans, and never adds spans. The two are independent components.
"""
import json
from collections import defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

from experiments.data.model import Span, normalize_mention
from experiments.kg.build import MAX_NGRAM


def _trigrams(s: str) -> set:
    s = f"  {s} "
    return {s[i:i + 3] for i in range(len(s) - 2)}


class KGIndex:
    def __init__(self, entries: Dict[str, Dict], name: str = ""):
        self.entries = entries
        self.name = name
        self._tri = None

    @classmethod
    def load(cls, kg_dir: Path, include_synthetic: bool = False) -> "KGIndex":
        kg_dir = Path(kg_dir)
        entries = json.loads((kg_dir / "index.json").read_text())
        name = kg_dir.name
        if include_synthetic:
            syn = json.loads((kg_dir / "index_synthetic.json").read_text())
            for k, v in syn.items():
                if k in entries:
                    merged = dict(entries[k])
                    merged["types"] = dict(merged["types"])
                    merged["synthetic_types"] = v["types"]
                    entries[k] = merged
                else:
                    entries[k] = v
            name += "+synthetic"
        return cls(entries, name)

    def lookup(self, text: str) -> Optional[Dict]:
        return self.entries.get(normalize_mention(text))

    def fuzzy(self, key: str, threshold: float) -> Optional[Tuple[str, float]]:
        if self._tri is None:
            self._tri = defaultdict(set)
            for k in self.entries:
                if len(k) >= 5:
                    for t in _trigrams(k):
                        self._tri[t].add(k)
        q = _trigrams(key)
        cand = defaultdict(int)
        for t in q:
            for k in self._tri.get(t, ()):
                cand[k] += 1
        best = None
        for k, shared in cand.items():
            sim = shared / (len(q) + len(_trigrams(k)) - shared)
            if sim >= threshold and (best is None or sim > best[1]):
                best = (k, sim)
        return best


@dataclass
class Fact:
    start: int
    end: int
    surface: str
    kg_key: str
    types: Dict[str, int]
    non_entity: int
    match: str          # exact | fuzzy
    similarity: float
    score: Tuple

    def render(self) -> str:
        total = sum(self.types.values())
        parts = [f"{t} ({n}x)" for t, n in sorted(self.types.items(), key=lambda kv: -kv[1])]
        text = f'"{self.surface}": annotated in training data as ' + ", ".join(parts)
        if self.non_entity:
            text += f"; also seen {self.non_entity}x not annotated as an entity"
        if self.match == "fuzzy":
            text += f' (closest known form: "{self.kg_key}")'
        return text + "."


def retrieve_facts(tokens: Sequence[str], index: KGIndex, max_facts: int = 10,
                   fuzzy_threshold: float = 0.9, use_fuzzy: bool = True) -> List[Fact]:
    """Rank candidate n-grams: longer span first, then evidence, then type purity;
    overlapping candidates keep the best-ranked one."""
    cands = []
    norm = [normalize_mention(t) for t in tokens]
    for i in range(len(tokens)):
        for n in range(MAX_NGRAM, 0, -1):
            j = i + n
            if j > len(tokens):
                continue
            key = " ".join(norm[i:j])
            if not key.strip() or all(not ch.isalnum() for ch in key):
                continue
            entry = index.entries.get(key)
            match, sim = "exact", 1.0
            if entry is None and use_fuzzy and n <= 3 and len(key) >= 6:
                hit = index.fuzzy(key, fuzzy_threshold)
                if hit:
                    key, sim = hit
                    entry, match = index.entries[key], "fuzzy"
            if entry is None:
                continue
            total = sum(entry["types"].values())
            purity = max(entry["types"].values()) / total if total else 0.0
            cands.append(Fact(i, j, " ".join(tokens[i:j]), key, dict(entry["types"]), entry["o"], match, sim,
                              (n, sim, total, purity)))
    cands.sort(key=lambda f: f.score, reverse=True)
    chosen, used = [], set()
    for f in cands:
        if any(k in used for k in range(f.start, f.end)):
            continue
        chosen.append(f)
        used.update(range(f.start, f.end))
        if len(chosen) >= max_facts:
            break
    return sorted(chosen, key=lambda f: f.start)


@dataclass
class ValidatorConfig:
    retype_purity: float = 0.9      # tau
    retype_min_count: int = 3       # f
    drop_non_entity_ratio: float = 0.9   # rho
    drop_min_count: int = 5


def validate(tokens: Sequence[str], pred: Sequence[Span], index: KGIndex,
             cfg: ValidatorConfig) -> Tuple[List[Span], List[Dict]]:
    """Post-hoc validation. Returns (new spans, actions). Never adds spans."""
    out, actions = [], []
    for s, e, t in pred:
        surface = " ".join(tokens[s:e])
        entry = index.lookup(surface)
        if entry is None:
            out.append((s, e, t))
            continue
        total = sum(entry["types"].values())
        o = entry["o"]
        if o + total >= cfg.drop_min_count and o / (o + total) >= cfg.drop_non_entity_ratio:
            actions.append({"action": "drop", "span": [s, e, t], "surface": surface, "o": o, "entity": total})
            continue
        best_type, best_n = max(entry["types"].items(), key=lambda kv: kv[1])
        if best_type != t and total >= cfg.retype_min_count and best_n / total >= cfg.retype_purity:
            actions.append({"action": "retype", "span": [s, e, t], "new_type": best_type,
                            "surface": surface, "types": entry["types"]})
            out.append((s, e, best_type))
            continue
        out.append((s, e, t))
    return out, actions
