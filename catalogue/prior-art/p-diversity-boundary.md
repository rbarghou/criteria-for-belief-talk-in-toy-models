---
id: p-diversity-boundary
type: prior-art
status: imported
confidence: single recent paper; not independently replicated; load-bearing for the whole diversity-sweep approach
---

## Purpose

Memorization/generalization boundaries in in-context Markov learning are set by data diversity, with two distinct subcircuit motifs and sharp boundaries between regimes.

## Content

Gibson, Cui and Reddy, "Distinct mechanisms underlying in-context learning in transformers" (arXiv 2604.12151, April 2026). A mechanistic characterization of transformers trained on a finite set of discrete Markov chains, identifying four algorithmic phases distinguished by whether the network memorizes or generalizes and whether it uses 1-point or 2-point statistics, implemented by two distinct subcircuit motifs: a **statistical induction head** for generalization, and a **task recognition head** (encode, pool, decode, producing a task vector) for memorization. The memorization/generalization boundaries are set by data diversity — the number of distinct chains — with one boundary from kinetic competition between the two subcircuits and a second from a representational bottleneck.

**Load-bearing, and thin.** This is the single paper that motivated rewriting the pool-size sweep (`r-diversity-sweep`) as the primary memorization knob rather than weight decay, and the reason `m` (trajectory multiplicity) was dropped in favor of `N` (pool size) as the sweep variable (`c-substrate`). It is not independently replicated. It supplies both the knob and a theory of where the boundaries sit, converting `s-transition-boundary` from an open search into a confirmation-or-falsification exercise — but if this paper's characterization does not hold at this substrate's scale, the diversity-sweep design inherits that risk directly. The task-recognition-head motif is also one of the two known-answer references for `s-tooling-validation` (with `p-statistical-induction-heads`), covering the memorizing side where the modular-arithmetic literature (`p-modular-arithmetic-circuit`) does not apply at all.

## Migration source

Gibson, Cui & Reddy, arXiv 2604.12151 (2026)
