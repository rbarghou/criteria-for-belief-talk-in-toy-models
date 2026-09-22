---
id: program
type: program
status: ready
---

## Purpose

Why the program exists, what counts as a result, and the space of possible experiments. Governs everything below it.

## Content

### 1. The program

Operationalize critical theory as mechanistic interpretability. Concretely: find conditions sufficient to describe specific emergent phenomena in AI systems, such that theoretical commitments produce measurements rather than vocabulary.

This is the applied arm of Shoggoth Theory, and a positive response to the MINP critique: rather than arguing mechanistic interpretability's essentialism is a problem, build the alternative and show what it measures.

### 2. The governing criterion

**A theoretical claim earns its place when it changes a measurement.** This is the load-bearing discipline of the whole program — what distinguishes a claim from vocabulary supplied to an experiment that would run identically without it. Applied to the reading that produced the reconciled amendments:

- **Passes.** Rationalizability: adds a measurement (`s-rationalizability`) distinguishing "the model is wrong" from "the model is not doing the kind of thing that admits of being right or wrong."
- **Passes.** Belief-versus-function-approximation: adds three implementable criteria the design otherwise lacked (multi-consumer structure, off-manifold coherence, path independence — `c-inst-derived`).
- **Fails, so far.** The observation that the epistemic-parity choice is a phenomenal/noumenal move in Kant's sense. Reframes correctly, changes nothing that gets logged. Held to the criterion, or dropped.

The criterion applies to this document too: a section here that cannot eventually name a measurement is a placeholder.

### 3. Target: structured misrecognition

The long-horizon goal is a toy model capable of self-reference in a specific sense — not self-report, not a model that predicts its own outputs accurately, but a system whose self-image is assembled from its own exterior and is systematically wrong in a way it cannot correct from inside. Mirror-stage méconnaissance with a mechanistic signature.

The distinction that makes this non-trivial: a model can fit a function predicting its own behaviour without anything resembling a belief that its behaviour is coherent and integrated. Function approximation is not belief; a self-predictor is not a self. The program needs criteria separating these — which is why §5 is the current rung rather than an aside.

**Concrete route this substrate would support.** Require the model to predict its own next action alongside the opponent's, sampled from a distribution it has no introspective access to — it observes its own past choices but not the logits that produced them. The self-model is an idealization assembled from observed exterior behaviour; the gap between predicted-self and enacted-self is structured, persistent, and directly measurable.

**Open caveat.** That route needs only stochastic action selection and self-observation — it needs neither an opponent nor this game. The misrecognition thread and the belief thread may want to be separate experiments; forcing them together could damage both. Unresolved (open strategic question 1, below).

### 4. The bootstrap chain, and where it breaks

Stated forward: you cannot study misrecognition before you can study belief; you cannot study belief before you have a substrate where belief has exact ground truth and no judge decides what counts as one. The RPS substrate supplies that.

**Where it breaks.** Every property making the substrate gradeable makes it non-social. Exact ground truth exists because the opponent does not respond. Greedy play is exactly optimal because the model cannot influence what it observes. The closed form survives because nothing is watching. The referential circularity that characterizes social belief — no stable optimum, because the target models you back — is precisely what tractability purchases by exclusion.

The chain fails under one reading and holds under another:

- **Fails** if the deliverable is "find the belief circuit, then add another agent." The belief circuit in a non-social task is a bigram estimator. The social case will not contain one. Nothing transfers.
- **Holds** if the deliverable is "validate substrate-independent criteria for distinguishing belief from function approximation, against a case where the right answer is independently known." The criteria concern representational format, not rock-paper-scissors, and can only be calibrated where ground truth is free.

**Consequence:** phase 1 is a calibration rig for belief criteria, not rung one of a belief ladder. Same code; different claimed deliverable.

### 5. Current rung: belief versus function approximation

