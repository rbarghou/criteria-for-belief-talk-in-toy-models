---
id: p-modular-arithmetic-circuit
type: prior-art
status: imported
confidence: CONTESTED — see p-algorithm-multiplicity
---

## Purpose

Modular addition is implemented by a sparse Fourier representation composed via trigonometric identities.

## Content

Nanda et al., "Progress Measures for Grokking via Mechanistic Interpretability," show modular addition is implemented via a sparse Fourier representation of the inputs, composed through trigonometric identities into the output — the canonical known-answer case the modular-arithmetic grokking literature supplies for validating circuit-identification tooling.

**Covers the wrong half for this project's purposes.** The modular-arithmetic answer concerns the *arithmetic* — win/lose/draw as a function of the action difference mod `n` — but the belief structure this project cares about is an *accumulator*, i.e. the count-and-normalize machinery, not the group-composition machinery. Tooling that correctly recovers a rotational Fourier representation is not thereby validated for recovering an accumulator (`s-tooling-validation`). The fix used here: validate additionally against the statistical-induction-head and task-recognition-head motifs (`p-statistical-induction-heads`, `p-diversity-boundary`), so both halves of the pipeline have a known answer. Weakened further by the fact that this answer is itself contested (`p-algorithm-multiplicity`).

## Migration source

Nanda et al., progress measures for grokking
