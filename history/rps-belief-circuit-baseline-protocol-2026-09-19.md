# Belief Circuits in Repeated Rock-Paper-Scissors — Baseline Protocol (rev. 2)

**Date:** 2026-09-19
**Supersedes:** rps-belief-circuit-baseline-protocol-2026-09-18.md
**Status:** foundation document for implementation
**Audience:** implementing engineer or coding agent

---

## 0. Changelog from rev. 1

**Structural changes:**

1. **Memorization pressure relocated.** Rev. 1 assumed a train/test split over opponent matrices would create the finite-input-space condition that grokking requires. It does not: the model never sees a matrix, only a fresh stochastic rollout, so nothing is memorizable. Memorization pressure is now supplied by two explicit knobs — pool size `N` (data diversity) and trajectory multiplicity `m` — and the transition is defined operationally in advance rather than identified post hoc (§4, §9.1).
2. **Phase ladder extended.** A self-supervised opponent-prediction phase is inserted between the supervised debug run and the policy-gradient run. It trains the posterior predictive directly without stipulating what belief means, and serves as the reference against which the policy-gradient result is read (§8).
3. **Graded action channel added as a paired variant.** Under action-only payoff, the sufficient statistic for behaviour is one categorical variable, not the full posterior. A stake channel with convex cost makes the exploit margin behaviourally revealed. The action-only and stake variants are run as a **pair**; their difference is a primary result, not a robustness check (§3.3, §9.3).
4. **Control conditions added** as a first-class section rather than scattered caveats: unexploitable and constant opponents at the task level, and random-init, raw-feature, and shuffled-target baselines at the probe level (§10).
5. **Self-action tokens removed from the baseline context**, retained as a named variant (§5).
6. **Opponent ladder added**: order-0 (i.i.d.) below the order-1 Markov baseline (§3.2).
7. **Parametric ablation confound fixed.** Rev. 1 swept episode length `K`, which evaluates out of distribution under learned positional embeddings. Dose-response is now read off round index `t` within a fixed-length episode, which is free (§9.5).
8. **Extension path forked.** Rev. 1 asserted that second-order belief, not testimony, is the first genuine extension. Given that the motivating question is trust, reputation, and the lying/wrong distinction, testimony is both closer to the target and cheaper — it does not require adaptive opponents and preserves exact ground truth. Both branches are now specified and the baseline's obligations to each are stated (§14).
9. **Deferred design axes recorded** rather than omitted: the tie-chain PD/stag-hunt embedding and the payoff-sum deformation parameter (§15).
10. **Prior art section added** (§16). The substrate has direct precedent that should be read before building.

**Phase renaming.** Rev. 1's Phase A and Phase B are now Phase A and Phase C. Phase B is new.

---

## 1. What this experiment is for

The question: **can a belief-like internal structure be localized in a small transformer, validated causally, and tracked developmentally across a memorization-to-generalization transition?**

"Belief" is used in a deliberately restricted sense throughout: *a posterior over hidden state, updated by evidence, and used to select an action.* No phenomenological or mentalistic claim is intended. Terms borrowed from philosophy of mind are held provisionally and are not licensed by experimental success (see §13).

The substrate is repeated generalized Rock-Paper-Scissors against a hidden opponent policy. The model must infer the opponent's behavioural tendencies from observed play and exploit them. The hidden state is the opponent's policy; the belief is the posterior over it; the action is the model's move, graded by payoff rather than by a stated answer.

### Why this substrate

1. **Exact ground truth.** With a Dirichlet prior over the opponent's policy, the posterior predictive is closed-form. At every round of every episode we know precisely what a Bayes-rational agent should believe and what it should play. No LLM judge, no annotation, no stipulated label.
2. **Tiny sufficient statistic.** The action-relevant belief is a distribution over `n` actions — `n-1` free numbers. Small enough to regress activations against directly and watch decodability emerge.
3. **Revealed preference.** Belief is inferred from graded action under payoff, not from a report. The model never states a belief; it acts on one.
4. **Intrinsic group structure.** Win/lose/draw is determined entirely by the action difference modulo `n`. The model must represent a cyclic group. The modular-arithmetic grokking literature has known circuit solutions for this, giving a partial known-answer case against which circuit-identification tooling can be checked.
5. **Dense reward.** Every round scores. Policy-gradient training is viable at toy scale without the credit-assignment sparsity that usually destabilizes small-scale RL.
6. **Known-good prediction substrate.** The underlying inference problem — in-context estimation of a Markov transition matrix — has been studied directly, with documented staged transitions and identified circuits (§16). This lowers feasibility risk and supplies a mechanistic hypothesis to confirm or falsify rather than an open search.
7. **A clean path to testimony.** Because the reporter's belief has exact ground truth, "lying" can later be operationalized as divergence between a report and a causally validated internal posterior, rather than between a report and a behavioural proxy (§14).

