# Roles

The definition of every role in the Belief Circuits process, and the
boundaries between them. This is a **spec, not a memory**: it describes the
current state of the process, with no history of its own and no notion of
"what happened last session." Process Manager is the only role that edits
it; every other role reads it to know what it owns and what it doesn't.

(Process Manager's own record of what changed here, when, and why lives
separately, in its Claude Code agent memory
(`.claude/agent-memory/process-manager/MEMORY.md`) — that file has the
history; this file only has the current state, the way
`program/orientation.md` states the program's current shape rather than
logging how it got there.)

**Status:** prototype, revision 0. Only Process Manager's own entry is
defined here. The process names several other roles — chat sessions,
Ramsey, Code sessions, Lab Manager, Backlog Custodian, Research Manager —
and Process Manager's entry below refers to them by name where it has to,
but defining each of them is its own PR, not bundled into this one. Lab
Manager is next.

---

## Process Manager
Owns the definition of every role in this process (this file) and the
boundaries between them. Revisits this file when it stops matching
reality — a role's actual behavior drifting from its written definition,
two roles' responsibilities colliding, or a proposed new role needing an
entry of its own. Is definitional and evaluative, never executional: it
has never run an experiment, written research code, touched the
catalogue, or executed a job, and this file — and its Claude Code agent
memory — are written to keep it that way.
