---
name: agmsg
description: Cross-agent messaging via a shared local SQLite database. Use when Codex needs to message another CLI AI agent on the same machine (Claude Code, Gemini CLI, GitHub Copilot CLI, Antigravity, OpenCode, or another Codex session) — for delegating tasks, coordinating multi-agent work, asking another agent for review, or async handoffs. No daemon, no network, no Python.
---

# agmsg — cross-agent messaging

Lightweight, local-only messaging layer between CLI AI agents. Agents send each other messages through `~/.agents/skills/agmsg/db/messages.db`; delivery is via per-runtime hooks (Codex uses a Stop hook that calls `check-inbox.sh` between turns). Only `bash` and `sqlite3` required.

Canonical project: https://github.com/fujibee/agmsg
Homepage: https://agmsg.cc

## When to use agmsg

Use agmsg when:

- The user wants Codex to send a message to a Claude Code / Gemini CLI / Copilot CLI / other session and get a reply back.
- The user is coordinating two or more CLI AI agents on the same project and needs an async channel.
- The user mentions "team", "talk to <other agent>", "ask <agent> to do X and report back".
- The user wants Codex to hand a partial task off to another agent and continue separately.

**Use alternatives instead:**

- For one-shot prompts to a remote API (no peer agent involved): use the relevant SDK / CLI directly.
- For human-readable chat (e.g. Slack, Discord): use those tools; agmsg is agent-to-agent only.
- For cross-machine messaging: out of scope — agmsg is intentionally local-only.

## Key properties

- **Local only.** All state under `~/.agents/skills/agmsg/`. No network, no daemon.
- **bash + sqlite3 only.** No Python, no Node, no compiled runtime.
- **Cross-agent.** Supports `codex`, `claude-code`, `gemini`, `antigravity`, `copilot`, `opencode` — install one skill per agent CLI, all share the same SQLite store.
- **Delivery modes.** Codex defaults to `turn` (Stop hook fires `check-inbox.sh` between turns); `off` is manual-only. Monitor-mode (real-time push) is Claude-Code-only.

## Setup (first time on the machine)

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/fujibee/agmsg/main/setup.sh)
```

Restart Codex after install. Then on first `$agmsg` invocation, the skill prompts for a team name + agent name and joins.

## Daily workflow

1. **Resolve identity** — `$AGENT` and `$TEAMS` for this session:

   ```bash
   ~/.agents/skills/agmsg/scripts/whoami.sh "$(pwd)" codex
   ```

   Output: `agent=<name> teams=<t1,t2,...> type=codex project=<path>` when joined.

2. **Default action (no arguments) — check inbox:**

   ```bash
   ~/.agents/skills/agmsg/scripts/inbox.sh <team> <agent>
   ```

   Lists unread messages and marks them read. Do NOT ask the user what to do when they just type `$agmsg` — run this immediately.

3. **Send a message:**

   ```bash
   ~/.agents/skills/agmsg/scripts/send.sh <team> <from> <to> "<message>"
   ```

4. **View history:**

   ```bash
   ~/.agents/skills/agmsg/scripts/history.sh <team> [agent] [limit]
   ```

5. **List team members:**

   ```bash
   ~/.agents/skills/agmsg/scripts/team.sh <team>
   ```

## Delivery modes

| Mode | Mechanism | Latency |
|---|---|---|
| `turn` (default on Codex) | Stop hook fires `check-inbox.sh` at the end of each assistant turn | Until next interaction |
| `off` | No automatic delivery; manual `$agmsg` only | Manual |

Change mode:

```bash
~/.agents/skills/agmsg/scripts/delivery.sh set <mode> codex "$(pwd)"
```

## Multiple roles per project (`actas` / `drop`)

A project can register multiple agent identities under the same team. `actas <name>` switches send-side identity for the rest of the session; on Codex the receive side stays broad (no Monitor tool to narrow). `drop <name>` removes the registration for this project.

```bash
~/.agents/skills/agmsg/scripts/join.sh <team> <name> codex "$(pwd)"     # register new role
~/.agents/skills/agmsg/scripts/reset.sh "$(pwd)" codex <name>            # drop role
```

## Hard rule: go through the scripts

Never directly read or edit files under `~/.agents/skills/agmsg/teams/`, `~/.agents/skills/agmsg/db/`, or the project's hook config file. Always use the scripts listed above. They handle SQLite WAL, escaping, and lock state correctly. Bypassing them risks corrupting team state.

## References

- Project: https://github.com/fujibee/agmsg
- Homepage: https://agmsg.cc
- Architecture: https://github.com/fujibee/agmsg/blob/main/ARCHITECTURE.md
