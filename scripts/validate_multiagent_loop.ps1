# Validate multi-agent engineering loop scaffold (Windows-friendly).
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$failures = @()

$requiredFiles = @(
  "docs/MULTIAGENT_ENGINEERING_LOOP.md",
  "docs/MULTIAGENT_ENGINEERING_LOOP.pt-BR.md",
  "docs/MULTIAGENT_LOOP_CHECKLIST.md",
  ".cursor/rules/core-rules/multiagent-loop-always.mdc",
  ".cursor/skills/multiagent-loop/SKILL.md",
  ".cursor/commands/multiagent.md",
  ".cursor/commands/plano-otimizado.md",
  ".cursor/commands/review.md",
  ".cursor/PARALLEL_AGENTS.md",
  ".cursor/MODEL_SELECTION_GUIDE.md",
  ".cursor/models/catalog.yaml",
  ".cursor/models/README.md",
  ".cursor/memory/README.md",
  ".claude/commands/multiagent.md",
  ".claude/commands/plano.md",
  ".claude/commands/review.md",
  ".claude/memory/README.md"
)

foreach ($rel in $requiredFiles) {
  if (-not (Test-Path (Join-Path $Root $rel))) { $failures += "missing file: $rel" }
}

$roles = @("intake", "orchestrator", "planner", "architect", "engineer", "executor", "reviewer")
foreach ($role in $roles) {
  foreach ($base in @(".cursor/agents", ".claude/agents")) {
    $rel = "$base/$role.md"
    if (-not (Test-Path (Join-Path $Root $rel))) { $failures += "missing agent: $rel" }
  }
}

$memoryDirs = @(
  ".cursor/memory/work",
  ".cursor/memory/durable",
  ".cursor/memory/log",
  ".claude/memory/work",
  ".claude/memory/durable",
  ".claude/memory/log"
)
foreach ($rel in $memoryDirs) {
  if (-not (Test-Path (Join-Path $Root $rel))) { $failures += "missing dir: $rel" }
}

$plan = Join-Path $Root ".cursor/plans/example-feature_a1b2c3d4.plan.md"
if (-not (Test-Path $plan)) {
  $failures += "missing file: .cursor/plans/example-feature_a1b2c3d4.plan.md"
} elseif ((Get-Content $plan -Raw) -notmatch "(?i)Acceptance criteria") {
  $failures += "example plan missing acceptance criteria"
}

$catalog = Join-Path $Root ".cursor/models/catalog.yaml"
if (-not (Test-Path $catalog)) {
  $failures += "missing file: .cursor/models/catalog.yaml"
} else {
  $catalogText = Get-Content $catalog -Raw
  foreach ($marker in @("schema_version:", "models:", "role_defaults:", "escalation:")) {
    if ($catalogText -notmatch [regex]::Escape($marker)) {
      $failures += "model catalog missing marker: $marker"
    }
  }
}

if ($failures.Count -gt 0) {
  Write-Host "FAIL — multi-agent loop scaffold"
  $failures | ForEach-Object { Write-Host "  - $_" }
  exit 1
}

Write-Host "PASS — multi-agent loop scaffold"
Write-Host ("  checked {0} files, {1} roles x2, {2} memory dirs, model catalog" -f $requiredFiles.Count, $roles.Count, $memoryDirs.Count)
exit 0
