"""Final analysis after TEST: every table and statistic of the paper, from frozen inputs only.

Writes results/analysis/:
  final_results.json             everything below, machine-readable
  tables/*.csv, tables/*.tex     classification, criteria, scorers, weights, ablation, strata, BERT,
                                 filtering, synthetic effects, corpus description
  figures/*.png                  reliability curves and criterion AUROC (if matplotlib is installed)
Nothing here is fitted on TEST: W3, B3, B4 and the isotonic maps come from the frozen DEV rows.
"""
import asyncio
import json
import pickle
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np

from experiments.data.adapters import BIOCsvAdapter, SFullAdapter
from experiments.data.model import normalize_mention
from experiments.eval.metrics import prf, sentence_counts
from experiments.eval.stats import approximate_randomization, holm, paired_bootstrap
from experiments.review import analysis as an
from experiments.review.report import block
from experiments.review.score import score_runs
from experiments.runner import Experiment
from experiments.schemas import get_schema
from pipeline import design
from pipeline.durable import atomic_write_json, read_jsonl
from pipeline.freeze import DEV_ROWS, FREEZE_FILE, verify_freeze
from pipeline.paths import ANALYSIS_DIR, FROZEN_DIR, ROOT
from pipeline.registry import QWEN_ORDER

N_BOOT_F1 = 10000
N_PERM = 10000
N_BOOT_AUROC = 2000
TABLES = ANALYSIS_DIR / "tables"
FIGURES = ANALYSIS_DIR / "figures"


class AnalysisError(RuntimeError):
    pass


# ---------------------------------------------------------------------------
# inputs

def test_runs(fz: Dict) -> Dict[Tuple[str, str, str], Experiment]:
    runs, pending = {}, []
    for key, cfgs in fz["test_configs"].items():
        for c in cfgs:
            e = Experiment(c)
            if not e.status()["state"].startswith("complete"):
                pending.append(c["name"])
            runs[(key, c["dataset"], c["condition"])] = e
    if pending:
        raise AnalysisError(f"{len(pending)} TEST runs are not complete (python3 execution2.py --stage test): {pending[:6]}")
    return runs


def sentence_level(e: Experiment):
    recs = sorted(e.records_for_evaluation(), key=lambda r: r["sid"])
    counts = [(c.tp, c.fp, c.fn) for c in
              (sentence_counts([tuple(x) for x in r["gold"]], [tuple(x) for x in r["pred"]]) for r in recs)]
    return [r["sid"] for r in recs], counts


def bootstrap_f1_ci(counts, n=N_BOOT_F1, seed=0):
    a = np.asarray(counts, dtype=np.int64)
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(a), size=(n, len(a)))
    s = a[idx].sum(axis=1)
    f = 2 * s[:, 0] / np.maximum(2 * s[:, 0] + s[:, 1] + s[:, 2], 1)
    return float(np.quantile(f, 0.025)), float(np.quantile(f, 0.975))


# ---------------------------------------------------------------------------
# A. classification

def classification(runs) -> List[Dict]:
    out = []
    for (key, ds, cond), e in sorted(runs.items()):
        m = json.loads((e.dir / "metrics.json").read_text())
        _, c = sentence_level(e)
        lo, hi = bootstrap_f1_ci(c)
        out.append({"model": key, "dataset": ds, "condition": cond, "precision": m["micro"]["precision"],
                    "recall": m["micro"]["recall"], "f1": m["micro"]["f1"], "f1_ci_low": lo, "f1_ci_high": hi,
                    "macro_f1": m["macro_f1"], "abandoned_sentences": m["run"]["n_abandoned_as_empty"],
                    "seen_unseen_recall": m.get("seen_unseen_recall")})
    return out


def f1_comparisons(runs, spec: Dict) -> Dict:
    out = {}
    for fam_name, fam in spec["families"].items():
        pairs = fam.get("f1_comparisons") or []
        if not pairs:
            continue
        res = {}
        for item in pairs:
            key, a, b = item["model"], item["a"], item["b"]
            for ds in design.DATASETS:
                if (key, ds, a) not in runs or (key, ds, b) not in runs:
                    continue
                ia, ca = sentence_level(runs[(key, ds, a)])
                ib, cb = sentence_level(runs[(key, ds, b)])
                if ia != ib:
                    raise AnalysisError(f"{key}/{ds} {a} vs {b}: different sentences")
                r = {"model": key, "dataset": ds, "a": a, "b": b, **paired_bootstrap(ca, cb, N_BOOT_F1)}
                if fam.get("tested"):
                    r.update(approximate_randomization(ca, cb, N_PERM))
                res[f"{key}:{ds}:{b}-{a}"] = r
        if fam.get("tested") and res:
            adj = holm({k: v["p_value"] for k, v in res.items()})
            for k in res:
                res[k]["p_holm"], res[k]["reject_holm_0.05"] = adj[k]["p_holm"], adj[k]["reject"]
        out[fam_name] = res
    return out


