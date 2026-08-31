# Kącik dyrektora — przedszkole · paczka do EduPlaner 2026

**Wersja 3.1.1 · rok szkolny 2026/2027 · 32 druki w 12 plikach · 91 stron A4 + 9-stronicowy spis**
**Trzy formaty: HTML interaktywny · PDF do druku · DOCX do edycji w Wordzie**

Komplet dokumentacji dyrektora przedszkola, zbudowany na tej samej zasadzie co
kącik nauczyciela: strona startowa ze spisem, potem druk po druku, każdy osobno.
Wszystko po polsku, format A4, marka PCTP (fiolet `#2D1B69`, pomarańcz
`#E8450A`, Arial).

---

## 1. Co jest w paczce

| Plik | Druki | Stron |
|---|---|---|
| `INDEKS_Kacik_Dyrektora.html` | strona startowa kącika (czego pilnować + kalendarz + matryca + lista druków + druki powiązane) | 9 |
| `Kacik_Dyrektora_Kalendarz_PCTP` | DK-1 — kalendarz roku z podziałem miesięcznym | 6 |
| `Kacik_Dyrektora_Plan_Pracy_PCTP` | DW-1 — plan pracy z wariantami placówek | 6 |
| `Kacik_Dyrektora_Nadzor_PCTP` | DN-1, DN-2, DN-3, DN-4, DN-5 | 14 |
| `Kacik_Dyrektora_Sprawozdanie_Nauczyciela_PPP` | D-1 | 9 |
| `Kacik_Dyrektora_Pomoc_PP_PCTP` | DP-1, DP-2, DP-3, DP-4 | 8 |
| `Kacik_Dyrektora_Organizacja_PCTP` | DO-1, DO-2, DO-3 | 6 |
| `Kacik_Dyrektora_Bezpieczenstwo_PCTP` | DB-1, DB-2, DB-3 | 6 |
| `Kacik_Dyrektora_Poradnia_Rodzice_PCTP` | DR-1, DR-2, DR-3 | 6 |
| `Kacik_Dyrektora_Rada_Pedagogiczna_PCTP` | RP-1, RP-2, RP-3, RP-4 | 10 |
| `Kacik_Dyrektora_Zmiany_2026_PCTP` | DZ-1, DZ-2, DZ-3 | 6 |
| `Kacik_Dyrektora_Rekrutacja_Ewaluacja_PCTP` | RE-1, EW-1, ZD-1 | 8 |
| `Kacik_Dyrektora_Program_Wychowawczy_PCTP` | PW-1 *(fakultatywny)* | 6 |

Każdy druk występuje w dwóch postaciach: **`.html`** (do podglądu w aplikacji)
i **`.pdf`** (gotowy wydruk). Pełne mapowanie sygnatura → plik → zakres stron
jest w `MANIFEST.json`.

---

## 2. Jak to osadzić w aplikacji

### Strona startowa
`INDEKS_Kacik_Dyrektora.html` to gotowy widok kącika (8 stron). Ma cztery
sekcje w kolejności, którą zamówiła autorka:

1. **Czego dyrektor musi pilnować** — osiem obszarów odpowiedzialności
2. **Kalendarz roku** — terminy z przepisu, każdy z sygnaturą druku
3. **Jaki dokument w jakiej sytuacji** — matryca sytuacja → sygnatury (2 strony)
4. **Lista druków** — karta na każdy druk z przyciskami *Otwórz PDF* / *Podgląd HTML* (4 strony)
5. **Druki z kącika nauczyciela, których potrzebuje dyrektor** — 9 pozycji z linkami do sąsiedniego katalogu, plus podstawa prawna zestawu

Linki w kartach są **względne** (`nazwa_pliku.pdf`), więc działają, jeśli
wszystkie pliki leżą w jednym katalogu. Przy innej strukturze podmień ścieżki
albo zbuduj listę z `MANIFEST.json`.

### Podgląd druku dla dyrektora
Otwórz plik `.html` — na górze jest **panel informacyjny** (co zawiera druk,
kiedy się go używa, terminy, na czym wykłada się kontrola) i przycisk **Drukuj**.
Panel ma `@media print { display: none }`, więc **nie trafia na wydruk** —
drukuje się wyłącznie sam formularz.

### Druk
```
format: A4
marginesy: brak
grafika tła: włączona
orientacja: pionowa
```
Bez włączonej grafiki tła znikną kolorowe nagłówki tabel i karty.

### Pliki są samowystarczalne
Zero zależności zewnętrznych: brak CDN, brak fontów z sieci, logo osadzone
jako inline SVG.

---

## 2a. Druki są interaktywne — co to znaczy dla integracji

