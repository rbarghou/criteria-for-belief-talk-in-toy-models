---
id: s-crit-residual
type: study
phase: 1
status: stub
primary_outcome: Whether the model's actions deviate in the direction the decoded belief deviates from the true posterior.
grounding: derived
depends_on: [{node: r-phase-c-stakevec, edge: needs}, {node: c-inst-derived, edge: needs}, {node: c-inst-grounded, edge: calibrates}]
---

## Purpose

Validates the probe rather than the model, and does so without depending on any control condition. Precondition for the testimony work in later phases.

## Content

*(stub — not yet migrated)*

## Migration source

Reconciled R12. Dependency noted in R30 (branch T).
