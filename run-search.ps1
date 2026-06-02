param(
    [Parameter(Position = 0, ValueFromRemainingArguments = $true)]
    [string[]]$ProgramArgs
)

$ErrorActionPreference = "Stop"

$projectRoot = $PSScriptRoot
$searchFile = Join-Path $projectRoot "stage-01-cs-foundations\Algorithms - CS50\search.c"
& (Join-Path $projectRoot "run-c.ps1") $searchFile @ProgramArgs
