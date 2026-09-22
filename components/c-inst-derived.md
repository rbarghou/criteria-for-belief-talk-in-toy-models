---
id: c-inst-derived
type: component
status: drafted
depends_on: [{node: c-inst-grounded, edge: calibrates}, {node: c-terminology, edge: needs}]
provides: probes, decoding, criteria tests
---

## Purpose

Instruments requiring a learned decoder: probes, decodability, decoded-belief measures, the residual test, and the four belief-vs-function-approximation criteria. Valid only where calibrated against grounded instruments; see the grounding report.

## Content

### Belief decodability

At every checkpoint, for each layer and position, fit linear probes from the residual stream to each target:

1. **Full predictive**, in centred-log-ratio coordinates (`c-terminology`; `p-compositional-data` for why). State the coordinate choice and report at least one alternative — raw probabilities, log probabilities, and clr give different answers about what "linear" means.
2. **Normalized counts (posterior mean policy)** and **total evidence**, reported *separately* — not the raw count matrix, which is confounded with elapsed time (`c-solvers`).
3. **Argmax class** — which action is the best response (3-way classification at n=3).
4. **Decision margin** — scalar regression.

Probe at **both** opponent-token positions (where evidence arrives) and action-emission positions (where it must have been gathered). Fit on training episodes, evaluate on held-out ones. Report per-layer profiles, not just the maximum.

Plot decodability against training step. **The central question is whether each target rises at, before, or after the behavioural return transition (`c-inst-grounded`) — and which of the four rises at all** (`s-decodability-timing`).

**Reporting requirement.** Report **excess** decodability over the controls below, not raw R² or raw accuracy. A rising raw curve alone is compatible with representation drift and norm growth and says nothing on its own.

### Probe-level controls

Every decodability number is reported as excess over the maximum of:

- **Random-init control.** Identical architecture, untrained weights, same probe-fitting procedure.
- **Raw-feature control.** Probe fit directly on the accumulated one-hot token history — the information trivially available without computation. Decisive: counts are nearly linearly recoverable from the input by accumulation alone, so a probe may be finding the input rather than the belief.
- **The decodability null.** Permute probe targets **between episodes at matched round index** — this preserves the target's temporal structure and marginal distribution while destroying its correspondence to *this* episode's activations. A naive shuffle across all positions is too easy to fail: the real target grows monotonically with round index, so a probe would beat that control partly for the wrong reason, overstating selectivity. (The unexploitable-opponent condition is *not* this control — see `c-inst-grounded`; it tests usage, not decodability.)

Report selectivity in the control-task sense (`p-probe-selectivity`): the gap between real-target and shuffled-target performance at matched capacity.

### Belief usage, derived half

- Fraction of model actions matching the best response to the *decoded* belief, as a function of decision margin, read against the true-belief version in `c-inst-grounded`.
- The A/S/S-full comparison (`c-substrate`) reported as a primary result here: which probe targets are decodable under each action-channel variant (`s-representation-vs-demand`).

### The residual test

The probe is fit to predict the *true* posterior, so the decoded belief is regularized toward truth and a *systematically wrong* belief is invisible by construction. Fix: examine the probe's residuals — the ways the decoded belief departs from the true one — and ask whether the model's actions follow those departures. Noise should not predict behaviour; a genuine internal state should (`s-crit-residual`). A positive result validates the **probe** rather than the model, and does so without depending on any control condition. Branch-T testimony work (phase 3) depends on this result: "lying" there is defined against a causally validated posterior, and the residual test is what establishes the probe is reading the network rather than reconstructing the reference.

### The four belief-versus-function-approximation criteria

As specified without these, nothing distinguishes belief from function approximation: the task is in-context estimation of a transition matrix, transformers are known to solve it, and every probe target is a deterministic function of the token sequence. Calling the intermediate activations "belief" would otherwise be a relabelling.

1. **Multi-consumer structure** (`s-crit-multiconsumer`). One internal state required to serve several distinct decision problems. Does one shared representation serve them, or do task-specific features form independently?
2. **Off-manifold coherence** (`s-crit-offmanifold`). Edit the state to a posterior the model has never had reason to hold and ask whether downstream behaviour follows it. A memorized map has no commitments off its data manifold.
3. **Path independence** (`s-crit-pathindependence`). The same count matrix is reachable by many orderings. Convergent representation means a state; retained ordering means a trace.
4. **Residual-following** (`s-crit-residual`, above). Where the decoded belief departs from truth, behaviour departs with it.

None of the four reads a belief out of the network; each checks whether the interior is *consistent* under some transformation. That substrate-independence is what a fitted probe direction never has on its own, and it is the program's governing methodological claim appearing inside the method rather than as a conclusion about it (`program/orientation.md` §5).

### The circuit-identity metric (open — see `records/questions.md`)

Nothing in the design states what would count as "the same circuit" across seeds, which otherwise leaves the degeneracy measurement (`s-uniqueness`) to inspection. Three candidates, none obviously dominant, to be fixed in the pre-registration artifact before the 30-seed run: representational similarity at matched layers (e.g. CKA); alignment of probe directions after optimal permutation of heads; functional equivalence under transplanting a head between models. **Not yet chosen — do not assume one.**

## Migration source

Protocol rev.2 §9.2, §10.3. Reconciled R6, R7, R12 (residual test), R14 (decodability null), R15 (the four criteria), R31 (circuit-identity metric).
