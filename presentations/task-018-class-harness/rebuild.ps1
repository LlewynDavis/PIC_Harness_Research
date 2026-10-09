$ErrorActionPreference = 'Stop'
$researchRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$runtimeRoot = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies'
$deckPython = Join-Path $runtimeRoot 'python\python.exe'
$skillRoot = Join-Path $env:USERPROFILE '.codex\skills\presentation-skill'
$env:PATH = (Join-Path $runtimeRoot 'node\bin') + ';' + $env:PATH
$env:PPTX_NODE_MODULES = Join-Path $runtimeRoot 'node\node_modules'
Push-Location $researchRoot
try {
    & $deckPython (Join-Path $PSScriptRoot 'build_source_editable.py')
    if ($LASTEXITCODE -ne 0) { throw 'Source generation failed' }
    & (Join-Path $runtimeRoot 'node\bin\node.exe') (Join-Path $PSScriptRoot 'build_native.cjs') --outline (Join-Path $PSScriptRoot 'outline.json') --output (Join-Path $PSScriptRoot 'build\agent-harness.pptx') --style-preset lab-report
    if ($LASTEXITCODE -ne 0) { throw 'Native PPT build failed' }
    & $deckPython (Join-Path $skillRoot 'scripts\qa_gate.py') --input (Join-Path $PSScriptRoot 'build\agent-harness.pptx') --outdir (Join-Path $PSScriptRoot 'build\qa') --style-preset lab-report --strict-geometry --skip-render --fail-on-visual-warnings --fail-on-design-warnings
    if ($LASTEXITCODE -ne 0) { throw 'PPT build or QA failed' }
    & (Join-Path $PSScriptRoot 'export_preview.ps1')
    & $deckPython (Join-Path $PSScriptRoot 'verify_native.py')
    if ($LASTEXITCODE -ne 0) { throw 'Native object verification failed' }
}
finally { Pop-Location }
