"""Minimal stand-in for `vllm serve` used by the tests (OpenAI-compatible subset).

Accepts the same command line. Chat: returns the first enum type for the first
token of the last user sentence. Embeddings: deterministic hash vectors.
FAKE_VLLM_CRASH_AFTER=N makes the process exit after N chat requests (only once:
a marker file next to FAKE_VLLM_STATE records that it crashed).
FAKE_VLLM_BAD_JSON=1 returns non-JSON content (tests failure handling).
"""
import hashlib
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

args = sys.argv[1:]
model = args[args.index("serve") + 1]
port = int(args[args.index("--port") + 1])
served = args[args.index("--served-model-name") + 1] if "--served-model-name" in args else model
if os.environ.get("FAKE_VLLM_REJECT_FLAG") and os.environ["FAKE_VLLM_REJECT_FLAG"] in args:
    print(f"vllm serve: error: unrecognized arguments: {os.environ['FAKE_VLLM_REJECT_FLAG']}", flush=True)
    sys.exit(2)
state = os.environ.get("FAKE_VLLM_STATE", "")
crash_after = int(os.environ.get("FAKE_VLLM_CRASH_AFTER", "0"))
count = {"n": 0}
# test oracle: {first enum type of a dataset: {lower-cased mention: type}} (noisy, see do_POST)
LEXICON = json.loads(open(os.environ["FAKE_VLLM_LEXICON"]).read()) if os.environ.get("FAKE_VLLM_LEXICON") else {}


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/health":
            return self._send(200, {})
        if self.path == "/v1/models":
            return self._send(200, {"data": [{"id": served}]})
        if self.path == "/version":
            return self._send(200, {"version": "0.0.0-fake"})
        self._send(404, {})

    def do_POST(self):
        req = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        if self.path == "/v1/embeddings":
            data = []
            for i, t in enumerate(req["input"]):
                h = hashlib.sha256(t.encode()).digest()
                data.append({"index": i, "embedding": [b / 255.0 for b in h[:16]]})
            return self._send(200, {"data": data})
        count["n"] += 1
        if crash_after and count["n"] > crash_after and state and not os.path.exists(state + ".crashed"):
            open(state + ".crashed", "w").write("1")
            os._exit(1)
        user = [m["content"] for m in req["messages"] if m["role"] == "user"][-1]
        sentence = user.split("Sentence:", 1)[-1].strip()
        enum = req["response_format"]["json_schema"]["schema"]["properties"]["entities"]["items"]["properties"]["type"]["enum"]
        first = sentence.split()[0] if sentence.split() else "x"
        ents = [{"text": first, "type": enum[0], "confidence": 0.55}]
        lex = LEXICON.get(enum[0]) or {}
        low = " " + sentence.lower() + " "
        for m, t in lex.items():
            if f" {m} " in low and t in enum:
                h = int(hashlib.md5((m + sentence).encode()).hexdigest(), 16) % 10
                text = sentence[low.index(f" {m} "):low.index(f" {m} ") + len(m)]
                ents.append({"text": text, "type": t if h < 7 else enum[(enum.index(t) + 1) % len(enum)],
                             "confidence": 0.95 if h < 7 else 0.6})
        content = json.dumps({"entities": ents})
        if os.environ.get("FAKE_VLLM_BAD_JSON") == "1":
            content = "not json"
        self._send(200, {"model": served, "choices": [{"message": {"content": content}, "finish_reason": "stop"}],
                         "usage": {"prompt_tokens": 10, "completion_tokens": 5}})


ThreadingHTTPServer(("127.0.0.1", port), H).serve_forever()
