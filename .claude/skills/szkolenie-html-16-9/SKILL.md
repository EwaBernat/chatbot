---
name: szkolenie-html-16-9
description: >-
  Generator pięknych szkoleń i prezentacji jako JEDEN plik HTML 16:9 — slajdy na
  rzutnik, notatki trenera pod klawiszem N, przegląd slajdów, eksport do PDF (A4
  poziomo, 1 slajd = 1 strona). Użyj ZAWSZE, gdy użytkowniczka prosi o: szkolenie
  dla rady pedagogicznej lub kadry, prezentację, slajdy, deck, warsztat, webinar,
  „zrób szkolenie z tych materiałów", „prezentacja na 25 slajdów", „ładna grafika
  do szkolenia", kolejną część istniejącego cyklu szkoleniowego, wersję szkolenia
  dla innego etapu edukacyjnego (przedszkole, SP 1–3, SP 4–8, szkoła średnia),
  albo gdy wgrywa materiał źródłowy (PDF, Word, skan, program terapeutyczny) i
  chce z niego zrobić szkolenie dla nauczycieli, terapeutów lub rodziców.
  Wyzwalaj też przy: „szkolenie na radę", „materiał na szkolenie", „slajdy do
  wydruku", „prezentacja z notatkami dla prowadzącego", „część II tego szkolenia".
  NIE używaj, gdy użytkowniczka wyraźnie chce plik .pptx do edycji w PowerPoincie
  (wtedy skill pptx) ani gdy prosi o ulotkę, broszurę lub dokument Word.
---

# Szkolenie HTML 16:9

Produkt: **jeden samodzielny plik HTML**, który otwiera się dwuklikiem, działa
offline (poza pobraniem krojów pisma) i jednocześnie jest: prezentacją na
rzutnik, skryptem dla prowadzącego i materiałem do wydruku.

Dlaczego HTML, a nie PowerPoint: jeden plik bez zależności, identyczny układ na
każdym komputerze, notatki trenera schowane pod klawiszem, eksport do PDF jednym
klawiszem i publikacja jako artifact do wysłania radzie pedagogicznej.

## Proces

### 1. Przeczytaj materiał źródłowy w całości, zanim zaczniesz projektować

Jeśli użytkowniczka wgrała plik, jest to najważniejszy wkład — nie streszczaj go
z pamięci ogólnej wiedzy, tylko go otwórz.

- PDF ze skanem (brak warstwy tekstowej, `pdftotext` zwraca pustkę): zainstaluj
  `poppler-utils`, a potem czytaj narzędziem Read po 10 stron naraz — strony
  wracają jako obrazy i widzisz układ, kolory i ilustracje.
- Z materiału wynotuj: **terminologię** (nazwy etapów, procedur, technik),
  **nazwy własne** (bohaterowie historyjek, autorzy metod), **paletę i motyw
  graficzny**, **liczby** (ile etapów, ile minut, jakie progi).

### 2. Przejmij identyfikację wizualną źródła zamiast wymyślać własną

