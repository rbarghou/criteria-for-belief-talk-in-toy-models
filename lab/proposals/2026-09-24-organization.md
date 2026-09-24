# Lab Manager proposal: how this repository takes in, builds, runs, and reports work

**Date:** 2026-09-24 · **From:** Lab Manager · **Status:** proposal. Nothing here is adopted. The only change to the repository is this file, on a feature branch.

**Readers.** Ramsey (all). Process Manager (§1–3, §5, §9–10). Backlog Custodian (§3.4). Research Manager (§4.4, §8, Appendix B).

**Revision 2 (same day).** §5 is rewritten. It now covers how the codebase itself is managed (architecture, interfaces, testing, keeping `main` healthy) and how coding agents are briefed, supervised, reviewed, and learned from. Summary item 8, §2, §8, §10 and Appendix A are updated to match, and Appendix C (the work-order template) is new.

---

## 0. Summary

The repository today is a careful **epistemic** structure (what the program claims and what depends on what) with no **work** layer (what has been asked of engineering) and no **execution** layer (what was built and run, from what, at what cost). This proposal adds the two missing layers as thinly as I can make them, and says who writes what.

The moves, in one screen:

1. **Three layers; references point upward only.** Requests cite graph nodes; job records cite requests and nodes. Graph nodes never cite requests or jobs, so the epistemic structure stays free of scheduling. This is the "scheduler" that `schema.md` already set aside as a separate concern.
2. **One file per promoted request**, in `requests/`, with the promoted text kept **word for word** and kept apart from my engineering restatement. The Backlog Custodian checks the one against the other on a single generated page (`generated/requests.md`) in the public repo.
3. **Acceptance criteria are committed before the work they judge runs.** Git history is the timestamp. This is the program's own pre-registration rule, applied to engineering. It is what lets the stakeholder side trust a result without needing to know how it was produced. Criteria I had to invent are tagged `[proposed]`, never passed off as the requester's.
4. **Results come only from reviewed code on `main`**, executed by the Lab Manager. Each execution leaves a job record: commit, config, seeds, environment, cost, output hashes. Other sessions build and test; they do not produce results.
5. **Authority is cited, not assumed.** Any change in meaning to `program/`, `components/`, `catalogue/`, or `records/` cites a request or a dated relayed decision. That is how a research-side decision becomes a repo edit without me becoming its uncredited author.
6. **The repository is the Lab Manager's memory.** This chat is lossy: context gets compacted and the container gets reclaimed. So my operating rules, cost policy, and record of environments live in `lab/`. `CLAUDE.md` carries the rules every coding session must follow, because it is the one file every session reads automatically.
7. **Infrastructure is decided by the first request that needs it.** Each deferred decision has a named trigger and a current lean. Only one is decided now: code goes in a single installable package, not loose scripts. Reversing that later costs the most, because every delegated session would otherwise invent its own layout.

8. **I maintain the code; agents contribute to it under a written contract.**
   - Modules mirror the graph's components, and imports may only follow its `needs` edges. The grounding firewall becomes a CI check.
   - Public interfaces between modules are mine to change. That is what lets agents work in parallel safely.
   - For delegated work I write the acceptance tests first. The agent makes them pass without editing them.
   - I verify every PR myself — contract, full test run, adversarial read — before it reaches `main`.
   - Lessons from each delegation are written back into the rules.

The overhead per request is: I write one file, mostly pasted text plus criteria. A status line changes as work proceeds. A delivery section is filled in at the end. The Custodian reads one page. That is all of it.

---

## 1. Principles

Everything below follows from these. If a later rule contradicts one of them, the rule is wrong.

| # | Principle | The failure it prevents |
|---|---|---|
| P1 | References point upward only: execution → work → epistemic. | Scheduling state leaking into the claim structure. Nodes rotting as statuses get hand-edited. |
| P2 | If it isn't in the repo, the Lab Manager doesn't know it. | Knowledge lost when context is compacted or a session ends. A successor Lab Manager can't take over. |
| P3 | One writer per kind of state. | Concurrent sessions silently corrupting shared files (see §5). |
| P4 | Criteria are committed before the work they judge runs. | Verification whose criteria were picked after seeing results. |
| P5 | Authority is cited, not assumed. | Scientific content changing through engineering edits nobody decided. |
| P6 | Infrastructure is added when a request needs it, never before. | Ceremony and a stack chosen before the problem is known. |

---

## 2. What the repository would look like

```
CLAUDE.md                  NEW  rules every coding session reads automatically (draft: Appendix A)
README.md, schema.md       existing; schema.md gains the request and job-record fields
program/  components/      existing, unchanged: the epistemic layer
catalogue/  records/       existing, unchanged
history/                   existing, frozen
requests/                  NEW  work layer: one file per request (example: Appendix B)
lab/
  README.md                NEW  Lab Manager operating manual: intake, delegation, execution, cost policy
  environments.md          NEW  what exists: environments, services, how credentials are provided (never their values)
  decisions.md             NEW  engineering decisions, plus deferred decisions with their triggers
  proposals/               NEW  engineering proposals to the stakeholder side (this is the first)
tools/dag.py               existing; gains validation and generates requests.md (§7)
generated/                 existing; gains requests.md (the Custodian's page) and, later, job status
.github/workflows/         NEW  CI: regenerate and fail on any difference or error; run tests once code exists

created by the first request that needs them, not before:
pyproject.toml  uv.lock  src/belief_circuits/  tests/     with the first code request (the solver, Appendix B)
configs/                                         with the first run configuration
jobs/                                            with the first execution whose output is claimed as a result
```

