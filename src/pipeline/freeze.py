"""Freeze stage: everything that TEST may depend on is decided on DEV and written once.

1. all DEV runs must be complete;
2. EntityClass scores every DEV run (with and without the BERT cross-check);
3. selection by DEV micro-F1 (ties -> smaller k / m): k for E1 (every size), E2/E3/E2c (4B), E2 (9B);
   m for E5 (4B); validator thresholds for E4 (on E0) and E6 (on the selected E5), 4B only;
4. W3 (DEV-calibrated weights), B3 and B4 fitted on the primary validity rows
   (E0 + selected E1 of every size, aligned predicted spans); W2 copied if configs/w2_frontier_weights.json exists;
5. TEST configurations and subsets created and registered (frozen hashes);
6. the vLLM runtime of every model taken from the DEV manifests (TEST must match it);
7. results/frozen/freeze.json (+ .sha256) and FREEZE_REPORT.md. Nothing is overwritten later.
"""
import hashlib
import itertools
import json
import pickle
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

from experiments.data.model import sha256_file
from experiments.fewshot.retrieve import EMBED_MODEL
from experiments.llm.ner import PROMPT_VERSION
from experiments.review import analysis as an
from experiments.review.score import score_runs
from experiments.runner import Experiment, derive_validator, derived_config, freeze as register
from experiments.subsets import get_subset
from models.review_defaults import THRESHOLDS
from pipeline import design
from pipeline.durable import atomic_write_json
from pipeline.paths import CONFIGS_DIR, FROZEN_DIR
from pipeline.qwen import RUNTIME_KEYS
from pipeline.registry import MODELS, QWEN_ORDER

FREEZE_FILE = FROZEN_DIR / "freeze.json"
FREEZE_SHA = FROZEN_DIR / "freeze.json.sha256"
LEARNED_DIR = FROZEN_DIR / "learned"
DEV_ROWS = FROZEN_DIR / "dev_validity_rows.jsonl"
W2_FILE = CONFIGS_DIR / "w2_frontier_weights.json"
COMPARISONS = CONFIGS_DIR / "comparisons_v6.json"
VALIDATOR_GRID = [{"retype_purity": p, "retype_min_count": f, "drop_non_entity_ratio": r, "drop_min_count": 5}
                  for p, f, r in itertools.product([0.8, 0.9, 0.95], [2, 5], [0.8, 0.9, 0.95])]
SELECT = {"4b": {"E1": "k", "E2": "k", "E3": "k", "E2c": "k", "E5": "m"}, "9b": {"E1": "k", "E2": "k"},
          "27b": {"E1": "k"}}


class FreezeError(RuntimeError):
    pass


def _f1(run_dir: Path) -> float:
    return json.loads((run_dir / "metrics.json").read_text())["micro"]["f1"]


def _value(cfg: Dict):
    """Grid value of a DEV config: None for E0, m for E5, k otherwise."""
    if cfg["condition"] == "E0":
        return None
    if cfg["condition"] == "E5":
        return cfg["rag"]["max_facts"]
    return cfg["fewshot"]["k"]


def dev_runs(models=QWEN_ORDER) -> Dict:
    """{(model, dataset, condition, value): Experiment}; raises if any DEV run is not complete."""
    out, pending = {}, []
    from pipeline.qwen import runnable
    for key in models:
        for cfg in design.dev_configs(key):
            if not runnable(cfg):                       # synthetic runs before execution1 finished
                pending.append(cfg["name"])
                continue
            e = Experiment(cfg)
            if not e.status()["state"].startswith("complete"):
                pending.append(cfg["name"])
            out[(key, cfg["dataset"], cfg["condition"], _value(e.cfg))] = e
    if pending:
        raise FreezeError(f"{len(pending)} DEV runs are not complete (run execution2.py --stage dev): "
                          f"{pending[:6]}{' ...' if len(pending) > 6 else ''}")
    return out


def select(runs: Dict) -> Dict:
    sel = defaultdict(lambda: defaultdict(dict))
    grid = defaultdict(list)
    for (key, ds, cond, val), e in runs.items():
        grid[(key, ds, cond)].append((val, _f1(e.dir), e.dir.name))
    for key, conds in SELECT.items():
        for ds in design.DATASETS:
            for cond in conds:
                cands = grid[(key, ds, cond)]
                best = max(cands, key=lambda c: (round(c[1], 10), -c[0]))
                sel[key][ds][cond] = best[0]
                sel[key][ds][f"{cond}_dev"] = {"selected_run": best[2], "dev_f1": best[1],
                                               "grid": {str(v): f for v, f, _ in sorted(cands)}}
    return json.loads(json.dumps(sel))


def tune_validator(source: Experiment, tag: str) -> Dict:
    results = []
    for i, v in enumerate(VALIDATOR_GRID):
        d = derive_validator(source.dir, f"{tag}-val{i}", v)
        results.append((round(_f1(d), 10), -i, v, d.name))
    f1, neg, v, name = max(results)
    return {"value": v, "dev_f1": f1, "run": name, "grid": [(r[2], r[0]) for r in results]}


