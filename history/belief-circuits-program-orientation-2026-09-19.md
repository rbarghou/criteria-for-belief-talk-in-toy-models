# Program Orientation — Belief Circuits

**Date:** 2026-09-19
**Status:** working orientation note, not a protocol and not an essay
**Relation to other documents:** `rps-belief-circuit-baseline-protocol-2026-09-19.md` is one experiment serving this program. The registers (`...-questions-register-...`, `...-amendments-register-...`) track the reading of that protocol.

**What this document is for.** To hold the program-level direction so it does not deform the protocol. A goal that surfaces mid-design can retroactively rewrite a sound experiment around an ambition it is not ready to serve. Keeping the two separate lets the protocol stay minimal and honest while the direction stays visible.

**What this document is not.** Not a development of the theory. Theoretical positions are recorded here as *decisions with consequences for measurement*, in compressed form, not argued or extended. Development belongs elsewhere.

---

## 1. The program

Operationalize critical theory as mechanistic interpretability. Concretely: find conditions sufficient to describe specific emergent phenomena in AI systems, such that theoretical commitments produce measurements rather than vocabulary.

This is the applied arm of Shoggoth Theory. It is also a positive response to the MINP critique: rather than arguing that mechanistic interpretability's essentialism is a problem, build the alternative and show what it measures.

---

## 2. The governing criterion

**A theoretical claim earns its place when it changes a measurement.**

This is the load-bearing discipline of the whole program, and the thing that distinguishes it from theory supplying vocabulary to an experiment that would have run identically without it. Applied retroactively to the 2026-09-19 reading:

- **Passes.** The revealed-preference/rationalizability observation: it adds a measurement to §9.3 (whether an action sequence is rationalizable by *any* belief trajectory, independent of correctness) that distinguishes "the model is wrong" from "the model is not doing the kind of thing that admits of being right or wrong."
- **Passes.** The belief-versus-function-approximation problem: it adds three criteria (multi-consumer structure, off-manifold coherence, path independence) that are implementable and that the protocol currently lacks.
- **Fails, so far.** The observation that §9.2's epistemic-parity choice is a phenomenal/noumenal move in Kant's sense. It reframes correctly but changes nothing that gets logged. Held to the criterion, or dropped.

The criterion applies to this document too. A section here that cannot eventually name a measurement is a placeholder.

---

## 3. Target: structured misrecognition

The long-horizon goal is a toy model capable of self-reference in a specific sense — not self-report, and not a model that predicts its own outputs accurately, but a system whose self-image is assembled from its own exterior and is systematically wrong in a way it cannot correct from inside. Mirror-stage méconnaissance with a mechanistic signature.

The distinction that makes this non-trivial: a model can fit a function that predicts its own behaviour without anything resembling a belief that its behaviour is coherent and integrated. Function approximation is not belief; a self-predictor is not a self. The program needs criteria that separate these, which is why §5 below is the current rung rather than an aside.

**Concrete route this substrate would support.** Require the model to predict its own next action alongside the opponent's. Its action is sampled from a distribution it has no introspective access to — it observes its own past choices but not the logits that produced them. The self-model is therefore an idealization assembled from observed exterior behaviour, and the gap between predicted-self and enacted-self is structured, persistent, and directly measurable.

**Caveat.** That route needs only stochastic action selection and self-observation. It does not need an opponent, and it does not need this game. The misrecognition thread and the belief thread may want to be separate experiments; forcing them together could damage both. Unresolved.

---

## 4. The bootstrap chain, and where it breaks

Stated forward: you cannot study misrecognition before you can study belief; you cannot study belief before you have a substrate where belief has exact ground truth and no judge decides what counts as one. The RPS protocol supplies that substrate.

**Where it breaks.** Every property that makes the substrate gradeable makes it non-social. Exact ground truth exists because the opponent does not respond. Greedy play is exactly optimal because the model cannot influence what it observes. The closed form survives because nothing is watching. The referential circularity that characterizes social belief — no stable optimum, because the target models you back — is precisely what the tractability purchases by exclusion.

So the chain fails under one reading and holds under another:

- **Fails** if the deliverable is "find the belief circuit, then add another agent." The belief circuit in a non-social task is a bigram estimator. The social case will not contain one. Nothing transfers.
- **Holds** if the deliverable is "validate substrate-independent criteria for distinguishing belief from function approximation, against a case where the right answer is independently known." The criteria are about representational format, not about rock-paper-scissors, and they can only be calibrated where ground truth is free.

**Consequence for the protocol:** it is a calibration rig for belief criteria, not rung one of a belief ladder. Same experiment, same code, different claimed deliverable. (Amendment A6.)

---

## 5. Current rung: belief versus function approximation

The open problem the protocol has to solve before anything above it is reachable.

Stated sharply: the RPS task is in-context estimation of a Markov transition matrix. Transformers are known to solve it with an identifiable circuit. Every probe target in the protocol is a deterministic function of the observed token sequence. The Bayesian vocabulary describes the optimal input-output map; it is not evidence that the network does anything other than approximate that map. Without further criteria, calling the intermediate activations "belief" is a relabelling — and it is the same essentialist move the MINP critique charges, assuming a determinate fact sits in the network awaiting discovery and then discovering it.

The three proposed criteria (multi-consumer structure, off-manifold coherence, path independence) are detailed in amendment A5.

**What they have in common, and why it matters to the program.** None of them reads a belief out of the network. Each checks whether the interior is *consistent* under some transformation — across consumers, across interventions, across histories. This is exterior consistency-checking applied to interior states, which is the MINP critique's own working thesis appearing inside the method rather than as a conclusion about it. That is a stronger position than the critique currently occupies: it stops being a complaint about mechanistic interpretability and becomes a specification of what mechanistic interpretability would have to do.

---

## 6. The option space: axes, dependencies, and minimal coordinates

Later experiments are not a sequence. They are coordinates in a space of game structures whose dimensions vary independently, and the program's method is to find the **minimal coordinate at which each target phenomenon first exists** — not to climb a ladder. Stating it this way prevents the common failure of building an elaborate environment and then being unable to say which of its features was load-bearing.

### 6.1 The axes

| Axis | Values | What moving costs | What it buys |
|---|---|---|---|
| **Loop closure** | open → closed | the exact Bayes-optimal reference (A10, A15) | the model's action enters its own observation stream |
| **Motive** | strictly competitive → mixed → common interest | nothing structural; changes what is optimal | anything for trust to be *about* |
| **Adaptivity** | fixed → reactive-stationary → learning | stationarity; a fixed object to hold a posterior over | an opponent that changes in response to history |
| **Neurality** | analytic → trained network → self | closed-form ground truth about the opponent | instrumentable opponent internals |
| **Channel** | none → cheap talk → costly signal → verifiable | strategy space; requires equilibrium analysis | reports, hence lying |
| **Observation** | complete → partial → mediated | the posterior must cover unobserved events | a reason for testimony to exist |
| **Population** | dyad → triad with observer → network with rotating roles | combinatorics; co-learning dynamics | reputation proper |
| **Self-inclusion** | own actions absent → present → own next action predicted | context length; a distractor with no task value | a self-model |

The current protocol sits at: loop open (rung 1) or closed (rung 1.5 under A10), strictly competitive, fixed, analytic, no channel, complete observation, dyad, own actions absent.

### 6.2 Dependency constraints

The axes constrain each other. Four are hard enough to state as ordering requirements:

1. **Motive before neurality.** Self-play in a zero-sum cyclic game converges to the uniform equilibrium. Two networks trained against each other at rock-paper-scissors will find maximal unpredictability and stay there — the least interesting outcome, containing no belief structure to find, because at equilibrium there is nothing to model. Neural-vs-neural is only worth doing once interests are partly aligned or information is asymmetric.
2. **Motive before deception.** Lying is undefined without an informative equilibrium: a false statement works only because statements are ordinarily believed. Where nothing is believed, a false message is noise, not a lie (A12).
3. **Partial observation before the channel is worth anything.** A report about something the receiver can see itself carries no information. Testimony requires an informational asymmetry to transmit across.
4. **Loop closure before self-modelling has consequences.** A self-model in a system whose actions leave no trace predicts something that never returns. The prediction cannot organize subsequent behaviour, which is what misrecognition requires (§3, and open question 5).