Każdy plik `.html` z drukiem (spis nie, to nawigacja) ma na końcu, tuż przed
`</body>`, wstrzykniętą **warstwę interaktywną**: jeden blok `<style>`, jeden
`<div class="pasek">` i jeden `<script>`. Blok jest **identyczny we wszystkich
plikach** — przy zmianie podmieniasz go wszędzie jednym przebiegiem.

### Co staje się wypełnialne

| Element w druku | Zachowanie |
|---|---|
| `.linijki div` — kropkowane linijki w polach | `contenteditable`, wpisujesz tekst |
| `td.puste` — puste komórki tabel | `contenteditable`; kropki znikają po wpisaniu (klasa `wpisane`) |
| `.metryczka .wypelnij` — pola w nagłówku strony | `contenteditable` |
| `.wybor .dopisz` — dopiski po „(jakie):” | `contenteditable` |
| `.kwadrat`, `td.kratka span` — kwadraty i kratki | klik przełącza klasę `zazn` (pomarańczowe wypełnienie) |
| `td.ocena` — skale `0 1 2 3 4`, `TAK NIE`, `M Ś D` | każdy token opakowany w `<b>`; klik wybiera jeden, klik ponowny odznacza |
| `.podpis .kreska` — linia podpisu | **celowo nieedytowalna**, podpis odręczny |

W całym kąciku: **2818 pól do wpisywania, 292 kratki, 293 skale** — razem **3403**
aktywne pola. Rozbicie na pliki jest w `MANIFEST.json` w polu
`pliki.<plik>.pola_interaktywne`.

### Autozapis

`localStorage`, klucz `"pctp:" + document.title`, zapis **0,7 s po ostatniej
zmianie**. Struktura wartości:

```jsonc
{ "p": { "p12": "Przedszkole nr 7" },   // pola tekstowe wg data-pctp
  "k": [ "k3", "k7" ],                   // zaznaczone kratki
  "o": { "o5": "3" } }                   // wybrane wartości skal
```

Identyfikatory `data-pctp` nadawane są **kolejnością w DOM przy starcie**, więc
są stabilne dopóki nie zmienisz struktury druku. Po zmianie treści druku stare
zapisy mogą trafić w inne pola — przy istotnej zmianie warto podbić `document.title`
albo wyczyścić klucz.

Jeżeli w aplikacji chcesz **własny backend zamiast localStorage**, podmień dwie
funkcje w skrypcie: `zapisz()` i `wczytaj()`. Reszta zostaje bez zmian —
`zbierz()` zwraca gotowy obiekt do wysłania.

### Wydruk

Wpisana treść **drukuje się normalnie**. W `@media print` ukrywane są: pasek
narzędzi (`.pasek`) i podświetlenie aktywnego pola. Warstwa **nie zmienia
wysokości stron** — zweryfikowane porównaniem wysokości wszystkich sekcji
`.page` przed i po wstrzyknięciu (każda 1122,52 px = A4).

### Pasek narzędzi

Stała pozycja w prawym dolnym rogu: status z godziną zapisu, **Wyczyść**
(z potwierdzeniem, kasuje też klucz w localStorage) i **Drukuj**
(`window.print()`).

### Zero zależności

Bez bibliotek, bez CDN, bez fontów z sieci. Czysty ES5 w IIFE, działa
z pliku lokalnego (`file://`) i z serwera statycznego.

---

## 2b. Wersja Word (.docx) — podkatalog `word/`

Każdy plik z drukami ma odpowiednik `.docx` w podkatalogu **`word/`**, o tej
samej nazwie. Dwanaście plików, 336 KB razem.

| Format | Do czego | Gdzie |
|---|---|---|
| `.html` | podgląd w aplikacji **i wypełnianie w przeglądarce** z autozapisem | katalog główny |
| `.pdf` | gotowy wydruk, czysty blankiet A4 | katalog główny |
| `.docx` | **edycja i wypełnianie w Wordzie**, gdy ktoś woli edytor niż przeglądarkę | `word/` |

### Jak powstają

Jeden parser czyta HTML druku i zamienia go na strukturę pośrednią, jeden
generator (`docx` npm) buduje z niej dokument. Dzięki temu wszystkie dwanaście
plików wygląda tak samo i każda zmiana w HTML da się przenieść do Worda jednym
przebiegiem — nie ma ręcznie składanych dokumentów.

### Co zostało zachowane

- **marka**: fiolet `#2D1B69`, pomarańcz `#E8450A`, Arial, A4, marginesy 15 mm;
- **tabele**: wiersz nagłówkowy fioletowy z białym tekstem, oznaczony jako
  nagłówek (powtarza się przy podziale tabeli między strony), naprzemienne
  cieniowanie wierszy `#FAF7F2`, ramki `#D9CFEE`, **szerokości kolumn przeniesione
  z HTML** (podane w DXA na tabeli i na każdej komórce);
