# Konspekty zajęć 3–4 lata — „Kolorowy Świat Emocji"

Siedem konspektów zajęć rozwijających kompetencje emocjonalne i społeczne
dla dzieci w wieku przedszkolnym, z **kompletem 21 celów SMART** (7 konspektów
× 3 poziomy wsparcia) gotowych do przeniesienia do IPET-u.

Przedszkolna wersja metody z zeszytu *Kolorowy Świat Emocji* (seria „Świat
Kolorów", część 1). Bohaterem jest **Miś Kolorek**, który zmienia chustkę
razem z emocją — odpowiednik siedemnastoletniego Rajmunda z wersji dla
nastolatka.

## Zawartość

| Część | Co zawiera |
|---|---|
| I | Jak korzystać z konspektów — sześć zasad cyklu i ramowy plan 12 tygodni |
| II | Trzy poziomy wsparcia — definicje, formy realizacji, podstawy prawne |
| III | **Wszystkie 21 celów SMART** w jednej tabeli, w układzie do sekcji III IPET-u |
| IV | Siedem konspektów zajęć |
| V | Karta obserwacji i ewaluacji celów — do wydruku dla każdego dziecka |
| VI | Podstawa prawna i źródła |

### Siedem konspektów

| Nr | Temat | Kolor · emocja | Czas |
|---|---|---|---|
| 1 | Pięć kolorów Misia Kolorka — poznajemy emocje | wszystkie pięć | 20 min |
| 2 | Żółty dzień Misia Kolorka — co mnie cieszy | żółty · radość | 20 min |
| 3 | Niebieski Miś — kiedy jest mi smutno | niebieski · smutek | 20 min |
| 4 | Czerwony Miś — co robię, kiedy się złoszczę | czerwony · złość | 20 min |
| 5 | Różowy Miś — kiedy chcę się schować | różowy · wstyd | 20 min |
| 6 | Szary Miś — czego się boję | szary · strach | 20 min |
| 7 | Paleta Misia Kolorka — gra „Kolorowa Ścieżka" | wszystkie pięć | 25 min |

Każdy konspekt zawiera: cel ogólny, cele operacyjne, **trzy cele SMART
(poziom I / II / III)** z obszarem KSzOF, kodem ICF, formą realizacji,
kryterium osiągnięcia i podstawą prawną, metody i formy pracy, środki
dydaktyczne, pięcioetapowy przebieg zajęć z czasami, sześć dostosowań dla
dzieci z różnymi potrzebami, pytania ewaluacyjne, odniesienia do podstawy
programowej i notatkę dla prowadzącego.

## Jak zapisane są cele SMART

Poziom wsparcia nie zmienia tematu zajęć — zmienia kryterium osiągnięcia
i ilość podpowiedzi wpisaną w treść celu:

- **Poziom I** — bieżąca praca w grupie; cel zakłada samodzielność, kryterium 4/5.
- **Poziom II** — zajęcia specjalistyczne w grupie do 4 osób; cel dopuszcza
  jedną podpowiedź wzrokową, kryterium 4/5.
- **Poziom III** — praca indywidualna i wsparcie nauczyciela współorganizującego;
  cel zawiera podpowiedź gestową i modelowanie, kryterium 3/5.

## Pliki

```
konspekty-3-4-lata/
├── Konspekty-Kolorowy-Swiat-Emocji-3-4-lata.docx   ← wersja EDYTOWALNA (Word)
├── Konspekty-Kolorowy-Swiat-Emocji-3-4-lata.pdf    ← do druku i wysyłki (22 strony A4)
├── Konspekty-Kolorowy-Swiat-Emocji-3-4-lata.html   ← ta sama treść w przeglądarce
├── konspekty-artifact.html                          ← wersja do publikacji
├── dane.js          ← ŹRÓDŁO TREŚCI — tu wprowadza się zmiany
├── generuj.js       ← składa dane.js do Worda
└── generuj-html.js  ← składa dane.js do HTML (z niego drukuje się PDF)
```

**Word i PDF pochodzą z tego samego pliku `dane.js`** — treść nie może się
rozjechać między wersjami.

## Jak wprowadzić zmianę

1. Popraw treść w `dane.js` (konspekty, cele SMART, poziomy wsparcia).
2. `node generuj.js` — powstaje plik .docx.
3. `node generuj-html.js` — powstaje HTML.
4. PDF: otwórz HTML w przeglądarce i wydrukuj do PDF (A4), albo:

   ```
   chromium --headless --no-pdf-header-footer \
     --print-to-pdf=Konspekty-Kolorowy-Swiat-Emocji-3-4-lata.pdf \
     file://$PWD/Konspekty-Kolorowy-Swiat-Emocji-3-4-lata.html
   ```

Pierwsze uruchomienie `generuj.js` wymaga `npm install docx`.

## Uwaga o pliku Word

Plik .docx przechodzi walidację schematu OOXML, ale nie został obejrzany
w Wordzie — LibreOffice w środowisku, w którym powstał, nie otwiera żadnych
plików .docx, więc nie dało się zrobić podglądu. Wersje PDF i HTML zostały
sprawdzone strona po stronie. **Przy pierwszym otwarciu Worda warto rzucić
okiem na układ tabel.**

## Zastrzeżenie merytoryczne

Cele SMART są wzorcami do dostosowania pod konkretne dziecko na podstawie
wielospecjalistycznej oceny poziomu funkcjonowania (WOPF). Materiał nie
zastępuje diagnozy ani terapii.

Numeracja punktów podstawy programowej — za załącznikiem nr 1 do Rozp. MEN
z 14.02.2017 r. Warto zweryfikować ją z aktualnym brzmieniem załącznika
przed załączeniem konspektów do dokumentacji.

---

Mirosława Ewa Jurczyszyn, pedagog specjalny · Pomorskie Centrum Terapii
Pedagogicznej, Koszalin · kontakt@eduplaner2026.pl · [usunięto]
