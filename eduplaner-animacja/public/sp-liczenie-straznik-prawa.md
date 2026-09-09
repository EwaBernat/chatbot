# Strażnik prawa — Szkoła podstawowa · część 6: jak policzyć KSzOF ręcznie
Weryfikacja wobec druku autorki `KSzOF_4_6.html` (KSzOF-IV-VI, 28 stron) · EduPlaner 2026, PCTP Koszalin · stan na 9.09.2026

## 1. Źródło narzędzia

Kwestionariusz Szkolnej Oceny Funkcjonalnej (KSzOF) — Z. Gajdzica, E. Widawska, S. Byra, E. Domagała-Zyśk, B. Jachimczak, R. Piotrowicz, E. Neroj, **Katowice–Kraków 2024**, opracowany w ramach modelu oceny funkcjonalnej dla edukacji włączającej. Przypis źródłowy znajduje się w samym druku autorki, na stronie 8 („Wynik i kwalifikacja”).

Skala stenowa to standardowe narzędzie psychometryczne: dziesięć jednostek, średnia **5,5**, odchylenie standardowe **2**. Klasyczny wzór: `sten = 5,5 + 2 × (X − M) / SD`, gdzie M i SD pochodzą z próby normalizacyjnej.

## 2. Wzór użyty w filmie — odczytany wprost z druku autorki

Film nie wprowadza żadnego własnego sposobu liczenia. Uczy dokładnie tego wzoru, który jest zaszyty w arkuszu autorki (funkcja `stenRaw` w skrypcie druku):

```
mn = liczba twierdzeń × 1        (minimum obszaru)
mx = liczba twierdzeń × 5        (maksimum obszaru)
f  = (suma − mn) / (mx − mn)     (pozycja na skali, 0–1)

f < 0,3077          →  sten = 1 + (f ÷ 0,3077) × 3
0,3077 ≤ f < 0,6827 →  sten = 5 + ((f − 0,3077) ÷ 0,375) × 2
f ≥ 0,6827          →  sten = 8 + ((f − 0,6827) ÷ 0,3173) × 2

sten zaokrąglone do liczby całkowitej, przycięte do 1–10
```

**Uproszczenia podane w filmie i ich uzasadnienie.** Ponieważ `mx − mn = 4 × liczba twierdzeń`, zachodzi tożsamość `f = (średnia − 1) ÷ 4`. To pozwala policzyć wynik na kartce ze średniej, bez sięgania po sumę i maksimum. Stałe podano w zaokrągleniu do dwóch miejsc (0,31 · 0,68 · 0,37 · 0,32) — sprawdzono, że dla wszystkich dziewięciu obszarów arkusza i dla wyniku ogólnego zaokrąglone stałe dają **ten sam sten** co stałe pełne.

Progi wyrażone wprost w średniej: `1 + 4 × 0,3077 = 2,23` oraz `1 + 4 × 0,6827 = 3,73`.

## 3. Kwalifikacja do poziomu wsparcia — wg druku autorki (str. 7, 8 i 25)

| Sten | Wynik | Poziom | Co to oznacza |
|---|---|---|---|
| 8–10 | wysoki | **Poziom I** | wsparcie w bieżącej pracy nauczyciela — dostosowanie metod, form pracy i wymagań, indywidualizacja; bez dodatkowych zajęć |
| 5–7 | przeciętny | **Poziom II** | wsparcie dodatkowe — formy pomocy psychologiczno-pedagogicznej: korekcyjno-kompensacyjne, logopedyczne, TUS, dydaktyczno-wyrównawcze, porady i konsultacje |
| 1–4 | niski | **Poziom III** | wsparcie specjalistyczne — obserwacja pogłębiona, WOPFU i IPET dla ucznia z orzeczeniem, zajęcia rewalidacyjne, kontakt z poradnią PP |

Progi wyniku ogólnego (52 pozycje): **194–260 pkt** → Poziom I · **116–193 pkt** → Poziom II · **52–115 pkt** → Poziom III. Te granice to ten sam wzór policzony raz dla n = 52: `52 + 0,3077 × 208 = 116` oraz `52 + 0,6827 × 208 = 194`.

Poziom wsparcia ustala się **dla każdego obszaru osobno**. Decyzję zespołu dokumentuje się protokołem posiedzenia — druk autorki wprost zaznacza, że **nie wymaga to uchwały rady pedagogicznej** (str. 25).

## 4. Rachunki pokazane w filmie — kontrola zgodności z arkuszem

Wszystkie liczby w narracji pochodzą z wypełnionego arkusza Zofii Lewandowskiej i zostały porównane z wartościami, które druk wylicza sam.

