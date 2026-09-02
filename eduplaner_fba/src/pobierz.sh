#!/bin/sh
# Pobranie wygenerowanych obrazów albo nagrań: na wejściu pary „kod URL"
# (jedna para w wierszu), na wyjściu pliki <katalog>/<kod>.<rozszerzenie>.
#
#   sh src/pobierz.sh assets/pomoce_fba png < pary.txt
#
# Linki z ElevenLabs są podpisane i wygasają po dwóch godzinach — pobieramy
# od razu po zakończeniu generowania, a nie „później".
KAT="$1"; EXT="$2"; mkdir -p "$KAT"
while read -r KOD URL; do
  [ -z "$KOD" ] && continue
  curl -sS -o "$KAT/$KOD.$EXT" "$URL" || { echo "BŁĄD $KOD"; continue; }
  echo "$KOD $(wc -c < "$KAT/$KOD.$EXT") B"
done