The open problem to solve before anything above it is reachable. Stated sharply: the RPS task is in-context estimation of a Markov transition matrix. Transformers are known to solve it with an identifiable circuit. Every probe target is a deterministic function of the observed token sequence. The Bayesian vocabulary describes the optimal input-output map; it is not evidence the network does anything other than approximate that map. Without further criteria, calling the intermediate activations "belief" is a relabelling — the same essentialist move the MINP critique charges, assuming a determinate fact sits in the network awaiting discovery and then discovering it.

The four criteria (`c-inst-derived`: multi-consumer structure, off-manifold coherence, path independence, residual-following) are the response. **What they have in common:** none reads a belief out of the network. Each checks whether the interior is *consistent* under some transformation — across consumers, across interventions, across histories. This is exterior consistency-checking applied to interior states — the MINP critique's own working thesis appearing inside the method rather than as a conclusion about it. That is a stronger position than the critique currently occupies: it stops being a complaint about mechanistic interpretability and becomes a specification of what mechanistic interpretability would have to do.

### 6. The option space: axes, dependencies, minimal coordinates

Later experiments are not a sequence. They are coordinates in a space of game structures whose dimensions vary independently, and the program's method is to find the **minimal coordinate at which each target phenomenon first exists** — not to climb a ladder. This prevents the common failure of building an elaborate environment and then being unable to say which of its features was load-bearing.

#### 6.1 The axes

| Axis | Values | What moving costs | What it buys |
|---|---|---|---|
| **Loop closure** | open → closed | the exact Bayes-optimal reference | the model's action enters its own observation stream |
| **Motive** | strictly competitive → mixed → common interest | nothing structural; changes what is optimal | anything for trust to be *about* |
| **Adaptivity** | fixed → reactive-stationary → learning | stationarity; a fixed object to hold a posterior over | an opponent that changes in response to history |
| **Neurality** | analytic → trained network → self | closed-form ground truth about the opponent | instrumentable opponent internals |
| **Channel** | none → cheap talk → costly signal → verifiable | strategy space; requires equilibrium analysis | reports, hence lying |
| **Observation** | complete → partial → mediated | the posterior must cover unobserved events | a reason for testimony to exist |
| **Population** | dyad → triad with observer → network with rotating roles | combinatorics; co-learning dynamics | reputation proper |
| **Self-inclusion** | own actions absent → present → own next action predicted | context length; a distractor with no task value | a self-model |

**Phase 1 sits at:** loop open (rung 1), strictly competitive, fixed, analytic, no channel, complete observation, dyad, own actions absent. **Phase 2 moves loop closure to closed** (rung 1.5, `c-substrate`) and nothing else. **Phase 3 (branch T)** additionally moves motive toward mixed (via the alignment scalar, §6.4) and channel to cheap talk, while returning loop closure to open — see the worked instance in §9 below.

#### 6.2 Dependency constraints

1. **Motive before neurality.** Self-play in a zero-sum cyclic game converges to the uniform equilibrium — two networks trained against each other at RPS find maximal unpredictability and stay there, containing no belief structure to find, because at equilibrium there is nothing to model. Neural-vs-neural is only worth doing once interests are partly aligned or information is asymmetric.
2. **Motive before deception.** Lying is undefined without an informative equilibrium: a false statement works only because statements are ordinarily believed. Where nothing is believed, a false message is noise, not a lie.
3. **Partial observation before the channel is worth anything.** A report about something the receiver can see itself carries no information. Testimony requires an informational asymmetry to transmit across.
4. **Loop closure before self-modelling has consequences.** A self-model in a system whose actions leave no trace predicts something that never returns; the prediction cannot organize subsequent behaviour, which is what misrecognition requires (§3; §8 Q5).

#### 6.3 Minimal coordinates for each target

| Phenomenon | Minimal coordinate | Note |
|---|---|---|
| Belief | phase-1 baseline as-is | but see §5 — the function-approximation objection means this coordinate may not suffice for a non-vacuous claim |
| Minimal social inference (is this thing responding to me?) | loop closed | learnable only by self-variation; §8 Q5 |
| Trust / reputation | motive mixed, plus either a triad with an observer or a channel | in strict competition the opponent is exhaustively characterized by its behaviour and trust has no object |
| Testimony | observation partial + channel + motive mixed | all three; any two are insufficient |
| Deception | the testimony coordinate + a receiver whose belief is measurable | measurability is the binding constraint, not the game structure |
| Introspection / self-model | self-inclusion + loop closed | |
| Structured misrecognition | self-inclusion + loop closed + structural self-opacity | the self-model must be *necessarily* wrong, not merely inaccurate (§3) |

