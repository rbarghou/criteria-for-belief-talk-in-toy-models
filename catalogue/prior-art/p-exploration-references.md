---
id: p-exploration-references
type: prior-art
status: imported
confidence: settled; phase 2 relevance
---

## Purpose

Principled computable policies that explore without an explicit exploration parameter.

## Content

Thompson sampling, and Russo & Van Roy on information-directed sampling (IDS): principled, computable policies that explore in proportion to genuine uncertainty and its expected reduction, without an explicit hand-tuned exploration parameter (an epsilon-schedule or temperature knob).

Both are named rungs in the six-member reference ladder (`c-solvers`): Thompson sampling (rung 4, explores in proportion to residual uncertainty) and information-directed sampling (rung 5, explicit regret-versus-information tradeoff). At phase 1, against an opponent that cannot react to the model, these rungs collapse onto posterior-greedy — there is no continuation value to protect, so nothing distinguishes them behaviourally. They become load-bearing only once the loop closes (phase 2, `catalogue/phases.md`), where IDS in particular supplies the reference quantity for the value-of-information probe target that phase 2 needs and phase 1 has no analogue for (`c-inst-derived` gap noted in the phase-2 description).

## Migration source

Thompson sampling; Russo & Van Roy on information-directed sampling
