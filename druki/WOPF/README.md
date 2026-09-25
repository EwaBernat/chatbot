# WOPF — Wielospecjalistyczna Ocena Poziomu Funkcjonowania

Karta scalająca ekosystemu **EduPlaner2026-MJ-PCTP**: nie ocenia ucznia od
nowa, tylko zbiera w jednym miejscu wyniki, które powstały wcześniej w innych
drukach (KSzOF, karta ABC/FBA, ToM, kwestionariusz mowy, profil sensoryczny,
profil biopsychospołeczny). Wspólna marka i konstrukcja z serii `ToM/` —
wzorem jest `klasy_1-3`.

## Arkusz zespołowy: nowa strona 9 — KSzOF połączone z ocenami (kody ICF + zalecenia wg 9 obszarów)

**Nowa strona, dopisana pod tabelą „Wyniki arkuszy źródłowych" (Sekcja 2).**
Na Twoją prośbę doszła strona 9 — 9 kart, po jednej na każdy obszar KSzOF (te
same nazwy, steny i poziomy co w Sekcji V, str. 4), a w każdej karcie:
- **Kody ICF pasujące do stwierdzonych trudności** tego obszaru (np. Obszar
  III „Porozumiewanie się" → d310, d330, d350; Obszar IV „Motoryka" → d445,
  b760) — dobrane do opisów trudności z Sekcji VI (str. 5), nie generyczne.
- **Obszar VII „Wzajemne kontakty i związki" połączony dodatkowo z Profilem
  ToM i ABC/FBA** (zgodnie z Twoim przykładem) — osobna notka pod nagłówkiem
  wprost mówi, że niski wynik tego obszaru łączy się z trudnością ToM
  (rozumienie cudzych intencji) i wzorcem ABC/FBA (ucieczka/unikanie przy
  zmianie aktywności), z odsyłaczem do str. 8. Kody ICF tego obszaru też to
  odzwierciedlają: d710/d720 (interakcje) + b152 (funkcje emocjonalne, z ToM)
  + d7203 (kontrolowanie zachowania w interakcji, z ABC/FBA).
- **6 kategorii zaleceń do realizacji**, dokładnie te, o które prosiłaś:
  metody i formy pracy, zakres dostosowań, zintegrowane działania
  nauczycieli, materiały dydaktyczne, zalecenia, cele edukacyjne i
  terapeutyczne — w zwartej siatce 2 kolumny × 3 wiersze pod każdą kartą.

Wszystko edytowalne (kody ICF i każde z 6 pól), tak jak reszta dokumentu —
treść to przykładowe uzupełnienie na bazie tego samego przypadku demo, do
podmiany dla konkretnego ucznia.

**Techniczna pułapka po drodze: `justify-content:space-between` na całej
stronie maskowało prawdziwy rozmiar treści.** Współdzielony CSS ma regułę,
która domyślnie rozciąga zawartość strony równomiernie na całą wysokość,
jeśli strona nie zawiera żadnego z kilku konkretnych, niepowiązanych z tym
komponentów (używanych gdzie indziej w dokumencie). Moje karty nie pasowały
do żadnego z nich, więc ta reguła się włączała: skracanie treści nie
zmieniało w ogóle zmierzonego marginesu na dole strony (wciąż ~12px), bo
oszczędzone piksele po prostu zamieniały się w większe odstępy MIĘDZY
kartami zamiast zmniejszać całkowitą wysokość — złapane dopiero pomiarem
rzeczywistej wysokości każdego bloku, nie tylko marginesu na dole. Efekt
uboczny: 9 kart przy tej regule wyglądałoby na ekranie/wydruku z ogromnymi,
nierównymi odstępami zamiast zwartej listy. Naprawione lokalnie (tylko na
tej stronie, nie w współdzielonym pliku CSS) przez jawne
`justify-content:flex-start` na tej jednej stronie. Po naprawie 9 kart
zmieściło się wygodnie na jednej stronie z marginesem 138px — początkowo
myślałam, że będą potrzebne 2 strony, ale to był efekt tej samej maskowanej
miary.

Zweryfikowane: `render_check_team.py` (11 stron, wszystkie bez przelewania),
edytowalność sprawdzona klikaniem i wpisywaniem tekstu, wizualnie na
rzeczywistym PDF-ie, zero błędów JS.

## Arkusz zespołowy: „Autor" → „Sporządzający" oraz nowa linia „Zalecenie do programu" w każdym profilu (str. 8)

**„Autor" → „Sporządzający" w metryczce każdego arkusza.** Na Twoją prośbę
zmieniłam etykietę w metryczce (Data / ~~Autor~~ Sporządzający / Nr arkusza)
we wszystkich 5 profilach w Sekcji 2 Załącznika — krótsza wersja z Twoich
dwóch propozycji, bo pełne „Nauczyciel sporządzający obserwację i opis" nie
mieściło się w wąskiej (46mm) kolumnie metryczki bez rozbicia na kilka linii.

**Nowa, trzecia linia w każdym profilu: „Zalecenie do programu
(IPET/PWES)".** Osobno od ogólnej „Charakterystyki" i „Zaleceń" (kierunki
pracy na co dzień), każdy z 5 profili dostał teraz wyróżnioną pomarańczowym
kolorem linię mówiącą wprost, co z tego wyniku wynika dla dokumentu
wynikowego — jaki to rodzaj wpisu (cel SMART, dostosowanie organizacyjne czy
warunek pracy) i jak decyzja zależy od faktycznego wyniku, np. dla ABC/FBA:
„jeśli ucieczka nadal występuje mimo modyfikacji poprzedników → cel SMART w
IPET; jeśli ustąpiła → utrzymać dostosowania profilaktycznie, bez osobnego
celu". To domyka most: Sekcja 2 (wyniki) → ta nowa linia (co to znaczy dla
programu) → Sekcja 4 (zalecenia zbiorcze) → IPET/PWES.

**Strona się przelała po dodaniu trzeciej linii (margines -85px), więc
skompresowałam styl tabeli** (padding 6px 9px→5px 8px, czcionka 8.8px→8.3px,
interlinia 1.5→1.3) zamiast skracać treść — margines wrócił do +71px, bez
przelewania. Czcionka jest teraz mała, ale wciąż czytelna (podobna gęstość
już zaakceptowana wcześniej na str. 3 i 5 tego dokumentu). Zweryfikowane:
`render_check_team.py`, edytowalność nowej linii sprawdzona klikaniem i
wpisywaniem tekstu, „Autor" faktycznie zniknął ze strony (sprawdzone
programowo), zero błędów JS.

