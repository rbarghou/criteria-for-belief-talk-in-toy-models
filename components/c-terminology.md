---
id: c-terminology
type: component
status: drafted
provides: fixed vocabulary
---

## Purpose

Canonical definitions. Every other document refers here rather than restating. Also the prohibition list.

## Content

### Belief

A posterior over hidden state, updated by evidence, and used to select an action. Nothing more. No phenomenological or mentalistic claim is intended; terms borrowed from philosophy of mind are held provisionally and are not licensed by experimental success.

### Circuit

Underspecified in the literature generally, ranging between a single feature, a hand-selected feature set, and "whatever the ablation procedure flagged" — the last close to circular. This program's response to the circularity is to specify the target *independently of the search that finds it*: the exact posterior is known before any model is trained.

That answers circularity but says nothing about **multiplicity**: several distinct structures may compute a target that was fixed in advance. Both must be stated together — a well-specified target does not imply a unique implementation. See `s-uniqueness` and the circuit-identity metric (open, `records/questions.md`).

**Prohibition.** No unqualified use of **circuit**, **degeneracy**, or **universality** without naming a level of description. Equivalence-class size is a joint property of the network and the analytic vocabulary — "the same circuit" at the level of attention patterns and "the same circuit" at the level of the input-output map are different claims.

### Trust, reputation

Not applicable at phase 1. In a strictly competitive game against a fixed opponent, the opponent is exhaustively characterized by its behavioural distribution; there is nothing for trust to be about, and a testimony channel would have only babbling equilibria. Do not use these words before phase 3 (branch T) exists.

### Theory of mind, introspection, deception

Not applicable at phase 1. Do not use these words in logs or results for phase 1 or phase 2.

### Experience, phenomenology

Not used, anywhere. The design specifies an information architecture — who observes what, in what order, encoded as which tokens — not a claim about experience.

### The belief hierarchy — three objects, previously all called "belief"

Each step down discards something specific:

1. **Posterior** — unnormalized concentrations over all rows of the transition matrix (9 numbers at n=3). Row sums encode confidence. Discards nothing.
2. **Posterior mean policy** — the row-stochastic point estimate (3×3 at n=3). Discards confidence.
3. **Posterior predictive** — the single row indexed by the opponent's most recent action (3 numbers, 2 free at n=3). Discards knowledge of situations not currently arising.

The one legitimate appearance of the *true* generative policy (rather than a posterior quantity) is Phase A's supervised target, which is exactly why Phase A is restricted to debugging (epistemic parity, `program/orientation.md`).

### Three scalars — previously all called "margin"

These come apart: a settled belief that the opponent is near-uniform has high evidence, small margin, small edge.

- **Edge** = `max_a E[a]`, the value available from acting optimally. Governs the optimal stake.
- **Decision margin** = `max_a E[a] − second-max_a E[a]`. Governs whether a model–reference disagreement is meaningful.
- **Evidence** = the row sum of posterior concentrations. How well-established the belief is.

**Vocabulary note.** The questions register's original reiteration entry for this concept used the single term "exploit margin" for what is now split three ways. That term is retired; do not use it going forward. Anywhere it appears in frozen history (`history/`), read it in context — usually it meant *decision margin*, occasionally *edge*, and the register itself did not yet distinguish them.

### Expected outcome of an action

For `n = 3`: the predictive probability on the action one step behind you, minus the predictive probability on the action one step ahead. Playing rock, you win on scissors and lose on paper; their playing rock costs nothing. General form (`c-solvers`): the sum of predictive probabilities on the actions you beat, minus the sum on the actions that beat you. The three expected outcomes always sum to zero, so they live on a plane.

### Conjugacy

Updating leaves you in the same distributional family you started in, so the update is arithmetic rather than integration — what makes the exact answer cheap enough to compute every round.

### Centred log-ratio (clr)

Take the natural log of each simplex component, then subtract the mean of those logs — equivalently, the log of each component divided by the geometric mean. Used as the coordinate system for probe regression targets (`c-inst-derived`). Fixes two things: the redundancy of the sum-to-one constraint, and the fact that equal probability *differences* are not equal in inferential weight while equal *ratios* are — differences in clr space are log ratios in probability space. See `p-compositional-data`.

### Causal validation

Not "we ran an ablation." The compound standard: dose-response over evidence, temporal dissociation across training, and relearning time (`c-inst-grounded`, `s-causal-structure`). Adopted because a single ablation at a single checkpoint cannot distinguish a structurally central mechanism from one the network would rebuild in a few steps.

### Epistemic parity

The reference is what an ideal reasoner with exactly the model's observations would believe — not the truth. Probe targets are posterior quantities, never generative parameters (`program/orientation.md` §7).

## Migration source

Protocol rev.2 §13. Reconciled R8 (edge / decision margin / evidence), R9 (posterior / mean policy / predictive), R10 (circuit: circularity vs multiplicity; no unqualified circuit/degeneracy/universality without a named level of description).
