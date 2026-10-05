"""Prompt construction, LLM call and output alignment for sentence-level NER."""
import hashlib
import json
import re
import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence, Tuple

import httpx

from experiments.data.model import Sentence, Span, tokenize
from experiments.schemas import DatasetSchema

PROMPT_VERSION = "ner-v2"   # confidence (required) and normalized_form (optional), as in EntityClass


def response_schema(schema: DatasetSchema) -> Dict:
    return {
        "type": "object",
        "properties": {
            "entities": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {"text": {"type": "string"},
                                   "type": {"type": "string", "enum": schema.type_names},
                                   "confidence": {"type": "number"},
                                   "normalized_form": {"type": "string"}},
                    "required": ["text", "type", "confidence"],
                },
            }
        },
        "required": ["entities"],
    }


def system_prompt(schema: DatasetSchema) -> str:
    types = "\n".join(f"- {t}: {d}" for t, d in schema.types.items())
    return (
        f"You are a biomedical named entity recognition system for the {schema.name} annotation scheme.\n"
        "Identify every mention of the following entity types in the sentence:\n"
        f"{types}\n\n"
        "Rules:\n"
        "- Copy each entity text exactly as it appears in the sentence (same characters and spacing).\n"
        "- Do not annotate text of any other type.\n"
        "- If the same entity text occurs several times, listing it once is enough.\n"
        "- For each entity give \"confidence\": your probability between 0.0 and 1.0 that the text and type "
        "are correct.\n"
        "- Optionally give \"normalized_form\": the canonical name of the entity when you know it.\n"
        '- Answer only with JSON of the form {"entities": [{"text": "...", "type": "...", "confidence": 0.0}]}; '
        'use {"entities": []} if there are none.\n'
        "- Example answers shown in the conversation are reference annotations and therefore carry no confidence."
    )


def gold_answer(s: Sentence) -> str:
    seen, ents = set(), []
    for text, t in s.mentions():
        if (text, t) not in seen:
            seen.add((text, t))
            ents.append({"text": text, "type": t})
    return json.dumps({"entities": ents}, ensure_ascii=False)


def user_message(sentence: str, facts: Optional[List[str]] = None) -> str:
    msg = ""
    if facts:
        msg += ("Knowledge retrieved from the training-data knowledge graph for strings in this sentence "
                "(evidence only; it can be incomplete or ambiguous):\n" + "\n".join(f"- {f}" for f in facts) + "\n\n")
    return msg + f"Sentence: {sentence}"


def build_messages(schema: DatasetSchema, query: Sentence, demos: Sequence[Sentence] = (),
                   facts: Optional[List[str]] = None, demo_facts: Optional[List[List[str]]] = None) -> List[Dict]:
    messages = [{"role": "system", "content": system_prompt(schema)}]
    for i, d in enumerate(demos):
        messages.append({"role": "user", "content": user_message(d.text, demo_facts[i] if demo_facts else None)})
        messages.append({"role": "assistant", "content": gold_answer(d)})
    messages.append({"role": "user", "content": user_message(query.text, facts)})
    return messages