The code layout, its import rules, and how it is kept healthy are covered in §5, Part A.

---

## 3. The work layer: requests

### 3.1 Intake

A promoted request reaches me the only way anything does: Ramsey relays it. From the stakeholder side I need only three things:

- a stable **reference** of any form (recorded exactly as given);
- its **kind** (`build` or `build-and-deliver-results`);
- the **text**.

If the kind is missing, I infer it and tag it `[proposed]`. There is no other template.

I then write `requests/req-NNNN-<slug>.md`. Numbering is sequential. That is safe because only the Lab Manager records requests (P3).

### 3.2 The request file

Front matter has seven fields, the same limit the node schema set itself:

```
id: req-0001
kind: build-and-deliver-results   # build | build-and-deliver-results
status: queued                    # queued | active | blocked | delivered | accepted | withdrawn
source: <stakeholder reference, verbatim>
promoted: 2026-09-25
serves: [c-solvers, r-solver-verification]   # graph nodes this work is for
needs: [req-0000]                             # other requests; same meaning as the graph's `needs`
```

Four sections follow.

1. **As promoted.** The relayed text, word for word. It is never edited, except to fix a transcription error, and that fix is logged.
2. **Engineering restatement.** What will be delivered and the checkable acceptance criteria. Each criterion is tagged `[from request]` or `[proposed]`. This section also records interface assumptions, stated as unverified where they are (Example C in the research candidates is the model case). It gives the file scope for any delegated work and, for results requests, the execution plan and a cost ceiling.
3. **Log.** Dated one-liners covering status changes, custodian findings, and relayed decisions.
4. **Delivery.** For `build`: what exists, how to use it, which tests show each criterion met, and any deviations. For `build-and-deliver-results`: see §4.3.

`delivered` is my last status. `accepted` is set only when Ramsey relays the stakeholder side's acceptance. A rejected delivery goes back to `active`, with the reason logged.

### 3.3 On the taxonomy

The two-kind contract covers what I was reaching for with my four-way split, so I'm not asking for more categories.

- "Design decision needed first" (the candidate examples D, E and F) is not a request kind. It is material that hasn't been promoted yet, and it should not reach me until it resolves into one of the two real kinds.
- "Process or documentation work" (G, H and I) is simply `build`, aimed at the repo instead of at code. The one real difference is which files it touches, and P5 already handles that by path.

One watch item: if requests start arriving that want an engineering *assessment* rather than an artifact — "what would the 30-seed run cost?" — we may need a third kind. I'm not proposing one until such a request exists.

Engineering work that originates with me goes into the same ledger, with `source: lab-manager`. That covers the skeleton itself, CI and the launcher. It keeps the Custodian's view complete. Anything that changes epistemic content or spends beyond the cost envelope still needs Ramsey's approval, and that approval is cited in the log.

### 3.4 What the Backlog Custodian reads and checks

Its entry point is `generated/requests.md` on `main` in the public repo. The page has one row per request: ID, source reference, kind, status, promoted date, title, and the nodes it serves.

The checks are:

1. every promoted item appears, with a matching reference and kind;
2. the *As promoted* text matches what was promoted;
3. the restatement neither adds untagged scope nor drops any;
4. the status matches what the stakeholder side believes.

Findings come back through Ramsey. I record each one in the request's log along with the correction.

Everything the Custodian needs is visible on `main`. That is why request bookkeeping should land on `main` promptly (§10, authorization a).

### 3.5 Research agents and the graph

Research agents never touch the repo, so "manipulating the DAG" arrives in one of two forms:

- a `build` request to edit nodes or edges, which is content and needs cited authority under P5; or
- a `build` request for a new generated view or check, which is tooling.

Generated views are the research side's read interface to the graph, and new ones are cheap.

---

## 4. The execution layer: code, jobs, artifacts, reports

### 4.1 Who runs what

- **Delegated sessions** build and test code on their own branches.
- **The Lab Manager** executes any job whose output will be claimed as a result, and only from a commit on `main`. That way the commit a result cites has been reviewed and cannot disappear the way a branch can. It also means every result has the same provenance shape and every paid execution passes through one set of cost controls (§6).

### 4.2 Job records (from the first execution)

`jobs/<job-id>/record.json` holds:

- the request and node(s) served;
- the git commit;
- the exact command and config;
- the seeds;
- the environment;
- start and end times, and status;
- cost;
- the outputs, each with a location, sha256, and size.

Small outputs (under about 5 MB of text, JSON or plots) are committed next to the record. Large outputs are recorded by manifest only; the bytes live in whatever store the artifact-storage decision picks (§6.4). Where an output can be regenerated deterministically, the generator, seed and hash are recorded instead of the bytes. The substrate's opponent pool is the obvious case: at most 4,096 policies from a recorded seed.

A job record is written **before** launch and finalized after, so a crash in the middle of a launch still leaves a trace.

### 4.3 What a results delivery contains

This is the Process Manager's "result plus enough methodology and provenance to evaluate the claim", in a fixed shape:

- **Result.** The answer, stated against each acceptance criterion: pass/fail or values.
- **Method.** What was run, in the stakeholder side's terms: sample sizes, tolerances, what was compared with what. No infrastructure detail.
- **Deviations.** Anything that differs from the request or its criteria, including criteria that were `[proposed]` and never confirmed. This section is where trust is earned or lost, so it is never left out and never softened.
- **Provenance.** Commit, job IDs, output hashes. Machine-level; the stakeholder side can skip it.
- **Reproduce.** One command.

