# Amendments — Reconciled Register

**Date:** 2026-09-22
**Supersedes:** `rps-belief-circuits-amendments-register-2026-09-19.md` (A1–A36), retained as the working history
**Method:** every original amendment was read against every other. Contradictions resolved, duplicates merged, statuses made consistent, and the set partitioned by which experiment it belongs to.

Items are renumbered R-series. Each records which originals it absorbs so the history stays traceable.

---

## 0. Reconciliation log

**The structural decision.** A6 and A7 argue the deliverable is substrate-independent *criteria* for distinguishing belief from function approximation, and that the protocol should stay minimal because criteria transfer and calibrations do not. A10 and its dependents expand the experiment substantially: a rung that costs the exact Bayes ceiling, a reference ladder that becomes the largest single piece of work in the project, a family scheme with its own gating calculations, mandatory tokenization changes, a broken dose-response axis, and a feasibility question that could force longer episodes.

None of that expansion is needed to validate the criteria. All four can be established against an opponent that ignores the model, where ground truth is exact and cheap.

**Therefore A10 is not an amendment to this experiment. It specifies a second one** — the first move along the loop-closure axis of orientation §6.1. The register is partitioned accordingly: Part 1 is rev. 3 of the current protocol; Part 2 is the second experiment.

**Build general, run narrow.** Because rung 1 is the zero-reactivity subspace of the 9×3 joint-state family (the nesting property, R20), the engine, sampler, tokenizer and solver can be built once for the general case while Experiment 1 draws only opponents that ignore the model. This preserves the exact ceiling and exact greedy optimality for Experiment 1, and Experiment 2 widens the pool rather than rebuilding. The split costs no duplicated engineering.

**Direct contradictions resolved:**

| Conflict | Resolution |
|---|---|
| A10's 4-member reference ladder vs A15's 6-member replacement, both approved | A10's ladder struck; A15's stands (R24) |
| A4 (keep self-tokens out) vs A20 (self-tokens mandatory) | Both true at different rungs. A4 survives only as the rationale for exclusion at rung 1, folded into R25 |
| A11 (optimal stake tracks the edge) vs A13 (stake vector tracks the whole expected-outcome vector) | A11's vocabulary survives whole (R8); A11's §3.3 correction is conditional on retaining single-stake S (R2) |
| A10a and A17a — overlapping reactivity material written a day apart | Merged into R20, four-corner lattice as frame, A10a's consequences as content |
| A1 declared superseded twice, by A10a and by A17, while still marked "deferred" | A1 superseded by R21 (family scheme). Closed. |

**Duplications merged:** A18's evidence-per-row into R27; A30's §11 rewrite absorbing A18's items 2–3 into R17; A6 and A31 into R16; A28's mismatched-history control with §10.3's shuffled-target into R14.

**Dependency inversions corrected.** A5, A16 and A29 were marked "proposed" while amendments depending on them were "accepted." All are now decided on their merits (R15, R31, R12 respectively).

**Two items decided that had been left open.** A24's residual test is promoted from "arguably a fourth criterion" to a full member of the criteria set (R15), since A33 already treats it as a precondition for branch T, which is a stronger claim than arguable. A3's rationalizability check is included (R11): it is cheap and it is the only measurement that distinguishes incoherence from error.

---

# PART 1 — Experiment 1 (protocol rev. 3)

Opponent ignores the model. Exact ceiling preserved. Deliverable: validated criteria.

## Outright errors in the current document

**R1 — §1 reason 2: sufficient statistic omits the state index.** *(absorbs A2)*
The count matrix is sufficient for inferring the policy but not for prediction, which requires knowing which row to read. State the statistic as the count matrix **plus a current-state index** (9 numbers plus a 3-way index at n=3), and introduce the predictive as its projection.

**R2 — §3.3: the optimal stake tracks the edge, not the margin.** *(absorbs A11 part 1)*
§6's formula sets the optimal stake proportional to `max_a E[a]`; §3.3 calls this the exploit margin, which §6 defines as `max_a E[a] − second-max_a E[a]`. Different quantities that move independently. *Conditional:* this correction applies to single-stake variant S. Under the stake vector (R3) the governing quantity is the whole expected-outcome vector and the sentence should be rewritten rather than repaired.

