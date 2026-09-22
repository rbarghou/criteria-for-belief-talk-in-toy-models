---
id: s-belief-persistence
type: study
phase: 1
status: drafted
primary_outcome: Whether a posterior installed by prediction training survives payoff pressure or erodes toward the argmax.
grounding: derived
depends_on: [{node: r-curriculum, edge: needs}, {node: r-phase-b-main, edge: needs}, {node: s-decodability-timing, edge: calibrates}]
---

## Purpose

The cleanest test of representation trailing function.

## Content

Run the full decodability suite on `r-curriculum`'s checkpoint trajectory (Phase B to convergence, then continued under payoff pressure from those weights), reading it against `r-phase-b-main`'s own trajectory.

**Primary outcome, precisely.** Whether the posterior installed by prediction training survives payoff pressure, or erodes toward the argmax as payoff pressure continues — calibrated against `s-decodability-timing`'s decodability-vs-training-step curves so "erosion" and "persistence" are read against the same excess-decodability baseline rather than raw numbers. Either outcome is informative: erosion is a direct, quantified demonstration that representational richness is not preserved once behaviour stops demanding it; persistence weakens that reading of "representation trails function" in a specific way and should be reported as such, not explained away. This is the cleanest available test of the thesis precisely because the curriculum condition holds the final task fixed and varies only training history (`program/orientation.md` §6.7).

## Migration source

Reconciled R19. Orientation 6.7.
