$ErrorActionPreference = 'Stop'
$finalDeck = Join-Path $PSScriptRoot 'Harness_课堂汇报_可编辑版.pptx'
$testDeck = Join-Path $PSScriptRoot 'build\editability-test.pptx'
$beforeHash = (Get-FileHash -LiteralPath $finalDeck -Algorithm SHA256).Hash
$app = New-Object -ComObject PowerPoint.Application
$pres = $null
try {
    $pres = $app.Presentations.Open($finalDeck, $true, $false, $false)
    $textShape = $null
    foreach ($shape in $pres.Slides.Item(3).Shapes) {
        if ($shape.HasTextFrame -eq -1 -and $shape.TextFrame.HasText -eq -1) {
            if ($shape.TextFrame.TextRange.Text -eq '自然语言进入设计流程') { $textShape = $shape; break }
        }
    }
    if ($null -eq $textShape) { throw 'Native editable annotation was not found' }
    $textShape.TextFrame.TextRange.Text = '自然语言进入设计流程 EDIT CHECK'
    $picture = $pres.Slides.Item(3).Shapes.Item('PaperOriginal_PhIDO_Fig1')
    $expectedLeft = $picture.Left + 7.2
    $picture.Left = $expectedLeft
    $pres.SaveCopyAs($testDeck, 24)
    $pres.Close()
    $pres = $app.Presentations.Open($testDeck, $true, $false, $false)
    $edited = $false
    foreach ($shape in $pres.Slides.Item(3).Shapes) {
        if ($shape.HasTextFrame -eq -1 -and $shape.TextFrame.HasText -eq -1) {
            if ($shape.TextFrame.TextRange.Text -eq '自然语言进入设计流程 EDIT CHECK') { $edited = $true }
        }
    }
    if (-not $edited) { throw 'Native text edit did not persist' }
    $moved = $pres.Slides.Item(3).Shapes.Item('PaperOriginal_PhIDO_Fig1')
    if ([Math]::Abs($moved.Left - $expectedLeft) -gt 0.05) { throw 'Independent picture move did not persist' }
    Write-Output 'PASS: native Chinese annotation edited; original figure moved; both persisted after save/reopen.'
}
finally {
    if ($null -ne $pres) { $pres.Close() }
    if ($app.Presentations.Count -eq 0) { $app.Quit() }
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($app) | Out-Null
}
$afterHash = (Get-FileHash -LiteralPath $finalDeck -Algorithm SHA256).Hash
if ($afterHash -ne $beforeHash) { throw 'Delivered deck unexpectedly changed during temporary edit test' }
Write-Output 'PASS: delivered deck unchanged.'
