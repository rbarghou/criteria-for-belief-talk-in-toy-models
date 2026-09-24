# Process Manager memory

This is Process Manager's actual memory — the history of what this role
has looked at, decided, and left open across invocations. It's loaded into
context automatically at the start of every invocation (`memory: project`
in `.claude/agents/process-manager.md`).

It is not the role registry. `process/roles.md` holds the current
definition of every role in the process and has no history of its own —
everyone reads it. This file is the opposite: only Process Manager needs
it, and its only job is to carry history forward.

## On the way out, every time

Append an entry below: today's date, what you looked at, what you decided
(including a decision to leave something unchanged), and anything left
open for next time. If you changed `process/roles.md`, say what and why —
the diff shows what, this log is where why survives. Never edit past
entries; correct a mistake with a new entry that says so.

If this file passes ~150 lines, fold older entries into a dated summary
paragraph at the bottom rather than trimming them silently.

## Log

### 2026-09-24 — Verified the Lab Manager entry against source; corrected one inaccuracy
Follow-up to the entry directly below, whose author lacked git/GitHub
access and flagged the "Standing proposal" paragraph as unverified. This
session had that access: fetched
`origin/claude/lab-manager-repo-orientation-siv329` and read
`lab/proposals/2026-09-24-organization.md` directly.

**Confirmed accurate:** the proposal's location, unmerged status, and the
substance of the Lab Manager description (build-vs-run, execution,
credentials/cost-consciousness leaning on provider controls, tooling
inventory, engineering-manager function) all match §0, §5–6 of the actual
proposal. The "Standing proposal, not yet settled" paragraph needed no
correction.

**Found inaccurate:** the "New standing roles" paragraph, which claimed
Lab Manager "routes proposals for new standing roles through Process
Manager rather than taking them to Ramsey directly." The proposal's §5.6
and §10.e say the opposite — a new standing agent "goes to Ramsey as a
proposal," addressed to Ramsey directly, with no mention of Process
Manager as an intermediary anywhere in the document. This wasn't a new
error from the prior entry: it traces back to `.claude/agents/
process-manager.md`'s own description and "What you own" section (from
PR #4), which made the same unsupported claim, attributed to "Lab
Manager's proposal," before this role ever read that proposal directly.
The prior entry's author trusted that pre-existing claim as "already-
merged, verified" — reasonably, since it was merged — but "merged" isn't
the same as "checked against its cited source," which is exactly the
gap this role exists to catch in other roles' self-descriptions and
missed in its own agent spec.

