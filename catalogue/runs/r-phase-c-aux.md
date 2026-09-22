---
id: r-phase-c-aux
type: run
phase: 1
status: drafted
depends_on: [{node: c-training, edge: needs}, {node: c-substrate, edge: needs}]
produces: checkpoints, logs
---

## Purpose

Payoff plus auxiliary prediction loss, weight swept toward zero. Rescue path and measurement of how much predictive pressure payoff fails to supply.

## Content

Payoff plus an auxiliary opponent-prediction loss with weight `β`, swept downward toward zero, run only if `r-phase-c-action` (or the stake variants) stalls. The smallest `β` at which the belief structure still forms is itself a measurement — it quantifies how much predictive pressure the payoff channel alone fails to supply.

**Pre-registration requirement (R18 secondary):** multiple seeds per `β`, and a criterion for "still forms" (e.g. a decodability threshold on a named target, at a named layer) fixed *before* the sweep runs — otherwise the reported threshold tracks nuisance parameters (seed variance, threshold arbitrariness) more than the quantity it claims to name. **All headline results come from the from-scratch Phase C runs; results from this run are reported as a separate, clearly labelled interpolation, never merged into the headline claim.**

## Migration source

Protocol rev.2 §8 Phase C-aux. Reconciled R18 secondary (seeds per beta, criterion fixed in advance).
