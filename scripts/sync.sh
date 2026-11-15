#!/usr/bin/env bash
# Sync the CareCatalyst repo: commit local changes, pull (rebase), push, update submodules.
set -u
cd "$(dirname "$0")/.."
git add -A
git diff --cached --quiet || git commit -q -m "Sync: work in progress ($(date '+%H:%M'))"
git pull -q --rebase --autostash || { echo "PULL CONFLICT - resolve manually"; exit 1; }
git push -q || { echo "PUSH FAILED"; exit 1; }
git submodule update --init --remote -q 2>/dev/null || true
git log --oneline -1