## Arkusz zespołowy: Sekcja 2 Załącznika przebudowana — charakterystyka i zalecenia zamiast pustych pól (str. 8)

**Problem: „wyniki arkuszy źródłowych" był mdły i zbyt wąsko rejestrował dane.**
Poprzednia wersja tabeli miała same wąskie pola do ręcznego uzupełnienia
(„Liczba zapisanych zdarzeń: ___", „Wynik: ___") — bez żadnej gotowej treści
merytorycznej, więc strona wyglądała pusto i nie pokazywała, jak faktycznie
korzystać z danych z innych narzędzi.

**Nowa kolejność źródeł: Profil biopsychospołeczny → ABC/FBA → Profil
sensoryczny → Rozwój mowy → Profil ToM** (poprzednio: ABC/FBA, sensoryczny,
mowa, ToM, biopsychospołeczny — na Twoją prośbę biopsychospołeczny przeszedł
na pierwsze miejsce, ToM na ostatnie).

**Każde źródło ma teraz prawdziwą charakterystykę i zalecenia**, nie puste
pola — na bazie tego samego przypadku demonstracyjnego, co w pozostałych
dwóch drukach WOPF (te same steny, te same karty Ułatwienia/Bariery/
Dobrostan, ten sam ABC, ten sam profil Dunna, ta sama ocena ToM i mowy), więc
wszystkie trzy dokumenty opisują teraz spójnie jednego przykładowego ucznia:
- **Profil biopsychospołeczny** — ułatwienia/bariery/dobrostan + czynniki
  środowiskowe (e310, e330/e425) i zalecenie utrzymania struktury dnia.
- **ABC/FBA** — 2 zdarzenia z arkusza, zachowanie kluczowe (ucieczka/unikanie
  wymagań) i plan PBS (modyfikacja poprzedników + zachowanie zastępcze).
- **Profil sensoryczny** — wrażliwość słuchowa i poszukiwanie bodźców
  przedsionkowo-proprioceptywnych, z konkretną dietą sensoryczną.
- **Rozwój mowy** — poziom mowy werbalnej i kierunki terapii logopedycznej.
- **Profil ToM** — poziom świadomości emocji i konkretne metody pracy (TUS,
  historyjki społeczne, zamiana ról).

Metryczka (Data / Autor / Nr arkusza) została bez zmian — to pola, które
faktycznie różnią się dla każdego ucznia, więc zostają puste i edytowalne.
Charakterystyka i zalecenia są też w pełni edytowalne (osobne `contenteditable`
pod etykietami „Charakterystyka:"/„Zalecenia:", żeby po podmianie ucznia dało
się je nadpisać, tak jak wszystkie inne pola w dokumencie) — zweryfikowane
przez faktyczne kliknięcie i wpisanie tekstu w przeglądarce, nie tylko
wizualnie. Zweryfikowane też `render_check_team.py` (margines na str. 8 spadł
z dużego zapasu do 140px — bez przelewania) i wizualnie na renderze
rzeczywistego PDF-a.

## Druk podstawowy: przywrócona pełna klauzula RODO oraz czynniki kontekstowe wg ICF

**Pełna, 7-punktowa klauzula informacyjna RODO + ważność dokumentu (str. 13,
Sekcja XXV).** Na Twoją prośbę zamieniłam skróconą, jednoakapitową wersję
RODO w druku podstawowym (`WOPF_karta_oceny`) na pełną klauzulę informacyjną
z art. 13/14 RODO — 7 punktów: administrator danych, inspektor ochrony
danych, cel i podstawa prawna, kategorie danych, odbiorcy, okres
przechowywania, prawa osób. Dodałam też osobną notkę „Bezpieczeństwo i
ważność dokumentu" (podpisy zespołu potwierdzają dokonanie oceny; podpis
rodzica potwierdza zapoznanie się z oceną, ale jego brak nie wstrzymuje
oceny — ewentualną odmowę należy odnotować). Nagłówek sekcji zmienił się na
„Wykaz załączników, RODO i ważność dokumentu". Ta pełna klauzula była już
raz napisana wcześniej w tej sesji i świadomie skrócona pod fidelity do
wzoru — przywróciłam ją teraz jednym ruchem z historii gita (commit
`50d405c`), tak jak zapowiadałam w sekcji „Do potwierdzenia przez autorkę"
niżej.

**Czynniki kontekstowe wg ICF (str. 8, Sekcja XI).** Dopisałam osobny
podrozdział „Czynniki kontekstowe wg ICF — czynniki środowiskowe i osobowe"
pod istniejącą triadą ułatwienia/bariery/dobrostan: checklisty czynników
środowiskowych (wsparcie rodziny i otoczenia — e310, postawy nauczycieli i
rówieśników — e330/e425) oraz czynników osobowych (temperament i styl
radzenia sobie ze stresem, motywacja i poczucie sprawczości). Też
przywrócone z historii gita (commit `6bfd4a2`), gdzie ta treść była już
raz napisana. Zweryfikowane: `render_check.py` (bez przelewania na żadnej
z 15 stron), `js_check.py` (zero błędów, przeliczanie stenów dalej działa)
i wizualnie na renderze rzeczywistego pliku PDF (nie tylko podglądu HTML).

## Załącznik: podpisy zespołu na końcu (str. 10)

Załącznik „Obserwacja pogłębiona" kończył się polami „Data ustalenia
zaleceń" i „Zespół" — bez miejsca na faktyczne podpisy, mimo że to
osobny, samodzielny dokument roboczy (patrz niżej), więc powinien mieć
własne zamknięcie, tak jak główny dokument ma swoje na str. 6 (Sekcja X).
Dodałam na samym końcu str. 10 nowy nagłówek „Podpisy zespołu
prowadzącego obserwację pogłębioną" i 4 linie podpisu: **Koordynator
zespołu** (nazwany, tak jak w tabeli ustaleń na str. 7) oraz 3 ogólne
**„Członek zespołu"** — celowo bez sztywno przypisanych ról (logopeda,
psycholog, terapeuta SI...), bo to, kto faktycznie podpisuje, zależy od
tego, które arkusze zespół włączył do konkretnej obserwacji. Ładnie
wypełniło to też sporo pustego miejsca na dole ostatniej strony
(margines spadł z 344 do 130 px).

## Załącznik: lepsze uzasadnienie obserwacji + przycisk „dodaj wiersz" + naprawiony błąd w tle