# ---------------------------------------------------------------------------
# B. EntityClass validity

def auroc_p(score, y, g, n=N_BOOT_AUROC, seed=0):
    """Two-sided sentence-bootstrap p-value for AUROC = 0.5."""
    idx = an._group_index(g)
    rng = np.random.default_rng(seed)
    vals = []
    for _ in range(n):
        rows = np.concatenate([idx[i] for i in rng.integers(0, len(idx), len(idx))])
        v = an.auroc(score[rows], y[rows])
        if v is not None:
            vals.append(v)
    vals = np.array(vals)
    return float(min(1.0, 2 * min((vals <= 0.5).mean(), (vals >= 0.5).mean())))


def learned_match(dev_rows, eval_rows) -> Dict:
    """The frozen pickles must reproduce the deterministic refit used inside the report."""
    fz = json.loads(FREEZE_FILE.read_text())
    out = {}
    for name, fit, bert in (("B3_logistic", an.fit_b3, True), ("B4_gbt", an.fit_b4, True),
                            ("B3_logistic_nobert", an.fit_b3, False), ("B4_gbt_nobert", an.fit_b4, False)):
        with open(ROOT / fz["learned_scorers"][name]["path"], "rb") as f:
            frozen = pickle.load(f)
        x = an.criterion_matrix(eval_rows, bert)
        refit = fit(an.criterion_matrix(dev_rows, bert), an.labels(dev_rows))
        out[name] = bool(np.allclose(frozen.predict_proba(x)[:, 1], refit.predict_proba(x)[:, 1]))
    if not all(out.values()):
        raise AnalysisError(f"frozen learned scorers are not reproduced: {out}")
    return out


def sentence_correlations(rows: List[Dict], runs_by_name: Dict[str, Experiment]) -> Dict:
    from scipy.stats import spearmanr
    x = an.criterion_matrix(rows)
    w0 = an.overall(x, an.W0)
    by_sent = defaultdict(list)
    comp = defaultdict(list)
    for r, s, c in zip(rows, w0, x[:, an.CRITERIA.index("completeness")]):
        by_sent[(r["run"], r["sid"])].append(s)
        comp[(r["run"], r["sid"])].append(c)
    f1s, fns, mean_s, min_s, share_pass, comp_m = [], [], [], [], [], []
    counts = {}
    for run in {k[0] for k in by_sent}:
        e = runs_by_name[run]
        for rec in e.records_for_evaluation():
            c = sentence_counts([tuple(v) for v in rec["gold"]], [tuple(v) for v in rec["pred"]])
            counts[(run, rec["sid"])] = c
    for k, scores in by_sent.items():
        c = counts[k]
        f1s.append(prf(c.tp, c.fp, c.fn)["f1"])
        fns.append(c.fn)
        mean_s.append(float(np.mean(scores)))
        min_s.append(float(np.min(scores)))
        share_pass.append(float(np.mean(np.array(scores) >= 0.75)))
        comp_m.append(float(np.mean(comp[k])))

    def rho(a, b):
        r = spearmanr(a, b)
        return {"rho": float(r.statistic), "p": float(r.pvalue), "n": len(a)}
    return {"mean_W0_vs_sentence_F1": rho(mean_s, f1s), "min_W0_vs_sentence_F1": rho(min_s, f1s),
            "share_passed_vs_sentence_F1": rho(share_pass, f1s),
            "mean_completeness_vs_sentence_FN": rho(comp_m, fns),
            "note": "sentences with at least one predicted span"}


