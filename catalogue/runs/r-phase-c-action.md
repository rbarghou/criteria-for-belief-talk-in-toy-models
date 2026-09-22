---
id: r-phase-c-action
type: run
phase: 1
status: drafted
depends_on: [{node: c-training, edge: needs}, {node: c-substrate, edge: needs}]
produces: checkpoints, logs
---

## Purpose

Policy gradient, payoff only, single action per round.

## Content

REINFORCE with a learned or running-mean baseline, reward = per-round payoff, variant A (single action, no stake). Initialized from scratch — **not** from `r-phase-b-main` weights (`c-training`, R4) — because inheriting Phase B's weights would beg the question of whether belief arises under payoff pressure alone.

No labels anywhere; the model sees only consequences. Under variant A specifically, there is no gradient anywhere that asks the network to predict the opponent, so the entire counting-and-normalizing machinery, if it forms, must be built through the payoff channel alone — this is the interesting condition (behaviour depends only on the sign structure of the posterior, per `c-substrate`) and also the fragile one. Entropy regularization or temperature scheduling is mandatory (`c-training`, R5) to prevent premature collapse onto a deterministic policy. If this run stalls, the rescue path is `r-phase-c-aux`, not a silent architecture or hyperparameter change.

## Migration source

Protocol rev.2 §8 Phase C, variant A. Reconciled R4, R5.
