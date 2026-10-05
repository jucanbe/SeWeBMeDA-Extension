"""Every path of the package, resolved from the VLLM_Paper root (nothing outside it)."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
MODELS_DIR = ROOT / "Models"
HF_HOME = MODELS_DIR / "huggingface"
MODEL_MANIFESTS = MODELS_DIR / "manifests"
EMBEDDINGS_DIR = ROOT / "embeddings"
LOGS_DIR = ROOT / "logs"
RESULTS_DIR = ROOT / "results"
RUNS_DIR = RESULTS_DIR / "runs"
FROZEN_DIR = RESULTS_DIR / "frozen"
ANALYSIS_DIR = RESULTS_DIR / "analysis"
CONFIGS_DIR = ROOT / "configs"
SYNTHETIC_DIR = ROOT / "synthetic"
BERT_DIR = ROOT / "BERT_models"
LOCK_FILE = ROOT / ".execution.lock"
PID_FILE = LOGS_DIR / "vllm.pid.json"


def configure_environment():
    """Model caches live inside the package; set before importing huggingface_hub / vllm."""
    os.environ["HF_HOME"] = str(HF_HOME)
    os.environ["HF_HUB_CACHE"] = str(HF_HOME / "hub")
    os.environ.setdefault("HF_HUB_ENABLE_HF_TRANSFER", "0")
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    os.environ["HF_MODULES_CACHE"] = str(HF_HOME / "modules")        # trust_remote_code modules
    os.environ["TRANSFORMERS_CACHE"] = str(HF_HOME / "hub")          # older transformers versions
    os.environ["HF_XET_CACHE"] = str(HF_HOME / "xet")
    os.environ["VLLM_CACHE_ROOT"] = str(MODELS_DIR / "vllm_cache")
    os.environ["XDG_CACHE_HOME"] = str(MODELS_DIR / "xdg_cache")      # other ~/.cache users
    # flashinfer ignores XDG and writes <FLASHINFER_WORKSPACE_BASE>/.cache/flashinfer (default: $HOME)
    os.environ["FLASHINFER_WORKSPACE_BASE"] = str(MODELS_DIR / "flashinfer")
    os.environ["TORCHINDUCTOR_CACHE_DIR"] = str(MODELS_DIR / "torchinductor_cache")
    os.environ["TRITON_CACHE_DIR"] = str(MODELS_DIR / "triton_cache")
    for d in (HF_HOME, MODEL_MANIFESTS, EMBEDDINGS_DIR, LOGS_DIR, RESULTS_DIR, SYNTHETIC_DIR):
        d.mkdir(parents=True, exist_ok=True)
