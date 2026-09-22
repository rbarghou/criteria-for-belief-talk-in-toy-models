---
id: s-crit-multiconsumer
type: study
phase: 1
status: stub
primary_outcome: Whether one shared representation serves several decision problems, or task-specific features form independently.
grounding: derived
depends_on: [{node: r-multiconsumer, edge: needs}, {node: c-inst-derived, edge: needs}, {node: s-tooling-validation, edge: enables}]
---

## Purpose

First of the four criteria. The criteria are the program's actual deliverable.

## Content

First of the four belief-versus-function-approximation criteria (`c-inst-derived`). Depends on `r-multiconsumer`, which is not yet specified (`records/questions.md`) — this study cannot run until that run's design is decided.

**Primary outcome, precisely.** Whether one internal state, required to serve several distinct decision problems, is served by one shared representation or by independently-forming task-specific features. The measurement is a probe-based comparison across the multiple consumers `r-multiconsumer` is meant to provide — hence `grounding: derived` — and its result in turn enables `s-tooling-validation`'s broader claim that the derived-instrument pipeline is trustworthy, since multi-consumer sharing (or its absence) is itself a structural fact the pipeline should be able to detect reliably once validated.

Of the four criteria, this is the one furthest from being runnable: the other three (`s-crit-offmanifold`, `s-crit-pathindependence`, `s-crit-residual`) are analyses on checkpoints that already exist from other phase-1 runs; this one needs a run that doesn't exist yet.

## Migration source

Reconciled R15 criterion 1.
