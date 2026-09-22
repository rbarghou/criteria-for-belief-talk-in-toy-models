---
id: phases
type: index
status: drafted
---

## Purpose

Which studies belong to which pass. Phase membership is a field on each study; this file is the readable view.

## Content

### Phase 1 — agnostic opponent, exact ceiling, criteria validation

Opponent ignores the model (rung 0 / rung 1, `c-substrate`). Exact Bayes ceiling preserved throughout. Deliverable: validated belief-versus-function-approximation criteria (`c-inst-derived`), not a found circuit (`program/orientation.md` §4). All 14 current studies and 12 current runs belong to phase 1; see `generated/orders.md` for execution and validity order.

### Phase 2 — reactive opponent (deferred, specified)

Loop closed: the opponent conditions on the joint state (its own last action, the player's last action) — rung 1.5 in the four-corner lattice (`c-substrate`). The model's action becomes an input to the process generating its own observations for the first time. This is the first move along `program/orientation.md` §6.1's loop-closure axis, and the minimal social task (§8 Q5 there — reactivity is observable only through self-variation).

What phase 2 needs that phase 1 does not, per the reconciled amendments (Part 2): the opponent family scheme generalized to reactivity and concentration axes over the 9×3 matrix (`c-substrate`); dropping trajectory multiplicity `m` in favor of pre-generating the opponent's randomness table rather than its trajectory, since the episode now unfolds against the model's own choices; the six-member reference ladder in full, since exact Bayes-optimal play over the 27-dimensional belief space is no longer closed-form and rungs 3–6 (certainty-equivalent, Thompson sampling, information-directed sampling) stop collapsing onto posterior-greedy; self-action tokens becoming mandatory rather than a later ablation; round-index dose-response analysis needing a second variable (rounds-remaining) since evidence and horizon are no longer the same axis; gating calculations (family distinguishability, evidence-per-row feasibility) run before any code is written; and a value-of-information probe target, since a generalizing network doing information-directed exploration must hold something like expected information gain per state — none of the phase-1 targets are this.

Phase 2's featured instrument, unavailable at phase 1: the rung-1/rung-1′ double dissociation, matched in difficulty by construction (`c-substrate`), a stronger tooling-validation case than the modular-arithmetic comparison because the right answer is a fact about sufficient statistics rather than a contested reading of a circuit (`p-algorithm-multiplicity`).

**Not yet a set of stub nodes.** Per the migration checklist, phase-2 study/run stubs are created when phase 2 actually opens, not speculatively now — the amendments content above (R20–R29, R33) stays in `history/rps-belief-circuits-amendments-reconciled-2026-09-22.md` Part 2 until then.

### Phase 3 — testimony (branch T, deferred, specified)

Two agents — **actor** and **reporter** — playing against the same fixed, non-adaptive opponent family, so the exact solver survives intact. The reporter observes rounds the actor does not; the actor receives the reporter's message before acting, over a limited-bandwidth channel. **Alignment scalar `w`**: the reporter's payoff is `w` times the actor's return plus `(1-w)` times its own exploitation return against the same opponent, swept 0 to 1. At `w=0`, babbling (the actor learns to ignore the channel); at `w=1`, a fully aligned informant and honest reporting; the interesting region is intermediate, where partial credibility must be established (`p-cheap-talk` for the Crawford–Sobel basis, including the prediction that alignment buys resolution — the number of distinguishable message classes should grow with `w`).

This branch is cheaper than the strategic-depth alternative (branch S — adaptive opponents, second-order belief, sacrifices the exact ceiling) and closer to the motivating question (trust, reputation, lying-versus-being-wrong). What the lying/wrong distinction requires is three things: a belief state with exact ground truth, a report channel not constrained to match it, and an incentive asymmetry that sometimes makes misreport profitable. Phase 1 already supplies the first, which is the rare one; second-order belief (branch S) is needed only for *strategic* deception, not for the distinction itself.

**Preconditions this places on phases 1–2.** An informative equilibrium is a precondition for the lying/wrong distinction, not one point on the alignment sweep — where nothing is believed, a false message is noise, not a lie (`program/orientation.md` §6.2). And branch T's central claim depends on the residual test (`s-crit-residual`) landing first: "lying" is defined against a causally validated posterior, and the residual test is what establishes the probe is reading the network rather than reconstructing the reference. At a reactive rung (phase 2), the actor's own choices determine which states are visited, so two agents cover *different regions* of the opponent's table — the reporter can know something the actor cannot reach without changing its own behaviour, giving testimony content that survives the receiver's accumulating evidence. At phase 1 (no reactivity), a reporter simply saw more rounds and any report is eventually redundant — phase 3's informational asymmetry is structural only once phase 2 exists.

**Not yet a set of stub nodes**, for the same reason as phase 2.

## Migration source

Phase 1: agnostic opponent, exact ceiling, criteria validation. Phase 2: reactive opponent (reconciled register Part 2). Phase 3: testimony (protocol rev.2 branch T, reconciled R30, R33).
