#!/usr/bin/env python3
"""Write repair batches for items that a sub-agent did not return (refusals or truncated output)."""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
man = json.loads((HERE / "batches/manifest.json").read_text())
batch, size = sys.argv[1], int(sys.argv[2])
m = next(x for x in man if x["batch"] == batch)
out = HERE / "outputs" / f"{batch}.jsonl"
done = set()
if out.exists():
    for l in out.read_text().splitlines():
        try: done.add(json.loads(l)["id"])
        except Exception: pass
miss = [i for i in m["ids"] if i not in done]
text = (HERE / "batches" / f"{batch}.md").read_text()
head = text[:text.index("## Item ")]
items = {mm.group(1): mm.group(0) for mm in re.finditer(r"## Item (\S+)\n.*?(?=\n## Item |\Z)", text, re.S)}
for k in range(0, len(miss), size):
    name = f"{batch}_r{k // size}"
    (HERE / "batches" / f"{name}.md").write_text(head + "\n".join(items[i] for i in miss[k:k + size]) + "\n")
    man.append({"batch": name, "condition": m["condition"], "dataset": m["dataset"], "ids": miss[k:k + size], "repair_of": batch})
    print(name, len(miss[k:k + size]))
(HERE / "batches/manifest.json").write_text(json.dumps(man, indent=1))
