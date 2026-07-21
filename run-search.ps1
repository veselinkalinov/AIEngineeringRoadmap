param(
    [Parameter(Position = 0, ValueFromRemainingArguments = $true)]
    [string[]]$ProgramArgs
)

$ErrorActionPreference = "Stop"

$projectRoot = $PSScriptRoot
$searchFile = Join-Path $projectRoot "stage-03-data-structures-algorithms\Data Structures and Alghorithms\Algorithms - CS50\asympthotic notation\linear_search.c"
& (Join-Path $projectRoot "run-c.ps1") $searchFile @ProgramArgs
