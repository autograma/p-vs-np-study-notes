#!/usr/bin/env python3
"""Regenerate GitHub-renderable copies from the pandoc sources in src/.

Workflow: edit ONLY the files under */src/ (pandoc math dialect: $...$ and
$$...$$), then run  `python3 convert.py`  from the repository root. This
rewrites the display copies (GitHub math dialect: $`...`$ and ```math fences)
so the two versions never drift apart.
"""
import re

PAIRS = [
    ("survey/src/p-vs-np-corridor.md", "survey/p-vs-np-corridor.md"),
    ("notes/src/theory-of-computation-notes.md", "notes/theory-of-computation-notes.md"),
]


def to_github_math(src_path: str, dst_path: str) -> None:
    lines = open(src_path, encoding="utf-8").read().split("\n")
    out, in_fence = [], False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        m = re.fullmatch(r"\$\$(.+)\$\$", stripped)
        if m and not line.lstrip().startswith(">"):
            indent = line[: len(line) - len(line.lstrip())]
            out += [indent + "```math", indent + m.group(1).strip(), indent + "```"]
            continue
        line = re.sub(r"\$\$(.+?)\$\$", lambda mo: "$`" + mo.group(1).strip() + "`$", line)
        line = re.sub(
            r"(?<![\$`])\$(?!\$)([^\$\n`]+?)\$(?!\$)",
            lambda mo: "$`" + mo.group(1) + "`$",
            line,
        )
        out.append(line)
    open(dst_path, "w", encoding="utf-8").write("\n".join(out))


if __name__ == "__main__":
    for src, dst in PAIRS:
        to_github_math(src, dst)
        print(f"regenerated {dst}  <-  {src}")
