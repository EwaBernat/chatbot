# WOPF — Wielospecjalistyczna Ocena Poziomu Funkcjonowania

Karta scalająca ekosystemu **EduPlaner2026-MJ-PCTP**: nie ocenia ucznia od
nowa, tylko zbiera w jednym miejscu wyniki, które powstały wcześniej w innych
drukach (KSzOF, karta ABC/FBA, ToM, kwestionariusz mowy, profil sensoryczny,
profil biopsychospołeczny). Wspólna marka i konstrukcja z serii `ToM/` —
wzorem jest `klasy_1-3`.

## Status: 12 stron — przebudowa wg przesłanego pliku WOPF.docx

| Plik | Opis |
|---|---|
| `WOPF_karta_oceny.html` | źródło — wszystkie 12 stron |
| `WOPF_karta_oceny.pdf` | pełny wydruk (headless Chromium, druk A4) |

**Ta wersja zastępuje poprzednią** (19 ponumerowanych punktów wg ręcznie
wpisanego „Planu WOPF") — przesłałaś plik `WOPF.docx`, który jest
dokładniejszym, autorytatywnym źródłem: 25 sekcji rzymskich (I–XXV) z
konkretną, gotową treścią (nie szablonem). Wróciliśmy więc do układu
sekcji rzymskich, ale z **prawdziwą treścią wyciągniętą z Twojego pliku**
zamiast moich wcześniejszych przykładowych/domyślnych tekstów. Grafika,
kolorystyka i styl bez zmian (fiolet `#2D1B69` + pomarańcz `#E8450A`,
Mulish/Lora, ta sama konstrukcja `.page`/`.sec`/`.cbgrid`/`.ta`).

**Ważne — układ na stronach A4 to moja decyzja, nie 1:1 z Worda.** Twój
`.docx` to płynący dokument bez podziału na strony A4 — 25 sekcji naturalnie
mieściło się różnie gęsto. Żeby uniknąć znanego z poprzednich wersji
problemu pustych stron, połączyłam kilka lżejszych sekcji na wspólne
strony A4 (patrz niżej, „Co jest w środku") — kolejność sekcji jest
dokładnie taka, jak w Twoim pliku, zmieniły się tylko podziały stron.

## Co jest w środku

- **Str. 1** — **Sekcja I: Dane ucznia i ścieżka dokumentacyjna** — pola
  podstawowe, ścieżka A/B, rodzaj oceny i tryb postępowania.
- **Str. 2** — **Sekcja II: Zespół specjalistów** (tabela 8 ról) i
  **Sekcja III: Mapa dokumentów źródłowych** (10 druków źródłowych).
  **Uwaga:** w Twoim pliku ostatnia kolumna tej tabeli („Wynik przeniesiony
  do sekcji") ma przesunięcie o 1 w wierszach 4–8 — np. „Karta ABC/FBA"
  wskazuje tam „Sekcja VI", a w Twoim samym dokumencie treść ABC/FBA jest
  faktycznie w Sekcji VII (bo między nimi jest jeszcze Sekcja VI
  „Charakterystyka jakościowa"). Poprawiłam to przesunięcie w tabeli, żeby
  numery sekcji faktycznie się zgadzały z nagłówkami w Twoim pliku.
- **Str. 3** — **Sekcja IV: Informacje medyczne** — checklist chorób i
  dysfunkcji (10 pozycji z Twojego pliku), leki, zalecenia, postępowanie
  w sytuacji nagłej.
- **Str. 4** — **Sekcja V: Wyniki oceny funkcjonalnej KSzOF** — tabela
  9 obszarów z Twoimi dokładnymi wartościami stenów (8,5,3,7,6,5,4,5,4),
  wykres (liczy się automatycznie z tabeli) i **Twój dokładny opis
  syntetyczny** („Średni wynik ogólny (sten): 5/10 (Poziom II)...").
  Ten opis jest zapisany jako już wypełniony (nie nadpisze się sam po
  zmianie stenów, tak jak reszta zamrożonych notatek w tym dokumencie) —
  dokładnie taki tekst, jaki jest w Twoim `.docx`.
- **Str. 5** — **Sekcja VI: Charakterystyka jakościowa obszarów KSzOF**
  (tabela mocne strony/trudności, Twój dokładny tekst) i **Sekcja VII:
  Obserwacja pogłębiona — zachowania trudne (ABC/FBA) oraz PBS** (zachowanie
  kluczowe, plan pozytywnego wsparcia, nota o Standardach Ochrony
  Małoletnich) — połączone na jednej stronie, bo osobno zostawały w połowie
  puste.
- **Str. 6** — **Sekcja VIII: Poznanie społeczne (ToM)** (tabela 5
  komponentów — wniosek do pracy wypełniony tylko przy pierwszych dwóch,
  tak jak w Twoim pliku, reszta pusta do wypełnienia) i **Sekcja IX: Mowa
  i komunikacja** (checklist sposobów porozumiewania się + wnioski
  logopedyczne) — połączone z tego samego powodu.
- **Str. 7** — dokończenie Sekcji IX (wnioski logopedyczne) i **Sekcja X:
  Przetwarzanie sensoryczne (model Dunna)** (profil + 4-punktowa lista
  „Dieta sensoryczna i organizacja przestrzeni") oraz **Sekcja XI: Kontekst
  biopsychospołeczny (ICF) oraz dobrostan** (ułatwienia/bariery/dobrostan)
  — trzy sekcje razem, każda z nich osobno zostawiała najwięcej pustego
  miejsca ze wszystkich stron.
- **Str. 8** — **Sekcja XII: Całościowy obraz funkcjonowania (synteza)**
  (tabela 8 obszarów, kolumna opisu pusta do wypełnienia — poprawiłam też
  literówkę „FUNKCELONOWANIA" → „FUNKCJONOWANIA" z tytułu w Twoim pliku).
- **Str. 9** — **Sekcja XIII: Przyczyny niepowodzeń i bariery** (4 krótkie
  notatki z Twoim tekstem) i **Sekcja XIV: Zakres i charakter wsparcia**
  (checklist 8 form wsparcia + doprecyzowanie organizacji).
- **Str. 10** — **Sekcja XV: Metody i formy pracy z uczniem** (5 metod
  wiodących z Twojego pliku, zaznaczone jako już stosowane — tak jak
  „PDF" obok każdej sugerowało w źródle, że to już ustalona treść, nie
  przykład do wyboru) i **Sekcja XVI: Dostosowanie wymagań i warunków
  pracy** (tabela 4 kanałów — **w pełni wypełniona Twoimi przykładami**,
  nie pusty szablon jak w poprzedniej wersji).
- **Str. 11** — **Sekcja XVII: Rekomendowane zajęcia specjalistyczne i
  rewalidacyjne**, **Sekcja XVIII: Zintegrowane działania nauczycieli i
  specjalistów**, **Sekcja XIX: Współpraca z rodzicami i międzysektorowa**,
  **Sekcja XX: Decyzja zespołu dotycząca poziomu wsparcia** i **Sekcja
  XXI: Cele SMART** (cel edukacyjny) — pięć sekcji na jednej stronie,
  wszystkie krótkie w Twoim pliku.
- **Str. 12** — dokończenie Sekcji XXI (cel terapeutyczny), **Sekcja XXII:
  Ocena efektywności udzielanego wsparcia** (tabela — Twój plik ma tu
  jeden zbiorczy wiersz „1–8", nie osobny wiersz na każdy zakres, więc tak
  to zostawiłam), **Sekcja XXIII: Przeniesienie informacji do IPET/PWES**
  (Twój jednozdaniowy opis „mostu transferowego", nie rozbudowana tabela
  jak w mojej poprzedniej wersji), **Sekcja XXIV: Podpisy** (5 podpisów —
  Twój plik łączy niektóre role, np. „Psycholog / Pedagog specjalny" w
  jednym podpisie) i **Sekcja XXV: Wykaz załączników i RODO**.

## Interaktywność

Tabela stenów w **sekcji V** ma pełne przeliczanie automatyczne: wpisanie
stenu 1–10 w dowolnym z 9 wierszy liczy poziom wsparcia w tym samym
wierszu, słupek i punkt na mapie radarowej. Opis syntetyczny pod tabelą
jest zapisany jako **już zamrożony** (Twój dokładny tekst z `.docx`,
`data-edited="1"`) — nie nadpisze się automatycznie, tak samo jak każda
inna ręcznie uzupełniona notatka w tym dokumencie. Jeśli będziesz chciała,
żeby dla innego ucznia opis liczył się sam z nowych stenów, wystarczy
skasować treść notatki — mechanizm auto-generowania nadal działa pod
spodem, tylko czeka na pustą notatkę.

## Znalezione i naprawione błędy konstrukcyjne

**Ten sam błąd co poprzednio, tym razem na kartach `.ta`.** Współdzielony
arkusz stylów ma regułę, która automatycznie rozciąga „samotny" element na
stronie na pełną wysokość karty — poprzednio łapało to tabele
(`table{flex:1 1 auto;height:100%}`), tym razem złapało też **karty
`.ta`** używane przez `ta_card()`/`ta_inner()`
(`.blk:has(>.ta)>.ta{flex:1}`). Na stronach z kilkoma krótkimi kartami
`.ta` z rzędu (np. Sekcja VII: 3 karty), każda z nich osobno rozciągała
się na ~1/3 wysokości strony zamiast trzymać naturalną, zwartą wysokość
tekstu — więc 3 zdania zajmowały całą stronę. Naprawione tak samo jak
poprzednio: `flex:0 0 auto` na karcie i jej opakowaniu `.blk`, tym razem
wbudowane bezpośrednio w funkcje `ta_card()`/`ta_inner()`, więc naprawa
obowiązuje wszędzie, gdzie te funkcje są użyte w tym dokumencie.

## Do potwierdzenia przez autorkę

- **Klauzula RODO (str. 12) — krótsza wersja z Twojego pliku, nie pełna
  7-punktowa.** Twój `.docx` ma jeden akapit RODO. Wcześniej w tej sesji
  (poprzednia wersja WOPF) była pełna, 7-punktowa klauzula informacyjna
  RODO (administrator, IOD, cel i podstawa prawna, kategorie danych,
  odbiorcy, okres przechowywania, prawa osób) — to bardziej kompletne
  spełnienie obowiązku informacyjnego z art. 13/14 RODO. Zostawiłam tu
  Twoją krótszą wersję (fidelity do przesłanego pliku), ale jeśli wolisz
  pełną klauzulę z powrotem — jest w historii gita (`git log`), mogę ją
  przywrócić jednym ruchem.
- **Poprawka przesunięcia numerów sekcji w mapie dokumentów (str. 2,
  Sekcja III)** — opisana wyżej w „Co jest w środku". Sprawdź, czy to
  faktycznie była pomyłka w oryginalnym pliku, czy numeracja w Twoim
  `.docx` miała inne znaczenie, którego nie uchwyciłam.
- **Podział na strony A4 to moja decyzja** (opisana na górze) — połączyłam
  kilka sekcji na wspólne strony, żeby uniknąć pustych stron. Jeśli wolisz
  np. każdą sekcję na osobnej stronie mimo pustego miejsca (łatwiej
  komuś dopisywać ręcznie po wydruku) — daj znać, mogę rozdzielić z
  powrotem.
- Żaden z czterech wariantów ToM ani WOPF nie jest jeszcze przeniesiony do
  `Zatwierdzone/` — czeka na Twoje potwierdzenie powyższych punktów.

## Jak powstał PDF

Tak jak reszta serii: `@page{size:A4}` + `@media print` w HTML, PDF to
odpowiednik **Ctrl+P → Zapisz jako PDF**, wygenerowany tu automatycznie
(headless Chromium, `print_background` + `prefer_css_page_size`).
Zweryfikowane renderem: 12 fizycznych stron, żadna nie ucina treści
(sprawdzone programowo — margines do stopki dodatni na każdej stronie, i
zbalansowane tagi `<div>` w całym dokumencie), zero błędów JS,
interaktywność stenów przetestowana.
