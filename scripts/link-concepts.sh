#!/usr/bin/env bash
# Links one concept repo as a git submodule.
# Usage: ./scripts/link-concepts.sh <today|vision> <repo-url>
#   today  = Concept A (Care Pathway Agent), already linked: devstar7674-beep/CareCatalyzer
#   vision = Concept B (Personal Health Agent)
set -euo pipefail

if [ $# -ne 2 ] || { [ "$1" != "today" ] && [ "$1" != "vision" ]; }; then
  echo "Usage: $0 <today|vision> <repo-url>" >&2
  exit 1
fi

cd "$(git rev-parse --show-toplevel)"

name="$1"
url="$2"
path="concepts/$name"
# remove placeholder folder before adding the submodule
if [ -f "$path/PLACEHOLDER.md" ]; then
  git rm -rq "$path"
  rm -rf "$path"
fi
git submodule add "$url" "$path"

git commit -m "Link concept repo '$name' as submodule"
echo "Done. Push with: git push"
