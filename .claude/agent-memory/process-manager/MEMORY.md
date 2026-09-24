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

(newest first. This role hasn't been invoked for real work yet — the one
entry below just records that the scaffolding exists. How it came to be
built is in the repo's git history, not here; this log is for what the
role does, not how it was set up.)

### 2026-09-24 — Scaffolding created
`.claude/agents/process-manager.md`, `process/roles.md`, and this memory
file were created, seeding `process/roles.md` with role definitions
ported from the process charter maintained in claude.ai project memory
for this program. One open item, not resolved here: whether
`process/roles.md` should become the authoritative copy of those
definitions, superseding the claude.ai memory version — that's Ramsey's
and the existing Process Manager chat's call, not this role's to settle
unilaterally.
