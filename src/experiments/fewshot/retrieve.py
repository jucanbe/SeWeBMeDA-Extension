"""Few-shot demonstration retrieval by embedding similarity.

Embeddings come from vLLM's OpenAI-compatible /v1/embeddings endpoint
(nomic-ai/nomic-embed-text-v1.5, with its "search_query:"/"search_document:" prefixes)
and are cached on disk keyed by text hash and model.
"""
import hashlib
import json
import random
from pathlib import Path
from typing import Dict, List, Optional, Sequence

import httpx
import numpy as np

from experiments.data.model import Sentence

EMBED_MODEL = "nomic-ai/nomic-embed-text-v1.5@e9b6763023c676ca8431644204f50c2b100d9aab"
CACHE_DIR = Path(__file__).resolve().parents[3] / "embeddings"          # VLLM_Paper/embeddings


class MissingEmbeddings(RuntimeError):
    pass


class Embedder:
    """Embedding cache keyed by (model id@revision, prefixed text).

    offline=True never calls a server: every embedding must already be cached
    (the embedding phase of execution2 fills the cache before Qwen starts)."""

    def __init__(self, base_url: str = "http://127.0.0.1:8002/v1", model: str = EMBED_MODEL,
                 cache_dir: Path = CACHE_DIR, batch_size: int = 64, offline: bool = False,
                 served_name: str = "nomic-ai/nomic-embed-text-v1.5", compute_fn=None):
        self.url = base_url.rstrip("/") + "/embeddings"
        self.model = model
        self.served_name = served_name
        self.batch_size = batch_size
        self.offline = offline
        self.compute_fn = compute_fn          # in-process fallback: texts (with prefixes) -> vectors
        self.cache_dir = Path(cache_dir) / model.replace("/", "__")
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self._mem: Dict[str, np.ndarray] = {}

    def _key(self, text: str) -> str:
        return hashlib.sha256(f"{self.model}\x00{text}".encode()).hexdigest()

    def _path(self, key: str) -> Path:
        return self.cache_dir / key[:2] / f"{key}.npy"

    def embed(self, texts: Sequence[str], kind: str) -> np.ndarray:
        prefix = {"query": "search_query: ", "document": "search_document: "}[kind]
        texts = [prefix + t for t in texts]
        keys = [self._key(t) for t in texts]
        missing = []
        for t, k in zip(texts, keys):
            if k in self._mem:
                continue
            p = self._path(k)
            if p.exists():
                self._mem[k] = np.load(p)
            else:
                missing.append((t, k))
        if missing and self.offline:
            raise MissingEmbeddings(f"{len(missing)} texts are not in the embedding cache "
                                    f"(e.g. {missing[0][0][:80]!r}); run the embedding phase first")
        for i in range(0, len(missing), self.batch_size):
            chunk = missing[i:i + self.batch_size]
            if self.compute_fn is not None:
                vectors = list(self.compute_fn([t for t, _ in chunk]))
            else:
                resp = httpx.post(self.url, json={"model": self.served_name, "input": [t for t, _ in chunk]},
                                  timeout=300)
                resp.raise_for_status()
                vectors = [d["embedding"] for d in sorted(resp.json()["data"], key=lambda d: d["index"])]
            for (t, k), vec in zip(chunk, vectors):
                v = np.asarray(vec, dtype=np.float32)
                v /= np.linalg.norm(v) or 1.0
                self._path(k).parent.mkdir(parents=True, exist_ok=True)
                np.save(self._path(k), v)
                self._mem[k] = v
        return np.stack([self._mem[k] for k in keys])


class DemoPool:
    """A pool of labelled sentences that may serve as demonstrations."""

    def __init__(self, name: str, sentences: List[Sentence], embedder: Optional[Embedder] = None,
                 exclude_texts: Optional[set] = None):
        exclude_texts = exclude_texts or set()
        allowed_splits = {"train", "synthetic"}
        for s in sentences:
            if s.split not in allowed_splits:
                raise ValueError(f"pool '{name}' contains a {s.split} sentence ({s.sid}); only TRAIN or synthetic allowed")
        self.name = name
        self.sentences = [s for s in sentences if " ".join(s.text.split()).lower() not in exclude_texts]
        self.embedder = embedder
        self._matrix = None

    @property
    def matrix(self) -> np.ndarray:
        if self._matrix is None:
            self._matrix = self.embedder.embed([s.text for s in self.sentences], "document")
        return self._matrix

    def nearest(self, query_vec: np.ndarray, k: int) -> List[Sentence]:
        if k <= 0:
            return []
        sims = self.matrix @ query_vec
        top = np.argsort(-sims, kind="stable")[:k]
        return [self.sentences[i] for i in top]

    def random(self, k: int, seed: int) -> List[Sentence]:
        rng = random.Random(seed)
        return rng.sample(self.sentences, k)


def select_demos(query: Sentence, pools: Dict[str, DemoPool], strategy: str, k: int, embedder: Embedder,
                 seed: int = 0) -> List[Sentence]:
    """strategy: original | synthetic | mixed | silver_original | random_original.

    mixed uses k//2 original and k - k//2 synthetic (same total k as the single-pool
    conditions), interleaved by similarity rank.
    """
    if k == 0 or strategy == "none":
        return []
    if strategy == "random_original":
        return pools["original"].random(k, seed)
    q = embedder.embed([query.text], "query")[0]
    if strategy in ("original", "synthetic", "silver_original"):
        demos = pools[strategy].nearest(q, k)
    elif strategy == "mixed":
        o = pools["original"].nearest(q, k // 2)
        s = pools["synthetic"].nearest(q, k - k // 2)
        demos = [x for pair in zip(s, o) for x in pair] + s[len(o):] + o[len(s):]
    else:
        raise ValueError(f"unknown few-shot strategy '{strategy}'")
    # most similar demonstration closest to the query in the prompt
    return list(reversed(demos))
