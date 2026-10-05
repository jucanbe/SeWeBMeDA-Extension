"""In-process fallback for nomic-embed-text-v1.5 (only if vLLM cannot serve it) and backend bookkeeping.

The model is loaded from VLLM_Paper/Models with the pinned remote code (nomic-ai/nomic-bert-2048),
mean-pooled and L2-normalised (the model's sentence-transformers pooling), truncated at 2,048 tokens
as in the vLLM setting, and unloaded (GPU memory freed) before any Qwen model starts.
"""
import gc
import json
from datetime import datetime, timezone
from typing import Dict, List, Optional

import numpy as np

from experiments.fewshot.retrieve import CACHE_DIR, EMBED_MODEL
from pipeline.durable import atomic_write_json
from pipeline.server import ServerError

BACKEND_FILE = CACHE_DIR / "backend.json"
MAX_LENGTH = 2048


def recorded_backend() -> Optional[str]:
    if not BACKEND_FILE.exists():
        return None
    return json.loads(BACKEND_FILE.read_text())["backend"]


def check_backend(backend: str, details: Dict):
    """Record the backend on first use; refuse to extend a cache computed with another backend."""
    if BACKEND_FILE.exists():
        rec = json.loads(BACKEND_FILE.read_text())
        if rec["backend"] != backend or rec["model"] != EMBED_MODEL:
            raise ServerError(f"embedding cache was computed with {rec['backend']} / {rec['model']}; "
                               f"refusing to add {backend} / {EMBED_MODEL} embeddings")
        return
    atomic_write_json(BACKEND_FILE, {"backend": backend, "model": EMBED_MODEL, "details": details,
                                     "pooling": "mean, L2-normalised", "max_length": MAX_LENGTH,
                                     "recorded_at": datetime.now(timezone.utc).isoformat()})


class LocalNomic:
    def __init__(self, prov: Dict, spec, batch_size: int = 64):
        self.prov = prov
        self.spec = spec
        self.batch_size = batch_size
        self.model = self.tok = None

    def __enter__(self):
        import torch
        from transformers import AutoModel, AutoTokenizer
        code_rev = self.spec.code_deps[0][1]
        path = self.prov["local_path"]
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"[EMBED] loading {self.spec.hf_id} in-process on {self.device}")
        self.tok = AutoTokenizer.from_pretrained(path)
        self.model = AutoModel.from_pretrained(path, trust_remote_code=True, code_revision=code_rev).to(self.device)
        self.model.eval()
        return self

    def provenance(self) -> Dict:
        import torch
        import transformers
        return {"transformers_version": transformers.__version__, "torch_version": torch.__version__,
                "device": self.device, "revision": self.spec.revision, "code_revision": self.spec.code_deps[0][1]}

    def embed(self, texts: List[str]) -> np.ndarray:
        import torch
        out = []
        with torch.no_grad():
            for i in range(0, len(texts), self.batch_size):
                enc = self.tok(texts[i:i + self.batch_size], padding=True, truncation=True, max_length=MAX_LENGTH,
                               return_tensors="pt").to(self.device)
                hidden = self.model(**enc)[0]
                mask = enc["attention_mask"].unsqueeze(-1).to(hidden.dtype)
                pooled = (hidden * mask).sum(1) / mask.sum(1).clamp(min=1e-9)
                pooled = torch.nn.functional.normalize(pooled, p=2, dim=1)
                out.append(pooled.float().cpu().numpy())
        return np.concatenate(out) if out else np.zeros((0, 768), dtype=np.float32)

    def __exit__(self, *exc):
        import torch
        del self.model
        self.model = None
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        print("[EMBED] in-process embedding model unloaded")