- **numeracja sekcji** w kolorowym kwadracie, pomarańczowym przy sekcjach
  oznaczonych `pom`;
- **bloki podstawy prawnej** jako ramka z pionowym paskiem w kolorze marki;
- **pola do wypełnienia** jako kropkowane linie — wpisuje się bezpośrednio
  w Wordzie;
- **kratki** jako znak `☐`, skale ocen jako tekst do obrysowania lub pogrubienia;
- **żywa pagina**: nagłówek z nazwą kącika, stopka `Strona X z Y`;
- **podział na strony** odpowiada wersji HTML i PDF — twardy podział w tych
  samych miejscach.

### Czego wersja Word nie ma

Nie ma warstwy interaktywnej z autozapisem — to funkcja przeglądarki. W Wordzie
wypełnia się bezpośrednio i zapisuje plik. Nie ma też panelu informacyjnego
z instrukcją; ta zostaje w wersji HTML.

### Regeneracja

```bash
python3 parsuj.py 'kacik-dyrektora/*.html'   # HTML -> druki.json
node gen.js word/                            # druki.json -> 12 plików .docx
```

### Weryfikacja, która przeszła

- walidacja XSD wszystkich dwunastu plików — bez błędów;
- kontrola kompletności treści wobec HTML: tytuły druków, nazwy sekcji,
  nagłówki kolumn, wiersze kluczowe, opcje wyboru i etykiety pól — **0 braków**;
- zgodność liczby podziałów stron z wersją HTML — zgodna we wszystkich plikach;
- szerokości kolumn każdej tabeli sumują się do szerokości kolumny tekstu.

---

## 3. Powiązania z kącikiem nauczyciela

Oba kąciki są jednym systemem — `MANIFEST.json` ma na to pole `powiazania`:

| Druk dyrektora | Powiązany druk nauczyciela |
|---|---|
| **D-1** — sprawozdanie z pomocy p-p | wypełnia **nauczyciel**; ostatnia strona (sekcje XV–XVII) należy do dyrektora |
| **DR-1** — wniosek poradni o opinię | samą opinię pisze nauczyciel na druku **O-2** |
| **DO-2** — kontrola dokumentacji | kontroluje dzienniki prowadzone na druku **Z-2** |
| **DP-4** — zbiorcza ocena efektywności | powstaje ze sprawozdań **D-1** i rejestru **DP-2** |
| **DN-2** — arkusz obserwacji zajęć | patrzy na zajęcia planowane drukami **R-2** i **KON** |

Jeżeli aplikacja pokazuje oba kąciki, warto zrobić z tych sygnatur linki
krzyżowe.

---

## 3a. Co doszło w wersji 2.0.0

| Nowość | Druk | Dlaczego |
|---|---|---|
| Podział miesięczny obowiązków, taki sam jak w checkliście nauczyciela K-1 | **DK-1** | dyrektor i nauczyciel patrzą na rok w tym samym układzie: zadanie, podstawa, termin, kratka, data wykonania |
| Plan nadzoru rozbudowany do 6 stron, z przepisem przy **każdym** elemencie | **DN-1** | § 23 ust. 2 i 3 rozporządzenia o nadzorze wymienia elementy planu wprost — każdy z nich ma teraz w druku własną podstawę |
| Pełna, ponumerowana lista **ośmiu kierunków polityki oświatowej 2026/2027** | **DN-1**, **DZ-3** | § 23 ust. 2 czyni je obowiązkową podstawą planu nadzoru |
| Sprawozdanie **semestralne** i **roczne**, oba rozliczające plan sekcja po sekcji | **DN-4**, **DN-5** | pierwsza tabela obu sprawozdań ma wiersze nazwane sekcjami planu DN-1 |
| Plan pracy przedszkola z wariantami: ogólnodostępne, z oddziałami integracyjnymi, integracyjne, specjalne | **DW-1** | limity liczebności oddziałów i zadania specyficzne różnią się między typami placówek |
| Protokół rady z **listą obecności i kworum**, harmonogram ośmiu zebrań obowiązkowych, wzór uchwały i rejestr | **RP-1**, **RP-2**, **RP-3** | art. 69–73 Prawa oświatowego; bez kworum uchwała jest nieważna |
| Karta zmian w statucie z terminami ustawowymi na rok 2026/2027 | **DZ-1** | ustawa z 3.07.2026 r. (Dz.U. 2026 poz. 1036) — statuty do 31.12.2026 r. |
| Plan wdrożenia nowej podstawy programowej z listą kontrolną na obserwację | **DZ-2** | Dz.U. 2026 poz. 378, zm. poz. 958 — obowiązuje od 1.09.2026 r. |

---

## 4. Stan prawny

