# Migration checklist

Content moves from four source documents into the skeleton. Nothing is deleted from the sources; they are frozen as history.

**Sources**
- `P` = `rps-belief-circuit-baseline-protocol-2026-09-19.md` (rev. 2)
- `R` = `rps-belief-circuits-amendments-reconciled-2026-09-22.md`
- `O` = `belief-circuits-program-orientation-2026-09-19.md`
- `Q` = `rps-belief-circuits-questions-register-2026-09-19.md`

Mark each line when the content has landed **and** been read back against the source.

## Protocol rev. 2

| Source | Destination | Done |
|---|---|---|
| P §1 (question, belief definition, why this substrate) | `program/orientation.md` + `components/terminology.md` | ☐ |
| P §1 (three motivating problems) | `program/orientation.md` | ☐ |
| P §2 (scope, three structural facts) | `catalogue/phases.md` + `components/substrate.md` | ☐ |
| P §3.1 (game) | `components/substrate.md` | ☐ |
| P §3.2 (opponent ladder) | `components/substrate.md` | ☐ |
| P §3.3 (action channels) | `components/substrate.md` + three `r-phase-c-*` runs | ☐ |
| P §3.4 (episode) | `components/substrate.md` | ☐ |
| P §4 (pool, splits, diversity) | `components/substrate.md` + `r-diversity-sweep` | ☐ |
| P §5 (tokenization) | `components/substrate.md` | ☐ |
| P §6 (solver) | `components/solvers.md` + `r-solver-verification` | ☐ |
| P §7 (model) | `components/training.md` | ☐ |
| P §8 (phase ladder, seeds, checkpointing) | `components/training.md` + the run nodes | ☐ |
| P §9.1 (transition) | `s-transition-boundary` | ☐ |
| P §9.2 (decodability) | `components/instruments-derived.md` + `s-decodability-timing` | ☐ |
| P §9.3 (usage) | `s-rationalizability`, `s-crit-residual`, `s-representation-vs-demand` | ☐ |
| P §9.4 (group structure) | `s-tooling-validation` + `r-larger-n` | ☐ |
| P §9.5 (interventions) | `components/instruments-grounded.md` + `s-causal-structure` | ☐ |
| P §10 (controls) | `components/instruments-derived.md` + `components/instruments-grounded.md` | ☐ |
| P §11 (build order) | superseded by `generated/orders.md`; the gates move to run nodes | ☐ |
| P §12 (can and cannot) | `program/orientation.md` + per-study limits | ☐ |
| P §13 (terminology) | `components/terminology.md` | ☐ |
| P §14 (extension path) | `catalogue/phases.md` (phase 3) | ☐ |
| P §15 (deferred axes) | `program/orientation.md` §6.4 — already consolidated there | ☐ |
| P §16 (prior art) | `catalogue/prior-art/*` | ☐ |
| P §17 (open questions) | `records/questions.md` | ☐ |

## Reconciled amendments

| Source | Destination | Done |
|---|---|---|
| R1, R3, R20–R21, R23, R25 (substrate) | `components/substrate.md` | ☐ |
| R2, R8, R24 (solver, scalars, ladder) | `components/solvers.md` | ☐ |
| R4, R5, R12b (training, seeds) | `components/training.md` | ☐ |
| R6, R7, R12, R14, R15, R31 (instruments) | `components/instruments-derived.md` | ☐ |
| R11, R13, R14 (grounded side) | `components/instruments-grounded.md` | ☐ |
| R9, R10 (vocabulary) | `components/terminology.md` | ☐ |
| R16 (deliverable, methodological limits) | `program/orientation.md` | ☐ |
| R17 (build order) | `generated/orders.md` + run-node gates | ☐ |
| R18 (A-vs-S confound) | `s-representation-vs-demand` | ☐ |
| R19 (curriculum) | `r-curriculum` + `s-belief-persistence` | ☐ |
| R29, R30, R32, R33 | `s-tooling-validation`, `catalogue/phases.md` | ☐ |
| R22, R26, R27, R28 (phase 2) | phase 2 stubs — create when phase 2 opens | ☐ |
| R Part 4 (open decisions) | `records/decisions.md` + `records/questions.md` | ☐ |

## Orientation and questions

| Source | Destination | Done |
|---|---|---|
| O §1–§5 | `program/orientation.md` (mostly in place) | ☐ |
| O §6 (option space, axes, dependencies, minimal coordinates) | `program/orientation.md` | ☐ |
| O §6.6 (tool validity), §6.7 (training history) | `program/orientation.md` | ☐ |
| O §7 (recorded positions) | `program/orientation.md` + `components/terminology.md` | ☐ |
| O §8 (open strategic questions) | `records/questions.md` | ☐ |
| Q1, Q2 | `records/questions.md` | ☐ |
| Q reiterate list | `components/terminology.md` | ☐ |

## Revision passes

1. **Completeness.** Walk every source section against the table; nothing unmapped.
2. **Read-back.** For each destination, read it cold and check it says what the source said — especially the caveats, which are the easiest thing to lose and the hardest to reconstruct.
3. **Contradiction sweep.** Re-run the reconciliation check across the new files; the split into many documents creates fresh opportunities for drift.
4. **Graph check.** Regenerate `generated/orders.md`; confirm no cycle, and confirm every study's grounding field matches its actual ancestry.
5. **Primary-outcome audit.** Every study has exactly one, stated in one sentence, and fixed before the run it consumes is executed.