**What I changed:** reworded `process/roles.md`'s "New standing roles"
paragraph and both spots in `.claude/agents/process-manager.md` (the
`description` frontmatter's invocation trigger, and "What you own") to
say accurately that a new standing agent goes to Ramsey directly per
Lab Manager's proposal, and that Process Manager's part is writing the
resulting role's entry into `process/roles.md` after Ramsey decides —
not reviewing the proposal before Ramsey sees it. Treated this as an
accuracy correction against a now-verified source, not a scope change:
narrows an unsupported claim to Process Manager's own authority, which
the existing self-scope rule already exempts from sign-off.

### 2026-09-24 — Added Lab Manager entry to `process/roles.md`
Follow-up to the queued item from the scaffolding entry below ("each gets
its own follow-up PR, Lab Manager first"). Before drafting, tried to
verify Lab Manager's standing organization proposal
(`lab/proposals/2026-09-24-organization.md`, reportedly on branch
`claude/lab-manager-repo-orientation-siv329`, unmerged as of PR #4's
description) against its actual current state, per "First, every time."
**Could not.** This session's tools are Read/Glob/Grep/Write/Edit only —
no Bash, no git, no GitHub MCP access — and the working tree is checked
out on `main`, where `lab/` doesn't exist and that branch was never
fetched (confirmed via `.git/refs` and `.git/logs/HEAD`: only this
role's own past branches are present locally). No other checkout of the
repo exists on the machine either. So the proposal's text was not
independently readable this session, contrary to the "don't take a
role's self-description at face value" instruction — I could not check
it against the source at all, only against what's already merged into
this repo.

What I used instead: (1) the already-merged cross-references to Lab
Manager inside `process/roles.md`'s own status note and
`.claude/agents/process-manager.md` (routes new-standing-role proposals
through Process Manager before Ramsey; "engineering and execution";
`lab/` holds its organization proposal on a branch) — these are verified
against this repo's actual current state, not secondhand; and (2) the
paraphrase of the proposal's contents that the calling agent supplied
(build-vs-run distinction, credentials/cost-consciousness, tooling
inventory, engineering-manager function), which I used for texture but
flagged inline in the new entry as unverified secondhand paraphrase, not
a reading of the source.

**What I wrote:** a `## Lab Manager` entry in `process/roles.md` matching
the Process Manager entry's format — role description, then bolded
subsections for "Standing proposal, not yet settled" (states the
proposal's claimed location, that it's unmerged, that Process Manager
treats it as a draft pending Ramsey per the same logic already applied
to itself, and an explicit flag that this session couldn't open it
directly), "New standing roles" (routing through Process Manager, cross-
referenced against Process Manager's own entry), and "Boundary with
Process Manager" (executional vs. definitional, and that Process
Manager's entry settles cross-role disputes subject to Ramsey). Also
updated the file's "Status" note at the top to drop "Lab Manager is
next" now that it's defined, without naming which role is next (not this
session's call).

**Open / flagged, not settled:** the "Standing proposal" paragraph is
explicitly hedged as unverified against source — next session (or
whoever has git/GitHub access) should actually open
`lab/proposals/2026-09-24-organization.md` on its branch, confirm it
still exists at that path with that content, and correct this entry if
it's drifted. This doesn't need Ramsey's sign-off to have been written
(it's a new role entry, not an expansion of Process Manager's own scope,
per the task's own framing), but the verification gap means it should be
treated as lower-confidence than the Process Manager entry until someone
checks the source. Not committed or pushed — left in the working tree
per instruction.

### 2026-09-24 — Fixes for gap-analysis findings #1, #3, #5, #8 (plus partial #2, #7)
Follow-up to an earlier gap analysis of `process/roles.md` and
`.claude/agents/process-manager.md` (that analysis itself isn't logged
here — it predates this entry). Edited both files to close the four gaps
flagged as most concrete, folding in two secondary ones where the fix
was a natural extension:

- **Gap #1 (unchecked self-scope authority).** Added a "Self-scope and
  sign-off" rule to both files: an *expansion* of Process Manager's own
  entry in `process/roles.md` can't be written in as settled without
  Ramsey's sign-off — it stays a flagged proposal until then. Also
  defined "needs sign-off" for the first time: (a) expanding own scope,
  (b) proposing a new standing role, (c) resolving a dispute where
  Process Manager is a party. Narrowing own scope, or syncing another
  role's entry to its observed behavior, doesn't need sign-off.
- **Gap #3 (no recusal path).** Added an explicit "Recusal" clause to
  both files: when Process Manager is a party to a dispute (about its
  own scope or about `process/roles.md` itself), it states the conflict
  and hands the decision to Ramsey rather than resolving it. Folded in
  gap #7 here too — the agent spec's `description` (invocation triggers)
  now explicitly lists "dispute is about Process Manager's own scope or
  this file itself" as a trigger, tied to recusal rather than unilateral
  resolution.
- **Gap #5 (advisory vs. binding never stated), folding in #2.** Added
  an "Authority" note to `process/roles.md` and a matching "What
  'resolving disputes' means" note to the agent spec: writing a boundary
  into `process/roles.md` is binding on the other roles (it's the
  canonical registry), but not binding on Ramsey, who can overrule any
  entry including Process Manager's own. This also bears on gap #2
  (Ramsey-vs-role-scope conflicts): the answer is Ramsey wins, full
  stop, and Process Manager's role is to write down the boundary and
  flag disagreement, not to adjudicate against Ramsey.
- **Gap #8 (REQUEST-doc ownership not mirrored in the registry).** The
  agent spec already claimed ownership of "the stakeholder-side chats'
  shared instructions (what a REQUEST is, what shape it takes)" but
  `process/roles.md`'s Process Manager entry didn't mention it — so per
  the registry's own rule (a role's scope isn't real for other roles
  until it's written in `process/roles.md`) that ownership wasn't
  discoverable. Added it to the Process Manager entry's opening
  sentence.

Did not touch: gap #4 (missing vs. stale artifacts) and gap #6
(versioning/drift-detection) — left out per the task's instruction to
only fold in secondary fixes if small and natural; these felt like they
need their own design (e.g., an actual audit/diff mechanism), not a
one-line addition, so left open rather than bolted on.

**Flagging for Ramsey, not settling unilaterally:** the self-scope
expansion rule and the recusal rule are themselves changes that *expand*
Process Manager's own authority in a sense (they formalize when it must
defer) — but they're net-narrowing (they constrain, not grow, what
Process Manager can settle on its own), so I judged them as not needing
sign-off under the very criterion they establish. Flagging this
judgment call explicitly rather than treating it as obviously
self-evident: if Ramsey reads the new self-scope rule and disagrees that
it applies retroactively to itself, that's a legitimate objection and
these edits should be treated as a proposal pending confirmation, not as
already settled. Not committed or pushed — left in the working tree per
instruction.

(newest first. This role hasn't been invoked for real work yet — the one
entry below just records that the scaffolding exists. How it came to be
built is in the repo's git history, not here; this log is for what the
role does, not how it was set up.)

### 2026-09-24 — Scaffolding created, scoped to Process Manager only
`.claude/agents/process-manager.md`, `process/roles.md`, and this memory
file were created. `process/roles.md` holds only the Process Manager
entry, ported from the process charter maintained in claude.ai project
memory for this program — the other roles it names (chat sessions,
Ramsey, Code sessions, Lab Manager, Backlog Custodian, Research Manager)
are referred to by name where necessary but not yet defined; each gets
its own follow-up PR, Lab Manager first. One open item, not resolved
here: whether `process/roles.md` should become the authoritative copy of
role definitions, superseding the claude.ai memory version — that's
Ramsey's and the existing Process Manager chat's call, not this role's to
settle unilaterally.
