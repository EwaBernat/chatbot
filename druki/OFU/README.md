# OFU — Ocena Funkcjonowania Ucznia

Etap **obserwacji/oceny** dla ścieżki B (uczeń **bez orzeczenia**) —
poprzedza PEWS dokładnie tak, jak WOPFU poprzedza IPET na ścieżce A:

| | Etap obserwacji (ocena) | Etap planowania (dokument wynikowy) |
|---|---|---|
| **Ścieżka A** (z orzeczeniem) | WOPFU | IPET |
| **Ścieżka B** (bez orzeczenia) | **OFU** (ten druk) | PEWS |

Dotąd ten etap dla ścieżki B nie miał żadnego dedykowanego narzędzia — PEWS
miało tylko własne, krótkie pola rozpoznania (Sekcje II–IV). OFU to
pogłębione, osobne narzędzie obserwacyjne obok nich — na wyraźną prośbę
autorki PEWS zostało bez zmian, więc pola w obu drukach częściowo się
tematycznie pokrywają (to świadoma decyzja, nie przeoczenie).

## Dlaczego to nie jest WOPFU

WOPFU (i jego 9-obszarowy aparat KSzOF/ICF/sten) to instrument specyficzny
dla ścieżki A, wymagany przez § 6 rozporządzenia o kształceniu specjalnym.
OFU **celowo go nie kopiuje** — zamiast tego używa własnych, prostszych 6
domen funkcjonowania (bez formalnego skalowania sten), obserwowanych
opisowo, adekwatnie do lżejszego wymogu prawnego dla pomocy
psychologiczno-pedagogicznej (Dz.U. 2017 poz. 1591; tekst jednolity:
Dz.U. 2023 poz. 1798).

## Struktura (4 strony)

1. **Dane ucznia i podstawa przeprowadzenia obserwacji** — co skłoniło
   zespół do obserwacji, cel, planowany okres + **Obszar I: Funkcjonowanie
   edukacyjne**.
2. **Obszary II–IV**: Komunikacja i porozumiewanie się, Zachowanie i
   regulacja emocji, Relacje społeczne i rówieśnicze.
3. **Obszary V–VI**: Samodzielność i samoobsługa, Uczestnictwo w życiu
   klasy i szkoły — oraz **Metody i źródła obserwacji**, z tabelą
   wskazującą, czy dla tego ucznia wykorzystano któryś z arkuszy
   źródłowych PCTP (ABC/FBA, Profil sensoryczny, Profil biopsychospołeczny,
   Mowa, ToM) — bez przepisywania ich wyników drugi raz, tylko odesłanie.
4. **Podsumowanie**: obszary priorytetowe, mocne strony, rekomendacja
   zespołu (przekazać do PEWS / kontynuować obserwację / skierować do
   poradni), podpisy, podstawa prawna, RODO.

Każda z 6 domen ma tę samą, powtarzalną strukturę: Mocna strona /
Trudność / Źródło-kiedy + podpowiedź, na czym się skupić.

Ta sama marka PCTP (fiolet `#2D1B69` + pomarańcz `#E8450A`, Mulish/Lora,
`.page`/`.phead`/`.pmeta`/`.pbody`/`.pfoot`, wspólny `base_css.html`) co
cała rodzina WOPFU/PEWS.

## Gęstość stron

Pierwsza wersja miała 5 stron ze 330–469px pustego miejsca na stronę.
Scalona do **4 stron** (99–469px marginesu — dwie strony gęste, dwie ze
świadomym zapasem: strona okładkowa i strona zamykająca z podpisami).

Zweryfikowane: programowy pomiar marginesu (wszystkie dodatnie), skan
poziomego przelewania (0 elementów). Po drodze znaleziony i naprawiony
błąd: nagłówek tabeli „Wykorzystano?" łamał się w połowie wyrazu przy
wąskiej kolumnie — skrócony do „Użyto?" i kolumna poszerzona.

## Odtworzenie PDF

Źródło: generator Python (`build_ofu.py`, poza repozytorium — w
scratchpadzie sesji), analogiczny do `WOPFU/` i `PEWS/` — reużywa te same
funkcje pomocnicze i ten sam `base_css.html`. PDF renderowany przez
headless Chromium (Playwright `page.pdf()`, A4).
