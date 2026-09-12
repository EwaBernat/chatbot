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
# każda część osobno: wyrównanie głośności (EBU R128, -16 LUFS) i przycięcie ciszy na końcu do ok. 0,6 s,
# żeby akapity brzmiały jednakowo głośno, a pauzy między nimi były równe
NORM="$OUT/czesci_norm"; rm -rf "$NORM"; mkdir -p "$NORM"; : > "$LISTA"; i=0
for f in "$@"; do i=$((i+1)); n=$(printf "%s/cz%02d.wav" "$NORM" "$i")
  "$FF" -y -loglevel error -i "$f" -af "areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,apad=pad_dur=0.6,loudnorm=I=-16:TP=-1.5:LRA=9" -ac 1 -ar 44100 "$n"
  printf "file '%s'\n" "$(realpath "$n")" >> "$LISTA"
done
"$FF" -y -loglevel error -f concat -safe 0 -i "$LISTA" -ac 1 -ar 44100 -codec:a libmp3lame -b:a 128k film/narracja.mp3
# granice między częściami (skumulowane długości, bez ostatniej) → napisy_z_pauz.py traktuje je jako pewne granice scen
: > "$OUT/czesci_czasy.txt"; SUMA=0
for f in "$NORM"/cz*.wav; do
  D=$("$FF" -i "$f" -f null - 2>&1 | sed -n 's/.*time=\([0-9:.]*\) bitrate.*/\1/p' | tail -1)
  SEK=$(echo "$D" | awk -F: '{ printf "%.3f", $1*3600+$2*60+$3 }')
  SUMA=$(awk -v a="$SUMA" -v b="$SEK" 'BEGIN{ printf "%.3f", a+b }')
  echo "$SUMA" >> "$OUT/czesci_czasy.txt"
done
sed -i '$d' "$OUT/czesci_czasy.txt"   # ostatnia wartość to koniec nagrania, nie granica
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
