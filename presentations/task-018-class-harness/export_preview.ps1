$ErrorActionPreference = 'Stop'
$deckPath = Join-Path $PSScriptRoot 'build\agent-harness.pptx'
$previewPath = Join-Path $PSScriptRoot 'renders'
New-Item -ItemType Directory -Force -Path $previewPath | Out-Null
$powerPoint = New-Object -ComObject PowerPoint.Application
$presentation = $null
try {
    $presentation = $powerPoint.Presentations.Open($deckPath, $true, $false, $false)
    $presentation.Export($previewPath, 'PNG', 1600, 900)
    $presentation.SaveAs((Join-Path $PSScriptRoot 'Harness_课堂汇报_初版.pdf'), 32)
    Copy-Item -LiteralPath $deckPath -Destination (Join-Path $PSScriptRoot 'Harness_课堂汇报_初版.pptx')
    Write-Output ("Exported {0} slides" -f $presentation.Slides.Count)
}
finally {
    if ($null -ne $presentation) { $presentation.Close() }
    if ($powerPoint.Presentations.Count -eq 0) { $powerPoint.Quit() }
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($powerPoint) | Out-Null
}
