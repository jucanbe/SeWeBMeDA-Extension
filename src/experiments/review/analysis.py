"""Validity analysis of EntityClass scores against gold correctness.

Input: the per-span rows written by experiments.review.score (entityclass.jsonl).
Everything here is computed after scoring; gold never enters a score.

Scorers
  W0..W3   EntityClass overall under a weight vector (same formula as the reviewer)
  B0       classifier-reported confidence alone
  B1       BERT agreement alone
  B2       surface seen in TRAIN with the same type (0/1)
  B3       logistic regression over the five criteria   (fitted on DEV)
  B4       gradient-boosted trees over the five criteria (fitted on DEV)

Statistics resample sentences, not entities (entities of a sentence are dependent).
"""
import itertools
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np

from experiments.data.adapters import load_jsonl
from models.review_defaults import ENTITY_WEIGHTS, THRESHOLDS

CRITERIA = ("congruence", "coverage", "constraint", "completeness", "consistency")
W0 = dict(ENTITY_WEIGHTS)
W1 = {c: 0.2 for c in CRITERIA}
STRATA = ("A_seen_same_type", "B_seen_other_type", "C_unseen")
ERROR_LABELS = ("correct", "type_error", "boundary_error", "boundary_type_error", "spurious")
MIN_CLASS_N = 30          # a cell needs this many correct and this many incorrect rows to get metrics
B4_PARAMS = dict(max_depth=3, n_estimators=200, learning_rate=0.05, random_state=0)


# ---------------------------------------------------------------------------
# data

def load_rows(run_dirs: Iterable[Path], include_unaligned: bool = False) -> List[Dict]:
    rows = []
    for d in run_dirs:
        for r in load_jsonl(Path(d) / "entityclass.jsonl"):
            if r["label"] == "unaligned" and not include_unaligned:
                continue
            rows.append(r)
    return rows


def criterion_matrix(rows: Sequence[Dict], bert: bool = True) -> np.ndarray:
    """Rows x five criteria. bert=False uses Consistency computed without the BERT cross-check."""
    x = np.array([[r["scores"][c] for c in CRITERIA] for r in rows], dtype=float)
    if not bert:
        x[:, CRITERIA.index("consistency")] = [r.get("consistency_no_bert", r["scores"]["consistency"]) for r in rows]
    return x


def labels(rows: Sequence[Dict]) -> np.ndarray:
    return np.array([r["correct"] for r in rows], dtype=int)


def groups(rows: Sequence[Dict]) -> np.ndarray:
    """Sentence identity (run + sentence), the resampling unit."""
    return np.array([f'{r["run"]}|{r["sid"]}' for r in rows])


# ---------------------------------------------------------------------------
# EntityClass overall and decision (identical to services/entity_reviewer.py)

def overall(x: np.ndarray, weights: Dict[str, float], drop: Sequence[str] = ()) -> np.ndarray:
    """Weighted mean over the assessed criteria with renormalised weights, rounded to 3 decimals.

    Computed row by row with the reviewer's own arithmetic so that values at a
    rounding boundary are identical to EntityReviewService._calculate_overall_score.
    """
    kept = [(j, weights[c]) for j, c in enumerate(CRITERIA) if c not in drop]
    total = sum(w for _, w in kept)
    if total <= 0:
        return np.zeros(len(x))
    rows = np.asarray(x, dtype=float).tolist()
    return np.array([round(max(0.0, min(1.0, sum(w * r[j] for j, w in kept) / total)), 3) for r in rows])


def decide(overall_score: np.ndarray, constraint: np.ndarray, type_valid: np.ndarray,
           thresholds: Dict[str, float] = THRESHOLDS) -> np.ndarray:
    """passed / needs_review / failed, as the reviewer decides."""
    out = np.where(overall_score >= thresholds["pass_threshold"], "passed",
                   np.where(overall_score >= thresholds["review_threshold"], "needs_review", "failed")).astype(object)
    out[(constraint < 0.4) | (~type_valid)] = "failed"
    return out


# ---------------------------------------------------------------------------
# baselines

def b0_confidence(rows: Sequence[Dict]) -> np.ndarray:
    return np.array([r["confidence"] if r["confidence"] is not None else 0.5 for r in rows], dtype=float)


