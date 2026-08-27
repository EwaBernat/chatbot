#!/usr/bin/env bash
# Buduje paczkę dystrybucyjną z aktualnej broszury.
# Uruchamiaj z katalogu głównego repozytorium: bash dystrybucja/zbuduj-paczke.sh
set -euo pipefail

BROSZURA="broszury/maly-ksiaze/maly-ksiaze-broszura.html"
CEL="dystrybucja"
CHROME="${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}"
STRON_W_DEMO=13          # okładka … trzecia strona rozdziału 1

[ -f "$BROSZURA" ] || { echo "Brak $BROSZURA — najpierw złóż broszurę."; exit 1; }

mkdir -p "$CEL"/{pelna,demo,podglad}
cp "$BROSZURA" "$CEL/pelna/maly-ksiaze-broszura.html"

echo "→ PDF pełny"
"$CHROME" --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$CEL/pelna/maly-ksiaze-broszura.pdf" "$BROSZURA" 2>/dev/null

echo "→ fragment demonstracyjny"
python3 - "$BROSZURA" "$CEL/demo/maly-ksiaze-demo.html" "$STRON_W_DEMO" <<'PY'
import re, sys, io
zrodlo, cel, ile = sys.argv[1], sys.argv[2], int(sys.argv[3])
s = io.open(zrodlo, encoding="utf-8").read()
p = s.index('<section class="page')
sekcje = re.findall(r'<section class="page.*?</section>', s[p:], re.S)
nota = ('<section class="page" id="demo-koniec"><h2 class="dzial-h">To jest fragment</h2>'
        f'<p class="lead">Widzisz pierwsze {ile} stron ze {len(sekcje)}. Pełna broszura zawiera '
        'wszystkie 27 rozdziałów, osiem zestawów ćwiczeń, grę planszową z instrukcją, '
        'scenariusz przedstawienia i materiały do wycięcia.</p>'
        '<div class="uwaga jasna"><b>Pomorskie Centrum Terapii Pedagogicznej</b><br>'
        'opracowanie: Mirosława Ewa Jurczyszyn<br>kontakt@eduplaner2026</div></section>')
demo = s[:p] + "\n".join(sekcje[:ile]) + nota + "</body>\n</html>\n"

# z arkusza stylów zostawiamy tylko obrazy, które w demo są naprawdę użyte
tresc = demo[demo.index('<section class="page'):]
uzyte = set(re.findall(r'\bfoto\d+\b', tresc)) | {"logo-foto", "mark-foto"}
demo = re.sub(r'(\.[a-zA-Z0-9_.,\s-]+)\{background-image:url\(data:[^)]*\)\}',
              lambda m: m.group(0) if set(re.findall(r'\.([a-zA-Z0-9_-]+)', m.group(1))) & uzyte else "",
              demo)
io.open(cel, "w", encoding="utf-8").write(demo)
PY
"$CHROME" --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$CEL/demo/maly-ksiaze-demo.pdf" "$CEL/demo/maly-ksiaze-demo.html" 2>/dev/null

echo "→ dokładny format A4"
# Chromium zapisuje arkusz jako 209,89 × 297,01 mm — swoje zaokrąglenie do pikseli.
# Nadpisujemy /MediaBox na dokładne A4 (595,2756 × 841,8898 pt). Podmiana ma tę samą
# długość w bajtach, więc tablica xref pozostaje poprawna.
python3 - "$CEL/pelna/maly-ksiaze-broszura.pdf" "$CEL/demo/maly-ksiaze-demo.pdf" <<'A4'
import sys
for sciezka in sys.argv[1:]:
    d = open(sciezka, "rb").read()
    n = d.count(b"594.95996 841.91998")
    open(sciezka, "wb").write(d.replace(b"594.95996 841.91998", b"595.27560 841.88980"))
    print(f"   {sciezka}: poprawiono {n} stron")
A4

echo "→ sumy kontrolne"
( cd "$CEL" && find pelna demo podglad -type f | sort | xargs sha256sum > sumy-kontrolne.txt )

echo "Gotowe:"
du -h "$CEL"/pelna/* "$CEL"/demo/*
