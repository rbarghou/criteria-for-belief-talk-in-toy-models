---
id: r-phase-c-aux
type: run
phase: 1
status: stub
depends_on: [{node: c-training, edge: needs}, {node: c-substrate, edge: needs}]
produces: checkpoints, logs
---

## Purpose

Payoff plus auxiliary prediction loss, weight swept toward zero. Rescue path and measurement of how much predictive pressure payoff fails to supply.

## Content

*(stub — not yet migrated)*

## Migration source

Protocol rev.2 §8 Phase C-aux. Reconciled R18 secondary (seeds per beta, criterion fixed in advance).
