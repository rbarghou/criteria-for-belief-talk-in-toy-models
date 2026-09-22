---
id: r-phase-b-main
type: run
phase: 1
status: drafted
depends_on: [{node: c-training, edge: needs}, {node: c-substrate, edge: needs}]
produces: checkpoints, logs
---

## Purpose

Opponent-prediction objective at the selected operating point, dense checkpointing. The reference condition against which payoff-only training is read.

## Content

Self-supervised opponent-prediction objective (`c-training`): cross-entropy on the opponent's actual next action, at opponent-token positions. Run at the operating point selected by `r-diversity-sweep`, on rung 1, with dense checkpointing (higher density around any visible transition — `c-training`).

**Role: the reference.** This is not a smuggled label the way Phase A is — the target is an event the model observes one token later regardless — but it trains the posterior predictive directly, which makes finding it in the network close to tautological. Its value is establishing *where* (layer), *when* (training step), and *in what form* an exactly-specified posterior appears when the objective demands it, so that Phase C (`r-phase-c-action`, `r-phase-c-stake1`, `r-phase-c-stakevec`) can be read as the question of whether the same structure appears when nothing demands it except consequences. Run the full `c-inst-derived`/`c-inst-grounded` measurement suite on this run's checkpoints, not just on Phase C's.

## Migration source

Protocol rev.2 §8 Phase B.