**Lepsze, rozwinięte uzasadnienie na str. 7.** Poprzednia wersja Załącznika
miała po przesłankach tylko jedno zdanie („Dwa wpisy ABC wskazują sytuacje
do sprawdzenia..."), które samo w sobie nie uzasadniało decyzji o
obserwacji. Zamieniłam je na pełny, szary „WZÓR UZASADNIENIA" (ten sam
komponent `.example-box`, co na Punkcie Kontrolnym w głównym dokumencie):
łączy wszystkie 3 przesłanki (niskie wyniki KSzOF, zdarzenia ABC, brakujące
wyniki mowy/ToM/sensoryki) we wniosek, dlaczego obserwacja jest zasadna i
co ma dać (weryfikacja hipotez, uzupełnienie danych, cele do IPET).

**Tabela „Współpraca z rodzicami" (str. 6) — teraz z przyciskiem „+ Dodaj
kolejną formę współpracy".** Poprzednio jedyny sposób na dopisanie
kolejnej formy współpracy to ręczne wpisanie w jeden zapasowy, pusty
wiersz. Dodałam działający przycisk (widoczny tylko na ekranie, nie na
wydruku) — każde kliknięcie dokłada nowy, w pełni edytowalny wiersz do
tabeli przez JavaScript, więc można dopisać dowolną liczbę własnych form
współpracy, nie tylko jedną. Sprawdzone dwoma kliknięciami i wpisaniem
tekstu w nowo dodany wiersz — działa.

**Przy okazji budowy przycisku znalazłam i naprawiłam realny błąd w
mechanizmie „nie drukuj".** Klasa `no-print` (używana m.in. na górnym
pasku narzędzi ✍️ we wszystkich trzech dokumentach) nie miała **żadnej**
reguły CSS, która faktycznie by ją ukrywała przy druku — pasek narzędzi
znikał z PDF-ów tylko przypadkiem, bo jest `position:fixed` (Chromium
samo pomija taki element przy łamaniu na strony). Gdy dodałam przycisk
zwykłym blokiem (`position` domyślne), `no-print` nic nie robiło i
przycisk **pojawiał się w PDF-ie** — złapałam to, renderując rzeczywisty
plik PDF, nie tylko podgląd w przeglądarce. Naprawione we wspólnym pliku
CSS (`@media print{.no-print{display:none}}`), więc `no-print` teraz
faktycznie działa **we wszystkich trzech dokumentach**, na każdym
elemencie, nie tylko na pasku narzędzi. Zweryfikowane renderując gotowy
PDF (nie tylko podgląd HTML) — przycisk zniknął, reszta bez zmian.

## Nowość: Załącznik „Obserwacja pogłębiona" dopisany do arkusza zespołowego (str. 7–10)

Przesłałaś osobny plik Word — `EduPlanner_2026_WOPF_SP_uzupełnienie_i_obserwacja_pogłębiona_2.docx` —
i poprosiłaś o „piękny druk" z tego jako Załącznik. To 4-sekcyjny,
samodzielny dokument roboczy do prowadzenia obserwacji pogłębionej: nie
duplikuje niczego z arkusza zespołowego, tylko rozwija to, na czym Sekcja
VII tego dokumentu (Punkt Kontrolny) się kończy — decyzję „uruchamiam
obserwację pogłębioną". Dlatego dopisałam go jako 4 nowe strony na końcu
`WOPF_SP_arkusz_zespolowy` (6→10 stron w tamtym momencie; od dopisania str. 9
z kodami ICF — patrz sekcja na górze pliku — dokument ma już **11 stron**),
w tej samej konstrukcji `.page`/`.sec`/`.tb`, a nie jako osobny plik.

- **Str. 7 — Załącznik, Sekcja 1: Decyzja o obserwacji pogłębionej.**
  Czerwony baner „ZAŁĄCZNIK" (ten sam wzór, co „PUNKT KONTROLNY"), 3
  przesłanki z Twojego pliku (KSzOF, wpisy ABC, brakujące wyniki mowy/
  ToM/sensoryki), tabela „jakie arkusze włączyć" (5 wierszy: ABC/FBA,
  profil sensoryczny, arkusz mowy, profil ToM warunkowo, profil
  biopsychospołeczny) i tabela ustaleń zespołu (koordynator, termin,
  data syntezy).
- **Str. 8 — Sekcja 2: Wyniki arkuszy źródłowych.** Duża tabela — dla
  każdego z 5 arkuszy osobno: metryczka (data / sporządzający / nr arkusza)
  i trzy linie na bazie wyników z tego narzędzia — charakterystyka, zalecenia
  i wyróżnione „Zalecenie do programu (IPET/PWES)" (nie puste pola — patrz
  sekcja na górze pliku), w kolejności: profil biopsychospołeczny, ABC/FBA,
  profil sensoryczny, rozwój mowy, profil ToM. Poniżej 3 checkboxy stanu
  danych i pole na brakujące arkusze.
- **Str. 9 — Sekcja 2 (ciąg dalszy): KSzOF połączone z ocenami.** Dopisana
  później — patrz sekcja na górze pliku.
- **Str. 10 — Sekcja 3: Synteza obserwacji** (przesunięta ze str. 9 po
  dopisaniu str. 9 z kodami ICF). Dwie tabele: „co wynika z kilku źródeł"
  (4 obszary × ustalenie × źródło/niepewność) i „opis zbiorczy do WOPF-SP"
  (mocne strony / trudności / warunki / dane brakujące) — dokładnie Twoje
  pola, puste do wypełnienia.
