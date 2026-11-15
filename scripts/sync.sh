#!/usr/bin/env bash
# Sync the CareCatalyst repo: commit local changes, pull (rebase), push, update submodules.
# The repo is PUBLIC: the deck, its PDFs, pitch drafts and submission texts are never auto-committed.
set -u
cd "$(dirname "$0")/.."
EXCLUDE=(':(exclude)presentation/deck.html' ':(exclude,glob)presentation/deck-*.html' ':(exclude)presentation/*.pdf' ':(exclude,glob)pitch/**'
         ':(exclude,glob)**/SUBMISSION*' ':(exclude,glob)**/DEV_BLOGPOST*' ':(exclude,glob)**/RUNBOOK*' ':(exclude,glob)**/.env*')
git add -A -- . "${EXCLUDE[@]}"
git diff --cached --quiet || git commit -q -m "Sync: work in progress ($(date '+%H:%M'))"
git pull -q --rebase --autostash || { echo "PULL CONFLICT - resolve manually, never drop someone else's version"; exit 1; }
git push -q || { echo "PUSH FAILED"; exit 1; }
git log --oneline -1
