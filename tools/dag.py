#!/usr/bin/env python3
"""Parse node front matter and generate orders, grounding, and Mermaid DAGs.

Edge semantics:
  needs        material/engineering. Constrains EXECUTION order.
  presupposes  epistemic, fatal. If the source fails, the target is meaningless.
  calibrates   epistemic, non-fatal. Source sets a number the target uses.
  enables      epistemic, instrumental. Source establishes the instrument.
Only `needs` constrains execution. All four constrain validity.
"""
import os, re, sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXEC_EDGES = {"needs"}
NODES = {}

def parse(path):
    txt = open(path).read()
    m = re.match(r"^---\n(.*?)\n---", txt, re.S)
    if not m: return
    fm, deps = {}, []
    for line in m.group(1).split("\n"):
        if line.startswith("depends_on:"):
            for n, e in re.findall(r"\{node:\s*([\w\-]+),\s*edge:\s*(\w+)\}", line):
                deps.append((n, e))
        elif ":" in line:
            k, v = line.split(":", 1); fm[k.strip()] = v.strip()
    fm["depends_on"] = deps; fm["path"] = os.path.relpath(path, ROOT)
    if "id" in fm: NODES[fm["id"]] = fm

for d, _, fs in os.walk(ROOT):
    if "/tools" in d or "/generated" in d or "/history" in d: continue
    for f in fs:
        if f.endswith(".md"): parse(os.path.join(d, f))

def toposort(edge_filter):
    indeg = defaultdict(int); adj = defaultdict(list)
    for nid, fm in NODES.items():
        for dep, edge in fm["depends_on"]:
            if edge not in edge_filter or dep not in NODES: continue
            adj[dep].append(nid); indeg[nid] += 1
    ready = sorted(n for n in NODES if indeg[n] == 0)
    order, layers = [], []
    while ready:
        layers.append(ready); order += ready
        nxt = []
        for n in ready:
            for m in adj[n]:
                indeg[m] -= 1
                if indeg[m] == 0: nxt.append(m)
        ready = sorted(nxt)
    cycle = [n for n in NODES if n not in order]
    return layers, cycle

def roots_of(nid, seen=None):
    """Terminal ancestors: nodes with no dependencies of any kind."""
    seen = seen or set()
    if nid in seen or nid not in NODES: return set()
    seen.add(nid)
    deps = NODES[nid]["depends_on"]
    if not deps: return {nid}
    out = set()
    for dep, _ in deps: out |= roots_of(dep, seen)
    return out

def ancestors_of(nid, seen=None):
    """All transitive dependencies of a node, regardless of edge type."""
    seen = seen or set()
    if nid in seen or nid not in NODES: return set()
    seen.add(nid)
    out = set()
    for dep, _ in NODES[nid]["depends_on"]:
        if dep in NODES:
            out.add(dep)
            out |= ancestors_of(dep, seen)
    return out

def mermaid_id(nid):
    """Safe Mermaid identifier, with the canonical graph ID kept as its label."""
    return "n_" + re.sub(r"\W", "_", nid)

def mermaid_node(nid):
    fm = NODES[nid]
    label = nid + (f" ({fm['status']})" if fm.get("status") == "stub" else "")
    return f'{mermaid_id(nid)}["{label}"]'

def mermaid_edges(edge_filter):
    """Prerequisite-to-dependent Mermaid edges, sorted for stable output."""
    out = []
    for nid in sorted(NODES):
        for dep, edge in sorted(NODES[nid]["depends_on"]):
            if edge in edge_filter and dep in NODES:
                out.append(f"{mermaid_id(dep)} -->|{edge}| {mermaid_id(nid)}")
    return out

def mermaid_graph(title, direction, edge_filter):
    """Full node graph, grouped by type for GitHub's Mermaid renderer."""
    connected = set()
    for nid, fm in NODES.items():
        for dep, edge in fm["depends_on"]:
            if edge in edge_filter and dep in NODES:
                connected.update((dep, nid))
    lines = [f"%% {title}", f"flowchart {direction}", ""]
    for node_type, label in [
        ("prior-art", "Prior art"),
        ("component", "Components"),
        ("run", "Runs"),
        ("study", "Studies"),
        ("program", "Program"),
        ("index", "Indexes"),
    ]:
        members = sorted(n for n in connected if NODES[n].get("type") == node_type)
        if not members:
            continue
        lines += [f"subgraph {node_type.replace('-', '_')}[\"{label}\"]"]
        lines += [mermaid_node(n) for n in members]
        lines += ["end", ""]
    lines += mermaid_edges(edge_filter)
    return "\n".join(lines) + "\n"

def mermaid_overview():
    counts = defaultdict(int)
    for fm in NODES.values():
        counts[fm.get("type", "unknown")] += 1
    return "\n".join([
        "%% Research-program DAG overview",
        "flowchart LR",
        f'prior["Prior art ({counts["prior-art"]})"] -->|calibrates| studies["Studies ({counts["study"]})"]',
        f'components["Components ({counts["component"]})"] -->|needs| runs["Runs ({counts["run"]})"]',
        f'components -->|needs / enables| studies',
        f'runs -->|needs| studies',
        f'studies -->|presupposes / enables| studies',
        "",
    ])

