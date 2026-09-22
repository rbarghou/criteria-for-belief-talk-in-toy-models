---
id: c-training
type: component
status: drafted
depends_on: [{node: c-substrate, edge: needs}, {node: c-solvers, edge: needs}]
provides: model, training loop, checkpointing, seeding
---

## Purpose

Architecture, optimizer, phase objectives, exploration control, checkpoint policy, seed management.

## Content

### Model

Decoder-only transformer, 2 layers, 4 heads, `d_model = 128`, `d_head = 32`, MLP hidden 512, learned positional embeddings, causal masking. Two layers is the known minimum for the induction-style solution (previous-token head feeding a matching head). Keep a 3-layer fallback configuration available if 2 layers fails to transition; do not start there. Keep the architecture boring — every nonstandard component is one more thing that could explain an anomalous result.

AdamW. Sweep weight decay over `1e-2` to `1e-1`, but treat it as a **secondary** knob: data diversity (`c-substrate`, `r-diversity-sweep`) is the primary lever on the memorization/generalization competition. (The original protocol over-weighted weight decay by analogy to the modular-arithmetic setting; that analogy does not transfer directly — see `p-algorithm-multiplicity`.) Large or full batch where memory allows. Train far past the point where training performance saturates.

### The phase ladder

Run in this order; the phases have distinct epistemic roles and later ones are read against earlier ones.

**Phase A — supervised sanity run** (`r-phase-a-sanity`). Target: the payoff-maximizing action given the opponent's *true* policy, which the generator knows. Cross-entropy on action positions. Purpose: cheap, clean curves, fast confirmation the substrate transitions at all. This phase **smuggles in a label** — the target depends on hidden state the model cannot observe — and does not satisfy the revealed-preference criterion. It is a debugging instrument only. Do not report Phase A findings as evidence about belief.

**Phase B — self-supervised opponent prediction** (`r-phase-b-main`). Target: the opponent's actual next action. Cross-entropy at opponent-token positions. This is *not* a smuggled label in Phase A's sense — the target is an event the model observes one token later regardless, nothing is stipulated about what belief means, and no privileged access to hidden state is granted. What it does do is train the posterior predictive *directly*, which makes finding it close to tautological. Its role is as a **reference**: it establishes where in the network, at what layer, and at what point in training an exactly-specified posterior appears when the objective demands it. Phase C is then read as whether the same structure appears when nothing demands it except consequences. Report the same measurement suite for Phase B as for Phase C.

**Phase C — policy gradient, the headline** (`r-phase-c-action`, `r-phase-c-stake1`, `r-phase-c-stakevec`). REINFORCE with a learned or running-mean baseline; reward equals per-round payoff. No labels anywhere; the model sees only consequences. Run under all action-channel variants (`c-substrate`). **Phase C initializes from scratch, not from Phase B weights** — if it inherited Phase B's weights it could not answer whether belief arises under payoff pressure alone, because it would already have one. Under variant A specifically, there is no gradient anywhere that asks the network to predict the opponent, so the entire counting-and-normalizing machinery must be built through the payoff channel alone — the interesting condition, and the fragile one.

**Exploration control (specified, not left implicit).** REINFORCE with a baseline and nothing else lets a policy collapse onto a deterministic choice, stop receiving information about the other actions, and sit there permanently. Specify entropy regularization or temperature, with a schedule, as a pre-registered hyperparameter — applies to the stake heads as well as the action head.

**Rescue path if Phase C stalls (Phase C-aux, `r-phase-c-aux`).** Payoff plus an auxiliary opponent-prediction loss with weight `β`, swept downward toward zero. The smallest `β` at which the belief structure still forms is itself a measurement — it quantifies how much predictive pressure the payoff channel fails to supply. Needs multiple seeds per `β` and a criterion for "still forms" fixed in advance, pre-registered — otherwise the threshold tracks nuisance parameters more than the quantity it names. **All headline results come from Phase C; Phase C-aux results are reported as a separate, clearly labelled interpolation.**

**Phase B→C, the curriculum condition** (`r-curriculum`, `s-belief-persistence`). Distinct from ordinary Phase C: train Phase B to convergence, then continue training under payoff pressure from those weights. Training prediction first and *then* applying payoff pressure asks whether an installed belief survives and is used. If a full posterior is installed and payoff pressure erodes it toward the argmax, that is a direct measurement of representational richness decaying to behavioural demand — the cleanest test of "representation trails function" the design has (see `program/orientation.md` on training history as a second, orthogonal axis).

### Seeds and pre-registration

Minimum 5 seeds per condition generally. **30 seeds for the cross-seed circuit comparison specifically** (`r-seed-replication`, `s-uniqueness`) — 5 is a floor adequate for comparing means but inadequate for a claim about a *distribution*: detecting a minority solution present at 10% frequency with 95% confidence needs ≈28 seeds, and 5 would miss it three times in five while reporting clean convergence. Separate the sources of variation for the 30-seed run: fix initialization and vary data order, then the reverse. Fix the primary outcome statistic, the transition definition, and the circuit-identity metric (`records/questions.md` — open) before looking at any decodability curves, as a written, timestamped pre-registration artifact dated before the first Phase B run. That artifact must also record: the "still forms" criterion for the Phase C-aux β sweep, and the no-leak assertion for round-trip tests (`c-substrate`).

### Checkpointing

Checkpoint **densely**, with higher density around any visible transition. Prior work (`p-diversity-boundary`, `p-statistical-induction-heads`) indicates generalizing circuits form gradually beneath a memorizing solution and that a visible transition is a cleanup phase rather than the moment generalization appears. The trajectory is the primary object of study, not the endpoint — budget disk accordingly; it is the whole point.

## Migration source

Protocol rev.2 §7, §8. Reconciled R4 (Phase C from scratch), R5 (exploration control), R12b (seed policy and factorial design).
