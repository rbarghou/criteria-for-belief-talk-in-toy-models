# Lab Manager proposal: how this repository takes in, builds, runs, and reports work

**Date:** 2026-09-24 · **From:** Lab Manager · **Status:** proposal. Nothing here is adopted. The only change to the repository is this file, on a feature branch.

**Readers.** Ramsey (all). Process Manager (§1–3, §5, §9–10). Backlog Custodian (§3.4). Research Manager (§4, §8, Appendix B).

**Revision 3 (same day).** §4 is new: how code, results, the research graph, and requests are kept from confusing each other. §5 now says how the code is managed, and treats delegation as something earned: I do each kind of work first, and small ceremonies decide when a new agent is warranted. Revision 2's detailed agent-management scheme and its work-order template are withdrawn as premature.

---

## 0. Summary

The repository today is a careful **epistemic** structure (what the program claims and what depends on what) with no **work** layer (what has been asked of engineering) and no **execution** layer (what was built and run, from what, at what cost). This proposal adds the two missing layers as thinly as I can make them, and says who writes what.

The moves, in one screen:

1. **Four kinds of thing, never confused (§4).**

   | Kind | What it is |
   |---|---|
   | Graph nodes | Claims |
   | Requests | Asks |
   | Code | Methods |
   | Results | Evidence |

   - Every fact lives in exactly one of them; anything combining two is a generated view.
   - Graph nodes cite evidence, never process. Code cites the specification, never the ask.
   - Each kind uses its own status words, so a status can't be misread across layers.
   - "Run" means only the graph node. An execution is a "job", and its parameters are a "config".
   - Results never edit the graph. A conclusion is added to a node, citing the result, only on research authority.
2. **One file per promoted request**, in `requests/`, with the promoted text kept **word for word** and kept apart from my engineering restatement. The Backlog Custodian checks the one against the other on a single generated page (`generated/requests.md`) in the public repo.
3. **Acceptance criteria are committed before the work they judge runs.** Git history is the timestamp. This is the program's own pre-registration rule, applied to engineering. It is what lets the stakeholder side trust a result without needing to know how it was produced. Criteria I had to invent are tagged `[proposed]`, never passed off as the requester's.
4. **Results come only from reviewed code on `main`**, executed by the Lab Manager. They are immutable, and each execution behind them leaves a job record: commit, config, seeds, environment, cost, output hashes.
5. **Authority is cited, not assumed.** Any change in meaning to `program/`, `components/`, `catalogue/`, or `records/` cites a request or a dated relayed decision. That is how a research-side decision becomes a repo edit without me becoming its uncredited author.
6. **The repository is the Lab Manager's memory.** This chat is lossy: context gets compacted and the container gets reclaimed. So my operating rules, cost policy, and record of environments live in `lab/`. `CLAUDE.md` carries the rules every coding session must follow, because it is the one file every session reads automatically.
7. **Infrastructure is decided by the first request that needs it.** Each deferred decision has a named trigger and a current lean. Only one is decided now: code goes in a single installable package, not loose scripts. Reversing that later costs the most, because every delegated session would otherwise invent its own layout.

8. **I do each kind of work first; delegation is earned (§5).** Every kind of work is performed by me first, with a playbook written as I go.
   - Three small ceremonies decide when to hand it off: a two-line retrospective per request, a delegation review once a playbook is stable, and demotion after repeated failures.
   - Any new *standing* agent comes to Ramsey as a proposal.
   - The code itself follows the graph: modules mirror components, imports follow `needs` edges, acceptance tests are written first, and `main` stays green.

The overhead per request is: I write one file, mostly pasted text plus criteria. A status line changes as work proceeds. A delivery section is filled in at the end. The Custodian reads one page. That is all of it.

---

## 1. Principles

Everything below follows from these. If a later rule contradicts one of them, the rule is wrong.

