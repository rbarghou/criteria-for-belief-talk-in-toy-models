---
id: c-solvers
type: component
status: drafted
depends_on: [{node: c-substrate, edge: needs}, {node: c-terminology, edge: needs}]
provides: posterior machinery, reference ladder
---

## Purpose

Posterior, predictive, the three scalars, and the ladder of reference players. Verified by Monte Carlo against the generative process before anything else is built.

## Content

### Posterior

Each row of `P` has a symmetric Dirichlet prior with concentration `α` (sampler default `α = 0.5`; also support a mismatched-prior configuration for robustness checks). Let `c[i][j]` be the number of times, so far in the episode, that the opponent played `j` immediately after having played `i`. The posterior over row `i` is `Dirichlet(α + c[i][·])`.

**The sufficient statistic for prediction is the count matrix plus the current-state index** — not the count matrix alone. The count matrix is sufficient for inferring the policy, but predicting the next action requires also knowing which row to read. State it as: 9 numbers plus a 3-way index, at n=3.

**Probing distinction (feeds `c-inst-derived`):** the **maintained statistic** is the full count matrix `c` (all `n` rows — the model does not know in advance which row it will need next); the **action-relevant projection** is the single row indexed by the opponent's most recent action. Both are probe targets. Raw counts are confounded with elapsed time (their row-sum total across the matrix is exactly the number of rounds elapsed, so a probe can score well by reading the positional embedding rather than the belief) — split the target into **normalized counts** (posterior mean policy, the informative part, probed per row in clr coordinates) and **total evidence** (the trivial part, probed and reported separately). General principle: check every probe target for a component computable from position alone, and split rather than sum.

### Posterior predictive

Given the opponent's most recent action `i`:

```
q[j] = (α + c[i][j]) / (n·α + Σ_k c[i][k])
```

`q` has length `n`, sums to 1 (n-1 free numbers), and is the action-relevant belief state. Under rung 0, drop the row index: `q[j] = (α + c[j]) / (n·α + Σ_k c[k])`.

### Best response, and the three scalars

Expected outcome of playing action `a` against predictive `q`:

```
E[a] = Σ_{d=1}^{(n-1)/2} q[(a-d) mod n]  −  Σ_{d=1}^{(n-1)/2} q[(a+d) mod n]
```

For n=3: `E[a] = q[(a-1) mod 3] − q[(a+1) mod 3]`.

- **Best response:** `argmax_a E[a]`.
- **Edge** = `max_a E[a]` — the value available; governs the optimal stake.
- **Decision margin** = `max_a E[a] − second-max_a E[a]` — governs whether a model–reference disagreement is meaningful. (These two were conflated as "exploit margin" in the original protocol; see `c-terminology`.)
- **Evidence** = row sum of posterior concentrations for the relevant row — how well-established the belief is.
- **Optimal stake (variant S):** `s* = clip(edge / (2λ), grid)` — tracks the edge, not the decision margin.
- **Optimal stake vector (variant S-full):** allocation proportional to each action's `E[a]`.

### The reference ladder

Phase 1 needs only the first two rungs, since greedy best-response to the exact posterior is *exactly* optimal against an opponent that cannot react to the model (no exploration-exploitation tradeoff exists in this regime — information arrives exogenously and the decision problem factorizes into independent one-shot decisions given the belief). The full six-member ladder is specified here because it is needed once the loop closes (phase 2), and because building it once avoids a second design pass:

1. **Uniform random.**
2. **Posterior-greedy** (belief, no planning, no exploration) — this is the phase-1 ceiling.
3. **Certainty-equivalent** (belief and planning, no exploration; the posterior mean matrix makes this a finite MDP over 9 states solvable by backward induction).
4. **Thompson sampling** (explores in proportion to residual uncertainty).
5. **Information-directed sampling** (explicit regret-versus-information tradeoff; see `p-exploration-references`).
6. **Omniscient optimal** (unachievable bound).

Gaps between adjacent rungs decompose into planning value, exploration value, and cost of ignorance. **At phase 1 (opponent cannot react), rungs 4–6 collapse onto rung 2**: explore/exploit balance is an output of the value function, not a tunable parameter, and there is no continuation value to an action beyond its immediate payoff when the opponent cannot respond to it. Rungs 3–6 become load-bearing only at reactive rungs, where they are needed because exact Bayes-optimal play over the continuous 27-dimensional belief space is intractable in closed form, and "fraction of ceiling" (`s-transition-boundary`) stops measuring inference quality alone once planning and exploration value are mixed in.

### Verification requirement — hard gate

Before training anything: verify the solver by Monte Carlo. Sample a known policy, generate long opponent sequences, confirm the posterior predictive converges to the true row distributions at the expected rate, and confirm best response and optimal stake against brute-force expected-payoff evaluation over the discrete grid. Add: **the posterior with zero observations must equal the prior** exactly (not just approximately, as a unit test). **Do not proceed until this passes** — see `r-solver-verification`.

## Migration source

Protocol rev.2 §6. Reconciled R2, R8, R24 (six-member ladder; Experiment 1 needs only the first two rungs, since greedy is exactly optimal against an agnostic opponent).
