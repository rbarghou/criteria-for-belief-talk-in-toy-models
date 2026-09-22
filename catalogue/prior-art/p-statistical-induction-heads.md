---
id: p-statistical-induction-heads
type: prior-art
status: imported
confidence: well established
---

## Purpose

Transformers trained on Markov sequences form statistical induction heads and pass through staged phases (uniform, unigram, then a rapid transition to bigram).

## Content

Edelman, Tsilivis, Goel, Edelman and Malach, "The Evolution of Statistical Induction Heads: In-Context Learning Markov Chains" (NeurIPS 2024, arXiv 2402.11004). Transformers trained to predict sequences from Markov chains drawn from a prior form **statistical induction heads** — computing next-token probabilities from in-context bigram statistics — and pass through staged training phases: uniform, then unigram, then a rapid transition to the bigram solution, with evidence that the simpler unigram solution *delays* formation of the bigram one.

This is the same inference problem as rung 1 (`c-substrate`) minus the payoff layer — the opponent-prediction objective (Phase B, `r-phase-b-main`) trains exactly this circuit directly, which is what makes Phase B "close to tautological" as a reference (`c-training`). The staged uniform→unigram→bigram structure is the direct precedent for `s-transition-boundary` and the checkpoint-density guidance in `c-training`. Used as one of the two known-answer motifs (with the task recognition head, `p-diversity-boundary`) for `s-tooling-validation`, since it covers the accumulator half that `p-modular-arithmetic-circuit` does not.

## Migration source

Edelman et al., NeurIPS 2024 (arXiv 2402.11004)