| # | Principle | The failure it prevents |
|---|---|---|
| P1 | Every fact lives in exactly one of four kinds of thing (claim, ask, method, evidence). Joins are generated. Graph nodes cite evidence, never process. Code cites the specification, never the ask (§4). | Code, results, the research graph, and requests drifting into and contradicting each other. |
| P2 | If it isn't in the repo, the Lab Manager doesn't know it. | Knowledge lost when context is compacted or a session ends. A successor Lab Manager can't take over. |
| P3 | One writer per kind of state. | Concurrent sessions silently corrupting shared files (see §5). |
| P4 | Criteria are committed before the work they judge runs. | Verification whose criteria were picked after seeing results. |
| P5 | Authority is cited, not assumed. | Scientific content changing through engineering edits nobody decided. |
| P6 | Infrastructure is added when a request needs it, never before. | Ceremony and a stack chosen before the problem is known. |

---

## 2. What the repository would look like

```
CLAUDE.md                  NEW  rules every coding session reads automatically (draft: Appendix A)
README.md, schema.md       existing; schema.md gains request, result and job fields and the §4 rules
program/  components/      existing, unchanged: the epistemic layer
catalogue/  records/       existing, unchanged
history/                   existing, frozen
requests/                  NEW  asks: one file per request (example: Appendix B)
lab/
  README.md                NEW  Lab Manager operating manual: intake, delegation, execution, cost policy
  environments.md          NEW  what exists: environments, services, how credentials are provided (never their values)
  decisions.md             NEW  engineering decisions, plus deferred decisions with their triggers
  proposals/               NEW  engineering proposals to the stakeholder side (this is the first)
  playbooks/               NEW  one per kind of work, written while doing it (§5.5); starts empty
tools/dag.py               existing; gains validation, the §4.3 citation rules, and the new views
generated/                 existing; gains requests.md (Custodian) and status.md (node × request × result)
.github/workflows/         NEW  CI: regenerate and fail on any difference or error; run tests once code exists

created by the first request that needs them, not before:
pyproject.toml  uv.lock  src/belief_circuits/  tests/     with the first code request (the solver, Appendix B)
configs/<run-node-id>/                           with the first run configuration
results/  jobs/                                  with the first execution whose output is claimed as a result
```

How the four kinds are kept apart is §4. The code layout is §5.1.

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
4. **Delivery.** For `build`: what exists, how to use it, which tests show each criterion met, and any deviations. For `build-and-deliver-results`: see §4.4.

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

## 4. Four kinds of thing, and how they are kept from confusing each other

The repo will hold four kinds of thing. They are easy to confuse, because they share vocabulary and point at each other constantly. The rules in this section are the main defence against that. Most of them are enforced by tooling rather than by care.

### 4.1 One question each

| Kind | The one question it answers | Lives in | IDs | How it changes | Written by |
|---|---|---|---|---|---|
| **Graph node** (a claim) | What does the program claim, and what does each claim rest on? | `program/`, `components/`, `catalogue/`, `records/` | `c-`, `r-`, `s-`, `p-` | Revised in place (git history is its history). A change in meaning needs cited authority. | Lab Manager, on research authority |
| **Request** (an ask) | What was engineering asked to do, and has it been done? | `requests/` | `req-NNNN` | Recorded once; afterwards only its status, log and delivery grow | Lab Manager |
| **Code** (a method) | How is anything computed? | `src/`, `tests/`, `configs/` | module paths; the commit SHA is the version | Evolves freely; a commit is tagged when a result used it | Lab Manager (later, also delegates: §5.5) |
| **Result** (evidence) | What happened when something was computed? | `results/` (with `jobs/` for the individual executions) | `res-NNNN`, `job-YYYYMMDD-NN` | **Immutable** once final; replaced by a new result, never edited | Lab Manager |

**The rule under the table:** every fact lives in exactly one of these four places. Anything that needs two of them side by side is a **generated view**, never a hand-kept copy. Copies are how the four drift apart.

