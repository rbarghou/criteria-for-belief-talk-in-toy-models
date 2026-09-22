# Node schema

Every document carries YAML-ish front matter. Keep it small: seven fields maximum, four edge types, nothing else until something actually demands more.

```
---
id: s-decodability-timing
type: study                  # program | component | run | study | prior-art | index
phase: 1                     # studies and runs only
status: stub                 # stub | drafted | ready | running | done | stale
primary_outcome: ...         # studies only — exactly one, one sentence
grounding: derived           # studies only — grounded | derived
produces: checkpoints, logs  # runs only
provides: ...                # components only
confidence: ...              # prior-art only
depends_on: [{node: r-phase-b-main, edge: needs}, {node: s-transition-boundary, edge: presupposes}]
---
```

## Rules

1. **One primary outcome per study.** If a study needs two, it is two studies. This is the rule the whole structure exists to enforce.
2. **Only `needs` constrains execution.** The other three constrain validity.
3. **`grounding: grounded`** means the conclusion rests only on probe-free instruments. Claiming it while transitively depending on `c-inst-derived` is an error; the tool reports it and exits unsuccessfully.
4. **Prior art gets nodes, not citations.** An imported claim carries a confidence marker and propagates it downward.
5. **`generated/` is never hand-edited.** Regenerate with `python3 tools/dag.py`.
6. **Status `stale`** is set on anything downstream of a re-done run. Propagating it automatically is the reason this exists rather than a notebook.
7. **Component and catalogue-node filenames** use their graph ID (`<id>.md`). Descriptive index documents, including `catalogue/phases.md`, `program/orientation.md`, and `records/*.md`, are exempt.

## What is deliberately absent

No priority field, no owner, no estimates, no dates. Those belong to a scheduler, not to the epistemic structure, and adding them is how a small schema stops being small.
