# Retired process-manager files

On 2026-10-17 Ramsey retired the three files in this folder. They were moved out of `.claude/` so that sessions opened in this repo no longer load them as an agent or a skill. They stay here so a future process manager session can find them.

The files are unchanged. Paths written inside them still name their old locations, and `process/roles.md` has been updated to the new ones. The original text and locations are visible at commit `8a3e60a9797b13c026fa407394fbcc0110550db1`.

| File here | What it was | Original path |
|---|---|---|
| `process-manager-agent.md` | A Claude Code subagent definition for the Process Manager role | `.claude/agents/process-manager.md` |
| `process-manager-skill.md` | The skill that carried out the persona in a session | `.claude/skills/process-manager/SKILL.md` |
| `process-manager-memory.md` | The dated log of what changed in `roles.md`, and why | `.claude/agent-memory/process-manager/MEMORY.md` |

The process they served is being redesigned. The working agreement for the new process will live in the hub repository, `repeated-rps-hub`.
