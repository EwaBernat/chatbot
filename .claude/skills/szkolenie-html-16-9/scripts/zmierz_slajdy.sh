#!/usr/bin/env bash
# Kontrola jakości prezentacji: mierzy, gdzie kończy się treść każdego slajdu.
#
# Slajd ma 720 px wysokości. Treść powinna kończyć się między ~560 a ~700 px:
#   > 700  = przepełnienie, treść wchodzi na numer slajdu lub wypada poza kadr
#   < 540  = slajd zbyt pusty, warto dodać treść albo zwiększyć skalę
#
# Użycie:  bash zmierz_slajdy.sh /sciezka/do/prezentacji.html
set -u
F="${1:?podaj ścieżkę do pliku HTML}"
CH=""
for c in /opt/pw-browsers/chromium-*/chrome-linux/chrome \
         "$(command -v chromium || true)" "$(command -v chromium-browser || true)" \
         "$(command -v google-chrome || true)" "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; do
  [ -n "$c" ] && [ -x "$c" ] && CH="$c" && break
done
if [ -z "$CH" ]; then
  echo "Nie znalazłem przeglądarki Chromium/Chrome — zmierz slajdy ręcznie w przeglądarce."; exit 2
fi

TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
cp "$F" "$TMP/m.html"
cat >> "$TMP/m.html" <<'JS'
<pre id="M"></pre><script>
setTimeout(function(){var o=[];document.querySelectorAll('.slide').forEach(function(s,i){
 var prev=s.className;s.classList.add('on');var sr=s.getBoundingClientRect(),m=0;
 s.querySelectorAll('*').forEach(function(e){
   if(e.classList.contains('num')||e.classList.contains('tag'))return;
   var r=e.getBoundingClientRect();if(r.height===0)return;
   var b=(r.bottom-sr.top)/(sr.height/720);if(b>m)m=b});
 o.push((i+1)+':'+Math.round(m)+':'+(s.classList.contains('cover')?'c':'n'));s.className=prev});
 document.getElementById('M').textContent=o.join(' ')},2500)</script>
JS

RAW="$("$CH" --headless=new --no-sandbox --disable-gpu --window-size=1500,900 \
  --virtual-time-budget=6000 --dump-dom "file://$TMP/m.html" 2>/dev/null \
  | sed -n '/<pre id="M">/,/<\/pre>/p' | sed 's/<[^>]*>//g' | head -1)"

[ -z "$RAW" ] && { echo "Pomiar się nie udał — sprawdź, czy plik ma sekcje .slide"; exit 3; }

echo "slajd  dół treści  status"
BAD=0
for pair in $RAW; do
  N="${pair%%:*}"; REST="${pair#*:}"; V="${REST%%:*}"; T="${pair##*:}"
  if   [ "$T" = "c" ]; then S="okładka — grafika może celowo wychodzić poza kadr"
  elif [ "$V" -gt 700 ]; then S="PRZEPEŁNIENIE — skróć treść"; BAD=1
  elif [ "$V" -lt 540 ]; then S="pusto — dodaj treść"
  else S="ok"; fi
  printf "%5s %10s  %s\n" "$N" "$V" "$S"
done
echo
[ "$BAD" = 1 ] && echo "Popraw slajdy oznaczone PRZEPEŁNIENIE i zmierz ponownie." || echo "Żaden slajd nie wychodzi poza kadr."