**R3 — §3.3: variant S should allocate a stake vector.** *(absorbs A13)*
Single-stake S reveals argmax and edge — one category plus one real — leaving one degree of freedom of the predictive behaviourally invisible. Allocating a stake to each action, with quadratic cost across the vector, makes the optimal allocation proportional to each action's expected outcome, which for n=3 determines the predictive uniquely. Strictly proper elicitation of the whole belief. Keep single-stake S as a named intermediate so the three-way comparison A / S / S-full isolates argmax, argmax-plus-edge, and full posterior.

**R4 — §8: state that Phase C initializes from scratch.** *(absorbs A21 part 1)*
"Run in this order" reads as a curriculum. If Phase C inherits Phase B's weights it cannot answer whether belief arises under payoff pressure alone, because it inherits one.

**R5 — §8: specify exploration control in Phase C.** *(absorbs A8)*
REINFORCE with a baseline and nothing else. A policy that collapses onto a deterministic choice stops receiving information about the other actions and can sit there permanently. Specify entropy regularization or temperature, with schedule, as a pre-registered hyperparameter. Applies to the stake heads as well.

**R6 — §9.2: raw counts are confounded with elapsed time.** *(absorbs A23)*
Their total across the matrix is exactly the number of rounds elapsed, so a probe can score well by reading the positional embedding. Split the target: **normalized counts** (the posterior mean policy — the informative part, probed per row in clr coordinates) and **total evidence** (the trivial part, probed and reported separately). General principle for §9.2: check every probe target for a component computable from position alone, and split rather than sum.

**R7 — §10.1: the unexploitable-opponent null controls usage, not decodability.** *(absorbs A28 part 1)*
With all rows uniform the *true* policy is uniform but the *posterior* is not — counts fluctuate and the correct predictive wanders. A model doing the correct computation tracks that, and a probe recovers it legitimately. What the condition removes is actionability, not belief. Reassign it to §9.3 (usage), where it is a clean null: a model appearing to track belief into action here is doing something spurious.

## Vocabulary — canonical home is §13

**R8 — Three scalars, currently all called "margin."** *(absorbs A11 part 2)*
*Edge* = `max_a E[a]`, the value available; governs the optimal stake. *Decision margin* = `max_a E[a] − second-max_a E[a]`; governs whether a model–reference disagreement is meaningful. *Evidence* = the row sum of posterior concentrations; how well-established the belief is. They come apart: a settled belief that the opponent is near-uniform has high evidence, small margin, small edge.