def b1_bert(rows: Sequence[Dict]) -> np.ndarray:
    """+p when BERT predicts the same type, -p when it predicts another type, 0 when it abstains."""
    out = []
    for r in rows:
        p = r.get("bert_p") or 0.0
        out.append(p if r["bert_agreement"] is True else -p if r["bert_agreement"] is False else 0.0)
    return np.array(out, dtype=float)


def b2_seen(rows: Sequence[Dict]) -> np.ndarray:
    return np.array([1.0 if r["stratum"] == "A_seen_same_type" else 0.0 for r in rows])


def fit_b3(x: np.ndarray, y: np.ndarray):
    from sklearn.linear_model import LogisticRegression
    return LogisticRegression(C=1.0, max_iter=1000).fit(x, y)


def fit_b4(x: np.ndarray, y: np.ndarray):
    from sklearn.ensemble import GradientBoostingClassifier
    return GradientBoostingClassifier(**B4_PARAMS).fit(x, y)


def grouped_oof(fit: Callable, x: np.ndarray, y: np.ndarray, g: np.ndarray, folds: int = 5) -> np.ndarray:
    """Out-of-fold probabilities with sentences kept together (DEV-only estimate of a learned scorer)."""
    from sklearn.model_selection import GroupKFold
    out = np.zeros(len(y))
    for tr, te in GroupKFold(n_splits=folds).split(x, y, g):
        out[te] = fit(x[tr], y[tr]).predict_proba(x[te])[:, 1]
    return out


# ---------------------------------------------------------------------------
# metrics

def auroc(score: np.ndarray, y: np.ndarray) -> Optional[float]:
    """Probability that a correct row outranks an incorrect one (ties count 1/2); vectorised ranks."""
    from scipy.stats import rankdata
    y = np.asarray(y)
    n1 = int(y.sum())
    n0 = int(len(y) - n1)
    if n1 == 0 or n0 == 0:
        return None
    ranks = rankdata(np.asarray(score, dtype=float))
    return float((ranks[y == 1].sum() - n1 * (n1 + 1) / 2.0) / (n1 * n0))


def pr_auc(score: np.ndarray, y: np.ndarray) -> Optional[float]:
    """Average precision for the class 'correct' (ties handled per distinct threshold)."""
    y = np.asarray(y)
    if y.sum() == 0:
        return None
    s = np.asarray(score, dtype=float)
    ap, tp, n, prev_recall = 0.0, 0, 0, 0.0
    for t in np.unique(s)[::-1]:
        m = s == t
        tp += int(y[m].sum())
        n += int(m.sum())
        recall = tp / y.sum()
        ap += (recall - prev_recall) * (tp / n)
        prev_recall = recall
    return float(ap)


def decision_metrics(decision: np.ndarray, y: np.ndarray) -> Dict:
    y = np.asarray(y).astype(bool)
    passed = decision == "passed"
    failed = decision == "failed"

    def rate(num, den):
        return float(num / den) if den else None
    return {
        "n": int(len(y)), "share_passed": rate(passed.sum(), len(y)), "share_failed": rate(failed.sum(), len(y)),
        "p_correct_given_passed": rate((passed & y).sum(), passed.sum()),
        "p_correct_given_not_passed": rate((~passed & y).sum(), (~passed).sum()),
        "false_acceptance": rate((passed & ~y).sum(), (~y).sum()),        # P(passed | incorrect)
        "false_rejection": rate((~passed & y).sum(), y.sum()),            # P(not passed | correct)
        "p_incorrect_given_failed": rate((failed & ~y).sum(), failed.sum()),
    }


def filtering(keep: np.ndarray, y: np.ndarray, total_gold: int) -> Dict:
    """P/R/F1 of the predictions kept by a filter, against all gold mentions of the evaluated sentences."""
    y = np.asarray(y).astype(bool)
    keep = np.asarray(keep).astype(bool)

    def prf(tp, n_pred):
        p = tp / n_pred if n_pred else 0.0
        r = tp / total_gold if total_gold else 0.0
        return {"precision": p, "recall": r, "f1": 2 * p * r / (p + r) if p + r else 0.0, "kept": int(n_pred)}
    return {"unfiltered": prf(int(y.sum()), len(y)), "filtered": prf(int((keep & y).sum()), int(keep.sum()))}