| Obszar | Twierdzeń | Suma / max | Średnia | Pozycja | Sten wg wzoru | Sten w druku | Poziom |
|---|---|---|---|---|---|---|---|
| I · Uczenie się | 14 | 42 / 70 | 3,00 | 0,50 | 6,03 → 6 | 6 | II |
| II · Zadania | 6 | 18 / 30 | 3,00 | 0,50 | 6,03 → 6 | 6 | II |
| III · Komunikacja | 8 | 24 / 40 | 3,00 | 0,50 | 6,03 → 6 | 6 | II |
| IV · Motoryka | 2 | 7 / 10 | 3,50 | 0,63 | 6,69 → 7 | 7 | II |
| V · Samoobsługa | 4 | 14 / 20 | 3,50 | 0,63 | 6,69 → 7 | 7 | II |
| VI · Życie domowe | 2 | 4 / 10 | 2,00 | 0,25 | 3,44 → 3 | 3 | III |
| VII · Kontakty | 10 | 20 / 50 | 2,00 | 0,25 | 3,44 → 3 | 3 | III |
| VIII · Edukacja | 4 | 8 / 20 | 2,00 | 0,25 | 3,44 → 3 | 3 | III |
| IX · Społeczność | 2 | 4 / 10 | 2,00 | 0,25 | 3,44 → 3 | 3 | III |
| **Ogółem** | **52** | **141 / 260** | **2,71** | **0,43** | **5,64 → 6** | **6** | **II** |

Rozkład poziomów: 0 obszarów na Poziomie I, 5 na Poziomie II, 4 na Poziomie III — zgodnie z tabelą „Liczba obszarów wg poziomu wsparcia” na str. 8 druku.

## 5. Podstawy prawne przywołane w filmie

| Zakres | Akt | Publikator |
|---|---|---|
| Rozpoznawanie indywidualnych potrzeb rozwojowych i edukacyjnych ucznia, formy pomocy | rozp. MEN z 9.08.2017 r. o pomocy psychologiczno-pedagogicznej | **t.j. Dz.U. 2023 poz. 1798** |
| Wielospecjalistyczna ocena poziomu funkcjonowania i IPET (uczeń z orzeczeniem), § 6 | rozp. MEN z 9.08.2017 r. o kształceniu specjalnym | **t.j. Dz.U. 2020 poz. 1309** |
| Podstawa ogólna kształcenia specjalnego, art. 127 | Prawo oświatowe | **t.j. Dz.U. 2026 poz. 820** |

## 6. Uwagi Strażnika — granica między przepisem a narzędziem

1. **Wzór i progi nie wynikają z przepisu.** Żaden przepis nie nakazuje przeliczać punktów na steny ani nie ustala granic poziomów wsparcia. Przepis wymaga rozpoznania potrzeb ucznia i udzielenia mu pomocy. Sposób liczenia pochodzi z narzędzia — dlatego warto wpisać go do procedury szkoły, żeby wynik nie zależał od tego, kto danego dnia liczy.
2. **„Poziom I / II / III” to nazewnictwo modelu oceny funkcjonalnej**, nie kategoria ustawowa. W dokumentacji ucznia obok poziomu zapisujemy zawsze konkretną formę pomocy z rozporządzenia.
3. **Kierunek skali.** W KSzOF wysoki sten oznacza dobre funkcjonowanie, czyli mniej wsparcia. To odwrotnie niż w skalach nasilenia trudności — warto powiedzieć to rodzicom wprost, żeby nie odczytali stenu 3 jako „trzeciego stopnia dobrego wyniku”.
4. **Reguła nadrzędna.** Średnia i sten mogą zamaskować pojedynczą jedynkę lub dwójkę. Każde takie twierdzenie podlega analizie zespołu niezależnie od wyniku obszaru — to zasada z materiałów autorki, nie z rozporządzenia, ale merytorycznie kluczowa.
5. **Arkusz niepełny.** Druk autorki dopuszcza pozostawienie pozycji pustej, gdy oceniający nie miał możliwości obserwacji, i sam pomija ją w sumie oraz w liczbie twierdzeń. Im więcej braków, tym ostrożniej czytamy sten wyniku ogólnego — wtedy pracujemy na profilu obszarowym.
6. **Ocena 270°.** Nauczyciel, rodzic i specjalista wypełniają cały arkusz niezależnie; wynik uzgodniony ustala zespół i to on trafia do dokumentacji.

Zasada Strażnika: publikatory sprawdzamy w ISAP (isap.sejm.gov.pl) bezpośrednio przed wpisaniem ich do dokumentu ucznia. Weryfikację wykonano wobec druku KSzOF autorki oraz skryptu szkolenia dla szkoły podstawowej.