#### 6.4 The motive axis: three implementations of mixed motive

1. **Payoff-sum deformation.** Tilt the matrix so outcomes at each cell no longer sum to zero. One continuous parameter, trivial to implement. Inert against a fixed non-adaptive opponent — nothing reciprocates, so no cooperation is possible.
2. **Move-sequence embedding (tie-chain).** A second payoff matrix triggered by a pattern of play. Attractive because entry into the cooperative regime is endogenous, requiring coordination. **As literally specified this yields a stag hunt, not a prisoner's dilemma:** a tie means both players played the same action, so tie-chain outcomes are symmetric by construction, and the off-diagonal temptation/sucker cells — the entire content of the dilemma — are unreachable this way. A second reading, in which the two ties only gate a *third* round whose moves may differ, does yield a genuine dilemma; which is intended has not been decided. For a program targeting trust specifically, the stag hunt may be the better base game regardless, on Skyrms' argument that the prisoner's dilemma models cooperation under temptation while the stag hunt models trust and assurance — whether the other party will show up, not whether defection tempts. Also inert against a fixed opponent, and additionally destroys the closed-form greedy optimum by making the decision problem non-myopic (a current action affects whether a chain starts).
3. **Inter-agent alignment scalar.** Leave the game untouched; make one agent's reward a weighted mixture of its own return and another's. Cheapest by a wide margin, and the only one preserving the exact posterior — the branch-T mechanism (`catalogue/phases.md` phase 3).

**The finding, and the residual reason not to settle for (3) alone.** Options 1 and 2 are inert against a fixed non-adaptive opponent, which is why branch T uses option 3. But 1 and 2 make mixed motive a property of the *game both parties face*, whereas 3 makes it a property of one agent's reward function the other cannot perceive. If the eventual target is an agent that can reason about whether cooperation is available at all, that difference is not cosmetic — revisit 1 and 2 once adaptive opponents exist (phase 2+).

#### 6.5 The neurality axis: three regimes of ground truth

Moving along this axis changes the *kind* of ground truth available, not just its difficulty.

- **Analytic opponent** — policy known in closed form, ideal belief computable. Phase 1–2 design.
- **Trained network opponent** — no Dirichlet parameters, so the exact posterior over its policy disappears; in exchange it can be instrumented, so what it actually believes becomes answerable by probing rather than calculation.
- **Self-play** — the same, plus co-learning non-stationarity and, in zero-sum, convergence to the uninteresting equilibrium (§6.2.1).

**Why this matters most for deception.** "A deceived B" requires knowing what B came to believe — known by construction against a scripted receiver, by instrumentation against a neural one, not at all against a human. The instrumented case is where the program's own regress lives: the measurement of deception comes to depend on the validity of a probe, which is the thing this program is trying to establish rather than assume. Neural-vs-neural is therefore not a later, harder version of the same experiment — it should not be entered until the probe-validity criteria of §5 have been established somewhere the answer is independently known.

#### 6.6 Tool validity does not travel with the tool

Standing commitment: **tooling validated at one coordinate is not thereby valid at another.** Three distinct mechanisms, with different remedies:

1. **Representational drift (mild).** A probe is fit to a particular network's basis; retraining moves the basis. Already handled by refitting probes per checkpoint. A nuisance, not a threat.
2. **Loss of referent (severe).** In neural-vs-heuristic, belief is an externally specified object and probe validity means agreement with something computed independently. In neural-vs-neural no such object exists — the belief being probed for concerns a counterpart that is itself learning, with no closed form. The tooling has not become miscalibrated; it has lost the thing that made calibration meaningful. No amount of retraining repairs this.
3. **Selection against legibility (conditional, but real).** An opponent sees behaviour, not internals, so there is no direct pressure against representational legibility as such — a model could represent its belief clearly and still deliberately randomize its play. But once a report channel exists and misreporting pays, training shapes the *relationship* between internal state and output — exactly the relationship probes exploit. If a probe is ever used inside the training loop as a detector, the pressure becomes direct: exposing the interior makes the interior part of the interface, and the interface is what gets optimized against. The MINP-critique regress in mechanical form.