def calibration(prob: np.ndarray, y: np.ndarray, bins: int = 10) -> Dict:
    prob, y = np.asarray(prob, dtype=float), np.asarray(y, dtype=float)
    edges = np.linspace(0, 1, bins + 1)
    idx = np.clip(np.digitize(prob, edges[1:-1]), 0, bins - 1)
    ece, curve = 0.0, []
    for b in range(bins):
        m = idx == b
        if m.any():
            ece += m.mean() * abs(prob[m].mean() - y[m].mean())
            curve.append({"bin": b, "n": int(m.sum()), "mean_score": float(prob[m].mean()),
                          "p_correct": float(y[m].mean())})
    return {"ece": float(ece), "brier": float(np.mean((prob - y) ** 2)), "curve": curve}


def fit_isotonic(score: np.ndarray, y: np.ndarray):
    from sklearn.isotonic import IsotonicRegression
    return IsotonicRegression(y_min=0.0, y_max=1.0, out_of_bounds="clip").fit(score, y)


def cliffs_delta(a: np.ndarray, b: np.ndarray) -> Optional[float]:
    """P(a > b) - P(a < b)."""
    if len(a) == 0 or len(b) == 0:
        return None
    y = np.r_[np.ones(len(a)), np.zeros(len(b))]
    return 2 * auroc(np.r_[a, b], y) - 1


def kruskal(samples: List[np.ndarray]) -> Optional[Dict]:
    from scipy.stats import kruskal as kw
    samples = [s for s in samples if len(s) > 0]
    if len(samples) < 2 or len({float(v) for s in samples for v in s}) < 2:
        return None
    h, p = kw(*samples)
    return {"H": float(h), "p": float(p), "groups": len(samples)}


# ---------------------------------------------------------------------------
# sentence-level bootstrap

def _group_index(g: np.ndarray) -> List[np.ndarray]:
    by = defaultdict(list)
    for i, k in enumerate(g):
        by[k].append(i)
    return [np.array(v) for v in by.values()]


def bootstrap_ci(stat: Callable[[np.ndarray], Optional[float]], g: np.ndarray, n: int = 2000, seed: int = 0,
                 alpha: float = 0.05) -> Optional[Dict]:
    """CI of stat(row indices) resampling sentences with replacement."""
    idx = _group_index(g)
    rng = np.random.default_rng(seed)
    vals = []
    for _ in range(n):
        pick = rng.integers(0, len(idx), len(idx))
        v = stat(np.concatenate([idx[i] for i in pick]))
        if v is not None:
            vals.append(v)
    if not vals:
        return None
    return {"ci_low": float(np.quantile(vals, alpha / 2)), "ci_high": float(np.quantile(vals, 1 - alpha / 2)),
            "n_resamples": len(vals)}


def paired_auroc_difference(a: np.ndarray, b: np.ndarray, y: np.ndarray, g: np.ndarray, n: int = 2000,
                            seed: int = 0) -> Dict:
    """AUROC(b) - AUROC(a) on the same rows, with a sentence-bootstrap CI and two-sided p-value."""
    idx = _group_index(g)
    rng = np.random.default_rng(seed)
    point = auroc(b, y) - auroc(a, y)
    diffs = []
    for _ in range(n):
        rows = np.concatenate([idx[i] for i in rng.integers(0, len(idx), len(idx))])
        ua, ub = auroc(a[rows], y[rows]), auroc(b[rows], y[rows])
        if ua is not None and ub is not None:
            diffs.append(ub - ua)
    diffs = np.array(diffs)
    p = 2 * min((diffs <= 0).mean(), (diffs >= 0).mean()) if len(diffs) else None
    return {"delta": float(point), "ci_low": float(np.quantile(diffs, 0.025)),
            "ci_high": float(np.quantile(diffs, 0.975)), "p": None if p is None else float(min(1.0, p))}


# ---------------------------------------------------------------------------
# W3: DEV-calibrated linear weights

