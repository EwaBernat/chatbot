# Kwestionariusz oceny rozwoju mowy — klasy IV–VI

Wariant wiekowy `klasy_1-3/` dla klas IV–VI. Ta sama konstrukcja, formuła
stenowa i logika co w `klasy_1-3/` (zobacz tamten `README.md` po pełny opis
przebudowy z innego systemu szablonów i napraw wspólnych dla całej serii:
podwójna numeracja „VI", brakujący CSS ramki SMART, ukryte rozciąganie
kart z wykresem) — tu tylko różnice specyficzne dla tego wariantu.

## Skąd ten druk

Przesłałaś `kwest_mowy_4_6.html` — ten sam kwestionariusz logopedyczny co
`klasy_1-3/`, ale z 25 pozycjami dobranymi do etapu klas IV–VI (bardziej
złożone umiejętności: sekwencje sylab, analiza fonemowa, wnioskowanie
z tekstu, definiowanie pojęć, argumentacja). Ekstrahowany w całości przed
budową (weryfikacja tekstu pozycja po pozycji, kodów ICF i wartości demo).

## Poprawiona niespójność nazw działów

Sprawdzając treść znalazłam, że sekcja „Działy wymagające terapii" (str. 3)
w przesłanym pliku była **dosłowną kopią** z wariantu klasy I–III — nazwy w
niej („Artykulacja i słuch fonematyczny", „Rozumienie mowy", „Mowa czynna")
nie pasowały do własnych, dostosowanych do wieku tytułów tabeli
kwestionariusza tego pliku („Artykulacja i fonologia", „Rozumienie mowy i
tekstu", „Mowa czynna i narracja"). Ujednoliciłam checklistę do tytułów
używanych w tabeli tego wariantu — reszta sekcji (mocne strony, formy
terapii, ćwiczenia domowe, dostosowania, karty diagnozy, podstawa prawna)
była w źródle identyczna dla obu wariantów, więc zostawiłam bez zmian.

## Struktura (4 strony) — identyczna z klasy_1-3

| Nowa strona | Zawartość |
|---|---|
| str. 1 | Tytuł, etap/źródło informacji, Metryczka (I), Arkusz kwestionariusza (II) — skala + działy I–III (15 pozycji) |
| str. 2 | dokończenie arkusza — działy IV–V (10 pozycji), Wykres słupkowy (III) + szybki odczyt + wynik ogólny + progi |
| str. 3 | Mapa radarowa (III c.d.) + opis merytoryczny, Podsumowanie działów (IV), Mocne strony (V), Działy wymagające terapii (VI) |
| str. 4 | Wskazanie do diagnozy pogłębionej + powiązanie z WOPF/IPET, Cele SMART (VII), Formy terapii (VIII), Ćwiczenia i dostosowania (IX), ewaluacja, podpisy, podstawa prawna |

## Zweryfikowane

Ten sam pełny cykl co `klasy_1-3/`: margines do stopki 9–86px na
wszystkich 4 stronach, zero błędów JS, automatyczne przeliczanie sten/
poziom/wykres po kliknięciu oceny sprawdzone na żywo (10→13 pkt poprawnie
dało sten 3→5), checkbox/radio/synchronizacja metryczki między stronami —
wszystko działa.

Dokument nie jest jeszcze przeniesiony do `Zatwierdzone/` — czeka na Twoje
potwierdzenie punktów wyżej.
