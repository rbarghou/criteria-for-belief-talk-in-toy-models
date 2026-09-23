#!/usr/bin/env python3
"""Parse node front matter and generate orders, grounding, and Mermaid DAGs.

Edge semantics:
  needs        material/engineering. Constrains EXECUTION order.
  presupposes  epistemic, fatal. If the source fails, the target is meaningless.
  calibrates   epistemic, non-fatal. Source sets a number the target uses.
  enables      epistemic, instrumental. Source establishes the instrument.
Only `needs` constrains execution. All four constrain validity.
"""
import os, re, subprocess, sys
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

VIEWS = [
    {
        "filename": "overview.mmd",
        "title": "Research-program overview",
        "direction": "LR",
        "nodes": {
            "prior": (None, "Prior-art<br/>claims"),
            "components": (None, "Shared<br/>components"),
            "runs": (None, "Training<br/>runs"),
            "studies": (None, "Pre-registered<br/>studies"),
        },
        "edges": [
            ("prior", "studies", "calibrates"),
            ("components", "runs", "needs"),
            ("components", "studies", "needs / enables"),
            ("runs", "studies", "needs"),
            ("studies", "studies", "presupposes / enables"),
        ],
    },
    {
        "filename": "foundation.mmd",
        "title": "Shared foundation and run production",
        "direction": "LR",
        "nodes": {
            "terminology": ("c-terminology", "Shared<br/>terminology"),
            "substrate": ("c-substrate", "Game and data<br/>substrate"),
            "solver": ("c-solvers", "Reference<br/>solver"),
            "grounded": ("c-inst-grounded", "Probe-free<br/>instruments"),
            "derived": ("c-inst-derived", "Probe-based<br/>instruments"),
            "training": ("c-training", "Training<br/>framework"),
            "verification": ("r-solver-verification", "Solver<br/>verification"),
            "prediction": ("r-phase-b-main", "Prediction<br/>run"),
            "policy": (None, "Policy-gradient<br/>run family"),
            "support": (None, "Supporting<br/>run family"),
        },
        "edges": [
            ("terminology", "substrate", "needs"),
            ("substrate", "solver", "needs"),
            ("solver", "grounded", "needs"),
            ("grounded", "derived", "calibrates"),
            ("substrate", "training", "needs"),
            ("solver", "training", "needs"),
            ("solver", "verification", "needs"),
            ("training", "prediction", "needs"),
            ("training", "policy", "needs"),
            ("training", "support", "needs"),
        ],
    },
    {
        "filename": "calibration-spine.mmd",
        "title": "Calibration and interpretability spine",
        "direction": "TB",
        "nodes": {
            "diversity": ("r-diversity-sweep", "Diversity<br/>sweep"),
            "grounded": ("c-inst-grounded", "Probe-free<br/>instruments"),
            "boundary": ("p-diversity-boundary", "Diversity-boundary<br/>prior art"),
            "transition": ("s-transition-boundary", "Behavioral<br/>transition"),
            "prediction": ("r-phase-b-main", "Prediction<br/>run"),
            "derived": ("c-inst-derived", "Probe-based<br/>instruments"),
            "composition": ("p-compositional-data", "Compositional-data<br/>prior art"),
            "tooling": ("s-tooling-validation", "Tooling<br/>validation"),
            "decoding": ("s-decodability-timing", "Decodability<br/>over training"),
        },
        "edges": [
            ("diversity", "transition", "needs"),
            ("grounded", "transition", "needs"),
            ("boundary", "transition", "calibrates"),
            ("transition", "decoding", "presupposes"),
            ("prediction", "decoding", "needs"),
            ("derived", "decoding", "needs"),
            ("composition", "decoding", "needs"),
            ("tooling", "decoding", "enables"),
        ],
    },
    {
        "filename": "causal-evidence.mmd",
        "title": "Grounded causal evidence",
        "direction": "LR",
        "nodes": {
            "prediction": ("r-phase-b-main", "Prediction-run<br/>checkpoints"),
            "stake": ("r-phase-c-stakevec", "Stake-vector<br/>checkpoints"),
            "grounded": ("c-inst-grounded", "Probe-free<br/>instruments"),
            "decoding": ("s-decodability-timing", "Decodability<br/>timing"),
            "causal": ("s-causal-structure", "Causal<br/>structure"),
            "counting": ("s-counting-vs-retrieval", "Counting versus<br/>retrieval"),
        },
        "edges": [
            ("prediction", "causal", "needs"),
            ("stake", "causal", "needs"),
            ("grounded", "causal", "needs"),
            ("decoding", "causal", "selects target"),
            ("prediction", "counting", "needs"),
            ("grounded", "counting", "needs"),
        ],
    },
    {
        "filename": "derived-criteria.mmd",
        "title": "Derived criterion suite",
        "direction": "LR",
        "nodes": {
            "checkpoints": (None, "Phase-1 checkpoint corpus:<br/>prediction and stake-vector runs"),
            "derived": ("c-inst-derived", "Probe-based<br/>instruments"),
            "criteria": (None, "Three derived criteria:<br/>off-manifold coherence<br/>path independence<br/>residual following"),
            "multirun": ("r-multiconsumer", "Multi-consumer<br/>run · stub"),
            "tooling": ("s-tooling-validation", "Tooling<br/>validation"),
            "multi": ("s-crit-multiconsumer", "Multi-consumer<br/>criterion · stub"),
        },
        "edges": [
            ("checkpoints", "criteria", "needs"),
            ("derived", "criteria", "needs"),
            ("multirun", "multi", "needs"),
            ("derived", "multi", "needs"),
            ("tooling", "multi", "enables"),
        ],
    },
    {
        "filename": "action-channels.mmd",
        "title": "Action-channel comparisons",
        "direction": "LR",
        "nodes": {
            "outputs": (None, "Policy-output runs:<br/>action-only and auxiliary"),
            "decoding": ("s-decodability-timing", "Decodability<br/>timing"),
            "payoff": ("s-payoff-alone", "Payoff-only<br/>comparison"),
            "channels": (None, "Action-channel comparison:<br/>action-only, single stake,<br/>stake vector"),
            "demand": ("s-representation-vs-demand", "Representation versus<br/>behavioral demand"),
            "behavior": (None, "Action-behavior runs:<br/>action-only and stake vector"),
            "grounded": ("c-inst-grounded", "Probe-free<br/>instruments"),
            "rational": ("s-rationalizability", "Belief<br/>rationalizability"),
        },
        "edges": [
            ("outputs", "payoff", "needs"),
            ("decoding", "payoff", "calibrates"),
            ("channels", "demand", "needs"),
            ("decoding", "demand", "enables"),
            ("behavior", "rational", "needs"),
            ("grounded", "rational", "needs"),
        ],
    },
    {
        "filename": "history-and-replication.mmd",
        "title": "Training history and replication",
        "direction": "LR",
        "nodes": {
            "prediction": ("r-phase-b-main", "Prediction<br/>run"),
            "curriculum": ("r-curriculum", "Curriculum<br/>run"),
            "decoding": ("s-decodability-timing", "Decodability<br/>timing"),
            "persistence": ("s-belief-persistence", "Belief<br/>persistence"),
            "seeds": ("r-seed-replication", "Seed-replication<br/>run"),
            "derived": ("c-inst-derived", "Probe-based<br/>instruments"),
            "tooling": ("s-tooling-validation", "Tooling<br/>validation"),
            "multiplicity": ("p-algorithm-multiplicity", "Algorithm-multiplicity<br/>prior art"),
            "uniqueness": ("s-uniqueness", "Circuit<br/>uniqueness · stub"),
        },
        "edges": [
            ("prediction", "persistence", "needs"),
            ("curriculum", "persistence", "needs"),
            ("decoding", "persistence", "calibrates"),
            ("seeds", "uniqueness", "needs"),
            ("derived", "uniqueness", "needs"),
            ("tooling", "uniqueness", "enables"),
            ("multiplicity", "uniqueness", "calibrates"),
        ],
    },
]

