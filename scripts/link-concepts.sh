#!/usr/bin/env bash
# Links the two concept repos as git submodules.
# Usage: ./scripts/link-concepts.sh <concept-A-today-url> <concept-B-vision-url>
set -euo pipefail

if [ $# -ne 2 ]; then
  echo "Usage: $0 <concept-A-today-url> <concept-B-vision-url>" >&2
  exit 1
fi

cd "$(git rev-parse --show-toplevel)"

for pair in "today|$1" "vision|$2"; do
  name="${pair%%|*}"
  url="${pair#*|}"
  path="concepts/$name"
  # remove placeholder folder before adding the submodule
  if [ -f "$path/PLACEHOLDER.md" ]; then
    git rm -rq "$path"
    rm -rf "$path"
  fi
  git submodule add "$url" "$path"
done

git commit -m "Link concept repos as submodules"
echo "Done. Push with: git push"