def simplex_grid(step: float = 0.05, k: int = 5) -> Iterable[Tuple[float, ...]]:
    n = round(1 / step)
    for c in itertools.combinations(range(n + k - 1), k - 1):
        parts = [b - a - 1 for a, b in zip((-1,) + c, c + (n + k - 1,))]
        yield tuple(p * step for p in parts)


def calibrate_w3(x: np.ndarray, y: np.ndarray, step: float = 0.05) -> Dict:
    """Non-negative weights summing to 1 that maximise DEV AUROC; ties go to the vector closest to equal."""
    best, best_key = None, None
    for w in simplex_grid(step):
        wv = np.array(w)
        a = auroc(np.round(x @ wv, 3), y)      # vectorised; the frozen weights are then applied with overall()
        key = (round(a, 6), -float(np.abs(wv - 0.2).sum()))
        if best_key is None or key > best_key:
            best, best_key = w, key
    return {"weights": {c: round(float(v), 2) for c, v in zip(CRITERIA, best)}, "dev_auroc": best_key[0],
            "step": step, "objective": "pooled DEV AUROC of the overall score"}


# ---------------------------------------------------------------------------
# analyses

def _cell_ok(y: np.ndarray) -> bool:
    return y.sum() >= MIN_CLASS_N and (len(y) - y.sum()) >= MIN_CLASS_N


def discrimination(score: np.ndarray, y: np.ndarray, g: Optional[np.ndarray] = None, n_boot: int = 0) -> Dict:
    out = {"n": int(len(y)), "n_correct": int(y.sum()), "auroc": auroc(score, y), "pr_auc": pr_auc(score, y),
           "base_rate": float(y.mean()) if len(y) else None}
    if n_boot and g is not None and out["auroc"] is not None:
        out["auroc_ci"] = bootstrap_ci(lambda i: auroc(score[i], y[i]), g, n_boot)
    return out


def criterion_analysis(rows: Sequence[Dict], bert: bool = True, n_boot: int = 0) -> Dict:
    """Per criterion: discrimination, distribution by error type, Kruskal-Wallis, Cliff's delta vs correct."""
    x, y, g = criterion_matrix(rows, bert), labels(rows), groups(rows)
    lab = np.array([r["label"] for r in rows])
    out = {}
    for j, c in enumerate(CRITERIA):
        s = x[:, j]
        by_label = {l: s[lab == l] for l in ERROR_LABELS}
        out[c] = {
            **discrimination(s, y, g, n_boot),
            "constant": bool(np.unique(s).size == 1),
            "by_error_type": {l: {"n": int(len(v)), "mean": float(v.mean()) if len(v) else None,
                                  "median": float(np.median(v)) if len(v) else None} for l, v in by_label.items()},
            "kruskal_wallis": kruskal(list(by_label.values())),
            "cliffs_delta_correct_vs": {l: cliffs_delta(by_label["correct"], v) for l, v in by_label.items()
                                        if l != "correct" and len(v)},
        }
    return out


def ablation(rows: Sequence[Dict], weights: Dict[str, float], total_gold: int, bert: bool = True) -> Dict:
    x, y = criterion_matrix(rows, bert), labels(rows)
    constraint = x[:, CRITERIA.index("constraint")]
    type_valid = np.array([r["type_valid"] for r in rows], dtype=bool)
    out = {}
    for drop in [()] + [(c,) for c in CRITERIA]:
        s = overall(x, weights, drop)
        d = decide(s, constraint, type_valid)
        out["all" if not drop else f"minus_{drop[0]}"] = {
            "auroc": auroc(s, y), "pr_auc": pr_auc(s, y), **decision_metrics(d, y),
            "filtering": filtering(d == "passed", y, total_gold)}
    return out


def stratified(score: np.ndarray, rows: Sequence[Dict], decision: Optional[np.ndarray] = None) -> Dict:
    y = labels(rows)
    strata = np.array([r["stratum"] for r in rows])
    out = {}
    for s in STRATA:
        m = strata == s
        cell = {"n": int(m.sum()), "n_correct": int(y[m].sum()), "n_incorrect": int(m.sum() - y[m].sum())}
        if _cell_ok(y[m]):
            cell.update(auroc=auroc(score[m], y[m]), pr_auc=pr_auc(score[m], y[m]))
            if decision is not None:
                cell.update(decision_metrics(decision[m], y[m]))
        else:
            cell["note"] = f"fewer than {MIN_CLASS_N} correct or incorrect rows; counts only"
        out[s] = cell
    return out


