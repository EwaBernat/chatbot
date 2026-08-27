# Mały Książę moim bohaterem — paczka do sprzedaży na stronie

Wszystko, co potrzebne, żeby wystawić broszurę na stronie: pliki do pobrania,
darmowy fragment, obrazy na kartę produktu, metadane i instrukcja zabezpieczenia
płatnych plików.

**Wydawca:** Pomorskie Centrum Terapii Pedagogicznej
**Autorka:** Mirosława Ewa Jurczyszyn · kontakt@eduplaner2026
**Wersja:** wydanie pierwsze, 2026

---

## 1. Co jest w paczce

```
dystrybucja/
├── pelna/                        ← produkt płatny, NIE wystawiaj publicznie
│   ├── maly-ksiaze-broszura.pdf   9,2 MB · 122 strony A4
│   └── maly-ksiaze-broszura.html  5,9 MB · jeden plik, wszystko w środku
├── demo/                         ← darmowy fragment, może leżeć publicznie
│   ├── maly-ksiaze-demo.pdf       1,6 MB · 14 stron (okładka … rozdział 1)
│   └── maly-ksiaze-demo.html      0,8 MB
├── podglad/                      ← obrazy na kartę produktu (JPG, 1000 px)
│   ├── miniatura.jpg              600 px — okładka do listy produktów
│   └── 01-okladka … 10-koniec     10 stron przekrojowych
├── metadane.json                 ← tytuł, opis, słowa kluczowe, ceny, pliki
├── sumy-kontrolne.txt            ← SHA-256 wszystkich plików
└── zbuduj-paczke.sh              ← regeneracja paczki po zmianach w treści
```

## 2. Czym jest ta broszura

| | |
|---|---|
| Format | A4 pionowo, 122 strony |
| Zawartość | 27 rozdziałów po 3 strony, 8 zestawów ćwiczeń, gra planszowa z instrukcją i 32 kartami zadań, scenariusz przedstawienia (8 scen), 16 kart do wycięcia, termometr emocji, krążki oceny |
| Odbiorcy | uczniowie 12–19 lat ze spektrum autyzmu; nauczyciele, terapeuci, rodzice |
| Języki | polski |
| Numeracja | ciągła 1–122, okładka to strona 1 bez nadruku |

## 3. HTML — co musisz wiedzieć

**Jeden plik, bez zależności.** Cała grafika (akwarele, logo) jest osadzona
w pliku jako `data:` URI, a rysunki wektorowe jako inline SVG. Nie ma folderu
`assets/`, nie ma nic do zgubienia przy wgrywaniu.

**Zero odwołań na zewnątrz.** Kroje Poppins i Lato są osadzone w pliku jako
`@font-face` z `data:` URI (14 odmian, ~190 KB). Nie ma zapytań do Google Fonts, więc
plik działa offline, nie wymaga wpisu w polityce prywatności i przechodzi restrykcyjne CSP.

To nie jest kosmetyka: PDF powstaje w przeglądarce bez dostępu do sieci. Dopóki kroje
wisiały pod adresem Google, w druku podstawiały się zastępniki (DejaVu Sans) i cały tekst
wyglądał na zbyt gruby. Odświeżenie krojów:
`python3 skille/broszura-lektura-autyzm/scripts/pobierz_kroje.py --out .../assets/kroje.css`.

**Tła drukują się bez pytania.** W `@media print` jest `print-color-adjust: exact`, więc
kolorowe pola i ramki wychodzą nawet wtedy, gdy użytkownik nie zaznaczy „Grafiki tła”.
Instrukcja w broszurze zostaje na wypadek przeglądarek, które tę własność ignorują.

**Arkusz ma dokładnie 210 × 297 mm.** Chromium zapisuje A4 jako 209,89 × 297,01 mm —
własne zaokrąglenie do siatki pikseli. `zbuduj-paczke.sh` nadpisuje `/MediaBox` na dokładne
wartości A4 (595,2756 × 841,8898 pt); podmiana ma tę samą długość w bajtach, więc tablica
xref zostaje poprawna. Jeśli budujesz PDF innym narzędziem, sprawdź ten wymiar.

