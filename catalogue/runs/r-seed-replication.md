---
id: r-seed-replication
type: run
phase: 1
status: drafted
depends_on: [{node: c-training, edge: needs}, {node: c-substrate, edge: needs}]
produces: checkpoints, logs
---

## Purpose

Thirty seeds at the main configuration, with initialization and data order varied factorially.

## Content

30 seeds (not the floor of 5 used elsewhere) at the main configuration selected by `r-diversity-sweep`, run under the Phase B objective (or whichever headline condition `s-uniqueness` targets). Initialization and data order varied **factorially** — fix one, vary the other, then the reverse — so the two sources of cross-seed variation are separable rather than confounded.

**Why 30, not 5.** Five seeds is an adequate floor for comparing means, but the cross-seed circuit comparison (`s-uniqueness`) concerns a *distribution* over solutions, not a mean. Detecting a minority solution present at 10% frequency with 95% confidence needs approximately 28 seeds; 5 would miss it three times in five and report clean convergence where none exists.

**Precondition, not yet satisfiable.** The circuit-identity metric (`records/questions.md`) must be fixed in the pre-registration artifact before this run's checkpoints are compared — without it, "the same circuit across seeds" is not a measurement.

## Migration source

Reconciled R12b.
