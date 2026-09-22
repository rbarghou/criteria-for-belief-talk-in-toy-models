---
id: s-representation-vs-demand
type: study
phase: 1
status: drafted
primary_outcome: Which probe targets are decodable under each action channel: action only, single stake, stake vector.
grounding: derived
depends_on: [{node: r-phase-c-action, edge: needs}, {node: r-phase-c-stake1, edge: needs}, {node: r-phase-c-stakevec, edge: needs}, {node: s-decodability-timing, edge: enables}]
---

## Purpose

Designated primary result. Confounded by training signal; may bound rather than identify.

## Content

Compare `c-inst-derived` decodability results across `r-phase-c-action`, `r-phase-c-stake1`, and `r-phase-c-stakevec`: which of the four probe targets is decodable under each action channel.

**Designated primary result.** If the full posterior is linearly decodable under S-full and only its argmax under A, that is direct evidence internal representation is shaped by what behaviour demands rather than by what the task's generative structure contains — the sharpest available operationalization of "representation trails function" in this design (`program/orientation.md` §5).

**Named confound, not swept under the primary-result label (R18).** The stake-vector payoff gradient carries information about the whole predictive at every round; variant A's gradient carries only which action paid. The channels differ in intended behavioural demand *and*, uncontrolled, in training signal — so a decodability difference may reflect S-full simply training better, not demand shaping representation. Mitigation, if the comparison is to identify rather than merely bound its effect: read decodability at equal fraction-of-ceiling rather than equal step count (using `s-tooling-validation`/`s-transition-boundary`'s ceiling definition), and construct a rich-gradient/poor-readout control if one can be built. **That control does not currently exist and no design for one has been proposed** (`records/questions.md`). Failing both, report in `program/orientation.md`'s methodological-limits terms that this comparison bounds the effect rather than identifies it — do not silently report it as identifying.

## Migration source

Reconciled R3, R18.