def total_gold(run_dirs: Iterable[Path]) -> int:
    return sum(len(r["gold"]) for d in run_dirs for r in load_jsonl(Path(d) / "predictions.jsonl"))


def weight_schemes(extra: Optional[Dict[str, Dict[str, float]]] = None) -> Dict[str, Dict[str, float]]:
    schemes = {"W0": W0, "W1": W1}
    schemes.update(extra or {})
    return schemes


def compare_scorers(eval_rows: Sequence[Dict], fit_rows: Optional[Sequence[Dict]], schemes: Dict[str, Dict],
                    gold_n: int, bert: bool = True, n_boot: int = 0, reference: str = "W0") -> Dict:
    """All scorers on eval_rows. Learned scorers and isotonic maps are fitted on fit_rows (DEV).

    With fit_rows=None the learned scorers are estimated out-of-fold on eval_rows
    (grouped by sentence): a DEV-only dry run, labelled as such.
    """
    x, y, g = criterion_matrix(eval_rows, bert), labels(eval_rows), groups(eval_rows)
    constraint = x[:, CRITERIA.index("constraint")]
    type_valid = np.array([r["type_valid"] for r in eval_rows], dtype=bool)
    scores = {name: overall(x, w) for name, w in schemes.items()}
    scores["B0_confidence"] = b0_confidence(eval_rows)
    scores["B1_bert_agreement"] = b1_bert(eval_rows)
    scores["B2_seen_in_train"] = b2_seen(eval_rows)
    if fit_rows is None:
        mode = "out-of-fold on the evaluated rows (DEV dry run)"
        scores["B3_logistic"] = grouped_oof(fit_b3, x, y, g)
        scores["B4_gbt"] = grouped_oof(fit_b4, x, y, g)
        iso_x, iso_y = x, y
    else:
        mode = "fitted on DEV rows, applied unchanged"
        fx, fy = criterion_matrix(fit_rows, bert), labels(fit_rows)
        scores["B3_logistic"] = fit_b3(fx, fy).predict_proba(x)[:, 1]
        scores["B4_gbt"] = fit_b4(fx, fy).predict_proba(x)[:, 1]
        iso_x, iso_y = fx, fy
    out = {"learned_scorers": mode, "n": int(len(y)), "base_rate": float(y.mean()), "scorers": {}}
    for name, s in scores.items():
        cell = discrimination(s, y, g, n_boot)
        if name in schemes:
            d = decide(s, constraint, type_valid)
            cell.update(decision=decision_metrics(d, y), filtering=filtering(d == "passed", y, gold_n))
            if fit_rows is not None:
                iso = fit_isotonic(overall(iso_x, schemes[name]), iso_y)
                cell["calibration_isotonic_from_dev"] = calibration(iso.predict(s), y)
        elif name.startswith(("B3", "B4")):
            cell["calibration"] = calibration(s, y)
        if name != reference and n_boot:
            cell[f"auroc_minus_{reference}"] = paired_auroc_difference(scores[reference], s, y, g, n_boot)
        out["scorers"][name] = cell
    return out


def score_summary(rows: Sequence[Dict], weights: Dict[str, float] = W0, bert: bool = True) -> Dict:
    """Distribution of the overall score and of the decisions (for condition comparisons)."""
    x = criterion_matrix(rows, bert)
    s = overall(x, weights)
    d = decide(s, x[:, CRITERIA.index("constraint")], np.array([r["type_valid"] for r in rows], dtype=bool))
    q = np.quantile(s, [0.1, 0.25, 0.5, 0.75, 0.9]) if len(s) else [None] * 5
    return {"n": int(len(s)), "mean": float(s.mean()) if len(s) else None,
            "quantiles": dict(zip(["q10", "q25", "q50", "q75", "q90"], map(float, q))),
            "decisions": dict(Counter(d.tolist()))}
