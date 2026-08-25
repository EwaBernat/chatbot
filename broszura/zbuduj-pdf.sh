#!/usr/bin/env bash
# Buduje Broszura-szablon-A4.pdf z szablonu HTML.
#   1) osadza fonty Mulish w pliku roboczym,
#   2) drukuje go do PDF przez Chrome/Chromium w trybie headless.
set -euo pipefail
cd "$(dirname "$0")"

python3 narzedzia/osadz-fonty.py

PRZEGLADARKA="${CHROME:-}"
if [ -z "$PRZEGLADARKA" ]; then
  for k in /opt/pw-browsers/chromium google-chrome chromium chromium-browser \
           "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; do
    if command -v "$k" >/dev/null 2>&1 || [ -x "$k" ]; then PRZEGLADARKA="$k"; break; fi
  done
fi
[ -n "$PRZEGLADARKA" ] || { echo "Nie znaleziono Chrome/Chromium. Ustaw CHROME=/sciezka/do/chrome"; exit 1; }

"$PRZEGLADARKA" --headless --disable-gpu --no-sandbox \
  --font-render-hinting=none --run-all-compositor-stages-before-draw \
  --virtual-time-budget=15000 --no-pdf-header-footer \
  --print-to-pdf="Broszura-szablon-A4.pdf" \
  "file://$PWD/szablon-broszury-A4-druk.html" 2>/dev/null

echo "Gotowe: Broszura-szablon-A4.pdf"