def mermaid_grounding():
    grounded, derived = [], []
    for nid in sorted(n for n in NODES if NODES[n].get("type") == "study"):
        if "c-inst-derived" in ancestors_of(nid):
            derived.append(nid)
        else:
            grounded.append(nid)
    lines = [
        "%% Grounding and derived-instrument ancestry",
        "flowchart TB",
        "",
        'grounded_instruments["c-inst-grounded"] -->|calibrates| derived_instruments["c-inst-derived"]',
        "",
        "subgraph grounded_studies[\"Studies with no derived-instrument ancestry\"]",
    ]
    lines += [mermaid_node(n) for n in grounded]
    lines += ["end", "", "subgraph derived_studies[\"Studies with derived-instrument ancestry\"]"]
    lines += [mermaid_node(n) for n in derived]
    lines += ["end", ""]
    lines += [f"grounded_instruments -->|grounded ancestry| {mermaid_id(n)}" for n in grounded]
    lines += [f"derived_instruments -. derived ancestry .-> {mermaid_id(n)}" for n in derived]
    return "\n".join(lines) + "\n"

def write_mermaid():
    directory = os.path.join(ROOT, "generated", "mermaid")
    os.makedirs(directory, exist_ok=True)
    files = {
        "overview.mmd": mermaid_overview(),
        "execution.mmd": mermaid_graph("Execution DAG: needs edges", "LR", {"needs"}),
        "validity.mmd": mermaid_graph("Validity DAG: all dependency edges", "TB", {"needs", "presupposes", "calibrates", "enables"}),
        "grounding.mmd": mermaid_grounding(),
    }
    for name, content in files.items():
        open(os.path.join(directory, name), "w").write(content)
    index = """# Mermaid DAGs

*Generated by `python3 tools/dag.py`. Do not edit by hand.*

- [Overview](overview.mmd) — the program's four node categories and edge types.
- [Execution DAG](execution.mmd) — only `needs` edges; use it to see what can start in parallel.
- [Validity DAG](validity.mmd) — every edge type; use it to see what must hold before a claim is interpretable.
- [Grounding DAG](grounding.mmd) — the boundary between probe-free and derived instruments, projected through transitive ancestry.
"""
    open(os.path.join(directory, "index.md"), "w").write(index)
    return len(files)

out = ["# Generated orders and grounding report",
       "", "*Regenerate with `python3 tools/dag.py`. Do not edit by hand.*", ""]

for title, filt, note in [
    ("Execution order", EXEC_EDGES, "What can be started when. Only material and engineering edges. Everything in a layer can proceed in parallel."),
    ("Validity order", {"needs","presupposes","calibrates","enables"}, "What can be claimed when. All edge types. A study may execute early and remain uninterpretable until its epistemic ancestors land."),
]:
    layers, cycle = toposort(filt)
    out += [f"## {title}", "", note, ""]
    for i, layer in enumerate(layers, 1):
        out.append(f"**Layer {i}** — " + ", ".join(f"`{n}`" for n in layer))
        out.append("")
    if cycle:
        out += ["**CYCLE DETECTED** involving: " + ", ".join(f"`{n}`" for n in sorted(cycle)), ""]
    else:
        out += ["*No cycle.*", ""]

out += ["## Grounding report", "",
        "For each study: its declared grounding, whether a derived instrument appears anywhere in its transitive ancestry, and its terminal ancestors. The ancestry scan, not the terminal-root list, checks the grounding rule.", ""]
out += ["| Study | Grounding | Derived-instrument ancestry | Terminal ancestors |", "|---|---|---|---|"]
grounding_errors = []
for nid in sorted(n for n in NODES if NODES[n].get("type") == "study"):
    r = sorted(roots_of(nid) - {nid})
    derived = "c-inst-derived" in ancestors_of(nid)
    grounding = NODES[nid].get("grounding", "?")
    out.append(f"| `{nid}` | {grounding} | {'yes' if derived else 'no'} | " + ", ".join(f"`{x}`" for x in r) + " |")
    if grounding == "grounded" and derived:
        grounding_errors.append(nid)

if grounding_errors:
    out += ["", "**GROUNDING ERROR** — studies marked `grounded` with derived-instrument ancestry: " + ", ".join(f"`{n}`" for n in grounding_errors)]

out += ["", "## Imported claims and their dependents", "",
        "Contested prior art propagates to everything below it.", ""]
for nid in sorted(n for n in NODES if NODES[n].get("type") == "prior-art"):
    dependents = sorted(m for m in NODES if any(d == nid for d, _ in NODES[m]["depends_on"]))
    conf = NODES[nid].get("confidence", "?")
    out.append(f"- `{nid}` ({conf}) → " + (", ".join(f"`{d}`" for d in dependents) if dependents else "*nothing yet*"))

open(os.path.join(ROOT, "generated", "orders.md"), "w").write("\n".join(out) + "\n")
mermaid_count = write_mermaid()
print(f"{len(NODES)} nodes; wrote generated/orders.md and {mermaid_count} Mermaid DAGs")
if grounding_errors:
    sys.exit(1)
