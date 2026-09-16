$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
Push-Location $repoRoot
try {
    if (-not (Test-Path ".venv\Scripts\python.exe")) {
        & "$PSScriptRoot\setup.ps1"
    }
    & .\.venv\Scripts\python.exe -m mkdocs build --strict
    if ($LASTEXITCODE -ne 0) {
        throw "mkdocs build --strict failed"
    }
    & .\.venv\Scripts\python.exe -m mkdocs serve --dev-addr 127.0.0.1:8000
}
finally {
    Pop-Location
}
