# Opus 5.5 reference (exploratory, outside the frozen protocol)

The same TEST sentences, prompts and demonstrations as the Qwen3.5 runs. Conditions E0 (zero-shot) and E1 (original demonstrations), 6192 sentences. All sentences have an output; 74 sentences that a safety filter stopped were rerun in smaller batches.

## Micro-F1 against gold (95% sentence-bootstrap CI)

| Condition | Dataset | Opus 5.5 | Qwen 27B | Qwen 9B | Qwen 4B |
|---|---|---|---|---|---|
| E0 | BC5CDR | 0.854 [0.839, 0.868] | 0.737 | 0.686 | 0.661 |
| E0 | BioRED | 0.890 [0.880, 0.899] | 0.714 | 0.673 | 0.626 |
| E0 | MedMentions | 0.478 [0.459, 0.496] | 0.330 | 0.275 | 0.208 |
| E1 | BC5CDR | 0.897 [0.885, 0.909] | 0.816 | 0.767 | 0.744 |
| E1 | BioRED | 0.914 [0.904, 0.924] | 0.808 | 0.751 | 0.722 |
| E1 | MedMentions | 0.669 [0.653, 0.684] | 0.617 | 0.563 | 0.514 |

## LAVA reviewer on the predictions (pooled over the 6 cells)

| | Opus 5.5 | Qwen 27B (same cells) |
|---|---|---|
| Predicted spans | 20797 | 18922 |
| Share correct | 0.715 | 0.644 |
| AUROC W_cal | 0.862 [0.854, 0.869] | 0.832 [0.825, 0.840] |
| AUROC W_eq | 0.848 | 0.791 |
| AUROC B0 (classifier confidence) | 0.883 | 0.766 |
| AUROC B2 (seen in TRAIN) | 0.657 | 0.707 |
| Passed at 0.75 (W_cal) | 80.8% | 93.0% |
| P(correct given passed) | 0.840 | 0.683 |
| False acceptance | 0.453 | 0.829 |
| False rejection | 0.051 | 0.014 |
| F1 unfiltered to filtered | 0.746 to 0.786 | 0.641 to 0.655 |

Per cell, the W_cal AUROC on the Opus predictions ranges from 0.759 (E0 BioRED) to 0.853 (E0 MedMentions).

## Caveats

- Run with Claude Code sub-agents, not through the API. Batches of up to 40 sentences per call, demonstrations given as text, no temperature or seed control.
- Sub-agent tool use was checked: only reading the batch file and writing the output file.
- The benchmarks are public, so memorisation by a frontier model cannot be excluded.
- Synthetic-demonstration conditions (E2, E3) were not run with Opus.

Scripts: build_inputs.py, make_repair.py, build_runs.py, score_opus.py, analyse.py. Full numbers: results/opus_results.json.
