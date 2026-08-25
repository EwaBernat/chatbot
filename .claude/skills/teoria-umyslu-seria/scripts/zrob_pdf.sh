#!/usr/bin/env bash
# Renderuje broszurę do PDF gotowego do druku (A4, bez nagłówków przeglądarki).
#   bash zrob_pdf.sh broszura.html broszura.pdf
set -euo pipefail
WE="${1:?podaj plik HTML}"; WY="${2:-${WE%.html}.pdf}"

CH="$(command -v chromium || command -v chromium-browser || command -v google-chrome || true)"
if [ -z "$CH" ]; then
  CH="$(ls -d /opt/pw-browsers/chromium-*/chrome-linux/chrome 2>/dev/null | tail -1 || true)"
fi
[ -n "$CH" ] || { echo "Nie znalazłem Chromium/Chrome."; exit 1; }

"$CH" --headless --no-sandbox --disable-gpu --virtual-time-budget=10000 \
      --print-to-pdf="$WY" --no-pdf-header-footer "file://$(cd "$(dirname "$WE")" && pwd)/$(basename "$WE")" 2>/dev/null

STRON_PDF=$(python3 -c "import re,sys;d=open(sys.argv[1],'rb').read();print(len(re.findall(rb'/Type\s*/Page[^s]',d)))" "$WY")
STRON_HTML=$(grep -c '<section class="page' "$WE" || true)
echo "PDF: $WY"
echo "Stron w PDF: $STRON_PDF   sekcji .page w HTML: $STRON_HTML"
[ "$STRON_PDF" = "$STRON_HTML" ] || echo "UWAGA: liczby się nie zgadzają — sprawdź przepełnienie stron (sprawdz_strony.py)."