- **Str. 11 — Sekcja 4: Zalecenia z orzeczenia i oceny** (przesunięta ze
  str. 10). Część A (zalecenia z orzeczenia — dane dokumentu, checkbox
  „uczeń nie ma orzeczenia", 3 puste wiersze na zalecenia) i część B
  (zalecenia zespołu z oceny, też 3 puste wiersze).

**Jedna zmiana treści — z konieczności, nie wyboru.** Twój plik w dwóch
miejscach mówił „jeżeli zaleceń jest więcej, dodaj wiersze w Wordzie" —
to nie ma sensu w gotowym, statycznym druku HTML/PDF (nie da się „dodać
wiersza" na wydrukowanej kartce). Zamieniłam na „kontynuuj na osobnej
kartce, zachowując numer punktu/strony" — ta sama intencja (jest miejsce
na więcej niż 3 zalecenia), tylko sformułowana dla fizycznego wydruku,
a nie edytowalnego pliku Word.

**Kilka stron (7, 9, 10) ma sporo pustego miejsca u dołu** — próbowałam
łączyć sekcje 3+4 na jedną stronę, ale realnie nie mieściło się (margines
do stopki wychodził na -180 px), więc zostały osobno. Czteroelementowa
treść z Twojego Worda naturalnie rozkłada się na 4 strony w tej
konstrukcji wizualnej — gdybyś wolała gęściej upakowane strony kosztem
mniejszej czcionki, daj znać.

## Kolory poziomów wsparcia odświeżone (oba dokumenty)

Zwróciłaś uwagę, że kolory Poziomu I/II/III (używane wszędzie: tabele
stenów, wykresy słupkowe i radarowe, „Wyniki w skrócie", karty Syntezy,
checkboxy decyzji zespołu) wyglądały stonowanie — a Poziom II konkretnie
jak brąz zamiast żółtego. Zmieniłam całą paletę na wersję bardziej
soczystą/nasyconą, w obu dokumentach naraz (jeden wspólny słownik
`POZIOM_COL` + jedna funkcja `wopfStenPoziom()` w JS, więc zmiana jest
spójna wszędzie, gdzie te kolory się pojawiają):

| Poziom | Było | Jest |
|---|---|---|
| I (zielony) | `#2E7D46` | `#16A34A` |
| II (żółty) | `#9a6b00` (wyglądał na brązowy) | `#D6A400` |
| III (czerwony) | `#b3261e` | `#DC2626` |

Konsekwentnie zmieniłam też 2 miejsca, które świadomie **kopiowały** te
same kolory dla spójności wizualnej, więc zostawienie ich po staremu
zepsułoby tę spójność: gradient banera „PUNKT KONTROLNY" w pełnym
dokumencie (używał tego samego czerwonego, co Poziom III) oraz karty
1 i 3 Syntezy funkcjonalnej w wersji skróconej („Mocne strony" i
„Przyczyny/bariery" — dobrałam im wcześniej kolory „ten sam odcień, co
Poziom I/III w tabeli KSzOF"). Jasne, pastelowe tła (np. `#eafaef`,
`#fff6da`, `#fdecec` pod kartami/chipami) zostawiłam bez zmian — to
neutralne, bardzo jasne podkłady, które dobrze współgrają z każdym
odcieniem pierwszego planu i nie wyglądały na „brązowe" same w sobie.

**Druga runda — same słupki wykresów jeszcze bardziej soczyste.** Napisałaś
jeszcze raz, mocniej, że kolory słupków w wykresach mają być piękne,
soczyste. Rozdzieliłam więc kolor na dwa warianty: `col` (jak wyżej —
używany tam, gdzie kolor jest jednocześnie tekstem: „Poziom I/II/III"
w tabeli, etykiety w chipach, checkboxy decyzji — tam musi zostać
czytelny na białym tle) i nowy `barCol`, używany wyłącznie do wypełnienia
słupków wykresu — bo słupek to duży, jednolity kwadrat koloru bez tekstu
na sobie, więc może być dużo bardziej nasycony bez utraty czytelności:

| Poziom | `col` (tekst, chipy, checkboxy) | `barCol` (tylko słupki wykresu) |
|---|---|---|
| I (zielony) | `#16A34A` | `#12B451` |
| II (żółty) | `#D6A400` | `#FFD500` — prawdziwy, czysty żółty |
| III (czerwony) | `#DC2626` | `#E8253D` |

Zmiana jest w jednym miejscu (`wopfStenPoziom()`) w każdym z **trzech**
dokumentów (w tym w nowym arkuszu zespołowym), więc słupki wyglądają
identycznie we wszystkich. Mapa radarowa i tak nie używała kolorów
Poziomu — jej fiolet/pomarańcz to kolorystyka marki, niezależna od tego
systemu.

## Status: trzy warianty druku — do porównania i wyboru najlepszej opcji

| Plik | Opis |
|---|---|
| `WOPF_karta_oceny.html` | pełna wersja, 25 sekcji, 15 stron |
| `WOPF_karta_oceny.pdf` | pełny wydruk (headless Chromium, druk A4) |
| `WOPF_SP_bez_poglebionej.html` | wersja skrócona (9 sekcji, **6 stron**), gdy zespół nie prowadzi obserwacji pogłębionej |
| `WOPF_SP_bez_poglebionej.pdf` | wydruk wersji skróconej |
| `WOPF_SP_arkusz_zespolowy.html` | trzeci wariant, „arkusz zespołowy" (10 sekcji + Załącznik „Obserwacja pogłębiona", **11 stron**), zbudowany wg Twojego przesłanego wzoru PDF |
| `WOPF_SP_arkusz_zespolowy.pdf` | wydruk arkusza zespołowego |

Szukasz najlepszej opcji spośród trzech — żaden z wariantów nie jest jeszcze
przeniesiony do `Zatwierdzone/`.

## „Arkusz zespołowy" (10 sekcji, 6 stron podstawowych) — trzeci wariant

Przesłałaś PDF „piękny WOPF-z czata" — inny, prostszy arkusz (bez kolorów,
bez wykresów, same tabele do wypełnienia), z prośbą „zrób według tego wzoru,
dodaj stronę z kolorowymi wykresami". Zapytałam, czy ma to zastąpić wersję
skróconą, czy być osobnym dokumentem — wybrałaś **osobny, trzeci plik**, bo
szukasz najlepszej opcji, nie jednej ostatecznej wersji.

**Co jest wierne Twojemu wzorowi:**

- Dokładnie 10 sekcji rzymskich (I–X) z Twojego PDF-a, w tej samej
  kolejności i z tym samym tekstem — łącznie z sekcją **VII: Decyzja
  zespołu o obserwacji pogłębionej** (Twój wzór jej nie usuwa, tylko
  zostawia otwartą: kontynuować / uzupełnić dane / przejść do planowania),
  czym ten wariant różni się od wersji skróconej (która tę sekcję usuwa
  całkowicie) i od pełnej wersji (która zakłada, że zespół już zdecydował
  się na obserwację pogłębioną).