def validity(runs, fz, n_boot=N_BOOT_AUROC) -> Dict:
    dev_rows = read_jsonl(DEV_ROWS)
    schemes = fz["weights"]
    primary = [e for (key, ds, cond), e in runs.items() if cond in design.PRIMARY_VALIDITY_CONDITIONS]
    rows = an.load_rows([e.dir for e in primary])
    rows_unaligned = an.load_rows([e.dir for e in primary], include_unaligned=True)
    gold = lambda sel: sum(len(r["gold"]) for e in primary if e.dir.name in {x["run"] for x in sel}
                           for r in e.records_for_evaluation())
    out = {"learned_scorers_reproduced": learned_match(dev_rows, rows),
           "pooled": block(rows, dev_rows, schemes, gold(rows), n_boot)}
    for key in QWEN_ORDER:
        sub = [r for r in rows if r["model"] == {"4b": "small", "9b": "medium", "27b": "large"}[key]]
        out.setdefault("by_model", {})[key] = block(sub, dev_rows, schemes, gold(sub), n_boot)
    for ds in design.DATASETS:
        sub = [r for r in rows if r["dataset"] == ds]
        out.setdefault("by_dataset", {})[ds] = block(sub, dev_rows, schemes, gold(sub), 0)
    out["sensitivity_including_unaligned"] = block(rows_unaligned, dev_rows, schemes, gold(rows_unaligned), 0)
    x, y, g = an.criterion_matrix(rows), an.labels(rows), an.groups(rows)
    crit = {c: auroc_p(x[:, j], y, g) for j, c in enumerate(an.CRITERIA)}
    adj = holm(crit)
    out["RQ1_criterion_tests"] = {c: {"auroc": an.auroc(x[:, j], y), "p": crit[c], "p_holm": adj[c]["p_holm"],
                                      "reject_holm_0.05": adj[c]["reject"]} for j, c in enumerate(an.CRITERIA)}
    sc = out["pooled"]["scorers_with_bert"]["scorers"]
    rq2 = {f"W0_vs_{b}": sc[b]["auroc_minus_W0"] for b in ("B0_confidence", "B1_bert_agreement",
                                                          "B2_seen_in_train", "B3_logistic", "B4_gbt")}
    rq3 = {f"W0_vs_{w}": sc[w]["auroc_minus_W0"] for w in schemes if w != "W0"}
    s_w3 = an.overall(x, schemes["W3"])
    fx, fy = an.criterion_matrix(dev_rows), an.labels(dev_rows)
    for b, fit in (("B3_logistic", an.fit_b3), ("B4_gbt", an.fit_b4)):
        rq3[f"W3_vs_{b}"] = an.paired_auroc_difference(s_w3, fit(fx, fy).predict_proba(x)[:, 1], y, g, n_boot)
    for fam, res in (("RQ2", rq2), ("RQ3", rq3)):
        adj = holm({k: v["p"] for k, v in res.items()})
        for k in res:
            res[k]["p_holm"], res[k]["reject_holm_0.05"] = adj[k]["p_holm"], adj[k]["reject"]
        out[f"{fam}_paired_auroc"] = res
    out["sentence_level"] = sentence_correlations(rows, {e.dir.name: e for e in primary})
    out["_rows"] = rows
    return out


# ---------------------------------------------------------------------------
# C. RQ5: synthetic data and the scorecard

RQ5_PAIRS = [("4b", "E1", "E2"), ("4b", "E1", "E3"), ("4b", "E1", "E2c"), ("4b", "E2c", "E2"), ("9b", "E1", "E2")]


def _rq5_arrays(rows: List[Dict]):
    x, y = an.criterion_matrix(rows), an.labels(rows)
    s = an.overall(x, an.W0)
    d = an.decide(s, x[:, an.CRITERIA.index("constraint")], np.array([r["type_valid"] for r in rows], bool))
    return s, y.astype(bool), (d == "passed")


def _rq5_stats(s, y, passed, gold_n):
    n_inc, n_cor = int((~y).sum()), int(y.sum())
    kept_tp = int((passed & y).sum())
    p = kept_tp / passed.sum() if passed.sum() else 0.0
    r = kept_tp / gold_n if gold_n else 0.0
    return {"auroc": an.auroc(s, y.astype(int)),
            "false_acceptance": float((passed & ~y).sum() / n_inc) if n_inc else None,
            "false_rejection": float((~passed & y).sum() / n_cor) if n_cor else None,
            "filtered_f1": 2 * p * r / (p + r) if p + r else 0.0}


