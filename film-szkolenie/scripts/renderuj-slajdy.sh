#!/usr/bin/env bash
# Zamienia slajdy prezentacji HTML na obrazy PNG dla filmu (2x, bez paska nawigacji).
# Użycie: bash renderuj-slajdy.sh <plik.html> <katalog-wyjsciowy> <liczba-slajdow>
set -eu
SRC="$1"; OUT="$2"; N="${3:-25}"
CH=""
for c in /opt/pw-browsers/chromium-*/chrome-linux/chrome "$(command -v chromium || true)" "$(command -v google-chrome || true)"; do
  [ -n "$c" ] && [ -x "$c" ] && CH="$c" && break
done
[ -z "$CH" ] && { echo "Brak przeglądarki Chromium"; exit 2; }

TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
cp "$SRC" "$TMP/film.html"
cat >> "$TMP/film.html" <<'PATCH'
<style>#hud,#rail,#notes,#gridview{display:none!important}
body{background:#241C3F}
.slide{border-radius:0!important;box-shadow:none!important}</style>
<script>
function dopasujDoFilmu(){var s=Math.min(window.innerWidth/1280,window.innerHeight/720);
document.documentElement.style.setProperty('--s',s);}
window.addEventListener('resize',dopasujDoFilmu);window.addEventListener('load',dopasujDoFilmu);
setInterval(dopasujDoFilmu,80);dopasujDoFilmu();
</script>
PATCH

mkdir -p "$OUT"
for i in $(seq 1 "$N"); do
  P=$(printf "%02d" "$i")
  "$CH" --headless=new --no-sandbox --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=2 --window-size=1280,720 --virtual-time-budget=6000 \
    --screenshot="$OUT/$P.png" "file://$TMP/film.html#s$i" >/dev/null 2>&1
  printf "."
done
echo " gotowe: $N obrazów w $OUT"
