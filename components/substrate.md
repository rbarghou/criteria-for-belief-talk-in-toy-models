---
id: c-substrate
type: component
status: drafted
depends_on: [{node: c-terminology, edge: needs}]
provides: game, opponent space, tokenization, episode structure
---

## Purpose

The generalized game and the full opponent policy space, with its degenerate subspaces named. Built once for the general case; Experiment 1 draws only from the zero-reactivity subspace.

## Content

### The game

Generalized Rock-Paper-Scissors with `n` actions, `n` odd. Actions are integers `0..n-1`. Action `a` beats action `b` iff `(a - b) mod n` lies in `1..(n-1)/2`. For `n = 3` this is standard RPS: `a` beats `b` iff `(a - b) mod 3 == 1`.

Outcome of playing `a` against opponent action `b`: `+1` if `(a-b) mod n` in `1..(n-1)/2`; `-1` if `(b-a) mod n` in `1..(n-1)/2`; `0` if `a == b`.

Phase 1 uses `n = 3`. `n` is a configuration parameter; larger odd `n` (5, 7, 9) is used only for `r-larger-n` (tooling validation — the cyclic signature is too thin at n=3 to be recognizably right or absent on its own).

### The opponent policy space — the 9×3 joint-state family, built once

The full opponent conditions on the pair (its own last action, the player's last action). This is a 2×2 lattice over which state variables it conditions on:

| Conditions on | Name | Contains |
|---|---|---|
| both | rung 1.5 | reactive opponents |
| its own only | **rung 1** | the phase-1 baseline family |
| the player's only | rung 1′ | "natural responders" — beat what the player just played |
| neither | rung 0 | i.i.d. opponents |

Three structural facts about this lattice, load-bearing for later phases even though phase 1 only uses one cell:

- **Rung 1′ contains the natural responders**, where rung 1 contains only opponents modeling themselves.
- **Rungs 1 and 1′ have complementary sufficient statistics** — one needs the opponent's own history, the other the player's — matched in difficulty by construction. This is the instrument behind `s-counting-vs-retrieval`'s phase-2 extension (`s-counting-vs-retrieval` migration note; the double dissociation itself is `catalogue/prior-art` / phase-2 study material, not yet a phase-1 node).
- **The reactivity latent is exact.** Model selection among the four pooling patterns has closed-form Dirichlet-multinomial evidence.

**Phase 1 draws only from rung 1 — the zero-reactivity subspace where the opponent ignores the model entirely.** This preserves the exact Bayes ceiling (§ below) and exact greedy optimality. Building the engine, sampler, tokenizer, and solver for the general joint-state case, then restricting the *pool* for phase 1, means phase 2 (reactive opponents) widens the pool rather than rebuilding — no duplicated engineering.

**Rung 0 (i.i.d.).** The opponent samples each action independently from a fixed categorical distribution `p`, drawn per episode from a symmetric Dirichlet with concentration `α`. Sufficient statistic: a single count vector of length `n`. No row selection. Used to isolate the counting problem from the row-selection problem (`s-counting-vs-retrieval`).

**Rung 1 (first-order Markov — the phase-1 baseline).** Opponent policy is an `n × n` row-stochastic matrix `P`, `P[i][j]` = probability of playing `j` given its own previous action was `i`. First action uniform. Sampled at episode start, never revealed. Rows drawn independently from a symmetric Dirichlet with `α = 0.5`. This family covers the interesting cases as special points: near-uniform rows give an unexploitable opponent (`c-inst-grounded` task-level null); permutation-like matrices give cyclers; a collapsed matrix gives a constant player (task-level floor); asymmetric rows give biased-frequency players.

Rung 1 layers two problems: maintaining `n` count rows, and gathering the row indexed by the opponent's most recent action. Rung 0 removes the second, which is why running both tells you which of the two a transition is about.

### Family scheme (governs pool construction generally, phase 1 and beyond)

A *family* is a set of constraints on regions of the joint-state matrix, not a list of individual opponents — sampling within a family is continuous and unbounded. Axes: **reactivity** (how much the rows sharing an opponent-last-action differ as the model's move varies — zero at rung 1 by construction) and **concentration** (how peaked each row is). A finite pool of individually-named opponents was considered and rejected: it yields a posterior over identity rather than over a parameter, which is a type-recognition / memorizing task by design, not the inference task this substrate is meant to pose.

### Action channel — two variants run as a pair (phase 1), a third named for later comparison

**Variant A (action only).** The model emits one action each round; payoff equals the outcome. The optimal policy is `argmax` of expected outcome (`c-solvers`), which depends only on the *sign structure* of the posterior, not its magnitudes — a model can reach the ceiling representing only a coarse partition of belief space.

**Variant S (single stake).** The model emits an action `a` and a stake `s` from a discrete grid. Payoff is `s · outcome(a, b) − λ · s²`. Optimal stake `s* = clip(edge / (2λ), grid)` — proportional to the **edge**, not the decision margin (these were conflated in the original protocol; see `c-terminology`). A 4-point grid `{0, 1, 2, 3}` is sufficient, with `λ` chosen so `s*` spans the grid over the empirical edge distribution.

**Variant S-full (stake vector).** Single-stake S reveals only argmax plus edge, leaving one degree of freedom of the predictive behaviourally invisible. Allocating a stake to *each* action, with quadratic cost summed across the vector, makes the optimal allocation proportional to each action's expected outcome — for n=3 this determines the predictive uniquely. Strictly proper elicitation of the whole belief. Single-stake S is retained as a named intermediate specifically so the three-way comparison A / S / S-full isolates argmax, argmax-plus-edge, and full posterior respectively.

**The A/S/S-full comparison is a primary result** (`s-representation-vs-demand`), not a robustness check — direct evidence, if it holds, that internal representation is shaped by what behaviour demands rather than by what the task's generative structure contains. It is confounded by training signal (`c-terminology` cross-reference; full statement in `s-representation-vs-demand`).

### Episode

- Sample or retrieve the opponent policy.
- Play `K = 64` rounds.
- Each round: the model emits its action (and stake, under S/S-full); the opponent's action for that round is then revealed. **No-leak requirement:** the opponent's round-`t` action must not be visible at the position where the model emits its round-`t` choice — a one-position leak makes the task trivial while every curve still looks normal. This must be asserted by a round-trip test, not just implemented correctly once.
- Episode return is the sum of per-round payoffs.

Because the model is causal and loss applies at every action position, a single 64-round episode contains every prefix length from 1 to 64. All prefix-length analyses (`s-causal-structure` dose-response) read off round index `t` within this fixed length and are therefore in-distribution. **Do not vary `K` to obtain a dose-response curve** — that confounds the measurement with positional out-of-distribution degradation under learned positional embeddings (the rev.-1 mistake this design corrects).

### Trajectory pre-generation and pool

The opponent's trajectory at rung 1 is exogenous — it depends only on the opponent's own previous action, never on the model's — so it can be pre-generated in full, with a recorded seed, and replayed rather than sampled fresh during training (common random numbers; reproducibility and a finite training set).

Two memorization knobs originally proposed:

- `N` — pool size (data diversity): number of distinct opponent policies.
- `m` — trajectory multiplicity: at `m = 1` the training set is `N` fixed sequences, memorizable outright; as `m → ∞` you recover fresh sampling and nothing is memorizable.

**`m` is dropped for phase 1.** At rung 1, memorization pressure is fully supplied by pool size `N` alone; pre-generating full trajectories per policy and replaying them is sufficient. (`m` becomes relevant again only at reactive rungs, where — per the phase-2 design — pre-generation shifts to the opponent's *randomness table* rather than its trajectory, since the trajectory there depends on the model's own choices. That is phase-2 material; noted here because it is the reason `m` is named at all in the source protocol.)

**Sweep `N` as the primary knob** (`r-diversity-sweep`, `s-transition-boundary`), powers of 2 from 16 to 4096, before committing to a single pool size for the main runs. See `p-diversity-boundary` for why this is expected to matter and where the boundary is expected to sit.

**Primary split.** 50/50 over policies. Training episodes draw only from the train half; evaluation only from the test half. Record all seeds.

**Secondary split (after the primary result exists).** Hold out a geometric region of policy space — e.g. all matrices where row 0 assigns probability greater than 0.6 to action 0. The held-out opponents are the *most exploitable* ones, so a generalization failure here shows up as failure on the easiest cases — a legible signature, not an ambiguous one.

### Tokenization

**Baseline (phase 1): opponent tokens only.** The model's own actions carry no information about the opponent's process at rung 1 — they are a pure distractor that also doubles sequence length. Context is the opponent's action history alone. Vocabulary `n + 1`: `OPP_0 .. OPP_{n-1}` plus `BOS`. For n=3, K=64: vocabulary 4, sequence length 65. The model emits its action at each position from a separate action head; the sampled action is not fed back into context.

Under variant S/S-full, the action head emits a joint `(action, stake)` categorical, or (preferred) two heads with a shared residual read — this makes the stake separately decodable.

**Variant SELF (later ablation).** Interleave the model's own actions as distinct tokens: `BOS, SELF_a0, OPP_b0, SELF_a1, OPP_b1, ...`. Vocabulary `2n+1`, length `2K+1`. Whether the added distractor changes the solution is worth knowing but is not the phase-1 default.

**Variant SHARED (later ablation).** Single action alphabet, role inferred from position parity. Whether the model learns parity is itself of interest.

**Self-action tokens become mandatory, not optional, once the loop closes (phase 2).** At a reactive rung the model's own last action is half the index into the row about to be used, and its action history is what lets past observations be attributed to rows — without it, inference is impossible there. Vocabulary becomes `2n+1`. Noted here because it is a structural consequence of the substrate design, not a phase-2 implementation detail: the same move that closes the loop forces the self-model channel open.

Loss and policy-gradient updates apply only at action-emission positions.

## Migration source

Protocol rev.2 §3, §4, §5. Reconciled R1, R3, R20 (four-corner lattice, as the space definition only), R21 (family scheme), R23 (common random numbers), R25 (tokenization variants).
