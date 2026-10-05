"""Pinned models and their vLLM launch settings (identical for DEV and TEST)."""
import os
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

MAX_MODEL_LEN = 16384
GPU_MEMORY_UTILIZATION = 0.90
TENSOR_PARALLEL = 1
SEED = 0
CHAT_PORT = int(os.environ.get("VLLM_PAPER_CHAT_PORT", "8000"))
EMBED_PORT = int(os.environ.get("VLLM_PAPER_EMBED_PORT", "8002"))


@dataclass(frozen=True)
class ModelSpec:
    key: str                      # short name used in run names and CLI
    hf_id: str
    revision: str
    role: str                     # annotator | classifier | embedding
    label: str                    # run-name label (small / medium / large / annotator / embedding)
    port: int
    serve_args: List[str]         # vLLM flags beyond the common ones
    alt_serve_args: List[List[str]] = field(default_factory=list)   # tried only if the primary flags are rejected
    request_extra: Dict = field(default_factory=dict)               # extra JSON fields of every request
    concurrency: int = 64
    max_tokens: int = 2048
    max_num_seqs: int = 0                         # explicit vLLM --max-num-seqs (0 = vLLM default)
    # remote code this model needs from OTHER repositories: (repo, pinned revision, file patterns).
    # nomic-embed-text-v1.5's config maps AutoConfig/AutoModel to nomic-ai/nomic-bert-2048, so that code
    # must be cached too, otherwise offline startup fails inside AutoConfig.from_pretrained.
    code_deps: Tuple[Tuple[str, str, Tuple[str, ...]], ...] = ()
    trust_remote_code: bool = False
    ignore_patterns: Tuple[str, ...] = ()       # repository files vLLM does not need (duplicate weight formats)


# Qwen3.5 is a hybrid (Mamba-style) model: vLLM's default max_num_seqs=1024 exceeds the 588 Mamba cache
# blocks available for 27B on one 94 GB GPU. All three sizes use the same explicit value, equal to the
# client concurrency, so the scheduler limit is identical across sizes and between DEV and TEST.
QWEN_MAX_NUM_SEQS = 64
QWEN_ARGS = ["--dtype", "bfloat16", "--max-model-len", str(MAX_MODEL_LEN), "--max-num-seqs", str(QWEN_MAX_NUM_SEQS),
             "--reasoning-parser", "qwen3"]

NOMIC_CODE_REVISION = "7710840340a098cfb869c4f65e87cf2b1b70caca"   # nomic-ai/nomic-bert-2048 (remote code)

COMMON_ARGS = ["--tensor-parallel-size", str(TENSOR_PARALLEL), "--gpu-memory-utilization", str(GPU_MEMORY_UTILIZATION),
               "--seed", str(SEED)]

MODELS: Dict[str, ModelSpec] = {
    "gpt-oss-20b": ModelSpec(
        key="gpt-oss-20b", hf_id="openai/gpt-oss-20b", revision="6cee5e81ee83917806bbde320786a8fb61efebee",
        role="annotator", label="annotator", port=CHAT_PORT,
        serve_args=["--max-model-len", str(MAX_MODEL_LEN)],
        request_extra={"reasoning_effort": "low"}, concurrency=64, max_tokens=4096,
        ignore_patterns=("original/*", "metal/*")),
    "4b": ModelSpec(
        key="4b", hf_id="Qwen/Qwen3.5-4B", revision="851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a",
        role="classifier", label="small", port=CHAT_PORT,
        serve_args=QWEN_ARGS + ["--language-model-only"], alt_serve_args=[list(QWEN_ARGS)],
        max_num_seqs=QWEN_MAX_NUM_SEQS,
        request_extra={"chat_template_kwargs": {"enable_thinking": False}}),
    "9b": ModelSpec(
        key="9b", hf_id="Qwen/Qwen3.5-9B", revision="c202236235762e1c871ad0ccb60c8ee5ba337b9a",
        role="classifier", label="medium", port=CHAT_PORT,
        serve_args=QWEN_ARGS + ["--language-model-only"], alt_serve_args=[list(QWEN_ARGS)],
        max_num_seqs=QWEN_MAX_NUM_SEQS,
        request_extra={"chat_template_kwargs": {"enable_thinking": False}}),
    "27b": ModelSpec(
        key="27b", hf_id="Qwen/Qwen3.5-27B", revision="fc05daec18b0a78c049392ed2e771dde82bdf654",
        role="classifier", label="large", port=CHAT_PORT,
        serve_args=QWEN_ARGS + ["--language-model-only"], alt_serve_args=[list(QWEN_ARGS)],
        max_num_seqs=QWEN_MAX_NUM_SEQS,
        request_extra={"chat_template_kwargs": {"enable_thinking": False}}, concurrency=QWEN_MAX_NUM_SEQS),
    "nomic-embed": ModelSpec(
        key="nomic-embed", hf_id="nomic-ai/nomic-embed-text-v1.5", revision="e9b6763023c676ca8431644204f50c2b100d9aab",
        role="embedding", label="embedding", port=EMBED_PORT,
        serve_args=["--trust-remote-code", "--code-revision", NOMIC_CODE_REVISION, "--runner", "pooling",
                    "--max-model-len", "2048"],
        alt_serve_args=[["--trust-remote-code", "--code-revision", NOMIC_CODE_REVISION, "--task", "embed",
                         "--max-model-len", "2048"]],
        concurrency=8, trust_remote_code=True, ignore_patterns=("onnx/*",),
        code_deps=(("nomic-ai/nomic-bert-2048", NOMIC_CODE_REVISION,
                    ("configuration_hf_nomic_bert.py", "modeling_hf_nomic_bert.py", "config.json")),)),
}
QWEN_ORDER = ["4b", "9b", "27b"]
LABEL_TO_KEY = {m.label: k for k, m in MODELS.items()}


def by_key(key: str) -> ModelSpec:
    key = key.lower()
    if key not in MODELS:
        raise KeyError(f"unknown model '{key}' (known: {', '.join(MODELS)})")
    return MODELS[key]
