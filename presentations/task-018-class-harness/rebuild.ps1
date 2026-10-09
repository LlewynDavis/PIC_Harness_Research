$ErrorActionPreference = 'Stop'
$researchRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$runtimeRoot = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies'
$deckPython = Join-Path $runtimeRoot 'python\python.exe'
$skillRoot = Join-Path $env:USERPROFILE '.codex\skills\presentation-skill'
$env:PATH = (Join-Path $runtimeRoot 'node\bin') + ';' + $env:PATH
$env:PPTX_NODE_MODULES = Join-Path $runtimeRoot 'node\node_modules'
Push-Location $researchRoot
try {
    & $deckPython (Join-Path $PSScriptRoot 'build_source_projects.py')
    if ($LASTEXITCODE -ne 0) { throw 'Source generation failed' }
    & $deckPython (Join-Path $skillRoot 'scripts\build_workspace.py') --workspace $PSScriptRoot --qa --skip-render --overwrite
    if ($LASTEXITCODE -ne 0) { throw 'PPT build or QA failed' }
    & (Join-Path $PSScriptRoot 'export_preview.ps1')
}
finally { Pop-Location }
