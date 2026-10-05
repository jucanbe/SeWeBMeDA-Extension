# Synthetic Biomedical Data Generation Via a Beam Tree Strategy: intrinsic, downstream and per-prediction evaluation

Code, frozen design and results of the experiments in the journal extension (Journal of Biomedical Semantics) of the SeWeBMeDA 2026 workshop paper *Synthetic Biomedical Data Generation Via a Beam Tree Strategy for Large Language Models* (Cano-Benito, Hertling, Berns, Paulheim).

- The beam-tree generator and the synthetic corpora of the workshop paper: <https://github.com/jucanbe/SyntheticBiomedicalData-BeamSearch>.
- The EntityClass application is released separately. `src/services` and `src/models` contain the snapshot of its reviewer that was used for every score in this study.

## Contents

| Path | Content |
|---|---|
| `execution1.py` | Silver annotation with gpt-oss-20b (TRAIN control sample and synthetic corpora) |
| `execution2.py` | Entity classification with Qwen3.5 4B/9B/27B: `--stage dev`, `freeze`, `test`, `analyze` |
| `smoke_embedding.py` | Offline check of the embedding model used for demonstration retrieval |
| `src/` | Pipeline, experiment conditions (E0–E6), knowledge-graph retrieval and validator, EntityClass scoring and analysis |
| `configs/comparisons_v6.json` | Pre-registered comparisons and statistics (its hash is part of the frozen design) |
| `tests/` | Unit tests and an end-to-end test against a fake vLLM server |
| `SyntheticDataset/` | The synthetic corpora evaluated in the paper (temperature 0.01), unchanged |
| `synthetic/s_full_silver/` | Silver entity annotations of the synthetic corpora |
| `synthetic/silver_control/` | Silver annotations of the 3 × 500 TRAIN control sentences, used to measure silver quality against gold |
| `results/frozen/` | Frozen design (`freeze.json` and its sha256), freeze report, DEV validity rows and fitted learned scorers |
| `results/subsets/` | Fixed DEV and TEST sentence subsets |
| `results/runs/` | The 105 DEV runs referenced by the freeze and the 39 TEST runs: predictions, metrics, manifests and per-span EntityClass scores |
| `results/analysis/` | Output of `execution2.py --stage analyze`: `final_results.json`, tables and figures |
| `W3_reanalysis/` | Re-analysis with the DEV-calibrated weights W3 as the default reviewer (see below) |

## Reviewer weights

The pre-registered analysis in `results/analysis/` reports the EntityClass overall score under three weightings (W0, W1 and W3). The paper uses W3 (Congruence 0.20, Coverage 0.00, Constraint 0.05, Completeness 0.30, Consistency 0.45), calibrated on DEV and frozen before TEST, as the default reviewer, together with equal weights (W1). `W3_reanalysis/reanalyse_w3.py` recomputes, from the stored per-span criterion scores, every statistic that the original analysis reported for the default weights: decisions, ablation, strata, robustness, comparisons with the baselines and the effect of synthetic demonstrations. It runs no model and does not rescore any span. Its output is `W3_reanalysis/results/w3_results.json`.

## Not included

- **Benchmark datasets.** BC5CDR, BioRED and MedMentions (ST21pv) must be obtained from their original sources and placed in `Datasets/{bc5cdr,biored,MedMentions}/{train,dev,test}.csv` in token-level BIO format with the columns `words,sentence_id,labels`.
- **Knowledge graphs.** `KnowledgeGraph/experiments/` is rebuilt from the TRAIN splits with `cd src && python3 -m experiments.kg.build --dataset BC5CDR` (and `BioRED`, `MedMentions`); the rebuilt index is identical to the one used in the study.
- **BERT models.** The dataset-specific BiomedBERT models used by the Consistency criterion (`BERT_models/`, about 1.2 GB) are fine-tuned on each TRAIN split with the training script of the EntityClass repository.
- **LLM weights.** Qwen3.5 and gpt-oss-20b are downloaded automatically at pinned revisions into `Models/`.

## Reproducing the study

Requirements: Python 3.12, Linux and an NVIDIA GPU (the study used one H100 94 GB).

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -U vllm --pre --extra-index-url https://wheels.vllm.ai/nightly
pip install -r requirements.txt

python3 execution1.py                    # silver annotation (gpt-oss-20b)
python3 execution2.py --stage dev        # DEV runs, Qwen3.5 4B -> 9B -> 27B
python3 execution2.py --stage freeze     # select settings, fit weights and scorers, freeze the TEST design
python3 execution2.py --stage test       # TEST runs, only the frozen configurations
python3 execution2.py --stage analyze    # tables and statistics
python3 W3_reanalysis/reanalyse_w3.py    # statistics with W3 as the default reviewer
```

To recompute only the statistics from the included runs, place the datasets, build the knowledge graphs and run `python3 W3_reanalysis/reanalyse_w3.py` (no GPU and no BERT models needed). The full `--stage analyze` additionally needs the BERT models. Every stage resumes safely, and the TEST stage refuses to run configurations that are not in the frozen design.

The run manifests record the original runtime environment, including paths on the computing cluster where the study was executed.

Tests: `python3 -m unittest discover -s tests -t .`

## Citation

[Add the citation of the journal article once published.]
