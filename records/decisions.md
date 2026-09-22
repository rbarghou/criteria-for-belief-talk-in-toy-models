---
id: decisions
type: index
status: drafted
---

# Decisions log

One line per decision, with the reason, so it does not get relitigated. Add to the top.

## 2026-09-22 — `s-causal-structure` is derived at the claim level
`s-causal-structure` measures ablation effects with grounded instruments, but it presupposes `s-decodability-timing` to select the candidate structure. That study depends on `c-inst-derived`, so the causal study's full evidential chain is derived. Its `grounding` is therefore `derived`; the prose retains the distinction that its final measurements are probe-free. The schema and graph tool now enforce this rule transitively, rather than only making a direct-edge distinction.

## 2026-09-22 — `tools/dag.py` excludes `/history` from the walk, but the node count does not move
Added the exclusion the handoff asked for (matches `/tools` and `/generated` treatment; `history/` is frozen source material, not graph content, and should never be eligible for parsing on principle). But the handoff's own verification step — "node count drops from 45 to 42" — does not hold: the count is 45 both before and after the change. None of the five `history/*.md` files begin with a literal `---` at byte 0 (they open with a `#` heading and bold metadata lines); the parser's front-matter regex is anchored to the start of the file, so the walker was never actually pulling nodes out of `history/` in the first place, exclusion or not. Flagging rather than adjusting the exclusion logic to force a number that isn't real — if a 42-node state is expected, something else changed (e.g. three of the current 45 nodes may not have existed at the point that expectation was written), and that should be checked against the source rather than assumed.

## 2026-09-22 — Experiment 1 uses an opponent agnostic to the player's last action
A reacting opponent destroys the exact ceiling, which is the reason for choosing this substrate at all, and none of the four criteria need it. The reacting opponent becomes phase 2. Declined alternative: a mixed pool letting the first run ask whether a model can tell it is being responded to.

## 2026-09-22 — The unit of pre-registration is the study, not the experiment
A study has exactly one primary outcome. "Experiment 1" is a phase — a named subset of studies — not a document.

## 2026-09-22 — Residual-following is a full criterion, not an optional fourth
It was logged as "arguably" a criterion while simultaneously being treated as a precondition for the testimony work. The stronger reading wins.

## 2026-09-22 — The rationalizability check is included
Cheap, and the only measurement that separates the model being wrong from the model not doing the kind of thing that admits of being right or wrong.

## 2026-09-22 — Direction-level temporal ablation is dropped
Separate fits at different checkpoints give no principled reason to call the result the same component. Head-level only.

## 2026-09-22 — The deliverable is validated criteria, not a found circuit
Criteria transfer across coordinates; calibrations do not. If the project produces only a validated probe direction, it has produced nothing that survives the next move.
