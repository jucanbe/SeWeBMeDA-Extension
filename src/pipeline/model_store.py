"""First-run model downloads into VLLM_Paper/Models (pinned revisions, resumable) and readiness checks.

A model is ready only when three things are present locally, all under VLLM_Paper/Models:
  1. weights            every weight file of the pinned snapshot (size + LFS sha256 = blob name)
  2. tokenizer/config   every other file of the snapshot (config, tokenizer, generation config, ...)
  3. remote code        for trust_remote_code models: the pinned code files of every code dependency
                        (for nomic-embed-text-v1.5 they live in nomic-ai/nomic-bert-2048), AND an
                        offline AutoConfig load that resolves the dynamic module from the local caches.
If (3) does not work offline, Hugging Face access is allowed once so that Transformers can cache the
dynamic module (still inside VLLM_Paper/Models); offline is then re-verified. Only if it still fails is
vLLM started online, and that is recorded.
"""
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Optional

from pipeline.durable import atomic_write_json
from pipeline.paths import HF_HOME, MODEL_MANIFESTS, MODELS_DIR, ROOT
from pipeline.registry import ModelSpec

WEIGHT_SUFFIXES = (".safetensors", ".bin", ".pt", ".pth", ".gguf", ".msgpack", ".h5", ".onnx")
HUB = HF_HOME / "hub"


def _manifest_path(spec: ModelSpec) -> Path:
    return MODEL_MANIFESTS / f"{spec.hf_id.replace('/', '__')}@{spec.revision}.json"


def _snapshot(repo: str, revision: str) -> Optional[Path]:
    """Local snapshot folder of a pinned commit in the package's hub cache (no network, no completeness
    rules of huggingface_hub: completeness is checked against our own manifest)."""
    p = HUB / f"models--{repo.replace('/', '--')}" / "snapshots" / revision
    return p if p.is_dir() else None


def _sha256(path: Path) -> str:
    import hashlib
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 24), b""):
            h.update(chunk)
    return h.hexdigest()


def _verify_cache_path() -> Path:
    return MODEL_MANIFESTS / "verified_files.json"


def _load_verified() -> Dict:
    p = _verify_cache_path()
    return json.loads(p.read_text()) if p.exists() else {}


def check_files(path: Path, files: Dict[str, int], lfs: Dict[str, str]) -> Dict[str, str]:
    """Problems per file ({} = all good).

    Snapshot entries are usually symlinks into blobs/; they are resolved. A file is valid when it exists
    with the expected size and, for LFS files, its CONTENT sha256 equals the Hub's LFS sha256. The blob
    file name is not used: with Xet storage it is not the sha256. Content hashes are computed once and
    remembered (keyed by resolved path, size and mtime), so later checks are instant.
    """
    problems = {}
    verified = _load_verified()
    changed = False
    for rel, size in files.items():
        f = path / rel
        real = Path(os.path.realpath(f))
        if not real.is_file():
            problems[rel] = "missing" + (" (broken symlink)" if f.is_symlink() else "")
            continue
        st = real.stat()
        if st.st_size != size:
            problems[rel] = f"size {st.st_size} != {size}"
            continue
        if rel in lfs:
            key = f"{real}|{st.st_size}|{int(st.st_mtime)}"
            sha = verified.get(key)
            if sha is None:
                print(f"[MODEL] verifying sha256 of {rel} ({size / 1e9:.2f} GB, once)")
                sha = _sha256(real)
                verified[key] = sha
                changed = True
            if sha != lfs[rel]:
                problems[rel] = f"sha256 {sha[:12]} != {lfs[rel][:12]}"
    if changed:
        atomic_write_json(_verify_cache_path(), verified)
    return problems


def _files_ok(path: Path, files: Dict[str, int], lfs: Dict[str, str]) -> bool:
    return not check_files(path, files, lfs)