Zestaw uwzględnia **cztery zmiany obowiązujące w roku szkolnym 2026/2027**:

- **Zakaz urządzeń elektronicznych — także w przedszkolach.** Ustawa z dnia
  3 lipca 2026 r. o zmianie ustawy — Prawo oświatowe (**Dz.U. 2026 poz. 1036**).
  Obowiązuje od **1 września 2026 r.**, statuty dostosowuje się **do 31 grudnia
  2026 r.** — to jedyny termin zapisany w ustawie wprost. Druki **DZ-1** i **RP-2**.
- **Nowa podstawa programowa wychowania przedszkolnego.** Rozp. ME z 11 marca
  2026 r. (**Dz.U. 2026 poz. 378**, zm. poz. 958): dziewięć obszarów, racjonalne
  usprawnienia, projektowanie uniwersalne. Druki **DZ-2**, **DW-1**, **DN-2**.
- **Ocena funkcjonalna.** Rozp. ME z 2 marca 2026 r. (**Dz.U. 2026 poz. 428**):
  opinia o funkcjonowaniu dziecka w **10 dni** od wniosku, z kopią dla rodziców.
  Druk **DR-1**.
- **Standardy ochrony małoletnich po nowelizacji.** Ustawa z 13 maja 2016 r.
  (t.j. Dz.U. 2024 poz. 560), zmieniona ustawą z 5 sierpnia 2025 r. — aktualizacja
  **do 15 sierpnia 2026 r.** Druki **DZ-1**, **DB-3**.

### Osiem kierunków polityki oświatowej państwa 2026/2027

Ustalone przez Ministra Edukacji na podstawie **art. 60 ust. 3 pkt 1** Prawa
oświatowego; **§ 23 ust. 2** rozporządzenia o nadzorze czyni je obowiązkową
podstawą planu nadzoru. Pełna lista jest w polu
`kierunki_polityki_oswiatowej_2026_2027` w `MANIFEST.json`, w sekcji II druku
**DN-1** i w druku **DZ-3**, gdzie każdy kierunek ma przypisane druki, w których
ma się pojawić.

### Terminy sztywne wpisane w druki

`MANIFEST.json` ma je maszynowo w polu `terminy_2026_2027`:
**15.08.2026** (standardy ochrony małoletnich) · **1.09.2026** (podstawa, zakaz
urządzeń, ocena funkcjonalna) · **15.09.2026** (plan nadzoru) · **31.12.2026**
(statut) · **30.04.2027** (MEN-I/74) · **31.08.2027** (wyniki i wnioski z nadzoru).
Poza nimi: **10 dni** na opinię dla poradni, **miesiąc** na skargę, **co najmniej
raz w roku** kontrola obiektu, **co najmniej dwa razy w roku** WOPFU.

Pełna lista podstaw prawnych: sekcja V indeksu oraz pole `podstawa_prawna`
w `MANIFEST.json`.

---

## 5. Czego paczka nie zastępuje

- **DB-2** nie zastępuje **protokołu powypadkowego** sporządzanego przez zespół
  powypadkowy według wzoru z załącznika do rozporządzenia MENiS.
- **DR-1** nie zastępuje **samej opinii** o funkcjonowaniu dziecka — to karta
  obiegu i terminu; opinię pisze nauczyciel na druku **O-2**.
- **DP-3** nie zastępuje **IPET** ani **WOPFU** — organizuje pracę zespołu,
  który je opracowuje.
- **DO-2** nie zastępuje **dzienników**, tylko je kontroluje.
- **DO-2** wskazuje na urzędowy wzór **MEN-I/74** — informacji o gotowości
  szkolnej nie da się zastąpić drukiem własnym.
- **DZ-1** nie zastępuje **statutu** — jest kartą zmian; statut przygotowuje
  i uchwala **rada pedagogiczna** (art. 72 ust. 1 Prawa oświatowego).
- **RP-3** nie zastępuje **regulaminu rady pedagogicznej** — ten rada ustala
  odrębnie (art. 73 ust. 2).

Zakres zgód w druku **DR-2** wymaga porównania ze statutem i procedurami
konkretnej placówki przed wdrożeniem.

---

## 6. Jak zmieniać druki

Źródłem jest **HTML**, PDF się z niego generuje:

```bash
chromium --headless --no-pdf-header-footer \
  --print-to-pdf=NAZWA.pdf NAZWA.html
```

Po każdej zmianie sprawdź, czy żadna strona się nie przelewa: liczba stron PDF
musi się zgadzać z liczbą sekcji `<section class="page">` w pliku HTML i z
wartością `stron` w `MANIFEST.json`.

Wspólne tokeny marki (kolory, ramki, odstępy) siedzą w bloku `:root` na górze
każdego pliku — zmiana tam przechodzi na cały druk.
