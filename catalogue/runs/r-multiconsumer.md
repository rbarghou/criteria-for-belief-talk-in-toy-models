---
id: r-multiconsumer
type: run
phase: 1
status: stub
depends_on: [{node: c-training, edge: needs}, {node: c-substrate, edge: needs}]
produces: checkpoints, logs
---

## Purpose

One internal state required to serve several distinct decision problems at once. A different training setup, not a variant of the phases above.

## Content

**Flagged, not specified.** This run is required by `s-crit-multiconsumer` (criterion 1 of the four belief-vs-function-approximation criteria: whether one shared internal state serves several distinct decision problems, or task-specific features form independently) but none of the four source documents describe a training setup for it. It is not a variant of any existing Phase A/B/C run — the whole point of the criterion is that it needs *multiple, distinct decision problems consuming the same posterior*, which none of the phase-1 runs as specified provide (each trains toward a single objective: predict the opponent, or maximize one payoff).

**What is known from the reconciled amendments (R15):** the question is whether the network builds one shared representation serving several decision problems, or independent task-specific features for each. What is not known, and should not be invented here: what the second (or third) decision problem *is* — e.g. a second payoff structure over the same belief, a second solver query, a held-out prediction target — nor the architecture needed to pose them jointly (shared trunk with multiple heads? sequential fine-tuning on a shared checkpoint? something else).

**This is genuinely new, previously unbudgeted work**, per the handoff carried into this migration — not an optional nice-to-have and not something to spec unilaterally. Needs a design decision from Ramsey before this stub can move past `status: stub`. Tracked in `records/questions.md`.

## Migration source

Reconciled R15 criterion 1. NOT PREVIOUSLY BUDGETED — new run.
