# Questions Register — RPS Belief Circuits

**Opened:** 2026-09-19
**Scope:** questions raised during the section-by-section reading of `rps-belief-circuit-baseline-protocol-2026-09-19.md`, deferred until the reading is complete.

Companion file: `rps-belief-circuits-amendments-register-2026-09-19.md`

---

## Q1 — Grounding of the game-theoretic definition of belief

**Raised at:** §1, after the posterior digression.

Ramsey wants historical and literature grounding for the game-theoretic notion of belief, for his own understanding rather than for any write-up: what its motivating cases were, and how it relates to the broader game-theoretic tradition. Broad sense of why it makes sense is already in place; what's missing is the lineage.

**Suggested entry point:** the elicitation of degree of belief through willingness to bet (Frank Ramsey, "Truth and Probability," 1926; de Finetti), which is the probabilistic cousin of revealed preference and the direct ancestor of the stake channel in §3.3. From there, the Bayesian-games line (Harsanyi, types) and the relation to equilibrium concepts.

**Cross-reference to amendments:** this becomes an amendment if the standard treatment defines belief in a way that diverges from §1's stipulation — particularly on whether beliefs range over *strategies*, over *types*, or over *states of the world*. Those are three different commitments and the document currently picks one implicitly.

**Status:** open.

---

## Q2 — Fuller question on §9.2 probe targets

**Raised at:** §1, after the simplex digression. Partially answered in place.

**Answered so far:** the four probe targets in §9.2 are not the generative parameters. None is the opponent's true policy matrix and none is α. All four are quantities computed from the observed history — what an ideal reasoner holding exactly the model's observations would believe. This is deliberate (epistemic parity): grading against the true policy would ask the network to represent something the evidence does not determine, so a failure would be uninformative and a partial success would measure evidence accumulation rather than computation. Separately, nothing about the policy or α reaches the model: §5 fixes the vocabulary at n+1 tokens. Probing is a measurement made from outside and is not a channel into the network. The one legitimate appearance of the true policy is Phase A's supervised target, which is exactly why the document restricts Phase A to debugging.

**Remaining:** Ramsey flagged a fuller version of the question to be taken up when the reading reaches §9.2.

**Status:** partially answered, deferred to §9.2.

---

## Terms flagged for reiteration

Not questions, but tracked here so they aren't lost. These are terms Ramsey asked to have restated as they recur rather than assumed:

- **Causal validation** — short form: not "we ran an ablation," but the compound standard of §9.5 (dose-response over evidence, temporal dissociation across training, relearning time), adopted because a single ablation at a single checkpoint cannot distinguish a structurally central mechanism from one the network would rebuild in a few steps.
- **Conjugacy** — short form: updating leaves you in the same distributional family you started in, so the update is arithmetic rather than integration, which is what makes the exact answer cheap enough to compute every round.
- **Posterior predictive** — short form: the three-level hierarchy. Unnormalized concentrations (the posterior, 9 numbers, row sums encode confidence), then the normalized mean policy (a point estimate, 3×3 row-stochastic), then the single row indexed by the opponent's last action (the predictive, 3 numbers, 2 free). Each step down discards something specific.
- **Exploit margin** — short form: the expected outcome of the best action minus that of the second-best. It measures how decisively the belief picks one action, not how much value is available (that is the *edge*, `max_a E[a]`) and not how well-established the belief is (that is the *evidence*, the row sum). See amendment A11; these three are currently conflated in the protocol.
- **Expected outcome of an action** — short form for n=3: the predictive probability on the action one step behind you, minus the predictive probability on the action one step ahead. Playing rock, you win on scissors and lose on paper; their playing rock costs nothing. General form: the sum of probabilities on the actions you beat, minus the sum on the actions that beat you. Note the three expected outcomes always sum to zero, so they live on a plane.
- **Centred log-ratio** — short form: take the natural log of each component, then subtract the mean of those logs; equivalently, the log of each component divided by the geometric mean. Used only as the coordinate system for the probe regression target in §9.2. It fixes two things — the redundancy of the sum-to-one constraint, and the fact that equal probability *differences* are not equal in inferential weight while equal *ratios* are. Differences in clr space are log ratios in probability space. (Worked through with diagrams 2026-09-21.)

**Confirmed comfortable, no reiteration needed:** posterior; memorization-to-generalization transition (and grokking as its special case); sufficient statistic; simplex; revealed preference; cyclic group; dense reward and credit assignment; policy gradient; in-context estimation; Markov chains; ablation; exploration-exploitation tradeoff; greedy; babbling equilibria; proper scoring rule; the two-layer induction mechanism (previous-token head feeding a matching head); weight decay; pre-registration.