### 6.3 Minimal coordinates for each target

| Phenomenon | Minimal coordinate | Note |
|---|---|---|
| Belief | baseline as-is | but see §5 — the function-approximation objection means this coordinate may not suffice for a non-vacuous claim |
| Minimal social inference (is this thing responding to me?) | loop closed | learnable only by self-variation; see open question 5 |
| Trust / reputation | motive mixed, plus either a triad with an observer or a channel | in strict competition the opponent is exhaustively characterized by its behaviour and trust has no object |
| Testimony | observation partial + channel + motive mixed | all three; any two are insufficient |
| Deception | the testimony coordinate + a receiver whose belief is measurable | measurability is the binding constraint, not the game structure |
| Introspection / self-model | self-inclusion + loop closed | |
| Structured misrecognition | self-inclusion + loop closed + structural self-opacity | the self-model must be *necessarily* wrong, not merely inaccurate (§3) |

### 6.4 The motive axis: three implementations of mixed motive

Consolidating material previously scattered across the protocol's deferred-axes section and the amendments register. Mixed motive can be introduced three ways, and they are not equivalent:

1. **Payoff-sum deformation.** Tilt the matrix so outcomes at each cell no longer sum to zero. One continuous parameter, trivial to implement.
2. **Move-sequence embedding.** A second payoff matrix triggered by a pattern of play — the tie-chain mechanism. Attractive because entry into the cooperative regime is endogenous and requires coordination to achieve. **As literally specified it yields a stag hunt, not a prisoner's dilemma:** a tie means both players played the same action, so tie-chain outcomes are symmetric by construction, and the off-diagonal temptation and sucker cells — the entire content of the dilemma — are unreachable. For a program targeting *trust* this may be the better game anyway, on Skyrms' argument that the dilemma models cooperation under temptation while the stag hunt models trust and assurance.
3. **Inter-agent alignment scalar.** Leave the game untouched; make one agent's reward a weighted mixture of its own return and another's. Cheapest by a wide margin, and the only one that preserves the exact posterior.

**The finding, and the residual reason not to settle for (3).** Options 1 and 2 are inert against a fixed non-adaptive opponent — nothing reciprocates, so no cooperation is possible — which is why branch T uses option 3. But 1 and 2 make the mixed motive a property of the *game both parties face*, whereas 3 makes it a property of one agent's reward function that the other cannot perceive. If the eventual target is an agent that can reason about whether cooperation is available, that difference is not cosmetic.

### 6.5 The neurality axis: three regimes of ground truth

Moving along this axis does not make the experiment harder in degree; it changes the kind of ground truth available, which is a different epistemic regime.

- **Analytic opponent.** Policy known in closed form, so the ideal belief is computable. Current design.
- **Trained network opponent.** No Dirichlet parameters, so the exact posterior over its policy disappears. In exchange, you built it and can instrument it: what it actually believes becomes answerable by probing rather than by calculation.
- **Self-play.** The same, plus co-learning non-stationarity and (in zero-sum) convergence to the uninteresting equilibrium.

**Why this matters most for deception.** The claim "A deceived B" requires knowing what B came to believe. Against a scripted receiver that is known by construction; against a neural receiver, by instrumentation; against a human, not at all. The instrumented case is precisely where the program's regress lives — the measurement of deception comes to depend on the validity of a probe, which is the thing this program is trying to establish rather than assume. Neural-vs-neural is therefore not a later, harder version of the same experiment. It should not be entered until the probe-validity criteria of §5 have been established somewhere the answer is independently known.

### 6.6 Tool validity does not travel with the tool

Standing commitment: **tooling validated at one coordinate is not thereby valid at another.** Do not assume that instruments working in the neural-vs-heuristic regime remain effective in neural-vs-neural after any retraining step. Three distinct mechanisms, with different remedies:

