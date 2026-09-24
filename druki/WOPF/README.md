# WOPF — Wielospecjalistyczna Ocena Poziomu Funkcjonowania

Karta scalająca ekosystemu **EduPlaner2026-MJ-PCTP**: nie ocenia ucznia od
nowa, tylko zbiera w jednym miejscu wyniki, które powstały wcześniej w innych
drukach (KSzOF, karta ABC/FBA, ToM, kwestionariusz mowy, profil sensoryczny,
profil biopsychospołeczny). Wspólna marka i konstrukcja z serii `ToM/` —
wzorem jest `klasy_1-3`.

## Status: 14 stron — przebudowa wg przesłanego pliku WOPF.docx

| Plik | Opis |
|---|---|
| `WOPF_karta_oceny.html` | źródło — pełna wersja, wszystkie 14 stron |
| `WOPF_karta_oceny.pdf` | pełny wydruk (headless Chromium, druk A4) |
| `WOPF_SP_bez_poglebionej.html` | wersja skrócona (9 sekcji, **6 stron**), gdy zespół nie prowadzi obserwacji pogłębionej |
| `WOPF_SP_bez_poglebionej.pdf` | wydruk wersji skróconej |

## Nowość: wersja „bez obserwacji pogłębionej" (6 stron)

Wkleiłaś w czacie pełny tekst innej, dużo krótszej wersji WOPF (9 sekcji
rzymskich I–X zamiast 25) i poprosiłaś o taki sam druk, ale bez
obserwacji pogłębionej. Zbudowałam go jako **osobny plik** obok pełnej,
14-stronicowej wersji — to inny, krótszy dokument, nie zamiennik tamtego,
więc żadna z Twoich wcześniej zatwierdzanych stron się nie zmieniła.

**Co zrobiłam z Twoim wklejonym tekstem, żeby faktycznie pasował do „bez
obserwacji pogłębionej":**