**What transfers, and what does not.** Calibration does not travel. Criteria might. The four criteria of §5 do not require knowing the right answer; they ask whether a representation behaves like a representation rather than whether it matches a reference — substrate-independent in a way a fitted probe direction never is. **The entire argument for phase 1 being a prerequisite rests on it producing criteria rather than calibrations.** If it produces only a validated probe direction, it has produced nothing that survives the move.

**Practical response — the single-axis transfer protocol.** Move one axis at a time, from a coordinate where ground truth exists to an adjacent one where it partially survives, and measure how much tool validity is lost per step. Reactive opponents (phase 2) retain a closed-form posterior. A neural opponent trained on a known family retains an approximately characterizable policy. A small neural opponent can itself be probed to establish what it believes even with no closed form. Each single-axis move leaves enough residual ground truth to ask whether the tool still recovers what is independently known — a degradation curve across the option space rather than a cliff discovered after crossing it.

**Residual honesty.** Tooling must co-evolve with its subjects in ways that probably cannot be specified in advance. The transfer protocol measures the problem; it does not solve it.

#### 6.7 A second, orthogonal axis: training history

§6.1's axes are all properties of the *environment*. There is a second dimension, orthogonal to all eight: the **developmental path** by which a network arrives at a given task. The same environment can be reached by different training histories, and whether the resulting networks are the same object is an open question with a measurement attached.

The concrete instance is the Phase B→C curriculum (`c-training`, `r-curriculum`, `s-belief-persistence`): training a model to predict the opponent and *then* subjecting it to payoff pressure produces a network at the same final coordinate as one trained under payoff pressure alone, behaviourally comparable by construction. Are they mechanistically the same?

Three reasons this belongs at program level:

1. **The sharpest test of "representation trails function."** If prediction training installs a full posterior and payoff pressure then erodes it toward the argmax — because the argmax is all behaviour requires — that is a direct, measurable demonstration that representational richness is not preserved for its own sake. If the posterior persists instead, the thesis is weakened in a specific and quantified way. Either outcome is a result.
2. **The constructive form of the frozen-checkpoint critique** (§1). Deliberately produce two networks matched on task and differing in history, and ask whether they are the same mechanism. If they differ mechanistically while matching behaviourally, behaviour underdetermines mechanism — demonstrated rather than asserted. The cross-seed circuit-comparison machinery (`c-inst-derived`, `s-uniqueness`) does the measuring.
3. **Rehearses a structure the program will need later.** An installed self-model subsequently subjected to payoff pressure has the same shape as this test.

**Implication.** Every coordinate in §6.1 is reachable by multiple paths. Where path-dependence is found, the coordinate alone does not specify the experiment, and results indexed only by environment are underspecified.

### 7. Recorded positions with measurement consequences

