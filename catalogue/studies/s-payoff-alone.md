---
id: s-payoff-alone
type: study
phase: 1
status: drafted
primary_outcome: Whether a belief-shaped intermediate appears under policy gradient with no predictive objective anywhere.
grounding: derived
depends_on: [{node: r-phase-c-action, edge: needs}, {node: r-phase-c-aux, edge: needs}, {node: s-decodability-timing, edge: calibrates}]
---

## Purpose

The philosophically interesting condition. Read against the prediction-trained reference.

## Content

The headline philosophical result. Run the full `c-inst-derived`/`c-inst-grounded` measurement suite on `r-phase-c-action` (rescued by `r-phase-c-aux` if the from-scratch run stalls), and read it against `r-phase-b-main` as the reference condition: does a belief-shaped intermediate appear under policy gradient alone, with no predictive objective anywhere in the loss?

**Reading discipline.** `r-phase-c-aux` results interpolate toward Phase B by construction (an auxiliary prediction loss is present, weighted by `β`) and must be reported as a separate, clearly labelled condition, never merged into this study's headline claim — the entire point of `r-phase-c-action` is that nothing in its objective asks for a prediction, so any belief-shaped structure found there is not close to tautological the way it is under `r-phase-b-main`.

## Migration source

Protocol rev.2 §8 Phase C. Reconciled R4.
