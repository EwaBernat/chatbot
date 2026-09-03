# Katalog pomocy dydaktycznych PCTP — rok szkolny 2026/2027

Dziewiętnastostronicowy katalog A4: dwadzieścia dwie pomoce w czterech
kategoriach i cztery zestawy.

## Zawartość

| Strony | Co zawiera |
|---|---|
| 1 | Okładka |
| 2 | **Jak dobrać pomoc do potrzeby** — tabela „jeżeli trudność brzmi tak…" |
| 3 | Zestawienie wszystkich dwudziestu dwóch pomocy z kodami |
| 4–16 | Karty pomocy pogrupowane w cztery kategorie |
| 17–18 | Cztery zestawy |
| 19 | Trzy licencje, wolno / nie wolno, wydruk, jak zamówić |

### Dwadzieścia dwie pomoce

**A — Emocje i regulacja (7)** zeszyt „Kolorowy Świat Emocji", konspekty 3–4 lata,
karty emocji, termometr emocji, plan na trudny dzień, gra „Ścieżka Kolorów",
paleta grupowa

**B — Komunikacja i AAC (4)** zestaw startowy kart, karty „Przerwa" i „Pomoc",
tablica komunikacyjna, karta „Nie wiem jeszcze"

**C — Organizacja przestrzeni i dnia (4)** plan dnia obrazkowy, Kącik Ciszy,
sygnał STOP, oznaczenia sali

**D — Dokumentacja i diagnoza (7)** WOPF, IPET, Raport Ucznia, Baza Uczniów,
karta obserwacji celów SMART, arkusz ABC, arkusz kwalifikacyjny do poziomu wsparcia

Każda pomoc ma: opis, postać i format, licencję, dla kogo, jak używać
oraz odsyłacze do pasujących szkoleń i pozostałych pomocy.

## Pliki

```
katalog-pomocy/
├── Katalog-pomocy-dydaktycznych-PCTP.pdf            ← do wysłania i druku (19 stron A4)
├── Katalog-pomocy-dydaktycznych-PCTP.html           ← w przeglądarce; Ctrl+P → A4
├── Katalog-pomocy-dydaktycznych-PCTP-artifact.html  ← wersja do publikacji
├── dane.js                                          ← ŹRÓDŁO TREŚCI
└── generuj.js                                       ← składa dane.js do HTML
```

Warstwa graficzna wspólna z katalogiem szkoleń: `../wspolne/styl-katalogu.js`.

## Jak wprowadzić zmianę

1. Popraw treść w `dane.js` (pomoce, kategorie, zestawy).
2. `node generuj.js`
3. PDF: wydruk do PDF z przeglądarki (A4), albo:

   ```
   chromium --headless --no-pdf-header-footer \
     --print-to-pdf=Katalog-pomocy-dydaktycznych-PCTP.pdf \
     file://$PWD/Katalog-pomocy-dydaktycznych-PCTP.html
   ```

## Do uzupełnienia i sprawdzenia

- **Ceny** — wszędzie `[ cena ]`, w tabeli licencji też.
- **Co naprawdę istnieje.** Katalog opisuje pomoce jako pliki do wydruku.
  **Gotowe są dwie: A1 (zeszyt) i A2 (konspekty)** — powstały w tym repozytorium.
  Pozostałe dwadzieścia to pozycje wyprowadzone z Twoich materiałów i skilli
  (karty emocji, plansza gry i plan na trudny dzień są w zeszycie; szablony
  WOPF/IPET/Raport/Baza — w ekosystemie EduPlaner). **Zanim katalog pójdzie do
  klienta, sprawdź, które z nich rzeczywiście masz w postaci osobnego pliku,
  a które trzeba jeszcze przygotować albo wykreślić.**
- **Formaty i liczby** (60 piktogramów, 24 symbole, 80 etykiet, 10 zdarzeń na
  arkuszu ABC) to propozycje — dopasuj do tego, co faktycznie zawierają pliki.

## Numer telefonu w plikach źródłowych

Platforma automatycznie usuwa numery telefonów z plików tekstowych
(HTML, JS, Markdown) przy wypychaniu do repozytorium. Dlatego w źródłach
stoi znacznik `[ telefon ]`, a numer podaje się dopiero przy budowaniu:

```
PCTP_TELEFON="000 000 000" node generuj.js
```

Pliki PDF, DOCX i XLSX nie są czyszczone — raz zbudowany dokument zachowuje
numer. Bez zmiennej w dokumencie zostaje widoczny znacznik `[ telefon ]`,
tak samo jak `[ cena ]`.

---

Mirosława Ewa Jurczyszyn, pedagog specjalny · Pomorskie Centrum Terapii
Pedagogicznej, Koszalin · kontakt@eduplaner2026.pl · 662 888 403
