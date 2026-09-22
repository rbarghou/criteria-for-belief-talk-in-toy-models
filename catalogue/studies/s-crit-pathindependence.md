---
id: s-crit-pathindependence
type: study
phase: 1
status: drafted
primary_outcome: Whether the representation converges for the same evidence reached by different orderings.
grounding: derived
depends_on: [{node: r-phase-b-main, edge: needs}, {node: c-inst-derived, edge: needs}]
---

## Purpose

Analysis on existing checkpoints; needs no new run.

## Content

Third of the four criteria. On existing `r-phase-b-main` checkpoints — no new run needed — construct multiple orderings of opponent-action evidence that arrive at the *same* count matrix (the same total evidence, permuted in sequence), feed each ordering through the network, and compare the resulting decoded (and, where possible, raw activation) state.

**Primary outcome, precisely.** Whether the representation converges to the same state for the same evidence reached by different orderings, or instead retains a trace of the specific ordering seen. Convergent representation across orderings is what a *state* summary (a genuine posterior, which by the mathematics of conjugate updating should not depend on order) looks like; retained ordering is what a *trace* (a sequential memory of the specific history) looks like, and a trace is closer to what a pure sequence-model function approximator would be expected to build.

**Relation to the other criteria.** This is the cheapest of the four to run, since generating alternative orderings requires no new training or intervention machinery — only replaying evidence in different sequences through frozen checkpoints — and it is the most direct probe-based test of whether the "posterior" language is doing real work rather than describing a sequential summary that happens to correlate with the true posterior on the orderings actually seen during training.

## Migration source

Reconciled R15 criterion 3.
