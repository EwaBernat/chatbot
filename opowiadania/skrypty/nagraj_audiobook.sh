#!/usr/bin/env bash
# Nagrywa audiobook „Rajmund i Arystoteles" TWOIM głosem — jeden plik MP3 na rozdział.
#
# Warunek: skill dane-i-glos musi mieć zapamiętany Twój głos.
#   sprawdzenie:   python3 .claude/skills/dane-i-glos/scripts/skonfiguruj_glos.py --pokaz
#   ustawienie:    python3 .claude/skills/dane-i-glos/scripts/skonfiguruj_glos.py nagranie.mp3 --nazwa "Ewa - narracja PL"
#
# Uruchomienie z katalogu głównego repozytorium:
#   bash opowiadania/skrypty/nagraj_audiobook.sh        # obie części
#   bash opowiadania/skrypty/nagraj_audiobook.sh 2      # tylko część druga
#
# Skrypt NIE używa cudzego głosu. Bez zapamiętanego głosu elevenlabs_tts.py
# odmawia i kończy się kodem 4 — wtedy nic się nie nagra.
set -euo pipefail

TTS=".claude/skills/dane-i-glos/scripts/elevenlabs_tts.py"

# część 1 albo 2; bez argumentu nagrywa obie
CZESC="${1:-wszystkie}"

nagraj_czesc() {
  local wejscie="$1"
  local wyjscie="$2"
  mkdir -p "$wyjscie"
  for plik in "$wejscie"/rozdzial-*.txt; do
    nazwa="$(basename "$plik" .txt)"
    mp3="$wyjscie/$nazwa.mp3"
    srt="$wyjscie/$nazwa.srt"
    if [ -f "$mp3" ]; then
      echo "pomijam (już jest): $mp3"
      continue
    fi
    echo "nagrywam: $nazwa"
    python3 "$TTS" "$plik" -o "$mp3" --srt "$srt" --speed 0.95
  done
  echo "Gotowe: $wyjscie"
}

if [ "$CZESC" = "1" ] || [ "$CZESC" = "wszystkie" ]; then
  nagraj_czesc "opowiadania/audio/scenariusz" "opowiadania/audio/czesc-1"
fi
if [ "$CZESC" = "2" ] || [ "$CZESC" = "wszystkie" ]; then
  nagraj_czesc "opowiadania/audio/scenariusz-czesc-2" "opowiadania/audio/czesc-2"
fi
