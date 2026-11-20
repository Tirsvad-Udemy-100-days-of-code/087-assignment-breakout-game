#!/usr/bin/env bash
# Take the screenshot of one development step in a Docker container.
# Usage: bash tools/screenshots/run.sh <step 0-7> <git ref> [output.png]
#   step  the lecture step (0 is the empty window)
#   ref   the commit or branch whose source is played (default: HEAD);
#         WORKTREE plays the files as they are on disk
# The default output is docs/images/step-<step>.png.
set -euo pipefail

step="${1:?usage: run.sh <step 0-7> [git ref] [output.png]}"
ref="${2:-HEAD}"
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
out="${3:-docs/images/step-${step}.png}"
image="breakout-screenshots"

# Play the source of that commit, not the working tree, plus today's capture tool.
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
if [[ "$ref" == "WORKTREE" ]]; then
  cp -r "$root/src" "$tmp/src"
else
  git -C "$root" archive "$ref" src | tar -x -C "$tmp"
fi
cp "$root/tools/screenshots/capture.py" "$tmp/capture.py"

docker build -q -t "$image" "$root/tools/screenshots" >/dev/null
mkdir -p "$(dirname "$root/$out")"
touch "$tmp/out.png"
# The container runs as a non-root user and must write the picture.
chmod -R a+rwX "$tmp"

winpath() { if command -v cygpath >/dev/null; then cygpath -m "$1"; else echo "$1"; fi; }

MSYS_NO_PATHCONV=1 docker run --rm \
  -v "$(winpath "$tmp"):/work" \
  -e PYTHONPATH=/work/src \
  "$image" python /work/capture.py "$step" /work/out.png

cp "$tmp/out.png" "$root/$out"
echo "saved $out"
