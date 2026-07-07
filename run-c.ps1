param(
    [switch]$BuildOnly,
    [Parameter(Position = 0)]
    [string]$SourceFile,
    [Parameter(Position = 1, ValueFromRemainingArguments = $true)]
    [string[]]$ProgramArgs
)

$ErrorActionPreference = "Stop"

function Test-Cs50SourceDir {
    param([AllowEmptyString()][string]$Path)

    if (-not $Path) {
        return $false
    }

    return (Test-Path -LiteralPath (Join-Path $Path "cs50.h")) -and (Test-Path -LiteralPath (Join-Path $Path "cs50.c"))
}

function Find-Cs50SourceDir {
    param([string]$SourceFile)

    if ($env:CS50_SRC_DIR -and (Test-Cs50SourceDir $env:CS50_SRC_DIR)) {
        return $env:CS50_SRC_DIR
    }

    $scriptCandidate = Join-Path $PSScriptRoot "AIEngineeringRoadmap\stage-01-cs-foundations\libcs50\src"
    if (Test-Cs50SourceDir $scriptCandidate) {
        return $scriptCandidate
    }

    $current = Split-Path -Parent $SourceFile
    while ($current) {
        $candidates = @(
            (Join-Path $current "libcs50\src"),
            (Join-Path $current "stage-01-cs-foundations\libcs50\src"),
            (Join-Path $current "AIEngineeringRoadmap\stage-01-cs-foundations\libcs50\src")
        )

        foreach ($candidate in $candidates) {
            if (Test-Cs50SourceDir $candidate) {
                return $candidate
            }
        }

        $parent = Split-Path -Parent $current
        if ($parent -eq $current) {
            break
        }
        $current = $parent
    }

    return $null
}

function Resolve-Gcc {
    $localGcc = "C:\tools\msys64\mingw64\bin\gcc.exe"
    if (Test-Path -LiteralPath $localGcc) {
        return $localGcc
    }

    return "gcc"
}

$resolvedSourceFile = $null
$candidateSourceFile = if ($SourceFile) { $SourceFile.Trim('"') } else { $null }

if ($candidateSourceFile -and (Test-Path -LiteralPath $candidateSourceFile) -and ([IO.Path]::GetExtension($candidateSourceFile) -eq ".c")) {
    $resolvedSourceFile = $candidateSourceFile
}

if (-not $resolvedSourceFile) {
    $defaultSearchFile = Join-Path $PSScriptRoot "stage-01-cs-foundations\Algorithms - CS50\search.c"
    if (Test-Path -LiteralPath $defaultSearchFile) {
        $resolvedSourceFile = $defaultSearchFile
    }
}

if (-not $resolvedSourceFile) {
    throw "Pass a .c file path to run-c.ps1, for example: .\run-c.ps1 .\main.c"
}

$resolvedSourceFile = (Resolve-Path $resolvedSourceFile).Path
$outputFile = [IO.Path]::ChangeExtension($resolvedSourceFile, ".exe")
$compiler = Resolve-Gcc
$compileArgs = @()

$sourceText = Get-Content -Raw $resolvedSourceFile
$usesCs50 = $sourceText -match '#\s*include\s*[<"]cs50\.h[>"]'

if ($usesCs50) {
    $cs50SourceDir = Find-Cs50SourceDir $resolvedSourceFile
    if (-not $cs50SourceDir) {
        throw "This file includes cs50.h, but no libcs50/src folder was found. Set CS50_SRC_DIR to the folder containing cs50.h and cs50.c."
    }

    $compileArgs += "-I$cs50SourceDir"
    $compileArgs += $resolvedSourceFile
    $compileArgs += (Join-Path $cs50SourceDir "cs50.c")
} else {
    $compileArgs += $resolvedSourceFile
}

$compileArgs += "-o"
$compileArgs += $outputFile

& $compiler @compileArgs
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

if ($BuildOnly) {
    exit 0
}

$number = $ProgramArgs | Where-Object { $_ -match '^-?\d+$' } | Select-Object -First 1

if ($number) {
    $number | & $outputFile
} else {
    & $outputFile
}
