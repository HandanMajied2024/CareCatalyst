#!/usr/bin/env bash
# Sync the CareCatalyst repo: commit local changes, pull (rebase), push, update submodules.
# The repo is PUBLIC: secrets (.env) are never committed. Since the submission (15.11.) everything else is shared.
set -u
cd "$(dirname "$0")/.."
EXCLUDE=(':(exclude,glob)**/.env*')
git add -A -- . "${EXCLUDE[@]}"
git diff --cached --quiet || git commit -q -m "Sync: work in progress ($(date '+%H:%M'))"
git pull -q --rebase --autostash || { echo "PULL CONFLICT - resolve manually, never drop someone else's version"; exit 1; }
git push -q || { echo "PUSH FAILED"; exit 1; }
git log --oneline -1
