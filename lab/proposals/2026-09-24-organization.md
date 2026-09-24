# Lab Manager proposal: how this repository takes in, builds, runs, and reports work

**Date:** 2026-09-24 · **From:** Lab Manager · **Status:** proposal. Nothing here is adopted. The only change to the repository is this file, on a feature branch.

**Readers.** Ramsey (all). Process Manager (§1–3, §5, §9–10). Backlog Custodian (§3.4). Research Manager (§4.4, §8, Appendix B).

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
pyproject.toml  src/belief_circuits/  tests/     with the first code request (the solver, Appendix B)
jobs/                                            with the first execution whose output is claimed as a result
```

Code layout, when it arrives, mirrors the component nodes: `substrate/`, `solvers/`, `training/`, `instruments/grounded/`, `instruments/derived/`. Each module names its node ID in its docstring.

The graph's grounding firewall then gets a counterpart in code: a test fails if anything under `instruments/grounded/` imports from `instruments/derived/`. It costs almost nothing and makes the program's central methodological worry — circular validation — something the build can catch.

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

## 5. Delegation and concurrency

**What I do directly:**

- anything touching epistemic content;
- tooling and process changes;
- small builds;
- all execution of results.

**What I delegate:** self-contained builds with test-checkable criteria and a bounded file scope. Candidate examples B (data pipeline) and C (training scaffold) are the likely first cases. Ramsey can override either way on any request.

**The work order lives in the request file,** not in a chat prompt. A delegated session's entire starting prompt is:

> "Read `CLAUDE.md`, then the Work order in `requests/req-NNNN-*.md`; deliver as a PR to `main`."

So the delegation is visible to the Custodian, is identical however the session gets started (by me through the session tools, or by Ramsey by hand), and survives the chat that launched it.

**The concurrency model is P3 made concrete:**

| State | Writer | How conflicts resolve |
|---|---|---|
| Request files, node content, node status | Lab Manager only | None arise |
| Code | Any session, on its own branch, within its work order's scope | At PR merge, by the Lab Manager |
| `generated/` | The tool only | Regenerate; never merge by hand. CI fails if `generated/` doesn't match the source files |
| `jobs/` | Lab Manager only | None arise |

Before I merge a delegated PR, I read the whole diff against the request's criteria rather than trusting the PR description.

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
| 3 | **B and C in parallel**, with the episode/batch interface written into both work orders as an explicit contract | Delegated | First training runs |
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
3. The graph's rules are enforced by the tool; never work around a failure. Grounded studies may not depend on derived
   instruments, and code under `instruments/grounded/` may not import from `instruments/derived/`.
4. The repo is public: no credentials, tokens, account identifiers, or personal information, ever.
5. Acceptance criteria are fixed before the work they judge. If one looks wrong, stop and say so; never adjust it to fit a result.
6. Do not start paid compute. Only the Lab Manager executes jobs whose outputs are claimed as results, from `main`.

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