**R9 — Three belief objects, currently all called "belief."** *(absorbs A32 part 2)*
*Posterior* (unnormalized concentrations over all rows; row sums encode confidence) → *posterior mean policy* (point estimate; row-stochastic matrix) → *posterior predictive* (the single row indexed by the opponent's last action). Each step down discards something specific: the first discards confidence, the second discards knowledge of situations not currently arising.

**R10 — §13 gains a positive function and one prohibition.** *(absorbs A32 parts 1 and 3)*
The "circuit" entry answers circularity — the target is fixed before any model is trained, so the circuit cannot be defined as whatever the ablation flagged — but says nothing about *multiplicity*: several structures may compute a target fixed in advance. State both. Add to the prohibition list: no unqualified use of **circuit**, **degeneracy** or **universality** without naming a level of description, since equivalence-class size is a joint property of the network and the analytic vocabulary.

## Measurement

**R11 — §9.3: add an internal rationalizability check.** *(absorbs A3; decided for inclusion)*
§9.3 measures agreement with the decoded belief and with the true belief. Both are accuracy measures; neither asks whether the action sequence is coherent at all. Add: does the observed sequence admit *some* consistent belief trajectory, independent of whether it is the right one? This separates "the model is wrong" from "the model is not doing the kind of thing that admits of being right or wrong." Cheap, and nothing else in the battery measures it.

**R12 — §9.3: the residual test.** *(absorbs A24; promoted to a criterion, see R15)*
The probe is fit to predict the true posterior, so the decoded belief is regularized toward truth and a *systematically wrong* belief is invisible by construction. Fix: examine the probe's residuals — the ways the decoded belief departs from the true one — and ask whether the model's actions follow those departures. Noise should not predict behaviour; a genuine internal state should. A positive result validates the **probe** rather than the model, and does so without depending on any control condition.

**R13 — §9.5: dissociation.** *(absorbs A25, A26)*
Double dissociation was raised in the lesion critique that motivated §9.5 and did not survive into the remedies; three warnings were inherited and one of two methods. Temporal dissociation does not substitute — it addresses structurality, not specificity.

*Available in Experiment 1:* the accumulator-versus-arithmetic dissociation. Predicting the opponent's next action and computing which action beats it have independently checkable outputs; look for an ablation degrading prediction while sparing the mapping, and another doing the reverse. (The stronger instrument, the rung 1 / rung 1′ matched pair, requires the reactive family and moves to Experiment 2 — see R29.)

*Temporal dissociation, kept but scoped.* Normalize effect size by available headroom first: as the network improves, ablating any load-bearing component costs more in absolute terms, so growth is confounded with a rising baseline. Head-level ablations only, since head indices are stable across checkpoints by construction. **Drop direction-level temporal ablation** — separate fits at different steps give no principled reason to call the result the same component. Coarse logarithmic checkpointing to locate the transition, then fine sampling in that window only. Marginal cost is the ablations alone; probe refitting is already paid for by §9.2.

**R14 — §9.5 and §10.3: relearning time, and the decodability null.** *(absorbs A27, A28 part 2, and the selectivity discussion)*

*Relearning time* needs four decisions the document leaves open. Match the control on **immediate performance drop**, not weight norm — equal norms do not mean equal damage. Distinguish **perturbation** (zero and resume; measures how fast the optimizer restores a deleted structure) from **constraint** (mask throughout resumed training; measures whether an alternative route exists and what it costs) — the masked version is the one that speaks to structural centrality. Fix and state the **optimizer state** at resume. And **re-examine the recovered network** with the circuit-identification machinery, since recovery time alone cannot distinguish rebuilding the same structure from building a different one.

*The decodability null.* §10.1 is not it (R7). The correct control permutes probe targets **between episodes at matched round index**, which preserves the target's temporal structure and marginal distribution while destroying its correspondence to this episode's activations. A naive shuffle across all positions is too easy to fail: the real target grows monotonically with round index, so the probe would beat the control partly for the wrong reason, overstating selectivity. Specify this once and use it for both the decodability null and the selectivity baseline.

**R15 — New section: belief versus function approximation. Four criteria.** *(absorbs A5, A24; decided)*
As specified, nothing in the protocol distinguishes belief from function approximation: the task is in-context estimation of a transition matrix, transformers are known to solve it, and every probe target is a deterministic function of the token sequence. Calling the intermediate activations "belief" is otherwise a relabelling — the same essentialism the MINP critique charges.

1. **Multi-consumer structure.** One internal state required to serve several distinct decision problems. Does one shared representation serve them, or do task-specific features form independently?
2. **Off-manifold coherence.** Edit the state to a posterior the model has never had reason to hold and ask whether downstream behaviour follows it. A memorized map has no commitments off its data manifold.
3. **Path independence.** The same count matrix is reachable by many orderings. Convergent representation means a state; retained ordering means a trace.
4. **Residual-following** (R12). Where the decoded belief departs from truth, behaviour departs with it.

None reads a belief out of the network; each checks whether the interior is *consistent* under some transformation. That is what makes them substrate-independent where a fitted probe direction is not, and it is the program's own thesis appearing inside the method rather than as a conclusion about it.

**R16 — §12 restated.** *(absorbs A6, A31)*
*The deliverable.* Every property making this substrate gradeable makes it non-social; the referential circularity of social belief is what the tractability excludes. So the bootstrap fails if the claim is "find the belief circuit, then add an agent" (the circuit here is a bigram estimator; nothing transfers), and holds if the claim is "validate substrate-independent criteria against a case where the right answer is independently known." Restate §12 accordingly: this is a **calibration rig for belief criteria**, not rung one of a belief ladder. Same code, different claimed deliverable.

*Add a methodological-limits category,* distinct from the existing scope limits — things the experiment cannot establish even when everything works:
- It cannot establish that a found circuit is *the* implementation rather than one of several; at best it bounds the equivalence class, at whichever level the identity metric operates on.
- It cannot establish that probe validity transfers anywhere (orientation §6.6 mirrored here).
- It cannot distinguish a network computing the posterior from one computing a sufficient proxy that agrees on-distribution. Criterion 2 is the attempt; if it fails, the distinction stays open, because on-distribution agreement is all anyone observes.

*Also:* the A-vs-S comparison bounds rather than identifies its effect (R18).

**R17 — §11 rewritten, not patched.** *(absorbs A30, A18 items 2–3)*
The existing gates — solver verification first, diversity sweep before the main runs — are correctly placed and survive. Four things are missing:
- **A step 0 of feasibility calculations**, since they determine the opponent design itself and could force a redesign before any code is written.
- **The no-leak assertion** in step 3's round-trip tests: the opponent's round-*t* action must not be visible where the model emits its round-*t* choice. A one-position leak makes the task trivial while every curve still looks normal.
- **Pre-registration as a produced artifact** — a written, timestamped document fixing the transition definition, the primary comparison statistic, and the "still forms" criterion for the β sweep, dated before the first Phase B run.
- **The circuit-identity metric chosen in advance** (R31), inside that artifact.

**R18 — The A-vs-S comparison is confounded by training signal.** *(absorbs A22)*
Under the stake vector, optimal allocation is proportional to expected outcomes, which are a linear function of the predictive — so the payoff gradient carries information about the whole predictive at every round, where variant A's carries only which action paid. The variants differ in **behavioural demand** (intended) and in **training signal** (not controlled). If the posterior is decodable under S and not A, S may simply train better.

Mitigations: read decodability at **equal fraction-of-ceiling** rather than equal step count; construct a rich-gradient/poor-readout control if one can be built (open, see Part 4); failing both, state in §12 that the comparison bounds rather than identifies.

*Secondary:* the Phase C-aux β threshold needs multiple seeds per β and a criterion for "still forms" fixed in advance, or it tracks nuisance parameters more than the quantity it names.

**R19 — Phase B→C as a named third condition.** *(absorbs A21 part 2)*
Distinct from R4. Training prediction first and *then* applying payoff pressure asks whether an installed belief survives and is used. If a full posterior is installed and payoff pressure erodes it toward the argmax, that is a direct measurement of representational richness decaying to behavioural demand — the cleanest test of "representation trails function" in the design, informative either way. Program framing in orientation §6.7.

**R12b — §10.4: replication.** *(absorbs A29)*
Five seeds is a floor for comparing means and inadequate for the cross-seed claim, which concerns a *distribution*. Detecting a minority solution at 10% with 95% confidence needs ≈28 seeds; five would miss it three times in five and report clean convergence. **Run 30 for the cross-seed comparison**; keep 5 elsewhere. Separate the sources of variation — fix initialization and vary data order, then the reverse. And fix the circuit-identity metric in advance (R31).

## Housekeeping

**R30 — §14, §15, §16, §17.** *(absorbs A12, A33 part 2, A34, A35, A36)*
- §14: state that an informative equilibrium is a **precondition** for the lying/wrong distinction, not one point on the alignment sweep — where nothing is believed, a false message is noise, not a lie. Add the Crawford–Sobel prediction that alignment buys resolution, so the number of distinguishable message classes should grow with `w`. And record that branch T's central claim **depends on R12**, since "lying" is defined against a causally validated posterior and the residual test is what establishes the probe is reading the network rather than reconstructing the reference.
- §15: cut to a pointer at orientation §6.4, retaining only the protocol-specific facts — that both in-game implementations of mixed motive are inert against fixed opponents, and that the tie-chain additionally destroys the closed-form greedy optimum. (Resolved there: as literally specified the tie-chain yields a **stag hunt**, not a prisoner's dilemma.)
- §16: add Zhong et al. on the Clock and the Pizza *and* the work disputing it (the known-answer case is contested at exactly the level §9.4 operates on); Russo and Van Roy on information-directed sampling and Thompson sampling; Aitchison on compositional data, currently uncited despite §9.2 using it; Chughtai, Chan and Nanda on universality.
- §17: replace the closed questions with the four live ones — see Part 4.

**R31 — The circuit-identity metric.** *(from A29; elevated because several claims are unmeasurable without it)*
Nothing in the protocol states what would count as "the same circuit" across seeds, which leaves the degeneracy measurement to inspection. Choose one in advance, in the pre-registration artifact: representational similarity at matched layers (e.g. CKA), alignment of probe directions after optimal permutation of heads, or functional equivalence under transplanting a head between models. Without a fixed criterion the measurement is not a measurement.

**R32 — §9.4: the known-answer case covers the wrong half.** *(absorbs A9)*
The modular-arithmetic answer concerns the *arithmetic*; the belief structure is an *accumulator*. Tooling that recovers a rotational representation is not thereby validated for recovering an accumulator. Cheap fix using material already present: validate additionally against §16's reported motifs for in-context Markov estimation — the statistical induction head and the task recognition head — so both halves have a known answer. Note also that the modular-arithmetic answer is itself contested (R30), which weakens it further. The stronger instrument lives in Experiment 2 (R29).

---

# PART 2 — Experiment 2 (reactive opponent)

Loop closed: the model's action becomes an input to the process generating its observations. This is the first move along orientation §6.1's loop-closure axis and the minimal social task.

**R20 — The 9×3 joint-state opponent, and the four-corner lattice.** *(absorbs A10, A10a, A17a)*
The opponent conditions on the *pair* of last actions rather than its own alone. Still fixed, stationary, non-learning, drawn once per episode; it does not model the model, it reacts to it. §3.2's ladder previously ran exogenous → adaptive and omitted this middle.

The space is a 2×2 lattice over which state variables the opponent conditions on: both (rung 1.5), its own only (rung 1), the player's only (**rung 1′**), neither (rung 0). Three consequences:
- **Rung 1′ contains the natural responders** — "beat what the player just played" — where rung 1 contains only opponents about themselves.
- **Rungs 1 and 1′ have complementary sufficient statistics.** One needs the opponent's history and not one's own; the other the reverse. Matched in difficulty by construction.
- **The reactivity latent is exact.** Model selection among four pooling patterns, each with closed-form Dirichlet-multinomial evidence.

*What closes with the loop:* exploration returns in the decision-theoretic sense (some rows are reachable only through one's own choices); temporal credit assignment returns at depth exactly one; and the exact Bayes-optimal reference is lost (R24).

*Caution at rung 1′:* a deterministic policy drives the opponent deterministically, and the pair can fall into a short limit cycle visiting few states. Exploitation actively destroys state coverage.

**R21 — The opponent family scheme.** *(absorbs A17; supersedes A1)*
A *family* is a set of constraints on regions of the 9×3 matrix, not a list of opponents; sampling within a family is continuous and unbounded. Axes: **reactivity** (how much the three rows sharing an opponent-last-action differ as the model's move varies) and **concentration** (how peaked each row is). Both apply to arbitrary subsets of rows, so the space is large by construction. *Rejected:* a finite pool of individual opponents, which yields a posterior over identity rather than over a parameter — type recognition, which is the memorizing motif by design.

**R22 — Reactivity is observable only through self-variation.**
A model that settles into a fixed exploitative pattern visits only the rows for its one habitual move, where a reactive and an indifferent opponent are indistinguishable. It cannot in principle discover whether it is being responded to. The discretization question and the explore/exploit question are therefore one question. Programmatic form in orientation §8 Q5.

**R23 — Pre-generation survives; drop trajectory multiplicity.** *(absorbs A14)*
Pre-generate the opponent's *randomness*, not its trajectory: a table of responses indexed by joint state and round. The episode then unfolds deterministically given the model's choices. Common random numbers; reproducibility and a finite training set survive. Drop `m` — memorization here is policy identification, not sequence storage, so pool size `N` remains the lever. **New cost:** the training distribution is co-determined by the model's changing policy, so it is non-stationary in a way rung 1 is not, and the data-diversity theory assumes a fixed distribution. Boundaries may move or blur.

**R24 — The reference ladder.** *(absorbs A15; supersedes A10's four-member ladder)*
Exact Bayes-optimal play over a continuous 27-dimensional belief space is intractable. **Explore/exploit balance is an output of the value function, not a tunable parameter** — an action landing in a poorly-known state has higher continuation value because the observation sharpens the posterior.

Ladder: uniform random / posterior-greedy (belief, no planning, no exploration) / certainty-equivalent (belief and planning, no exploration; the posterior mean matrix makes this a finite MDP over 9 states solvable by backward induction) / **Thompson sampling** (explores in proportion to residual uncertainty) / **information-directed sampling** (explicit regret-versus-information tradeoff) / omniscient optimal (unachievable bound). Gaps between adjacent members decompose into planning value, exploration value, and cost of ignorance.

*Consequence:* Phase A's supervised target must be an **exploring** reference; imitating a myopic one teaches the model not to explore. And §9.1's "fraction of ceiling" stops measuring inference quality alone.

**R25 — Self-action tokens become mandatory.** *(absorbs A20, and A4's rationale)*
The model's own last action is half the index into the row about to be used, and its action history is what allows past observations to be attributed to rows. Without it the inference is impossible. Vocabulary 2n+1, length 2K+1. A4's exclusion argument holds only at rung 1, and is retained as the record of why. **Structural result worth keeping:** the same move that closes the loop forces the self-model channel open — one cannot construct the minimal social task without giving the model a record of its own behaviour.

**R26 — Round index conflates evidence and horizon.** *(absorbs A19)*
§3.4's argument that prefix-length analysis is free holds at rung 1. Once actions have consequences, a planning model behaves differently at round 60 than round 10 with identical evidence. Condition the dose-response analysis on rounds-remaining as a second variable and report the two-dimensional profile, or train on variable episode lengths.

**R27 — Gating calculations.** *(absorbs A18 item 1, and A10's cost note)*
**Family distinguishability:** expected divergence per round between each pair of families, hence rounds-to-separate. Any pair indistinguishable inside the episode budget is not a latent the model can infer; merge them. **Evidence per row:** 9 rows from 64 rounds gives ≈7 observations per row against 21 at rung 1, with standard error near 0.2 against 0.1 — resolving only gross differences. A genuine feasibility concern; may force longer episodes or coarser families. Both run before the engine is built.

**R28 — Value-of-information probe target.** *(absorbs A16; decided)*
If optimal play requires weighing what an action would teach, a generalizing network must hold something like expected information gain per state. That is none of the existing targets. Information-directed sampling (R24) supplies the reference quantity directly. Worth more than completeness: a representation of what one does not yet know, used to choose actions that reduce it, is much harder to dismiss as a relabelled intermediate than a count accumulator is.

**R29 — The rung 1 / rung 1′ double dissociation.** *(from A25, A17a)*
The preferred instrument, available only here. An ablation targeting self-history retrieval should impair rung 1′ and spare rung 1; one targeting opponent-history retrieval the reverse. **The two tasks are matched in difficulty by construction** — both 3-row estimation problems with identical statistical structure — which removes the difficulty confound before the experiment starts rather than arguing it away afterward. This is also a better tooling-validation case than modular arithmetic (R32), since the right answer is a fact about sufficient statistics rather than a contested reading of a circuit.

**R33 — Branch T's informational asymmetry becomes structural.** *(absorbs A33 part 1)*
At rung 1 a reporter simply saw more rounds, and any report is eventually redundant. Here the actor's own choices determine which states are visited, so two agents have coverage of *different regions* of the opponent's table. The reporter can know something the actor cannot reach without changing its behaviour — testimony with content that survives the receiver's accumulating evidence.

---

# PART 3 — Program level

Already executed in `belief-circuits-program-orientation-2026-09-19.md`: the separation of program from protocol (A7), the option-space axes and dependencies (§6), tool validity across coordinates (§6.6), training history as a second axis (§6.7), and the self-variation finding (§8 Q5).

**One addition.** The Experiment 1 / Experiment 2 split made in §0 above is the first application of §6's own method — finding the minimal coordinate at which a target phenomenon exists. Belief criteria are validatable at loop-open; the minimal social inference is not. Worth recording in the orientation document as a worked instance rather than leaving it implicit here.

---

# PART 4 — Open decisions

**1. Does the first run need an opponent that reacts to the model?**
**DECIDED 2026-09-22: no.** Experiment 1 uses an opponent agnostic to the player's last action. Confirmed by Ramsey; not to be reopened without new information.

The reason: an opponent that reacts destroys the exact ceiling, which is the entire reason for choosing this substrate, and none of the four criteria in R15 need it. The reacting opponent becomes Experiment 2 (Part 2), which is specified but deferred.

Recorded because it was a live alternative: running both opponent kinds in the first pool would let the first experiment ask whether a model can tell it is being responded to. That was declined in favour of the cheap, certain run first.

**2. Can a rich-gradient, poor-readout control be constructed?** (R18)
If yes, the A-vs-S comparison identifies its effect. If no, it bounds it, and a designated primary result becomes weaker. Unresolved; worth a day of thought before building.

**3. Which family set survives the distinguishability gate?** (R27, Experiment 2)
Determines what the opponent pool actually is. Answerable by calculation before any code.

**4. Which circuit-identity metric?** (R31)
Must be fixed in the pre-registration artifact. Three candidates listed; none obviously dominant.
