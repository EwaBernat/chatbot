# Edytor własnych konspektów

`src/moje_konspekty_fba.py`. Przy każdej komórce z celem jest **+**, który otwiera
formularz o tej samej strukturze co konspekt gotowy. Zapisany scenariusz otwiera
się i drukuje tak samo — ta sama karta, ten sam druk KC-3 A4. Nad tabelą panel
„Moje konspekty" z listą scenariuszy danej wersji wiekowej.

To odpowiednik `moje_konspekty.py` z banku KPOF, ale **nie jest jego kopią** —
poniżej różnice, których nie wolno zgubić przy zmianach.

## Co jest tu inne niż w banku

**Zachowanie zastępcze ma własne pole i bez niego konspekt się nie zapisze.** To
ono jest treścią planu PBS. Pole wchodzi wypełnione brzmieniem z wiersza tabeli
(`tr[data-zast]`), nauczycielka może je doprecyzować. W banku takiego pola nie ma,
bo tam cel nie wisi na funkcji zachowania.

**Klucz `localStorage` jest inny niż klucz banku**
(`eduplaner2026.moje-konspekty-fba.v1`), a wczytywanie kopii JSON odrzuca pozycje
spoza tego druku i mówi, ile pominęło. Konspekt z banku wisiałby tu w próżni: tam
cel ma numer twierdzenia, tu wskaźnik FBA.

**Sekcja VII ma trzy warianty karty pomocy** — gotową, własną albo żadną,
niezależnie od materiału do wycięcia:

* **gotowa** — `.pom` i `.zal` **klonowane** z konspektu tego wskaźnika. Klonujemy
  węzeł dokumentu, a nie kopiujemy mediów do `localStorage`: nagranie to 30 kB
  w base64 i magazyn skończyłby się po kilkunastu konspektach. Poza tym dziecko
  ma słyszeć **to samo** polecenie i widzieć **ten sam** symbol.
* **własna** — pełny druk KC-4 pisany od zera, ze zdjęciem i nagraniem wgranym
  z dysku.
* **żadna**.

Przełączenie na kartę gotową **nie kasuje** wgranego zdjęcia ani nagrania —
miejsce zwalnia przycisk „Usuń", świadomie. Skasowanie przy okazji przełączenia
to utrata pracy, której nauczycielka się nie spodziewa.

## Media własnej karty

Zdjęcie wgrywa się z dysku i **zmniejsza w przeglądarce** przez `canvas` do
900 px JPEG jakości 0.82 — tyle samo, ile mają zdjęcia pomocy gotowych. Bez tego
jedno zdjęcie z telefonu (3–5 MB) zajmuje cały magazyn. Nagranie przyjmujemy do
600 kB; komunikat odmowy podaje wagę pliku i limit, żeby dało się zareagować.

Panel pokazuje, ile miejsca zajęły konspekty. Przy pełnym magazynie komunikat
mówi, **co zrobić** (zapisz kopię JSON, usuń zdjęcie albo nagranie), zamiast
samego „nie udało się zapisać". `zapisz()` zwraca `'ok'`, `'pamiec'` albo
`'brak-miejsca'` właśnie po to.

## Pułapki, które już raz kosztowały rundę

**Kolejność skryptów.** `MK.skrypt()` idzie **przed** `KON.SKRYPT` w dokumencie.
Oba nasłuchują kliknięć na `document` w fazie przechwytywania, więc decyduje
kolejność rejestracji; handler plusa wygasza zdarzenie przez
`stopImmediatePropagation`. Odwrotna kolejność otwiera dwa okna naraz i tyle samo
wychodzi z drukarki.

**Miejsce na plus rezerwuje pływak na komórce, nie na tekście celu.**
`td.g.haskon::before{float:right}` — nie `.tresc::before`. Pływak wpięty w tekst
wciągał róg z przyciskiem do prostokąta `.tresc` i kliknięcie w cel przy prawej
krawędzi otwierało edytor zamiast gotowego konspektu.

**`[hidden]` przegrywa z `display:grid` z klasy.** Styl autora ma pierwszeństwo
przed stylem przeglądarki, więc blok pól własnej karty potrzebuje jawnego
`.mkf-pola[hidden]{display:none}`.

**Podgląd własnego konspektu nie niesie `data-wersja`.** Wydruk zeszytu wybiera
konspekty po tym atrybucie i wciągnąłby do niego ten jeden, akurat otwarty.

**Escape nie zamyka formularza.** Zamyka podgląd — ten jest zwykłym `.kmodal`
i dziedziczy wszystko. Formularz ma własne okno i własny krzyżyk, który **pyta**
przed zamknięciem: jeden przypadkowy ruch nie może skasować rozpisanego
scenariusza. Krzyżyk jest w obu oknach, w prawym górnym rogu — nauczycielka
szuka go tam niezależnie od tego, czy konspekt czyta, czy pisze.

**`zmierz_konspekty.mjs` mierzy tylko `.kmodal[id^="kon-"]`.** `#mkf-widok` to
puste okno podglądu; wliczone do pomiaru dawałoby 76 konspektów i zerową
wysokość.

## Jak to testować

Oglądanie nie wystarcza — trzeba przeklikać. Wzór:

```js
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const p = await b.newPage({ viewport: { width: 1240, height: 960 } });
const err = []; p.on('pageerror', e => err.push(String(e)));
p.on('dialog', d => d.accept());              // edytor pyta przy zamykaniu
await p.route('**://fonts.*/**', r => r.abort());
await p.goto('file:///.../Tabela_celow_FBA_wiek_poziom.html');

// plus otwiera edytor i NIE otwiera przy okazji gotowego konspektu
await p.locator('#w-A tr[data-wsk="II.3"] td.g[data-lvl="p2"] .mkf-add').click();
// klik w tekst celu otwiera gotowy konspekt
await p.locator('#w-A tr[data-wsk="II.3"] td.g[data-lvl="p2"] .tresc').click();
```

Warto sprawdzić za każdym razem: plus vs. klik w cel, zapis i blokady (tytuł,
zachowanie zastępcze, nazwa własnej karty), oznaczenie komórki ✎, licznik
w panelu, trwałość po `reload()`, edycję z podglądu, krzyżyk w obu oknach,
sekcję VII (klon albo własna karta z działającym nagraniem) i wysokość wydruku.
Wersje B i C są ukryte na starcie — najpierw kliknij zakładkę.

Playwright może nie importować się z katalogu modułu; dowiąż go na czas testu
i **skasuj dowiązanie** po wszystkim:

```bash
mkdir -p node_modules && ln -sfn /opt/node22/lib/node_modules/playwright node_modules/playwright
# ... testy ...
rm -f node_modules/playwright && rmdir node_modules
```

## Uwaga o pisaniu skryptu w Pythonie

`SKRYPT` w tym module to zwykły łańcuch Pythona, nie raw-string. Znak nowej linii
w łańcuchu JS zapisuj jako `\\n`, a apostrof wewnątrz `url()` w ogóle pomijaj —
data-URI nie zawiera cudzysłowów ani nawiasów, więc `url(<data-uri>)` bez
cudzysłowu jest poprawne i tak samo robią karty gotowe. Podwójne odkodowanie
`\\'` i `\\n` przy edytowaniu tego pliku skryptem wysypało już parser JS.
Po każdej zmianie:

```bash
python3 -c "import sys;sys.path.insert(0,'src');import moje_konspekty_fba as M;open('/tmp/mk.js','w').write(M.skrypt())"
node --check /tmp/mk.js
```
