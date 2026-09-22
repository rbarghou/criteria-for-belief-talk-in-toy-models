---
id: r-phase-c-stake1
type: run
phase: 1
status: drafted
depends_on: [{node: c-training, edge: needs}, {node: c-substrate, edge: needs}]
produces: checkpoints, logs
---

## Purpose

Policy gradient with one stake on the chosen action. Named intermediate: reveals argmax plus edge.

## Content

REINFORCE, from scratch, variant S: the model emits an action and one stake from a discrete grid (`c-solvers`, `c-substrate`). Payoff `s · outcome(a,b) − λs²`; optimal stake tracks the **edge**, `max_a E[a]`, not the decision margin (a correction from the reconciled amendments — the two were conflated in the original protocol). Choose `λ` so `s*` spans the grid over the empirical edge distribution; a 4-point grid `{0,1,2,3}` is sufficient.

Retained as a **named intermediate**, not merely a step toward the fuller stake-vector variant (`r-phase-c-stakevec`): the three-way comparison A / S / S-full is specifically designed to isolate what each channel reveals — argmax alone, argmax-plus-edge, and full posterior respectively (`s-representation-vs-demand`). Same exploration-control and from-scratch requirements as `r-phase-c-action`.

## Migration source

Reconciled R3.