def rq5(runs, n_boot=N_BOOT_AUROC) -> Dict:
    out = {}
    for key, a, b in RQ5_PAIRS:
        for ds in design.DATASETS + ["pooled"]:
            dss = design.DATASETS if ds == "pooled" else [ds]
            ra = an.load_rows([runs[(key, d, a)].dir for d in dss])
            rb = an.load_rows([runs[(key, d, b)].dir for d in dss])
            gold_by_sent = {(d, r["sid"]): len(r["gold"]) for d in dss
                            for r in runs[(key, d, a)].records_for_evaluation()}
            arr_a, arr_b = _rq5_arrays(ra), _rq5_arrays(rb)
            sa = dict(_rq5_stats(*arr_a, sum(gold_by_sent.values())), summary=an.score_summary(ra))
            sb = dict(_rq5_stats(*arr_b, sum(gold_by_sent.values())), summary=an.score_summary(rb))
            sents = sorted(gold_by_sent)
            ia, ib = defaultdict(list), defaultdict(list)
            for i, r in enumerate(ra):
                ia[(r["dataset"], r["sid"])].append(i)
            for i, r in enumerate(rb):
                ib[(r["dataset"], r["sid"])].append(i)
            rng = np.random.default_rng(0)
            diffs = defaultdict(list)
            for _ in range(n_boot):
                pick = [sents[i] for i in rng.integers(0, len(sents), len(sents))]
                ja = np.array([j for s_ in pick for j in ia.get(s_, [])], dtype=int)
                jb = np.array([j for s_ in pick for j in ib.get(s_, [])], dtype=int)
                g = sum(gold_by_sent[s_] for s_ in pick)
                xa = _rq5_stats(*(v[ja] for v in arr_a), g)
                xb = _rq5_stats(*(v[jb] for v in arr_b), g)
                for m in ("auroc", "false_acceptance", "false_rejection", "filtered_f1"):
                    if xa[m] is not None and xb[m] is not None:
                        diffs[m].append(xb[m] - xa[m])
            out[f"{key}:{ds}:{b}-{a}"] = {
                "a": sa, "b": sb,
                "differences": {m: {"delta": (sb[m] - sa[m]) if sa[m] is not None and sb[m] is not None else None,
                                    "ci_low": float(np.quantile(v, 0.025)), "ci_high": float(np.quantile(v, 0.975))}
                                for m, v in diffs.items() if v}}
    return out


# ---------------------------------------------------------------------------
# D. RQ6: the original synthetic corpora

def _token_offsets(tokens):
    offs, pos = [], 0
    for t in tokens:
        offs.append((pos, pos + len(t)))
        pos += len(t) + 1
    return offs


def _char_to_token_span(offs, start, end):
    idx = [i for i, (a, b) in enumerate(offs) if a < end and start < b]
    return (idx[0], idx[-1] + 1) if idx else None


