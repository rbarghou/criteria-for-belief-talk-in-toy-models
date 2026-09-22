# Amendments Register — RPS Belief Circuits

**Opened:** 2026-09-19
**Scope:** proposed changes to `rps-belief-circuit-baseline-protocol-2026-09-19.md` surfaced during the section-by-section reading. Candidates for a rev. 3; none are decided.

Companion file: `rps-belief-circuits-questions-register-2026-09-19.md`

---

## A1 — Opponent-type rung (hierarchical latent)

**Raised at:** §1, reason 1 (Dirichlet / conjugacy).
**Bears on:** §3.2 opponent ladder, §6 solver, §9.2 probe targets, §14 branch T.

Currently α is fixed at 0.5 for both sampler and model prior. Proposal: make the *kind* of opponent a second, coarser hidden variable, inferred alongside the specific policy.

- **Discrete, not continuous.** A discrete set of α values preserves exact tractability: maintain a weight per α value, predictive becomes a finite weighted mixture. A continuous range requires numerical integration over α — cheap (one-dimensional) but no longer closed-form, and the closed form is what everything downstream grades against.
- **What it buys:** a second layer of hidden state — not just *which* opponent but *which kind*. A step toward "type" in the game-theoretic sense, which is what the trust/reputation program needs. Practically, a small categorical latent is a much cleaner probe target than a continuous vector: it separates "this is a lopsided opponent" from "this opponent favours paper."
- **Cautions.** (i) A pure counting solution is robust across α — it converges to the same place, only at a different rate — so type inference may do very little work, and what work it does concentrates early in the episode where signal is weakest. The structure could be added and prove invisible. (ii) Varying the sampler's α while holding the model's prior fixed is a *different* experiment — prior misspecification, a robustness test already gestured at in §6. Identical in code, not the same thing.
- **Preferred variant:** discrete *structural families* (cyclers, constant players, frequency-biased players) rather than discrete α. Same hierarchical structure, behaviourally legible latent.

**Status:** deferred, not decided.

---

## A2 — §1 reason 2: sufficient statistic wording

**Raised at:** §1, reason 2.
**Bears on:** §1 only (wording), with a conceptual echo in §6 and §9.2.

Reason 2 states the sufficient statistic as "a distribution over n actions — n−1 free numbers," which is the *predictive* and therefore has row selection already baked in without saying so. The transition count matrix is sufficient for inferring the policy, but not for prediction: prediction requires knowing which row to read, which is determined by the opponent's most recent action.

**Fix:** state the sufficient statistic as the count matrix *plus a current-state index* — 9 numbers plus a 3-way index at n=3 — and let the predictive be introduced as the projection of that.

**Status:** accepted in principle (Ramsey requested it be logged).

---

## A3 — §9.3: add an internal rationalizability check

**Raised at:** §1, reason 3 (revealed preference), during the structuralism digression.
**Bears on:** §9.3, §12.

§9.3 currently measures consistency of the model's actions with the *decoded* belief and with the *true* belief. Both are accuracy measures. Neither measures whether the action sequence is coherent at all.

Revealed preference recovers a utility function only if observed choices satisfy consistency axioms; if they are violated, no rationalizing function exists and the method has nothing to say. The protocol grades against a Bayes-optimal reference and thereby imports that consistency assumption silently. A model whose behaviour is *incoherent* — not rationalizable by any belief trajectory, correct or otherwise — would score badly on return and poorly on decodability, and the document as written would read that as "no belief structure formed." Those are different findings.

**Proposal:** add a third measurement — whether the observed action sequence admits *some* coherent belief trajectory, independent of whether it is the right one. This separates "the model is wrong" from "the model is not doing the kind of thing that admits of being right or wrong."

**Status:** proposed.

---

## A4 — §5: reclassify the SELF variant

**Raised at:** discussion of the program's direction.
**Bears on:** §5, §14, §17.

