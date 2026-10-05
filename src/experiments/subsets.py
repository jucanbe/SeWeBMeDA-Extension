"""Fixed, immutable evaluation subsets.

A subset is selected once with a recorded seed and stored as a manifest; later
calls load the manifest and refuse to silently change it.

Stratification: every sentence is assigned to the stratum of the rarest gold
type it contains (by frequency in the split), or "none"; strata are sampled in
proportion to their size (largest-remainder rounding, at least one sentence
per non-empty stratum), which preserves type representation.
"""
import json
import random
from collections import Counter, defaultdict
from pathlib import Path
from typing import List

from experiments.data.adapters import BIOCsvAdapter
from experiments.data.model import Sentence, sha256_file
from experiments.schemas import RESULTS_DIR, get_schema

SUBSET_DIR = RESULTS_DIR / "subsets"


def select(sentences: List[Sentence], n: int, seed: int) -> List[str]:
    if n >= len(sentences):
        return [s.sid for s in sentences]
    freq = Counter(t for s in sentences for _, _, t in s.spans)
    strata = defaultdict(list)
    for s in sentences:
        types = {t for _, _, t in s.spans}
        key = min(types, key=lambda t: (freq[t], t)) if types else "none"
        strata[key].append(s.sid)
    total = len(sentences)
    quotas = {k: max(1, int(n * len(v) / total)) for k, v in strata.items()}
    remainders = sorted(strata, key=lambda k: n * len(strata[k]) / total - int(n * len(strata[k]) / total), reverse=True)
    i = 0
    while sum(quotas.values()) < n:
        k = remainders[i % len(remainders)]
        if quotas[k] < len(strata[k]):
            quotas[k] += 1
        i += 1
    while sum(quotas.values()) > n:
        k = max(quotas, key=lambda k: quotas[k])
        quotas[k] -= 1
    rng = random.Random(seed)
    chosen = []
    for k in sorted(strata):
        chosen.extend(rng.sample(sorted(strata[k]), min(quotas[k], len(strata[k]))))
    order = {s.sid: i for i, s in enumerate(sentences)}
    return sorted(chosen, key=order.get)


def get_subset(dataset: str, split: str, n: int, seed: int = 20261001) -> Path:
    schema = get_schema(dataset)
    adapter = BIOCsvAdapter(schema)
    path = SUBSET_DIR / f"{schema.folder}_{split}_{'full' if n <= 0 else n}_seed{seed}.json"
    source_hash = sha256_file(adapter.path(split))
    if path.exists():
        m = json.loads(path.read_text())
        if m["source_sha256"] != source_hash:
            raise RuntimeError(f"{path} was built from a different {split}.csv")
        return path
    sentences = adapter.load(split)
    ids = [s.sid for s in sentences] if n <= 0 else select(sentences, n, seed)
    chosen = set(ids)
    sub = [s for s in sentences if s.sid in chosen]
    type_counts = Counter(t for s in sub for _, _, t in s.spans)
    full_counts = Counter(t for s in sentences for _, _, t in s.spans)
    manifest = {
        "dataset": schema.name, "split": split, "n": len(ids), "seed": seed,
        "method": "full split" if n <= 0 else "stratified by rarest gold type, proportional allocation",
        "source_file": f"{schema.folder}/{split}.csv", "source_sha256": source_hash,
        "mentions": sum(type_counts.values()), "type_counts": dict(type_counts),
        "full_split_type_counts": dict(full_counts), "sentence_ids": ids,
    }
    SUBSET_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest, indent=1))
    path.chmod(0o444)
    return path


def load_subset(path: Path) -> List[str]:
    return json.loads(Path(path).read_text())["sentence_ids"]
