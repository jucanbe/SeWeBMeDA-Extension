#!/usr/bin/env python3
"""Score the Opus run directories with the reviewer snapshot used in the study (writes entityclass.jsonl inside each Opus run)."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "src"))
from experiments.review.score import score_runs  # noqa: E402
score_runs(sorted((HERE / "runs").glob("opus-*")), use_bert=True)