- Wszystkie pola są **puste, do wypełnienia** — zgodnie z Twoim wzorem
  („Pola należy wypełnić danymi konkretnego ucznia; wcześniejsze przykłady
  wyników nie są przenoszone do druku"), łącznie z notatkami metodologicznymi
  z Twojego PDF-a (np. „Nie obliczaj średniej ze stenów jako nowego wyniku
  narzędzia bez podstawy metodologicznej").
- Ścieżka A/B, mapa 10 dokumentów źródłowych, tabela 6 ról zespołu, 6 ról
  „Zakresu i charakteru wsparcia" (VIII.3) — treść przepisana z Twojego
  pliku bez zmian, tylko przeniesiona w konstrukcję `.page`/`.sec`/`.tb`
  fioletu `#2D1B69` + pomarańczu `#E8450A`, Mulish/Lora, zamiast gołego,
  czarno-białego układu z PDF-a.

**Jedno odstępstwo od wzoru — „strona z kolorowymi wykresami", o którą
prosiłaś:** Twój PDF ma w Sekcji V samą pustą tabelę (Nr / Obszar / Wynik /
Poziom / Źródło), bez żadnego wykresu. Dodałam pod tabelą dokładnie ten sam
zestaw wykresów, co w pozostałych dwóch dokumentach — słupkowy + mapa
radarowa + siatka „Wyniki w skrócie" (9 kolorowych chipów) — i **wypełniłam
tabelę tym samym przykładowym przypadkiem, co reszta serii** (steny
8,5,3,7,6,5,4,5,4), żeby wykresy było faktycznie widać kolorowe przy
otwarciu, a nie pustą oś. Reszta dokumentu (sekcje I–IV, VI–X) zostaje
pusta zgodnie z Twoim wzorem — steny w tabeli i wykresy są w pełni
edytowalne i przeliczają się automatycznie, tak jak w pozostałych dwóch
dokumentach (wpisz nowy sten → poziom, wykresy i „Wyniki w skrócie"
aktualizują się same). **Opis syntetyczny pod wykresami liczy się też sam
od razu przy otwarciu pliku** (nie jest zamrożony jak w pozostałych dwóch
dokumentach) — bardziej pasuje do charakteru „arkusza roboczego", który
zaczyna pusty i wypełnia się na żywo.

**Podział na strony — moja decyzja, nie z Twojego PDF-a.** Twój dokument
miał 7 stron płynących bez podziału A4. Pierwsza wersja tutaj też wyszła na
7 stron, ale str. 5 (Sekcja VII) i str. 6 (VIII.3 „Zakres i charakter
wsparcia") miały osobno sporo pustego miejsca u dołu. Na Twoją prośbę
przeniosłam VIII.3 na str. 5, razem z Sekcją VII i VIII.1–2 — żeby to się
zmieściło, ścieśniłam trochę tabelę ról (mniejsza czcionka/padding w
komórkach) i skróciłam 2 puste pola do wypełnienia w VIII.1/VIII.2 (były
nadmiarowo wysokie). Dokument skrócił się z 7 do **6 stron**, a str. 5
jest teraz gęsto, ładnie wypełniona (margines do stopki: 67 px, wcześniej
tam było 391 px pustego miejsca). Aktualny układ: **Str. 1** Sekcja I,
**Str. 2** Sekcje II+III+IV, **Str. 3** Sekcja V + wykresy, **Str. 4**
Sekcja VI, **Str. 5** Sekcja VII + VIII.1–3, **Str. 6** Sekcja VIII.4 +
IX + X.

**Ścieżka A/B — teraz realnie do zaznaczenia (str. 1).** Karty Ścieżki A i
Ścieżki B były na starcie samym opisowym tekstem — informowały, ale nie
dało się zaznaczyć, którą ścieżkę zespół faktycznie wybrał dla danego
ucznia. Dodałam pod spód przycisk radiowy (jak w pozostałych dwóch
dokumentach) i podświetlenie wybranej karty (pomarańczowa ramka i jasne
tło) — wybór jest jeden z dwóch (A **albo** B, nie oba naraz) i widać go
gołym okiem od razu na wydruku, nie tylko przy zaznaczonym kółku.

**Naprawiony błąd — 5 pustych pól do wypełnienia nie dawało się kliknąć
i wpisać tekstu.** Zauważyłaś to przy „Mocne strony" (VIII.2) i punkcie
pod nim; sprawdziłam cały dokument i ten sam błąd miały jeszcze 3 inne
puste pola: „Wyniki niewykonane / nieobserwowane" (str. 3), „Indywidualne
potrzeby rozwojowe" (VIII.1, tuż nad „Mocne strony") oraz oba pola w
VIII.4 „Przyczyny trudności" (str. 6). Wszystkie pięć wyglądały jak pola
do wypełnienia (jasnofioletowe tło, obramowanie), ale brakowało im atrybutu
`contenteditable`, więc kliknięcie i pisanie nic nie robiło — czysto
techniczne przeoczenie przy budowie tego dokumentu, teraz naprawione i
sprawdzone (wpisanie tekstu faktycznie działa) we wszystkich pięciu
miejscach. Instruktażowe notki (szare, kursywą, np. „Wpisz tylko
informacje potwierdzone...") celowo zostają nieedytowalne — to podpowiedzi
do czytania, nie pola do wypełnienia.

**Dodana klauzula RODO (na końcu, str. 6).** Twój wzór PDF w ogóle jej nie
miał — ani pełnej, ani skróconej. Dodałam dokładnie ten sam, jednoakapitowy
tekst, który jest już w pełnym dokumencie (Sekcja XXV): „Dane przetwarzane
są w celu realizacji zadań związanych z organizacją kształcenia specjalnego
i pomocy psychologiczno-pedagogicznej zgodnie z przepisami prawa oświatowego
oraz RODO." — na samym końcu strony 6, po „Podstawie odniesienia", tym
samym drobnym, szarym stylem `.legal`.

**Tabela „Współpraca z rodzicami" (Sekcja IX, str. 6) — rozszerzona o 2
nowe wiersze.** 4 istniejące wiersze były na sztywno ustalonymi typami
współpracy z Twojego wzoru (zawiadomienie o spotkaniu, informacje od
rodzica, forma konsultacji, przekazanie kopii WOPFU/IPET) — nie było
miejsca na nic więcej. Dodałam: **„Zgoda na przetwarzanie danych osobowych
(RODO)"** jako nazwany wiersz (data/sposób/osoba do wypełnienia, tak jak
reszta), oraz **całkiem pusty, w pełni edytowalny wiersz na końcu** —
zarówno nazwa ustalenia, jak i data/sposób/osoba są do wpisania, więc
zespół może dopisać dowolny inny rodzaj współpracy z rodzicem, którego
nie przewiduje żaden z 5 gotowych wierszy. Sprawdziłam klikiem i wpisaniem
tekstu, że oba pola pustego wiersza faktycznie działają.

**Wzór uzasadnienia na Punkcie Kontrolnym (Sekcja VII, str. 5) — nowy,
szary „ściągawkowy" box.** Blankiet obserwacji pogłębionej i pole „Wybór i
uzasadnienie" były zupełnie puste, bez podpowiedzi jak wygląda dobrze
napisane uzasadnienie. Dodałam między tabelą obserwacji a checkboxami
decyzji nowy komponent `.example-box` — jasnoszare tło, szara plakietka
„WZÓR UZASADNIENIA" — z przykładowym tekstem wskazującym na Poziom III
(ten sam, którego użyłam w analogicznym miejscu pełnego dokumentu):
„Na podstawie analizy zebranych danych wstępnych oraz KSzOF, Zespół
Specjalistów stwierdza, że uczeń w obszarach III, VII oraz IX funkcjonuje
na poziomie III wsparcia. (...)" — spójne z demo-danymi w tym samym
dokumencie (Sekcja V: obszary III, VII, IX rzeczywiście wychodzą na
Poziom III). To czysty wzór do naśladowania, nie pole do wypełnienia —
prawdziwe uzasadnienie zespół wpisuje osobno, w kolumnie „Wybór i
uzasadnienie" tabeli Decyzji. Żeby to się zmieściło, dociążyłam trochę
resztę strony (mniejsze pola VIII.1/VIII.2) — margines do stopki: 25 px.

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
**6 stron**.

Trzy karty pod checklistą chorób („Leki podawane w szkole", „Zalecenia
i przeciwwskazania", „Postępowanie w sytuacji nagłej") stały pionowo
jedna pod drugą — najpierw stanęły w jednym rzędzie obok siebie (siatka
3 kolumn), a na Twoją kolejną prośbę są teraz w układzie **„2+1"**: „Leki"
i „Zalecenia" obok siebie w jednym, węższym rzędzie (2 kolumny), a
„Postępowanie w sytuacji nagłej" osobno, w pełnej szerokości karty w
rzędzie pod spodem — bo to dłuższy, ważniejszy tekst (procedura na
wypadek nagłej sytuacji), który zasługuje na więcej miejsca niż wąska
1/3 karty. Treść bez zmian merytorycznych. Margines do stopki nadal
dodatni (81 px).

### Sekcja VII (Synteza funkcjonalna) przeprojektowana — była zbyt monotonna

Zwróciłaś uwagę, że strona z wykresami wygląda dobrze, ale Synteza
Funkcjonalna (dawna str. 6, teraz str. 5) — nie. Miała rację: to był
rząd identycznych, kremowych, przerywaną linią obramowanych karteczek,
bez koloru i bez wyraźnego podziału. Przeprojektowałam ją na 4 kolorowe
karty, po jednej na każdy z 4 punktów syntezy — kolor koduje charakter
punktu, spójnie z resztą dokumentu. Kolejność kart (na Twoją prośbę,
odgórnie w dół strony) to:

- **1 · Mocne strony, zainteresowania i uzdolnienia** — zielony (ten sam
  odcień, co Poziom I w tabeli KSzOF), siatka 2 kolumn.
- **2 · Indywidualne potrzeby rozwojowe i edukacyjne** — niebieski,
  siatka 2 kolumn.
- **3 · Przyczyny niepowodzeń, trudności, bariery i ograniczenia** —
  czerwony (ten sam odcień, co Poziom III), siatka 2 kolumn, **rozbite na
  3 osobne kategorie** (na Twoją prośbę): bariery komunikacyjne, bariery
  regulacyjne i bariery środowiskowe — wcześniej pierwsze dwie były
  połączone w jeden punkt „komunikacyjne i regulacyjne".
- **4 · Zakres i charakter wsparcia** — fiolet marki PCTP, lista ról
  (kto + co robi) zamiast checkboxów, bo to już ustalone zadania
  zespołu, nie opcje do zaznaczenia.

Karty pierwotnie stanęły w kolejności Indywidualne potrzeby → Mocne
strony → Zakres wsparcia → Przyczyny/bariery; obecna kolejność to wynik
dwóch kolejnych próśb (najpierw „Mocne strony" na samą górę i
„Indywidualne potrzeby" na drugie miejsce, potem „Przyczyny/bariery" na
trzecie). Każda karta zachowała swój oryginalny kolor i całą treść —
zmieniła się wyłącznie kolejność kart i numer na znaczniku (numeracja
zawsze odpowiada aktualnej pozycji na stronie, 1–4 od góry). Margines do
stopki nadal dodatni.

**Karta 4 („Zakres i charakter wsparcia") — opisy ról rozbudowane
Twoim dokładnym tekstem.** Wcześniej role miały bardzo skrócone,
hasłowe opisy (np. Psycholog: „redukcja lęku, interpretacja sygnałów
społecznych, wsparcie emocjonalne"); podmieniłam je na Twój pełny tekst
z pytania o ten sam zestaw 5 ról, więc opisy są teraz pełnymi zdaniami z
konkretami (np. Pedagog specjalny doszło „eliminowanie barier
środowiskowych", nazwa roli doprecyzowana na „Pedagog specjalny /
Nauczyciel współorganizujący"). Dodałam też podtytuł karty „(nauczyciele,
specjaliści, pomoc nauczyciela)" z Twojego tekstu. **Jedna rzecz do
sprawdzenia:** Twój tekst dla roli Psychologa zawiera dopisek „(w oparciu
o wyniki ToM)" — zostawiłam go dokładnie tak, jak podałaś, ale zwracam
uwagę, że to ten sam odnośnik do Testu Teorii Umysłu, który wcześniej
świadomie usunęłam z tej wersji dokumentu (patrz „Nowość: wersja «bez
obserwacji pogłębionej»" na górze), bo ToM jest narzędziem Modułu II,
którego ta wersja nie obejmuje. Zostawiłam go na Twoje wyraźne życzenie
(wkleiłaś pełny tekst), ale jeśli to przeoczenie z kopiowania z pełnego
dokumentu, daj znać, usunę dopisek tak jak poprzednio.

### Sekcja VIII (Współpraca z rodzicami) — doszedł podtytuł „Potwierdzenie zapoznania się z dokumentem"

Drobne dopełnienie struktury na Twoją prośbę (przesłałaś pełny tekst tej
sekcji do porównania) — data zawiadomienia rodziców i miejsce na podpis
rodzica miały już dokładnie tę treść, tylko bez własnego podtytułu nad
nimi; teraz mają, spójnie z pozostałymi dwoma podpunktami tej sekcji
(„Formy i harmonogram bieżącej współpracy", „Działania wspomagające w
środowisku domowym", które już tam były). **Do zaznaczenia:** Twój
wklejony tekst nazywa kolejną sekcję „SEKCJA X: Podpisy członków zespołu
specjalistów", a w tym dokumencie jest ona Sekcją IX — to nie pomyłka z
mojej strony, tylko konsekwencja wcześniejszej zmiany opisanej na górze
(„Usunęłam całą Sekcję VII" — usunięcie punktu kontrolnego pogłębionej
obserwacji z Twojego pierwotnego tekstu przesunęło całą resztę numeracji
o 1 w dół, więc Twoje „X" z oryginału odpowiada tu „IX"). Zostawiłam
numerację taką, jaka już jest w dokumencie, żeby nie rozjechała się z
resztą — treść i 5 ról podpisów zgadzają się z Twoim tekstem jeden do
jednego.

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
| **PUNKT KONTROLNY** — Decyzja zespołu | czerwony | str. 6, na początku strony | — (bramka) |
| **MODUŁ II** — Obserwacja pogłębiona | fiolet | str. 6, nad Sekcją VII | VII–XI |
| **CZĘŚĆ KOŃCOWA** — Planowanie wsparcia | fiolet | str. 8, nad Sekcją XII | XII–XXV |

„Punkt kontrolny" to nowa treść, nie tylko baner — dodałam pod nim 2
checkboxy („Uruchamiam moduł pogłębiony (Sekcje VII–XI)" / „Zamykam na
module I → Część Końcowa (Sekcja XII)"), bo Twoja mapa opisuje to jako
prawdziwą bramkę decyzyjną zespołu, nie tylko nagłówek. Kolor czerwony
(taki sam jak Poziom III w tabeli stenów) celowo odróżnia to jako moment
decyzji, a nie kolejny moduł.

Pod banerem doszła notka **„Rekomendowany poziom wsparcia"** — edytowalny
akapit uzasadniający decyzję zespołu (Twój dokładny tekst: obszary III,
VII i IX na poziomie III wsparcia → zespół zarządza obserwację pogłębioną
przy użyciu wskazanych narzędzi diagnostycznych), żeby bramka miała realne
uzasadnienie merytoryczne, a nie same puste checkboxy. Jeśli w konkretnym
przypadku zespół decyduje inaczej niż ten domyślny, wypełniony tekst —
treść jest w pełni edytowalna (`contenteditable`), można ją nadpisać albo
wyczyścić.

Pod tą notką doszła też tabelka **„Plan obserwacji pogłębionej — obszary
priorytetowe (Poziom III)"** (Twój dokładny tekst, 6 kolumn: Lp. / Obszar /
Cel obserwacji — Pytanie badawcze / Narzędzie — Metoda diagnozy /
Odpowiedzialni / Termin), po jednym wierszu na każdy z 3 obszarów Poziomu
III (III, VII, IX) — konkretny, przypisany do osób i terminu plan działania,
nie tylko nazwa obszaru. **Wiersz 3 (Obszar IX) uzupełniłam sama** — wklejony
tekst urwał się w połowie zdania („analiza środowiskow...") i bez osoby
odpowiedzialnej/terminu; dokończyłam „analiza środowiskowa", a jako
odpowiedzialnych wpisałam Pedagoga specjalnego i Psychologa (ci sami, co
w Zakresie wsparcia zajmują się lękiem/wycofaniem — pasuje do celu tego
wiersza) i „do 14 dni" (tak jak w wierszach 1–2). Sprawdź, czy to
dobrze oddaje Twoją intencję.

**Nowość:** pod checkboxami doszła krótka notka zamykająca obie ścieżki —
„Zamknięcie na module I" wprost mówi, że obserwacja kończy się tu i zespół
przechodzi od razu do Części Końcowej, a przy module pogłębionym jest
klikalny link **„Załącznik"**, który w HTML (i w większości czytników PDF)
przenosi bezpośrednio do nowego załącznika na str. 14–15 — nie trzeba
kartkować ręcznie.

**Punkt kontrolny dostał własną stronę (str. 6), oddzielną od Sekcji VI.**
Wcześniej tabela Sekcji VI, cały Punkt Kontrolny i początek Modułu II
(Sekcja VII) były upchnięte na jednej stronie — po dodaniu „Rekomendowanego
poziomu wsparcia" strona zaczęła się realnie nie mieścić (ujemny margines
do stopki). Zamiast dalej ściskać czcionkę, rozdzieliłam to na dwie strony:
str. 5 to teraz tylko Sekcja VI (i ma dzięki temu dużo więcej oddechu — patrz
niżej), a str. 6 to Punkt Kontrolny + Moduł II + Sekcja VII w komfortowym,
nieściśniętym rozmiarze czcionki. Dokument urósł z 14 do **15 stron**;
wszystkie odsyłacze do numerów stron dalej w dokumencie (Załącznik,
Sekcja XXV) zostały poprawione.

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
  (tabela mocne strony/trudności) — **teraz na własnej stronie, z
  rozbudowanymi opisami.** Wcześniej dzieliła stronę z Sekcją VII i miała
  krótkie, hasłowe opisy w komórkach; na Twoją prośbę („większe opisy w
  tabelce, żeby wypełniała całą stronę") rozwinęłam każdy z 18 opisów
  (9 obszarów × mocne strony/trudności) o dodatkowe, spójne z resztą
  profilu ucznia zdanie, i powiększyłam czcionkę/odstępy w komórkach
  (9,9px→11px, dopasowany padding) — tabela teraz realnie wypełnia stronę
  zamiast zostawiać duży pusty pas na dole.
- **Str. 6** — **Punkt Kontrolny** (banner + nowa notka „Rekomendowany
  poziom wsparcia" + 2 checkboxy decyzji + notka zamykająca, opisane wyżej
  w „Podział na etapy") i **Sekcja VII: Obserwacja pogłębiona — zachowania
  trudne (ABC/FBA) oraz PBS** — dawniej dzieliła stronę z Sekcją VI, teraz
  ma własną, pełnowymiarową stronę (patrz „Punkt kontrolny dostał własną
  stronę" wyżej). **Nowość:** na górze Sekcji VII, przed „Zachowanie
  kluczowe", jest prawdziwa **tabelka ABC** (Data / Poprzednik (A) /
  Zachowanie (B) / Konsekwencja (C)) — 2 przykładowe zdarzenia z obserwacji
  (te same, co w prototypie panelu nauczyciela z tej samej sesji, dla
  spójności). To dokładnie metoda, od której sekcja bierze nazwę —
  wcześniej był tylko jeden opisowy akapit „zachowanie kluczowe", teraz
  jest pod nim jako synteza tabeli powyżej.
- **Str. 7** — **Sekcja VIII: Poznanie społeczne (ToM)** (tabela 5
  komponentów — wniosek do pracy wypełniony tylko przy pierwszych dwóch,
  tak jak w Twoim pliku, reszta pusta do wypełnienia) i **Sekcja IX: Mowa
  i komunikacja** — połączone na jednej stronie, bo osobno zostawały w
  połowie puste. **Nowość:** Sekcja IX ma teraz tę samą tabelkę co ToM
  (Sposób porozumiewania się / Wynik 0–2 / Wniosek do pracy) zamiast
  checklisty — 6 sposobów porozumiewania się z Twojego pliku jako wiersze,
  wniosek logopedyczny przy „Mowa werbalna", reszta pusta do wypełnienia.
  Pod tabelą osobna karta „Kierunki terapii i zasady pracy w grupie" z
  resztą oryginalnego tekstu.
- **Str. 8** — **Sekcja X: Przetwarzanie sensoryczne (model Dunna)** —
  **też przebudowana na tabelkę w stylu ToM** (Układ zmysłowy / Wynik 0–2 /
  Wniosek do pracy): 5 układów zmysłowych, wniosek wypełniony przy
  „Słuchowy" i „Przedsionkowo-proprioceptywny" (dokładnie to, co było w
  Twoim opisie profilu), reszta pusta — plus niezmieniona 4-punktowa lista
  „Dieta sensoryczna i organizacja przestrzeni" pod tabelą. Dalej **Sekcja
  XI: Kontekst biopsychospołeczny (ICF) oraz dobrostan**
  (ułatwienia/bariery/dobrostan) — trzy sekcje razem na tej samej stronie,
  każda z nich osobno zostawiała najwięcej pustego miejsca ze wszystkich
  stron. **Na Twoją prośbę doszedł tu też podrozdział „Czynniki
  kontekstowe wg ICF"** — czynniki środowiskowe (wsparcie rodziny i
  otoczenia, postawy nauczycieli i rówieśników) i czynniki osobowe
  (temperament, motywacja) jako checklisty; przywrócone z historii gita
  (patrz sekcja na górze pliku).
- **Str. 9** — **Sekcja XII: Całościowy obraz funkcjonowania (synteza)**
  (tabela 8 obszarów, kolumna opisu pusta do wypełnienia — poprawiłam też
  literówkę „FUNKCELONOWANIA" → „FUNKCJONOWANIA" z tytułu w Twoim pliku).
- **Str. 10** — **Sekcja XIII: Przyczyny niepowodzeń i bariery** (4 krótkie
  notatki z Twoim tekstem) i **Sekcja XIV: Zakres i charakter wsparcia**
  (checklist 8 form wsparcia + doprecyzowanie organizacji).
- **Str. 11** — **Sekcja XV: Metody i formy pracy z uczniem** (5 metod
  wiodących z Twojego pliku, zaznaczone jako już stosowane — tak jak
  „PDF" obok każdej sugerowało w źródle, że to już ustalona treść, nie
  przykład do wyboru) i **Sekcja XVI: Dostosowanie wymagań i warunków
  pracy** (tabela 4 kanałów — **w pełni wypełniona Twoimi przykładami**,
  nie pusty szablon jak w poprzedniej wersji).
- **Str. 12** — **Sekcja XVII: Rekomendowane zajęcia specjalistyczne i
  rewalidacyjne**, **Sekcja XVIII: Zintegrowane działania nauczycieli i
  specjalistów**, **Sekcja XIX: Współpraca z rodzicami i międzysektorowa**,
  **Sekcja XX: Decyzja zespołu dotycząca poziomu wsparcia** i **Sekcja
  XXI: Cele SMART** (cel edukacyjny) — pięć sekcji na jednej stronie,
  wszystkie krótkie w Twoim pliku.
- **Str. 13** — dokończenie Sekcji XXI (cel terapeutyczny), **Sekcja XXII:
  Ocena efektywności udzielanego wsparcia** (tabela — Twój plik ma tu
  jeden zbiorczy wiersz „1–8", nie osobny wiersz na każdy zakres, więc tak
  to zostawiłam), **Sekcja XXIII: Przeniesienie informacji do IPET/PWES**
  (Twój jednozdaniowy opis „mostu transferowego", nie rozbudowana tabela
  jak w mojej poprzedniej wersji), **Sekcja XXIV: Podpisy** (5 podpisów —
  Twój plik łączy niektóre role, np. „Psycholog / Pedagog specjalny" w
  jednym podpisie) i **Sekcja XXV: Wykaz załączników, RODO i ważność
  dokumentu** (karta „Załączniki" wskazuje str. 14–15 jako miejsce
  zbiorczego zestawienia obserwacji pogłębionej; **na Twoją prośbę
  przywrócona pełna, 7-punktowa klauzula informacyjna RODO** —
  administrator, IOD, cel i podstawa prawna, kategorie danych, odbiorcy,
  okres przechowywania, prawa osób — w miejsce krótszego akapitu, plus
  osobna notka „Bezpieczeństwo i ważność dokumentu"; patrz sekcja na górze
  pliku).
- **Str. 14–15 — nowy Załącznik: „Zbiorcze zestawienie obserwacji
  pogłębionej"** (poza numeracją rzymską — to materiał pomocniczy, nie
  kolejna sekcja WOPF). Str. 14: intro + **A1** tabelka ABC (Sekcja VII),
  **A2** tabelka ToM (Sekcja VIII), **A3** tabelka Mowa (Sekcja IX) — te
  same tabele, co w głównym dokumencie, po prostu przedrukowane razem do
  szybkiego przeglądu. Str. 15: **A4** tabelka Profil sensoryczny (Sekcja
  X), potem „Zakres dostosowań i działań podjętych" (metody wiodące z
  Sekcji XV + tabela dostosowań z Sekcji XVI, też przedrukowane) i na
  końcu „Zalecenia do pracy — podsumowanie" — **to jedyny fragment
  załącznika, który jest moją syntezą**, nie przedrukiem: krótki akapit
  łączący kierunki pracy rozproszone po wnioskach w tabelach A1–A4.
  Dotyczy wyłącznie sytuacji, gdy zespół faktycznie uruchomił moduł
  pogłębiony — dlatego intro na str. 14 wprost to zaznacza.

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

- ~~Klauzula RODO (Sekcja XXV) — krótsza wersja, nie pełna 7-punktowa.~~
  **Zrobione.** Na Twoją wyraźną prośbę przywróciłam pełną, 7-punktową
  klauzulę z historii gita (teraz str. 13 — dokument urósł do 15 stron od
  czasu, gdy pisałam tę notatkę) — patrz sekcja na samej górze pliku.
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
