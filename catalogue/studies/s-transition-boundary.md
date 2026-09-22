---
id: s-transition-boundary
type: study
phase: 1
status: drafted
primary_outcome: Whether a train/test gap opens at any pool size, and at which pool size the memorizing and generalizing solutions compete.
grounding: grounded
depends_on: [{node: r-diversity-sweep, edge: needs}, {node: c-inst-grounded, edge: needs}, {node: p-diversity-boundary, edge: calibrates}]
---

## Purpose

Gating study. If no gap opens anywhere, the developmental question is malformed and six other studies lose their footing.

## Content

Gating study, run on `r-diversity-sweep`'s checkpoints. Measure mean return per round on train and test pools at each pool size `N`, against the exact solver (ceiling) and uniform random play (floor); plot against training step (`c-inst-grounded`).

**Pre-registered definition.** Primary: the step at which held-out mean return per round first crosses the midpoint between floor and ceiling. Secondary: the step maximizing the derivative of held-out return with respect to log training step. Both must be fixed before looking at any decodability curve, per the pre-registration artifact (`c-training`).

**The train/test gap is the actual finding, not the transition per se.** If no gap opens at any `N`, there was no memorization phase, and any claim about a memorization-to-generalization transition should be withdrawn regardless of how sharp the return curve looks. If a gap does open, its width and location select the operating point for the main runs. Six other phase-1 studies (`s-decodability-timing`, `s-payoff-alone`, `s-belief-persistence`, `s-representation-vs-demand`, `s-causal-structure`, and indirectly `s-counting-vs-retrieval`) presuppose that this study finds a real transition to time other measurements against; a null result here is informative for the program (`p-diversity-boundary` may not characterize this substrate at this scale) but leaves those six without their footing.

## Migration source

Protocol rev.2 §4, §9.1. Reconciled R23.