def status(spec: ModelSpec) -> Dict:
    """What is present locally: weights / tokenizer+config / remote code (files only)."""
    out = {"weights": False, "tokenizer_config": False, "remote_code_files": not spec.code_deps, "path": None}
    man = _manifest_path(spec)
    path = _snapshot(spec.hf_id, spec.revision)
    if path is None or not man.exists():
        return out
    meta = json.loads(man.read_text())
    import fnmatch
    required = {r: s for r, s in meta["files"].items()          # intentionally skipped formats are never required
                if not any(fnmatch.fnmatch(r, p) for p in spec.ignore_patterns)}
    weights = {r: s for r, s in required.items() if r.endswith(WEIGHT_SUFFIXES)}
    others = {r: s for r, s in required.items() if not r.endswith(WEIGHT_SUFFIXES)}
    lfs = meta.get("lfs_sha256", {})
    pw, po = check_files(path, weights, lfs), check_files(path, others, lfs)
    out.update(path=str(path), weights=bool(weights) and not pw, tokenizer_config=not po,
               weight_files=sorted(weights), problems={**pw, **po})
    deps_ok = True
    for dep in meta.get("code_dependencies", []):
        p = _snapshot(dep["repo"], dep["revision"])
        deps_ok &= p is not None and _files_ok(p, dep["files"], dep.get("lfs_sha256", {}))
    if spec.code_deps:
        out["remote_code_files"] = deps_ok and len(meta.get("code_dependencies", [])) == len(spec.code_deps)
    return out


def _download(repo: str, revision: str, allow_patterns=None, ignore_patterns=()) -> Dict:
    from huggingface_hub import HfApi, snapshot_download
    info = HfApi().model_info(repo, revision=revision, files_metadata=True)
    if info.sha != revision:
        raise RuntimeError(f"{repo}: revision {revision} resolved to {info.sha}")
    import fnmatch
    sib = [s for s in info.siblings
           if (allow_patterns is None or any(fnmatch.fnmatch(s.rfilename, p) for p in allow_patterns))
           and not any(fnmatch.fnmatch(s.rfilename, p) for p in ignore_patterns)]
    files = {s.rfilename: s.size for s in sib if s.size is not None}
    print(f"[MODEL] {repo}: {len(files)} files, {sum(files.values()) / 1e9:.2f} GB")
    path = Path(snapshot_download(repo, revision=revision, cache_dir=str(HUB), max_workers=8,
                                  allow_patterns=list(allow_patterns) if allow_patterns else None,
                                  ignore_patterns=list(ignore_patterns) or None))
    lfs = {s.rfilename: s.lfs.sha256 for s in sib if s.lfs is not None}
    problems = check_files(path, files, lfs)
    if problems:
        raise RuntimeError(f"{repo}: download incomplete or corrupted: {problems}")
    return {"repo": repo, "revision": revision, "local_path": str(path), "files": files, "lfs_sha256": lfs}


