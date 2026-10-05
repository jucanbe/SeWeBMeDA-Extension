"""Tests of the H100/vLLM package without GPUs or real models.

    python3 -m unittest discover -s tests            unit tests (seconds)
    VLLM_PAPER_E2E=1 python3 -m unittest tests.test_package.EndToEnd
                                                     whole workflow against a fake vLLM server in a temporary
                                                     copy of the package (execution1 -> dev -> freeze -> test -> analyze)
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pipeline.durable import CorruptJSONL, DurableAppender, atomic_write_json, read_jsonl  # noqa: E402
from pipeline.workqueue import MAX_ATTEMPTS, Outcome, ServerDown, run_resumable  # noqa: E402


class DurableFiles(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_truncated_last_line_is_repaired(self):
        p = self.tmp / "a.jsonl"
        p.write_text('{"a": 1}\n{"a": 2}\n{"a": 3, "b"')
        self.assertEqual([r["a"] for r in read_jsonl(p)], [1, 2])
        self.assertEqual(p.read_text(), '{"a": 1}\n{"a": 2}\n')
        with DurableAppender(p) as w:
            w.write({"a": 4})
        self.assertEqual([r["a"] for r in read_jsonl(p)], [1, 2, 4])

    def test_complete_last_line_without_newline_is_kept(self):
        p = self.tmp / "b.jsonl"
        p.write_text('{"a": 1}\n{"a": 2}')
        self.assertEqual(len(read_jsonl(p)), 2)
        with DurableAppender(p) as w:
            w.write({"a": 3})
        self.assertEqual([r["a"] for r in read_jsonl(p)], [1, 2, 3])

    def test_corrupt_middle_line_aborts(self):
        p = self.tmp / "c.jsonl"
        p.write_text('{"a": 1}\nGARBAGE\n{"a": 3}\n')
        with self.assertRaises(CorruptJSONL):
            read_jsonl(p)

    def test_atomic_write_leaves_no_temporary_file(self):
        p = self.tmp / "m.json"
        atomic_write_json(p, {"x": 1})
        atomic_write_json(p, {"x": 2})
        self.assertEqual(json.loads(p.read_text()), {"x": 2})
        self.assertEqual([f.name for f in self.tmp.iterdir()], ["m.json"])


class WorkQueue(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.out, self.fail = self.tmp / "out.jsonl", self.tmp / "fail.jsonl"

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def run_q(self, process, items=("a", "b", "c", "d"), health=None):
        return run_resumable(list(items), key=lambda x: x, process=process, out_path=self.out,
                             fail_path=self.fail, concurrency=2, tag="[T]", health_check=health)

    def test_failures_are_not_completed_and_are_retried(self):
        calls = {}

        def process(x):
            calls[x] = calls.get(x, 0) + 1
            if x == "b" and calls[x] < 3:
                return Outcome(False, reason="bad json", error_kind="response")
            return Outcome(True, record={"v": x})
        r = self.run_q(process)
        self.assertEqual(r.completed, 4)
        self.assertEqual(calls["b"], 3)
        self.assertEqual(sorted(x["_key"] for x in read_jsonl(self.out)), ["a", "b", "c", "d"])
        self.assertEqual(len(read_jsonl(self.fail)), 2)

    def test_persistent_failure_is_abandoned_after_bounded_attempts(self):
        r = self.run_q(lambda x: Outcome(False, reason="no", error_kind="response") if x == "c"
                       else Outcome(True, record={}))
        self.assertEqual(r.abandoned, ["c"])
        self.assertEqual(sum(1 for f in read_jsonl(self.fail) if f["key"] == "c"), MAX_ATTEMPTS)
        self.assertTrue(read_jsonl(self.fail)[-1]["abandoned"])
        calls = []
        r2 = self.run_q(lambda x: calls.append(x) or Outcome(True, record={}))       # rerun: nothing left
        self.assertEqual(calls, [])
        self.assertEqual(r2.abandoned, ["c"])

    def test_server_down_stops_and_resume_skips_completed(self):
        def down(x):
            if x == "c":
                return Outcome(False, reason="refused", error_kind="connection")
            return Outcome(True, record={"v": x})
        with self.assertRaises(ServerDown):
            self.run_q(down, health=lambda: False)
        done = {x["_key"] for x in read_jsonl(self.out)}
        self.assertNotIn("c", done)
        calls = []
        self.run_q(lambda x: calls.append(x) or Outcome(True, record={"v": x}))
        self.assertNotIn("a", calls)
        self.assertIn("c", calls)
        self.assertEqual(len(read_jsonl(self.out)), 4)

    def test_exception_in_processing_is_logged_not_swallowed(self):
        def boom(x):
            raise ValueError("bug")
        r = self.run_q(boom, items=("z",))
        self.assertEqual(r.abandoned, ["z"])
        self.assertIn("ValueError", read_jsonl(self.fail)[0]["reason"])


class LockAndDesign(unittest.TestCase):
    def test_lock_is_exclusive_across_processes(self):
        code = ("import sys,time; sys.path.insert(0,'src'); from pipeline.server import ExecutionLock\n"
                "with ExecutionLock('holder'): print('held', flush=True); time.sleep(4)")
        p = subprocess.Popen([sys.executable, "-c", code], cwd=ROOT, stdout=subprocess.PIPE, text=True)
        self.assertEqual(p.stdout.readline().strip(), "held")
        from pipeline.server import ExecutionLock, LockBusy
        with self.assertRaises(LockBusy):
            with ExecutionLock("second"):
                pass
        p.wait()
        with ExecutionLock("after"):
            pass

    def test_design_counts_and_no_lora(self):
        from pipeline import design
        n = {k: len(design.dev_configs(k)) for k in ("4b", "9b", "27b")}
        self.assertEqual(n, {"4b": 63, "9b": 27, "27b": 15})
        names = [c["name"] for k in n for c in design.dev_configs(k)]
        self.assertEqual(len(names), len(set(names)))
        blob = json.dumps(design.all_dev_configs()) + (ROOT / "configs" / "comparisons_v6.json").read_text()
        for cond in ('"E8"', '"E9"', "peft", "lora_"):
            self.assertNotIn(cond, blob.replace('"removed": ["E8", "E9"', ""))
        self.assertFalse((ROOT / "src" / "experiments" / "peft").exists())

    def test_every_path_is_inside_the_package(self):
        from experiments.fewshot.retrieve import CACHE_DIR
        from experiments.kg.build import KG_ROOT
        from experiments.review.score import BERT_ROOT
        from experiments.schemas import DATASETS_DIR, PROJECT_ROOT, RESULTS_DIR, SYNTHETIC_DIR, SYNTHETIC_FULL_DIR
        from pipeline.paths import HF_HOME, MODELS_DIR
        for p in (PROJECT_ROOT, DATASETS_DIR, SYNTHETIC_FULL_DIR, SYNTHETIC_DIR, RESULTS_DIR, KG_ROOT, CACHE_DIR,
                  BERT_ROOT, HF_HOME, MODELS_DIR):
            self.assertTrue(str(p).startswith(str(ROOT)), p)
        self.assertTrue(HF_HOME.is_relative_to(ROOT / "Models"))
        src = "\n".join(f.read_text() for f in (ROOT / "src").rglob("*.py"))
        for bad in ("../EntityClass", "EntityClass/", "1234/v1", "lmstudio", "llama-server"):
            self.assertNotIn(bad, src)

    def test_missing_model_is_detected_without_network(self):
        os.environ["HF_HUB_OFFLINE"] = "1"
        from pipeline.model_store import _snapshot
        from pipeline.registry import ModelSpec
        fake = ModelSpec("x", "nobody/not-a-model", "0" * 40, "classifier", "small", 1, [])
        self.assertIsNone(_snapshot(fake.hf_id, fake.revision))

    def test_test_stage_refuses_without_freeze(self):
        from pipeline.freeze import FREEZE_FILE, FreezeError, verify_freeze
        if FREEZE_FILE.exists():
            self.skipTest("a real freeze exists")
        with self.assertRaises(FreezeError):
            verify_freeze()

    def test_test_config_without_registration_is_rejected(self):
        from experiments.runner import ProtocolError, check_protocol, resolve
        from pipeline import design
        from pipeline.registry import MODELS
        cfg = resolve(dict(design.base_config(MODELS["4b"], "BC5CDR", "test", {"n": 10, "seed": 1}),
                           name="t", condition="E0", frozen=True))
        with self.assertRaises(ProtocolError):
            check_protocol(cfg)
        with self.assertRaises(ProtocolError):
            check_protocol(dict(cfg, frozen=False))


@unittest.skipUnless(os.environ.get("VLLM_PAPER_E2E") == "1", "set VLLM_PAPER_E2E=1 for the end-to-end run")
class EndToEnd(unittest.TestCase):
    """execution1 -> dev -> freeze -> test -> analyze with a fake vLLM server in a temporary package copy."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp()) / "VLLM_Paper"
        cls.tmp.mkdir()
        for name in ("src", "configs", "tests"):
            shutil.copytree(ROOT / name, cls.tmp / name, ignore=shutil.ignore_patterns("__pycache__"))
        for name in ("execution1.py", "execution2.py"):
            shutil.copy(ROOT / name, cls.tmp / name)
        for name in ("Datasets", "SyntheticDataset", "KnowledgeGraph", "BERT_models"):
            (cls.tmp / name).symlink_to(ROOT / name)
        lex = {}
        sys.path.insert(0, str(cls.tmp / "src"))
        from experiments.data.adapters import BIOCsvAdapter
        from experiments.schemas import get_schema
        for ds in ("BC5CDR", "BioRED", "MedMentions"):
            sch = get_schema(ds)
            ad = BIOCsvAdapter(sch, cls.tmp / "Datasets")
            m = {}
            for split in ("train", "dev", "test"):
                for s in ad.load(split):
                    for text, t in s.mentions():
                        if len(text) > 3:
                            m[text.lower()] = t
            lex[sch.type_names[0]] = m
        (cls.tmp / "lexicon.json").write_text(json.dumps(lex))
        cls.env = dict(os.environ, VLLM_PAPER_TEST_MODE="1", VLLM_PAPER_TEST_SCALE="24",
                       VLLM_PAPER_VLLM_BIN=str(cls.tmp / "tests" / "fake_vllm_server.py"),
                       VLLM_PAPER_CHAT_PORT="18000", VLLM_PAPER_EMBED_PORT="18002", VLLM_PAPER_READY_TIMEOUT="60",
                       FAKE_VLLM_LEXICON=str(cls.tmp / "lexicon.json"), PYTHONDONTWRITEBYTECODE="1",
                       FAKE_VLLM_REJECT_FLAG="--language-model-only")     # exercises the documented fallback flags

    @classmethod
    def tearDownClass(cls):
        if os.environ.get("VLLM_PAPER_E2E_KEEP") == "1":
            print(f"\nkept: {cls.tmp}")
        else:
            shutil.rmtree(cls.tmp.parent)

    def run_cmd(self, *args, env=None, expect=0):
        t0 = time.time()
        p = subprocess.run([sys.executable, *args], cwd=self.tmp, env=env or self.env, capture_output=True,
                           text=True, timeout=3600)
        out = p.stdout + p.stderr
        print(f"\n--- {' '.join(args)} ({time.time() - t0:.0f} s, exit {p.returncode})\n{out[-3000:]}")
        self.assertEqual(p.returncode, expect, out[-4000:])
        return out

    def test_full_workflow(self):
        out = self.run_cmd("execution2.py", "--stage", "test", expect=1)
        self.assertIn("refused", out)                                   # no freeze yet
        self.run_cmd("execution2.py", "--stage", "freeze", expect=1)    # DEV incomplete
        # annotation with a crash of the fake server after 40 requests: bounded restart + resume
        env = dict(self.env, FAKE_VLLM_CRASH_AFTER="40", FAKE_VLLM_STATE=str(self.tmp / "crash1"))
        out = self.run_cmd("execution1.py", env=env)
        self.assertIn("restart 1/3", out)
        self.assertIn("SUMMARY", out)
        out = self.run_cmd("execution1.py")
        self.assertIn("Nothing to do", out)
        # DEV with a crash in the middle
        env = dict(self.env, FAKE_VLLM_CRASH_AFTER="150", FAKE_VLLM_STATE=str(self.tmp / "crash2"))
        out = self.run_cmd("execution2.py", "--stage", "dev", env=env)
        self.assertIn("restart 1/3", out)
        self.assertIn("DEV is complete", out)
        manifests = list((self.tmp / "results" / "runs").glob("dev-*/manifest.json"))
        self.assertEqual(len(manifests), 105)
        self.assertTrue(all(json.loads(m.read_text())["status"] == "complete" for m in manifests))
        out = self.run_cmd("execution2.py", "--stage", "dev")
        self.assertIn("105/105", out.replace(" ", "").replace("runscomplete:", ""))
        out = self.run_cmd("execution2.py", "--stage", "freeze")
        self.assertIn("design frozen", out)
        fz = json.loads((self.tmp / "results" / "frozen" / "freeze.json").read_text())
        self.assertNotIn("--language-model-only", fz["runtime"]["4b"]["serve_args"])
        self.assertFalse(any(c["condition"] in ("E8", "E9") for cfgs in fz["test_configs"].values() for c in cfgs))
        self.run_cmd("execution2.py", "--stage", "freeze", expect=1)    # never re-frozen silently
        out = self.run_cmd("execution2.py", "--stage", "test")
        self.assertIn("TEST SUMMARY", out)
        out = self.run_cmd("execution2.py", "--stage", "analyze")
        res = json.loads((self.tmp / "results" / "analysis" / "final_results.json").read_text())
        self.assertIn("RQ1_criterion_tests", res["validity"])
        self.assertTrue(all(res["validity"]["learned_scorers_reproduced"].values()))
        self.assertTrue((self.tmp / "results" / "analysis" / "tables" / "classification.tex").exists())
        # tampering with the frozen design is detected
        cmp_ = self.tmp / "configs" / "comparisons_v6.json"
        cmp_.write_text(cmp_.read_text() + " ")
        out = self.run_cmd("execution2.py", "--stage", "test", expect=1)
        self.assertIn("changed after the freeze", out)


if __name__ == "__main__":
    unittest.main()
