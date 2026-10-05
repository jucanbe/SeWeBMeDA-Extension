"""The experiment design (plan v6 without LoRA): DEV grid, TEST matrix, runtime spec.

DEV (200 sentences per dataset, seed 20261001):
  Qwen 4B : E0; E1 k=1/3/5/10; random k=5 (Rnd); E5 m=5/10/20; E2, E3, E2c k=1/3/5/10
  Qwen 9B : E0; E1 k=1/3/5/10; E2 k=1/3/5/10
  Qwen 27B: E0; E1 k=1/3/5/10
  Each size tunes its own k (independent tuning; documented in configs/comparisons_v6.json).
TEST (BioRED full TEST; BC5CDR and MedMentions 1,000 stratified, seed 20261001):
  Qwen 4B : E0, E1, E2, E3, E2c, E5, E4 (E0 + validator), E6 (E5 + validator)
  Qwen 9B : E0, E1, E2
  Qwen 27B: E0, E1
"""
import os
from typing import Dict, List

from pipeline.registry import MODELS, QWEN_ORDER, ModelSpec

DATASETS = ["BC5CDR", "BioRED", "MedMentions"]
DEV_SUBSET = {"n": 200, "seed": 20261001}
TEST_SUBSETS = {"BC5CDR": {"n": 1000, "seed": 20261001}, "BioRED": {"n": 0, "seed": 20261001},
                "MedMentions": {"n": 1000, "seed": 20261001}}
if os.environ.get("VLLM_PAPER_TEST_SCALE"):          # end-to-end tests with a fake server only
    _n = int(os.environ["VLLM_PAPER_TEST_SCALE"])
    DEV_SUBSET = {"n": _n, "seed": 20261001}
    TEST_SUBSETS = {d: {"n": _n, "seed": 20261001} for d in TEST_SUBSETS}
KS = [1, 3, 5, 10]
MS = [5, 10, 20]
STRATEGY = {"E1": "original", "E2": "synthetic", "E3": "mixed", "E2c": "silver_original"}
DEV_CONDITIONS = {"4b": ["E0", "E1", "Rnd", "E5", "E2", "E3", "E2c"], "9b": ["E0", "E1", "E2"], "27b": ["E0", "E1"]}
TEST_CONDITIONS = {"4b": ["E0", "E1", "E2", "E3", "E2c", "E5"], "9b": ["E0", "E1", "E2"], "27b": ["E0", "E1"]}
TEST_DERIVED = {"4b": {"E4": "E0", "E6": "E5"}}            # validator conditions, no LLM calls
PRIMARY_VALIDITY_CONDITIONS = ["E0", "E1"]
MAX_TOKENS = 2048


def model_block(spec: ModelSpec, base_url: str = None) -> Dict:
    return {"key": spec.key, "id": spec.hf_id, "revision": spec.revision, "label": spec.label,
            "base_url": base_url or f"http://127.0.0.1:{spec.port}/v1", "extra_body": spec.request_extra}


def runtime_spec(spec: ModelSpec) -> Dict:
    """Static part of the runtime; enters every config and therefore the frozen hash."""
    from pipeline.registry import GPU_MEMORY_UTILIZATION, MAX_MODEL_LEN, SEED, TENSOR_PARALLEL
    return {"engine": "vllm", "dtype": "bfloat16", "max_model_len": MAX_MODEL_LEN,
            "tensor_parallel_size": TENSOR_PARALLEL, "gpu_memory_utilization": GPU_MEMORY_UTILIZATION,
            "server_seed": SEED, "thinking": "disabled", "structured_output": "json_schema",
            "concurrency": spec.concurrency, "max_num_seqs": spec.max_num_seqs}


def base_config(spec: ModelSpec, dataset: str, split: str, subset: Dict) -> Dict:
    return {"dataset": dataset, "split": split, "subset": subset, "model": model_block(spec),
            "runtime": runtime_spec(spec), "max_tokens": MAX_TOKENS, "temperature": 0.0, "seed": 0}


def condition_fields(cond: str, value=None) -> Dict:
    if cond == "E0":
        return {}
    if cond in STRATEGY:
        return {"fewshot": {"strategy": STRATEGY[cond], "k": value}}
    if cond == "Rnd":
        return {"fewshot": {"strategy": "random_original", "k": value}}
    if cond == "E5":
        return {"rag": {"enabled": True, "max_facts": value}}
    raise ValueError(cond)


def dev_configs(model_key: str) -> List[Dict]:
    spec = MODELS[model_key]
    out = []
    for ds in DATASETS:
        base = base_config(spec, ds, "dev", DEV_SUBSET)
        for cond in DEV_CONDITIONS[model_key]:
            if cond == "E0":
                grid = [None]
            elif cond == "Rnd":
                grid = [5]
            elif cond == "E5":
                grid = MS
            else:
                grid = KS
            for v in grid:
                suffix = "" if v is None else (f"-m{v}" if cond == "E5" else f"-k{v}")
                out.append(dict(base, name=f"dev-{cond}{suffix}-{spec.label}-{ds}", condition=cond,
                                **condition_fields(cond, v)))
    return out


def all_dev_configs(models=QWEN_ORDER) -> Dict[str, List[Dict]]:
    return {m: dev_configs(m) for m in models}


def needs(cfg: Dict) -> str:
    """Which annotation set a config needs: 'original' (synthetic pool), 'control' (E2c) or ''."""
    strat = cfg.get("fewshot", {}).get("strategy")
    if strat in ("synthetic", "mixed"):
        return "original"
    if strat == "silver_original":
        return "control"
    return ""


def test_configs(model_key: str, selection: Dict) -> List[Dict]:
    """selection[model_key][dataset][cond] = selected k or m."""
    spec = MODELS[model_key]
    out = []
    for ds in DATASETS:
        base = base_config(spec, ds, "test", TEST_SUBSETS[ds])
        for cond in TEST_CONDITIONS[model_key]:
            v = None if cond == "E0" else selection[model_key][ds][cond]
            out.append(dict(base, name=f"test-{cond}-{spec.label}-{ds}", condition=cond, frozen=True,
                            **condition_fields(cond, v)))
    return out
