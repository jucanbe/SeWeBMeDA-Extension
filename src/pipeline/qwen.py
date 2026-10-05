"""Embedding phase and Qwen LLM stages (DEV and TEST), strictly one model at a time."""
import time
from pathlib import Path
from typing import Dict, List, Optional

from experiments import annotation
from experiments.data.model import Sentence
from experiments.fewshot.retrieve import EMBED_MODEL, Embedder
from experiments.llm.ner import ChatClient, build_messages, parse_response, response_schema
from experiments.runner import Experiment, needs_embeddings
from experiments.schemas import get_schema
from pipeline import design, local_embed
from pipeline.journal import journal
from pipeline.orchestrate import banner, prepare_model, print_estimate, smoke_chat, with_recovery
from pipeline.progress import Progress
from pipeline.registry import MODELS, ModelSpec
from pipeline.server import ServerError, VLLMServer, environment

RUNTIME_KEYS = ("hf_id", "revision", "vllm_version", "serve_args", "request_extra", "max_num_seqs")
SIZE_FACTOR = {"4b": 1.0, "9b": 0.5, "27b": 0.2}          # rough relative throughput, replaced by measurements


def runnable(cfg: Dict) -> bool:
    """Synthetic/E2c configs need complete annotations from execution1."""
    need = design.needs(cfg)
    return not need or annotation.is_complete(cfg["dataset"], need)


def split_runnable(cfgs: List[Dict]):
    ok = [c for c in cfgs if runnable(c)]
    waiting = [c["name"] for c in cfgs if not runnable(c)]
    return ok, waiting


# ---------------------------------------------------------------------------
# embeddings

def embedding_texts(exps: List[Experiment]) -> Dict[str, List[str]]:
    docs, queries = set(), set()
    for e in exps:
        if not needs_embeddings(e.cfg):
            continue
        for pool in e.pools(embedder=None).values():
            docs.update(s.text for s in pool.sentences)
        queries.update(e.query_texts())
    return {"document": sorted(docs), "query": sorted(queries)}


def missing_embeddings(texts: Dict[str, List[str]]) -> Dict[str, List[str]]:
    emb = Embedder(offline=True)
    prefix = {"query": "search_query: ", "document": "search_document: "}
    return {kind: [t for t in ts if not emb._path(emb._key(prefix[kind] + t)).exists()] for kind, ts in texts.items()}


def embedding_phase(exps: List[Experiment], log_dir: Path, kill_stale: bool):
    """Fill the embedding cache before any Qwen model starts (one model at a time).

    Primary backend: vLLM serving nomic-embed-text-v1.5. If vLLM cannot start it, the same model
    (same revision and pinned remote code) is loaded in-process with Transformers, used, and unloaded.
    The backend is recorded in embeddings/backend.json; a cache is never extended with a different backend.
    """
    banner("EMBEDDINGS (nomic-embed-text-v1.5)")
    missing = missing_embeddings(embedding_texts(exps))
    n = sum(len(v) for v in missing.values())
    if not n:
        print("[EMBED] all required embeddings are cached; the embedding model is not started")
        return
    spec = MODELS["nomic-embed"]
    prov = prepare_model(spec)
    recorded = local_embed.recorded_backend()
    if recorded in (None, "vllm"):
        try:
            with VLLMServer(spec, log_dir, kill_stale=kill_stale, offline=prov["offline_ok"]) as srv:
                local_embed.check_backend("vllm", {"vllm_version": srv.version, "serve_args": srv.args_used})
                _fill(Embedder(srv.base_url, offline=False, batch_size=256), missing, n)
            journal("embeddings", model=EMBED_MODEL, computed=n, backend="vllm")
            return
        except ServerError as e:
            if recorded == "vllm":
                raise ServerError(f"vLLM cannot serve the embedding model now ({e}), but the existing cache was "
                                  "computed with vLLM; refusing to mix backends") from e
            print(f"[EMBED] vLLM could not serve nomic-embed ({e}); using the in-process Transformers fallback")
            journal("embedding_fallback", reason=str(e))
    with local_embed.LocalNomic(prov, spec) as model:
        local_embed.check_backend("transformers", model.provenance())
        _fill(Embedder(offline=False, compute_fn=model.embed), missing, n)
    journal("embeddings", model=EMBED_MODEL, computed=n, backend="transformers")


def _fill(emb: Embedder, missing: Dict[str, List[str]], n: int):
    prog = Progress("[EMBED]", n, unit="text")
    for kind, texts in missing.items():
        for i in range(0, len(texts), 2048):
            chunk = texts[i:i + 2048]
            emb.embed(chunk, kind)
            prog.update(len(chunk))
    prog.close()


# ---------------------------------------------------------------------------
# LLM stage

