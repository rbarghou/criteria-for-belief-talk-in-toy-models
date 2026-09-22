---
id: s-causal-structure
type: study
phase: 1
status: drafted
primary_outcome: Whether candidate components are causally load-bearing, whether their effect grows or decays across training, and how expensive they are to rebuild.
grounding: derived
depends_on: [{node: r-phase-b-main, edge: needs}, {node: r-phase-c-stakevec, edge: needs}, {node: c-inst-grounded, edge: needs}, {node: s-decodability-timing, edge: presupposes}]
---

## Purpose

Dose-response, temporal dissociation with headroom normalization, relearning time, and the accumulator-versus-arithmetic double dissociation.

## Content

The full causal-validation battery from `c-inst-grounded`, run on `r-phase-b-main` and `r-phase-c-stakevec` checkpoints, presupposing `s-decodability-timing` has already established which structure is even a candidate for intervention:

- **Dose-response over evidence** — ablation effect as a function of round index `t` within episode, free because every prefix length occurs in every 64-round episode; never obtained by varying episode length `K`.
- **Temporal dissociation, headroom-normalized** — effect size against training step, head-level only (direction-level dropped: no principled reason to call fits at different steps the same component), coarse-then-fine checkpointing around the transition.
- **Relearning time** — perturbation (zero-and-resume) versus constraint (mask-throughout) distinguished explicitly, control matched on immediate performance drop rather than weight norm, optimizer state fixed at resume, and the recovered network re-examined with the identification machinery rather than trusting recovery speed alone.
- **The accumulator-versus-arithmetic double dissociation** (`s-counting-vs-retrieval` cross-reference) — the phase-1-available instrument; the stronger rung-1/rung-1′ pair is phase 2.

**Primary outcome, precisely.** Whether candidate components are causally load-bearing (dose-response), whether their effect grows or decays across training (temporal dissociation — growth indicates a genuine belief mechanism, decay indicates a memorization artifact), and how expensive they are to rebuild (relearning time). The measurements are grounded — none requires a fitted probe, only the reference solver and behavioural scoring — but the study's conclusion is **derived** because `s-decodability-timing` selects which structure is a candidate for intervention. The `grounding` field describes the full evidential chain, not merely the final measurement.

**Caveat to carry through every result here.** Mean-ablation substitutes a population average, not an absence; downstream layers may receive a state the network never produces on any real forward pass. A positive dose-response or temporal-dissociation result is consistent with distant dysfunction, a conduit role, or a degenerate alternate route producing the same function — the lesion tradition's inherited hazards, not resolved by this design, only guarded against by triangulating across the three instruments rather than reporting any one alone.

## Migration source

Protocol rev.2 §9.5. Reconciled R13, R14.
