$ErrorActionPreference = 'Stop'
$taskRoot = Split-Path -Parent $PSScriptRoot
$taskOutput = Join-Path $taskRoot 'tmp/task-017'
New-Item -ItemType Directory -Force -Path "$taskOutput/docx", "$taskOutput/slides" | Out-Null
$taskDocx = Join-Path $taskRoot 'output/task-007/面向光子芯片智能设计的三方向技术调研_飞书上传版.docx'
$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    $doc = $word.Documents.Open($taskDocx, $false, $true)
    $doc.ExportAsFixedFormat("$taskOutput/docx/report.pdf", 17)
    $doc.Close(0)
} finally { $word.Quit() }
$taskWorkspace = Join-Path $taskRoot 'presentations/task-010-group-meeting-rebuild'
$taskDeck = "$taskWorkspace/build/deck-workspace.pptx"
$powerpoint = New-Object -ComObject PowerPoint.Application
try {
    $deck = $powerpoint.Presentations.Open($taskDeck, $true, $false, $false)
    for ($i = 1; $i -le $deck.Slides.Count; $i++) {
        $deck.Slides.Item($i).Export("$taskOutput/slides/slide-$i.png", 'PNG', 1920, 1080)
    }
    $deck.SaveAs("$taskOutput/slides/deck.pdf", 32)
    $deck.Close()
} finally { $powerpoint.Quit() }
Write-Output 'Read-only Word/PPT rendering completed. Original user PDFs untouched.'
