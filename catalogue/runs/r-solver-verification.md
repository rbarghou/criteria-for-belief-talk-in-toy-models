---
id: r-solver-verification
type: run
phase: 1
status: drafted
depends_on: [{node: c-solvers, edge: needs}]
produces: checkpoints, logs
---

## Purpose

Monte Carlo check that the posterior converges at the expected rate and that best response, margin and stake match brute force. Hard gate: nothing proceeds until it passes.

## Content

Not a training run — a verification pass on `c-solvers`, gating everything else. Sample a known policy `P`, generate long opponent sequences, and confirm:

- The posterior predictive converges to the true row distributions at the expected rate as evidence accumulates.
- Best response, edge, decision margin, and optimal stake (single and vector) match brute-force expected-payoff evaluation over the discrete grid.
- The posterior with zero observations equals the prior exactly (unit test, not a convergence check).

**Hard gate.** Nothing else in the build order proceeds — no tokenizer, no model, no training — until this passes. If any of these checks is soft-failed or skipped "for now," every downstream measurement inherits an unverified reference and every subsequent result becomes uninterpretable.

## Migration source

Protocol rev.2 §6 verification requirement. Add: posterior with zero observations must equal the prior.
