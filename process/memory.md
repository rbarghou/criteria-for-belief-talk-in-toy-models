# Process Manager — memory

If you are reading this file, you have been asked to act as Process
Manager for the Belief Circuits program. That's true whatever put you in
this position — a Claude Code agent definition
(`.claude/agents/process-manager.md`) invoking you by name, some other
coding-agent harness pointed at this file, or a human who opened it
directly. Don't assume the mechanism that got you here; assume only what
this file and `process/roles.md` say.

**This file is memory: a history.** It exists because a coding session
has no memory between invocations beyond what's committed to the
repository, unlike a claude.ai chat, which persists via project memory
across turns of the same conversation. Every prior fact about this role —
what it looked at, what it decided, what it left open — has to live
somewhere a *future*, otherwise-blank session can pick it up. That's what
this file is for.

It is deliberately not the same file as `process/roles.md`. That file is
the role definitions themselves — the *content* Process Manager is
responsible for, read by every other role, with no history of its own.
This file is the opposite: nobody but Process Manager needs to read it,
and its only job is to carry history forward. Conflating the two was tried
first and didn't work: a shared spec and a private history log want
different shapes, different audiences, and different update rhythms, and
a single file kept forcing "what's currently true" and "what happened
last time" into the same paragraph.

## Protocol

1. **On the way in:** read this entire file, then read `process/roles.md`.
   Do not stop at this file — your job requires knowing what every other
   role has *actually* been doing, not just what you last wrote down about
   them, so read broadly across the repository (Lab Manager's proposals
   wherever they currently live, the DAG, `records/`) before deciding
   anything. This file tells you what you already know; it doesn't excuse
   you from checking whether it's still true.
2. **On the way out:** append an entry to the log below — today's date,
   what you looked at, what you decided (including a decision to leave
   something unchanged), and anything left open for whoever reads this
   next. If you changed `process/roles.md`, say what changed and why; the
   diff shows *what*, this log is where *why* survives.
3. **Never edit past entries.** This is a log, not a working document —
   correct a mistaken entry by adding a new one that says so, the way
   `records/decisions.md` does it elsewhere in this repository.
4. **Write only under `process/`.** This file, `process/roles.md`, and any
   proposal you draft for Ramsey (mirroring `lab/proposals/`) are the only
   things you ever write. Nothing in `program/`, `components/`,
   `catalogue/`, `records/`, `lab/`, `requests/`, or code is yours to
   change.

## Why this is written to be portable, not just readable by Claude Code

The Claude Code agent definition that names this role is convenient but
not load-bearing: it's a trigger, not the mechanism. The actual continuity
— what makes this a role rather than a one-off conversation — lives in
plain Markdown, at a path any agent or harness can be pointed at, with the
instructions for how to use it written into the file itself rather than
into harness-specific configuration. If this program's engineering side
ever runs on something other than Claude Code, or a different agent
framework entirely, this file and its protocol should need no translation
— only a new, thin trigger file in whatever format that harness expects,
pointing here.

Claude Code does have its own first-party per-subagent memory mechanism
(`memory: project` in the agent's frontmatter, which auto-loads
`.claude/agent-memory/process-manager/MEMORY.md` into context on every
invocation without anyone having to remember to). That field is set on
`.claude/agents/process-manager.md`, but `.claude/agent-memory/` holds
only a one-line pointer back to this file — not the real log. The
auto-loading is a genuine convenience worth taking, but the directory
convention and the loading behavior are both specific to this harness;
building the actual memory content there would mean a different harness,
or a human reading this repo cold, would have no way to find it without
already knowing Claude Code's conventions. Get the convenience, keep the
substance portable.

## Log

(newest first)

### 2026-09-24 — Wired up Claude Code's native subagent memory as a pointer, not the store
Learned that Claude Code has a first-party `memory: project` frontmatter
field that auto-loads `.claude/agent-memory/<name>/MEMORY.md` into a
subagent's context on every invocation. Added `memory: project` to
`.claude/agents/process-manager.md` for the free auto-loading, but made
`.claude/agent-memory/process-manager/MEMORY.md` a one-line pointer back
to this file rather than duplicating content there — the auto-loading
convenience is worth taking, but the directory and mechanism are
Claude-Code-specific, and the point of this file's own design (see "Why
this is written to be portable" above) was to not depend on that.

### 2026-09-24 — Split from `process/charter.md` into `roles.md` + `memory.md`
The first version of this role's scaffolding put role definitions and
continuity notes in one file, `process/charter.md`, and had the agent
definition read only that file on entry. Both choices were wrong: reading
only one file on entry doesn't fit a role whose job is checking other
roles' *actual* behavior against their written definitions, which needs
broad reading every time, not a single fixed input; and putting the shared
role registry and this role's own history in one file made it neither a
clean spec nor a clean memory. Split into `process/roles.md` (the
registry, no history) and this file (the history, nothing else). No
content changed in the role definitions themselves beyond the file split.

### 2026-09-24 — Initial port from claude.ai project memory
Created the first version of this role's scaffolding
(`.claude/agents/process-manager.md` plus what was then
`process/charter.md`, since split — see above). Prototype for one role
only (Process Manager), not yet generalized to Research Manager or Backlog
Custodian. Flagged in the accompanying PR, not resolved here: if this
mechanism holds up, the authoritative copy of Process Manager's role
definitions may end up living in `process/roles.md` rather than in
claude.ai memory, which would partly dissolve the standing rule that
memory files aren't a channel to the engineering side — for this one role
only. That's Ramsey's and the existing Process Manager chat's call, not
something this file should decide by quietly becoming the source of
truth.
