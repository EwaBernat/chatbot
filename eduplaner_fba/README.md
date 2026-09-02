# Druk FBA-C — cele SMART do obserwacji pogłębionej

Ciąg dalszy karty **ABC / FBA** (analiza funkcjonalna zachowania i pozytywne
wsparcie — PBS). Tamta kończy się pięcioma celami SMART, po jednym na funkcję
zachowania. Wyznaczają kierunek planu, ale na obserwację pogłębioną są za
szerokie: „skorzysta z ustalonej strategii wyciszenia” nie mówi, w której
z pięciu sytuacji napięcia liczymy postęp.

Ten druk rozpisuje tamte pięć celów na **25 celów szczegółowych** — po jednym
do każdego wskaźnika kwestionariusza funkcji. Każdy ma zachowanie, które widać,
liczbę, którą da się policzyć, i termin, w którym sprawdzamy. Osiem stron A4
pionowo: wprowadzenie · pięć stron z kartami celów · dwie strony tabeli ewaluacji.

## Składanie dokumentu

```bash
# formularz bez nazwiska (to jest wersja w repozytorium)
python3 src/build_cele_fba.py

# pod konkretnego ucznia — punktacja pięciu funkcji z kwestionariusza
python3 src/build_cele_fba.py --uczen "Imię Nazwisko" --klasa "III A" \
    --wyniki 7,8,13,7,13

# pomiar: czy każda strona mieści się na jednej kartce A4
node src/zmierz_strony.mjs Cele_SMART_FBA_obserwacja_poglebiona.html
```

Dokumenty z nazwiskiem nie wchodzą do repozytorium (`.gitignore`) — noszą dane
osobowe ucznia. Zostaje sam formularz.

## Druk FBA-T — tabela wiek × poziom wsparcia

Ten sam materiał ułożony tak, jak układa go bank celów SMART KPOF: zakładki
wersji wiekowych, wiersz na wskaźnik, trzy kolumny poziomów wsparcia.
**225 celów** (25 wskaźników × 3 poziomy × 3 wersje) — nauczyciel wybiera
komórkę, zamiast przepisywać cel pod dziecko.

```bash
python3 src/build_tabela.py     # Tabela_celow_FBA_wiek_poziom.html
node src/do_pdf.mjs             # oba druki do PDF: FBA-C pionowo, FBA-T poziomo
```

| wersja | wiek | czym się różni |
|---|---|---|
| A | 3–4 lata | symbol podany do ręki, krótkie czasy, proste zachowanie |
| B | 5 lat | karta na stoliku plus słowo, czasy średnie |
| C | 6 lat | słowo zamiast karty, nazywanie własnego stanu, planowanie |

Poziom wsparcia zmienia **warunki zadania**, nie funkcję zachowania: Poziom III —
podpora dorosłego, 3 z 5 sytuacji, 4 tygodnie; Poziom II — pomoc w zasięgu,
4 z 5, 8 tygodni; Poziom I — bez pomocy przedmiotowej i z trudniejszym
zachowaniem, 4 z 5, 12 tygodni. Kryterium na Poziomie I nie rośnie do 5 z 5:
„za każdym razem” to w przedszkolu cel nie do osiągnięcia i psuje ewaluację,
zamiast ją domykać.

### 75 konspektów zajęć

Każdy wskaźnik w każdej wersji wiekowej ma konspekt we wzorze druku **KC-3**
z banku KPOF — **25 × 3 = 75 scenariuszy**. Sekcje I–VII, cel terapeutyczny
z rozpisaniem SMART, pomoce, metody, tabela przebiegu w parach N/D, trzy
modyfikacje w kolorach oceny, wskazówka dla prowadzącego i materiał do wydruku.

Jeden konspekt obsługuje **trzy poziomy wsparcia**: poziom zmienia sekcję VI
(modyfikacje), a nie scenariusz. Konspekt otwiera się **kliknięciem celu**
w tabeli — wtedy pokazuje cel z klikniętej komórki i wyróżnia ten poziom —
albo z **wykazu konspektów** nad tabelą, i wtedy pokazuje wszystkie trzy cele
naraz. Cel edukacyjny czyta się **na żywo z tabeli**: po poprawce w
`dane_poziomy.py` konspekt nie zaczyna żyć własną wersją celu.

Treść leży w pięciu modułach po jednym na funkcję (`konspekty_fba_1.py` … `_5.py`);
`konspekty_fba.py` je scala i dokłada to, co wynika z wieku i z tabeli. Rdzeń
konspektu (tytuł, ICF, punkty podstawy, metody, wskazówka, materiał) jest wspólny
dla trzech wersji wiekowych; wariant wiekowy niesie cel terapeutyczny, przebieg
i pomoc charakterystyczną dla wieku.

### 25 pomocy dydaktycznych i 75 poleceń jej głosem

