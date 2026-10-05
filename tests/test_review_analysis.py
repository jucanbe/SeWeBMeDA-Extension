"""EntityClass validity analysis: gold labelling, strata, metrics, weights, baselines,
and agreement of the analysis formulas with the real reviewer."""
import asyncio
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import numpy as np

from experiments.review import analysis as an
from experiments.review.score import entity_for_span, gold_label, train_stratum
from models.review_defaults import ENTITY_SETTINGS, ENTITY_WEIGHTS, THRESHOLDS
from services.entity_reviewer import EntityReviewService


def row(correct, scores, stratum="C_unseen", sid="s", label=None, conf=0.9, agree=None, p=None, type_valid=True):
    return {"run": "r", "sid": sid, "correct": correct, "label": label or ("correct" if correct else "spurious"),
            "scores": dict(zip(an.CRITERIA, scores)), "stratum": stratum, "confidence": conf,
            "bert_agreement": agree, "bert_p": p, "type_valid": type_valid}


class GoldLabelTests(unittest.TestCase):
    GOLD = [(0, 2, "Disease"), (5, 6, "Chemical")]

    def test_error_categories(self):
        self.assertEqual(gold_label((0, 2, "Disease"), self.GOLD), "correct")
        self.assertEqual(gold_label((0, 2, "Chemical"), self.GOLD), "type_error")
        self.assertEqual(gold_label((1, 2, "Disease"), self.GOLD), "boundary_error")
        self.assertEqual(gold_label((1, 3, "Chemical"), self.GOLD), "boundary_type_error")
        self.assertEqual(gold_label((3, 4, "Disease"), self.GOLD), "spurious")

    def test_strata(self):
        index = {"aspirin": {"types": {"Chemical": 3}}, "cold": {"types": {"Disease": 1}}, "the": {"types": {}}}
        self.assertEqual(train_stratum("Aspirin", "Chemical", index), "A_seen_same_type")
        self.assertEqual(train_stratum("cold", "Chemical", index), "B_seen_other_type")
        self.assertEqual(train_stratum("ibuprofen", "Chemical", index), "C_unseen")
        self.assertEqual(train_stratum("the", "Chemical", index), "C_unseen")

    def test_span_is_linked_to_classifier_output(self):
        tokens = ["Renal", "failure", "after", "5-FU", "(", "FU", ")"]
        ents = [{"text": "renal failure", "type": "Disease", "confidence": 0.7},
                {"text": "5-FU (FU)", "type": "Chemical", "confidence": 0.4}]
        self.assertEqual(entity_for_span(tokens, (0, 2, "Disease"), ents)["confidence"], 0.7)
        self.assertEqual(entity_for_span(tokens, (3, 7, "Chemical"), ents)["confidence"], 0.4)
        self.assertIsNone(entity_for_span(tokens, (0, 2, "Chemical"), ents))


class MetricTests(unittest.TestCase):
    def test_auroc_hand_cases(self):
        y = np.array([1, 1, 0, 0])
        self.assertEqual(an.auroc(np.array([0.9, 0.8, 0.2, 0.1]), y), 1.0)
        self.assertEqual(an.auroc(np.array([0.1, 0.2, 0.8, 0.9]), y), 0.0)
        self.assertEqual(an.auroc(np.array([0.5, 0.5, 0.5, 0.5]), y), 0.5)
        self.assertAlmostEqual(an.auroc(np.array([0.9, 0.3, 0.3, 0.1]), y), 0.875)   # one tie = half
        self.assertIsNone(an.auroc(np.array([0.1, 0.2]), np.array([1, 1])))

    def test_auroc_and_pr_auc_match_sklearn(self):
        from sklearn.metrics import average_precision_score, roc_auc_score
        rng = np.random.default_rng(0)
        for _ in range(20):
            y = rng.integers(0, 2, 200)
            s = np.round(rng.random(200) + 0.3 * y, 1)                              # many ties
            self.assertAlmostEqual(an.auroc(s, y), roc_auc_score(y, s), places=10)
            self.assertAlmostEqual(an.pr_auc(s, y), average_precision_score(y, s), places=10)

    def test_decision_metrics(self):
        d = np.array(["passed", "passed", "needs_review", "failed", "passed"], dtype=object)
        y = np.array([1, 0, 1, 0, 1])
        m = an.decision_metrics(d, y)
        self.assertAlmostEqual(m["p_correct_given_passed"], 2 / 3)
        self.assertAlmostEqual(m["false_acceptance"], 1 / 2)        # 1 of 2 incorrect passed
        self.assertAlmostEqual(m["false_rejection"], 1 / 3)         # 1 of 3 correct not passed
        self.assertAlmostEqual(m["p_incorrect_given_failed"], 1.0)

    def test_filtering(self):
        f = an.filtering(np.array([1, 1, 0, 0]), np.array([1, 0, 1, 0]), total_gold=4)
        self.assertAlmostEqual(f["unfiltered"]["precision"], 0.5)
        self.assertAlmostEqual(f["unfiltered"]["recall"], 0.5)
        self.assertAlmostEqual(f["filtered"]["precision"], 0.5)
        self.assertAlmostEqual(f["filtered"]["recall"], 0.25)       # filtering cannot recover missed entities

    def test_calibration(self):
        c = an.calibration(np.array([0.05, 0.05, 0.95, 0.95]), np.array([0, 0, 1, 1]))
        self.assertAlmostEqual(c["ece"], 0.05)
        self.assertAlmostEqual(c["brier"], 0.0025)

    def test_cliffs_delta(self):
        self.assertEqual(an.cliffs_delta(np.array([3, 4]), np.array([1, 2])), 1.0)
        self.assertEqual(an.cliffs_delta(np.array([1, 2]), np.array([1, 2])), 0.0)