§5 removes the model's own actions from the baseline context, correctly, because they carry no information about the opponent's process. The SELF variant (interleaving the model's own action tokens) is currently filed as a later ablation.

For any extension toward self-modelling, that channel is not a distractor — it is the only route by which a self-model could form. The optimisation that makes the baseline clean deletes the thing a later stage would need.

**Proposal:** keep SELF out of the baseline, but reclassify it in the document from "later ablation" to the named axis along which the program extends, so the reason it is absent is recorded as a deliberate scoping decision rather than a cleanup.

**Status:** proposed.

---

## A5 — New section: belief versus function approximation

**Raised at:** discussion of the program's direction.
**Bears on:** §9 (new subsection), §12, §13.

**The problem this addresses.** As specified, the protocol does not distinguish belief from function approximation. The task is in-context estimation of a transition matrix; §16 establishes that transformers solve it with an identifiable circuit; and every target in §9.2 is a deterministic function of the observed token sequence. The Bayesian vocabulary describes the optimal input-output map — it is not evidence that the network does anything other than approximate it. A hostile reading: the intermediate activations of a function approximator have been relabelled "belief," which is the same essentialist move the MINP critique charges — assuming a determinate fact sits in the network awaiting discovery, then discovering it.

**Proposed criteria**, all implementable and all substrate-independent:

1. **Multi-consumer structure.** A function approximator can collapse its intermediate along whatever route is cheapest. A belief is a representation not indexed to a single use. Test: one model whose single internal state must serve several distinct decision problems (predict the opponent, select an action, size a stake) — does one shared representation serve all three, or do three task-specific features form independently?
2. **Off-manifold coherence.** Edit the internal state to a posterior the model has never had reason to hold — an arbitrary value, not one from the training distribution — and ask whether downstream behaviour follows it correctly. A memorized map has no commitments off the manifold its data produced; a general representational format does. Activation patching used as belief transplant rather than as lesion.
3. **Path independence.** The same count matrix is reachable by many orderings of the same observations. If the representation converges regardless of route, the network has a state; if it retains the path, it has a trace.

**Note on what these share.** None reads a belief out of the network. Each checks whether the interior is *consistent* under some transformation — across consumers, across interventions, across histories. This is exterior consistency-checking applied to interior states, which is the MINP critique's own thesis reappearing inside the method rather than as a conclusion about it.

**Status:** proposed. Probably the highest-value amendment on this list.

---

## A6 — §12: restate the deliverable

**Raised at:** discussion of the program's direction.
**Bears on:** §12, and the framing of §1.

Every property that makes this substrate gradeable makes it non-social: exact ground truth exists because the opponent does not respond; greedy play is exactly optimal because the model cannot influence what it observes; the closed form survives because nothing is watching. The referential circularity that characterizes social belief is precisely what the tractability is purchased by excluding.

Consequently the bootstrap logic works under one reading and fails under another:

- **Fails** if the deliverable is "we found the belief circuit, and stage two adds another agent." The belief circuit in a non-social task is a bigram estimator; the social case will not contain one. Nothing transfers.
- **Works** if the deliverable is "we validated substrate-independent criteria for distinguishing belief from function approximation against a case where the right answer is independently known." The criteria in A5 are not about rock-paper-scissors; they are about representational format, and they can only be calibrated where ground truth is free.

**Proposal:** restate §12 so the protocol is explicitly a *calibration rig for belief criteria* rather than the first rung of a belief ladder. Same experiment, same code, different claimed deliverable. Also state the baseline's non-sociality as a named limitation with a named exit (§14 branch T), rather than leaving it implicit in §2.

**Status:** proposed.

---

## A7 — Separate the program from the protocol

**Raised at:** discussion of the program's direction.
**Bears on:** document structure.

The reading surfaced a program-level goal (operationalizing critical theory as mechanistic-interpretability measurements; bootstrapping toward toy models capable of self-reference and structured misrecognition) that the protocol is not ready to serve and should not be rewritten around. A program goal that surfaces mid-reading can retroactively deform a sound protocol.

**Proposal:** keep the protocol minimal and honest about being a calibration rig, and put the program — bootstrap logic, the self-reference target, and the working criterion that *a theoretical claim earns its place when it changes a measurement* — in a sibling orientation document that the protocol points at.

**Related note, recorded so it is not lost.** A concrete route toward structured misrecognition that this substrate would support: require the model to predict its own next action alongside the opponent's. Its action is sampled from a distribution it has no introspective access to — it observes its own past choices but not the logits that produced them. The self-model is therefore an idealization assembled from its own exterior, and the gap between predicted-self and enacted-self is structured, persistent, and directly measurable. Note that this requires only stochastic action selection and self-observation — not an opponent — so it may not want to be the same experiment. Forcing the two threads together could damage both.

**Status:** proposed.

---

## A8 — §8 Phase C: specify exploration control

**Raised at:** §1, reason 5 (policy gradient).
**Bears on:** §8 Phase C and C-aux, §11 build order.

§8 specifies REINFORCE with a learned or running-mean baseline and says nothing about exploration.

Because policy gradient only ever observes the outcome of the action actually taken, learning depends on the policy staying stochastic enough to keep sampling alternatives. A policy that collapses early onto a deterministic choice stops receiving information about the other actions and can sit there permanently, never discovering that one of them pays better. With only 3 actions and dense reward, premature collapse is a realistic failure mode, not a theoretical one.

**Fix:** specify the exploration control explicitly — entropy regularization (a penalty on the policy becoming over-confident) or a temperature on the action distribution, with its schedule — and treat its setting as a pre-registered hyperparameter rather than something tuned after seeing results. Under variant S this applies to the stake head as well as the action head.

**Status:** accepted in principle (Ramsey requested it be logged).

---

## A9 — §9.4: the known-answer case covers the wrong half

**Raised at:** §1, the tool-validation gap.
**Bears on:** §9.4, §12, and (as the cheap fix) §16.

The tool-validation argument rests on the cyclic group structure, where the modular-arithmetic grokking literature has established what the circuit looks like: a circular representation with rotation-style composition. §9.4 already concedes this signature is thin at n=3 and proposes larger odd n as the mitigation.

**The unstated problem is different and larger.** The known answer concerns the *arithmetic* — the mechanism implementing the beats-relation. The belief structure is a different computational shape: an accumulator that counts and normalizes over a context window. Tooling that successfully recovers a rotational representation is not thereby validated for recovering an accumulator. So the known-answer case validates part of the pipeline and not necessarily the part the experiment is actually about.

**Cheap fix, using material already in the document.** §16 supplies a second known-answer case aimed at exactly the right half: the statistical induction head (the generalizing motif) and the task recognition head (encode, pool, decode — the memorizing motif) identified for in-context Markov estimation. §9.4 should add validation against these reported circuit motifs alongside the modular-arithmetic case, so that both halves of the pipeline have a known answer.

**Status:** proposed.

---

## A10 — Add a reactive-stationary opponent rung (rung 1.5)

**Raised at:** §2, exploration-exploitation.
**Bears on:** §2 (structural facts), §3.2 (ladder), §6 (solver and references), §9.1 (what the return ratio means), §14, and orientation open question 5.
**Priority:** high. This is the structural gap in the ladder, not a refinement.

**The proposal.** An opponent whose state is the *pair* of last actions — the model's and its own — rather than its own alone. Nine states, each with a 3-way distribution, so a 9×3 table instead of 3×3. The opponent is still fixed, stationary, non-learning, and drawn once at episode start. It does not model the model; it merely reacts to it.

**The gap this fills.** §3.2's ladder runs exogenous (rung 1) → adaptive (rung 2) and omits the middle. §2's out-of-scope list names "adaptive opponents" and "multi-agent co-learning," neither of which describes this. As written, the proposal is not excluded, not specified, and likely to be misfiled as adaptive.

**Also fix:** §2 states exogeneity as a property of the substrate ("the model's actions cannot influence the observation stream"). It is a property of rung 1 specifically and should be stated as such.

**What it recovers — three things at once:**

1. **The action-observation loop closes.** The model's action becomes an input to the process generating its future observations. This is the minimal form of that closure — the opponent reacts without modelling — and it is the condition identified as necessary for self-reference in orientation open question 5.
2. **Exploration returns** in the decision-theoretic sense §2 declares dead. Some rows are reachable only through the model's own choices: to learn the row for joint state (rock, paper) it must play rock when the opponent last played paper. State-space coverage becomes something the agent controls and can fail at.
3. **Temporal credit assignment returns at depth exactly one.** An action at round *t* determines which row governs *t*+1, and nothing beyond. This rung is therefore a concrete candidate answer to the minimal-reward-chain question (orientation Q5), arrived at independently of it.

**What it costs.**

- *The posterior survives intact.* Nine rows, each Dirichlet, still conjugate, still counting and normalizing. 27 numbers instead of 9. Probe targets grow but stay small.
- *The Bayes-optimal reference is lost.* Greedy play stops being optimal because an action trades immediate payoff against both future payoff and future information. Exact Bayes-optimal play requires backward induction over a continuous 27-dimensional belief space and is not computable.
- *Evidence per row drops threefold.* Nine rows from 64 rounds gives roughly 7 observations per row against 21 at rung 1. Inference is substantially harder at the same episode length; longer episodes may be needed, which costs context and compute and shifts where the transition sits.

**The reference ladder that replaces the single ceiling.** All four are exactly computable:

1. **Uniform random** — floor, as now.
2. **Posterior-greedy** — exact posterior (still closed-form), best immediate response, no planning. *Belief without planning.*
3. **Certainty-equivalent** — take the posterior mean matrix, treat it as truth, solve exactly. With the matrix fixed the problem is a finite MDP over 9 states and 3 actions across 64 rounds; backward induction on that is trivial. So planning is exact and only the belief half is approximated. *This is the heuristic optimum.*
4. **Omniscient optimal** — same finite MDP solved with the true matrix. Unachievable upper bound.

**Why the ladder is an improvement, not just compensation.** The gap between (2) and (3) is the value of planning. The gap between (3) and (4) is the cost of not knowing. The gap between (3) and the uncomputable Bayes-optimal is the value of deliberate information-gathering — identically zero at rung 1, nonzero the moment the loop closes, and boundable from below. Rung 1 collapses belief and planning into one reference and makes the decomposition invisible; rung 1.5 separates them. A model matching (2) but not (3) has the belief and not the plan, which is a distinction that matters directly to whether belief is a distinct object from the policy consuming it.

**Consequence for §9.1.** Under rung 1, "fraction of ceiling achieved" measures inference quality alone. Under rung 1.5 it conflates inference and planning, and the ladder replaces the single ratio.

**Status:** requested for inclusion.

### A10a — The nesting property (Ramsey's observation)

Rung 1 is the subspace of rung 1.5 where, for each of the opponent's own last actions, the three rows corresponding to the model's three possible moves are identical. A linear constraint on the larger table. Four consequences:

1. **One experiment, not two.** Train on the larger family and put both kinds of opponent in the evaluation pool. Rung 1 becomes a subset of the test set rather than a separate run with its own model and curves.
2. **The distinction is itself the right latent.** "Does this opponent react to me, or is it indifferent to me" is the minimal form of "is there another agent here." This is a far more legible type variable than the α proposal in A1, and semantically closer to the program: reactivity is the precondition of recognition. Supersedes A1 as the preferred opponent-type latent.
3. **It stays exact.** Put a prior over which family the opponent came from; the posterior over reactivity is then a comparison between a pooled and an unpooled Dirichlet-multinomial, both with closed-form evidence. The predictive becomes a two-component mixture. Still exact, still cheap, still no judge.
4. **It yields a clean measurement.** A model that has learned the 9-row structure and meets a 3-row opponent must *discover the degeneracy* — notice that rows it tracks separately are the same, and pool evidence across them. Pooling triples effective sample size per row, so a model that fails to pool is measurably worse on exactly those opponents and fine on the others. This asks directly whether the network discovers that it is irrelevant to the opponent, or tabulates forever. A question about whether it represents structure or merely counts, with a behavioural signature.

---

## A11 — Separate edge, margin, and evidence (three scalars currently conflated)

**Raised at:** §3.3, exploit margin.
**Bears on:** §3.3 (an outright error), §6, §9.2, §9.3.

**The error.** §3.3 states that the optimal stake under variant S is a monotone function of the exploit margin. It is not. §6's formula sets the optimal stake proportional to `max_a E[a]` — the expected outcome of the *best* action — while §6 defines the exploit margin as `max_a E[a] − second-max_a E[a]`. For n=3 these move independently: the three expected outcomes always sum to zero, but the top one and the top-minus-second are different functions of the predictive. §3.3's prose is wrong; §6's formula is right.

**Three distinct scalars, all currently called or treated as one:**

1. **Edge** — `max_a E[a]`. How much value is on the table. Governs the optimal stake.
2. **Decision margin** — `max_a E[a] − second-max_a E[a]`. How decisively the belief picks out one action; how robust the argmax is. Governs whether a disagreement between model and reference is meaningful.
3. **Evidence** — the row sum of the posterior concentrations for the currently relevant row. Epistemic confidence in the belief itself, as distinct from the decisiveness of the action it recommends.

**They come apart.** A well-established belief that the opponent plays near-uniformly: high evidence, small margin, small edge. A thin belief after two observations suggesting strong bias: low evidence, large margin, large edge. A case where two actions both pay well but it is unclear which pays better: large edge, small margin — stake large, choose uncertainly.

**Fix:**
- Correct the claim in §3.3 and name the three quantities distinctly throughout.
- Add all three as probe targets in §9.2 (currently only "exploit margin" appears, target 4).
- Use all three as calibration axes in §9.3 rather than the single conflated one.

**Why the margin matters as a calibration variable at all** (worth stating in the document, currently implicit): raw agreement rates between model and reference are close to uninformative alone. At near-zero margin two actions are almost equally good and a "wrong" choice is not a meaningful error. The signature of a model genuinely using its belief is the *shape* — tight agreement at high margin decaying toward chance as margin approaches zero — not any single agreement number.

**Status:** accepted (Ramsey: "an important amendment").

---

## A12 — §14: the alignment scalar is a precondition, not just a parameter

**Raised at:** §2, babbling equilibria.
**Bears on:** §14 branch T.

§14 treats the alignment scalar `w` as a parameter to sweep from 0 to 1, with babbling predicted at `w = 0`.

**What this misses.** Lying is not well-defined in a babbling equilibrium. To lie is to exploit a convention of truthfulness — a false statement works only because statements are ordinarily believed. Where nothing is believed, a false message is not a lie but noise. So the partially-aligned region is not merely the interesting part of the sweep; it is the only region where the object of study exists at all.

**Fix:** state in §14 that establishing an informative equilibrium is a precondition for the lying/wrong distinction, not merely one point on a sweep. The experiment's first task under branch T is to find the region where credible transmission is sustainable; the deception work happens only there.

**Also from Crawford–Sobel, worth adding as a quantitative prediction:** alignment buys resolution. The sender can credibly convey a partition of its information whose granularity increases with alignment. So expect the number of distinguishable message classes to grow with `w` — a measurable prediction, not merely a direction.

**Status:** proposed.

---

## A13 — Variant S should allocate a stake vector, not a single stake

**Raised at:** §3.3, proper scoring rule.
**Bears on:** §3.3, §5 (heads), §6 (solver), §9.2, §9.3.

**The problem.** §3.3 hedges that the quadratic-cost stake makes the task "closer to a proper scoring rule." The hedge is doing more work than it appears.

- **Variant A** reveals only the argmax. Everything else about the belief is behaviourally invisible.
- **Variant S** (one stake on the chosen action) reveals the argmax *and* the edge, since the optimal stake is `max_a E[a] / (2λ)`. Strictly more, and genuinely graded.
- **But not the posterior.** For n=3 the predictive has 2 free numbers; S reveals one category plus one real. One degree of freedom is unresolved: nothing in the model's behaviour depends on which of the two *non-chosen* actions it considers more likely. Variant S elicits a projection of the belief, not the belief.

**Why this matters for the experiment's logic.** The A-vs-S comparison is a primary result (§3.3) intended to test whether internal representation is shaped by what behaviour demands. But if the full posterior turns out decodable under S, that is not explained by behavioural demand either — S doesn't require it. As designed, the comparison can show that richer demand yields richer representation; it cannot cleanly test the limiting claim.

**The fix.** Let the model allocate a stake to *each* action rather than one stake to a chosen action, with the quadratic cost applied across the vector: payoff = Σ_a s_a · outcome(a, b) − λ Σ_a s_a². The optimal allocation is then proportional to each action's expected outcome, so the full vector `E[·]` is behaviourally revealed. For n=3 that vector determines the predictive uniquely (the map from predictive to expected-outcome vector is invertible on the simplex). This makes the action channel a strictly proper elicitation of the entire belief.

**Cost:** three stake heads instead of one; a slightly larger action space; solver updated to emit the full optimal allocation. No loss of closed form.

**Naming:** keep the single-stake version as a named intermediate (it isolates "argmax plus edge") if the three-way comparison A / S / S-full is worth running. Otherwise S-full replaces S.

**Status:** accepted (Ramsey requested it be logged).

---

## A14 — §4: pre-generation survives a reactive opponent (correction)

**Raised at:** §4 reading.
**Bears on:** §4, §11.
**Note:** this corrects a claim made during the reading that A10 destroys pre-generation. It does not.

**The correction.** Pre-generation does not require the opponent's trajectory to be exogenous. It requires the *randomness* to be fixed. For each opponent, pre-draw a table of responses indexed by joint state and round number — what the opponent would play if it found itself in that state at that round, sampled from the appropriate row. The episode then unfolds deterministically as a function of the model's own choices: whichever state play lands in, the opponent's response is already written down. Common random numbers. Reproducibility, recorded seeds, and a genuinely finite training set all survive rung 1.5 intact.

**Drop trajectory multiplicity (`m`).** It only ever made sense at rung 1, where memorization means storing sequences. Memorization in this setting is actually *policy identification* — recognize which opponent you face from a short prefix, then apply a stored copy of its behaviour (the encode-pool-decode motif of §16). That mechanism is indifferent to whether the sequence was pre-generated or rolled out live, because what it memorizes is the policy, not the trajectory. So pool size `N` remains the lever at both rungs, and `m` should be removed rather than repaired.

**New cost to record under rung 1.5.** When the opponent reacts to the model, the training data distribution is partly determined by the model's own current policy, which changes throughout training. The data distribution is therefore non-stationary in a way it is not at rung 1, and the data-diversity theory being leaned on (§16) assumes a fixed data distribution. The memorization/generalization boundaries may move or blur.

**Status:** accepted.

---

## A15 — A10's reference ladder is defective: none of its members explore

**Raised at:** discussion of pre-computed optimal play.
**Bears on:** A10's ladder, §6, §8 Phase A, §9.1.

**The defect.** A10 proposed four references: uniform random, posterior-greedy, certainty-equivalent, and omniscient optimal. Of these, posterior-greedy and certainty-equivalent do not explore, and omniscient optimal has nothing to explore *for*. So the ladder contains no reference that behaves correctly in a game where information has value — which is precisely the property rung 1.5 introduces.

**The conceptual point that was under-stated.** In the Bayes-adaptive formulation there is one optimization, not two. The state is the belief; the optimal policy maps belief to action by backward induction over how the belief will evolve; an action landing in a poorly-known joint state has higher continuation value because the observation it produces sharpens the posterior and improves every later decision. The value of information is already inside the value function. **The explore/exploit balance is an output, not a tunable parameter.** Exact solution over a continuous 27-dimensional belief space remains intractable.

**Two principled, computable substitutes that genuinely explore:**

- **Thompson sampling.** Draw one policy from the posterior, play the best response to that draw. Explores in proportion to residual uncertainty, with no explicit exploration term anywhere. Asymptotically near-optimal. Trivially cheap.
- **Information-directed sampling** (Russo & Van Roy). For each action, compute expected immediate regret and expected information gain, and optimize the tradeoff explicitly. This is the literal formalization of "query the belief for what would be most informative."

**Revised ladder:** uniform random / posterior-greedy (belief, no planning, no exploration) / certainty-equivalent (belief and planning, no exploration) / Thompson (exploring) / information-directed (exploring, explicit VOI) / omniscient optimal (unachievable bound). The gaps between adjacent members now decompose into planning value, exploration value, and cost of ignorance separately.

**Consequence for §8 Phase A.** The supervised target must be an exploring reference. Imitating a myopic one teaches the model not to explore, which would poison the phase that is supposed to establish feasibility.

**Status:** accepted.

---

## A16 — §9.2: add a value-of-information probe target

**Raised at:** discussion of pre-computed optimal play.
**Bears on:** §9.2, §12.

If optimal play at rung 1.5 requires weighing what an action would teach, then a network that generalizes well must hold something like *expected information gain from landing in this joint state*. That is not a posterior, not a predictive, not an argmax, and not a margin — it is none of §9.2's four targets, and none of the three scalars in A11.

**Proposal:** add it as a fifth probe target, computed from the reference solver (information-directed sampling supplies it directly as a per-action quantity).

**Why it matters beyond completeness.** A count accumulator is the minimum a competent model must have and is exactly what the function-approximation objection (A5) says proves nothing. A representation of what one does not yet know, used to choose actions that reduce it, is a different kind of object and much harder to dismiss as a relabelled intermediate. If it is there, it is the stronger finding.

**Status:** proposed.

---

## A17 — The opponent family scheme (supersedes A1, extends A10a)

**Raised at:** discussion of discretization.
**Bears on:** §3.2, §4, §6, §9.2.

**The scheme.** A *family* is a set of constraints on regions of the 9×3 policy matrix — not a list of opponents. Within a family, sampling is continuous and unbounded, so infinitely many distinct opponents exist. Finiteness is at the level of families only.

Constraint axes:

- **Reactivity** — how much the three rows sharing an opponent-last-action differ as the model's own last action varies. Zero reactivity collapses to rung 1 (A10a). This is the socially meaningful latent: "does this thing respond to me, or is it indifferent to me" is the minimal form of "is there another agent here."
- **Concentration** — how peaked each row is on the simplex; governs exploitability.

Both axes apply to arbitrary *subsets* of rows independently, so high reactivity to rock and low reactivity to paper is a distinct family from its mirror. The space is therefore large by construction, and can be made larger as needed.

**Explicitly rejected:** a genuinely finite pool of individual opponents. That yields a posterior over *identity* rather than over a parameter — type recognition rather than parameter estimation — which is Gibson et al.'s *memorizing* motif by construction, and would push the model toward memorization by design.

**Required governing principle:** see A18. The family space explodes fast (three reactivity levels applied per opponent-last-action group is already 27 combinations before concentration or per-player-action asymmetry), and needs a selection criterion rather than taste.

### A17a — The four-corner lattice (Ramsey's observation)

The 9×3 space is not a line between "ignores me" and "reacts to me." It is a 2×2 lattice over *which state variables the opponent conditions on*:

| | conditions on own last action | ignores own last action |
|---|---|---|
| **conditions on player's last action** | full joint (rung 1.5) | **rung 1′** — responds only to the player |
| **ignores player's last action** | **rung 1** — does its own thing | rung 0 — i.i.d. |

Rung 1′ was previously unnamed and is worth having:

1. **It contains the natural responders.** Rung 1 yields cyclers, constant players, and frequency-biased players — opponents about themselves. Rung 1′ yields "beat whatever the player just played," the shape of most actual RPS heuristics and of tit-for-tat in the neighbouring game. An opponent recognizably *about the model* lives at this corner, and the corner is a better place to look than the continuum between corners.
2. **The two corners have complementary sufficient statistics.** At rung 1 the model needs only the opponent's history; its own is irrelevant. At rung 1′ the model needs only its own history; the opponent's is irrelevant. This gives a matched pair of tasks where the same architecture must route attention to opposite streams. Whether it learns to identify *which* stream matters — rather than always attending to both, or to whichever it learned first — is a mechanistic question with a clean signature and a known right answer. **This is a better tooling-validation case than the modular-arithmetic one (§9.4, A9), because it tests the retrieval machinery rather than the arithmetic.**
3. **It sharpens the latent.** Rather than inferring a continuous reactivity parameter, the model performs model selection among four pooling patterns, each with closed-form Dirichlet-multinomial evidence. Four hypotheses, exactly computable posterior, correct answer known.

**Caution to record with it.** At rung 1′ a model that plays deterministically drives the opponent deterministically, and the pair becomes a closed dynamical system that can fall into a short limit cycle visiting only a few of the nine states. This is the exploration problem in its most acute form: exploitation actively destroys state coverage rather than merely failing to improve it.

**Status:** accepted.

---

## A18 — Gating calculations to add to §11 build order

**Raised at:** §3.4 and the discretization discussion.
**Bears on:** §11. All three are cheap, and all three are currently absent.

1. **Family distinguishability.** For each pair of families, compute the expected divergence per round between the observation distributions they induce, giving rounds-to-separate. Any pair that cannot be told apart inside the episode budget is not a latent the model can infer — probing for it will find nothing, not because the model failed but because the information was never in the data. Merge such pairs rather than keeping them.
2. **Evidence per row.** At rung 1, 64 rounds over 3 rows gives roughly 21 observations per row, standard error near 0.1, resolving differences of about 0.2 — probably sufficient given the lopsided opponents α = 0.5 produces. At rung 1.5, 9 rows gives roughly 7 observations per row and standard error near 0.2, resolving only gross differences. **This is a genuine feasibility concern for A10** and argues for longer episodes or coarser families. It should gate the build, not surface in week three.
3. **No-leak test.** Assert explicitly that the opponent's round-*t* action is not visible at any position where the model emits its round-*t* choice. A one-position leak makes the task trivial and every curve meaningless while looking entirely normal.

**Status:** accepted.

---

## A19 — §9.5: round index conflates evidence and horizon under a reactive opponent

**Raised at:** §3.4, causal masking.
**Bears on:** §9.5.

§3.4's argument that prefix-length analysis is free — every episode contains all prefix lengths, so dose-response reads off round index in-distribution — holds cleanly for prediction and probe measurements at rung 1.

Under A10 it stops holding for anything involving planning. A model that plans behaves differently at round 60 than at round 10 with identical evidence, because the remaining horizon is shorter and the value of information falls toward zero as the episode ends. Round index therefore becomes an evidence-*and*-horizon axis, and the two must be separated before the dose-response profile means anything.

**Possible separations:** vary total episode length across evaluation runs (reintroducing the positional out-of-distribution problem §3.4 was avoiding, so only viable if trained on variable lengths); or condition the analysis on rounds-remaining as a second variable and report the two-dimensional profile.

**Status:** proposed.

---

## A20 — §5: self-action tokens become mandatory under A10

**Raised at:** §5 reading.
**Bears on:** §5, A4, §14.

§5's baseline excludes the model's own actions from the context on the grounds that they carry no information about the opponent's process, and files the SELF variant as a later ablation. A4 reclassified it as the program's extension axis.

**Under A10 it is neither optional nor merely forward-looking — it is required.** If the opponent's behaviour depends on the joint state, the model's own last action is half the index into the row about to be used, and its action *history* is what allows past observations to be attributed to rows at all. Seeing the opponent play paper tells you nothing unless you know which of the nine states you were in when it did. A model without access to its own action history cannot perform the inference.

**Consequence:** the baseline tokenization changes under A10 — vocabulary 2n+1, sequence length 2K+1, own actions interleaved. The "distractor" argument applies only at rung 1.

**Worth recording as a structural result, not just a fix.** A4 argued that the optimization making the baseline clean deletes the channel a later stage would need. A10 makes that deletion impossible rather than merely regrettable: the same move that closes the loop forces the self-model channel open. One cannot construct the minimal social task without also, unavoidably, giving the model a record of its own behaviour.

**Status:** accepted.

---

## A21 — §8: phase initialization is unspecified

**Raised at:** §8 reading.
**Bears on:** §8, §11, §12.

§8 says to run the phases in this order but never states whether Phase C initializes from Phase B's weights or from scratch. These are entirely different experiments, and "run in this order" reads naturally as a curriculum to anyone implementing it.

- **From Phase B's weights:** the belief machinery is already present before policy gradient begins. Phase C then cannot answer the question it exists to ask — whether a belief-shaped intermediate arises under payoff pressure *alone* — because it inherits one.
- **From scratch:** the phases are independent experiments run in a convenient order, and the comparison is legitimate.

**Fix:** state explicitly that Phase C initializes from scratch. The headline claim depends on it.

**But add the curriculum as a named third condition (Phase B→C).** It asks a different and genuinely valuable question: does an *installed* belief survive and get used under payoff pressure? If Phase B installs a full posterior and payoff pressure then erodes it toward the argmax — because that is all behaviour requires — that is a direct, measurable instance of representational richness decaying to behavioural demand. It is the cleanest available test of the "representation trails function" thesis in the whole design, and informative whichever way it comes out. See the orientation document, §6.7.

**Status:** accepted (both parts).

---

## A22 — The A-vs-S comparison is confounded by training signal

**Raised at:** §8 Phase C reading.
**Bears on:** §3.3, §8, §9.2, §9.3. Affects a designated *primary* result.

**The confound.** Under A13's stake vector, the optimal allocation is proportional to each action's expected outcome, which is a linear function of the predictive. So the payoff gradient under the stake variant carries information about the *whole predictive at every round*, whereas under variant A it carries only which action paid.

The two variants therefore differ in two ways at once:

1. **Richer behavioural demand** — the intended manipulation, and what §3.3 claims the comparison tests.
2. **Richer training signal** — not intended, and not controlled.

If the full posterior is decodable under S and not under A, that cannot be cleanly attributed to representation tracking behavioural demand. S may simply train better.

**Proposed disentanglements:**

- **Match on learning outcome, not training steps.** Read decodability at equal fraction-of-ceiling rather than at equal step count. Necessary but probably not sufficient, since the *route* differs even at matched endpoints.
- **Construct a rich-gradient / poor-readout control if possible** — a variant whose training signal carries predictive information but whose behaviour reveals only the argmax. If constructible, this isolates the manipulation.
- **Failing both,** state in §12 that the comparison bounds rather than identifies the effect.

**Secondary item from the same paragraph — the Phase C-aux β threshold.** "The smallest β at which belief structure still forms" is a threshold on a continuum, and its location will vary with learning rate, seeds, pool size, and everything else. It needs multiple seeds at each β and a criterion for "still forms" fixed in advance (see pre-registration, §8), or it becomes a number that tracks nuisance parameters more than the quantity it claims to measure.

**Status:** accepted.

---

## A23 — §9.2 target 2: raw counts are confounded with elapsed time

**Raised at:** §9.2, centred log-ratio discussion.
**Bears on:** §9.2, §10.3.

§9.2 specifies coordinate care for target 1 (the predictive, in centred log-ratio coordinates) and none for target 2 (the count matrix). Counts are worse behaved than probabilities.

**The confound.** Raw counts are unbounded and grow with round index — their total across the matrix is exactly the number of rounds elapsed. A probe regressing onto raw counts can therefore achieve substantial R² by reading elapsed time, which is trivially available from the positional embedding and requires the network to have learned nothing whatsoever about the opponent.

**Why the existing controls miss it.** §10.3's random-initialization control also has positional embeddings, but untrained ones, so it will not exhibit the same readable time signal. The raw-feature control (probe on accumulated one-hot history) would partly catch it, but the decomposition below is cleaner and diagnostic rather than merely protective.

**Fix — decompose the target, as A11 does for the scalars:**

1. **Normalized counts** — the posterior mean policy, one row-stochastic matrix. The informative part. Probe this in clr coordinates per row, consistent with target 1.
2. **Total evidence** — the row sums, or their total. The trivial part. Probe separately and report separately; high decodability here is expected and uninteresting.

Reporting them jointly as "the count matrix" allows the trivial component to inflate the number that will be read as evidence of belief representation.

**General principle worth stating in §9.2:** every probe target should be checked for a component that is computable from position alone. Where one exists, split it out rather than regressing against the sum.

**Status:** accepted.

---

## A24 — §9.3: the decoded-belief measurement cannot see a wrong belief

**Raised at:** §9.3 reading.
**Bears on:** §9.2, §9.3, §12. Structural, not a detail.

§9.3 lists two measurements: agreement between the model's action and the best response to the *decoded* belief, and agreement with the best response to the *true* belief.

**The problem.** The probe is fit to predict the true posterior. The decoded belief is therefore by construction an estimate of the true belief — noisy, but regularized toward truth by the fitting procedure itself. Two consequences:

1. The two measurements are not independent. They will track each other closely and the first adds little information over the second.
2. **The most interesting case is invisible.** If the model holds a *systematically wrong* belief and acts on it correctly, a probe anchored to the true posterior will not recover that wrong belief — it was trained not to. As specified, §9.3 can show the model acts consistently with the correct belief, but cannot distinguish a model that computes the right posterior and uses it from one that computes something else and behaves similarly.

**Fix — the residual test.** Examine the probe's residuals: the ways the decoded belief departs from the true one. Then ask whether the model's actions follow those departures.

- If the decoded belief is merely a noisy readout of the true belief, the residuals are noise and should not predict behaviour.
- If the decoded quantity is the network's own belief, then where it deviates from truth the model's action should deviate in the same direction.

**Why this is worth more than the measurement it repairs.** A positive result validates the *probe* rather than the model: it shows the probe is reading the network's state rather than reconstructing the reference from information available in the input. That is a direct answer to the standing objection that probes find the input rather than the computation (§10.3), and it does not depend on any control condition.

**Relation to A5.** This is arguably a fourth criterion in the belief-vs-function-approximation set — call it *residual-following* — and it shares their character: it checks a consistency relation rather than agreement with a reference, so it may transfer to regimes where no reference exists (orientation §6.6).

**Status:** accepted.

---

## A25 — §9.5: double dissociation was dropped, and the task supports two

**Raised at:** §9.5, temporal dissociation.
**Bears on:** §9.5, §9.4, A9, A17a.

**The gap.** The lesion-study critique that motivated §9.5 raised diaschisis, fibers-of-passage, degeneracy, *and* double dissociation. The first three survive in §9.5's caveat list. Double dissociation appears nowhere in the remedies. The protocol inherited three warnings and one of the two methods.

**Why temporal dissociation does not substitute.** Double dissociation exists to kill one confound: that function A is simply harder or more resource-hungry than B, so any general degradation hits A first. The remedy is symmetry — a second lesion impairing B and sparing A — which requires two components crossed with two functions. Temporal dissociation is structurally a *single* dissociation with training step as the varied factor. It addresses structurality (is this component built into or abandoned by the network) rather than specificity (is this component particular to this function). Orthogonal questions.

**Two available double dissociations:**

1. **Accumulator vs. arithmetic.** Predicting the opponent's next action and computing which action beats it are separable subcomputations with independently checkable outputs. Measure predictive accuracy and beats-mapping correctness separately; look for an ablation degrading prediction while sparing the mapping, and another doing the reverse. Same split A9 identified as the two halves of the pipeline.
2. **Rung 1 vs. rung 1′ (preferred).** A17a's matched pair has complementary sufficient statistics: one task requires attending to the opponent's history and ignoring one's own, the other the reverse. An ablation targeting self-history retrieval should impair rung 1′ and spare rung 1; one targeting opponent-history retrieval should do the opposite. **The two tasks are matched in difficulty by construction** — both are 3-row estimation problems with identical statistical structure — which removes the difficulty confound before the experiment begins rather than arguing it away afterward.

**Action:** relabel A17a as a double-dissociation design, not merely a tooling-validation case.

**Status:** accepted.

---

## A26 — §9.5: temporal dissociation needs headroom normalization, and scoping

**Raised at:** §9.5, temporal dissociation.
**Bears on:** §9.5, §11.

**The confound.** As training proceeds the network improves, so ablating *any* load-bearing component costs more in absolute terms simply because there is more performance to destroy. A growing ablation effect is therefore confounded with a growing baseline, and the growth-vs-decay signature the test relies on could be produced by a component with nothing to do with belief. **Normalize effect size by available headroom** (distance from the current model's return to the floor, or to the reference at that checkpoint) before the trajectory shape is interpreted.

**Scoping decision — keep, but narrow.** The case for keeping it: it is the only bridge between the correlational decodability timeline and the causal claim. The headline result is a *timing* claim; decodability is measured across training while every other ablation is measured at a point. Without a causal measurement on the same time axis, one is asserting that a correlational time series and a point-estimate causal result describe the same object. Relearning time does not substitute (it asks about commitment, at one moment); double dissociation does not substitute (specificity, not structurality).

**Cost correction.** The expensive component — probe refitting per checkpoint — is already paid for by §9.2, which fits probes at every checkpoint regardless. The marginal cost of temporal dissociation is the ablations alone: ~8 heads plus MLP blocks × checkpoints × a few hundred eval episodes. Minutes at this model size.

**Narrowing:**

- Run only on components implicated in the timing claim, not as a broad sweep.
- **Head-level ablations only.** Head indices are stable across checkpoints by construction, so the correspondence problem is handled for free.
- **Drop direction-level temporal ablation outright.** The direction found at step 10k and the one found at step 50k come from separate fits with no principled reason to call them the same component. The resulting trajectory is uninterpretable rather than merely noisy.
- Coarse logarithmic checkpointing to locate the transition, then fine sampling only in the window around it. Two passes.

**Recorded case for cutting, should the decision be revisited.** Under A6's reframing the deliverable is validated criteria, and temporal dissociation is not among the A5 criteria; a minimal first pass could defer it and lose nothing that transfers. What would be lost is the protocol's answer to the first of its three motivating problems (the frozen-checkpoint critique), leaving the document addressing two of three while citing all three as motivation. A program cost, not a measurement cost.

**Status:** accepted (keep, scoped as above).

---

## A27 — §9.5: four unspecified decisions in the relearning-time test

**Raised at:** §9.5 reading.
**Bears on:** §9.5, §11.

The test — ablate, resume training, measure steps to recovery against a matched control — leaves four decisions open, each of which changes what is being measured.

1. **The matching variable.** §9.5 says a control ablation "of similar magnitude." Magnitude in what sense? Matching on weight norm does not match functional damage: two ablations of equal norm can cost wildly different performance. **Match on immediate performance drop instead** — perturb the control until it produces the same initial degradation, then compare recovery from equal depths. Otherwise the comparison is between climbs from two different starting points.

2. **Perturbation vs. constraint.** "Ablate and resume" is ambiguous between two different experiments:
   - *Zero the weights and resume* — gradient descent may simply refill them. This measures how fast the optimizer restores a deleted structure.
   - *Mask the component throughout resumed training* — the network cannot restore it and must route around. This measures whether an alternative route exists and what it costs to build.
   
   Both are informative; they answer different questions; **the masked version is the one that speaks to structural centrality** and to the degeneracy question. Specify which, or run both.

3. **Optimizer state at resume.** Preserved Adam moments and a fresh optimizer give substantially different recovery curves. Neither is obviously correct. Fix it and state it.

4. **Recovery of what.** A network can recover behaviour by rebuilding the same structure or by building a different one, and recovery time alone cannot distinguish these. **Re-examine the recovered network with the same circuit-identification machinery** and report whether the restored circuit matches the ablated one. This is the local counterpart of the cross-seed comparison.

**Framing note.** Relearning time, cross-seed comparison, and degeneracy are three views of one quantity: the size of the equivalence class of implementations the task admits. Cross-seed samples it globally; relearning time probes it locally (fast relearning implies a large class in the neighbourhood); degeneracy is the name for the class being larger than one. Reporting them together, as estimates of a single quantity, is stronger than reporting them as three separate tests.

**Status:** accepted.

---

## A28 — §10.1: the unexploitable-opponent null controls usage, not decodability

**Raised at:** §10 reading.
**Bears on:** §10.1, §9.2, §9.3.

§10.1 specifies an opponent with all rows uniform and claims that "no belief is possible" there, so any apparent belief decodability is spurious by construction, calibrating the false-positive rate of the probe pipeline.

**The claim is wrong.** The opponent's *true* policy is uniform; the *posterior* is not. With finite evidence the observed counts fluctuate, so the predictive computed from them wanders around uniform rather than sitting on it — after 20 observations in a row one might have 7, 6, 7, and the correct predictive is not (1/3, 1/3, 1/3). A model performing the correct Bayesian computation tracks those fluctuations, and a probe would recover them legitimately. **Decodability in this condition can be genuinely nonzero and entirely correct.**

**What the condition actually removes is actionability, not belief.** Margin and edge both hover near zero and acting on the belief has no expected value.

**Correct assignment:**

- **It is a clean control for §9.3 (belief usage).** A model that appears to track its belief into action here is doing something spurious, because there is nothing to act on.
- **It is not a control for §9.2 (decodability),** which is what the document claims it for.

**The gap this leaves.** A proper decodability null requires the *target* to be uninformative rather than the task to be unexploitable — probing for the posterior computed from a different episode's history. That is essentially the shuffled-target control already in §10.3. So the battery has the right instrument in the wrong slot and believes it has coverage where it does not.

**Fix:** reassign §10.1 to the usage column, state the shuffled-target control in §10.3 as the decodability null, and consider a stronger version — a mismatched-history control, where the probe target is the posterior from a different episode of the *same* length, which preserves the target's marginal distribution while destroying its correspondence to this episode's activations.

**Note on §10.2 (constant opponent).** Sound as stated. Worth adding that it sits at near-maximal margin and edge throughout, so it is the high-signal end of every calibration curve in §9.3, not only a floor test for the machinery.

**Status:** accepted.

---

## A29 — §10.4: five seeds is a floor for means and inadequate for the degeneracy claim

**Raised at:** §10.4 reading.
**Bears on:** §10.4, §9.5 (cross-seed comparison), §8 (pre-registration).

§10.4 specifies a minimum of five seeds per condition. That is defensible for comparing means — whether condition A reaches higher decodability than condition B. It is inadequate for the cross-seed circuit comparison, which is not a claim about a mean but about a **distribution**: the size of the equivalence class of implementations the task admits.

**Power calculation.** To detect a minority solution occurring at rate *p* with 95% confidence requires roughly n ≈ log(0.05) / log(1 − p) seeds. For a minority mode at 10% — the rough scale of a Clock/Pizza-style bimodality — that is about 28 seeds. Five seeds have a 59% chance of missing such a mode entirely, and would report clean convergence.

At 2 layers and d_model 128 the cost argument that justifies small seed counts at scale does not apply. **Run 30 for the cross-seed comparison specifically;** keep 5 as the floor for ordinary mean comparisons.

**Separate the sources of variation.** A "seed" currently varies initialization, data order, and episode draws together. For the degeneracy question these should be separated: fix initialization and vary data order, then fix data order and vary initialization. Divergence attributable to initialization and divergence attributable to training order are different findings, and the factorial design is cheap at this scale. This also pairs with A21's curriculum condition, which is a third source of path dependence.

**The weakest link — no criterion for circuit identity.** The protocol nowhere states what would count as "the same circuit" across seeds, which leaves the cross-seed comparison to be settled by inspection. This must be pre-registered along with everything else in §8. Candidate metrics, to be chosen in advance rather than after seeing results:

- representational similarity between models at matched layers (e.g. CKA);
- alignment of probe directions after optimal permutation of heads;
- functional equivalence under transplanting a head from one model into another.

Without a fixed criterion the degeneracy measurement is not a measurement.

**Status:** proposed.

---

## A30 — §11: missing steps, and a note that the section needs rewriting

**Raised at:** §11 reading.
**Bears on:** §11. Interacts with A10, A15, A17, A18, A21, A22, A26, A29.

**Framing.** §11 sequences what the earlier sections specify, so nearly every accepted amendment changes it. It should be rewritten wholesale at revision time rather than patched. The two existing gates — solver verification before anything else, diversity sweep before the main runs — are correctly placed and should survive.

**Four things missing entirely:**

1. **A step 0 of feasibility calculations.** A18's gating calculations (family distinguishability; evidence per row) determine the *opponent design itself* and must run before the game engine is built. The evidence-per-row number in particular could send the design back to longer episodes or coarser families before a line of code is written — which is the point of having it early. Currently it has nowhere to live.
2. **The no-leak assertion belongs in step 3.** A18's third item — that the opponent's round-*t* action is not visible at any position where the model emits its round-*t* choice — is a round-trip test, and step 3 is where round-trip tests are.
3. **Pre-registration as a produced artifact, not an instruction.** §8 says to fix the transition definition, the primary comparison statistic, and the "still forms" criterion for the β sweep in advance. Nothing in the build order produces a document containing them. Add a step whose output is a written, timestamped pre-registration dated before the first Phase B run.
4. **The circuit-identity metric (A29) must be chosen before step 12.** Choosing it while looking at the circuits is exactly the flexibility pre-registration exists to remove. It belongs in the pre-registration artifact above.

**Two steps that have grown and are now under-budgeted:**

- **Step 1 (engine and sampler).** With rungs 0, 1, 1′, and 1.5, and families defined as constraint sets rather than a single Dirichlet draw, this is substantially more work than the document assumes.
- **Step 2 (reference solver).** No longer one object. The ladder is posterior-greedy, certainty-equivalent (requiring finite-horizon backward induction over joint states), Thompson sampling, information-directed sampling, and the omniscient solve — four or five implementations, each needing its own verification. **This is probably the single largest piece of work in the project and the document budgets it as a preliminary.**

**Status:** accepted.

---

## A31 — §12: add a methodological-limits category, and restate the "can" list

**Raised at:** §12 reading.
**Bears on:** §12. Interacts with A5, A6, A9, A22, A24, A29, and orientation §6.6.

**The "can" list needs restating.** It still describes finding a structure, timing it, and testing its causal necessity. A6 argues the deliverable is *validated criteria* rather than a found circuit; A5 and A24 supply the criteria; A22 downgrades the A-vs-S comparison from identifying to bounding. None of that is written here yet.

**The structural gap.** Every item on the current "cannot" list is a *scope* limit — phenomenology, deception, trust, second-order belief, transfer to larger models — things the experiment does not address because it was not built to. There is no category for *methodological* limits: things it cannot establish even when everything works exactly as designed. Three belong there.

1. **It cannot establish that the found circuit is *the* implementation rather than one of several.** At best it bounds the size of the equivalence class, and only at whichever level of description the circuit-identity metric operates on (A29). Since that size is a joint property of the network and the analytic vocabulary, the result is indexed to a choice that is not itself empirical.
2. **It cannot establish that probe validity transfers anywhere.** This is orientation §6.6 mirrored into the protocol: whatever is validated is validated at this coordinate, and the single-axis transfer protocol measures the degradation rather than preventing it.
3. **It cannot distinguish a network computing the posterior from one computing a sufficient proxy that coincides with the posterior on everything the training distribution produces.** A5's off-manifold criterion is the attempt to reach that distinction; if it comes back negative, the distinction stays open, because on-distribution agreement is all anyone ever observes.

**Note on (3).** This is the sharpest form of the project's motivating epistemological prior expressed inside the protocol's own accounting. Stating it as a limit rather than leaving it implicit is what makes the document honest about what a positive result would mean.

**Status:** accepted.

---

## A32 — §13: give the terminology section a positive function

**Raised at:** §13 reading.
**Bears on:** §13, and consolidates vocabulary content currently stranded in A11, A23, and the §6 reading.

**1. The "circuit" entry is half an answer.** It says the design's response to the term's circularity is to specify the target independently of the search that finds it — the exact posterior is known before any model is trained. That defeats *circularity*: the circuit can no longer be defined as whatever the ablation flagged. It does nothing about *multiplicity*. Even with the target fixed in advance, several structures may compute it, and "the circuit" remains a definite description without a unique referent. State both; the second is what the degeneracy measurements (A25, A27, A29) are actually about.

**2. The section is currently entirely prohibitive** — a list of words not to use yet. It should also be where the document's own vocabulary is pinned down, since several amendments are definitional fixes that currently sit in measurement sections and will not govern usage elsewhere from there. Move or mirror into §13:

- **The three scalars (A11).** *Edge* = `max_a E[a]`, the value available. *Decision margin* = `max_a E[a] − second-max_a E[a]`, how decisively the belief picks an action. *Evidence* = the row sum of posterior concentrations, how well-established the belief is. The document currently calls all three "margin."
- **Counts (A23).** *Raw counts* (confounded with elapsed time) vs *normalized counts* (the posterior mean policy).
- **The three belief objects.** *Posterior* (unnormalized concentrations over all rows; row sums encode confidence), *posterior mean policy* (a point estimate; the row-stochastic matrix), *posterior predictive* (the single row indexed by the opponent's most recent action). The document sometimes calls all three "belief."

**3. Add to the prohibition list: unqualified use of "circuit," "degeneracy," or "universality" without naming a level of description.** Equivalence-class size is a joint property of the network and the analytic vocabulary, so any such claim that does not name its level is underspecified. Two circuit-level solutions collapsing to one manifold-level solution is not a contradiction; reporting either without its level is an error.

**Status:** accepted.

---

## A33 — §14: two additions to branch T

**Raised at:** §14 reading.
**Bears on:** §14, §11, A10, A24.

**1. Under A10 the informational asymmetry becomes structural rather than stipulated.** §14 specifies that the reporter observes rounds the actor does not. At rung 1 that is simply "more rounds." At rung 1.5 the actor's own choices determine which joint states are visited, so two agents with different observation histories have coverage of *different regions of the opponent's table*. The reporter can know something about a state the actor has never entered and cannot reach without changing its own behaviour.

This is a materially better asymmetry: the report concerns something the recipient could not have obtained by waiting, so the testimony has content that survives the receiver's own accumulating evidence. At rung 1, by contrast, any report is eventually redundant — the actor will see the same thing given enough rounds — which weakens the channel's value and therefore the incentive structure around it.

**2. Branch T depends on A24 and the document does not say so.** The branch's central claim is that lying can be defined as divergence between a report and the reporter's *causally validated* internal posterior. That requires the reporter's belief to be measurable, which requires the probe machinery to be trustworthy on the reporter specifically. A24's residual test is the instrument that establishes this, since it distinguishes a probe reading the network's own state from one reconstructing the reference from information available in the input.

**A24 is therefore not only a repair to §9.3 — it is a precondition for branch T's central claim.** State it as a dependency in the build path.

**Status:** accepted.

---

## A34 — §15: cut to a pointer

**Raised at:** §15 reading.
**Bears on:** §15, orientation §6.4.

§15's three items — the tie-chain embedding, the payoff-sum deformation, and the argument that mixed motive should enter between agents first — were consolidated into orientation §6.4, which also resolves the open question §15 leaves standing: as literally specified the tie-chain yields a **stag hunt**, not a prisoner's dilemma, because tie-chain outcomes are symmetric by construction and the off-diagonal temptation and sucker cells are unreachable. For a program targeting trust that may be the better game (Skyrms).

This is now duplicated material, and duplicated material drifts.

**Fix:** cut §15 to a pointer at the orientation document's motive axis, retaining only what is protocol-specific rather than option-space-general — namely that **both in-game implementations are inert against fixed non-adaptive opponents**, since nothing reciprocates and no cooperation is possible, and that the tie-chain additionally destroys the closed-form greedy optimum by making the decision non-myopic. Those are facts about this baseline; the rest belongs upstream.

**Status:** accepted.

---

## A35 — §16: four additions to prior art

**Raised at:** §16 reading.
**Bears on:** §16, §9.4, A9.

The two in-context Markov papers remain the load-bearing citations. Four should join them:

1. **Zhong, Liu, Tegmark and Andreas, "The Clock and the Pizza: Two Stories in Mechanistic Explanation of Neural Networks" (NeurIPS 2023)** — plus the more recent work disputing it, which argues that on re-analysis these networks converge to the same algorithmic and geometric solution across architectures, seeds and hyperparameters, and that universality may reside in the structure of the learned manifolds. This pair is now load-bearing rather than contextual: it is the evidence that the modular-arithmetic known-answer case is **contested at exactly the level §9.4 operates on** (reinforcing A9), and it is the field's clearest instance of equivalence-class size being level-relative (A32 item 3). Note also that both Clock and Pizza are frequency-based — the documented multiplicity is *within* a family, not across families, and which appears is determined by an architectural detail (uniform vs. learnable attention) that forms no part of the functional specification.
2. **Russo and Van Roy on information-directed sampling**, and Thompson sampling generally — A15 makes both reference players rather than background reading.
3. **Aitchison on compositional data analysis** — the source of the centred log-ratio machinery, which currently appears in §9.2 with no citation.
4. **Chughtai, Chan and Nanda, "A Toy Model of Universality"** — group composition tasks, relevant to the universality question §9.4 leans on.

**Status:** accepted.

---

## A36 — §17: the open questions are mostly closed; replace them

**Raised at:** §17 reading.
**Bears on:** §17.

**Closed by the reading:**

- *Which reading of the tie-chain mechanism?* Resolved: as literally specified it is a **stag hunt**, not a prisoner's dilemma. The live question is now which game is wanted, and a program targeting trust argues for the stag hunt (A34, orientation §6.4).
- *Branch T or branch S?* Settled in T's favour, both by Ramsey's confirmation and by the ordering constraint in orientation §6.5 (motive must move before neurality; self-play in zero-sum converges to the uninteresting equilibrium).
- *Counting, row-gathering, or their composition?* Has an instrument now: A17a's matched pair of rung 1 against rung 1′, whose complementary sufficient statistics separate the two.
- *Does variant S belong in the baseline?* Survives only in mutated form — see (3) below.

**Four questions to replace them,** all generated by the reading and none currently recorded as questions rather than buried inside amendments:

1. **Which circuit-identity metric,** chosen in advance? Without one the degeneracy measurement is not a measurement (A29).
2. **Does the evidence-per-row budget survive at rung 1.5,** or must episodes grow? Roughly 7 observations per row against 21 at rung 1. A gating calculation whose answer changes the design before anything is built (A18).
3. **Can a rich-gradient, poor-readout control be constructed** to disentangle A22's confound? If not, a designated primary result becomes a bound rather than a finding. Also: is the three-way A / S / S-full comparison worth running (A13)?
4. **Which family set survives the distinguishability gate** (A18)? This determines what the opponent pool actually is.

**Status:** accepted.