**Każda strona wypełnia cały arkusz** dzięki `min-height:296.5mm` w `@media print`. Bez tego
strona kończyła się na wysokości swojej treści, a lewy zielony pasek — rysowany jako tło
o wysokości elementu — urywał się w połowie kartki. Pół milimetra zapasu chroni przed
wypchnięciem drugiego, pustego arkusza przez zaokrąglenia.

**Druk.** Plik ma `@page { size: A4; margin: 0 }` i sekcje o stałej wysokości.
Użytkownik drukuje przez Ctrl+P: papier A4, marginesy „brak”, skala 100%,
**zaznaczona „Grafika tła”**. Ta ostatnia opcja jest kluczowa — bez niej znikają
kolorowe pola i ramki. Instrukcja jest też na stronie 2 samej broszury.

**Nie ruszaj `@media screen and (max-width:800px)`.** Ta reguła celowo ma
`screen` — bez tego słowa breakpoint odpala się przy druku (A4 to ok. 793 px)
i rozwala układ na dwa arkusze na stronę.

**Osadzenie na stronie.** Trzy sposoby, wybierz jeden:

```html
<!-- a) prosty odsyłacz do pobrania -->
<a href="/pobierz/broszura.pdf" download>Pobierz PDF (9 MB)</a>

<!-- b) czytnik w ramce — polecany dla wersji HTML -->
<iframe src="/czytaj/broszura.html" style="width:100%;height:90vh;border:0"
        title="Mały Książę moim bohaterem"></iframe>

<!-- c) osobna podstrona — najlepsze SEO, plik serwowany jak zwykły HTML -->
```

## 4. Zabezpieczenie płatnych plików

**Nigdy nie linkuj bezpośrednio do `/pelna/`.** Plik pod stałym adresem trafi
do wyszukiwarki albo na forum w ciągu tygodnia.

Trzymaj `pelna/` **poza katalogiem publicznym** i wydawaj plik dopiero po
sprawdzeniu zamówienia.

**nginx + X-Accel-Redirect** (plik nigdy nie jest widoczny z zewnątrz):

```nginx
location /chronione/ {
    internal;
    alias /var/prywatne/broszury/;
}
```

```php
<?php  // /pobierz.php?token=...
$zamowienie = sprawdz_token($_GET['token'] ?? '');      // Twoja logika
if (!$zamowienie) { http_response_code(403); exit('Brak dostępu'); }

header('Content-Type: application/pdf');
header('Content-Disposition: attachment; filename="maly-ksiaze-broszura.pdf"');
header('X-Accel-Redirect: /chronione/maly-ksiaze-broszura.pdf');
```

**Node / Express:**

```js
app.get('/pobierz/:token', async (req, res) => {
  const zamowienie = await sprawdzToken(req.params.token)
  if (!zamowienie) return res.sendStatus(403)
  res.download('/var/prywatne/broszury/maly-ksiaze-broszura.pdf',
               'maly-ksiaze-broszura.pdf')
})
```

**Token jednorazowy albo wygasający** — najprostszy wariant: losowy ciąg
w bazie, powiązany z zamówieniem, ważny 72 godziny i maksymalnie 5 pobrań.
Wystarczy przeciw dzieleniu się linkiem, nie przeszkadza uczciwemu kupującemu,
któremu przerwie się pobieranie.

**Znak wodny z danymi kupującego** (opcjonalnie, mocno zniechęca do
rozsyłania) — dokładany w locie przy pobraniu:

```bash
# przykład z qpdf/ghostscript albo biblioteką PDF w Twoim języku
# nadruk w stopce: "Egzemplarz dla: jan.kowalski@example.com · zamówienie 1234"
```

Jeśli tego nie robisz, nie szkodzi — sam token już załatwia większość
przypadków.

## 5. Karta produktu

