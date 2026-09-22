# Belief Circuits — repository skeleton

**Created:** 2026-09-22. Structure only; content migration pending (see `MIGRATION.md`).

## Why it is shaped this way

The earlier documents conflated two different things under the word "experiment": a **run**, which is a configuration that costs compute and produces checkpoints, and a **study**, which is a question with exactly one pre-registered primary outcome. The relation between them is many-to-many. Separating them is forced rather than aesthetic: pre-registration requires one primary outcome per study, so a single document carrying fourteen primary outcomes against one body of data is a fishing licence however carefully each claim is worded.

Separating them also made three things visible that were not:

- **Risk was hidden.** `s-transition-boundary` can simply fail, and if it does, six other studies lose their footing. It was previously step 5 of a 12-step build.
- **Sequencing was wrong.** Tooling validation sat at step 11, after every study depending on the tooling had run.
- **The deliverable was buried.** The program says what transfers is the *criteria*; the criteria studies were step 10 of 12, and one of them needs a training run nobody had budgeted for (`r-multiconsumer`).

## Layout

- `program/` — why the program exists and what counts as a result. Governs everything below.
- `components/` — shared engineering and vocabulary. Built once, used by many runs. The split between `instruments-grounded` and `instruments-derived` is structural, not editorial: it is what makes the acyclicity check computable.
- `catalogue/runs/` — configurations. Each declares the components it needs.
- `catalogue/studies/` — questions. Each declares one primary outcome, the runs it consumes, and the claims it presupposes.
- `catalogue/prior-art/` — imported claims, each with a confidence marker, so contestation propagates to whatever rests on it.
- `catalogue/phases.md` — which studies belong to which pass. Phase membership is a field on each study; this is the readable view.
- `records/` — decisions, questions, and the frozen amendment history.
- `generated/` — computed, never hand-edited.
- `tools/dag.py` — regenerates `generated/orders.md`.

## The three graphs

Studies depend on studies (epistemic), studies depend on runs (material), runs depend on components (engineering). Composed, they give a computable task order — but **two** orders, not one. The epistemic edges constrain what can be *claimed*, not what can be *started*; collapsing them would serialise work that could run in parallel.

Edge types, because they fail differently:

| Edge | Meaning | On failure of the source |
|---|---|---|
| `needs` | material or engineering | target cannot run |
| `presupposes` | epistemic, fatal | target is meaningless |
| `calibrates` | epistemic, non-fatal | target's conclusion moves |
| `enables` | epistemic, instrumental | target's instrument is unvalidated |

## The grounding question

Some instruments owe nothing to any fitted decoder: behavioural scoring, ablation effects measured behaviourally, attention patterns read off rather than fitted, and the solver verified by Monte Carlo. Others require a learned decoder: probes, decodability, decoded-belief measures, the residual test.

The risk is circular validation — the tooling validating itself. Making this a graph turns that into a check rather than an assumption: does every path terminate in a node that owes nothing to the instruments under test? `generated/orders.md` answers it per study.

The honest characterisation is that this is **bootstrapping made explicit**. In phase 1 the grounded base is large, so probes can be calibrated against it and then extended to where grounded measurement is unavailable — a legitimate move, and an inductive one. At later coordinates the grounded base largely vanishes, and the same graph will show most of its roots removed. The four criteria are the proposed answer to that: they check internal consistency rather than agreement with a reference, which is what you do when calibration is no longer available. That is the program's central bet, and it can lose, because coherence is weaker than correctness.
