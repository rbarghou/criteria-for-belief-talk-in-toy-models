---
id: s-decodability-timing
type: study
phase: 1
status: drafted
primary_outcome: Whether belief decodability rises before, at, or after the behavioural transition, and which of the probe targets rises at all.
grounding: derived
depends_on: [{node: r-phase-b-main, edge: needs}, {node: c-inst-derived, edge: needs}, {node: s-transition-boundary, edge: presupposes}, {node: s-tooling-validation, edge: enables}, {node: p-compositional-data, edge: needs}]
---

## Purpose

The protocol's original headline. Meaningless without a transition to time against.

## Content

Fit the four `c-inst-derived` probe targets (full predictive in clr, normalized-counts/total-evidence split, argmax class, decision margin) at every checkpoint of `r-phase-b-main`, at both opponent-token and action-emission positions, and plot excess decodability (over the random-init, raw-feature, and matched-round-index shuffle controls) against training step.

**Primary outcome, precisely.** Whether each of the four rises at, before, or after `s-transition-boundary`'s behavioural transition — and which of the four rises at all. This was the protocol's original headline measurement; it is meaningless without a transition to time against, which is why it presupposes `s-transition-boundary` rather than merely needing its runs. It in turn enables `s-tooling-validation`: a decodability profile that matches the staged uniform→unigram→bigram structure reported for the same inference problem elsewhere (`p-statistical-induction-heads`) is itself a piece of evidence the tooling is finding something real rather than an artifact of the probe-fitting procedure.

## Migration source

Protocol rev.2 §9.2. Reconciled R6, R14.
