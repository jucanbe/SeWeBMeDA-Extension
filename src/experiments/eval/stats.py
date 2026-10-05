"""Paired statistics over sentences for comparing two systems on the same TEST set.

Both procedures resample or permute at the sentence level, because predictions
within a sentence are dependent and every compared condition is evaluated on
the same sentences.
"""
from typing import Dict, List, Sequence, Tuple

import numpy as np

from experiments.eval.metrics import micro_f1_from_totals

Counts = Sequence[Tuple[int, int, int]]   # per sentence (tp, fp, fn)


def _f1(arr: np.ndarray) -> float:
    tp, fp, fn = arr.sum(axis=0)
    return micro_f1_from_totals(tp, fp, fn)


def _check(a: Counts, b: Counts):
    a, b = np.asarray(a, dtype=np.int64), np.asarray(b, dtype=np.int64)
    if a.shape != b.shape:
        raise ValueError("systems must be evaluated on the same sentences")
    return a, b


def paired_bootstrap(a: Counts, b: Counts, n: int = 10000, seed: int = 0, alpha: float = 0.05) -> Dict:
    """95% CI of micro-F1(B) - micro-F1(A) by resampling sentences with replacement."""
    a, b = _check(a, b)
    rng = np.random.default_rng(seed)
    m = len(a)
    idx = rng.integers(0, m, size=(n, m))
    sa = a[idx].sum(axis=1)             # (n, 3)
    sb = b[idx].sum(axis=1)
    fa = 2 * sa[:, 0] / np.maximum(2 * sa[:, 0] + sa[:, 1] + sa[:, 2], 1)
    fb = 2 * sb[:, 0] / np.maximum(2 * sb[:, 0] + sb[:, 1] + sb[:, 2], 1)
    d = fb - fa
    return {"delta": _f1(b) - _f1(a), "ci_low": float(np.quantile(d, alpha / 2)),
            "ci_high": float(np.quantile(d, 1 - alpha / 2)), "n_resamples": n, "seed": seed}


def approximate_randomization(a: Counts, b: Counts, n: int = 10000, seed: int = 0) -> Dict:
    """Two-sided p-value for H0: A and B are exchangeable, swapping per-sentence outputs.

    p = (#{|delta_perm| >= |delta_obs|} + 1) / (n + 1)   (Noreen 1989; Yeh 2000)
    """
    a, b = _check(a, b)
    rng = np.random.default_rng(seed)
    obs = abs(_f1(b) - _f1(a))
    swap = rng.random((n, len(a))) < 0.5            # (n, m)
    ta = np.where(swap[..., None], b[None], a[None]).sum(axis=1)
    tb = np.where(swap[..., None], a[None], b[None]).sum(axis=1)
    fa = 2 * ta[:, 0] / np.maximum(2 * ta[:, 0] + ta[:, 1] + ta[:, 2], 1)
    fb = 2 * tb[:, 0] / np.maximum(2 * tb[:, 0] + tb[:, 1] + tb[:, 2], 1)
    extreme = int((np.abs(fb - fa) >= obs - 1e-12).sum())
    return {"delta_abs": obs, "p_value": (extreme + 1) / (n + 1), "n_permutations": n, "seed": seed}


def _f1_rows(sums: np.ndarray) -> np.ndarray:
    return 2 * sums[:, 0] / np.maximum(2 * sums[:, 0] + sums[:, 1] + sums[:, 2], 1)


def bootstrap_difference_of_differences(a1: Counts, b1: Counts, a2: Counts, b2: Counts, n: int = 10000,
                                        seed: int = 0, alpha: float = 0.05) -> Dict:
    """CI of [F1(b1) - F1(a1)] - [F1(b2) - F1(a2)], all four systems on the same sentences."""
    arrs = [np.asarray(x, dtype=np.int64) for x in (a1, b1, a2, b2)]
    if len({x.shape for x in arrs}) != 1:
        raise ValueError("all systems must be evaluated on the same sentences")
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(arrs[0]), size=(n, len(arrs[0])))
    f = [_f1_rows(x[idx].sum(axis=1)) for x in arrs]
    d = (f[1] - f[0]) - (f[3] - f[2])
    point = (_f1(arrs[1]) - _f1(arrs[0])) - (_f1(arrs[3]) - _f1(arrs[2]))
    return {"delta": point, "ci_low": float(np.quantile(d, alpha / 2)), "ci_high": float(np.quantile(d, 1 - alpha / 2)),
            "p_two_sided_bootstrap": float(min(1.0, 2 * min((d <= 0).mean(), (d >= 0).mean()))),
            "n_resamples": n, "seed": seed}


def holm(pvalues: Dict[str, float], alpha: float = 0.05) -> Dict[str, Dict]:
    """Holm-Bonferroni step-down adjustment within one family of comparisons."""
    items = sorted(pvalues.items(), key=lambda kv: kv[1])
    m = len(items)
    out, running = {}, 0.0
    for i, (name, p) in enumerate(items):
        adj = min(1.0, max(running, (m - i) * p))
        running = adj
        out[name] = {"p": p, "p_holm": adj, "reject": adj <= alpha}
    return out


def gap_closed(f1_small_base: float, f1_small_aug: float, f1_large_base: float) -> float:
    """Fraction of the small-to-large gap closed by augmentation (can be <0 or >1)."""
    gap = f1_large_base - f1_small_base
    return (f1_small_aug - f1_small_base) / gap if gap else float("nan")
