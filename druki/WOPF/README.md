# WOPF — Wielospecjalistyczna Ocena Poziomu Funkcjonowania

Karta scalająca ekosystemu **EduPlaner2026-MJ-PCTP**: nie ocenia ucznia od
nowa, tylko zbiera w jednym miejscu wyniki, które powstały wcześniej w innych
drukach (KSzOF, karta ABC/FBA, ToM, kwestionariusz mowy, profil sensoryczny,
profil biopsychospołeczny). Wspólna marka i konstrukcja z serii `ToM/` —
wzorem jest `klasy_1-3`.

## Status: 14 z 27 stron (w budowie)

| Plik | Opis |
|---|---|
| `WOPF_karta_oceny.html` | źródło — w budowie, strony 1–14 gotowe |
| `WOPF_karta_oceny.pdf` | wydruk 14 pierwszych stron (headless Chromium, druk A4) |

Budowa idzie partiami po kilka stron, każda partia renderowana i
zweryfikowana wizualnie względem oryginalnego 27-stronicowego PDF-a autorki,
zanim ruszy kolejna.

## Co jest gotowe (strony 1–14)

- **Str. 1** — tytuł, „Karta scalająca", sekcja I „Dane ucznia" (10 pól, bez
  danych zbędnych — RODO).
- **Str. 2** — sekcja Ia „Ścieżka dokumentacyjna" (Ścieżka A z orzeczeniem →
  IPET / Ścieżka B bez orzeczenia → PWES), rodzaj oceny, sekcja II „Zespół
  specjalistów" (tabela 8 ról).
- **Str. 3** — sekcja III „Mapa dokumentów źródłowych" (11 druków źródłowych
  i sekcja, do której trafia ich wynik — „zasada jednego źródła").
- **Str. 4** — sytuacje szkolne objęte obserwacją, zakres i czas obserwacji,
  sekcja IV „Informacje medyczne".
- **Str. 5–9** — sekcja V „Wyniki oceny funkcjonalnej KSzOF": panel
  synchronizacji druków (`.synbox`, ta sama konstrukcja co w oryginalnym,
  przedsimplifikowanym ToM), tabela 9 obszarów ICF z **edytowalnymi stenami**,
  wykres słupkowy + mapa radarowa (nowa, zbudowana dla WOPF — 9 osi), opis
  wyników **generowany automatycznie** z wpisanych stenów, sekcja Va
  (charakterystyka jakościowa 9 obszarów) i Vb (synteza opisowa, punkty 1–3
  z 4 — punkt 4 przechodzi na stronę 10).
- **Str. 10** — dokończenie sekcji Vb (kierunki pracy), sekcja VI
  „Zachowanie — funkcje zachowań trudnych" (transfer z karty ABC/FBA).
- **Str. 11** — plan pozytywnego wsparcia (PBS), nota o Standardach Ochrony
  Małoletnich, sekcja VII „Poznanie społeczne — teoria umysłu" (transfer z
  ToM), sekcja VIII „Mowa i komunikacja" (transfer z kwestionariusza mowy).
- **Str. 12** — sposób porozumiewania się, kierunki terapii logopedycznej,
  sekcja IX „Przetwarzanie sensoryczne" (transfer z profilu sensorycznego,
  model Dunn).
- **Str. 13** — wnioski sensoryczne, sekcja X „Kontekst biopsychospołeczny"
  (12 czynników środowiskowych ICF), ułatwienia/bariery/dobrostan, nagłówek
  sekcji XI.
- **Str. 14** — sekcja XI „Całościowy obraz funkcjonowania" (tabela synteza
  8 obszarów z kodami ICF i źródłem), sekcja XII „Indywidualne potrzeby
  rozwojowe i edukacyjne" (3 pola opisowe).

## Interaktywność

Tylko sekcja V (wyniki KSzOF) ma pełne przeliczanie automatyczne — to
jedyna sekcja, w której WOPF prezentuje liczby (steny), więc tylko tu ma to
sens. Wpisanie stenu 1–10 w dowolnym z 9 wierszy tabeli automatycznie:
poziom wsparcia w tym samym wierszu (kolor + etykieta Poziom I/II/III),
słupek i punkt na mapie radarowej, średnia ogólna i poziom wsparcia na
stronie 7, opis wyników pod tabelą (zamraża się po pierwszej ręcznej
poprawce — ten sam wzorzec co `#autoOpis` w ToM). Pozostałe sekcje
(VI–XII) to pola i tabele do ręcznego wypełnienia — WOPF tylko *rejestruje*
to, co przenosi się z innych druków, nie przelicza tego samodzielnie.

## Znaleziony i naprawiony błąd konstrukcyjny

Współdzielony arkusz stylów (ten sam co w całej serii ToM) ma regułę, która
automatycznie rozciąga JEDYNĄ tabelę na stronie na 100% wysokości karty
(`flex:1 1 auto;height:100%`), żeby wiersze ładnie wypełniały pustą
przestrzeń. Na stronach, gdzie po tabeli jest jeszcze dużo innej treści
(strony 6, 8, 14), ta reguła konfliktowała z `table-layout:fixed` i
powodowała, że **ostatni wiersz tabeli był rysowany, ale zasłaniany przez
następny blok** (niewidoczny mimo poprawnej pozycji w DOM). Naprawione przez
jawne wyłączenie tego rozciągania (`flex:0 0 auto;height:auto`) na każdej
tabeli budowanej dla WOPF. Przy okazji dociśnięto odstępy na stronach
12–13, które realnie nie mieściły się na jednej karcie.

## Do potwierdzenia przez autorkę

- **Sekcja VII, komponenty ToM (K1–K5)**: oryginalny PDF autorki używa
  innego zestawu komponentów („Świadomość emocji własnych", „Rozpoznawanie
  emocji innych", „Przyjmowanie perspektywy", „Rozumienie intencji", „Język
  niedosłowny") niż którykolwiek z trzech gotowych wariantów ToM w tym
  repozytorium (klasy 1-3/4-6/7-8 mają inne, bardziej rozbudowane nazwy
  komponentów). Przepisane tu **dosłownie z oryginału WOPF** — wymaga
  Twojej decyzji, czy to osobny, uproszczony zestaw K1–K5 (możliwe, że to
  wcześniejsza wersja ToM klasy 1-3, zanim ją rozbudowano), czy pomyłka do
  poprawienia.
- Strony 15–27 jeszcze nie zbudowane (sekcje XIII–XXIII: bariery i
  przyczyny niepowodzeń, sposób pracy, zajęcia i programy, decyzja zespołu,
  cele SMART, ocena efektywności, przekazanie do IPET/PWES).
- Przy stronach 25–26 oryginalnego PDF-u autorki zauważona wcześniej
  anomalia w kolejności „Opinia zespołu" — do sprawdzenia przy budowie tej
  partii.

## Jak powstał PDF

Tak jak reszta serii: `@page{size:A4}` + `@media print` w HTML, PDF to
odpowiednik **Ctrl+P → Zapisz jako PDF**, wygenerowany tu automatycznie
(headless Chromium, `print_background` + `prefer_css_page_size`).
Zweryfikowane renderem: 14 fizycznych stron, żadna nie ucina treści
(sprawdzone programowo — margines do stopki dodatni na każdej stronie).
