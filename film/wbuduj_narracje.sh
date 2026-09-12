#!/usr/bin/env bash
# Wbudowuje gotowe nagranie narracji (Twój głos z ElevenLabs, jeden lub kilka plików MP3 w kolejności)
# do filmu: skleja części → film/narracja.mp3 → kopia do film/remotion/public → (opcjonalnie) render MP4.
# Użycie:  bash film/wbuduj_narracje.sh czesc1.mp3 [czesc2.mp3 ...]
#          RENDER=1 bash film/wbuduj_narracje.sh czesc1.mp3        # od razu render Remotion
set -euo pipefail
cd "$(dirname "$0")/.."
[ $# -ge 1 ] || { echo "podaj co najmniej jeden plik MP3 z narracją"; exit 2; }
FF="${FFMPEG:-$(python3 -c 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())' 2>/dev/null || command -v ffmpeg)}"
[ -x "$FF" ] || { echo "brak ffmpeg"; exit 3; }
OUT=film/out; mkdir -p "$OUT"
LISTA="$OUT/czesci.txt"; : > "$LISTA"
for f in "$@"; do [ -f "$f" ] || { echo "nie ma pliku: $f"; exit 4; }; printf "file '%s'\n" "$(realpath "$f")" >> "$LISTA"; done
# sklejenie z przekodowaniem do jednolitego MP3 (44,1 kHz, mono, 128 kb/s) – niezależnie od źródeł
"$FF" -y -loglevel error -f concat -safe 0 -i "$LISTA" -ac 1 -ar 44100 -codec:a libmp3lame -b:a 128k film/narracja.mp3
DUR=$( { "$FF" -i film/narracja.mp3 2>&1 || true; } | sed -n 's/.*Duration: \([0-9:.]*\).*/\1/p')
echo "narracja.mp3: $DUR (części: $#)"
mkdir -p film/remotion/public/foto film/remotion/public/awatar
cp film/narracja.mp3 film/remotion/public/narracja.mp3
cp film/ocena_funkcjonalna_film.html film/remotion/public/
cp film/foto/*.webp film/remotion/public/foto/
cp film/awatar/ewa_pctp.png film/awatar/ewa_pctp_intro.webm film/remotion/public/awatar/
[ -f "$OUT/napisy.srt" ] && cp "$OUT/napisy.srt" film/remotion/public/napisy.srt || true
[ -f "$OUT/awatar.mp4" ] && cp "$OUT/awatar.mp4" film/remotion/public/awatar.mp4 || true
echo "film HTML wczyta narracja.mp3 sam (leży obok pliku filmu)."
if [ "${RENDER:-0}" = "1" ]; then
  BR="${REMOTION_BROWSER:-$(find /opt/pw-browsers -maxdepth 3 -type f -name headless_shell 2>/dev/null | head -1)}"
  cd film/remotion && npx remotion render OcenaFunkcjonalna ../out/film.mp4 ${BR:+--browser-executable="$BR"} --concurrency=2
  echo "gotowe → film/out/film.mp4"
fi
