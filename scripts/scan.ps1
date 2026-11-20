<#
.SYNOPSIS
  Local security scan with opengrep. Run it before every push.
.PARAMETER Opengrep
  Path of the opengrep executable.
#>
param(
  [string]$Opengrep = (Join-Path $HOME ".opengrep\cli\latest\opengrep.exe")
)
$ErrorActionPreference = "Stop"
if (-not (Test-Path $Opengrep)) { throw "opengrep not found at $Opengrep" }
Set-Location (Join-Path $PSScriptRoot "..")
$targets = @("src", "tests", "scripts", "tools") | Where-Object { Test-Path $_ }
& $Opengrep scan --config auto --severity ERROR --error --quiet @targets
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Write-Host "opengrep: no error-severity finding in $($targets -join ', ')"