- **No judge.** Phenomena are not operationalized by a rubric applied by another model. Ground truth comes from the generative process or not at all. → Determines substrate choice; rules out most naturalistic settings.
- **Revealed preference, not report.** Belief is read from graded action, never from a stated answer. → Requires a graded action channel (the stake variants), since a single categorical choice can only reveal an ordering's top element.
- **Epistemic parity.** The reference is what an ideal reasoner with exactly the model's observations would believe — not the truth. → Probe targets are posterior quantities, never generative parameters.
- **Trajectory over endpoint.** A causal claim at one checkpoint cannot distinguish a structurally central mechanism from one that would be rebuilt in a few steps. → Dense checkpointing; the three-part causal standard (`c-inst-grounded`).
- **Reputation requires mixed motive.** In a strictly competitive game the opponent is exhaustively characterized by its behavioural distribution, so trust has no object and a testimony channel has only babbling equilibria. → Mixed motive must enter before any trust work; cheapest entry is between agents (§6.4's alignment scalar), not inside the game's move structure.

### 8. Open strategic questions

1. Are the belief thread and the misrecognition thread one experiment or two? (§3.)
2. Which extension branch is the real destination — testimony (branch T) or strategic depth (branch S)? Phase ordering (`catalogue/phases.md`) currently assumes testimony.
3. Does the game-theoretic tradition's notion of belief range over strategies, over types, or over states of the world, and does the current stipulation need adjusting to match? (`records/questions.md`, entry on grounding for the game-theoretic notion of belief.)
4. What is the minimal setting in which self-opacity is structural rather than stipulated?
5. **Are reward chains a necessary cost of self-reference, and if so what is the minimal one?** If they are, the program's real object is the cost-benefit structure of games that permit misrecognition, and phase 1 is the foundation that makes those costs legible.

   Two things separated: *temporal credit assignment* (delayed reward) is a property of learning dynamics; *causal closure of the action-observation loop* — whether the agent's action is an input to the process generating its future observations — is a property of task structure. Phase 1 has neither, and what makes misrecognition unreachable there is the second: a system whose actions leave no trace has nothing for a self-model to be about in the consequential sense. The mirror stage is constitutive; the misrecognized unity organizes subsequent behaviour, which requires the loop to close.

   Closing the loop appears to drag delayed reward back in unavoidably: if actions affect observations, and observations affect which action is best, then actions affect future payoffs — this holds even for purely informational coupling (choosing what to observe rather than what to do), since observing well now pays off later. So reward chains look *entailed* rather than independently required, and the minimization target is their **depth**, not their presence. How short can the chain be — depth one, where an action at round `t` affects only the payoff at `t+1`?

   **Second axis, possibly more important than depth.** Whether the loop passes through inert environment or through another agent that is modelling you. Self-reference in the register this program works in is mediated by the Other; the mirror is a site of recognition, not a physical surface. A depth-one chain through a modelling opponent and a depth-one chain through a mechanical environment are structurally different objects at identical chain length.

   **Conjecture to test rather than assume — the tractability/sociality tradeoff.** Each step toward misrecognition costs exactly the property that makes belief gradeable. Closing the loop destroys the exogenous opponent, which destroys the exact ceiling, which destroys the reference everything is graded against (§4). The program question is whether any point on that frontier has both, or whether the frontier is strict.

   **Finding (2026-09-20): reactivity is observable only through self-variation.** Under a reactive-opponent design (phase 2), the latent distinguishing a responsive opponent from an indifferent one is defined by how the opponent's behaviour varies with the *model's* last action. A model that settles into a fixed exploitative pattern visits only the rows for its one habitual move, where a reactive and an indifferent opponent are indistinguishable — it cannot in principle discover whether it is being responded to.

   Two consequences. Practically, the discretization question and the explore/exploit question are one question, not two: the minimal social latent is learnable only by deliberately varying oneself, making exploration constitutive rather than instrumental. Programmatically, this is the sharpest thing the substrate has produced on its own terms — the condition for registering that another agent is present is self-variation, and a system that has converged on a policy has thereby foreclosed its own capacity to detect the other. A structural claim with a measurement attached (§2).

### 9. The Experiment 1 / Experiment 2 split as a worked instance of §6's method

The phase 1 / phase 2 split (`catalogue/phases.md`) is the first application of §6's own method: finding the minimal coordinate at which a target phenomenon first exists, rather than building the maximal environment and asking what happened to be load-bearing. Belief criteria (§5) are validatable at loop-open, where the exact ceiling still exists and every one of the four criteria in `c-inst-derived` is answerable against an opponent that ignores the model. The minimal *social* inference — whether a model can tell it is being responded to (§8 Q5) — is not validatable there at all; it requires loop closure and is unlearnable without self-variation. Recording it here as the worked instance rather than leaving it implicit in the phase split: the two phases are not stages of one growing experiment, they are two different minimal coordinates for two different phenomena that happen to share an engine.
