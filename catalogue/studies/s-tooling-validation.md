---
id: s-tooling-validation
type: study
phase: 1
status: drafted
primary_outcome: Whether the circuit-identification machinery recovers the known structure at larger n and the reported motifs for in-context Markov estimation, without being told what to look for.
grounding: derived
depends_on: [{node: r-larger-n, edge: needs}, {node: c-inst-derived, edge: needs}, {node: p-modular-arithmetic-circuit, edge: presupposes}, {node: p-statistical-induction-heads, edge: presupposes}]
---

## Purpose

Runs first or nearly first. If the tooling cannot recover a known answer, every downstream study is uninterpretable.

## Content

Run the full `c-inst-derived` circuit-identification pipeline on `r-larger-n`'s checkpoints (n = 5, 7, 9) without telling it what to look for, and check whether it recovers the reported motifs from `p-modular-arithmetic-circuit` (the arithmetic half) and `p-statistical-induction-heads`/`p-diversity-boundary` (the accumulator half — statistical induction head and task recognition head).

**Why both halves are needed, not just the modular-arithmetic comparison.** The modular-arithmetic literature's known answer concerns the *arithmetic* (win/lose/draw as a function of action difference mod n); the belief structure this project cares about is an *accumulator* (count-and-normalize). Tooling that correctly recovers a rotational Fourier representation is not thereby validated for recovering an accumulator — the two are different computational structures and a tool could succeed at one and fail at the other silently. This study's design closes that gap with material already present in the source documents rather than requiring new prior-art.

**Runs first or nearly first, and gates the rest.** If the tooling cannot recover a known answer here, every downstream derived-instrument study (`s-decodability-timing`, `s-payoff-alone`, `s-belief-persistence`, `s-representation-vs-demand`, all four criteria studies, `s-uniqueness`) is uninterpretable — a null there would be indistinguishable from a tooling failure.

**Known weakness in the reference itself, not to be smoothed over.** The modular-arithmetic answer is contested (`p-algorithm-multiplicity`): whether Zhong et al.'s "Clock" and "Pizza" are genuinely distinct algorithms or the same solution at different levels of description is unresolved in the literature this study borrows from. A validation result here that leans on the arithmetic half alone inherits that dispute; leaning on the accumulator half (which is not contested in the same way) is the more defensible half of this study's evidence.

## Migration source

Protocol rev.2 §9.4. Reconciled R32. Note the modular-arithmetic answer is contested (p-algorithm-multiplicity).
