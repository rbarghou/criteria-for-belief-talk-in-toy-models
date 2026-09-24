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
