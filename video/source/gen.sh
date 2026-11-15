#!/bin/bash
# usage: gen.sh N
cd "$(dirname "$0")"
BASE=$(grep '^BASE:' prompts.txt | cut -d: -f2-)
P=$(grep "^$1|" prompts.txt | cut -d'|' -f2-)
codex exec --skip-git-repo-check -s read-only -- "Generate exactly ONE image with your image generation tool. $BASE Scene: $P" > img/log_$1.txt 2>&1
echo done $1