1. **Representational drift (mild).** A probe is fit to a particular network's basis; retraining moves the basis. Already handled by refitting probes per checkpoint. A nuisance, not a threat.
2. **Loss of referent (severe).** In the neural-vs-heuristic regime, belief is an externally specified object and probe validity means agreement with something computed independently. In neural-vs-neural no such object exists: the belief being probed for concerns a counterpart that is itself learning, and there is no closed form. The tooling has not become miscalibrated — it has lost the thing that made calibration meaningful. No amount of retraining repairs this, because there is nothing to retrain against.
3. **Selection against legibility (conditional, but real).** An opponent sees behaviour, not internals, so there is no direct pressure against representational legibility as such — a model could represent its belief clearly and then deliberately randomize its play. But once a report channel exists and misreporting pays, training shapes the *relationship* between internal state and output, which is exactly the relationship probes exploit. And if a probe is ever used inside the training loop as a detector, the pressure becomes direct: exposing the interior makes the interior part of the interface, and the interface is what gets optimized against. This is the MINP-critique regress in mechanical form.

**What transfers, and what does not.** Calibration does not travel. Criteria might. The three criteria of §5 — multi-consumer structure, off-manifold coherence, path independence — do not require knowing the right answer; they ask whether a representation behaves like a representation rather than whether it matches a reference. That is what makes them substrate-independent in a way a fitted probe direction never is. **The entire argument for the current protocol being a prerequisite rests on it producing criteria rather than calibrations.** If it produces only a validated probe direction, it has produced nothing that survives the move.

**Practical response — the single-axis transfer protocol.** Turn the warning into a measurement. Move one axis at a time, from a coordinate where ground truth exists to an adjacent one where it partially survives, and measure how much tool validity is lost per step. Reactive opponents retain a closed-form posterior. A neural opponent trained on a known family retains an approximately characterizable policy. A small neural opponent can itself be probed to establish what it believes even where no closed form exists. Each single-axis move leaves enough residual ground truth to ask whether the tool still recovers what is independently known — yielding a degradation curve across the option space rather than a cliff discovered after crossing it.

**Residual honesty.** Tooling must co-evolve with its subjects in ways that probably cannot be specified in advance. The transfer protocol measures the problem; it does not solve it.

### 6.7 A second, orthogonal axis: training history

§6.1's axes are all properties of the *environment*. There is a second dimension the option space needs, and it is orthogonal to all eight: the **developmental path** by which a network arrives at a given task. The same environment can be reached by different training histories, and whether the resulting networks are the same object is an open question with a measurement attached.

The concrete instance is the phase curriculum (amendment A21). Training a model to predict the opponent and *then* subjecting it to payoff pressure produces a network at the same final coordinate as one trained under payoff pressure alone. The two are behaviourally comparable by construction. Are they mechanistically the same?

Three reasons this belongs at program level rather than as a protocol detail:

1. **It is the sharpest test of "representation trails function."** If prediction training installs a full posterior and payoff pressure then erodes it toward the argmax — because the argmax is all behaviour requires — that is a direct, measurable demonstration that representational richness is not preserved for its own sake. If instead the posterior persists, the thesis is weakened in a specific and quantified way. Either outcome is a result.
2. **It is the constructive form of the frozen-checkpoint critique.** The program's founding complaint (§1, and the protocol's §1) is that a checkpoint does not tell you about the trajectory that produced it. The curriculum condition inverts the complaint into an experiment: deliberately produce two networks matched on task and differing in history, and ask whether they are the same mechanism. If they differ mechanistically while matching behaviourally, behaviour underdetermines mechanism — demonstrated rather than asserted. The cross-seed circuit-comparison machinery already specified (protocol §9.5) does the measuring.
3. **It rehearses a structure the program will need later.** An installed self-model subsequently subjected to payoff pressure has the same shape. Whatever is learned about whether installed structure survives its objective transfers to that case.

**Implication for the option space.** Every coordinate in §6.1 is reachable by multiple paths. Where path-dependence is found, the coordinate alone does not specify the experiment, and results indexed only by environment are underspecified.

---

## 7. Recorded positions with measurement consequences

Compressed. Each is a commitment already made, with its downstream effect noted.

