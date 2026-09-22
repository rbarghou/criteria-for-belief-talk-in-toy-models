---
id: r-solver-verification
type: run
phase: 1
status: stub
depends_on: [{node: c-solvers, edge: needs}]
produces: checkpoints, logs
---

## Purpose

Monte Carlo check that the posterior converges at the expected rate and that best response, margin and stake match brute force. Hard gate: nothing proceeds until it passes.

## Content

*(stub — not yet migrated)*

## Migration source

Protocol rev.2 §6 verification requirement. Add: posterior with zero observations must equal the prior.