def prompt_hash(messages: List[Dict]) -> str:
    return hashlib.sha256(json.dumps(messages, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:16]


# ---------------------------------------------------------------------------
# alignment

def _find_all(tokens: List[str], sub: List[str], lower: bool) -> List[int]:
    if not sub:
        return []
    tk = [t.lower() for t in tokens] if lower else tokens
    sb = [t.lower() for t in sub] if lower else sub
    n = len(sb)
    return [i for i in range(len(tk) - n + 1) if tk[i:i + n] == sb]


def align(tokens: List[str], entities: List[Dict], valid_types: Sequence[str]) -> Tuple[List[Span], List[Dict]]:
    """Map predicted strings to token spans.

    Each string is matched to ALL its occurrences (whitespace tokens, then the
    benchmark-style tokenizer, then case-insensitive). Overlapping predictions
    are resolved by keeping the longer span (gold annotations are flat).
    Returns (spans, unaligned predictions).
    """
    cands, unaligned = [], []
    for ent in entities:
        text, etype = str(ent.get("text", "")).strip(), ent.get("type")
        if etype not in valid_types or not text:
            unaligned.append({"text": text, "type": etype, "reason": "invalid"})
            continue
        hits = []
        for sub in (text.split(), tokenize(text)):
            for lower in (False, True):
                hits = _find_all(tokens, sub, lower)
                if hits:
                    n = len(sub)
                    break
            if hits:
                break
        if not hits:
            unaligned.append({"text": text, "type": etype, "reason": "not_found"})
            continue
        for h in hits:
            cands.append((h, h + n, etype))
    cands = sorted(set(cands), key=lambda s: (-(s[1] - s[0]), s[0]))
    chosen, used = [], set()
    for s, e, t in cands:
        if any(i in used for i in range(s, e)):
            continue
        chosen.append((s, e, t))
        used.update(range(s, e))
    return sorted(chosen), unaligned


def parse_response(content: str) -> Tuple[List[Dict], Optional[str]]:
    """Returns (entities, error)."""
    if not content:
        return [], "empty"
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", content, re.S)
        if not m:
            return [], "invalid_json"
        try:
            data = json.loads(m.group(0))
        except json.JSONDecodeError:
            return [], "invalid_json"
    ents = data.get("entities") if isinstance(data, dict) else None
    if not isinstance(ents, list):
        return [], "no_entities_field"
    return [e for e in ents if isinstance(e, dict)], None


# ---------------------------------------------------------------------------
# OpenAI-compatible chat client (vLLM)

SERVER_ERRORS = ("connection", "server")      # error kinds that mean the server is down or broken


def schema_hash(schema: DatasetSchema) -> str:
    return hashlib.sha256(json.dumps(response_schema(schema), sort_keys=True).encode()).hexdigest()


@dataclass
class LLMResult:
    content: str
    reasoning: str
    finish_reason: str
    usage: Dict
    latency_s: float
    model: str
    error: Optional[str] = None
    error_kind: Optional[str] = None          # connection | server | client | timeout | None


class ChatClient:
    """Plain OpenAI chat-completions client. `extra_body` carries model-specific request
    fields (gpt-oss reasoning_effort, Qwen chat_template_kwargs) and is part of the run config."""

    def __init__(self, model: str, base_url: str, max_tokens: int = 2048, temperature: float = 0.0,
                 seed: int = 0, timeout: float = 600.0, extra_body: Optional[Dict] = None, retries: int = 3):
        self.model = model
        self.url = base_url.rstrip("/") + "/chat/completions"
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.seed = seed
        self.extra_body = dict(extra_body or {})
        self.retries = retries
        self.http = httpx.Client(timeout=timeout, limits=httpx.Limits(max_connections=256,
                                                                      max_keepalive_connections=256))

    def body(self, messages: List[Dict], json_schema: Optional[Dict]) -> Dict:
        body = {"model": self.model, "messages": messages, "temperature": self.temperature,
                "max_tokens": self.max_tokens, "seed": self.seed, **self.extra_body}
        if json_schema is not None:
            body["response_format"] = {"type": "json_schema",
                                       "json_schema": {"name": "entities", "strict": True, "schema": json_schema}}
        return body

    def chat(self, messages: List[Dict], json_schema: Optional[Dict] = None) -> LLMResult:
        body = self.body(messages, json_schema)
        last, kind = None, None
        for attempt in range(self.retries):
            t0 = time.time()
            try:
                r = self.http.post(self.url, json=body)
                if r.status_code >= 500:
                    kind = "server"
                    raise httpx.HTTPStatusError(f"HTTP {r.status_code}: {r.text[:300]}", request=r.request, response=r)
                if r.status_code >= 400:
                    # a request the server rejects will be rejected again: no retry
                    return LLMResult("", "", "error", {}, time.time() - t0, self.model,
                                     error=f"HTTP {r.status_code}: {r.text[:500]}", error_kind="client")
                d = r.json()
                ch = d["choices"][0]
                msg = ch["message"]
                content = msg.get("content") or ""
                reasoning = msg.get("reasoning_content") or msg.get("reasoning") or ""
                if not content.strip() and json_schema is not None and reasoning.strip().startswith("{"):
                    content = reasoning
                return LLMResult(content, reasoning, ch.get("finish_reason") or "", d.get("usage") or {},
                                 time.time() - t0, d.get("model", self.model))
            except httpx.TimeoutException as e:
                last, kind = e, "timeout"
            except (httpx.ConnectError, httpx.RemoteProtocolError, httpx.ReadError, httpx.WriteError) as e:
                last, kind = e, "connection"
            except httpx.HTTPStatusError as e:
                last = e
            except (KeyError, ValueError) as e:
                last, kind = e, "server"
            if attempt + 1 < self.retries:
                time.sleep(2 * (attempt + 1))
        return LLMResult("", "", "error", {}, 0.0, self.model, error=str(last), error_kind=kind)