def ensure_model(spec: ModelSpec) -> Dict:
    """Download whatever is missing (weights, tokenizer/config, remote code); return provenance."""
    if os.environ.get("VLLM_PAPER_TEST_MODE") == "1":           # unit tests: fake server, no weights
        return {"hf_id": spec.hf_id, "revision": spec.revision, "local_path": "test-mode", "files": {},
                "offline_ok": True}
    st = status(spec)
    print(f"[MODEL] {spec.hf_id} @ {spec.revision[:12]}: weights {'present' if st['weights'] else 'MISSING'}, "
          f"tokenizer/config {'present' if st['tokenizer_config'] else 'MISSING'}, "
          f"remote code {'present' if st['remote_code_files'] else 'MISSING'}"
          + ("" if spec.code_deps else " (not needed)")
          + (f"; problems: {st['problems']}" if st.get("problems") else ""))
    man = _manifest_path(spec)
    if st["weights"] and st["tokenizer_config"] and st["remote_code_files"]:
        print(f"[MODEL] {spec.hf_id} already present (weights: {', '.join(st['weight_files'])}). Skipping download.")
        prov = json.loads(man.read_text())
    else:
        print(f"[MODEL] MODEL DOWNLOAD into {HUB}")
        print("[MODEL] This can take a long time on the first run (several GB); interrupted downloads resume.")
        t0 = time.time()
        main = _download(spec.hf_id, spec.revision, ignore_patterns=spec.ignore_patterns)
        deps = [_download(repo, rev, patterns) for repo, rev, patterns in spec.code_deps]
        prov = {"hf_id": spec.hf_id, "revision": spec.revision, "local_path": main["local_path"],
                "files": main["files"], "lfs_sha256": main["lfs_sha256"], "code_dependencies": deps,
                "total_bytes": sum(main["files"].values()), "downloaded_at": datetime.now(timezone.utc).isoformat(),
                "download_seconds": round(time.time() - t0)}
        atomic_write_json(man, prov)
        print(f"[MODEL] Download complete and verified ({time.time() - t0:.0f} s).")
    if spec.trust_remote_code:
        prov["offline_ok"] = prepare_remote_code(spec, prov)
        atomic_write_json(man, prov)
    else:
        prov["offline_ok"] = True
    return prov


# ---------------------------------------------------------------------------
# trust_remote_code

_PROBE = r"""
import json, sys
from transformers import AutoConfig
path, code_rev = sys.argv[1], sys.argv[2]
cfg = AutoConfig.from_pretrained(path, trust_remote_code=True, code_revision=code_rev or None)
print(json.dumps({"config_class": type(cfg).__module__ + "." + type(cfg).__name__}))
"""


def probe_remote_code(spec: ModelSpec, path: str, offline: bool) -> Dict:
    """Load the config with trust_remote_code in a fresh process (no GPU) using only VLLM_Paper caches."""
    env = dict(os.environ)
    if offline:
        env.update(HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1")
    else:
        env.pop("HF_HUB_OFFLINE", None)
        env.pop("TRANSFORMERS_OFFLINE", None)
    code_rev = spec.code_deps[0][1] if spec.code_deps else ""
    r = subprocess.run([sys.executable, "-c", _PROBE, path, code_rev], env=env, capture_output=True, text=True,
                       timeout=600, cwd=str(ROOT))
    ok = r.returncode == 0
    return {"ok": ok, "offline": offline, "detail": (r.stdout.strip() if ok else r.stderr.strip()[-1500:])}


def modules_cache_files() -> list:
    d = Path(os.environ.get("HF_MODULES_CACHE", HF_HOME / "modules"))
    return sorted(str(p.relative_to(MODELS_DIR)) for p in d.rglob("*.py")) if d.exists() else []


def prepare_remote_code(spec: ModelSpec, prov: Dict) -> bool:
    """True if the dynamic code resolves offline (after at most one online caching pass)."""
    path = prov["local_path"]
    first = probe_remote_code(spec, path, offline=True)
    if first["ok"]:
        print(f"[MODEL] remote code resolves offline from VLLM_Paper/Models ({first['detail']})")
        prov["remote_code"] = {"offline_probe": first, "modules": modules_cache_files()}
        return True
    print("[MODEL] remote code not resolvable offline yet; allowing Hugging Face access once to cache it "
          "inside VLLM_Paper/Models")
    online = probe_remote_code(spec, path, offline=False)
    second = probe_remote_code(spec, path, offline=True) if online["ok"] else {"ok": False, "detail": "online failed"}
    prov["remote_code"] = {"offline_probe_before": first, "online_probe": online, "offline_probe_after": second,
                           "modules": modules_cache_files()}
    if second["ok"]:
        print("[MODEL] remote code cached; offline load verified")
        return True
    print("[MODEL] WARNING: remote code still not resolvable offline; vLLM will start with Hugging Face access "
          "enabled (caches stay in VLLM_Paper/Models). Details in the model manifest.")
    return False
