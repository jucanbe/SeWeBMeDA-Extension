# Freeze report

Frozen at 2026-10-04T02:21:05.496328+00:00 (prompt ner-v2, embeddings nomic-ai/nomic-embed-text-v1.5@e9b6763023c676ca8431644204f50c2b100d9aab).

## Selected settings (DEV micro-F1; ties -> smaller value)

| Model | Dataset | Setting | Selected | DEV F1 |
|---|---|---|---|---|
| 4b | BC5CDR | E1 k | 10 | 0.725 |
| 4b | BC5CDR | E2 k | 1 | 0.665 |
| 4b | BC5CDR | E3 k | 10 | 0.698 |
| 4b | BC5CDR | E2c k | 10 | 0.717 |
| 4b | BC5CDR | E5 m | 10 | 0.739 |
| 4b | BioRED | E1 k | 10 | 0.711 |
| 4b | BioRED | E2 k | 1 | 0.661 |
| 4b | BioRED | E3 k | 10 | 0.699 |
| 4b | BioRED | E2c k | 1 | 0.668 |
| 4b | BioRED | E5 m | 5 | 0.690 |
| 4b | MedMentions | E1 k | 10 | 0.520 |
| 4b | MedMentions | E2 k | 10 | 0.309 |
| 4b | MedMentions | E3 k | 10 | 0.483 |
| 4b | MedMentions | E2c k | 10 | 0.326 |
| 4b | MedMentions | E5 m | 20 | 0.429 |
| 9b | BC5CDR | E1 k | 10 | 0.765 |
| 9b | BC5CDR | E2 k | 1 | 0.696 |
| 9b | BioRED | E1 k | 10 | 0.755 |
| 9b | BioRED | E2 k | 10 | 0.703 |
| 9b | MedMentions | E1 k | 10 | 0.550 |
| 9b | MedMentions | E2 k | 5 | 0.328 |
| 27b | BC5CDR | E1 k | 10 | 0.805 |
| 27b | BioRED | E1 k | 10 | 0.788 |
| 27b | MedMentions | E1 k | 10 | 0.607 |

## Validator thresholds (4B)

- BC5CDR E4: {'retype_purity': 0.8, 'retype_min_count': 2, 'drop_non_entity_ratio': 0.8, 'drop_min_count': 5} (DEV F1 0.637)
- BC5CDR E6: {'retype_purity': 0.8, 'retype_min_count': 2, 'drop_non_entity_ratio': 0.8, 'drop_min_count': 5} (DEV F1 0.752)
- BioRED E4: {'retype_purity': 0.9, 'retype_min_count': 2, 'drop_non_entity_ratio': 0.9, 'drop_min_count': 5} (DEV F1 0.658)
- BioRED E6: {'retype_purity': 0.9, 'retype_min_count': 2, 'drop_non_entity_ratio': 0.8, 'drop_min_count': 5} (DEV F1 0.702)
- MedMentions E4: {'retype_purity': 0.8, 'retype_min_count': 2, 'drop_non_entity_ratio': 0.9, 'drop_min_count': 5} (DEV F1 0.370)
- MedMentions E6: {'retype_purity': 0.8, 'retype_min_count': 2, 'drop_non_entity_ratio': 0.8, 'drop_min_count': 5} (DEV F1 0.562)

## EntityClass weights

| Scheme | congruence | coverage | constraint | completeness | consistency |
|---|---|---|---|---|---|
| W0 | 0.25 | 0.15 | 0.25 | 0.15 | 0.20 |
| W1 | 0.20 | 0.20 | 0.20 | 0.20 | 0.20 |
| W3 | 0.20 | 0.00 | 0.05 | 0.30 | 0.45 |

W3 DEV AUROC 0.852. W2: not available (optional).
Thresholds: pass 0.75, review 0.5.
DEV validity rows: 10363.

## Runtime that TEST must match

- 4b: Qwen/Qwen3.5-4B @ 851bf6e806ef, vLLM 0.30.1rc1.dev622+gf03026a54, args --tensor-parallel-size 1 --gpu-memory-utilization 0.9 --seed 0 --dtype bfloat16 --max-model-len 16384 --max-num-seqs 64 --reasoning-parser qwen3 --language-model-only
- 9b: Qwen/Qwen3.5-9B @ c20223623576, vLLM 0.30.1rc1.dev622+gf03026a54, args --tensor-parallel-size 1 --gpu-memory-utilization 0.9 --seed 0 --dtype bfloat16 --max-model-len 16384 --max-num-seqs 64 --reasoning-parser qwen3 --language-model-only
- 27b: Qwen/Qwen3.5-27B @ fc05daec18b0, vLLM 0.30.1rc1.dev622+gf03026a54, args --tensor-parallel-size 1 --gpu-memory-utilization 0.9 --seed 0 --dtype bfloat16 --max-model-len 16384 --max-num-seqs 64 --reasoning-parser qwen3 --language-model-only

## TEST configurations

- 4b: test-E0-small-BC5CDR, test-E1-small-BC5CDR, test-E2-small-BC5CDR, test-E3-small-BC5CDR, test-E2c-small-BC5CDR, test-E5-small-BC5CDR, test-E0-small-BioRED, test-E1-small-BioRED, test-E2-small-BioRED, test-E3-small-BioRED, test-E2c-small-BioRED, test-E5-small-BioRED, test-E0-small-MedMentions, test-E1-small-MedMentions, test-E2-small-MedMentions, test-E3-small-MedMentions, test-E2c-small-MedMentions, test-E5-small-MedMentions, test-E4-small-BC5CDR, test-E6-small-BC5CDR, test-E4-small-BioRED, test-E6-small-BioRED, test-E4-small-MedMentions, test-E6-small-MedMentions
- 9b: test-E0-medium-BC5CDR, test-E1-medium-BC5CDR, test-E2-medium-BC5CDR, test-E0-medium-BioRED, test-E1-medium-BioRED, test-E2-medium-BioRED, test-E0-medium-MedMentions, test-E1-medium-MedMentions, test-E2-medium-MedMentions
- 27b: test-E0-large-BC5CDR, test-E1-large-BC5CDR, test-E0-large-BioRED, test-E1-large-BioRED, test-E0-large-MedMentions, test-E1-large-MedMentions

TEST has not been run. Start it only after approval: `python3 execution2.py --stage test`.
