$ErrorActionPreference = 'Stop'
$deckPath = Join-Path $PSScriptRoot 'Harness_课题介绍_原理与案例_模板版.pptx'
$renderPath = Join-Path $PSScriptRoot 'renders'
New-Item -ItemType Directory -Force -Path $renderPath | Out-Null
$app = New-Object -ComObject PowerPoint.Application
$pres = $null
try {
    $pres = $app.Presentations.Open($deckPath,$true,$false,$false)
    Start-Sleep -Milliseconds 1500
    $pres.Export($renderPath,'PNG',1600,900)
    $pres.SaveAs((Join-Path $PSScriptRoot 'Harness_课题介绍_原理与案例_模板版.pdf'),32)
    Write-Output ('Exported '+$pres.Slides.Count+' template slides')
}
finally {
    if ($null -ne $pres) { $pres.Close() }
    if ($app.Presentations.Count -eq 0) { $app.Quit() }
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($app) | Out-Null
}
