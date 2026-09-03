# Katalog szkoleń PCTP — rok szkolny 2026/2027

Dziewiętnastostronicowy katalog A4: dwanaście szkoleń w czterech ścieżkach
tematycznych i trzy pakiety dla zespołów.

## Zawartość

| Strony | Co zawiera |
|---|---|
| 1 | Okładka |
| 2 | Cztery formy prowadzenia, przebieg współpracy, opis ścieżek |
| 3 | Zestawienie wszystkich dwunastu szkoleń z kodami |
| 4–16 | Karta każdego szkolenia — jedna strona na szkolenie |
| 17–18 | Trzy pakiety dla zespołów |
| 19 | Warunki, rozliczenie, jak zamówić |

### Dwanaście szkoleń

**Ścieżka A — Emocje i kompetencje społeczne**
A1 Kolorowy Świat Emocji (6 h) · A2 Emocje w przedszkolu (6 h) · A3 Trening umiejętności społecznych (8 h)

**Ścieżka B — Dokumentacja i ocena funkcjonalna**
B1 WOPF krok po kroku (8 h) · B2 IPET, który działa (8 h) · B3 Trzy poziomy wsparcia (4 h) · B4 Ewaluacja IPET-u (4 h)

**Ścieżka C — Uczeń o specjalnych potrzebach**
C1 Uczeń w spektrum w grupie ogólnodostępnej (8 h) · C2 Zachowania trudne — model ABC (8 h) · C3 Dostosowania w projektowaniu uniwersalnym (6 h)

**Ścieżka D — Narzędzia i wdrożenia**
D1 Komunikacja alternatywna i wspomagająca (6 h) · D2 EduPlaner 2026 (4 h)

Każde szkolenie ma: opis, czas, liczebność grupy, dla kogo, dostępne formy,
program z modułami i minutami, efekty dla uczestnika oraz materiały w cenie.

## Pliki

```
katalog-szkolen/
├── Katalog-szkolen-PCTP.pdf            ← do wysłania i druku (19 stron A4)
├── Katalog-szkolen-PCTP.html           ← ta sama treść w przeglądarce; Ctrl+P → A4
├── Katalog-szkolen-PCTP-artifact.html  ← wersja do publikacji
├── dane.js                             ← ŹRÓDŁO TREŚCI — tu wprowadza się zmiany
└── generuj.js                          ← składa dane.js do HTML
```

Warstwa graficzna jest wspólna z katalogiem pomocy: `../wspolne/styl-katalogu.js`.

## Jak wprowadzić zmianę

1. Popraw treść w `dane.js` (szkolenia, ścieżki, formy, pakiety).
2. `node generuj.js`
3. PDF: otwórz HTML w przeglądarce i wydrukuj do PDF (A4), albo:

   ```
   chromium --headless --no-pdf-header-footer \
     --print-to-pdf=Katalog-szkolen-PCTP.pdf \
     file://$PWD/Katalog-szkolen-PCTP.html
   ```

Dodanie szkolenia to jeden obiekt w tablicy `SZKOLENIA` — trafi automatycznie
do zestawienia i dostanie własną stronę.

## Do uzupełnienia i sprawdzenia

- **Ceny** — wszędzie stoi `[ cena ]`. Wpisz w `dane.js` i przebuduj.
- **Programy szkoleń** zostały napisane na podstawie kompetencji widocznych
  w Twoich materiałach (metoda pięciu kolorów, WOPF, IPET, KSzOF, ICF,
  poziomy wsparcia, model ABC, AAC, EduPlaner). **Przejrzyj je i wykreśl to,
  czego nie prowadzisz albo nie chcesz prowadzić.**
- **Zaświadczenia** — katalog obiecuje zaświadczenie o ukończeniu przy każdym
  szkoleniu. Sprawdź, czy to zgodne z formą prawną, w jakiej działa PCTP.
- **Warunki rezygnacji i rozliczenia** (str. 19) to propozycja — potwierdź
  z księgowością.

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