class OverallAndDecisionTests(unittest.TestCase):
    """The analysis must reproduce the reviewer's own overall score and decision."""

    def test_matches_reviewer(self):
        reviewer = EntityReviewService(config={"weights": dict(ENTITY_WEIGHTS), "thresholds": dict(THRESHOLDS),
                                               "settings": dict(ENTITY_SETTINGS)})
        rng = np.random.default_rng(1)
        x = np.round(rng.random((300, 5)), 3)
        mine = an.overall(x, an.W0)
        for i in range(300):
            ref = reviewer._calculate_overall_score(dict(zip(an.CRITERIA, x[i].tolist())), ENTITY_WEIGHTS)
            self.assertAlmostEqual(mine[i], ref, places=9)

    def test_ablation_renormalises_like_an_unassessed_criterion(self):
        reviewer = EntityReviewService(config={})
        x = np.array([[0.9, 0.3, 1.0, 0.95, 0.8]])
        scores = dict(zip(an.CRITERIA, x[0].tolist()))
        scores["coverage"] = None
        self.assertAlmostEqual(an.overall(x, an.W0, drop=("coverage",))[0],
                               reviewer._calculate_overall_score(scores, ENTITY_WEIGHTS), places=9)

    def test_decision_rules(self):
        d = an.decide(np.array([0.8, 0.6, 0.3, 0.9, 0.9]), np.array([1.0, 1.0, 1.0, 0.3, 1.0]),
                      np.array([True, True, True, True, False]))
        self.assertEqual(d.tolist(), ["passed", "needs_review", "failed", "failed", "failed"])


class WeightAndBaselineTests(unittest.TestCase):
    def test_simplex_grid(self):
        grid = list(an.simplex_grid(0.25))
        self.assertEqual(len(grid), 70)                            # C(8, 4)
        self.assertTrue(all(abs(sum(w) - 1) < 1e-9 and min(w) >= 0 for w in grid))

    def test_w3_finds_the_informative_criterion(self):
        rng = np.random.default_rng(2)
        y = rng.integers(0, 2, 400)
        x = rng.random((400, 5))
        x[:, 2] = y * 0.6 + rng.random(400) * 0.4                  # only "constraint" is informative
        w = an.calibrate_w3(x, y, step=0.25)["weights"]
        self.assertEqual(w["constraint"], 1.0)

    def test_baselines(self):
        rows = [row(True, [1] * 5, "A_seen_same_type", conf=0.7, agree=True, p=0.9),
                row(False, [0] * 5, "B_seen_other_type", conf=None, agree=False, p=0.6),
                row(False, [0] * 5, "C_unseen", conf=0.2, agree=None, p=None)]
        self.assertEqual(an.b0_confidence(rows).tolist(), [0.7, 0.5, 0.2])
        self.assertEqual(an.b1_bert(rows).tolist(), [0.9, -0.6, 0.0])
        self.assertEqual(an.b2_seen(rows).tolist(), [1.0, 0.0, 0.0])

    def test_learned_scorers_use_only_the_five_criteria_and_never_see_eval_labels(self):
        rng = np.random.default_rng(3)

        def make(n, tag):
            out = []
            for i in range(n):
                c = bool(rng.integers(0, 2))
                s = rng.random(5)
                s[0] = 0.7 * c + 0.3 * s[0]
                out.append(row(c, s.tolist(), sid=f"{tag}{i // 2}"))
            return out
        dev, test = make(300, "d"), make(200, "t")
        res = an.compare_scorers(test, dev, an.weight_schemes(), gold_n=150)
        self.assertEqual(res["learned_scorers"], "fitted on DEV rows, applied unchanged")
        self.assertGreater(res["scorers"]["B3_logistic"]["auroc"], 0.8)
        self.assertGreater(res["scorers"]["B4_gbt"]["auroc"], 0.8)
        flipped = [dict(r, correct=not r["correct"]) for r in test]
        res2 = an.compare_scorers(flipped, dev, an.weight_schemes(), gold_n=150)
        self.assertAlmostEqual(res2["scorers"]["B3_logistic"]["auroc"], 1 - res["scorers"]["B3_logistic"]["auroc"])

    def test_stratified_reports_counts_only_for_small_cells(self):
        rows = [row(i % 2 == 0, [0.5] * 5, "A_seen_same_type") for i in range(80)] + \
               [row(True, [0.5] * 5, "C_unseen") for _ in range(5)]
        out = an.stratified(np.arange(85, dtype=float), rows)
        self.assertIn("auroc", out["A_seen_same_type"])
        self.assertNotIn("auroc", out["C_unseen"])
        self.assertEqual(out["B_seen_other_type"]["n"], 0)

    def test_sentence_bootstrap_keeps_sentences_together(self):
        g = np.array(["a", "a", "b", "b", "c"])
        seen = []
        an.bootstrap_ci(lambda i: seen.append(sorted(i.tolist())) or 0.5, g, n=20)
        for sample in seen:
            self.assertEqual(sample.count(0), sample.count(1))
            self.assertEqual(sample.count(2), sample.count(3))


if __name__ == "__main__":
    unittest.main()
