---
id: r-diversity-sweep
type: run
phase: 1
status: stub
depends_on: [{node: c-training, edge: needs}, {node: c-substrate, edge: needs}]
produces: checkpoints, logs
---

## Purpose

Powers of two from 16 to 4096 under the prediction objective, to locate the memorization/generalization boundary and select the operating point.

## Content

*(stub — not yet migrated)*

## Migration source

Protocol rev.2 §4. Reconciled R23 (drop trajectory multiplicity).
