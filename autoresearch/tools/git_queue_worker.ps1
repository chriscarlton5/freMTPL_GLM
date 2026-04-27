param(
  [string]$RepoRoot = "",
  [int]$PollSeconds = 2,
  [switch]$Once
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($RepoRoot)) {
  $RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
} else {
  $RepoRoot = (Resolve-Path $RepoRoot).Path
}

$QueueDir = Join-Path $RepoRoot "autoresearch\scratch\git_queue"
$DoneDir = Join-Path $RepoRoot "autoresearch\scratch\git_done"
$FailedDir = Join-Path $RepoRoot "autoresearch\scratch\git_failed"

New-Item -ItemType Directory -Path $QueueDir -Force | Out-Null
New-Item -ItemType Directory -Path $DoneDir -Force | Out-Null
New-Item -ItemType Directory -Path $FailedDir -Force | Out-Null

function Test-PathInsideRepo {
  param([string]$RelativePath)

  if ([System.IO.Path]::IsPathRooted($RelativePath)) {
    throw "Job path must be relative, got absolute path: $RelativePath"
  }
  if ($RelativePath -match '(^|[\\/])\.\.([\\/]|$)') {
    throw "Job path must not traverse upward: $RelativePath"
  }

  $full = [System.IO.Path]::GetFullPath((Join-Path $RepoRoot $RelativePath))
  $rootFull = [System.IO.Path]::GetFullPath($RepoRoot)
  if (-not $full.StartsWith($rootFull, [System.StringComparison]::OrdinalIgnoreCase)) {
    throw "Job path escapes repo: $RelativePath"
  }
  if (-not (Test-Path -LiteralPath $full)) {
    throw "Job path does not exist: $RelativePath"
  }
}

function Move-JobFile {
  param(
    [string]$JobPath,
    [string]$DestinationDir,
    [string]$Suffix
  )

  $stamp = Get-Date -Format "yyyyMMdd_HHmmss"
  $name = [System.IO.Path]::GetFileNameWithoutExtension($JobPath)
  $dest = Join-Path $DestinationDir "$stamp`_$name`_$Suffix.json"
  Move-Item -LiteralPath $JobPath -Destination $dest -Force
}

function Invoke-GitQueueJob {
  param([string]$JobPath)

  Write-Host "Processing git job: $JobPath"
  $job = Get-Content -LiteralPath $JobPath -Raw | ConvertFrom-Json

  if ([string]::IsNullOrWhiteSpace($job.message)) {
    throw "Job is missing message."
  }
  if ($null -eq $job.paths -or $job.paths.Count -eq 0) {
    throw "Job is missing paths."
  }

  [string[]]$paths = @($job.paths | ForEach-Object { [string]$_ })
  foreach ($path in $paths) {
    Test-PathInsideRepo -RelativePath $path
  }

  & git -C $RepoRoot status --short
  if ($LASTEXITCODE -ne 0) { throw "git status failed." }

  & git -C $RepoRoot add -- @paths
  if ($LASTEXITCODE -ne 0) { throw "git add failed." }

  & git -C $RepoRoot diff --cached --quiet
  $hasChanges = $LASTEXITCODE -ne 0
  if ($hasChanges) {
    & git -C $RepoRoot commit -m $job.message
    if ($LASTEXITCODE -ne 0) { throw "git commit failed." }
  } else {
    Write-Host "No staged changes for job; skipping commit."
  }

  if ($job.push -eq $true) {
    & git -C $RepoRoot push
    if ($LASTEXITCODE -ne 0) { throw "git push failed." }
  }

  Move-JobFile -JobPath $JobPath -DestinationDir $DoneDir -Suffix "done"
}

Write-Host "Git queue worker running for repo: $RepoRoot"
Write-Host "Queue: $QueueDir"

while ($true) {
  $jobs = Get-ChildItem -LiteralPath $QueueDir -Filter "*.json" -File | Sort-Object Name
  foreach ($job in $jobs) {
    try {
      Invoke-GitQueueJob -JobPath $job.FullName
    } catch {
      Write-Host "Job failed: $($job.FullName)" -ForegroundColor Red
      Write-Host $_.Exception.Message -ForegroundColor Red
      Move-JobFile -JobPath $job.FullName -DestinationDir $FailedDir -Suffix "failed"
    }
  }

  if ($Once) {
    break
  }
  Start-Sleep -Seconds $PollSeconds
}
