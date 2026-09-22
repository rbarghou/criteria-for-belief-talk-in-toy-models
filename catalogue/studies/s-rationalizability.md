---
id: s-rationalizability
type: study
phase: 1
status: drafted
primary_outcome: Whether the observed action sequence admits any consistent belief trajectory, independent of whether it is the correct one.
grounding: grounded
depends_on: [{node: r-phase-c-action, edge: needs}, {node: r-phase-c-stakevec, edge: needs}, {node: c-inst-grounded, edge: needs}]
---

## Purpose

Separates the model being wrong from the model not doing the kind of thing that admits of being right or wrong. Fully grounded: needs no probe.

## Content

On `r-phase-c-action` and `r-phase-c-stakevec` checkpoints, ask whether the observed action sequence admits *some* consistent belief trajectory — any sequence of posteriors under which the actions taken would be individually rational — independent of whether that trajectory matches the true or decoded posterior.

**Why this is a distinct study rather than folded into belief-usage measurement.** `s-representation-vs-demand` and the usage components of `c-inst-grounded`/`c-inst-derived` both measure *agreement* with a reference belief — they are accuracy measures. Neither asks whether the action sequence is coherent at all, so neither can distinguish "the model is wrong" from "the model is not doing the kind of thing that admits of being right or wrong." This study adds exactly that check. It is fully grounded — no probe is needed, since rationalizability is a property of the action sequence alone against the space of possible belief trajectories, not of decoded internal states — cheap, and nothing else in the battery measures it.

## Migration source

Reconciled R11.