def corpus_description(bert_service=None) -> Dict:
    from experiments.annotation import silver_records
    out = {}
    for ds in design.DATASETS:
        schema = get_schema(ds)
        ad = BIOCsvAdapter(schema)
        train_lex = defaultdict(Counter)
        for s in ad.load("train"):
            for text, t in s.mentions():
                train_lex[normalize_mention(text)][t] += 1
        test = ad.load("test")
        test_lex = {normalize_mention(m) for s in test for m, _ in s.mentions()}
        dev_lex = {normalize_mention(m) for s in ad.load("dev") for m, _ in s.mentions()}
        test_only = {m for m in test_lex - set(train_lex) - dev_lex if len(m) >= 5 and any(c.isalpha() for c in m)}
        rows = SFullAdapter(schema).load()
        silver = silver_records(ds, "original")
        control = silver_records(ds, "control")
        mentions = [(" ".join(r["tokens"][a:b]), t) for r in silver for a, b, t in r["spans"]]
        surf = [normalize_mention(m) for m, _ in mentions]
        d = {"rows": len(rows), "unique_sentences": len({" ".join(r.provenance['raw_sentence'].split()) for r in rows}),
             "annotated_sentences": len(silver), "silver_mentions": len(mentions),
             "mentions_per_sentence": len(mentions) / len(silver) if silver else None,
             "type_distribution": dict(Counter(t for _, t in mentions)),
             "requested_domain_satisfied": float(np.mean([r["domain_satisfied"] for r in silver])) if silver else None,
             "novel_mentions_vs_train": float(np.mean([s not in train_lex for s in surf])) if surf else None,
             "distinct_mentions": len(set(surf)),
             "distinct_novel_mentions": len(set(surf) - set(train_lex)),
             "span_sources": dict(Counter(v for r in silver for v in r["sources"].values())),
             "exposure": {"sentences_with_test_only_mention": float(np.mean([any(m in " ".join(r["tokens"]).lower()
                                                                                 for m in test_only) for r in silver]))
                          if silver and test_only else None,
                          "test_mentions_present_in_synthetic_silver": float(np.mean([m in set(surf) for m in test_lex]))
                          if test_lex else None,
                          "note": "TEST-only = gold mention in TEST, never in TRAIN or DEV (length >= 5, alphabetic)"}}
        if control:
            tp = fp = fn = 0
            for r in control:
                g, p = {tuple(x) for x in r["gold"]}, {tuple(x) for x in r["spans"]}
                tp, fp, fn = tp + len(g & p), fp + len(p - g), fn + len(g - p)
            d["silver_quality_on_train_control"] = dict(prf(tp, fp, fn), n_sentences=len(control))
            ag = [r["agreement"] for r in control]
            d["annotator_gazetteer_agreement_control"] = {
                "gazetteer_spans": sum(a["gazetteer_spans"] for a in ag),
                "found_by_annotator": sum(a["annotator_found_gazetteer"] for a in ag)}
        if bert_service is not None and silver:
            from experiments.bert_validator import select_benchmark_bert
            name = select_benchmark_bert(ds, bert_service)
            tp = fp = fn = 0
            for r in silver:
                offs = _token_offsets(r["tokens"])
                ents, _ = bert_service.classify(" ".join(r["tokens"]), name)
                b = set()
                for e in ents:
                    sp = _char_to_token_span(offs, e["start_pos"], e["end_pos"])
                    if sp:
                        b.add((sp[0], sp[1], e["type"]))
                s_ = {tuple(x) for x in r["spans"]}
                tp, fp, fn = tp + len(b & s_), fp + len(b - s_), fn + len(s_ - b)
            d["bert_vs_silver"] = dict(prf(tp, fp, fn), note="silver spans as reference; exact span and type")
        out[ds] = d
    return out


def entityclass_on_silver(bert_service=None) -> Dict:
    """EntityClass scores of the silver entities of the original synthetic corpora (descriptive)."""
    from experiments.annotation import silver_records
    from experiments.review.benchmark import BenchmarkKG, build_reviewer
    out = {}
    for ds in design.DATASETS:
        schema = get_schema(ds)
        reviewer = build_reviewer(schema.name, bert_service=bert_service, kg=BenchmarkKG(schema))
        scores, decisions = [], Counter()

        async def go():
            for r in silver_records(ds, "original"):
                ents = {(str(e.get("text", "")).strip(), e.get("type")): e
                        for e in (r["annotator"].get("entities") or [])}
                for a, b, t in r["spans"]:
                    text = " ".join(r["tokens"][a:b])
                    e = ents.get((text, t), {})
                    conf = e.get("confidence") if isinstance(e.get("confidence"), (int, float)) else None
                    res = await reviewer.evaluate_entity(text, t, e.get("normalized_form"), " ".join(r["tokens"]),
                                                         conf, "llm", run_bert_validation=bert_service is not None)
                    scores.append([res[c].score if res[c] is not None else np.nan for c in an.CRITERIA]
                                  + [res["overall_score"]])
                    decisions[res["review_status"]] += 1
        asyncio.run(go())
        arr = np.array(scores) if scores else np.zeros((0, 6))
        out[ds] = {"entities": len(scores), "decisions": dict(decisions),
                   "mean": {c: float(np.nanmean(arr[:, j])) for j, c in enumerate(list(an.CRITERIA) + ["overall"])}
                   if len(arr) else {}}
    return out


def exposure_recall(runs) -> Dict:
    """TEST gold recall split by: seen in TRAIN / exposed (only in synthetic silver) / unseen; E1 vs E2."""
    from experiments.annotation import silver_records
    out = {}
    for key, conds in (("4b", ("E1", "E2", "E3")), ("9b", ("E1", "E2"))):
        for ds in design.DATASETS:
            train = {normalize_mention(m) for s in BIOCsvAdapter(get_schema(ds)).load("train") for m, _ in s.mentions()}
            syn = {normalize_mention(" ".join(r["tokens"][a:b])) for r in silver_records(ds, "original")
                   for a, b, _ in r["spans"]}
            for cond in conds:
                hit, tot = Counter(), Counter()
                for rec in runs[(key, ds, cond)].records_for_evaluation():
                    pred = {tuple(x) for x in rec["pred"]}
                    for a, b, t in rec["gold"]:
                        m = normalize_mention(" ".join(rec["tokens"][a:b]))
                        g = "seen_in_train" if m in train else ("exposed_synthetic_only" if m in syn else "unseen")
                        tot[g] += 1
                        hit[g] += (a, b, t) in pred
                out[f"{key}:{ds}:{cond}"] = {g: {"recall": hit[g] / tot[g] if tot[g] else None, "gold": tot[g]}
                                             for g in ("seen_in_train", "exposed_synthetic_only", "unseen")}
    return out


