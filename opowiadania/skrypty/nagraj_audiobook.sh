#!/usr/bin/env bash
# Nagrywa audiobook „Rajmund i Arystoteles" TWOIM głosem — jeden plik MP3 na rozdział.
#
# Warunek: skill dane-i-glos musi mieć zapamiętany Twój głos.
#   sprawdzenie:   python3 .claude/skills/dane-i-glos/scripts/skonfiguruj_glos.py --pokaz
#   ustawienie:    python3 .claude/skills/dane-i-glos/scripts/skonfiguruj_glos.py nagranie.mp3 --nazwa "Ewa - narracja PL"
#
# Uruchomienie z katalogu głównego repozytorium:
#   bash opowiadania/skrypty/nagraj_audiobook.sh
#
# Skrypt NIE używa cudzego głosu. Bez zapamiętanego głosu elevenlabs_tts.py
# odmawia i kończy się kodem 4 — wtedy nic się nie nagra.
set -euo pipefail

TTS=".claude/skills/dane-i-glos/scripts/elevenlabs_tts.py"
WEJSCIE="opowiadania/audio/scenariusz"
WYJSCIE="opowiadania/audio"

mkdir -p "$WYJSCIE"

for plik in "$WEJSCIE"/rozdzial-*.txt; do
  nazwa="$(basename "$plik" .txt)"
  mp3="$WYJSCIE/$nazwa.mp3"
  srt="$WYJSCIE/$nazwa.srt"
  if [ -f "$mp3" ]; then
    echo "pomijam (już jest): $mp3"
    continue
  fi
  echo "nagrywam: $nazwa"
  python3 "$TTS" "$plik" -o "$mp3" --srt "$srt" --speed 0.95
done

echo "Gotowe. Pliki MP3 i napisy SRT są w $WYJSCIE"
