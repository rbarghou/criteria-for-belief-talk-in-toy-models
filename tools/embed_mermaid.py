#!/usr/bin/env python3
"""Embed Mermaid files linked from an index into one Markdown preview document."""
import re
import sys
from pathlib import Path

LINK = re.compile(r"^- \[([^\]]+)\]\(([^)]+\.mmd)\)(?: — (.*))?$")

def main(index_arg, output_arg):
    index = Path(index_arg)
    output = Path(output_arg)
    diagrams = []
    for line in index.read_text().splitlines():
        match = LINK.match(line)
        if match:
            title, relative_path, description = match.groups()
            diagrams.append((title, index.parent / relative_path, description))
    if not diagrams:
        raise ValueError(f"No Mermaid links found in {index}")

    lines = ["# Rendered Mermaid DAGs", "", "*Generated from `index.md`. Do not edit by hand.*", ""]
    for title, path, description in diagrams:
        if not path.is_file():
            raise FileNotFoundError(path)
        lines += [f"## {title}", ""]
        if description:
            lines += [description, ""]
        lines += ["```mermaid", path.read_text().rstrip(), "```", ""]
    output.write_text("\n".join(lines))
    print(f"embedded {len(diagrams)} Mermaid diagrams in {output}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: embed_mermaid.py INDEX.md OUTPUT.md")
    main(sys.argv[1], sys.argv[2])