Każdy wskaźnik ma **pomoc dydaktyczną** w sekcji VII konspektu — druk **KC-4**:
zdjęcie poglądowe pomocy, lista „co przygotować”, trzy kroki użycia i wskazówka.
Zdjęcia (`assets/pomoce_fba/k_<kod>.jpg`) rysuje model `gemini-2.5-flash-image`
w tej samej pastelowej konwencji co ilustracje w banku KPOF; obrazek z tekstem
odrzucamy i generujemy od nowa, bo napis na pomocy dla trzylatka nic nie znaczy.

Do każdej pomocy w każdej wersji wiekowej idzie **nagrane polecenie dla dziecka**
— 75 nagrań jej głosem (`assets/audio_fba/<wersja><kod>.mp3`), przycisk ▶ przy
tekście polecenia w sekcji VII. Nagrywa się je modelem `eleven_v3` w jej
sklonowanym głosie (`voice_id` w `CLAUDE.md`), w rejestrze
`[warmly, smiling, telling a story to a small child]` i **czystą prozą**.
Tekst nagrania to zawsze polecenie **do dziecka**, w drugiej osobie — nie
instrukcja dla nauczyciela; to, co ma zrobić dorosły, siedzi w trzech krokach obok.

Nagrania z ElevenLabs kompresujemy do 40 kbps mono, a oryginał zostaje jako
`*.orig.mp3` (poza repozytorium — nagranie głosu to dana biometryczna):

```bash
python3 src/kompresuj_fba.py        # PNG → k_*.jpg, MP3 → 40 kbps mono
python3 -c "import sys;sys.path.insert(0,'src');import karta_pomocy as K;print(K.braki())"
```

`braki()` zwraca listę pomocy bez zdjęcia i poleceń bez nagrania. Karta bez
któregoś z nich nie psuje budowania — dostaje pole zastępcze i wyłączony przycisk,
więc dokument składa się poprawnie na każdym etapie kompletowania mediów.

Konspekty drukują się pionowo, mimo że tabela wokół nich jest pozioma
(`@page kon`): scenariusz na jednej kartce, materiał do wydruku na drugiej.
Przycisk w wykazie drukuje **cały zeszyt jednej wersji** — 25 konspektów,
50 stron. Karty w materiale mają puste pola na symbole: symbol bierze się
z biblioteki EduPlaner, żeby dziecko widziało ten sam obrazek tu, na tablicy
AAC i w planie dnia.

```bash
node src/zmierz_konspekty.mjs   # czy każdy konspekt mieści się na jednej kartce
```

### Własne konspekty nauczycielki

Bank ma 75 gotowych scenariuszy, ale każde dziecko jest inne i prędzej czy
później trzeba napisać własny. Przy **każdej komórce z celem** jest **+**, który
otwiera formularz o dokładnie takiej samej strukturze co konspekt gotowy
(I cel · II pomoce · III metody · IV–V realizacja · przebieg N/D · VI modyfikacje
· wskazówka). Zapisany scenariusz otwiera się i drukuje tak samo — ta sama karta,
ten sam druk KC-3 A4. Nad tabelą jest panel **Moje konspekty** z listą własnych
scenariuszy tej wersji wiekowej.

Oba okna — formularz i podgląd — mają **krzyżyk w prawym górnym rogu**, w tym
samym miejscu co konspekt gotowy. Krzyżyk formularza pyta, zanim zamknie: Escape
i kliknięcie w tło celowo **nie** zamykają edytora, bo nie mogą skasować
niezapisanej pracy jednym przypadkowym ruchem.

Trzy rzeczy, które ten edytor trzyma inaczej niż zwykły formularz:

* **Zachowanie zastępcze ma własne pole** i bez niego konspekt się nie zapisze.
  To ono jest treścią planu PBS: uczymy innej drogi do tej samej funkcji, nie
  odbieramy dziecku funkcji. Pole wchodzi wypełnione brzmieniem z wiersza tabeli.
* **Cel edukacyjny czyta się na żywo z tabeli**, nie kopiuje do rekordu — po
  poprawce w `dane_poziomy.py` własny konspekt nie zaczyna żyć nieaktualną
  wersją celu. Zmiana poziomu w formularzu od razu pokazuje cel z tej kolumny.
* **Sekcja VII ma trzy warianty karty pomocy** — gotową, własną albo żadną,
  niezależnie od materiału do wycięcia. Karta **gotowa** i arkusz klonują się
  z konspektu tego samego wskaźnika: kopiujemy węzeł dokumentu, nie media do
  `localStorage`, bo dziecko ma słyszeć **to samo** polecenie i widzieć **ten
  sam** symbol, co przy scenariuszu gotowym. Karta **własna** to pełny druk KC-4
  pisany od zera: nazwa, co przygotować, trzy kroki, wskazówka, polecenie dla
  dziecka, **własne zdjęcie** i **własne nagranie**.