Jeśli materiał ma swój świat wizualny (kolor, motyw, metaforę), szkolenie ma
wyglądać jak jego kontynuacja — wtedy kadra od razu widzi, że to jedna rodzina
materiałów. Przenieś: paletę wiodącą, motyw graficzny (u „Budowania mostów
społecznych" są to tory i most), krój o podobnym charakterze, metaforę przewodnią.

Gdy materiału nie ma, dobierz paletę do tematu: jeden kolor wiodący + neutralne
tło z lekkim odchyleniem w stronę tego koloru + kolory semantyczne (zielony
„rób tak", czerwony „nie rób", bursztyn „uwaga"). Kolory semantyczne to nie
akcenty dekoracyjne — niosą znaczenie i nie zmieniają się między slajdami.

### 3. Zaprojektuj strukturę, zanim napiszesz pierwszy slajd

Domyślnie 25 slajdów w 4 modułach — tyle mieści się w 90 minutach rady
pedagogicznej. Sprawdzony układ:

| Część | Slajdy | Rola |
|---|---|---|
| Wprowadzenie | 1–2 | okładka + mapa szkolenia z zakresami slajdów |
| Moduł I | 3–8 | fundament: czym to jest, jak się rozwija, dlaczego ważne |
| Moduł II | 9–13 | rozpoznanie: sygnały, grupy ryzyka, mity, zmiana perspektywy |
| Moduł III | 14–21 | narzędzia: procedura krok po kroku, gotowe zdania, wyposażenie |
| Moduł IV | 22–25 | wdrożenie: własny materiał, pułapki, rodzice, plan na 30 dni |

Na slajdzie 2 poproś uczestników, żeby pomyśleli o jednym konkretnym dziecku —
na ostatnim slajdzie budują dla niego plan. To spina szkolenie klamrą i zamienia
bierne słuchanie w pracę.

### 4. Pisz slajdy tak, jak mówi praktyk, nie jak pisze podręcznik

- **Nagłówek to teza, nie etykieta.** Nie „Rozwój teorii umysłu", tylko „Jak
  teoria umysłu rozwija się wiekowo" albo „Bez teorii umysłu nie działa nic, co
  nazywamy umiejętnościami społecznymi".
- **Jedna myśl na slajd.** Jeśli slajd potrzebuje dwóch nagłówków, to są dwa slajdy.
- **Dawaj gotowe zdania do wypowiedzenia**, nie zalecenia. Zamiast „stosuj język
  mentalny" → tabela „zamiast: «Przeproś Kubę» → powiedz: «Kuba myślał, że wieża
  zostanie. Teraz jest smutny»". To jest to, co kadra wynosi ze szkolenia.
- **Kolumna „co widzi nauczyciel" obok „co dzieje się w dziecku"** przesuwa
  perspektywę mocniej niż akapit o empatii.
- Nie przepisuj list z materiału źródłowego jeden do jednego — przekładaj je na
  sytuacje z sali, bo szkolenie ma być użyteczne w poniedziałek rano.
- Unikaj emoji jako ikon; rysunek wektorowy albo typografia wyglądają poważniej.

### 5. Notatki trenera są obowiązkowe

To one zamieniają slajdy w szkolenie, które może poprowadzić ktoś inny. W
`data-notes` każdego slajdu napisz: co powiedzieć własnymi słowami, gdzie się
zatrzymać, jakie pytanie zadać sali, co pokazać na żywo. 2–4 zdania.

Uwaga techniczna, która potrafi zepsuć cały slajd: `data-notes` to atrybut HTML
w cudzysłowach, więc **nie wolno w nim użyć znaku `"`** (ani surowego `>`).
Dozwolone jest `<b>...</b>` do wyróżnień. Cudzysłów w środku urwie atrybut, a
parser połknie klasy następnych elementów — slajd rozsypie się w niepozorny
sposób (np. nagłówek straci styl). Cytaty w notatkach zapisuj jako „…" albo
bez cudzysłowu.

### 6. Zbuduj plik z szablonu

Skopiuj `assets/szablon.html` do katalogu docelowego i wypełnij. Szablon zawiera
kompletny system: tokeny kolorów, typografię, komponenty, nawigację klawiaturą,
przegląd slajdów, notatki, tryb druku. Gotowe komponenty z przykładami do
wklejenia znajdziesz w `references/komponenty.md` — zajrzyj tam przy pisaniu
slajdów, zamiast wymyślać własne klasy.

Plik pisz **bez** `<!doctype>`, `<html>`, `<head>` i `<body>` — dzięki temu ten
sam plik działa lokalnie w przeglądarce i nadaje się do publikacji jako artifact.

### 7. Sprawdź, zanim oddasz

```bash
bash scripts/zmierz_slajdy.sh sciezka/do/prezentacji.html
```

Skrypt mierzy, gdzie kończy się treść każdego slajdu (slajd ma 720 px). Popraw
wszystko oznaczone jako PRZEPEŁNIENIE — na rzutniku wygląda to na ucięty slajd.
Slajdy oznaczone „pusto" albo dogęść treścią, albo zwiększ skalę, dodając im
klasę `big`.

Potem obejrzyj kilka slajdów naprawdę — zrzut ekranu z przeglądarki wyłapie to,
czego liczby nie pokażą (nachodzące elementy, zły kontrast, nieczytelną grafikę):

```bash
CH=/opt/pw-browsers/chromium-*/chrome-linux/chrome
$CH --headless=new --no-sandbox --window-size=1400,860 --virtual-time-budget=4500 \
    --screenshot=slajd8.png "file:///pelna/sciezka/prezentacja.html#s8"
```

Obejrzyj co najmniej: okładkę, slajd z ilustracją i slajd najgęstszy.

### 8. Oddaj w trzech formach

1. **Artifact** — link do wysłania radzie (publikuj plik przez narzędzie Artifact).
2. **Plik** — wyślij użytkowniczce przez SendUserFile, bo chce mieć go u siebie.
3. **Repozytorium** — commit na wskazanej gałęzi + krótki README z klawiszami i
   spisem modułów.

W odpowiedzi napisz: co wzięłaś z jej materiału, co dodałaś od siebie i które
slajdy warto wydrukować dla uczestników.

## Cykl szkoleń

Gdy powstaje kolejna część (inny etap edukacyjny, dalszy ciąg programu):

- zachowaj identyfikację, siatkę i komponenty — zmienia się treść, nie system;
- w podtytule i na mapie oznacz część („Część II · SP 1–3"), żeby materiały
  układały się w serię;
- powtórz to, co jest wspólne, w skróconej formie (jeden slajd przypomnienia),
  a nie w pełnej — uczestnicy części II zwykle byli na części I, ale nie wszyscy;
- zmień przykłady na właściwe dla etapu: w przedszkolu kukiełki i szatnia, w SP
  1–3 przezwiska, zeszyt, praca w grupach, świetlica.

## Częste błędy

- Cudzysłów w `data-notes` — najczęstsza przyczyna „dziwnie wyglądającego" slajdu.
- Slajd-lista: siedem punktów pod sobą. Rozbij na karty albo tabelę porównawczą.
- Ilustracja rysowana „na siłę": jeśli rysunek nie pokazuje mechanizmu, lepiej
  dać dobrą typografię. Rysuj tam, gdzie obraz tłumaczy coś szybciej niż zdanie
  (procedura, komiks z testem, skala, przepływ).
- Zbyt drobna czcionka w kartach — to ma być czytelne z ostatniego rzędu sali.
  Poniżej 14 px schodzą tylko przypisy.
- Polskie znaki: wybieraj kroje z Google Fonts mające zestaw latin-ext
  (Figtree, Source Sans 3, Lora są sprawdzone).