`metadane.json` zawiera gotowe pola: tytuł, podtytuł, opis krótki i długi,
słowa kluczowe, liczba stron, format, odbiorcy, spis części. Wstaw je
w swój sklep bez przepisywania.

Obrazy z `podglad/` są w proporcji A4 (1000 × 1414 px). `miniatura.jpg`
nadaje się na listę produktów, reszta na galerię i karuzelę.

Sugerowana struktura sprzedaży:

1. **Darmowy fragment** (`demo/`) — do pobrania bez rejestracji, z widoczną
   informacją, że to 14 stron ze 122. Buduje zaufanie i zbiera adresy e-mail.
2. **Wersja PDF** — plik do druku, główny produkt.
3. **Wersja HTML** — dla szkół, które czytają na tablicy albo na tablecie;
   można sprzedawać razem z PDF-em jako jeden pakiet.

## 6. Prawa

„Le Petit Prince” Antoine'a de Saint-Exupéry'ego należy w Polsce do domeny
publicznej od 2015 roku. **Streszczenie, pytania, ćwiczenia, gra, scenariusz
i cały układ broszury są samodzielnym opracowaniem autorki** i to one są
przedmiotem sprzedaży.

Akwarele przygotowano w narzędziu generatywnym i dobrano do scen; rysunki
wektorowe, plansza, termometr i karty powstały na potrzeby tej broszury.
Pełna nota jest na stronie 2 pliku (metryczka wydawnicza).

Licencja dla kupującego, którą warto wpisać w regulamin: **jedna licencja =
jedna placówka**; wolno drukować i kopiować na potrzeby własnej szkoły,
poradni lub gabinetu; nie wolno odsprzedawać ani publikować pliku w sieci.

## 7. Regeneracja paczki

Treść broszury żyje w repozytorium jako JSON + generator w Pythonie, nie jako
ręcznie pisany HTML. Po zmianie treści:

```bash
cd broszury/maly-ksiaze
python3 ../../skille/broszura-lektura-autyzm/scripts/zloz_broszure.py \
  ../../skille/broszura-lektura-autyzm/assets/maly-ksiaze.json \
  --out maly-ksiaze-broszura.html \
  --linie ../../skille/broszura-lektura-autyzm/assets/maly-ksiaze-linie.json \
  --skala 1.15

# kontrola składu — MUSI przejść przed publikacją
python3 ../../skille/broszura-lektura-autyzm/scripts/sprawdz_sklad.py \
  maly-ksiaze-broszura.html --pdf ../../dystrybucja/pelna/maly-ksiaze-broszura.pdf

cd ../.. && bash dystrybucja/zbuduj-paczke.sh
```

`sprawdz_sklad.py` sprawdza trzy rzeczy: czy HTML się domyka, czy żadna sekcja
nie przekracza 292 mm (czyli czy nie rozleje się na dwa arkusze) i czy PDF ma
dokładnie tyle stron, ile jest sekcji. Jeśli zgłosi błąd — nie publikuj,
bo w druku wyjdą puste strony.

## 8. Znane ograniczenia

- **Plik jest duży** (PDF 9 MB, HTML 6 MB) — to cena za osadzone akwarele
  w rozdzielczości do druku. Podaj rozmiar przy przycisku pobierania.
- **HTML nie jest responsywny w sensie mobilnym** — to dokument A4, nie strona
  internetowa. Na telefonie da się czytać, ale wygodniej jest w PDF.
- **Brak wyszukiwania pełnotekstowego** w wersji HTML poza tym, co daje Ctrl+F
  w przeglądarce.
- **Podgląd w `<iframe>`** nie zablokuje zapisania pliku przez użytkownika.
  Do wersji HTML traktuj to jako wygodę czytania, nie zabezpieczenie.

## 9. Kontakt

Pytania o treść, licencję i kolejne broszury z serii:
**Mirosława Ewa Jurczyszyn**, Pomorskie Centrum Terapii Pedagogicznej,
kontakt@eduplaner2026