def render_view(view):
    """Render a deliberately curated Mermaid view, not the raw full graph."""
    for node_id, _ in view["nodes"].values():
        if node_id is not None and node_id not in NODES:
            raise ValueError(f"{view['filename']}: unknown node {node_id}")
    lines = [f"%% {view['title']}", f"flowchart {view['direction']}", ""]
    for alias, (_, label) in view["nodes"].items():
        lines.append(f'{alias}["{label}"]')
    lines.append("")
    for source, target, label in view["edges"]:
        lines.append(f"{source} -->|{label}| {target}")
    return "\n".join(lines) + "\n"

def write_mermaid():
    directory = os.path.join(ROOT, "generated", "mermaid")
    os.makedirs(directory, exist_ok=True)
    files = {view["filename"]: render_view(view) for view in VIEWS}
    for name in os.listdir(directory):
        if name.endswith(".mmd") and name not in files:
            os.remove(os.path.join(directory, name))
    for name, content in files.items():
        open(os.path.join(directory, name), "w").write(content)
    index = """# Mermaid DAGs

*Generated by `python3 tools/dag.py`. Do not edit by hand.*

- [Rendered diagrams for Markdown preview](rendered.md) — fenced Mermaid blocks for VS Code and GitHub Markdown preview.
- [Program overview](overview.mmd)
- [Shared foundation and run production](foundation.mmd)
- [Calibration and interpretability spine](calibration-spine.mmd)
- [Grounded causal evidence](causal-evidence.mmd)
- [Derived criterion suite](derived-criteria.mmd)
- [Action-channel comparisons](action-channels.mmd)
- [Training history and replication](history-and-replication.mmd)
"""
    index_path = os.path.join(directory, "index.md")
    rendered_path = os.path.join(directory, "rendered.md")
    open(index_path, "w").write(index)
    subprocess.run([sys.executable, os.path.join(ROOT, "tools", "embed_mermaid.py"), index_path, rendered_path], check=True)
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
