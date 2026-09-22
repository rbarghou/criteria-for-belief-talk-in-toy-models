---
id: s-counting-vs-retrieval
type: study
phase: 1
status: drafted
primary_outcome: Whether the transition concerns the count-accumulation machinery, the row-selection machinery, or their composition.
grounding: grounded
depends_on: [{node: r-phase-b-main, edge: needs}, {node: c-inst-grounded, edge: needs}]
---

## Purpose

Rung 0 against rung 1. The stronger instrument (rung 1 against rung 1-prime) requires the reactive family and belongs to phase 2.

## Content

Compare rung 0 (i.i.d. opponent, no row selection) against rung 1 (`r-phase-b-main`'s Markov opponent, count-and-select) using `c-inst-grounded`'s dose-response and temporal-dissociation instruments. Rung 1 layers two computational problems — maintaining `n` count rows, and gathering the row indexed by the opponent's most recent action; rung 0 removes the second.

**Primary outcome, precisely.** Whether the behavioural transition (and any decodability transition riding with it) concerns the count-accumulation machinery, the row-selection machinery, or their composition — answered by which ablations affect rung-0-trained networks versus rung-1-trained ones differently.

**Deliberately thin at phase 1, by design not oversight.** This is a *weaker* instrument than the double dissociation available once the loop closes: rung 0 versus rung 1 differ in more than one respect (rung 0 also removes any exploitable structure a fixed-row opponent has), so an ablation effect that differs between them is consistent with several explanations. The stronger instrument — the rung-1/rung-1′ matched pair, matched in difficulty by construction since both are 3-row estimation problems with identical statistical structure — requires the reactive opponent family and belongs to phase 2 (`catalogue/phases.md`). This study is what phase 1 can do with the instrument it has; it is not a substitute for the phase-2 version.

## Migration source

Protocol rev.2 §3.2. Reconciled R13, R29 (phase 2 version).
