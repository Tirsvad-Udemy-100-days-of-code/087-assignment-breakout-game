#!/usr/bin/env bash
# Local security scan with opengrep. Run it before every push.
# Usage: bash scripts/scan.sh
# Env:   OPENGREP  path of the opengrep executable
#        (default: ~/.opengrep/cli/latest/opengrep.exe)
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
opengrep="${OPENGREP:-$HOME/.opengrep/cli/latest/opengrep.exe}"

if [[ ! -x "$opengrep" ]]; then
  echo "opengrep not found at $opengrep (set OPENGREP)" >&2
  exit 2
fi

cd "$root"
targets=()
for dir in src tests scripts tools; do
  [[ -d "$dir" ]] && targets+=("$dir")
done

"$opengrep" scan --config auto --severity ERROR --error --quiet "${targets[@]}"
echo "opengrep: no error-severity finding in ${targets[*]}"