### 4.2 The specific confusions, and the rule for each

1. **"Run" means three different things today.** It can mean the graph's run node (`r-phase-b-main`, a configuration the program reasons about), the file that sets its parameters, or one execution of it.
   - **Rule:** "run" means only the graph node. The parameter file is a **config** (`configs/r-phase-b-main/`, named after its node, exactly one directory per run node). An execution is a **job**.
   - The tooling checks that every config directory matches a run node, and that every job cites both.
2. **A study's primary outcome versus a request's acceptance criteria.**
   - The primary outcome is the *scientific* pre-registration and lives in the study node.
   - Acceptance criteria are the *engineering* definition of done and live in the request.
   - **Rule:** a request serving a study may check that the work was done properly: every seed ran, every control was computed, the outputs are reproducible. It may never restate, sharpen, or decide the study's outcome. If delivering it needs a scientific choice (a threshold, a statistic), that choice goes back as a question.
   - This keeps two pre-registrations from quietly merging into one that engineering wrote.
3. **A result versus a conclusion.**
   - A result is what came out.
   - A conclusion is the research side's reading of it.
   - **Rule:** results never edit nodes. When the research side draws a conclusion, the node gains a **Findings** entry citing the result's ID, as an authorized edit.
   - "Delivered" in a request therefore never means "established" in the graph. The request can be closed while the claim is still open, or contested.
4. **Three statuses, deliberately given different words.**

   | Kind | Values |
   |---|---|
   | Node: how resolved the claim is | `stub`, `drafted`, `ready`, `imported` |
   | Request: where the ask is | `queued`, `active`, `blocked`, `delivered`, `accepted`, `withdrawn` |
   | Job | `launched`, `succeeded`, `failed`, `aborted` |
   | Result | `final`, `superseded` |

   `running`, `done` and `stale` are retired from nodes. No word appears in two lists, so a status can never be read in the wrong layer. 8 prior-art nodes already use `imported`, which the schema never listed; it becomes legitimate.
   **Research Manager please note:** node status then only ever describes the claim.
5. **A component node versus the code that implements it.** The node is the specification; the module is an implementation of it.
   - Implementing forces choices the specification doesn't make (the stake cost λ and the best-response tie-break, for example).
   - **Rule:** any constant that carries research meaning lives in a config file, not in code, and carries a `source:` of either a node, a relayed decision, or `proposed`.
   - A generated list of every `proposed` parameter is then a standing, accurate list of specification gaps for the Research Manager. Code never settles one silently.
6. **Evidence going stale.** A result is tied to its commit and config. If either later changes along a path the result depends on, the result isn't edited.
   - The generated status view flags it as possibly stale.
   - If it needs redoing, the new result supersedes it.
   - This is `schema.md`'s stale-propagation rule, now computed from evidence rather than typed by hand.

### 4.3 Who may cite whom

This one table enforces the separation. `tools/dag.py` checks it.

| From ↓ may cite → | Node | Request | Code | Result |
|---|---|---|---|---|
| **Node** | yes (typed edges) | **never** | **never** | yes, only in *Findings*, on authority |
| **Request** | yes (`serves`) | yes (`needs`) | yes (paths in its plan) | yes (its delivery) |
| **Code / config** | yes (docstring, `source:`) | **never** | yes | **never** |
| **Result** | yes | yes | yes (commit) | yes (`supersedes`) |

Two lines carry the design:

- **nodes cite evidence, never process;**
- **code cites the specification, never the ask.**

So the epistemic record never depends on how the work was organized, and the code never encodes who asked for what. This replaces the first version's P1 ("references point upward only"), which was too strict: the graph does need to cite evidence once conclusions exist.

### 4.4 What a result contains

`results/res-NNNN/` holds `report.md` plus a manifest.

