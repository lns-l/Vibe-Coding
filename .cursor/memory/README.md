# Cursor memory layers (multi-agent loop)

> **Purpose:** Work / durable / log memory layout for the engineering loop.
> **Função:** Definir quem escreve em cada camada e os paths por execução.

Canonical policy: [docs/MULTIAGENT_ENGINEERING_LOOP.md](../../docs/MULTIAGENT_ENGINEERING_LOOP.md) §6.

## Layout

```
.cursor/memory/
├── README.md
├── work/                 # Per-run drafts (each role writes only under its folder)
│   └── <correlation-id>/
│       ├── briefing.md
│       ├── intake/
│       ├── planner/
│       ├── architect/
│       ├── engineer/
│       ├── executor/
│       └── reviewer/
├── durable/              # Validated facts — orchestrator ONLY
│   └── .gitkeep
└── log/                  # Append-only audit lines
    └── .gitkeep
```

## Rules

- Correlation ID: `run-<YYYYMMDD>-<short-hash>`
- Every record: author (role), date (ISO), source
- Never store secrets, tokens, passwords, or PII
- Agents must not write outside their role folder under `work/`
- Only `@orchestrator` / `/multiagent` consolidates into `durable/`
- `log/` is append-only (new line or new file per event; no edits/deletes)

## Minimal log line

```text
<ISO8601> | <correlation-id> | <role> | <action> | <result-summary>
```
