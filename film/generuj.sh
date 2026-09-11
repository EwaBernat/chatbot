#!/usr/bin/env bash
# Potok produkcji filmu: narracja → Twój głos (ElevenLabs) → Twój awatar (HeyGen) → MP4 (Remotion).
# Uruchamiaj z katalogu repozytorium:  bash film/generuj.sh [etap]
#   etapy: glos | awatar | remotion | wszystko (domyślnie)
# Klucze wyłącznie w zmiennych środowiskowych: ELEVENLABS_API_KEY, HEYGEN_API_KEY, HEYGEN_AVATAR_ID.
set -euo pipefail
cd "$(dirname "$0")/.."
SK=.claude/skills/dane-i-glos/scripts
OUT=film/out; mkdir -p "$OUT"
ETAP="${1:-wszystko}"

glos() {
  # Skrypt odmawia, gdy skill nie ma zapamiętanego Twojego głosu (kod 4). Najpierw:
  #   python3 $SK/skonfiguruj_glos.py nagranie.mp4 --nazwa "Ewa - narracja PL"
  python3 "$SK/skonfiguruj_glos.py" --pokaz
  python3 "$SK/elevenlabs_tts.py" film/narracja.txt -o "$OUT/narracja.mp3" --srt "$OUT/napisy.srt" \
          --model eleven_multilingual_v2 --stability 0.6 --similarity 0.75 --speed 0.97
}

awatar() {
  : "${HEYGEN_AVATAR_ID:?Ustaw HEYGEN_AVATAR_ID (python3 $SK/heygen_awatar.py --awatary)}"
  python3 "$SK/heygen_awatar.py" --audio "$OUT/narracja.mp3" --avatar-id "$HEYGEN_AVATAR_ID" \
          --styl circle --tlo "#2D1B69" --czekaj -o "$OUT/awatar.mp4"
}

remotion() {
  python3 film/build_film.py
  mkdir -p film/remotion/public/foto
  cp film/ocena_funkcjonalna_film.html film/remotion/public/
  cp film/foto/*.webp film/remotion/public/foto/
  [ -f "$OUT/narracja.mp3" ] && cp "$OUT/narracja.mp3" film/remotion/public/ || echo "brak narracja.mp3 – film bez głosu nie powstanie (zasada: tylko Twój głos)"
  [ -f "$OUT/napisy.srt" ]   && cp "$OUT/napisy.srt"   film/remotion/public/ || true
  [ -f "$OUT/awatar.mp4" ]   && cp "$OUT/awatar.mp4"   film/remotion/public/ || echo "brak awatar.mp4 – w kole zostanie miejsce na awatar"
  [ -f "$OUT/narracja.mp3" ] || exit 4
  cd film/remotion && npm install && npx remotion render OcenaFunkcjonalna ../out/film.mp4 \
      --browser-executable="${REMOTION_BROWSER:-}" 2>/dev/null || npx remotion render OcenaFunkcjonalna ../out/film.mp4
}

case "$ETAP" in
  glos) glos ;;
  awatar) awatar ;;
  remotion) remotion ;;
  wszystko) glos; awatar; remotion ;;
  *) echo "etap: glos | awatar | remotion | wszystko"; exit 2 ;;
esac
echo "gotowe → $OUT"
