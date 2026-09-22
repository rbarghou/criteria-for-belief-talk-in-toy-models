---
id: r-diversity-sweep
type: run
phase: 1
status: drafted
depends_on: [{node: c-training, edge: needs}, {node: c-substrate, edge: needs}]
produces: checkpoints, logs
---

## Purpose

Powers of two from 16 to 4096 under the prediction objective, to locate the memorization/generalization boundary and select the operating point.

## Content

Under the Phase B (opponent-prediction) objective, sweep pool size `N` over powers of two from 16 to 4096, at rung 1, with trajectory multiplicity `m` dropped (`c-substrate`: pre-generated fixed trajectories per policy, replayed rather than freshly sampled).

**Purpose is selection, not measurement.** A fixed pool of, say, 4096 may sit entirely inside the generalizing regime (`p-diversity-boundary`), in which case there is no memorization phase to transition out of and the developmental question (`s-transition-boundary`) is malformed. This run exists to locate the memorization/generalization boundary and select the operating point closest to it — where the competition between the memorizing and generalizing mechanisms is actually visible — **before** committing to a single pool size for `r-phase-b-main` and the Phase C runs. Do not skip this and pick a pool size by convention; it determines whether there is a transition to study at all.

Diagnostic to log: the train/test gap in mean return per round at each `N`. No gap at any `N` means no memorization phase exists in this substrate at this scale, which would need to be reported as a finding about the sweep, not quietly worked around by picking the smallest `N` and calling it done.

## Migration source

Protocol rev.2 §4. Reconciled R23 (drop trajectory multiplicity).