# ---------------------------------------------------------------------------
# E. tables and figures

def write_table(name: str, rows: List[Dict], cols: Optional[List[str]] = None, caption: str = ""):
    TABLES.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    cols = cols or list(rows[0])
    with open(TABLES / f"{name}.csv", "w", encoding="utf-8") as f:
        f.write(",".join(cols) + "\n")
        for r in rows:
            f.write(",".join("" if r.get(c) is None else (f"{r[c]:.4f}" if isinstance(r[c], float) else str(r[c]))
                             for c in cols) + "\n")

    def tex(v):
        if v is None:
            return "--"
        if isinstance(v, float):
            return f"{v:.3f}"
        return str(v).replace("_", r"\_").replace("%", r"\%")
    L = [r"\begin{table}[t]", r"\centering", r"\small", r"\begin{tabular}{" + "l" * len(cols) + "}", r"\hline",
         " & ".join(tex(c) for c in cols) + r" \\", r"\hline"]
    L += [" & ".join(tex(r.get(c)) for c in cols) + r" \\" for r in rows]
    L += [r"\hline", r"\end{tabular}", rf"\caption{{{tex(caption or name)}}}", rf"\label{{tab:{name}}}", r"\end{table}"]
    (TABLES / f"{name}.tex").write_text("\n".join(L) + "\n")


def tables(res: Dict):
    write_table("classification", res["classification"],
                ["model", "dataset", "condition", "precision", "recall", "f1", "f1_ci_low", "f1_ci_high", "macro_f1",
                 "abandoned_sentences"], "Micro P/R/F1 on TEST with 95% sentence-bootstrap CI")
    v = res["validity"]
    write_table("criteria", [{"criterion": c, **{k: t[k] for k in ("auroc", "p", "p_holm")}}
                             for c, t in v["RQ1_criterion_tests"].items()], caption="Criterion AUROC (pooled)")
    for scope, blk in [("pooled", v["pooled"])] + [(f"model_{k}", b) for k, b in v["by_model"].items()]:
        sc = blk["scorers_with_bert"]["scorers"]
        write_table(f"scorers_{scope}", [{"scorer": n, "auroc": s["auroc"], "pr_auc": s["pr_auc"],
                                          "false_acceptance": (s.get("decision") or {}).get("false_acceptance"),
                                          "false_rejection": (s.get("decision") or {}).get("false_rejection"),
                                          "filtered_f1": (s.get("filtering") or {}).get("filtered", {}).get("f1")}
                                         for n, s in sc.items()], caption=f"Scorers ({scope})")
        write_table(f"ablation_{scope}", [{"variant": k, "auroc": a["auroc"], "pr_auc": a["pr_auc"],
                                           "false_acceptance": a["false_acceptance"],
                                           "false_rejection": a["false_rejection"],
                                           "filtered_f1": a["filtering"]["filtered"]["f1"]}
                                          for k, a in blk["ablation_W0"].items()], caption=f"Criterion ablation ({scope})")
        write_table(f"strata_{scope}", [{"stratum": k, **{m: s.get(m) for m in ("n", "n_correct", "auroc", "pr_auc",
                                                                                  "false_acceptance", "false_rejection")}}
                                        for k, s in blk["strata_W0"].items()], caption=f"Seen/unseen strata ({scope})")
        nb = blk["scorers_without_bert"]["scorers"]
        write_table(f"bert_{scope}", [{"scorer": n, "auroc_with_bert": sc[n]["auroc"], "auroc_without_bert": nb[n]["auroc"]}
                                      for n in sc if n in nb and n.startswith(("W", "B3", "B4"))],
                    caption=f"Consistency with and without BERT ({scope})")
    write_table("rq5_synthetic_scorecard", [{"comparison": k, **{f"d_{m}": d["delta"] for m, d in r["differences"].items()},
                                             **{f"{m}_ci": f"[{d['ci_low']:.3f}, {d['ci_high']:.3f}]"
                                                for m, d in r["differences"].items()}}
                                            for k, r in res["rq5"].items()], caption="Synthetic data and the scorecard")
    f1rows = [{"comparison": k, "delta_f1": r["delta"], "ci_low": r["ci_low"], "ci_high": r["ci_high"],
               "p": r.get("p_value"), "p_holm": r.get("p_holm")}
              for fam in res["f1_comparisons"].values() for k, r in fam.items()]
    write_table("f1_comparisons", f1rows, caption="Pre-registered F1 comparisons")
    write_table("synthetic_corpora", [{"dataset": ds, **{k: v for k, v in d.items() if not isinstance(v, dict)}}
                                      for ds, d in res["synthetic_corpora"].items()],
                caption="Original synthetic corpora (silver annotation)")