- The report has a fixed shape, which is the Process Manager's "result plus enough methodology and provenance":
  - **Result**, stated against each acceptance criterion;
  - **Method**, in the stakeholder side's terms;
  - **Deviations**, never omitted or softened, including any `[proposed]` criteria nobody confirmed;
  - **Provenance** (commit, jobs, output hashes);
  - **Reproduce**, as one command.
- The manifest lists the outputs with their hashes and where they're stored.
- Small outputs are committed alongside it. Large ones are stored elsewhere and referenced (§6.4). Deterministically regenerable ones are recorded as generator plus seed plus hash.
- Each execution behind a result has a record in `jobs/`: commit, command, config, seeds, environment, times, cost, outputs. It is written *before* launch, so a crash still leaves a trace.
- A request's Delivery section only *links* the result and summarizes it in a paragraph. It is not a second copy.

Results come only from code on `main`, executed by the Lab Manager, so the commit a result cites was reviewed and cannot disappear.

### 4.5 The generated views that join them

- **`generated/requests.md`.** The Custodian's page (§3.4).
- **`generated/status.md`.** One row per graph node, showing:
  - the node's claim status;
  - open requests serving it;
  - the latest result, and whether it is possibly stale;
  - `proposed` parameters awaiting a decision.

  This is the Research Manager's whole-picture view, and nobody maintains it by hand.
- **Existing orders and grounding report.** Unchanged.

### 4.6 One thread traced end to end: solver verification

1. **The node.** `r-solver-verification` (node) says what must be checked and why it gates everything.
2. **The request.** `req-0001` records the promoted ask, verbatim, and my restatement with `[proposed]` criteria (Appendix B).
3. **The code.** `src/belief_circuits/solvers/` implements `c-solvers`; its docstring cites the node, not the request.
4. **The config.** `configs/r-solver-verification/` holds the tolerances and sample sizes, each with a `source:`.
5. **The execution and result.**
   - `job-…` records the execution.
   - `res-0001` reports pass or fail per criterion. It is immutable, and its commit is tagged `result/res-0001`.
6. **Delivery.** `req-0001` goes to `delivered` and links `res-0001`.
7. **The conclusion.** The Research Manager decides the gate has passed. On relayed authority, the node gains a *Findings* entry citing `res-0001`, and `req-0001` goes to `accepted`.
8. **Later.** If the solver's code changes, `status.md` flags `res-0001` as possibly stale for this node. Nobody has to remember to.

Each step writes to exactly one kind of thing, and every cross-reference points in an allowed direction.

---

## 5. The codebase, and moving from doing to delegating

### Part A — Managing the code

#### 5.1 Layout follows the graph's components; imports follow its `needs` edges

```
src/belief_circuits/
  substrate/            c-substrate
  solvers/              c-solvers
  training/             c-training
  instruments/grounded/ c-inst-grounded
  instruments/derived/  c-inst-derived
  jobs/                 thin entry points: read a config, call the library, write a result
tests/                  mirrors src/; acceptance tests in tests/acceptance/<req-id>/
configs/<run-node-id>/  one directory per run node (§4.2)
```

- `substrate` imports nothing from the project. `solvers` may import `substrate`, and `training` may import both.
- `instruments/derived` may import `instruments/grounded`, never the reverse.
- Nothing imports from `jobs/`.
- One test checks every import direction, so the grounding firewall is enforced in code as well as in the graph.

**The library is pure.**
- Random number generators are passed in explicitly, never taken from a global seed.
- There is no file, environment or network access outside `jobs/`.
- Meaningful constants come from configs (§4.2 item 5).

This makes almost everything testable on CPU in seconds, and makes determinism checkable.

#### 5.2 Interfaces are explicit and change deliberately

- A module's public interface is what its `__init__.py` exports, with type annotations. Everything else is internal.
- Public interfaces have contract tests.
- Changing a public interface is its own small change, with its knock-on effects stated. That is what will make parallel work safe once there is any (§5.5).
- Where work is built against an interface that doesn't exist yet (candidate example C against B), the interface is written first, as types plus a contract test. The assumption is then checked by a test rather than trusted.

