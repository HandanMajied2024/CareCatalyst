#!/bin/bash
# copy video sources (not renders) into the CareCatalyst repo under video/
set -e
SRC="$(cd "$(dirname "$0")" && pwd)"; DST="$SRC/../../CareCatalyst/video"
mkdir -p "$DST/img" "$DST/screens" "$DST/fonts" "$DST/voice" "$DST/sfx"
cp "$SRC"/{record.py,voice.py,lines.json,timeline.js} "$DST/"
sed 's#\.\./screens/#screens/#g' "$SRC/video.html" > "$DST/video.html"
cp "$SRC"/img/eero{1,2,3,4}.jpg "$DST/img/"; cp "$SRC"/fonts/*.woff2 "$DST/fonts/"
cp "$SRC"/voice/*.mp3 "$DST/voice/"; cp "$SRC"/sfx/*.mp3 "$DST/sfx/"
for f in $(grep -o '\.\./screens/[^"]*' "$SRC/video.html" | sort -u); do cp "$SRC/$f" "$DST/screens/"; done
printf 'frames/\n_frames/\n*.mp4\n*.wav\n*.webm\n' > "$DST/.gitignore"
echo synced to $DST