- **Usunęłam całą Sekcję VII** („Punkt kontrolny — decyzja zespołu o
  obserwacji pogłębionej") — w Twoim wklejonym tekście ta sekcja
  dokumentowała, że zespół **zdecydował się** przeprowadzić obserwację
  pogłębioną (protokół: „Zespół zarządza przeprowadzenie obserwacji
  pogłębionej..."). To wprost sprzeczne z „bez obserwacji pogłębionej",
  więc ta sekcja nie mogła zostać — nie ma jej w wersji skróconej.
  Kolejne sekcje przesunęłam o jeden numer w dół (VIII→VII, IX→VIII,
  X→IX), żeby nie było dziury w numeracji.
- **Sekcja III (Mapa dokumentów źródłowych) — skrócona z 10 do 5
  wierszy.** Twój wklejony tekst wymieniał też Kartę ABC/FBA, Test ToM,
  Kwestionariusz rozwoju mowy i Profil sensoryczny/biopsychospołeczny —
  to wszystko narzędzia Modułu II (obserwacji pogłębionej). Skoro tej
  obserwacji nie ma, te narzędzia nie zostały użyte, więc usunęłam te 4
  wiersze z mapy źródeł (zostawiłam tylko: metryczka, orzeczenie/opinia,
  KSzOF, wywiad z rodzicem, opinie nauczycieli) i dopisałam pod tabelą
  notkę tłumaczącą dlaczego. **To moja interpretacja — jeśli wolisz mieć
  tam wszystkie 10 wierszy tak jak wkleiłaś, mimo że część nie została
  wykorzystana, daj znać.**
- **Poprawiłam 2 odsyłacze do sekcji, które w Twoim tekście wskazywały
  poza ten dokument** („Wywiad z rodzicem" → „Sekcja X–XII", „Opinie
  nauczycieli" → „Sekcja XI–XVIII") — to sekcje z dłuższej, 25-sekcyjnej
  wersji, których tu nie ma. Zamieniłam na realne sekcje tego dokumentu
  (odpowiednio VII+IX i V–VII).
- **Jedno zdanie w nowej Sekcji VII (Synteza funkcjonalna) zmienione.**
  Punkt 3 w Twoim tekście uzasadniał terapię psychologiczną słowami „w
  oparciu o wyniki ToM" — ale Test Teorii Umysłu to narzędzie Modułu II,
  którego tu nie ma. Usunęłam to uzasadnienie (zdanie zostaje, tylko bez
  tego dopisku) — reszta syntezy w tej sekcji opiera się wyłącznie na
  KSzOF i charakterystyce jakościowej (Sekcje V–VI), więc nie wymagała
  zmian.
- **Kolumnę „Zakres punktu" w tabeli KSzOF (Sekcja V) wypełniłam** —
  w Twoim wklejonym tekście była obecna w nagłówku, ale pusta w każdym
  wierszu. Wpisałam tam zakresy stenów odpowiadające legendzie nad
  tabelą (8–10 / 5–7 / 1–4) — liczy się automatycznie razem z poziomem,
  gdy zmienisz sten.
- **Reszta treści (Sekcje I, II, IV, V, VI, oraz punkty 1, 2 i 4 nowej
  Sekcji VII, Sekcja VIII/Współpraca z rodzicami, Sekcja IX/Podpisy) to
  Twój tekst praktycznie bez zmian** — tylko przeniesiony w gotową
  konstrukcję druku (fiolet `#2D1B69` + pomarańcz `#E8450A`, Mulish/Lora,
  te same `.sec`/`.tb`/`.ta`/`.cbgrid`, co reszta serii).

Zweryfikowane: 6 fizycznych stron (patrz niżej — str. 3 połączona ze
str. 2), margines do stopki dodatni na każdej, zero błędów JS, steny
w Sekcji V przeliczają poziom i zakres punktu automatycznie (tak jak
w pełnej wersji).

### Dodane wykresy i „Wyniki w skrócie" (Sekcja V, str. 4)

Ta krótsza wersja nie miała jeszcze wykresów KSzOF, które pełna,
14-stronicowa wersja już ma — dogoniłam to tutaj:

- **Wykres słupkowy i mapa radarowa** — te same, co w pełnej wersji
  (`build_bar_svg`/`build_radar_svg`), słupki i punkty kolorowane wg
  poziomu (zielony/żółty/czerwony), liczą się automatycznie razem ze
  stenami w tabeli powyżej.
- **„Wyniki w skrócie"** — 9 kompaktowych „chipów" w siatce 3×3 (3
  rzędy), po jednym na obszar: numer rzymski, skrócona nazwa, duży sten
  i poziom, też kolorowane i też aktualizowane na żywo przy edycji
  stenu. To „wybrane elementy pod wykresem" — skrót tabeli powyżej,
  żeby stronę dało się ogarnąć jednym rzutem oka, nie tylko z tabeli.
- **Czcionka podniesiona do 10px** w tabeli i w opisie syntetycznym
  (było 9,9px / 8,6px) — zgodnie z prośbą, żeby tekst na tej stronie
  było wygodniej czytać.
- Żeby to wszystko zmieściło się na jednej stronie bez białych
  przestrzeni, „chipy" są w formie zwartego jednowierszowego paska
  (numer + nazwa + sten + poziom obok siebie), a nie pełnej,
  rozbudowanej karty — pierwsza wersja z pełnowymiarowymi kartami nie
  mieściła się na stronie (wychodziła o ok. 170 px za stopkę).

### Sekcja IV przeniesiona na dół str. 2 (dawna str. 3 zniknęła)

Informacje medyczne (Sekcja IV) miały wcześniej własną, w połowie pustą
stronę 3. Przeniosłam tę sekcję na dół strony 2, razem z Sekcją II
(Zespół) i Sekcją III (Mapa źródeł) — cały dokument skrócił się z 7 do
**6 stron**. Żeby to się zmieściło, checklista chorób i 3 karty
(„Leki", „Zalecenia", „Postępowanie w sytuacji nagłej") są odrobinę
zwarciejsze niż w pierwszej wersji (mniejszy odstęp, bez zmiany treści
merytorycznej) — margines do stopki nadal dodatni, ale ciasny (kilka
pikseli), więc to jedna z gęściej wypełnionych stron w dokumencie.

### Sekcja VII (Synteza funkcjonalna) przeprojektowana — była zbyt monotonna

Zwróciłaś uwagę, że strona z wykresami wygląda dobrze, ale Synteza
Funkcjonalna (dawna str. 6, teraz str. 5) — nie. Miała rację: to był
rząd identycznych, kremowych, przerywaną linią obramowanych karteczek,
bez koloru i bez wyraźnego podziału. Przeprojektowałam ją na 4 kolorowe
karty, po jednej na każdy z 4 punktów syntezy — kolor koduje charakter
punktu, spójnie z resztą dokumentu:

- **1 · Indywidualne potrzeby** — niebieski, siatka 2 kolumn.
- **2 · Mocne strony i uzdolnienia** — zielony (ten sam odcień, co
  Poziom I w tabeli KSzOF), siatka 2 kolumn.
- **3 · Zakres i charakter wsparcia** — fiolet marki PCTP, lista ról
  (kto + co robi) zamiast checkboxów, bo to już ustalone zadania
  zespołu, nie opcje do zaznaczenia.
- **4 · Przyczyny niepowodzeń i bariery** — czerwony (ten sam odcień,
  co Poziom III), siatka 2 kolumn.

Każda karta ma numerowany, kolorowy okrągły znacznik zamiast tekstu
„1 ·", „2 ·" itd. Treść merytoryczna bez zmian — tylko przeorganizowana
z pionowego stosu jednakowych karteczek w coś z wyraźną hierarchią i
kolorem. Margines do stopki nadal dodatni.

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

## Podział na etapy (moduły)

Wg przesłanej „Mapy architektury druku WOPF" (PDF) druk jest wizualnie
podzielony na 4 etapy — bez zmiany numeracji sekcji rzymskich, tylko
dodane kolorowe paski-banery nad sekcją, która rozpoczyna dany etap:

| Etap | Kolor | Gdzie zaczyna się | Sekcje |
|---|---|---|---|
| **MODUŁ I** — Część bazowa | fiolet | str. 1, nad Sekcją I | I–VI |
| **PUNKT KONTROLNY** — Decyzja zespołu | czerwony | str. 5, po tabeli Sekcji VI | — (bramka) |
| **MODUŁ II** — Obserwacja pogłębiona | fiolet | str. 5, nad Sekcją VII | VII–XI |
| **CZĘŚĆ KOŃCOWA** — Planowanie wsparcia | fiolet | str. 7, nad Sekcją XII | XII–XXV |

„Punkt kontrolny" to nowa treść, nie tylko baner — dodałam pod nim 2
checkboxy („Uruchamiam moduł pogłębiony (Sekcje VII–XI)" / „Zamykam na
module I → Część Końcowa (Sekcja XII)"), bo Twoja mapa opisuje to jako
prawdziwą bramkę decyzyjną zespołu, nie tylko nagłówek. Kolor czerwony
(taki sam jak Poziom III w tabeli stenów) celowo odróżnia to jako moment
decyzji, a nie kolejny moduł.

**Nowość:** pod checkboxami doszła krótka notka zamykająca obie ścieżki —
„Zamknięcie na module I" wprost mówi, że obserwacja kończy się tu i zespół
przechodzi od razu do Części Końcowej, a przy module pogłębionym jest
klikalny link **„Załącznik"**, który w HTML (i w większości czytników PDF)
przenosi bezpośrednio do nowego załącznika na str. 13–14 — nie trzeba
kartkować ręcznie.

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
  dokładnie taki tekst, jaki jest w Twoim `.docx`. **Nowość:** pod opisem
  syntetycznym doszło „Podsumowanie jakościowe wg poziomów wsparcia" — pasek
  4 kolorowych kafli (wzór `.bands`: suma stenów + zakres stenów dla
  każdego poziomu) i tabelka 3-wierszowa (Poziom / Obszary / Czego
  dotyczyły) wymieniająca, które konkretnie obszary trafiły na zielony,
  czerwony i żółty poziom oraz czego dotyczyły trudności w każdym z nich —
  wszystko wyliczone z tych samych stenów co tabela i wykres powyżej.
- **Str. 5** — **Sekcja VI: Charakterystyka jakościowa obszarów KSzOF**
  (tabela mocne strony/trudności, Twój dokładny tekst) i **Sekcja VII:
  Obserwacja pogłębiona — zachowania trudne (ABC/FBA) oraz PBS** — połączone
  na jednej stronie, bo osobno zostawały w połowie puste. **Nowość:** na
  górze Sekcji VII, przed „Zachowanie kluczowe", doszła prawdziwa **tabelka
  ABC** (Data / Poprzednik (A) / Zachowanie (B) / Konsekwencja (C)) — 2
  przykładowe zdarzenia z obserwacji (te same, co w prototypie panelu
  nauczyciela z tej samej sesji, dla spójności). To dokładnie metoda, od
  której sekcja bierze nazwę — wcześniej był tylko jeden opisowy akapit
  „zachowanie kluczowe", teraz jest pod nim jako synteza tabeli powyżej.
  Reszta (plan pozytywnego wsparcia, nota o Standardach Ochrony
  Małoletnich) bez zmian treściowych, tylko odrobinę zwarciejszy odstęp,
  żeby nowa tabela zmieściła się na tej samej stronie.
- **Str. 6** — **Sekcja VIII: Poznanie społeczne (ToM)** (tabela 5
  komponentów — wniosek do pracy wypełniony tylko przy pierwszych dwóch,
  tak jak w Twoim pliku, reszta pusta do wypełnienia) i **Sekcja IX: Mowa
  i komunikacja** — połączone z tego samego powodu. **Nowość:** Sekcja IX
  ma teraz tę samą tabelkę co ToM (Sposób porozumiewania się / Wynik 0–2 /
  Wniosek do pracy) zamiast checklisty — 6 sposobów porozumiewania się z
  Twojego pliku jako wiersze, wniosek logopedyczny przy „Mowa werbalna",
  reszta pusta do wypełnienia. Pod tabelą osobna karta „Kierunki terapii i
  zasady pracy w grupie" z resztą oryginalnego tekstu.
- **Str. 7** — **Sekcja X: Przetwarzanie sensoryczne (model Dunna)** —
  **też przebudowana na tabelkę w stylu ToM** (Układ zmysłowy / Wynik 0–2 /
  Wniosek do pracy): 5 układów zmysłowych, wniosek wypełniony przy
  „Słuchowy" i „Przedsionkowo-proprioceptywny" (dokładnie to, co było w
  Twoim opisie profilu), reszta pusta — plus niezmieniona 4-punktowa lista
  „Dieta sensoryczna i organizacja przestrzeni" pod tabelą. Dalej **Sekcja
  XI: Kontekst biopsychospołeczny (ICF) oraz dobrostan**
  (ułatwienia/bariery/dobrostan) — trzy sekcje razem na tej samej stronie,
  każda z nich osobno zostawiała najwięcej pustego miejsca ze wszystkich
  stron.
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
  jednym podpisie) i **Sekcja XXV: Wykaz załączników i RODO** (karta
  „Załączniki" teraz też wskazuje str. 13–14 jako miejsce zbiorczego
  zestawienia obserwacji pogłębionej).
- **Str. 13–14 — nowy Załącznik: „Zbiorcze zestawienie obserwacji
  pogłębionej"** (poza numeracją rzymską — to materiał pomocniczy, nie
  kolejna sekcja WOPF). Str. 13: intro + **A1** tabelka ABC (Sekcja VII),
  **A2** tabelka ToM (Sekcja VIII), **A3** tabelka Mowa (Sekcja IX) — te
  same tabele, co w głównym dokumencie, po prostu przedrukowane razem do
  szybkiego przeglądu. Str. 14: **A4** tabelka Profil sensoryczny (Sekcja
  X), potem „Zakres dostosowań i działań podjętych" (metody wiodące z
  Sekcji XV + tabela dostosowań z Sekcji XVI, też przedrukowane) i na
  końcu „Zalecenia do pracy — podsumowanie" — **to jedyny fragment
  załącznika, który jest moją syntezą**, nie przedrukiem: krótki akapit
  łączący kierunki pracy rozproszone po wnioskach w tabelach A1–A4.
  Dotyczy wyłącznie sytuacji, gdy zespół faktycznie uruchomił moduł
  pogłębiony — dlatego intro na str. 13 wprost to zaznacza.

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

Nowe „Podsumowanie jakościowe" (pasek 4 kafli + tabelka 3-wierszowa) pod
opisem syntetycznym **nie przelicza się samo** po zmianie stenów — to
świadoma decyzja, nie przeoczenie. Pasek kafli (suma stenów, zakresy
poziomów) jest czystym podsumowaniem liczbowym i mógłby się przeliczać
automatycznie, ale tabelka obok wiąże listę obszarów z konkretnym opisem
trudności — po zmianie stenów dla innego ucznia trzeba by przenieść całe
zdania między wierszami, nie tylko przeliczyć listę numerów, więc żeby nie
rozjechać liczb z opisem, żadna z tych dwóch części nie przelicza się sama.
Kolumna „Czego dotyczyły" w tabelce jest zwykłym polem do edycji (tak jak
wszystkie inne pola w tym dokumencie) — dla nowego ucznia podmieniasz
treść ręcznie, tak samo jak sumę stenów w pasku kafli.

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

