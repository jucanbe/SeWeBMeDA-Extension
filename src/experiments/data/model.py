"""Common in-memory representation of original and synthetic sentences."""
import hashlib
import re
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# (start_token, end_token_exclusive, type)
Span = Tuple[int, int, str]

ORIGINAL = "original"
SYNTHETIC = "synthetic"
S_FULL = "S-full"
S_TRAIN = "S-train"


@dataclass
class Sentence:
    dataset: str
    split: str                      # train | dev | test | synthetic
    sid: str                        # stable identifier, e.g. "bc5cdr:train:42"
    tokens: List[str]
    spans: List[Span] = field(default_factory=list)
    origin: str = ORIGINAL          # original | synthetic
    track: Optional[str] = None     # None for original data, S-full / S-train for synthetic
    label_source: str = "gold"      # gold | silver:<annotator> | none
    provenance: Dict = field(default_factory=dict)

    @property
    def text(self) -> str:
        """The unit shown to the LLM: tokens joined by single spaces."""
        return " ".join(self.tokens)

    def mentions(self) -> List[Tuple[str, str]]:
        return [(" ".join(self.tokens[s:e]), t) for s, e, t in self.spans]

    def to_dict(self) -> Dict:
        d = asdict(self)
        d["text"] = self.text
        return d


def bio_to_spans(labels: List[str]) -> Tuple[List[Span], int]:
    """Convert BIO tags to spans.

    An I- tag that does not continue a span of the same type starts a new span
    (conlleval / seqeval default behaviour). Returns (spans, repaired_count).
    """
    spans: List[Span] = []
    start, cur_type, repaired = None, None, 0
    for i, label in enumerate(labels):
        label = label or "O"
        if label.startswith("B-"):
            if cur_type is not None:
                spans.append((start, i, cur_type))
            start, cur_type = i, label[2:]
        elif label.startswith("I-"):
            if cur_type == label[2:]:
                continue
            repaired += 1
            if cur_type is not None:
                spans.append((start, i, cur_type))
            start, cur_type = i, label[2:]
        else:
            if cur_type is not None:
                spans.append((start, i, cur_type))
            start, cur_type = None, None
    if cur_type is not None:
        spans.append((start, len(labels), cur_type))
    return spans, repaired


def spans_to_bio(n_tokens: int, spans: List[Span]) -> List[str]:
    tags = ["O"] * n_tokens
    for s, e, t in sorted(spans):
        if any(tags[i] != "O" for i in range(s, e)):
            continue  # overlapping spans cannot be represented in BIO; keep the first
        tags[s] = f"B-{t}"
        for i in range(s + 1, e):
            tags[i] = f"I-{t}"
    return tags


_TOKEN_RE = re.compile(r"\w+(?:[-‑']\w+)*|[^\w\s]", re.UNICODE)


def tokenize(text: str) -> List[str]:
    """Word/punctuation tokenizer approximating the benchmarks' tokenization."""
    return _TOKEN_RE.findall(text)


_NO_SPACE_BEFORE = {".", ",", ";", ":", "!", "?", ")", "]", "}", "%", "'s"}
_NO_SPACE_AFTER = {"(", "[", "{"}


def detokenize(tokens: List[str]) -> str:
    """Deterministic detokenizer used to build natural-text generator references."""
    out = ""
    for i, tok in enumerate(tokens):
        if i == 0:
            out = tok
        elif tok in _NO_SPACE_BEFORE or out.endswith(tuple(_NO_SPACE_AFTER)):
            out += tok
        else:
            out += " " + tok
    return out


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def normalize_mention(text: str) -> str:
    """Normalisation used for lexicon/KG lookups (case, whitespace, dashes)."""
    text = text.lower().replace("‑", "-").replace("–", "-")
    return " ".join(text.split())
