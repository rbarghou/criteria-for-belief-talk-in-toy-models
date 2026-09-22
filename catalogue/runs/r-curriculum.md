---
id: r-curriculum
type: run
phase: 1
status: drafted
depends_on: [{node: c-training, edge: needs}, {node: c-substrate, edge: needs}]
produces: checkpoints, logs
---

## Purpose

Prediction training followed by payoff pressure, initialized from the Phase B weights. Distinct from the from-scratch Phase C runs.

## Content

Train `r-phase-b-main`'s objective to convergence, then continue training the *same weights* under Phase C's payoff-only objective — distinct from `r-phase-c-action` etc., which initialize from scratch. Produces a network at the same final task coordinate as the from-scratch Phase C runs, behaviourally comparable by construction.

**Why this run exists as its own node rather than a variant flag on Phase C.** It is the sharpest available test of "representation trails function" (`program/orientation.md` §6.7): if prediction training installs a full posterior and payoff pressure then erodes it toward the argmax — because the argmax is all behaviour requires — that is a direct, measurable demonstration that representational richness is not preserved for its own sake once nothing demands it. If the posterior instead persists through payoff pressure, the thesis is weakened in a specific, quantified way. Either outcome is reportable; feed the checkpoint trajectory through the full decodability suite (`c-inst-derived`) and read it against `r-phase-b-main`'s own trajectory as the reference (`s-belief-persistence`).

## Migration source

Reconciled R19. Program framing: orientation 6.7.