#### 5.3 Testing

| Tier | What | When |
|---|---|---|
| Unit and contract | Public functions and interface invariants | Every push (CI), under 1 min |
| Exhaustive and property | Numerical code against brute force or known identities | Every push, under 2 min |
| Smoke | Each entry point end to end on a tiny config | Every push, under 3 min, CPU |
| Validation | Real-scale runs whose output is a result | Only as jobs, by the Lab Manager |

- **Determinism is tested.** Same config and seed give byte-identical outputs on CPU. Any GPU nondeterminism is recorded, never absorbed.
- **Acceptance tests are written before the code they judge**, by whoever holds the criteria. They are not edited to fit. This is P4 applied to code, whether the work ends up done by me or delegated.

#### 5.4 Keeping `main` healthy

- **Always green.** Nothing merges with CI red, and a broken `main` outranks all other work.
- **CI checks:**
  - `ruff`;
  - the test tiers;
  - `tools/dag.py` validation, including the §4.3 citation rules;
  - the import-direction test.
- **Dependencies** are locked in `uv.lock`. Each addition gets a one-line reason in `lab/decisions.md`.
- **Small changes, one purpose each.** Refactors never ride along with features.
- **The commit that produced a reported result is tagged** `result/res-NNNN`.
- **A maintenance pass after every ~5 merged code requests** (dead code, duplication, awkward interfaces, slow tests), recorded as a `source: lab-manager` request.

### Part B — From doing to delegating

#### 5.5 The principle: delegation is earned by a process that already works

On the first pass through any kind of work, I do it myself. There is no fully formed delegation process at the start, deliberately. A brief written before anyone has done the work is a guess, and an agent following a guessed brief produces confident, wrong output that is expensive to review.

What *is* fixed from the start is how we will decide when a new agent is needed. Each kind of work moves through four stages:

| Stage | Meaning | What exists |
|---|---|---|
| **0 · Performed** | I do it myself | A **playbook** (`lab/playbooks/<kind-of-work>.md`), written *while* doing it: the steps, the checks, what went wrong |
| **1 · Repeatable** | Done at least twice, and the playbook barely changed the second time | A playbook stable enough to brief someone else |
| **2 · Delegated, watched** | First handoffs to an agent, with the playbook as the brief | I verify everything the agent produces, as if I'd doubted it |
| **3 · Delegated** | Routine | Spot checks; the playbook stays the brief and keeps being corrected |

A "kind of work" is something like:
- "implement a component module against a frozen interface";
- "turn a run node into a config and a smoke test";
- "execute a seed sweep";
- "record a request";
- "make an authorized graph edit".

Playbooks accrete from real requests; none are written in advance.

#### 5.6 The ceremonies

Three, all small.

1. **Retrospective**, at the end of every request. Two lines in the request's Log (what went smoothly, what didn't), and an update to the relevant playbook. This is the only one that happens every time.
2. **Delegation review.** This runs when a kind of work reaches stage 1 **and** there is a reason to hand it off:
   - requests are queueing behind me;
   - the work could run in parallel with other work;
   - or it is using up the context I need for the manager's job.

   It asks three questions:
   - *Can the input be fully specified in writing?*
   - *Is checking the work much cheaper than doing it?*
   - *Could it ever require a choice with research meaning?*

   Its outcome is one entry in `lab/decisions.md`: *delegate*, *not yet*, or *never*, with the reason.
   - A one-off handoff (a subagent in my session, or a temporary cloud session) is mine to decide.
   - A new **standing** agent — a persistent role, like mine — goes to Ramsey as a proposal, because it is a new identity with its own continuity and access.
3. **Demotion.** A delegated kind of work that fails verification twice drops back a stage, and I do it again until the playbook is fixed. A repeated failure means the playbook is wrong, not that the agent needs a stricter brief.