- **No judge.** Phenomena are not operationalized by a rubric applied by another model. Ground truth comes from the generative process or not at all. → Determines substrate choice; rules out most naturalistic settings.
- **Revealed preference, not report.** Belief is read from graded action, never from a stated answer. → Requires a graded action channel (the stake variant), because a single categorical choice can only reveal an ordering's top element.
- **Epistemic parity.** The reference is what an ideal reasoner with exactly the model's observations would believe — not the truth. → Probe targets are posterior quantities, never generative parameters.
- **Trajectory over endpoint.** A causal claim at one checkpoint cannot distinguish a structurally central mechanism from one that would be rebuilt in a few steps. → Dense checkpointing; the three-part causal standard in §9.5 of the protocol.
- **Reputation requires mixed motive.** In a strictly competitive game the opponent is exhaustively characterized by its behavioural distribution, so trust has no object and a testimony channel has only babbling equilibria. → Mixed motive must enter before any trust work; cheapest entry is between agents (the alignment scalar in branch T), not inside the game's move structure.

---

## 8. Open strategic questions

1. Are the belief thread and the misrecognition thread one experiment or two? (§3 caveat.)
2. Which extension branch is the real destination — testimony, or strategic depth? The protocol's build order currently assumes testimony.
3. Does the game-theoretic tradition's notion of belief range over strategies, over types, or over states of the world, and does the protocol's stipulation need adjusting to match? (Questions register Q1.)
4. What is the minimal setting in which self-opacity is structural rather than stipulated?

5. **Are reward chains a necessary cost of self-reference, and if so what is the minimal one?** If they are, then the program's real object is the cost-benefit structure of games that permit misrecognition, and this protocol is the foundation that makes those costs legible.

   Sharpened, with two things separated. *Temporal credit assignment* (delayed reward) is a property of learning dynamics. *Causal closure of the action-observation loop* — whether the agent's action is an input to the process generating its future observations — is a property of task structure. The current design has neither, and what makes misrecognition unreachable here is the second: a system whose actions leave no trace has nothing for a self-model to be about in the consequential sense. The mirror stage is constitutive; the misrecognized unity organizes subsequent behaviour, which requires the loop to close.

   Closing the loop appears to drag delayed reward back in unavoidably: if actions affect observations, and observations affect which action is best, then actions affect future payoffs. This holds even for purely informational coupling (an agent choosing what to observe rather than what to do) — observing well now pays off later. So reward chains look *entailed* rather than independently required, and the minimization target is not their presence but their **depth**. How short can the chain be? Depth one, where an action at round *t* affects only the payoff at *t*+1?

   **Second axis, possibly more important than depth.** Whether the loop passes through inert environment or through another agent that is modelling you. Self-reference in the register this program works in is mediated by the Other; the mirror is a site of recognition, not a physical surface. A depth-one chain through a modelling opponent and a depth-one chain through a mechanical environment are structurally different objects at identical chain length.

   **Conjecture to test rather than assume — the tractability/sociality tradeoff.** Each step toward misrecognition costs exactly the property that makes belief gradeable. Closing the loop destroys the exogenous opponent, which destroys the exact ceiling, which destroys the reference everything is graded against (§4). The program question is whether any point on that frontier has both, or whether the frontier is strict.

   **Finding (2026-09-20): reactivity is observable only through self-variation.** Under the reactive-opponent design (amendment A10), the latent that distinguishes a responsive opponent from an indifferent one is defined by how the opponent's behaviour varies with the *model's* last action. A model that settles into a fixed exploitative pattern visits only the rows corresponding to its one habitual move, where a reactive and an indifferent opponent are indistinguishable. It cannot in principle discover whether it is being responded to.

   Two consequences. Practically, the discretization question and the explore/exploit question are one question, not two: the minimal social latent is learnable only by deliberately varying oneself, which makes exploration constitutive rather than instrumental. Programmatically, this is the sharpest thing the substrate has yet produced on its own terms — the condition for registering that another agent is present is self-variation, and a system that has converged on a policy has thereby foreclosed its own capacity to detect the other. That is a structural claim with a measurement attached, and it should be held to the criterion in §2.