### What motivated building a toy substrate at all

This work responds to three methodological problems in existing interpretability work on model self-report:

- **The frozen-checkpoint problem.** Ablation studies are run on static published checkpoints, which never compensate, reorganize, or relearn. A causal claim built on a single point of a training trajectory cannot distinguish a structurally central mechanism from one that would be rebuilt in a few gradient steps.
- **The judge problem.** When the target behaviour is operationalized by an LLM judge applying a rubric, the rubric does definitional work — fluency thresholds and required discourse orderings become part of what the phenomenon *means*.
- **The tool-validation gap.** Interpretability tooling is typically applied only where nobody knows the right answer, so a tooling failure and a genuine finding are indistinguishable.

This design addresses all three: the trajectory is ours to checkpoint, correctness is decidable from the generative process, and the group structure supplies a partial known-answer case.

---

## 2. Scope of the baseline

**In scope:** single model, fixed non-adaptive opponents, first-order belief only.

**Out of scope for the baseline** (later stages): reporters or testimony, deception, alignment as a hidden type, second-order belief, adaptive opponents, multi-agent co-learning, mixed-motive payoffs.

**Two structural facts to state up front, because several claims depend on them.**

*The model's actions cannot influence the observation stream.* The opponent's next action depends only on its own previous action, never on the model's. There is therefore no exploration-exploitation tradeoff: information arrives exogenously, and the decision problem factorizes into independent one-shot decisions given the belief. This is what licenses treating greedy best response to the exact posterior as an *exact* ceiling rather than a heuristic bound. It also means the baseline is, formally, a prediction problem with a decision layer bolted on — which is a feature at this stage and a limitation to be removed later.

*Against fixed opponents there is no penalty for predictability.* Nothing is watching, so greedy exploitation is optimal and the strategic pressure to randomize does not exist. The baseline measures whether belief forms and is used, not whether it is used strategically.

*Against fixed opponents, reputation reduces to prediction.* In a strictly competitive game the opponent is exhaustively characterized by its behavioural distribution; there is nothing for trust to be about, and a testimony channel would have only babbling equilibria. Mixed motive is a prerequisite for the trust-directed branch, and §14 specifies where it enters.

---

## 3. Task specification

### 3.1 Game

Generalized Rock-Paper-Scissors with `n` actions, `n` odd. Actions are integers `0..n-1`. Action `a` beats action `b` iff `(a - b) mod n` lies in `1..(n-1)/2`.

For `n = 3` this is standard RPS: `a` beats `b` iff `(a - b) mod 3 == 1`.

Outcome of playing `a` against opponent action `b`:

- `+1` if `(a - b) mod n` in `1..(n-1)/2`
- `-1` if `(b - a) mod n` in `1..(n-1)/2`
- `0` if `a == b`

**Baseline uses `n = 3`.** `n` is a configuration parameter; larger odd `n` is used for the tooling-validation runs (§9.4).

### 3.2 Opponent ladder

Three rungs. Build rung 1 first; it is strictly simpler and isolates one of the two things rung 2 requires.

**Rung 0 (i.i.d.).** The opponent samples each action independently from a fixed categorical distribution `p`, drawn per episode from a symmetric Dirichlet with concentration `α`. The sufficient statistic is a single count vector of length `n`. There is no row selection.

**Rung 1 (first-order Markov, the baseline).** The opponent policy is an `n × n` row-stochastic matrix `P`, where `P[i][j]` is the probability of playing `j` given its own previous action was `i`. First action uniform. Sampled at episode start, never revealed. Rows drawn independently from a symmetric Dirichlet with `α = 0.5`.

This family covers the interesting cases as special points: near-uniform rows give an unexploitable opponent; permutation-like matrices give cyclers; a collapsed matrix gives a constant player; asymmetric rows give biased-frequency players.

Note that rung 1 layers two problems: maintaining `n` count rows, and gathering the row indexed by the opponent's most recent action. Rung 0 removes the second. Running both tells you which of the two the transition is about.

**Rung 2 (adaptive).** Out of scope; see §14.

### 3.3 Action channel — two variants, run as a pair

**Variant A (action only).** Each round the model emits one action. Payoff equals the outcome.

Under this variant the optimal policy is `argmax` of the expected outcome, which depends only on the *sign structure* of the posterior, not its magnitudes. A model can reach the ceiling while representing only a coarse partition of belief space.

