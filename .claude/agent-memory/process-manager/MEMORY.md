Your real memory is `process/memory.md` at the repo root, not this file.

This directory exists only because Claude Code auto-loads
`.claude/agent-memory/process-manager/MEMORY.md` into your context
automatically on every invocation (see `memory: project` in
`.claude/agents/process-manager.md`) — a convenience specific to this
harness. `process/memory.md` is where the actual log, the protocol, and
the reasoning live, deliberately written in plain Markdown at a path any
harness (or a human) can read without knowing Claude Code's conventions.

Read `process/memory.md` now. Don't write your log entries here — write
them there. If this file and `process/memory.md` ever disagree,
`process/memory.md` is correct.