### 4.4 Splitting the node `status` field (Research Manager please note)

Today `status` mixes two things. `stub`, `drafted` and `ready` describe how well resolved a node's content is. `running`, `done` and `stale` describe execution. The second group is typed in by hand, so it will drift from reality the day real jobs exist.

Proposal:

- The node `status` keeps only its conceptual meaning (`stub | drafted | ready`, plus `imported` for prior art, which 8 nodes already use though the schema never listed it). It is set only on cited authority.
- Execution state (`running`, `done`, `stale`) is computed from job records and appears only in generated views.
- `stale` propagation — which `schema.md` gives as the whole reason the graph exists rather than a notebook — becomes automatic once job records exist.

Whether a node is ready for engineering is then not a node field at all. It is ready when a promoted request with checkable criteria exists for it.

---

## 5. The codebase and the coding agents that work on it

I am the codebase's **maintainer**. Coding agents are **contributors**. I am accountable for three things:

- `main` is always green and always trustworthy;
- the architecture stays coherent as agents add to it;
- no agent's work reaches `main` without my having verified it myself.

The first half of this section is how the code is kept in shape. The second half is how I work with the agents who write most of it.

### Part A — Managing the codebase

#### 5.1 Architecture: modules follow components, and imports follow the graph

```
src/belief_circuits/
  substrate/      c-substrate   game rules, opponent sampling, pools, episodes, tokenization
  solvers/        c-solvers     posterior, predictive, scalars, reference ladder
  training/       c-training    model, objectives for each phase, loop, checkpointing, seeding
  instruments/
    grounded/     c-inst-grounded   behavioural scoring, ablations, attention read-offs
    derived/      c-inst-derived    probes, decodability, the four criteria
  jobs/           entry points: thin command-line wrappers that read a config, call the library, and write outputs
tests/            mirrors src/; acceptance tests live in tests/acceptance/<req-id>/
configs/          one file per run configuration, named after its run node (configs/r-phase-b-main/...)
```

The rules for this layout:

- **Imports only go in the direction the graph's `needs` edges point.** `substrate` imports nothing from the project. `solvers` may import `substrate`. `training` may import both. `instruments/derived` may import `instruments/grounded`, never the reverse. Nothing imports from `jobs/`.
- **A single test checks every import direction.** A cycle, or a grounded module reaching into derived, fails CI. This is the grounding firewall enforced in code.
- **The library is pure; side effects live at the edges.** Library functions take their inputs explicitly: random-number generators are passed in, and nothing uses a global seed or reads files or environment variables. Only `jobs/` touches disk, the network, or config files.
  - This keeps nearly everything testable on CPU in milliseconds.
  - It makes determinism checkable.
  - It means a job's recorded config really is its complete input.
- **A run node in the graph maps to a config directory, not to code.** Runs are configurations of the library (README: "a run is a configuration"). A new run should almost never need new library code. When it does, that fact is visible in the request.

#### 5.2 Interfaces between modules are owned and explicit

- The functions and data types one module exposes to another form its **public interface**. Each module's `__init__.py` names them, with type annotations.
  - Examples: `Episode`, `Pool`, `posterior_predictive`, `best_response`, `Model`, `Checkpoint`.
  - Everything else in the module is private and free to change.
- **Public interfaces are the Lab Manager's to change.** An agent may change a module's internals freely within its work order. If its task needs a public interface to change, it stops and proposes the change in its pull request (PR); it does not make the change.
  - This is the single rule that makes parallel agents safe.
  - Two agents can work in `substrate` and `training` at once because the seam between them is frozen while they work.
- **Interfaces are frozen by tests.** Each public interface has contract tests (types, shapes, invariants such as "tokenized episodes never expose round t's opponent action at round t's decision position"). Changing an interface means changing its contract test, which only I do, in its own PR, with a list of affected code.
- **An interface can be assumed before it exists.** When work is built against an interface that doesn't exist yet (candidate example C against B's episodes), I write the interface first, as types and a contract test with a stub. Both agents then build to that, and the assumption is checked by a test instead of being trusted.

#### 5.3 Testing: tiers, determinism, and acceptance tests as the contract

