# Memory (Claude Code)

> **Purpose:** Session memory guide plus multi-agent work/durable/log layers.
> **Função:** Explicar memória Claude Code e as camadas do loop multiagente.

Canonical loop: [docs/MULTIAGENT_ENGINEERING_LOOP.md](../../docs/MULTIAGENT_ENGINEERING_LOOP.md) §6.

## Multi-agent layers (this repo)

```
.claude/memory/
├── work/<correlation-id>/<role>/   # Per-run drafts — each role own folder
├── durable/                        # Validated facts — orchestrator ONLY (examples)
├── log/                            # Append-only audit examples
├── examples/                       # Sample MEMORY.md fragments
└── README.md
```

- Correlation ID: `run-<YYYYMMDD>-<short-hash>`
- No secrets/PII in any layer
- Only the orchestrator promotes into durable / project MEMORY

## Persistent Claude Code memory (runtime)

Real cross-session persistence lives in:

```
~/.claude/projects/<project-name>/memory/
├── MEMORY.md          # Index (loaded every session, < 200 lines)
├── user-*.md          # type: user
├── feedback-*.md      # type: feedback
├── project-*.md       # type: project
└── ref-*.md           # type: reference
```

This folder holds **examples** to copy locally.  
Do not commit PII, credentials, or production data.

See `docs/CLAUDE_CODE_GUIDE.md` §8 and `examples/`.