def model_smoke(srv: VLLMServer, client: ChatClient):
    """Automatic check before a Qwen model's first real request and after every restart.

    /health must answer 200, /v1/models must list exactly this model, and 3 structured classification
    requests (the first DEV-subset sentence of each dataset, production prompt and JSON schema) must all
    return valid, untruncated JSON. Any failure raises ServerError: the server is stopped cleanly and the
    stage aborts.
    """
    import httpx
    from experiments.data.adapters import BIOCsvAdapter
    from experiments.subsets import get_subset, load_subset
    health = httpx.get(f"http://127.0.0.1:{srv.spec.port}/health", timeout=10).status_code
    served = srv.served_models()
    if health != 200 or served != [srv.spec.hf_id]:
        raise ServerError(f"smoke check failed: /health {health}, /v1/models {served}")
    print(f"[SMOKE] /health 200, /v1/models {served}, max_num_seqs {srv.spec.max_num_seqs}")
    msgs, schemas = [], []
    for ds in design.DATASETS:
        schema = get_schema(ds)
        sents = {s.sid: s for s in BIOCsvAdapter(schema).load("dev")}
        sid = load_subset(get_subset(ds, "dev", design.DEV_SUBSET["n"], design.DEV_SUBSET["seed"]))[0]
        msgs.append(build_messages(schema, sents[sid]))
        schemas.append(response_schema(schema))
    smoke_chat(client, msgs, schemas, min_ok=len(msgs), parse=parse_response)
    journal("model_smoke_ok", model=srv.spec.hf_id)


def check_runtime(actual: Dict, frozen: Dict, key: str):
    diff = {k: (frozen.get(k), actual.get(k)) for k in RUNTIME_KEYS if frozen.get(k) != actual.get(k)}
    if diff:
        raise ServerError(f"runtime of {key} differs from the frozen DEV runtime: {diff}")


def run_llm_stage(stage: str, configs: Dict[str, List[Dict]], log_dir: Path, kill_stale: bool,
                  frozen_runtime: Optional[Dict[str, Dict]] = None, after_model=None) -> Dict:
    summary = {}
    measured_rate: Dict[str, float] = {}
    for key, cfgs in configs.items():
        spec: ModelSpec = MODELS[key]
        exps = [Experiment(c) for c in cfgs]
        pending = [e for e in exps if not e.status()["state"].startswith("complete")]
        banner(f"QWEN {key.upper()} {stage.upper()}: {len(exps) - len(pending)}/{len(exps)} runs complete")
        if pending:
            prov = prepare_model(spec)
            with VLLMServer(spec, log_dir, kill_stale=kill_stale, offline=prov["offline_ok"]) as srv:
                rt = srv.runtime()
                if frozen_runtime is not None:
                    check_runtime(rt, frozen_runtime[key], key)
                env = environment({"execution": f"execution2 {stage}"})
                client = ChatClient(spec.hf_id, srv.base_url, max_tokens=design.MAX_TOKENS,
                                    extra_body=spec.request_extra)
                embedder = Embedder(offline=True)
                banner(f"SMOKE TEST (Qwen {key.upper()})")
                model_smoke(srv, client)
                banner("EXPERIMENT EXECUTION")
                t0, n0 = time.time(), sum(e.status()["completed"] for e in pending)
                for i, e in enumerate(pending, 1):
                    tag = f"[QWEN {key.upper()}][{e.cfg['dataset']}][{e.cfg['name'].split('-', 1)[1].rsplit('-', 2)[0]}]"
                    with_recovery(srv, lambda e=e, tag=tag: e.run(client, spec.concurrency, embedder, srv.healthy,
                                                                   runtime=rt, environment=env, tag=tag),
                                  lambda: model_smoke(srv, client), e.dir.name)
                    done_now = sum(x.status()["completed"] for x in pending) - n0
                    rate = done_now / max(time.time() - t0, 1e-6)
                    measured_rate[key] = rate
                    if i == 1 or i == len(pending) or i % 5 == 0:
                        rows = []
                        for k2, c2 in configs.items():
                            left = sum(Experiment(c).status()["remaining"] for c in c2)
                            r2 = measured_rate.get(k2) or (rate * SIZE_FACTOR[k2] / SIZE_FACTOR[key])
                            rows.append((f"Qwen {k2.upper()} {stage}" + ("" if k2 in measured_rate else " (rough)"),
                                         left, r2))
                        title = ("FIRST-RUN BENCHMARK RESULT: e" if i == 1 else "E") + \
                            "stimated remaining H100 time"
                        print_estimate(title, rows)
        if after_model:
            after_model(key)
        summary[key] = {e.cfg["name"]: e.status()["state"] for e in exps}
    return summary
