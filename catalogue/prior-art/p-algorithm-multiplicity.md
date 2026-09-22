---
id: p-algorithm-multiplicity
type: prior-art
status: imported
confidence: CONTESTED in both directions; the dispute is itself the finding, and it makes equivalence-class size level-relative
---

## Purpose

At least two distinct algorithms solve modular addition, selected by architectural detail; more recent work argues convergence at the level of representation manifolds.

## Content

Zhong et al. (NeurIPS 2023, "The Clock and the Pizza") found that networks trained on modular addition converge to at least two qualitatively distinct algorithms — the "Clock" and "Pizza" circuits — with the outcome selected by architectural detail rather than by the task alone. Subsequent work disputes the reading, arguing the two are the same solution viewed at different levels, converging at the level of representation manifolds rather than diverging as distinct algorithms.

The dispute is the finding, not a resolved fact this project can cite one-sidedly. It bears on two things directly: it is the reason the known-answer case for `s-tooling-validation` is contested at exactly the level `c-inst-grounded`'s attention-pattern and ablation instruments operate on (see `p-modular-arithmetic-circuit`); and it is a direct precedent for why `s-uniqueness` needs a circuit-identity metric fixed *before* looking at cross-seed results (`records/questions.md`) — without one, "the same circuit" versus "two circuits" is exactly the kind of question this dispute shows cannot be settled by inspection alone.

## Migration source

Zhong et al., NeurIPS 2023 (Clock and Pizza), plus subsequent dispute
