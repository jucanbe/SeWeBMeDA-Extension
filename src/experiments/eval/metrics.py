"""Span-level NER evaluation.

Primary criterion: a predicted span is correct iff its token boundaries and its
type both equal a gold span (exact span + exact type).
"""
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

from experiments.data.model import Span, spans_to_bio, normalize_mention


def prf(tp: int, fp: int, fn: int) -> Dict[str, float]:
    p = tp / (tp + fp) if tp + fp else 0.0
    r = tp / (tp + fn) if tp + fn else 0.0
    f = 2 * p * r / (p + r) if p + r else 0.0
    return {"precision": p, "recall": r, "f1": f, "tp": tp, "fp": fp, "fn": fn}


@dataclass
class SentenceCounts:
    """Per-sentence counts; the unit for paired resampling."""
    tp: int
    fp: int
    fn: int
    per_type: Dict[str, Tuple[int, int, int]]


def sentence_counts(gold: Sequence[Span], pred: Sequence[Span]) -> SentenceCounts:
    g, p = set(map(tuple, gold)), set(map(tuple, pred))
    per_type = {}
    for t in {s[2] for s in g | p}:
        gt = {s for s in g if s[2] == t}
        pt = {s for s in p if s[2] == t}
        per_type[t] = (len(gt & pt), len(pt - gt), len(gt - pt))
    return SentenceCounts(len(g & p), len(p - g), len(g - p), per_type)


def aggregate(counts: Iterable[SentenceCounts], types: Sequence[str]) -> Dict:
    counts = list(counts)
    tp = sum(c.tp for c in counts)
    fp = sum(c.fp for c in counts)
    fn = sum(c.fn for c in counts)
    per_type = {}
    for t in types:
        ttp = sum(c.per_type.get(t, (0, 0, 0))[0] for c in counts)
        tfp = sum(c.per_type.get(t, (0, 0, 0))[1] for c in counts)
        tfn = sum(c.per_type.get(t, (0, 0, 0))[2] for c in counts)
        per_type[t] = prf(ttp, tfp, tfn)
        per_type[t]["support"] = ttp + tfn
    supported = [t for t in types if per_type[t]["support"] > 0]
    macro = sum(per_type[t]["f1"] for t in supported) / len(supported) if supported else 0.0
    out = {"micro": prf(tp, fp, fn), "macro_f1": macro, "macro_types": supported, "per_type": per_type,
           "n_sentences": len(counts)}
    return out


def micro_f1_from_totals(tp: float, fp: float, fn: float) -> float:
    denom = 2 * tp + fp + fn
    return 2 * tp / denom if denom else 0.0


def overlap_counts(gold: Sequence[Span], pred: Sequence[Span]) -> Tuple[int, int, int]:
    """Lenient matching: same type and overlapping tokens, one-to-one (greedy)."""
    used = set()
    tp = 0
    for ps, pe, pt in sorted(pred):
        for j, (gs, ge, gt) in enumerate(sorted(gold)):
            if j in used or gt != pt:
                continue
            if ps < ge and gs < pe:
                used.add(j)
                tp += 1
                break
    return tp, len(pred) - tp, len(gold) - tp


def token_counts(n_tokens: int, gold: Sequence[Span], pred: Sequence[Span]) -> Tuple[int, int, int]:
    """Token-level counts on entity tokens (type must match; B/I distinction ignored)."""
    g = [t[2:] if t != "O" else "O" for t in spans_to_bio(n_tokens, list(gold))]
    p = [t[2:] if t != "O" else "O" for t in spans_to_bio(n_tokens, list(pred))]
    tp = sum(1 for a, b in zip(g, p) if a != "O" and a == b)
    fp = sum(1 for a, b in zip(g, p) if b != "O" and a != b)
    fn = sum(1 for a, b in zip(g, p) if a != "O" and a != b)
    return tp, fp, fn


ERROR_KINDS = ("correct", "type_error", "boundary_error", "boundary_type_error", "spurious", "missed")


def error_taxonomy(gold: Sequence[Span], pred: Sequence[Span]) -> Counter:
    """Classify each prediction and each unmatched gold span (nervaluate-style)."""
    out = Counter()
    g, p = set(map(tuple, gold)), set(map(tuple, pred))
    exact = g & p
    out["correct"] += len(exact)
    g_left, p_left = g - exact, p - exact
    matched_gold = set()
    for ps, pe, pt in sorted(p_left):
        same_bounds = [x for x in g_left if x[0] == ps and x[1] == pe]
        overlap = [x for x in g_left if ps < x[1] and x[0] < pe]
        if same_bounds:
            out["type_error"] += 1
            matched_gold.add(same_bounds[0])
        elif any(x[2] == pt for x in overlap):
            out["boundary_error"] += 1
            matched_gold.add(next(x for x in overlap if x[2] == pt))
        elif overlap:
            out["boundary_type_error"] += 1
            matched_gold.add(overlap[0])
        else:
            out["spurious"] += 1
    out["missed"] += len(g_left - matched_gold)
    return out


def confusion(gold: Sequence[Span], pred: Sequence[Span]) -> Counter:
    """(gold_type, pred_type) counts for spans with identical boundaries; 'O' for missing."""
    c = Counter()
    gb = {(s, e): t for s, e, t in gold}
    pb = {(s, e): t for s, e, t in pred}
    for k in set(gb) | set(pb):
        c[(gb.get(k, "O"), pb.get(k, "O"))] += 1
    return c


def evaluate(records: List[Dict], types: Sequence[str], train_lexicon: Optional[Set[str]] = None) -> Dict:
    """records: dicts with tokens, gold (spans), pred (spans)."""
    counts, ov, tok, err, conf = [], [0, 0, 0], [0, 0, 0], Counter(), Counter()
    seen = {"seen": [0, 0], "unseen": [0, 0]}   # [tp, gold]
    for r in records:
        gold = [tuple(s) for s in r["gold"]]
        pred = [tuple(s) for s in r["pred"]]
        counts.append(sentence_counts(gold, pred))
        for i, v in enumerate(overlap_counts(gold, pred)):
            ov[i] += v
        for i, v in enumerate(token_counts(len(r["tokens"]), gold, pred)):
            tok[i] += v
        err += error_taxonomy(gold, pred)
        conf += confusion(gold, pred)
        if train_lexicon is not None:
            pset = set(pred)
            for s in gold:
                key = "seen" if normalize_mention(" ".join(r["tokens"][s[0]:s[1]])) in train_lexicon else "unseen"
                seen[key][1] += 1
                seen[key][0] += int(s in pset)
    out = aggregate(counts, types)
    out["overlap"] = prf(*ov)
    out["token"] = prf(*tok)
    out["errors"] = {k: err.get(k, 0) for k in ERROR_KINDS}
    out["confusion"] = {f"{g}->{p}": n for (g, p), n in sorted(conf.items())}
    if train_lexicon is not None:
        out["seen_unseen_recall"] = {k: {"recall": v[0] / v[1] if v[1] else 0.0, "gold": v[1]} for k, v in seen.items()}
    return out
