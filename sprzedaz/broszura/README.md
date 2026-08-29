# Broszura sprzedażowa — „Kolorowy Świat Emocji"

Siedemnastostronicowa broszura A4 do sprzedaży zeszytu *Kolorowy Świat Emocji*
(seria „Świat Kolorów", część 1, PCTP Koszalin).

## Co jest w środku

| Strona | Zawartość |
|---|---|
| 1 | Okładka |
| 2 | Czym jest zeszyt — liczby, dla kogo, gdzie się sprawdzi, jak jest zrobiony |
| 3 | Mapa zeszytu — trzy strefy i miniatury ośmiu stron |
| 4 | Osiem kącików rozdziału, strona po stronie, plus trzy poziomy zadań |
| 5–9 | **Pięć stref koloru** — radość, smutek, złość, wstyd, lęk. Każda: zdjęcie otwierające, mapa ciała, opowiadanie, sytuacje, cztery kroki i miniatura strony ucznia |
| 10 | Strefa gry — „Ścieżka Kolorów", zasady i dwie wersje trudności |
| 11 | Strefa narzędzi — karty emocji, plan na trudny dzień, strona bezpieczeństwa, dyplom |
| 12 | Strefa dorosłego — rób / unikaj, trzy pytania startowe, kiedy kierować do specjalisty |
| 13–15 | **Dostosowania dla 15 grup uczniów** — dla każdej: co bywa trudne, co robi zeszyt, twoje dostosowanie i numery stron |
| 16 | Trzy licencje, dane techniczne, wolno / nie wolno |
| 17 | Kontakt, zapowiedź części 2 |

Grupy uczniów na stronach 13–15: spektrum autyzmu · ADHD · niepełnosprawność
intelektualna w stopniu lekkim i umiarkowanym · dysleksja · słabowzroczność ·
niedosłuch · mutyzm wybiórczy · uczeń niemówiący (AAC) · afazja · zaburzenia
lękowe i obniżony nastrój · zaburzenia przetwarzania sensorycznego ·
niepełnosprawność ruchowa · zaburzenia zachowania · FASD.

## Pliki

```
broszura/
├── Broszura-Kolorowy-Swiat-Emocji.pdf    ← gotowa do wysłania i druku (A4, 17 stron)
├── Broszura-Kolorowy-Swiat-Emocji.html   ← ta sama broszura w przeglądarce; Ctrl+P → A4
├── broszura-artifact.html                ← wersja do publikacji jako Artifact / na stronie
├── broszura.src.html                     ← ŹRÓDŁO do edycji (krótkie znaczniki zamiast grafik)
├── fonts.css                             ← kroje pisma wklejone jako base64
├── grafiki/                              ← 39 zdjęć i miniatur stron zeszytu
└── zbuduj.py                             ← składa źródło + grafiki w gotowe pliki
```

## Jak wprowadzić zmianę

1. Popraw treść w `broszura.src.html`. Grafiki są tam zapisane jako `{{IMG:nazwa|opis}}` —
   `nazwa` to plik `grafiki/nazwa.jpg`.
2. `python3 zbuduj.py` — powstają oba pliki HTML z wklejonymi grafikami i krojami.
3. PDF: otwórz `Broszura-Kolorowy-Swiat-Emocji.html` w przeglądarce i wydrukuj do PDF
   (A4, marginesy zerowe, grafiki tła włączone). Albo z wiersza poleceń:

   ```
   chromium --headless --no-pdf-header-footer \
     --print-to-pdf=Broszura-Kolorowy-Swiat-Emocji.pdf \
     file://$PWD/Broszura-Kolorowy-Swiat-Emocji.html
   ```

## Do uzupełnienia przed wysyłką

Na stronie 16 w trzech miejscach stoi `[ cena ]`. Ceny nie były ustalone —
wpisz je w `broszura.src.html` i przebuduj.

## Skąd pochodzą zdjęcia

Wszystkie zdjęcia i miniatury są wyjęte z samego pliku
`Kolorowy-Swiat-Emocji-czesc-1.pdf` — to fotografie osadzone w zeszycie
oraz renderowane strony produktu. Broszura nie pokazuje niczego,
czego nie ma w sprzedawanym pliku.

## Druk

- Format A4 pionowo, 210 × 297 mm, pełny kolor.
- Grafiki schodzą do krawędzi strony (okładka, strony stref) — przy druku
  offsetowym poproś drukarnię o **spady 3 mm** i trzymaj tekst
  min. 8 mm od krawędzi.
- Druk domowy i biurowy: „dopasuj do strony" wyłączone, skala 100%.

---

Autorka treści zeszytu: Mirosława Ewa Jurczyszyn, pedagog specjalny.
Wydawca: Pomorskie Centrum Terapii Pedagogicznej, Koszalin.
kontakt@eduplaner2026.pl · [usunięto] · www.eduplaner2026.pl