- **Klauzula RODO (str. 12, Sekcja XXV) — krótsza wersja z Twojego pliku, nie pełna
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
- **Treść kolumny „Czego dotyczyły" w tabelce Podsumowania (str. 4) — moja
  synteza, nie cytat z jednego źródła.** Listę obszarów w każdym wierszu
  (i sumę/zakresy stenów w pasku kafli nad tabelką) wzięłam wprost z
  tabeli/wykresu nad nią (te same steny), ale krótkie opisy „czego
  dotyczyły" dla poziomu II i III ułożyłam sama na podstawie trudności
  opisanych dla tych samych obszarów w Sekcji VI (str. 5, „Charakterystyka
  jakościowa" — kolumna „Trudności"), tylko skrócone do formy tabelkowej.
  To sensowne wnioski wynikające z tego, co już jest w dokumencie, ale to
  synteza, nie gotowy tekst z któregoś z Twoich źródeł — sprawdź, czy te
  konkretne sformułowania Ci odpowiadają.
- **9 obszarów (Sekcja V) vs. 8 obszarów (Sekcja XII) — to samo, co flagowała
  Twoja „Mapa architektury"** w notatce „Do uzgodnienia przed wdrożeniem".
  Potwierdzam, że to realna niezgodność w tym dokumencie: Sekcja V liczy 9
  obszarów ICF (I–IX), a tabela syntezy w Sekcji XII ma inny, 8-punktowy
  podział (Poznawczy, Społeczny, Emocjonalny, Komunikacja i mowa,
  Zachowanie, Sensoryczno-motoryczny, Samoobsługa, Uczestnictwo w życiu
  szkoły) — to inna kategoryzacja, nie te same nazwy przycięte do ośmiu.
  Obie wersje pochodzą z Twojego `.docx` bez zmian z mojej strony. Trzeba
  ustalić, czy Sekcja XII ma używać dokładnie tych samych 9 obszarów co
  Sekcja V, czy to świadomie inny, bardziej ogólny podział na potrzeby
  syntezy — nie zmieniałam żadnej z tabel, dopóki się nie zdecydujesz.
