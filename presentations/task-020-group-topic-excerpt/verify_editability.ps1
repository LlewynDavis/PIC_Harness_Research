$ErrorActionPreference = 'Stop'
$finalDeck = Join-Path $PSScriptRoot 'Harness_课题介绍_原理与案例_模板版.pptx'
$buildDir = Join-Path $PSScriptRoot 'build'
New-Item -ItemType Directory -Force -Path $buildDir | Out-Null
$testDeck = Join-Path $buildDir 'editability-test.pptx'
$beforeHash = (Get-FileHash -LiteralPath $finalDeck -Algorithm SHA256).Hash
$app = New-Object -ComObject PowerPoint.Application
$pres = $null
try {
    $pres = $app.Presentations.Open($finalDeck,$true,$false,$false)
    $text = $pres.Slides.Item(1).Shapes.Item('Editable_Module_1_Body')
    $text.TextFrame.TextRange.Text = 'EDIT CHECK'
    $picture = $pres.Slides.Item(2).Shapes.Item('PaperOriginal_Kharel_Fig2a')
    $expectedLeft = $picture.Left + 7.2
    $picture.Left = $expectedLeft
    $pres.SaveCopyAs($testDeck,24)
    $pres.Close()
    $pres = $app.Presentations.Open($testDeck,$true,$false,$false)
    if ($pres.Slides.Item(1).Shapes.Item('Editable_Module_1_Body').TextFrame.TextRange.Text -ne 'EDIT CHECK') { throw 'Text edit did not persist' }
    if ([Math]::Abs($pres.Slides.Item(2).Shapes.Item('PaperOriginal_Kharel_Fig2a').Left - $expectedLeft) -gt 0.05) { throw 'Picture move did not persist' }
    Write-Output 'PASS: native text edit and independent figure move persisted after save/reopen.'
}
finally {
    if ($null -ne $pres) { $pres.Close() }
    if ($app.Presentations.Count -eq 0) { $app.Quit() }
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($app) | Out-Null
}
if ((Get-FileHash -LiteralPath $finalDeck -Algorithm SHA256).Hash -ne $beforeHash) { throw 'Final deck unexpectedly changed' }
Write-Output 'PASS: final deck unchanged.'
