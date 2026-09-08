# Druk — reguły, o które łatwo się potknąć

Bank i zeszyty drukują się z przeglądarki (Ctrl+P) albo skryptami
`src/generuj_*_pdf.mjs`. Poniższe reguły powstały z błędów, które w tym projekcie
już raz weszły do dokumentu i wyszły dopiero przy drukarce.

## Dwie orientacje w jednym dokumencie

Bank drukuje się **poziomo** — tabela ma trzy poziomy wsparcia obok siebie
i pionowo się nie mieści. Ale arkusze i karty pomocy muszą wyjść **pionowo**.
Robi to nazwana strona CSS:

```css
@page arkusz { size: A4 portrait; margin: 10mm }
.zal { page: arkusz }
```

To samo dotyczy pojedynczego konspektu drukowanego z modalu:
`html.print-konspekt .kcard { page: arkusz }`. Bez tego konspekt wychodził
poziomo, mimo że cała jego zawartość jest pionowa.

## Zeszyt musi cofnąć regułę banku

Zeszyty konspektów dziedziczą arkusz stylów banku, a bank chowa modale przy
druku:

```css
@media print { .kmodal { display: none } }
```

W zeszycie konspekt **jest** treścią, więc `build_konspekty.py` cofa tę regułę
u siebie:

```css
@media print {
  .kmodal { display: block !important; position: static !important; … }
  .zal-strefa { display: block !important }
  .zal { break-inside: avoid; page-break-inside: avoid }
}
```

Bez tego cały zeszyt wychodził z drukarki jako **jedna pusta strona**. Objaw jest
mylący, bo na ekranie wszystko wygląda dobrze.

## Budżet strony i pomiar

A4 to 210×297 mm; przy marginesie 9 mm zostaje 192×279 mm, czyli **726×1054 px**
przy 96 dpi. Sprawdzaj pomiarem, nie okiem:

```bash
node .claude/skills/bank-celow-smart/scripts/zmierz_a4.mjs
```

Skrypt renderuje dokumenty w trybie druku i mierzy każdą sekcję `.zal` — arkusze
i karty pomocy. Kończy się kodem 1, gdy cokolwiek wychodzi poza stronę.

Gdy arkusz nie mieści się: dołóż kolumn w siatce, skróć wstęp arkusza albo zdejmij
kafle. Zmniejszanie czcionki jest ostatecznością — te materiały ogląda dziecko.

## Fonty ładujemy nieblokująco

```html
<link rel="stylesheet" media="print" onload="this.media='all'" href="…fonts…">
```

Przy niedostępnym CDN blokujący `<link>` trzymał biały ekran kilkanaście sekund
i wyglądało to na zepsuty dokument. Pomiary i zrzuty rób z zablokowanymi fontami
(`p.route('**://fonts.*/**', r => r.abort())`) — wynik ma być powtarzalny także
bez internetu.

## Generowanie PDF

```bash
# z katalogu eduplaner_przedszkole; playwright bywa globalny
node src/generuj_bank_pdf.mjs        # bank, A4 poziomo, stopka z numeracją
node src/generuj_pomoce_pdf.mjs      # zeszyty pomocy, karta na stronę
```

Zeszyty konspektów drukuje się przez `page.pdf({ preferCSSPageSize: true })` —
reguły `@page` w dokumencie same ustawiają orientację.

Po wygenerowaniu sprawdź liczbę stron i orientację, zamiast zakładać:

```python
from pypdf import PdfReader
r = PdfReader("Konspekty_5_lat.pdf")
print(len(r.pages), {("%dx%d" % (p.mediabox.width, p.mediabox.height)) for p in r.pages})
# oczekiwane: 594x841 (A4 pionowo) dla zeszytów, 842x595 dla banku
```

## Playwright w tym środowisku

Chromium jest w obrazie: `/opt/pw-browsers/chromium`. Moduł `playwright` bywa
globalny (`/opt/node22/lib/node_modules`) — node szuka modułów przy pliku skryptu,
nie przy katalogu roboczym, więc dowiązanie `node_modules` pomaga tylko skryptom
leżącym obok. Skrypty tego skilla same sprawdzają kilka lokalizacji.
