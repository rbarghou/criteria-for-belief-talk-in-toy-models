---
id: decisions
type: index
status: drafted
---

# Decisions log

One line per decision, with the reason, so it does not get relitigated. Add to the top.

## 2026-09-23 — `s-causal-structure` reclassified from `grounded` to `derived`
Resolves the tension logged 2026-09-22 below. Ramsey's ruling: grounding should describe the whole causal chain a claim rests on, not just its last step — a study that presupposes a `derived` study for target selection is not fully grounded even if the measurement it finally takes is probe-free, because the schema's `grounded`/`derived` split exists to say what a study's *conclusion* can be trusted without, and this one can't be trusted without the decodability result that picked its ablation target. Reclassified; `depends_on` unchanged (the `presupposes` edge to `s-decodability-timing` already correctly described the relationship — only the summary field was wrong).

## 2026-09-23 — Confirmed: the dag.py 45→42 expectation was never true, not a regression
Checked out the very first skeleton commit (`da4a899`, before any migration content and before the `/history` exclusion existed) and ran its own unmodified `tools/dag.py` against it: 45 nodes, same as today. The 42-node expectation in the original handoff was false at the moment the skeleton was created, not something that drifted during migration or was broken by the exclusion fix. No further action needed on the tool; the record is corrected rather than the count forced to match a target that was never real.

## 2026-09-22 — Flagging, not resolving: `s-causal-structure` claims `grounded` but presupposes a `derived` study
`s-causal-structure` (grounding: grounded) has a `presupposes` edge to `s-decodability-timing` (grounding: derived, needs `c-inst-derived`). The written rule — "a study claiming grounded shouldn't have a `needs` or `calibrates` edge into `c-inst-derived`" — is satisfied literally: there is no direct `needs`/`calibrates` edge from `s-causal-structure` into `c-inst-derived`, and the ablation-effect measurements themselves are probe-free. But the *reason* `s-causal-structure` presupposes `s-decodability-timing` is that it needs a decodability result to identify which component is even a candidate for ablation — the target of the grounded measurement is selected by a derived one. **Resolved 2026-09-23 above: reclassified as `derived`.**

## 2026-09-22 — `tools/dag.py` excludes `/history` from the walk, but the node count does not move
Added the exclusion the handoff asked for (matches `/tools` and `/generated` treatment; `history/` is frozen source material, not graph content, and should never be eligible for parsing on principle). But the handoff's own verification step — "node count drops from 45 to 42" — does not hold: the count is 45 both before and after the change. None of the five `history/*.md` files begin with a literal `---` at byte 0 (they open with a `#` heading and bold metadata lines); the parser's front-matter regex is anchored to the start of the file, so the walker was never actually pulling nodes out of `history/` in the first place, exclusion or not. **Confirmed 2026-09-23 above: this was true from the skeleton's first commit, not a migration-induced drift.**

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