| Tier | What | When | Budget |
|---|---|---|---|
| Unit and contract | Every public function; every interface invariant | Every push, CI | Under 1 minute total |
| Exhaustive and property checks | Numerical code checked against brute force or known identities (the solver's exhaustive checks, Appendix B) | Every push, CI | Under 2 minutes |
| Smoke | Each job's entry point runs end to end on a tiny config: a few steps of training, a tiny pool, one checkpoint written and reloaded | Every push, CI | Under 3 minutes, CPU |
| Validation | Real-scale runs whose output is a result | Only as jobs (§4), by the Lab Manager | By cost envelope |

- **Determinism is tested, not hoped for.** For each job type, a test runs the same config and seed twice and checks the outputs are byte-identical on CPU.
  - GPU nondeterminism is recorded in job records where it occurs, never silently absorbed.
  - Without determinism, "the same run" can't be reproduced, and the program's claims about training history (`program/orientation.md` §6.7) can't be tested.
- **Acceptance tests are written before the work, by me, and are the contract.** For every `build` request with a delegated agent, the work order points at `tests/acceptance/<req-id>/`. I write those tests, and they fail, before the agent starts.
  - The agent's job is to make them pass without editing them.
  - CI flags any diff to an acceptance test that I didn't author.
  - This is P4 (criteria before work) applied to code. It is also the most effective single guard against the main failure mode of coding agents: redefining "done" to match what they built.
- **Every acceptance criterion in a request maps to a named test**, and the delivery section lists them. A criterion that can't be written as a test (rare, and mostly about results) is marked as checked by review, and I say how I checked it.

#### 5.4 Keeping `main` healthy

- **Always green.** Nothing merges with CI red. If `main` breaks anyway (a dependency release, an environment change), fixing it outranks all other work.
- **Minimal quality gates in CI:**
  - `ruff` for lint and formatting (one tool, no configuration debates);
  - the test tiers above;
  - `tools/dag.py` validation;
  - the import-direction test.
  - No type checker at first; annotations on public interfaces are required, and I'll add a checker if interface bugs start slipping through review.
- **Dependencies are locked and deliberate.** `uv.lock` is committed. Adding a dependency is a one-line entry in `lab/decisions.md` saying why. Agents may not add dependencies; they ask in the PR.
- **Small PRs, one purpose each.** Refactoring is never mixed into feature work: a refactor is its own PR with no change in behaviour, shown by unchanged tests.
- **The commit is the version.** There are no releases. When a job produces a reported result, its commit is tagged `result/<req-id>`, so the exact code behind any claim stays one click away even after `main` moves on.
- **Maintenance passes.** After every ~5 merged code requests, or before any phase's first paid training run, I do one pass: dead code, duplicated helpers, interfaces that have grown awkward, slow tests. It's recorded as a `source: lab-manager` request so it's visible. This is how architecture debt from many small agent contributions gets paid down on purpose instead of accumulating.
- **Documentation stays where readers already look.**
  - Each module's docstring names its node and its public interface.
  - The graph's component nodes remain the design documentation.
  - There's no separate docs tree. The node explains *why*, the code *how*, the request *what was asked and delivered*.

### Part B — Working with coding agents

#### 5.5 Which kind of agent, for which work

| Work | Who | Why |
|---|---|---|
| Epistemic content edits, interface changes, tooling, all result executions, reviews and merges | Lab Manager, directly | Needs authority, continuity, or paid credentials |
| Small, bounded code tasks (under ~an hour, one module) | A subagent inside my session, in an isolated git worktree | Cheapest to brief and verify; returns in-session; no separate environment |
| Substantial builds (a component, a pipeline, a scaffold) | A separate Claude Code cloud session, launched by me with the session tools (or by Ramsey by hand) | Runs in parallel for hours without consuming my context; has its own branch and PR |

**Concurrency:** I start with **at most two cloud agents at once**, raising the cap only once the review loop below is shown not to be the bottleneck. More agents than I can review adds risk, not speed.

#### 5.6 The work order: what an agent receives

The work order is a section of the request file (template: Appendix C). It is written so an agent that has read only `CLAUDE.md` and this one section can do the job. It contains:

1. **Goal.** One paragraph, in engineering terms, with a link to the graph node for context.
2. **Scope.** The exact paths the agent may create or modify. Everything else is read-only to it. CI on its PR flags any file changed outside scope.
3. **Interfaces.** The public interfaces it must *use* (frozen) and must *provide* (with their contract tests already in place).
4. **Acceptance tests.** The path to the failing tests it must make pass.
5. **Constraints.** Dependencies allowed, CPU-only, runtime budgets for tests, no paid compute.
6. **Out of scope.** What *not* to do, especially tempting adjacent work.
7. **Stop-and-ask conditions.** The agent stops, opens a draft PR, and writes its question there — it does not guess — if:
   - an acceptance test looks wrong;
   - it needs a public interface change or a new dependency;
   - a choice would change a research meaning (a threshold, a definition, a grid, a tie-breaking rule);
   - it's about to exceed scope.
   The rule is that research meaning is never decided by an agent.
8. **Definition of done.** All acceptance tests and CI pass, and a PR with the required description is open.

The launching prompt stays one line pointing at the work order. So the brief is versioned, visible to the Custodian, and identical no matter who starts the session.

#### 5.7 Launch, supervision, and questions in flight

1. **Prepare.**
   - I merge the acceptance tests and any interface stubs to `main` first.
   - I create the branch `req-NNNN-<slug>` from that commit.
   - The environment is ready from the first command: a session-start hook installs dependencies, so an agent never improvises its setup.
2. **Launch.** I start the session on that branch with the one-line prompt, and log the session link and branch in the request's Log.
3. **Supervise by events, not by polling.** I subscribe to the agent's PR. When it opens a draft with a question, pushes, or CI fails, I'm notified.
   - Engineering questions (inside my authority) I answer on the PR, so the answer lives with the code.
   - Questions about research meaning go to Ramsey as a relay. The request goes to `blocked` until the answer comes back. The agent's session is paused or closed; it is not left guessing.
4. **Stalls.** If an agent produces nothing reviewable within its expected time, or the same CI failure survives two attempts, I stop it and take one of two routes:
   - **Re-scope:** the work order was wrong or too big; split it.
   - **Take over:** finish it myself from its branch.
   Either way the Log records what happened, because repeated stalls on one kind of task are a signal about how I write work orders.

#### 5.8 Review: verify, never trust the summary

The agent's PR description is a claim, not evidence. Before merging, I:

1. **Check the contract held:**
   - acceptance tests are byte-identical to what I wrote;
   - no file outside scope changed;
   - no dependency was added;
   - no public interface changed without an approved proposal.
2. **Run everything myself**, on a fresh checkout of the PR branch, not relying on the agent's report or even only on CI. That includes the determinism test and each smoke test.
3. **Read the whole diff adversarially,** looking specifically for the failure modes coding agents actually have:
   - tests weakened or special-cased to pass;
   - errors swallowed;
   - silent fallbacks;
   - hard-coded values standing in for computation;
   - code that's more general than asked;
   - duplicated helpers that already exist elsewhere;
   - comments claiming behaviour the code doesn't have.
   I also use the code-review tooling as a second pass. It is not a substitute for my read.
4. **Check the research-meaning guard:** any constant, threshold or default in the diff that carries meaning must trace to the request, a node, or a relayed decision. An agent-invented one is a review failure even if every test passes.

**Outcomes:**

- **Merge.** Squash into one commit whose message cites the request. Then regenerate, set the request to `delivered` (for a `build`) or proceed to execution (for a results request), and close the session.
- **Rework.** Line comments on the PR. The same agent session resumes if it's still alive; otherwise a fresh one gets the branch plus the review comments as its brief.
  - **Two rework rounds maximum.** After that I re-scope or take over. A third round means the work order was the problem.
- **Reject.** The branch is closed with the reason logged. This is rare, and usually means the scope was wrong.

#### 5.9 Parallel agents without collisions

Parallel work is safe when four conditions hold together:

- work orders have **disjoint write scopes**;
- the seams between them are **frozen public interfaces** with contract tests;
- **shared files** (`pyproject.toml`, `uv.lock`, `CLAUDE.md`, `configs/` conventions, anything under `tests/acceptance/`) are Lab Manager–only;
- `generated/` is **never merged by hand**, only regenerated.

When two PRs are both ready, I merge them one at a time, re-running CI on the second after the first lands.

**The concurrency table (P3 made concrete):**

| State | Writer | How conflicts resolve |
|---|---|---|
| Request files, node content, node status, `jobs/` | Lab Manager only | None arise |
| Public interfaces, contract and acceptance tests, shared config files | Lab Manager only | None arise; agents propose changes in PRs |
| Module internals, new tests | Agents, within their work order's scope | Disjoint scopes; at merge, by the Lab Manager |
| `generated/` | The tool only | Regenerate; CI fails on any difference |

#### 5.10 Closing the loop: what agents teach the process

Every delegated request ends with a two-line entry in its Log:

- what went smoothly;
- what the agent had to ask about or got wrong.

When the same lesson shows up twice, it becomes a rule, in one of three places:

- `CLAUDE.md`, if every session needs it;
- the work-order template, if it's about briefing;
- `lab/README.md`, if it's about how I operate.

This is how the codebase's conventions accumulate in writing instead of in my head (P2). It is also the evidence for §9's simplification triggers: if agents rarely ask questions and rarely need rework, the work orders can get shorter.

**Token spend is cost too.** For mechanical tasks (a well-specified module with complete acceptance tests), I'll run agents on a smaller model and keep the larger model for design-heavy work and for my own reviews. The model used is recorded in the request's Log, so over time we learn which tasks need which.

---

## 6. Environments, credentials, cost

### 6.1 What exists today (checked 2026-09-24, read-only)

**Lab Manager's cloud container**
- Python 3.11 and `uv`, 4 CPUs, 15 GB RAM, no GPU.
- numpy, torch and pytest are not preinstalled.
- The disk is ephemeral: anything not pushed is lost when the container is reclaimed.

**Claude Code cloud environments**
- One environment exists ("Default").
- Sessions I create would run in it too.
- Whether they would inherit the RunPod access below has not been checked yet (§10, item d).

**RunPod** is the paid compute service in view.
- The API is reachable from this environment. The credential is injected by the network proxy; no key material exists in the container or the repo.
- The account is shared with at least one other project: one pre-existing storage volume, not ours.
- The account has a spend limit of 80, which I read as RunPod's cap on hourly spend rate in USD. The current burn, about $0.005/hr, matches storage for the existing volume, which is consistent with that reading.
- **A rate cap does not bound total spend.** A forgotten pod bills until someone stops it. The provider's control is necessary but not sufficient.

**GitHub**
- git push works.
- The GitHub tool connection has been intermittent in this session.
- No CI is configured.

This section becomes `lab/environments.md` and is kept current there.

### 6.2 The credentials decision (the Process Manager left this to me)

**Credentials are held at the environment level, never in the repo** (which is public) and never in code. Paid execution is routed through **one in-repo launcher module** rather than a separate build service.

The launcher is the "intermediate service" in miniature. It:

- enforces the cost envelope;
- sets a hard maximum lifetime on every paid resource;
- names every resource with a `bc-` prefix;
- writes the job record before launch.

A standalone build service would be more infrastructure than a few runs of a two-layer model justify, and the launcher's guarantees are testable code rather than intentions.

**Revisit** if more than one session ever needs to launch paid work at once, or if spend stops being small. **Build the launcher** with the first request that needs paid compute, not now.

### 6.3 Cost policy (goes into `lab/README.md`; the numbers are for Ramsey to set)

1. **CPU in the session container is the default.** It costs nothing extra. Candidate examples A, B, and the small-scale tests of C all fit. Paid compute is used only for GPU work or jobs estimated at over about 2 hours.
2. **Spending without asking** is allowed up to a proposed **$5 per job, $20 per request, and $50 per rolling 30 days** of paid compute for this project. Anything above that goes to Ramsey first, with an estimate. The Process Manager's intent — no per-run sign-off, rely on provider controls — holds inside the envelope.
3. **Every paid resource has a maximum lifetime set at launch** and is recorded before it starts.
4. **Every Lab Manager session begins with a sweep.**
   - List pods and endpoints.
   - Any `bc-` resource without a live job record is terminated, and the termination is logged.
   - Resources without the prefix belong to other projects and are **never touched**.
5. **No persistent storage volumes** until the artifact-storage decision is made, because storage bills continuously.
6. **Cost is recorded on every job record** and totalled in a generated view, so spend can be read from the public repo without anyone relaying it.

### 6.4 Deferred decisions and their triggers (goes into `lab/decisions.md`)

| Decision | Made when | Current lean |
|---|---|---|
| Package and dependency tooling | First code request | **Decided now:** one package (`src/belief_circuits`), `pyproject.toml`, `uv`, numpy, pytest |
| Deep-learning framework | First model code (C) | PyTorch with a plain training loop; no Lightning |
| Config system | C | Plain dataclasses plus config files; no Hydra |
| Orchestration of many seeds and phases | First sweep | A loop inside the launcher; no workflow engine |
| Experiment-tracking platform | First sweep; revisit at about 50 jobs | None: job records plus metrics files |
| Artifact storage | First large output that can't be regenerated | Open. Candidates: a RunPod volume (bills continuously, tied to one region), S3-compatible storage, Hugging Face Hub (the repo is public anyway) |
| Paid-execution launcher | First paid job | As in §6.2 |
| Session setup hook (installs deps for delegated sessions) | First delegation | Yes, once code exists |

---

## 7. Repairs to the existing tooling (part of the skeleton, no content changes)

`tools/dag.py` currently lets three kinds of error pass silently:

- **Files that should be nodes but have no front matter are skipped.** This is how the `history/` exclusion turned out to have never done anything; `records/decisions.md` has the entry.
- **Dependencies on unknown node IDs are dropped from the orders.** None exist today; a typo tomorrow would vanish without a trace.
- **Field values are not checked against the schema.** 8 prior-art nodes use `status: imported`, which the schema doesn't list.

**Fixes:**

- make each of these an error;
- legitimize `imported` for prior art;
- add CI that re-runs the tool and fails if `generated/` differs from what the source files produce.

This protects the grounding check, the one guarantee the whole structure is built around. Right now that check only fires if someone remembers to run the tool.

The tool stays stdlib-only. PyYAML is available, but it isn't needed until the front matter outgrows single-line values.

---

## 8. Proposed engineering priority

| Step | What | Who | Blocks |
|---|---|---|---|
| 0 | **Adopt the skeleton**: `CLAUDE.md`, `lab/`, `requests/` and its generated page, the §7 validation, CI. One PR, no experiment code, no content changes. | Lab Manager | Everything below |
| 1 | **Two small content decisions** (relayed): the gate semantics for example G, and correcting the reversed prose in `s-crit-multiconsumer` and `s-decodability-timing`. Can be one request. | Research side decides; Lab Manager edits | Building B and C in parallel with A |
| 2 | **Pilot: A** (solver plus verification). CPU only, $0. Also serves to calibrate this process: if intake, restatement, custodian check and delivery feel heavy on the simplest possible request, we cut before scaling. | Lab Manager, directly | Every graded result |
| 3 | **B and C in parallel**, as the first two delegations. Before launch I merge the episode/batch interface as types plus a contract test and stub (§5.2), and each request's acceptance tests. This step doubles as the trial of §5's agent process. | Two cloud agents; Lab Manager reviews and merges | First training runs |
| 4 | **Before the first paid training job**: the pre-registration document exists (example H; its content is research-side), the launcher refuses Phase B/C jobs until it is committed, and the artifact-storage decision is made | Research side writes; Lab Manager enforces | Phase B/C results |

D, E, F and I are research decisions. None of them is on the engineering critical path through step 4.

**My recommendation on G** (the decision is the research side's):

- **Where the gap is.** The graph's execution order doesn't distinguish *building* a component from *executing* a run. The two request kinds do, and G is exactly where that gap bites.
- **What the gate should block.** Executing anything graded against the solver — every training run — not building B or C.
  - B never calls the solver.
  - C calls it only for Phase A targets and for evaluation against the Bayes ceiling.
  - Building either before A passes risks rework if the solver's interface changes, but not invalid results.
- **How to encode it.** As a `needs` edge from each training-run node to `r-solver-verification`, with the launcher refusing those jobs until a passing verification job is on record. This keeps the prose's intent (nothing *runs* ungrounded) while letting three strands of building proceed at once.
- **What G was really asking.** The candidate-examples document asked whether tooling should enforce prose-stated hard constraints. My answer is yes, and the launcher is where execution gates get enforced mechanically from the graph.

---

## 9. Deliberately absent, and when to cut

In the spirit of `schema.md`'s own "what is deliberately absent":

- **No issue tracker or project board.** Files in git are the ledger, and the Custodian reads one page.
- **No priority, estimate, or owner fields on requests.** Priority is what Ramsey promotes and in what order. Engineering priority is argued in proposals like this one, not encoded in fields.
- **No tracking platform, config framework, workflow engine, or artifact store** until a trigger in §6.4 fires.
- **No handoff directory, inbox, or outbox.** This agrees with the Process Manager's position.
- **No approval gate between intake and work.** Custodian review is asynchronous. The only gates are the existing epistemic ones plus the cost envelope.
- **No description of stakeholder roles in the repo.** Those belong to the Process Manager.

**Cut first, if this is too much:**

1. If the Custodian finds no discrepancies over the first ~5 requests, drop the separate restatement check and keep the word-for-word text plus the criteria.
2. If requests turn out routinely tiny, allow several per file.
3. If delegating costs more than the work, stop delegating below that size.
4. If nothing reads job records by the time phase-1 runs are under way, fold them into the delivery sections.

**Add structure only if:**

- paid launches need to run concurrently;
- there are more than about 50 jobs, which would justify tracking; or
- there are more than about 20 open requests at once, which might justify a board.

---

## 10. What I need decided

**From Ramsey** (after Process Manager review, if their process requires it):

- **a. Standing authorizations.** Any of these can be withheld. The process still works, but it routes through you.
  1. Commit request bookkeeping directly to `main`.
  2. Merge reviewed PRs to `main` once CI is green.
  3. Create delegated coding sessions.
  4. Launch paid compute within the envelope.
- **b. The cost envelope numbers** (§6.3).
- **c. The Lab Manager continuity point.** If this chat is lost, a new session reading `lab/` should be able to resume the role. Please confirm that is the intent.
- **d. (Optional) A second cloud environment** without paid-service credentials for delegated sessions. I will check on the first delegation whether sessions inherit RunPod access. If they do, instruction-only restraint (Appendix A, rule 6) is weaker than simply not providing the credential.
- **e. Agent defaults** (§5.5–5.10). Please confirm or change:
  - at most two cloud agents at once;
  - a two-round limit on rework before I re-scope or take over;
  - a smaller model for mechanical tasks.
  Also: do you want to start agent sessions yourself sometimes? Either way works, since the brief lives in the repo.

**From the Process Manager:**

- confirmation of the three-item intake minimum (§3.1);
- confirmation that the Custodian's reading path in §3.4 matches its role;
- whether `[proposed]` criteria must be confirmed before a *free* execution, or only before a paid one. My default: execute, and disclose under Deviations.

**From the Research Manager:**

- G's semantics (§8);
- acknowledgement of the status split (§4.4);
- the spec questions that drafting Appendix B surfaced. They will come back properly when A is promoted; they are listed there so the RM isn't surprised.

---

## Appendix A — draft `CLAUDE.md` (read automatically by every coding session)

```markdown
# Working in this repository

This repo is the engineering side of the Belief Circuits research program; README.md explains the program and the graph.

## Your role
- Started with a pointer to `requests/req-NNNN-*.md`? You are a delegated engineer. Your assignment is that file's
  Work order; your scope is the paths it lists. Report problems in your PR; do not edit request files.
- Otherwise you are the Lab Manager: read `lab/README.md` first.

## Rules for every session
1. Never hand-edit `generated/`. Run `python3 tools/dag.py` and commit its output with the change that caused it.
2. `program/`, `components/`, `catalogue/`, `records/` change in meaning only with cited authority (a request ID or a dated
   relayed decision) in the commit message. Delegated sessions do not edit them.
3. The graph's rules are enforced by the tool; never work around a failure. Imports follow the graph: substrate <- solvers
   <- training; instruments/derived may import grounded, never the reverse; nothing imports from jobs/. A test checks this.
4. The repo is public: no credentials, tokens, account identifiers, or personal information, ever.
5. Acceptance criteria are fixed before the work they judge. Never edit anything under `tests/acceptance/`; if a test
   looks wrong, stop and say so.
6. Do not start paid compute. Only the Lab Manager executes jobs whose outputs are claimed as results, from `main`.

## Code conventions
- Library code is pure: RNGs are passed in, no global seeds, no file/env/network access outside `jobs/`.
- Public interfaces are what each module's `__init__.py` exports. Change internals freely within scope; propose, never
  make, public-interface changes.
- No new dependencies without asking. Run `ruff check`, `ruff format`, and `pytest` before pushing.
- Never set a meaningful constant (threshold, grid, default, tie-break) that isn't in your work order or a node. Ask.

## Delegated sessions: stop and ask
Open a draft PR with your question, and stop, if: an acceptance test looks wrong; you need an interface change or a new
dependency; a choice would change research meaning; or the work would leave your scope. Don't guess.

## Delivering (delegated sessions)
Open a PR to `main` titled `req-NNNN: <title>`. Description: what was built; for each acceptance criterion, the test that
shows it; deviations; open questions. Unverified interface assumptions from the Work order stay labelled as such.
```

---

## Appendix B — worked example: candidate example A as a request file

*Illustrative only. Nothing has been promoted. Example A's text from the candidate-examples document stands in for the promoted text.*

```markdown
---
id: req-0001
kind: build-and-deliver-results
status: queued
source: <stakeholder reference as relayed>
promoted: 2026-09-2x
serves: [c-solvers, r-solver-verification]
needs: []
---

## As promoted
> Confirm, by direct simulation, that the hand-derived Bayesian solver (posterior update, best response, decision margin,
> optimal stake) actually behaves as its closed-form formulas say it should, before anything downstream is allowed to
> treat those formulas as ground truth. [...]

## Engineering restatement
**Deliverable.** (1) `belief_circuits.solvers`: posterior, predictive, E[a], best response, edge, margin, evidence,
optimal stake (S) and stake vector (S-full), for general odd n; reference-ladder rungs 1-2. Also the part of
`c-substrate` the solver and its Monte Carlo need: game rules and the opponent-policy sampler. (2) The
`r-solver-verification` checks, executed, with a verdict per check.

**Acceptance criteria.** [from request] = stated in the request or its nodes. [proposed] = Lab Manager's, committed here
before execution, open to objection.
1. [from request] The posterior with zero observations equals the prior exactly. [proposed: exact rational equality,
   not a float tolerance.]
2. [from request] Best response, edge, margin, stake and stake vector match brute-force expected-payoff evaluation.
   [proposed: exhaustive, not sampled. At n=3, every row count vector reachable in a 64-round episode (45,760 vectors);
   at n=5 and 7, exhaustive up to 20 observations per row, sampled beyond. Best responses compared as sets of tied
   actions; real values to 1e-12 relative; stakes across a range of lambda.]
3. [from request] The predictive converges "at the expected rate". [proposed: the log-log slope of mean squared error
   against row-visit count is -1 +/- 0.05 over 10^2 to 10^5 visits, averaged over 1,000 policies drawn from the prior.]
4. [proposed; adds a check the source does not name] Calibration. With policies drawn from the prior, the posterior's
   50% and 90% credible intervals cover the true row probabilities at their nominal rates, within Monte Carlo error.
   Why: every consistent estimator converges, so check 3 would pass for a wrong posterior (the wrong alpha, for example).
   Calibration is what checks that it is *the* posterior.

**Interface.** Nothing upstream. Downstream, B and C import `solvers` and `substrate.game`; their signatures become an
interface contract once merged. B then extends `substrate` with pools, episodes and tokenization.

**Spec questions surfaced while writing these criteria** (for the Research Manager; not resolved here):
- S-full's stake grid is unspecified. With signed, continuous stakes, the optimal vector E[a]/(2*lambda) determines the
  predictive, as c-substrate says. With a non-negative grid like S's {0,1,2,3} it does not: whenever only one action
  has positive expected outcome, the other two are clipped to zero and cannot be told apart. Verification will test
  both readings; which is intended is a research call.
- lambda has no value ("chosen so s* spans the grid over the empirical edge distribution"). Verification doesn't need
  one; training does.
- Tie-breaking for best response is unspecified. It matters for Phase A targets whenever the predictive is uniform
  (all E[a] = 0).

**Execution.** Session container, CPU, estimated under 10 minutes, $0.

## Log
- 2026-09-2x recorded from relay.

## Delivery
(Result / Method / Deviations / Provenance / Reproduce: empty until delivered)
```

---

## Appendix C — work-order template (a section of the request file), illustrated with candidate example B

*Illustrative only. The paths and test names show the shape; the real ones are written when B is promoted.*

```markdown
## Work order

**Goal.** Build the phase-1 data pipeline for `c-substrate`: sample rung-1 opponent policies, build train/test pools
from a recorded seed, pre-generate trajectories, and tokenize episodes (vocab 4, length 65) for the training loop.

**Scope — you may create or modify only:**
- src/belief_circuits/substrate/  (except __init__.py's public names, which are fixed below)
- tests/unit/substrate/
Everything else is read-only to you.

**Interfaces.**
- Use (frozen): `substrate.game.outcome`, `substrate.game.sample_policy` (merged with req-0001).
- Provide (types and contract tests already on main): `Pool`, `Episode`, `tokenize(episode) -> TokenizedEpisode`,
  `make_pool(size, seed, split) -> Pool`. Contract tests: tests/contract/substrate/.

**Acceptance tests (already on main, currently failing):** tests/acceptance/req-0003/
- test_no_leak_round_trip: for every episode and round t, the opponent's round-t action is absent from the
  tokens visible at round t's decision position. A failure prints the offending episode and round.
- test_pool_determinism: same (size, seed) gives a byte-identical pool.
- test_split_disjoint: train and test policies never overlap; 50/50 over policies.
- test_pool_scale: size 4096 builds in under 30 s on 4 CPUs and round-trips through save and load.

**Constraints.** numpy only. CPU only. Unit tests in under 30 s in total. No paid compute.

**Out of scope.** Storage backends beyond local files; phase-2 reactive opponents (keep the joint-state representation
general, but implement only rung 0 and rung 1 sampling); tokenization variants SELF and SHARED.

**Stop and ask if:** an acceptance or contract test looks wrong; the interfaces above don't fit the work; you need a
dependency; or you'd have to choose anything with research meaning (e.g. the secondary held-out split's region).

**Done when:** acceptance, contract and unit tests pass, CI is green, and a PR titled `req-0003: substrate data
pipeline` is open with the required description.
```

Two things this example shows.

**The no-leak requirement becomes a test.** The research candidates noted that `c-substrate` only says no-leak "must be asserted by a round-trip test", without saying what the test does. Writing the acceptance test is where the Lab Manager has to make that operational. Since what counts as a leak is plainly defined in the node, this is an engineering choice, not a research one, and it is tagged `[proposed]` in the restatement anyway.

**The storage-format question is contained, not decided.** The pool's on-disk format is kept behind the `Pool` interface's save and load. Local files now, anything later, without touching callers. This is how §6.4's deferred decisions stay deferred without blocking work.
