---
id: r-larger-n
type: run
phase: 1
status: drafted
depends_on: [{node: c-training, edge: needs}, {node: c-substrate, edge: needs}]
produces: checkpoints, logs
---

## Purpose

Identical pipeline at n = 5, 7, 9, where the cyclic signature is rich enough to be recognizably right or absent.

## Content

Identical pipeline (engine, tokenizer, solver, Phase B objective) at `n = 5, 7, 9`, instead of the baseline `n = 3`.

**Why n=3 alone is not enough for tooling validation.** Win/lose/draw depends only on the action difference mod `n`, so a cyclic group must be represented somewhere — but at `n=3` the group is too small for a rich representation-theoretic signature (essentially one non-trivial frequency pair). The validation case is thin at baseline. At larger `n`, the cyclic structure produces a signature comparable to the modular-arithmetic literature's (`p-modular-arithmetic-circuit`, `p-algorithm-multiplicity`). If the tooling recovers the expected structure at larger `n` without being told what to look for, that is evidence the tooling works, and it transfers back to interpreting the `n=3` runs (`s-tooling-validation`).

## Migration source

Protocol rev.2 §9.4. Reconciled R32.