def runtime_fingerprints(runs: Dict) -> Dict[str, Dict]:
    out = {}
    for key in QWEN_ORDER:
        rts = {json.dumps({k: e._read_manifest()["runtime"].get(k) for k in RUNTIME_KEYS}, sort_keys=True)
               for (m, *_), e in runs.items() if m == key}
        if len(rts) != 1:
            raise FreezeError(f"DEV runs of {key} were produced with different runtimes: {rts}")
        out[key] = json.loads(rts.pop())
    return out


def validity_rows(runs: Dict, sel: Dict) -> List[Dict]:
    rows = []
    for key in QWEN_ORDER:
        for ds in design.DATASETS:
            for cond in design.PRIMARY_VALIDITY_CONDITIONS:
                val = None if cond == "E0" else sel[key][ds][cond]
                rows.extend(an.load_rows([runs[(key, ds, cond, val)].dir]))
    return rows


def load_w2() -> Optional[Dict]:
    if not W2_FILE.exists():
        return None
    w = json.loads(W2_FILE.read_text())
    weights = w["weights"]
    if set(weights) != set(an.CRITERIA) or abs(sum(weights.values()) - 1) > 1e-6 or min(weights.values()) < 0:
        raise FreezeError(f"{W2_FILE.name}: weights must cover {an.CRITERIA}, be >= 0 and sum to 1")
    return {"weights": weights, "provenance": {k: v for k, v in w.items() if k != "weights"},
            "sha256": sha256_file(W2_FILE)}


