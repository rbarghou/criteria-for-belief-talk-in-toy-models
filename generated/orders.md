# Generated orders and grounding report

*Regenerate with `python3 tools/dag.py`. Do not edit by hand.*

## Execution order

What can be started when. Only material and engineering edges. Everything in a layer can proceed in parallel.

**Layer 1** — `amendments-history`, `c-terminology`, `decisions`, `p-algorithm-multiplicity`, `p-cheap-talk`, `p-compositional-data`, `p-diversity-boundary`, `p-exploration-references`, `p-modular-arithmetic-circuit`, `p-probe-selectivity`, `p-statistical-induction-heads`, `phases`, `program`, `questions`

**Layer 2** — `c-inst-derived`, `c-substrate`

**Layer 3** — `c-solvers`

**Layer 4** — `c-inst-grounded`, `c-training`, `r-solver-verification`

**Layer 5** — `r-curriculum`, `r-diversity-sweep`, `r-larger-n`, `r-multiconsumer`, `r-phase-a-sanity`, `r-phase-b-main`, `r-phase-c-action`, `r-phase-c-aux`, `r-phase-c-stake1`, `r-phase-c-stakevec`, `r-seed-replication`

**Layer 6** — `s-belief-persistence`, `s-causal-structure`, `s-counting-vs-retrieval`, `s-crit-multiconsumer`, `s-crit-offmanifold`, `s-crit-pathindependence`, `s-crit-residual`, `s-decodability-timing`, `s-payoff-alone`, `s-rationalizability`, `s-representation-vs-demand`, `s-tooling-validation`, `s-transition-boundary`, `s-uniqueness`

*No cycle.*

## Validity order

What can be claimed when. All edge types. A study may execute early and remain uninterpretable until its epistemic ancestors land.

**Layer 1** — `amendments-history`, `c-terminology`, `decisions`, `p-algorithm-multiplicity`, `p-cheap-talk`, `p-compositional-data`, `p-diversity-boundary`, `p-exploration-references`, `p-modular-arithmetic-circuit`, `p-probe-selectivity`, `p-statistical-induction-heads`, `phases`, `program`, `questions`

**Layer 2** — `c-substrate`

**Layer 3** — `c-solvers`

**Layer 4** — `c-inst-grounded`, `c-training`, `r-solver-verification`

**Layer 5** — `c-inst-derived`, `r-curriculum`, `r-diversity-sweep`, `r-larger-n`, `r-multiconsumer`, `r-phase-a-sanity`, `r-phase-b-main`, `r-phase-c-action`, `r-phase-c-aux`, `r-phase-c-stake1`, `r-phase-c-stakevec`, `r-seed-replication`

**Layer 6** — `s-counting-vs-retrieval`, `s-crit-offmanifold`, `s-crit-pathindependence`, `s-crit-residual`, `s-rationalizability`, `s-tooling-validation`, `s-transition-boundary`

**Layer 7** — `s-crit-multiconsumer`, `s-decodability-timing`, `s-uniqueness`

**Layer 8** — `s-belief-persistence`, `s-causal-structure`, `s-payoff-alone`, `s-representation-vs-demand`

*No cycle.*

## Grounding report

For each study: whether its conclusion rests only on probe-free instruments, and which terminal ancestors it depends on. A study whose roots all lie outside the derived instruments is self-supporting; one that does not is leaning on a calibration.

| Study | Grounding | Terminal ancestors |
|---|---|---|
| `s-belief-persistence` | derived | `c-terminology`, `p-compositional-data`, `p-diversity-boundary`, `p-modular-arithmetic-circuit`, `p-statistical-induction-heads` |
| `s-causal-structure` | grounded | `c-terminology`, `p-compositional-data`, `p-diversity-boundary`, `p-modular-arithmetic-circuit`, `p-statistical-induction-heads` |
| `s-counting-vs-retrieval` | grounded | `c-terminology` |
| `s-crit-multiconsumer` | derived | `c-terminology`, `p-modular-arithmetic-circuit`, `p-statistical-induction-heads` |
| `s-crit-offmanifold` | derived | `c-terminology` |
| `s-crit-pathindependence` | derived | `c-terminology` |
| `s-crit-residual` | derived | `c-terminology` |
| `s-decodability-timing` | derived | `c-terminology`, `p-compositional-data`, `p-diversity-boundary`, `p-modular-arithmetic-circuit`, `p-statistical-induction-heads` |
| `s-payoff-alone` | derived | `c-terminology`, `p-compositional-data`, `p-diversity-boundary`, `p-modular-arithmetic-circuit`, `p-statistical-induction-heads` |
| `s-rationalizability` | grounded | `c-terminology` |
| `s-representation-vs-demand` | derived | `c-terminology`, `p-compositional-data`, `p-diversity-boundary`, `p-modular-arithmetic-circuit`, `p-statistical-induction-heads` |
| `s-tooling-validation` | derived | `c-terminology`, `p-modular-arithmetic-circuit`, `p-statistical-induction-heads` |
| `s-transition-boundary` | grounded | `c-terminology`, `p-diversity-boundary` |
| `s-uniqueness` | derived | `c-terminology`, `p-algorithm-multiplicity`, `p-modular-arithmetic-circuit`, `p-statistical-induction-heads` |

## Imported claims and their dependents

Contested prior art propagates to everything below it.

- `p-algorithm-multiplicity` (CONTESTED in both directions; the dispute is itself the finding, and it makes equivalence-class size level-relative) → `s-uniqueness`
- `p-cheap-talk` (settled theory; phase 3 relevance) → *nothing yet*
- `p-compositional-data` (settled mathematics) → `s-decodability-timing`
- `p-diversity-boundary` (single recent paper; not independently replicated; load-bearing for the whole diversity-sweep approach) → `s-transition-boundary`
- `p-exploration-references` (settled; phase 2 relevance) → *nothing yet*
- `p-modular-arithmetic-circuit` (CONTESTED — see p-algorithm-multiplicity) → `s-tooling-validation`
- `p-probe-selectivity` (well established) → *nothing yet*
- `p-statistical-induction-heads` (well established) → `s-tooling-validation`