**Variant S (action plus stake).** Each round the model emits an action `a` and a stake `s` from a discrete grid. Payoff is

```
s · outcome(a, b) − λ · s²
```

With expected outcome `E[a]` as defined in §6, expected payoff is `s·E[a] − λs²`, maximized at `s* = clip(E[a] / (2λ), grid)`. The optimal stake is therefore a monotone function of the exploit margin, and the margin becomes behaviourally revealed rather than merely internally available. Choose `λ` so that `s*` spans the grid over the empirical margin distribution; a 4-point grid `{0, 1, 2, 3}` is sufficient.

The point of the pair is not robustness. **The comparison between A and S is a primary result.** If the full posterior is linearly decodable under S and only its argmax under A, that is direct evidence that internal representation is shaped by what behaviour demands rather than by what the task's generative structure contains — which is the sharpest available operationalization of the hypothesis that recoverable mechanism trails function.

### 3.4 Episode

- Sample or retrieve opponent policy and its pre-generated action trajectory (§4).
- Play `K = 64` rounds.
- Each round the model emits its action (and stake, under variant S); the opponent's action for that round is then revealed. The model must not see the opponent's round-`t` action before emitting its own.
- Episode return is the sum of per-round payoffs.

Because the model is causal and loss applies at every action position, a single 64-round episode already contains every prefix length from 1 to 64. All prefix-length analyses (§9.5) read off round index `t` and are therefore in distribution. Do not vary `K` to obtain them.

---

## 4. Opponent pool, trajectory pre-generation, and splits

The opponent's trajectory is exogenous — it depends only on the opponent's own previous action, never on the model's. It can therefore be pre-generated in full.

**Pre-generate trajectories.** For each opponent policy in the pool, pre-generate `m` complete 64-round opponent action sequences with a recorded seed. Training episodes replay these sequences rather than sampling fresh ones.

**Two memorization knobs.**

- `N` — pool size (data diversity). The number of distinct opponent policies.
- `m` — trajectory multiplicity. At `m = 1` the training set is a finite collection of `N` fixed sequences that can be memorized outright. As `m` grows, memorization becomes progressively less available and the counting solution more attractive. At `m → ∞` you recover fresh sampling and there is nothing to memorize.

**Sweep `N` as the primary knob.** Recent work characterizing in-context Markov learning finds that the memorization/generalization boundaries are set by data diversity, with a low-diversity memorizing regime, a high-diversity generalizing regime, and sharp boundaries between them (§16). A fixed pool of 4096 may well sit entirely inside the generalizing regime, in which case no memorization phase exists to transition out of and the developmental question is malformed. Run a diversity sweep — powers of 2 from 16 to 4096 — *before* committing to a single pool size, and select the operating point closest to the boundary, where the competition between mechanisms is visible.

**Primary split.** 50/50 over policies. Training episodes draw only from the train half; evaluation only from the test half. Record all seeds.

**Secondary split (after the primary result exists).** Hold out a geometric region of policy space — for example all matrices where row 0 assigns probability greater than 0.6 to action 0. Note the direction of the resulting shift: the held-out opponents are the *most exploitable* ones, so a generalization failure here appears as failure on the easiest cases, which is a legible signature.

---

## 5. Tokenization

**Baseline: opponent tokens only.** The model's own actions carry no information about the opponent's process — they are a distractor and they double the sequence length. The baseline context is the opponent's action history alone:

Vocabulary `n + 1`: `OPP_0 .. OPP_{n-1}` plus `BOS`. For `n = 3`, `K = 64`: vocabulary 4, sequence length 65. The model emits its action at each position from a separate action head; the sampled action is not fed back into the context.

Under variant S the action head emits a joint `(action, stake)` categorical, or two heads with a shared residual read. Prefer two heads: it makes the stake decodable separately.

**Variant SELF (later ablation).** Interleave the model's own actions as distinct tokens: `BOS, SELF_a0, OPP_b0, SELF_a1, OPP_b1, ...`, vocabulary `2n + 1`, length `2K + 1`. Whether the added distractor changes the solution is worth knowing, but it should not be the default.

**Variant SHARED (later ablation).** Single action alphabet with role inferred from position parity. Whether the model learns parity is itself interesting.

Loss and policy-gradient updates apply only at action-emission positions.

---

## 6. Reference solver

This must be built and verified **before any model is trained.** Everything downstream grades against it.

### Posterior