- **Interpretacja prośby „zakończ druk po obserwacji podstawowej / załącznik
  po kliknięciu na informacje pogłębione".** Twoja wiadomość miała kilka
  możliwych odczytań, więc wybrałam wersję, która działa i na papierze, i
  na ekranie: (1) „zakończ druk" — krótka notka przy checkboxie „Zamykam
  na module I", że ta ścieżka kończy się przejściem od razu do Części
  Końcowej (nie da się fizycznie „ukryć" stron w papierowym A4, więc to
  informacja, nie mechanizm pomijania stron); (2) „po kliknięciu" —
  prawdziwy klikalny link (`<a href="#...">`) przy checkboxie „Uruchamiam
  moduł pogłębiony", który w HTML i w czytnikach PDF przenosi do nowego
  Załącznika (str. 13–14) — w druku papierowym to po prostu odsyłacz
  „patrz Załącznik". Jeśli miałaś na myśli coś innego (np. żeby to
  zachowanie dodać w interaktywnym **panelu nauczyciela**, a nie w tym
  drukowanym dokumencie) — daj znać, łatwo to przenieść lub poprawić.
- Żaden z czterech wariantów ToM ani WOPF nie jest jeszcze przeniesiony do
  `Zatwierdzone/` — czeka na Twoje potwierdzenie powyższych punktów.

## Jak powstał PDF

Tak jak reszta serii: `@page{size:A4}` + `@media print` w HTML, PDF to
odpowiednik **Ctrl+P → Zapisz jako PDF**, wygenerowany tu automatycznie
(headless Chromium, `print_background` + `prefer_css_page_size`).
Zweryfikowane renderem: 14 fizycznych stron, żadna nie ucina treści
(sprawdzone programowo — margines do stopki dodatni na każdej stronie, i
zbalansowane tagi `<div>` w całym dokumencie), zero błędów JS,
interaktywność stenów przetestowana.
