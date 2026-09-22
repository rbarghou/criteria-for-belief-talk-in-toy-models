---
id: c-inst-grounded
type: component
status: drafted
depends_on: [{node: c-solvers, edge: needs}, {node: c-terminology, edge: needs}]
provides: probe-free measurement
---

## Purpose

Instruments that owe nothing to any fitted decoder: behavioural scoring against the reference ladder, ablation effects measured behaviourally, attention patterns read off rather than fitted, and solver verification. These are the roots of the dependency graph.

## Content

### Transition measurement (behavioural)

Mean return per round on train and test pools, against two references: the exact solver (ceiling) and uniform random play (floor). Plot against training step.

**Pre-registered transition definition.** Primary: the step at which held-out mean return per round first crosses the midpoint between floor and ceiling. Secondary: the step maximizing the derivative of held-out return with respect to log training step.

**Report the train/test gap explicitly.** If there is no gap, there was no memorization phase, and any claim about a memorization-to-generalization transition should be withdrawn regardless of how sharp the return curve looks — use the gap as the diagnostic for whether the diversity sweep found the right operating point (`s-transition-boundary`).

### Rationalizability (grounded — no probe)

Does the observed action sequence admit *some* consistent belief trajectory, independent of whether it is the correct one? Separates "the model is wrong" from "the model is not doing the kind of thing that admits of being right or wrong." Cheap, and nothing else in the battery measures it (`s-rationalizability`).

### Belief usage, grounded half

- Fraction of model actions matching the best response to the *true* belief, as a function of decision margin. A model genuinely using its belief should track the best response closely at large margin and behave near-arbitrarily at small margin.
- Under variant S/S-full: correlation between emitted stake and optimal stake, as a function of margin — the measurement distinguishing "represents a decision boundary" from "represents a graded posterior." (The decoded-belief half of usage, and the derived-vs-true comparison, live in `c-inst-derived` since they require a probe.)

### Task-level controls

**Unexploitable opponent (all rows uniform).** With all rows uniform the *true* policy is uniform, but the *posterior* is not — counts fluctuate and the correct predictive wanders. A model doing the correct computation tracks that, and a probe recovering it is recovering something real. **This condition controls usage, not decodability**: what it removes is actionability. A model appearing to act on belief here — matching a decoded or true best response above chance — is doing something spurious, since there is nothing to exploit. Use accordingly, in `s-rationalizability`/usage measurement, not as a decodability null.

**Constant opponent.** Plays a fixed action every round. Inference is trivial — only the identity of one action must be recovered. Bounds the measurement from the other side: confirms the machinery detects belief when belief is maximally easy.

### Attention patterns

Read off directly (which positions attend to which), not fitted. Used as corroborating, non-probe evidence for the causal-structure work below; never substituted for the intervention results.

### Interventions and causal structure (grounded core; see `s-causal-structure`)

Only after the behavioural transition and usage measurements are stable.

- **Dose-response over evidence.** Ablate candidate components and measure effect size as a function of round index `t` within the episode. A component implementing belief-tracking should matter more as evidence accumulates; a correlated component should show a flat profile. Because all prefix lengths occur inside every episode (`c-substrate`), this is in-distribution and free — do not vary episode length `K` to obtain it.
- **Temporal dissociation.** Ablate at every checkpoint, plot effect size against training step. Normalize effect size by available headroom first — as the network improves, ablating any load-bearing component costs more in absolute terms, so raw growth is confounded with a rising baseline. **Head-level ablations only**, since head indices are stable across checkpoints by construction; direction-level temporal ablation is dropped — separate fits at different training steps give no principled reason to call the result the same component. Coarse logarithmic checkpointing to locate the transition, then fine sampling in that window only. A genuine belief mechanism should show its ablation effect *growing* across the transition; a memorization artifact should show it *decaying*.
- **Relearning time.** Ablate, resume training, measure steps to recovery against a matched control ablation of similar magnitude in a non-candidate direction. Four decisions the original protocol left open, now fixed: match the control on **immediate performance drop**, not weight norm (equal norms do not mean equal damage); distinguish **perturbation** (zero and resume — measures how fast the optimizer restores a deleted structure) from **constraint** (mask throughout resumed training — measures whether an alternative route exists and what it costs; the masked version is the one that speaks to structural centrality); fix and state the **optimizer state** at resume; and **re-examine the recovered network** with the circuit-identification machinery, since recovery time alone cannot distinguish rebuilding the same structure from building a different one. Slow recovery indicates a structurally distinctive position; comparable recovery across targets indicates degeneracy.
- **Accumulator-versus-arithmetic double dissociation (available at phase 1).** Predicting the opponent's next action and computing which action beats it have independently checkable outputs. Look for an ablation degrading prediction while sparing the mapping, and another doing the reverse (`s-counting-vs-retrieval`). The stronger instrument — the rung-1/rung-1′ matched pair, matched in difficulty by construction — requires the reactive family and belongs to phase 2.

**Caveat to carry into all interventions.** Mean-ablation substitutes a population average, not an absence, and may hand downstream layers a state the network never produces on any single forward pass. Inherited hazards from the lesion tradition apply: distant dysfunction from lost input rather than local destruction; a component acting as conduit rather than origin; degenerate alternate routes producing the same function. Double dissociation was raised as a requirement by the original lesion critique and did not fully survive into the remedies — temporal dissociation addresses *structurality*, not *specificity*; it does not substitute for a genuine double dissociation where one is available.

### Solver verification

Monte Carlo check that the posterior converges at the expected rate and that best response, decision margin, and stake match brute-force evaluation, plus the exact-prior-at-zero-observations unit test (`c-solvers`, `r-solver-verification`). Hard gate: nothing else proceeds until this passes.

## Migration source

Protocol rev.2 §9.1, parts of §9.3 and §9.5. Reconciled R11 (rationalizability), R13 (behavioural side), R14 (relearning time).