Zdjęcie własnej pomocy wgrywa się z dysku i **zmniejsza w przeglądarce** do 900 px
(JPEG, jakość 0.82) — tyle samo, ile mają zdjęcia pomocy gotowych. Bez tego jedno
zdjęcie z telefonu zajęłoby cały magazyn przeglądarki. Nagranie przyjmujemy do
600 kB (MP3, M4A, WAV, OGG); nagranie z ElevenLabs jej głosem waży około 30 kB.
Panel pokazuje, ile miejsca zajmują konspekty, a gdy magazyn się skończy, komunikat
mówi wprost, co zrobić: zapisz kopię JSON i usuń zdjęcie albo nagranie. Przełączenie
karty na gotową **nie kasuje** wgranego zdjęcia i nagrania — miejsce zwalnia się
przyciskiem „Usuń", świadomie.

Dane leżą w `localStorage` pod kluczem `moje_konspekty_fba.KLUCZ` — **innym niż
klucz banku KPOF**, żeby dwa zbiory się nie mieszały; przy wczytywaniu kopii
pozycje spoza tego druku są pomijane i zliczane w komunikacie. To jedyny magazyn,
jaki ma dokument otwierany z dysku, więc panel ma **zapis kopii do pliku JSON
i wczytanie jej z powrotem** i mówi wprost, że bez tego konspekty nie przejdą na
inny komputer. Gdy przeglądarka blokuje `localStorage`, edytor działa dalej
w pamięci karty i pokazuje ostrzeżenie.

Własny scenariusz mieści się na jednej kartce A4 do ośmiu długich kroków
przebiegu (pomiar: 1043 px przy budżecie 1091). Dłuższy przechodzi na drugą
stronę — nic się nie psuje, ale warto o tym wiedzieć przed drukiem.

Tabela drukuje się **poziomo** i drukuje się ta wersja wiekowa, która jest
otwarta — tak jak bank. Pas z nazwą wersji siedzi w `thead`, więc powtarza się
na każdej kartce; bez niego druga i trzecia strona nie mówiły, czyj to rocznik.

## Skąd kryterium i horyzont

Nie z podręcznika, tylko z punktacji funkcji u tego ucznia — tak samo jak
w banku celów SMART horyzont wynika z poziomu wsparcia:

| punktacja | ocena | kryterium | horyzont |
|---|---|---|---|
| 10–15 | dominująca | 8 z 10 sytuacji | 4 tygodnie |
| 5–9 | istotna | 7 z 10 sytuacji | 8 tygodni |
| 0–4 | słaba | 6 z 10 sytuacji | 12 tygodni |

Funkcja dominująca dostaje najkrótszy horyzont nie dlatego, że jest łatwiejsza,
tylko dlatego, że jest priorytetem planu — sprawdzamy ją najczęściej.

Horyzont trzymamy w trzech formach gramatycznych (`4 tygodni` · `4 tygodniach`
· `4 tygodnie`), bo wchodzi w trzy różne zdania. Jedna forma dawała
„weryfikacja po 4 tygodni” w druku, który idzie do rodzica.

## Co gdzie leży

```
src/dane_fba.py         25 celów SMART do obserwacji pogłębionej (druk FBA-C)
src/dane_poziomy.py     225 celów: wiek × poziom wsparcia (druk FBA-T)
src/build_cele_fba.py   składanie druku FBA-C
src/build_tabela.py     składanie druku FBA-T
src/konspekty_fba.py    scalanie konspektów: rdzeń + wariant wiekowy + tabela
src/konspekty_fba_1..5.py  treść konspektów, moduł na funkcję zachowania
src/konspekt_fba.py     renderowanie konspektu i wykazu (wzór KC-3)
src/pomoce_fba.py       25 pomocy dydaktycznych i 75 poleceń dla dziecka
src/karta_pomocy.py     renderowanie karty pomocy z nagraniem (wzór KC-4)
src/symbole_fba.py      mapowanie kart i pasków na bibliotekę symboli EduPlaner
src/kompresuj_fba.py    kompresja zdjęć pomocy i nagrań
src/logo.py             logo PCTP w nagłówkach druków
src/moje_konspekty_fba.py  edytor własnych konspektów nauczycielki
src/zmierz_konspekty.mjs   pomiar wysokości druku wszystkich 75 konspektów
src/zmierz_strony.mjs   pomiar, czy strony mieszczą się na A4
src/do_pdf.mjs          wydruk obu druków do PDF
```

Cele mówią o **zachowaniu zastępczym** — pełniącym tę samą funkcję co zachowanie
trudne, tylko akceptowalnym. Nie odbieramy uczniowi funkcji (ucieczki, uwagi,
regulacji), uczymy innej drogi do niej. To odróżnia plan PBS od karania reakcji
i o to samo trzeba dbać przy każdym dopisywanym celu.