Each row of `P` has a symmetric Dirichlet prior with concentration `α` (use the sampler's `α = 0.5`; also support a mismatched-prior configuration for later robustness checks).

Let `c[i][j]` be the number of times, so far in the episode, that the opponent played `j` immediately after having played `i`. The posterior over row `i` is `Dirichlet(α + c[i][·])`.

Note the distinction, which matters for probing: the **maintained statistic** is the full count matrix `c` (all `n` rows, because the model does not know which row it will need next), while the **action-relevant projection** is the single row indexed by the opponent's most recent action. Both are probe targets (§9.2).

### Posterior predictive

Given the opponent's most recent action `i`, the predictive probability that its next action is `j`:

```
q[j] = (α + c[i][j]) / (n·α + Σ_k c[i][k])
```

This vector `q` (length `n`, sums to 1, so `n-1` free numbers) is the action-relevant belief state.

Under rung 0, drop the row index: `q[j] = (α + c[j]) / (n·α + Σ_k c[k])`.

### Best response, exploit margin, optimal stake

Expected outcome of playing action `a` against predictive `q`:

```
E[a] = Σ_{d=1}^{(n-1)/2} q[(a-d) mod n]  −  Σ_{d=1}^{(n-1)/2} q[(a+d) mod n]
```

For `n = 3` this reduces to `E[a] = q[(a-1) mod 3] − q[(a+1) mod 3]`.

- **Best response:** `argmax_a E[a]`.
- **Exploit margin:** `max_a E[a] − second-max_a E[a]`. Log it every round; it is the calibration variable for several measurements.
- **Optimal stake (variant S):** `s* = clip(max_a E[a] / (2λ), grid)`.

### Verification requirement

Before training anything: verify the solver by Monte Carlo. Sample a known policy, generate long opponent sequences, confirm the posterior predictive converges to the true row distributions at the expected rate, and confirm best response and optimal stake against brute-force expected-payoff evaluation over the discrete grid. **Do not proceed until this passes.**

---

## 7. Model

- Decoder-only transformer, 2 layers, 4 heads, `d_model = 128`, `d_head = 32`, MLP hidden 512, learned positional embeddings, causal masking.
- Two layers is the known minimum for the induction-style solution (previous-token head feeding a matching head). Keep a 3-layer configuration available as a fallback if 2 layers fails to transition; do not start there.
- AdamW. Sweep weight decay over `1e-2` to `1e-1`. Note that weight decay is a *secondary* knob here — data diversity (§4) is the primary lever on the memorization/generalization competition, and rev. 1 over-weighted weight decay by analogy to the modular-arithmetic setting.
- Large batch or full batch where memory allows.
- Train far past the point where training performance saturates.

Keep the architecture boring. Every nonstandard component is one more thing that could explain an anomalous result.

---

## 8. Training — the phase ladder

Run in this order. The phases have distinct epistemic roles and the later ones are read against the earlier ones.

### Phase A — supervised sanity run

Target: the payoff-maximizing action given the opponent's *true* policy, which the generator knows. Cross-entropy on action positions.

Purpose: cheap, clean curves; fast confirmation that the substrate transitions at all. This phase **smuggles in a label** — the target depends on hidden state the model cannot observe — and does not satisfy the revealed-preference criterion. It is a debugging instrument. Do not report Phase A findings as evidence about belief.

### Phase B — self-supervised opponent prediction

Target: the opponent's actual next action. Cross-entropy at opponent-token positions.

This is *not* a smuggled label in the sense Phase A is. The target is an event the model observes one token later regardless; nothing is stipulated about what belief means, and no privileged access to hidden state is granted. What it does do is train the posterior predictive *directly*, which makes finding it close to tautological.

Its role is therefore as a **reference**: it establishes where in the network, at what layer, and at what point in training an exactly-specified posterior appears when the objective demands it. Phase C is then read as the question of whether the same structure appears when nothing demands it except consequences.

Report the same measurement suite (§9) for Phase B as for Phase C.

### Phase C — policy gradient (the headline)

REINFORCE with a learned or running-mean baseline; reward equals per-round payoff. No labels anywhere; the model sees only consequences. Run under both action-channel variants (§3.3).

Note what Phase C is asking of the network: under variant A there is no gradient anywhere that asks it to predict the opponent, so the entire counting-and-normalizing machinery must be built through the payoff channel alone. This is the interesting condition and also the fragile one.

**Rescue path if Phase C stalls (Phase C-aux).** Payoff plus an auxiliary opponent-prediction loss with weight `β`, swept downward toward zero. The smallest `β` at which the belief structure still forms is itself a measurement — it quantifies how much predictive pressure the payoff channel fails to supply.

**All headline results come from Phase C.** Phase C-aux results are reported as a separate, clearly labelled interpolation.

### Seeds and pre-registration

Minimum 5 seeds per condition. Fix the primary outcome statistic and the transition definition (§9.1) before looking at any decodability curves.

### Checkpointing

Checkpoint **densely**, with higher density around any visible transition. Prior work indicates generalizing circuits form gradually beneath a memorizing solution and that the visible transition is a cleanup phase rather than the moment generalization appears. The trajectory is the primary object of study, not the endpoint. Budget disk for this; it is the whole point.

---

## 9. Measurements

### 9.1 Transition

Mean return per round on train and test pools, against two references: the exact solver (ceiling) and uniform random play (floor). Plot against training step.

**Pre-register the transition definition.** Primary: the step at which held-out mean return per round first crosses the midpoint between floor and ceiling. Secondary: the step maximizing the derivative of held-out return with respect to log training step.

**Report the train/test gap explicitly.** If there is no gap, there was no memorization phase, and claims about a memorization-to-generalization transition should be withdrawn regardless of how sharp the return curve looks. Use the gap as the diagnostic for whether the diversity sweep (§4) found the right operating point.

### 9.2 Belief decodability

At every checkpoint, for each layer and each position, fit linear probes from the residual stream to each of four targets:

1. **Full predictive**, in centered-log-ratio coordinates. `q` lives on the simplex, so raw probabilities, log probabilities, and centered log-ratio give different answers about what "linear" means; centered log-ratio removes the redundant direction. State the choice and report at least one alternative.
2. **Full count matrix / posterior over all rows** — the maintained statistic, not just the action-relevant projection.
3. **Argmax class** — which action is the best response (3-way classification).
4. **Exploit margin** — scalar regression.

Probe at **both** opponent-token positions (where evidence arrives) and action-emission positions (where it must have been gathered).

Probes are fit on training episodes and evaluated on held-out ones. Report per-layer profiles, not just the maximum.

Plot decodability against training step. **The central question of the baseline is whether each of these rises at, before, or after the return transition — and which of the four rises at all.**

Reporting requirement: report **excess** decodability over the controls in §10.3, not raw R² or raw accuracy. A rising raw curve is compatible with representation drift and norm growth and says nothing on its own.

### 9.3 Belief usage

Decodability shows the belief is represented. Usage requires more:

- Fraction of model actions matching the best response to the *decoded* belief.
- Fraction matching the best response to the *true* belief.
- Both as a function of exploit margin. A model genuinely using its belief should track the best response closely at large margin and behave near-arbitrarily at small margin.
- **Under variant S:** correlation between emitted stake and optimal stake, as a function of margin. This is the measurement that distinguishes "represents a decision boundary" from "represents a graded posterior."

The A-versus-S comparison (§3.3) is reported here as a primary result: which probe targets from §9.2 are decodable under each variant.

### 9.4 Group structure and tooling validation

Win/lose/draw depends only on the action difference modulo `n`, so a cyclic group must be represented somewhere.

Honest caveat: at `n = 3` the group is too small for a rich representation-theoretic signature — essentially one non-trivial frequency pair. The validation case is thin at the baseline setting.

**Mitigation:** run the identical pipeline at `n = 5, 7, 9`, where the cyclic structure produces a signature comparable to the modular-arithmetic literature. If the tooling recovers the expected structure at larger `n` without being told what to look for, that is evidence the tooling works, and it transfers to the `n = 3` runs.

### 9.5 Interventions

Only after 9.1–9.3 produce stable results.

- **Dose-response over evidence.** Ablate candidate components and measure effect size as a function of round index `t` within the episode. A component implementing belief-tracking should matter more as evidence accumulates; a correlated component should show a flat profile. Because all prefix lengths occur inside every episode, this is in-distribution and free. (Rev. 1 proposed sweeping episode length `K`, which confounds the measurement with positional out-of-distribution degradation under learned positional embeddings.)
- **Temporal dissociation.** Ablate at every checkpoint and plot effect size against training step. A genuine belief mechanism should show its ablation effect *growing* across the transition; a memorization artifact should show it *decaying*.
- **Relearning time.** Ablate, resume training, measure steps to recovery against a matched control ablation of similar magnitude in a non-candidate direction. Slow recovery indicates a structurally distinctive position; comparable recovery across targets indicates degeneracy — the "circuit" is whichever route the search happened to find first.
- **Cross-seed circuit comparison.** Whether the same structure is found in independently seeded runs is a cheap and direct test of whether "the circuit" is a property of the task or of the search. Report it alongside relearning time; the two answer the same question from different directions.

**Caveat to carry into all of the above.** Mean-ablation substitutes a population average, not an absence, and may hand downstream layers a state the network never produces on any single forward pass. Inherited hazards from the lesion tradition apply: distant dysfunction from lost input rather than local destruction; a component acting as conduit rather than origin; degenerate alternate routes producing the same function.

---

## 10. Control conditions

These are not optional and they are cheap. Without them a positive result is not defensible and a negative result is not interpretable.

### 10.1 Task-level null — unexploitable opponent

All rows uniform. No belief is possible; the posterior predictive is constant at uniform and the exploit margin is identically zero. Any apparent belief decodability in this condition is spurious by construction and calibrates the false-positive rate of the entire probe pipeline.

### 10.2 Task-level floor — constant opponent

Opponent plays a fixed action every round. Inference is trivial; only the identity of one action must be recovered. This bounds the measurement from the other side and confirms the machinery detects belief when belief is maximally easy.

### 10.3 Probe-level baselines

Every decodability number in §9.2 is reported as excess over the maximum of:

- **Random-init control.** Identical architecture, untrained weights, same probe fitting procedure.
- **Raw-feature control.** Probe fit directly on the accumulated one-hot token history — the information trivially available without any computation. This is the decisive control: counts are nearly linearly recoverable from the input by accumulation, so a probe may be finding the input rather than the belief.
- **Shuffled-target control.** Same probe capacity, targets permuted across episodes. Establishes what the probe's capacity alone buys.

Report selectivity in the control-task sense: the gap between real-target and shuffled-target performance at matched capacity.

### 10.4 Replication

Minimum 5 seeds per reported condition, with the primary comparison statistic fixed in advance.

---

## 11. Build order

1. Game engine, opponent sampler, trajectory pre-generation with recorded seeds; rung 0 and rung 1.
2. **Exact reference solver, with Monte Carlo verification.** Gate: verification must pass before anything else proceeds.
3. Tokenizer and episode serializer; round-trip tests.
4. Model and training loop; Phase A supervised run on rung 0 to confirm the substrate transitions.
5. **Diversity sweep.** Vary `N` (and `m`) under Phase B to locate the memorization/generalization boundary. Select the operating point. Do not skip this; it determines whether there is a transition to study.
6. Phase B self-supervised run with dense checkpointing, at the selected operating point, rungs 0 and 1.
7. Probe harness with all four targets and all three probe-level controls; decodability across checkpoints.
8. Task-level control conditions (§10.1, §10.2).
9. Phase C policy-gradient run, variants A and S.
10. Belief-usage analysis, including the A-versus-S comparison.
11. Larger-`n` runs for tooling validation.
12. Interventions.

---

## 12. What this experiment can and cannot establish

**Can:** whether a structure linearly encoding the exact Bayesian posterior forms; when it forms relative to the behavioural transition; which *aspect* of the posterior forms (full distribution, argmax, margin) and under which action channel; whether the model's actions are consistent with using it; whether candidate components are causally necessary under dose-response and temporal-dissociation tests; whether ablated structure is quickly rebuilt; whether the same structure recurs across seeds.

**Cannot:** anything about phenomenology, experience, or introspection. Anything about deception — the baseline has no report channel and no incentive structure over reports. Anything about trust or reputation — those require mixed motive, which the baseline excludes by construction. Anything about second-order belief. Anything about whether the transformer's solution resembles what larger models do.

**On negative results.** Rev. 1 claimed that a null here would be substantial evidence against the tractability of belief-localization generally. That claim was too strong as stated, because a null confounds at least three things: belief does not form, belief forms but not in a linearly decodable basis, and training simply failed. The phase ladder (§8) and the control conditions (§10) exist to separate these. With them in place, a null is informative: if Phase B produces a clean decodable posterior and Phase C does not, that is a specific and meaningful finding about what payoff pressure alone builds. Without them, a null is uninterpretable.

---

## 13. Terminological discipline

To be maintained in code comments, logs, and write-ups:

- **Belief** — posterior over hidden state, updated by evidence, used to select action. Nothing more.
- **Circuit** — currently underspecified in the literature, ranging between a single feature, a hand-selected feature set, and "whatever the ablation procedure flagged." The last is close to circular. This design's response is to specify the target *independently of the search that finds it*: the exact posterior is known before any model is trained.
- **Trust, reputation** — not applicable to the baseline. In a strictly competitive game against a fixed opponent these reduce to prediction. Do not use the words before §14's testimony branch exists.
- **Theory of mind, introspection, deception** — not applicable to the baseline. Do not use these words in logs or results for this stage.
- **Experience, phenomenology** — not used. The design specifies an information architecture: who observes what, in what order, encoded as which tokens.

---

## 14. Extension path — two branches

Rev. 1 asserted that the first genuine extension is second-order belief rather than testimony. That ordering follows from a research question about strategic depth. It does not follow from a research question about trust, reputation, and the distinction between lying and being wrong, which needs less machinery than rev. 1 assumed. Both branches are specified here; the baseline should be built knowing which one it is serving.

### Branch T — testimony (cheaper, closer to the motivating question)

What the lying/wrong distinction actually requires is three things: a belief state with exact ground truth, a report channel not constrained to match it, and an incentive asymmetry that sometimes makes misreport profitable. The baseline supplies the first, which is the rare one. Second-order belief is required for *strategic* deception — selecting the lie that will be believed — but not for the distinction itself.

Minimal design:

- Two agents, **actor** and **reporter**, playing against the same fixed opponent family. Opponents remain non-adaptive, so the exact solver survives intact.
- The reporter observes rounds the actor does not. The actor receives the reporter's message before acting.
- Message channel of limited bandwidth — one token from a small alphabet, or a coarse-binned distribution.
- **Alignment scalar `w`.** The reporter's payoff is `w` times the actor's return plus `(1 − w)` times its own exploitation return against the same opponent. One scalar, swept from 0 to 1.

Predictions worth pre-registering: at `w = 0`, opposed interests should yield babbling — the actor learns to ignore the channel. At `w = 1` the reporter is a fully aligned informant and reporting should be honest. The interesting region is intermediate, where partial credibility must be established.

The payoff of this branch is the operationalization it enables. "Lying" becomes divergence between the emitted message and the reporter's *decoded and causally validated* posterior — not divergence between a message and a behavioural proxy, and not a judge's rubric. That is a stronger operationalization than the literature this project is responding to currently has.

Note the requirement this places on the baseline: the probe and intervention pipeline must be validated well enough that "the reporter's belief" is a defensible measurement rather than a probe artifact. §10 is not optional if branch T is the destination.

### Branch S — strategic depth (rev. 1's path)

Against an adaptive opponent, the meta-regress ("I model you modelling me") closes at period `n` for the restricted family of opponents that apply a fixed rotation to their best response: shifting your best response `n` times returns you to where you started, because argmax composition over the cyclic group has order `n`. First-order belief is the opponent's action distribution; second-order belief is which rotation the opponent applies, one of `n` possibilities.

**Correction to rev. 1.** This closure is a property of a chosen restriction of the strategy space, not a theorem about the game. The best-response map on the simplex is not a group action; against mixed strategies the regress does not close, it drifts toward the uniform equilibrium. The design idea survives; the theorem-shaped phrasing does not.

Prerequisites: adaptive opponents (the RoShamBo competition corpus, 43 policies preserved in OpenSpiel, or the Iocaine-style meta-strategy family). Cost: once opponents adapt, the exact ceiling stops being computable in closed form, and the clean grading against a known optimum that justifies the whole substrate goes away. That is the boundary condition on this branch and it should be weighed before entering.

### Which branch the baseline serves

Branch T needs: a validated probe pipeline, exact ground truth preserved, fixed opponents, and a second agent. Branch S needs: adaptive opponents and the sacrifice of the exact ceiling. The baseline as specified here serves branch T. If branch S is the real destination, the diversity sweep and the control battery matter less and the larger-`n` group-structure work matters more.

---

## 15. Deferred design axes

Recorded so the decision is made deliberately rather than by omission.

### 15.1 Tie-chain payoff embedding

Proposed mechanism: under normal play, payoffs are zero-sum as specified. If a tie occurs on the round following another tie, the payoff for that round (or the subsequent one) is drawn from a different, symmetric matrix indexed by the consecutive tied actions. The proportion of mixed-motive to zero-sum play is then tunable via the tie-chain rate.

Attractive because entry into the mixed-motive regime is *endogenous* — it requires successful mutual prediction, so coordination is itself the gateway — and because it requires no new actions or tokens.

**Open question to resolve before implementing.** A tie means both players played the same action, so tie-chain outcomes are symmetric by construction. Symmetric outcomes are the diagonal of a 2×2 game; the off-diagonal cells — temptation and sucker — are exactly what makes a prisoner's dilemma a dilemma and cannot be reached this way. As literally described, the embedding yields a **stag hunt** (joint gain, joint loss, coordination required) rather than a prisoner's dilemma. A second reading, in which the two ties are only a gate and the payoff matrix applies to a *third* round whose moves may differ, does yield a genuine dilemma. Decide which is intended.

For a research program targeting trust specifically, the stag hunt may be the better base game on Skyrms' argument: the prisoner's dilemma models cooperation under temptation, while the stag hunt models trust and assurance — the question is not whether you would gain by defecting but whether you believe the other party will show up.

**Why deferred.** Against fixed non-adaptive opponents the embedding is inert: there is nothing reciprocating, so no cooperation is possible and the mechanism does no work. It also makes the decision problem non-myopic — a current action affects whether a chain starts — which costs the closed-form greedy optimum that grades everything downstream. It becomes live only alongside adaptive opponents.

### 15.2 Payoff-sum deformation

A simpler mixed-motive knob: tilt the payoff matrix so that the outcomes at each cell no longer sum to zero. At balance you have the pure cyclic game with closed orbits under replicator dynamics; tilt one way and the interior point becomes attracting, the other and you get an outward spiral. This is a single continuous parameter and is trivial to implement.

**Why deferred.** Same reason: against a fixed opponent, nothing to cooperate with, so it changes the arithmetic without changing the strategic situation. Also inert in the baseline.

### 15.3 Where mixed motive should actually enter first

Given 15.1 and 15.2 are both inert against fixed opponents, the cheapest place to introduce mixed motive is **between agents rather than inside the game** — the alignment scalar `w` in branch T (§14). It leaves the game, the solver, and the exact ground truth entirely untouched, and it makes trust a one-dimensional sweep rather than a redesign. Revisit 15.1 and 15.2 only once adaptive opponents exist.

---

## 16. Prior art to read before building

The substrate is less unexplored than rev. 1 implied. This is good news for feasibility and it relocates the novelty claim to where it actually is: the causal validation, the payoff wrapper, and the testimony extension — not the inference task itself.

**Directly on this task.** Edelman, Tsilivis, Goel, Edelman and Malach, "The Evolution of Statistical Induction Heads: In-Context Learning Markov Chains" (NeurIPS 2024, arXiv 2402.11004): transformers trained to predict sequences from Markov chains drawn from a prior form *statistical induction heads* computing next-token probabilities from in-context bigram statistics, and pass through staged training phases — uniform, then unigram, then a rapid transition to the bigram solution — with evidence that the simpler unigram solution *delays* formation of the bigram one. That is the same inference problem as rung 1 here, minus the payoff layer, and the staged structure is directly relevant to §9.1.

**Directly on the diversity knob.** Gibson, Cui and Reddy, "Distinct mechanisms underlying in-context learning in transformers" (arXiv 2604.12151, April 2026): a mechanistic characterization of transformers trained on a finite set of discrete Markov chains, identifying four algorithmic phases distinguished by whether the network memorizes or generalizes and whether it uses 1-point or 2-point statistics, implemented by two distinct subcircuit motifs — a *statistical induction head* for generalization and a *task recognition head* (encode, pool, decode, producing a task vector) for memorization. The memorization/generalization boundaries are set by data diversity, the number of distinct chains, with one boundary from kinetic competition between subcircuits and a second from a representational bottleneck.

This paper is the reason §4 was rewritten. It supplies both the knob and a theory of where the boundaries sit, and it means the mechanistic hypothesis for this substrate is already partly specified — which converts §9 from an open search into a confirmation-or-falsification exercise. Read it before the diversity sweep.

**Adjacent.** Nichani, Damian and Lee on transformers learning causal structure from Markov sequences by gradient descent; Bietti et al., "Birth of a Transformer," on induction heads and associative memory; Olsson et al. on induction heads generally.

**Methodological.** Hewitt and Liang on control tasks and probe selectivity (§10.3). Nanda et al., "Progress Measures for Grokking via Mechanistic Interpretability," and the grokking literature generally — noting that the grokking analogy applies less directly here than rev. 1 assumed (§4).

**For the extension branches.** Crawford and Sobel, "Strategic Information Transmission," on cheap talk and babbling equilibria under opposed interests — the formal basis for the `w = 0` prediction in §14. Skyrms, *The Stag Hunt and the Evolution of Social Structure*, for the trust-versus-temptation distinction in §15.1. Proper scoring rules and the betting elicitation of degree of belief, for the rationale behind variant S in §3.3.

*All citations above should be verified against the primary sources before appearing in any write-up.*

---

## 17. Open questions

1. Which reading of the tie-chain mechanism is intended (§15.1), and is the stag hunt or the prisoner's dilemma the right target game for trust?
2. Is branch T or branch S the real destination? The build order in §11 assumes T.
3. Does the A-versus-S comparison (§3.3) belong in the baseline, or does the added vocabulary and head complexity justify deferring variant S to a second pass?
4. At rung 1, does the transition of interest concern the counting machinery, the row-gathering machinery, or their composition? Rung 0 is the instrument for answering this, but the answer determines what "the belief circuit" names.
