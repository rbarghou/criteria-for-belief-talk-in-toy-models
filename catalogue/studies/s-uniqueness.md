---
id: s-uniqueness
type: study
phase: 1
status: stub
primary_outcome: Whether independently seeded runs converge on the same circuit, at a level of description fixed in advance.
grounding: derived
depends_on: [{node: r-seed-replication, edge: needs}, {node: c-inst-derived, edge: needs}, {node: s-tooling-validation, edge: enables}, {node: p-algorithm-multiplicity, edge: calibrates}]
---

## Purpose

Estimates the size of the equivalence class of implementations. Unmeasurable without the circuit-identity metric.

## Content

Apply the circuit-identity metric to `r-seed-replication`'s 30 checkpoints, separated by the two factorial sources of variation (initialization, data order), and to `s-tooling-validation`'s recovered structure at larger n as a sanity check that the metric behaves sensibly on a case with a partially known answer.

**Primary outcome, precisely.** Whether independently seeded runs converge on the same circuit, at a level of description fixed in advance — this study is what estimates the size of the equivalence class of implementations that solve this task, which is the concrete, measurable form of "circuit" the `c-terminology` prohibition demands (no unqualified circuit talk without naming a level).

**Currently unmeasurable — flagged, not worked around.** No circuit-identity metric has been chosen (`records/questions.md`; three candidates — representational similarity/CKA, probe-direction alignment after head permutation, functional equivalence under head transplant — none obviously dominant). This study cannot proceed past `status: stub` until the pre-registration artifact fixes one. `p-algorithm-multiplicity` is the direct precedent for why this cannot be settled by inspection: the Clock/Pizza dispute is exactly the kind of disagreement a level-relative identity metric is meant to resolve in advance rather than adjudicate after the fact.

## Migration source

Reconciled R12b, R31. Orientation: degeneracy is level-relative.