def figures(res: Dict):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception:
        print("[ANALYZE] matplotlib not installed: figures skipped (tables are complete)")
        return
    FIGURES.mkdir(parents=True, exist_ok=True)
    sc = res["validity"]["pooled"]["scorers_with_bert"]["scorers"]
    fig, ax = plt.subplots(figsize=(4.5, 4.5))
    for name in ("W0", "W3", "B4_gbt"):
        cal = sc[name].get("calibration_isotonic_from_dev") or sc[name].get("calibration")
        if cal:
            ax.plot([c["mean_score"] for c in cal["curve"]], [c["p_correct"] for c in cal["curve"]], "o-", label=name)
    ax.plot([0, 1], [0, 1], "k--", lw=0.8)
    ax.set_xlabel("predicted probability (isotonic map from DEV)")
    ax.set_ylabel("observed P(correct)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURES / "reliability_pooled.png", dpi=200)
    fig, ax = plt.subplots(figsize=(6, 3.5))
    keys = list(res["validity"]["by_model"])
    width = 0.8 / len(keys)
    for i, k in enumerate(keys):
        crit = res["validity"]["by_model"][k]["criteria_with_bert"]
        ax.bar(np.arange(len(an.CRITERIA)) + i * width, [crit[c]["auroc"] or 0 for c in an.CRITERIA], width, label=k)
    ax.axhline(0.5, color="k", lw=0.8, ls="--")
    ax.set_xticks(np.arange(len(an.CRITERIA)) + 0.4 - width / 2)
    ax.set_xticklabels(an.CRITERIA, rotation=20)
    ax.set_ylabel("AUROC")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURES / "criterion_auroc_by_model.png", dpi=200)


# ---------------------------------------------------------------------------

def analyze_stage(n_boot: int = N_BOOT_AUROC) -> Dict:
    fz = verify_freeze()
    runs = test_runs(fz)
    print(f"[ANALYZE] {len(runs)} TEST runs; scoring with EntityClass (resumes)")
    score_runs([e.dir for e in runs.values()])
    spec = json.loads((ROOT / fz["comparisons"]["path"]).read_text())
    from experiments.review.score import BERT_ROOT, CachedBert, best_device
    from services.bert_ner import BERTNERService
    bert = CachedBert(BERTNERService(models_dir=str(BERT_ROOT), device=best_device()))
    res = {"freeze": {"frozen_at": fz["frozen_at"], "sha256": (FROZEN_DIR / "freeze.json.sha256").read_text().strip()},
           "classification": classification(runs)}
    print("[ANALYZE] pre-registered F1 comparisons")
    res["f1_comparisons"] = f1_comparisons(runs, spec)
    print("[ANALYZE] EntityClass validity (RQ1-RQ4)")
    v = validity(runs, fz, n_boot)
    v.pop("_rows", None)
    res["validity"] = v
    print("[ANALYZE] synthetic data and the scorecard (RQ5)")
    res["rq5"] = rq5(runs, n_boot)
    print("[ANALYZE] original synthetic corpora (RQ6)")
    res["synthetic_corpora"] = corpus_description(bert)
    res["entityclass_on_silver"] = entityclass_on_silver(bert)
    res["exposure_recall"] = exposure_recall(runs)
    atomic_write_json(ANALYSIS_DIR / "final_results.json", res)
    tables(res)
    figures(res)
    print(f"[ANALYZE] done: {ANALYSIS_DIR / 'final_results.json'}, tables in {TABLES}, figures in {FIGURES}")
    return res
