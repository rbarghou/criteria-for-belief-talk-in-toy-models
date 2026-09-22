---
id: r-phase-c-stakevec
type: run
phase: 1
status: drafted
depends_on: [{node: c-training, edge: needs}, {node: c-substrate, edge: needs}]
produces: checkpoints, logs
---

## Purpose

Policy gradient with a stake allocated to every action. Strictly proper elicitation of the whole predictive.

## Content

REINFORCE, from scratch, variant S-full: a stake is allocated to *every* action, with quadratic cost summed across the whole vector, making the optimal allocation proportional to each action's expected outcome — for n=3 this determines the predictive uniquely, a strictly proper elicitation of the whole belief (`c-substrate`, `c-solvers`).

**The confound to carry into interpretation (R18).** The stake-vector payoff gradient carries information about the whole predictive at every round, where variant A's gradient carries only which action paid — the variants differ in intended **behavioural demand** but also, uncontrolled, in **training signal**. If the posterior is decodable under this run and not under `r-phase-c-action`, that may simply mean S-full trains better, not that behavioural demand shapes representation. Mitigations specified for the downstream study (`s-representation-vs-demand`): read decodability at equal fraction-of-ceiling rather than equal step count, and construct a rich-gradient/poor-readout control if one can be built — open, unresolved (`records/questions.md`).

## Migration source

Reconciled R3, R18 (confound).
