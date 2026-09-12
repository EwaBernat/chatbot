#!/usr/bin/env bash
# Potok produkcji filmu: narracja → Twój głos (ElevenLabs) → Twój awatar (HeyGen) → MP4 (Remotion).
# Uruchamiaj z katalogu repozytorium:  bash film/generuj.sh [etap]
#   etapy: glos | awatar | remotion | wszystko (domyślnie)
# Klucze wyłącznie w zmiennych środowiskowych: ELEVENLABS_API_KEY, HEYGEN_API_KEY, HEYGEN_AVATAR_ID,
# HEYGEN_VOICE_ID (głos „Ewa - narracja PL” z konta HeyGen: python3 $SK/heygen_awatar.py --glosy --jezyk polish).
set -euo pipefail
cd "$(dirname "$0")/.."
SK=.claude/skills/dane-i-glos/scripts
OUT=film/out; mkdir -p "$OUT"
ETAP="${1:-wszystko}"
# Awatar Ewy PCTP z konta HeyGen (podany przez autorkę); głos „Ewa - narracja PL” podaj w HEYGEN_VOICE_ID.
export HEYGEN_AVATAR_ID="${HEYGEN_AVATAR_ID:-2e72ce3de82f419b8ac71983ab705b59}"
# Pierwszy akapit narracja.txt to intro Ewy (gotowy klip ze skilla) – do nagrania idzie tekst od 2. akapitu.
NARR="$OUT/narracja_bez_intro.txt"; awk -v RS= -v ORS="\n\n" "NR>1" film/narracja.txt > "$NARR"

glos() {
  # Skrypt odmawia, gdy skill nie ma zapamiętanego Twojego głosu (kod 4). Najpierw:
  #   python3 $SK/skonfiguruj_glos.py nagranie.mp4 --nazwa "Ewa - narracja PL"
  python3 "$SK/skonfiguruj_glos.py" --pokaz
  python3 "$SK/elevenlabs_tts.py" "$NARR" -o "$OUT/narracja.mp3" --srt "$OUT/napisy.srt" \
          --model eleven_v3 --stability 0.6 --similarity 0.75 --speed 0.97
}

awatar() {
  # Wariant A (domyślny dla tego filmu): HeyGen czyta narrację głosem „Ewa - narracja PL” z Twojego konta
  # HeyGen – tym samym, którym mówi intro Ewy PCTP. Ścieżkę dźwięku wyciągamy z filmu do narracja.mp3.
  : "${HEYGEN_AVATAR_ID:?Ustaw HEYGEN_AVATAR_ID (python3 $SK/heygen_awatar.py --awatary)}"
  if [ -n "${HEYGEN_VOICE_ID:-}" ]; then
    python3 "$SK/heygen_awatar.py" "$NARR" --avatar-id "$HEYGEN_AVATAR_ID" --voice-id "$HEYGEN_VOICE_ID" \
            --styl circle --tlo "#2D1B69" --czekaj -o "$OUT/awatar.mp4"
    ffmpeg -y -i "$OUT/awatar.mp4" -vn -acodec libmp3lame -q:a 2 "$OUT/narracja.mp3"
  else
    # Wariant B: usta do gotowego MP3 z ElevenLabs (etap glos)
    python3 "$SK/heygen_awatar.py" --audio "$OUT/narracja.mp3" --avatar-id "$HEYGEN_AVATAR_ID" \
            --styl circle --tlo "#2D1B69" --czekaj -o "$OUT/awatar.mp4"
  fi
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
  wszystko) if [ -n "${HEYGEN_VOICE_ID:-}" ]; then awatar; else glos; awatar; fi; remotion ;;
  *) echo "etap: glos | awatar | remotion | wszystko"; exit 2 ;;
esac
echo "gotowe → $OUT"