**Probably never delegated:** graph edits carrying research meaning, executing and reporting results, and merging to `main`. **Likely first:** implementing a module against a frozen interface, where acceptance tests already exist.

#### 5.7 What holds for any agent from the start

Before any playbook exists, a few guardrails apply to every coding session, because breaking them would damage the separation in §4. They live in `CLAUDE.md` (Appendix A):

- never edit acceptance tests;
- never start paid compute;
- never change graph content;
- never settle a choice with research meaning (stop and ask instead);
- stay within the paths you were given.

Everything else about agents (brief format, concurrency, which model, how many rework rounds) is deliberately left for the playbooks to establish from experience.

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
| 3 | **B, then C**, done by me, writing the "implement a module against a frozen interface" playbook as I go (§5.5). The episode/batch interface goes in first, as types plus a contract test. After C comes the first delegation review: if the playbook held steady across A, B and C, the next module-building request is a candidate to hand off. | Lab Manager | First training runs |
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
- **e. The delegation ceremonies** (§5.5–5.6). Please confirm that one-off handoffs are my call, and that any new *standing* agent comes to you as a proposal.

**From the Process Manager:**

- confirmation of the three-item intake minimum (§3.1);
- confirmation that the Custodian's reading path in §3.4 matches its role;
- whether `[proposed]` criteria must be confirmed before a *free* execution, or only before a paid one. My default: execute, and disclose under Deviations.

**From the Research Manager:**

- G's semantics (§8);
- acknowledgement of the separate status vocabularies and the *Findings* mechanism (§4.2), and the `proposed`-parameter list as the standing list of specification gaps;
- the spec questions that drafting Appendix B surfaced. They will come back properly when A is promoted; they are listed there so the RM isn't surprised.

---

## Appendix A — draft `CLAUDE.md` (read automatically by every coding session)

```markdown
# Working in this repository

This repo is the engineering side of the Belief Circuits research program; README.md explains the program and the graph.

## Your role
- The Lab Manager reads `lab/README.md` first.
- Any other session has been handed a specific task. Its instructions (and, once they exist, the relevant playbook in
  `lab/playbooks/`) say what to do and which paths it may touch.

## Four kinds of thing: never mix them
- Graph nodes (`program/`, `components/`, `catalogue/`, `records/`) are claims. Requests (`requests/`) are asks.
  Code (`src/`, `tests/`, `configs/`) is method. Results (`results/`, `jobs/`) are evidence.
- Nodes cite results only in a Findings section, never requests or code. Code and configs cite nodes, never requests
  or results. `tools/dag.py` checks this.
- "Run" means a graph node. An execution is a "job"; its parameters are a "config" in `configs/<run-node-id>/`.
- Results are immutable. Never edit one; a redo is a new result that supersedes it.

## Rules for every session
1. Never hand-edit `generated/`. Run `python3 tools/dag.py` and commit its output with the change that caused it.
2. Graph nodes change in meaning only with cited authority (a request ID or dated relayed decision) in the commit
   message, and only the Lab Manager edits them.
3. Imports follow the graph: substrate <- solvers <- training; instruments/derived may import grounded, never the
   reverse; nothing imports from jobs/. A test checks this.
4. The repo is public: no credentials, tokens, account identifiers, or personal information, ever.
5. Never edit anything under `tests/acceptance/`. If a test looks wrong, stop and say so.
6. Do not start paid compute. Only the Lab Manager executes jobs whose outputs are claimed as results, from `main`.
7. Never settle a choice with research meaning (threshold, grid, statistic, tie-break). Meaningful constants live in
   configs with a `source:`; if you'd have to invent one, stop and ask.

## Code conventions
- Library code is pure: RNGs are passed in, no global seeds, no file/env/network access outside `jobs/`.
- Public interfaces are what each module's `__init__.py` exports; changing one is its own deliberate change.
- No new dependencies without asking. Run `ruff check`, `ruff format`, and `pytest` before pushing.
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
