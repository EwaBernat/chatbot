#!/usr/bin/env bash
# Renderuje oba filmy. Skalę można podać jako pierwszy argument (1 = 1080p, 0.6667 = 720p).
set -u
SKALA="${1:-1}"
SUFIKS="${2:-}"
export REMOTION_CHROMIUM="${REMOTION_CHROMIUM:-/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell}"
cd "$(dirname "$0")/.."
node scripts/oblicz-czas.mjs
npx remotion render CzescI  "out/mosty-czesc1-przedszkole${SUFIKS}.mp4" --scale="$SKALA" --jpeg-quality=82 --log=info
npx remotion render CzescII "out/mosty-czesc2-klasy1-3${SUFIKS}.mp4"  --scale="$SKALA" --jpeg-quality=82 --log=info
echo "GOTOWE"
