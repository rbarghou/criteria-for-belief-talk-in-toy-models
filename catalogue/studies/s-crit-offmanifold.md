---
id: s-crit-offmanifold
type: study
phase: 1
status: drafted
primary_outcome: Whether downstream behaviour follows an internal state edited to a posterior the model has never had reason to hold.
grounding: derived
depends_on: [{node: r-phase-b-main, edge: needs}, {node: r-phase-c-stakevec, edge: needs}, {node: c-inst-derived, edge: needs}]
---

## Purpose

Analysis on existing checkpoints; needs no new run.

## Content

Second of the four criteria. On existing `r-phase-b-main` and `r-phase-c-stakevec` checkpoints — no new run needed — edit the decoded internal state (via the fitted probe direction) to a posterior the model has never had reason to hold, given the training distribution it actually saw, and ask whether downstream behaviour follows the edited state rather than the original.

**Primary outcome, precisely.** Whether downstream behaviour tracks an off-manifold edit. A memorized input-output map has no commitments off its data manifold — editing the "belief" of a pure lookup table should do nothing coherent to its output, where a network genuinely computing the posterior should produce behaviour consistent with the edited value. This is the criterion most directly targeting the function-approximation objection (`program/orientation.md` §5): a network that passes this is doing more than reproducing the training distribution's input-output pairs.

**Limit, stated in advance rather than discovered after running it.** Per `program/orientation.md`'s methodological-limits category: this criterion cannot distinguish a network computing the true posterior from one computing a sufficient proxy that merely agrees with it on-distribution, because off-manifold behaviour is exactly the region where such a proxy and the true computation can still diverge in ways this test cannot see if the proxy was built to be robust to exactly this kind of edit. A pass here is evidence, not proof.

## Migration source

Reconciled R15 criterion 2.