def freeze_stage(note: str = "") -> Dict:
    if FREEZE_FILE.exists():
        raise FreezeError(f"{FREEZE_FILE} already exists; the design is frozen. "
                          "Delete results/frozen/ deliberately only if you intend to re-freeze before any TEST run.")
    runs = dev_runs()
    print("[FREEZE] all DEV runs complete; scoring DEV predictions with EntityClass")
    score_runs([e.dir for e in runs.values()])
    sel = select(runs)
    validators = {}
    for ds in design.DATASETS:
        validators[ds] = {"E4": tune_validator(runs[("4b", ds, "E0", None)], f"dev-E4-small-{ds}"),
                          "E6": tune_validator(runs[("4b", ds, "E5", sel["4b"][ds]["E5"])], f"dev-E6-small-{ds}")}
    rows = validity_rows(runs, sel)
    FROZEN_DIR.mkdir(parents=True, exist_ok=True)
    with open(DEV_ROWS, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    x_b, x_nb, y = an.criterion_matrix(rows, bert=True), an.criterion_matrix(rows, bert=False), an.labels(rows)
    w3 = an.calibrate_w3(x_b, y)
    w3_nb = an.calibrate_w3(x_nb, y)
    LEARNED_DIR.mkdir(parents=True, exist_ok=True)
    learned = {}
    for name, fit, x in (("B3_logistic", an.fit_b3, x_b), ("B4_gbt", an.fit_b4, x_b),
                         ("B3_logistic_nobert", an.fit_b3, x_nb), ("B4_gbt_nobert", an.fit_b4, x_nb)):
        p = LEARNED_DIR / f"{name}.pkl"
        with open(p, "wb") as f:
            pickle.dump(fit(x, y), f)
        learned[name] = {"path": str(p.relative_to(FROZEN_DIR.parents[1])), "sha256": sha256_file(p)}
    w2 = load_w2()
    schemes = {"W0": an.W0, "W1": an.W1, "W3": w3["weights"]}
    if w2:
        schemes["W2"] = w2["weights"]

    test_cfgs, registry = {}, {}
    for key in QWEN_ORDER:
        cfgs = design.test_configs(key, sel)
        for ds in design.DATASETS:
            if key in design.TEST_DERIVED:
                base = {c["condition"]: c for c in cfgs if c["dataset"] == ds}
                for cond, src in design.TEST_DERIVED[key].items():
                    d = derived_config(base[src], f"test-{cond}-{MODELS[key].label}-{ds}", validators[ds][cond]["value"])
                    cfgs.append(d)
        for c in cfgs:
            registry[c["name"]] = register(c, note or "frozen on DEV").name
        test_cfgs[key] = cfgs
    subsets = {ds: get_subset(ds, "test", design.TEST_SUBSETS[ds]["n"], design.TEST_SUBSETS[ds]["seed"]).name
               for ds in design.DATASETS}
    freeze = {
        "frozen_at": datetime.now(timezone.utc).isoformat(), "note": note,
        "design": "plan v6 without LoRA (E8/E9 removed); independent k tuning per model size",
        "prompt_version": PROMPT_VERSION, "embedding_model": EMBED_MODEL,
        "selection": sel, "validators": validators,
        "weights": schemes, "w3_dev_auroc": w3["dev_auroc"], "w3_nobert": w3_nb,
        "w2": w2, "thresholds": dict(THRESHOLDS), "learned_scorers": learned,
        "b4_params": an.B4_PARAMS, "dev_validity_rows": {"path": str(DEV_ROWS.relative_to(FROZEN_DIR.parents[1])),
                                                         "rows": len(rows), "sha256": sha256_file(DEV_ROWS)},
        "runtime": runtime_fingerprints(runs), "test_configs": test_cfgs, "frozen_registry": registry,
        "test_subsets": subsets, "comparisons": {"path": "configs/comparisons_v6.json",
                                                 "sha256": sha256_file(COMPARISONS)},
        "dev_runs": sorted(e.dir.name for e in runs.values()),
    }
    atomic_write_json(FREEZE_FILE, freeze)
    FREEZE_SHA.write_text(sha256_file(FREEZE_FILE) + "\n")
    write_report(freeze)
    return freeze


def verify_freeze() -> Dict:
    """Everything TEST relies on; raises FreezeError on any mismatch."""
    if not FREEZE_FILE.exists():
        raise FreezeError("no frozen design: run 'python3 execution2.py --stage freeze' after DEV")
    if not FREEZE_SHA.exists() or FREEZE_SHA.read_text().strip() != sha256_file(FREEZE_FILE):
        raise FreezeError("freeze.json does not match its recorded sha256")
    fz = json.loads(FREEZE_FILE.read_text())
    if sha256_file(COMPARISONS) != fz["comparisons"]["sha256"]:
        raise FreezeError("configs/comparisons_v6.json changed after the freeze")
    for name, meta in fz["learned_scorers"].items():
        if sha256_file(FROZEN_DIR.parents[1] / meta["path"]) != meta["sha256"]:
            raise FreezeError(f"learned scorer {name} changed after the freeze")
    if sha256_file(DEV_ROWS) != fz["dev_validity_rows"]["sha256"]:
        raise FreezeError("DEV validity rows changed after the freeze")
    if fz["prompt_version"] != PROMPT_VERSION or fz["embedding_model"] != EMBED_MODEL:
        raise FreezeError("prompt version or embedding model differs from the frozen design")
    from experiments.runner import frozen_hash, resolve
    for key, cfgs in fz["test_configs"].items():
        for c in cfgs:
            if f"{frozen_hash(resolve(c))}.json" != fz["frozen_registry"][c["name"]] or \
                    not (FROZEN_DIR / fz["frozen_registry"][c["name"]]).exists():
                raise FreezeError(f"frozen registry mismatch for {c['name']}")
        for c in design.test_configs(key, fz["selection"]):
            if c not in [x for x in cfgs if x["name"] == c["name"]]:
                raise FreezeError(f"TEST config {c['name']} differs from the current design code")
    return fz


def write_report(fz: Dict):
    L = [f"# Freeze report", "", f"Frozen at {fz['frozen_at']} (prompt {fz['prompt_version']}, "
         f"embeddings {fz['embedding_model']}).", "", "## Selected settings (DEV micro-F1; ties -> smaller value)", "",
         "| Model | Dataset | Setting | Selected | DEV F1 |", "|---|---|---|---|---|"]
    for key, per_ds in fz["selection"].items():
        for ds, s in per_ds.items():
            for cond in SELECT[key]:
                L.append(f"| {key} | {ds} | {cond} {SELECT[key][cond]} | {s[cond]} | {s[cond + '_dev']['dev_f1']:.3f} |")
    L += ["", "## Validator thresholds (4B)", ""]
    for ds, v in fz["validators"].items():
        for c in ("E4", "E6"):
            L.append(f"- {ds} {c}: {v[c]['value']} (DEV F1 {v[c]['dev_f1']:.3f})")
    L += ["", "## EntityClass weights", "", "| Scheme | " + " | ".join(an.CRITERIA) + " |",
          "|---|" + "---|" * len(an.CRITERIA)]
    for name, w in fz["weights"].items():
        L.append(f"| {name} | " + " | ".join(f"{w[c]:.2f}" for c in an.CRITERIA) + " |")
    L += ["", f"W3 DEV AUROC {fz['w3_dev_auroc']:.3f}. W2: {'included' if fz['w2'] else 'not available (optional)'}.",
          f"Thresholds: pass {fz['thresholds']['pass_threshold']}, review {fz['thresholds']['review_threshold']}.",
          f"DEV validity rows: {fz['dev_validity_rows']['rows']}.", "", "## Runtime that TEST must match", ""]
    for key, rt in fz["runtime"].items():
        L.append(f"- {key}: {rt['hf_id']} @ {rt['revision'][:12]}, vLLM {rt['vllm_version']}, args {' '.join(rt['serve_args'])}")
    L += ["", "## TEST configurations", ""]
    for key, cfgs in fz["test_configs"].items():
        L.append(f"- {key}: " + ", ".join(c["name"] for c in cfgs))
    L += ["", "TEST has not been run. Start it only after approval: `python3 execution2.py --stage test`."]
    (FROZEN_DIR / "FREEZE_REPORT.md").write_text("\n".join(L) + "\n")
