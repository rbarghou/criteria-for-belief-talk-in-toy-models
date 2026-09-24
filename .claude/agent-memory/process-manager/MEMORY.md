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

(newest first)

### 2026-09-24 — Collapsed the memory file into this one, dropped the portability layer
Earlier passes built a separate `process/memory.md`, reasoning it should
be readable without depending on Claude Code's conventions, and treated
this file (`.claude/agent-memory/process-manager/MEMORY.md`) as a one-line
pointer to it. Simplified on request: use Claude Code's native per-agent
memory directly rather than building an abstraction layer over it. This
file is now the actual memory; `process/memory.md` is deleted, and its
log entries below are carried forward unchanged in substance.

### 2026-09-24 — Split role definitions and memory into separate files
The first version put role definitions and continuity notes in one file
and had the agent definition read only that file on entry. Both choices
were wrong: reading only one file on entry doesn't fit a role whose job is
checking other roles' *actual* behavior against their written
definitions, which needs broad reading every time, not a single fixed
input; and putting the shared role registry and this role's own history in
one file made it neither a clean spec nor a clean memory. Split into
`process/roles.md` (the registry, no history — unchanged by this entry)
and a memory file (history, nothing else — now this file).

### 2026-09-24 — Initial port from claude.ai project memory
Created the first version of this role's scaffolding: the agent
definition and role registry, ported from the process charter maintained
in claude.ai project memory for this program. Prototype for one role only
(Process Manager), not yet generalized to Research Manager or Backlog
Custodian. Flagged in the accompanying PR, not resolved here: if this
mechanism holds up, the authoritative copy of Process Manager's role
definitions may end up living in `process/roles.md` rather than in
claude.ai memory, which would partly dissolve the standing rule that
memory files aren't a channel to the engineering side — for this one role
only. That's Ramsey's and the existing Process Manager chat's call, not
something this file should decide by quietly becoming the source of
truth.
