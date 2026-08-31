# Historyjka obrazkowa — pięć scen, trzy karty, narracja jej głosem

Historyjka to najbogatszy załącznik w banku: pięć ilustrowanych scen, trzy karty
A4 w gradacji trudności i nagrana narracja. Mają ją trzy konspekty — C1-01
„Jak rośnie kwiatek”, B1-01 „Zgubiony klucz”, C7-32 „Wieża Zosi”.

Rób ją, gdy konspekt prosi w pomocach o „karty historyjki obrazkowej”,
„historyjki społeczne”, „historyjki o skutkach” — czyli gdy sednem zajęć jest
opowiadanie i kolejność zdarzeń, a nie pojedynczy przedmiot.

## Gradacja poziomów

| poziom | obrazków | co pokazuje |
|---|---|---|
| III | 3 | problem i rozwiązanie |
| II | 4 | z przyczyną zdarzenia |
| I | 5 | pełny łuk narracyjny |

Sekwencje: III = sceny 1, 3, 5 · II = 1, 2, 3, 5 · I = wszystkie pięć. Ta sama
scena wraca na trzech kartach, więc trzymamy ją **raz, w klasie CSS**, a nie
w atrybucie `src` — inaczej ten sam obrazek trafiłby do pliku trzykrotnie.

## Kod

`src/zalaczniki_hist.py`, słownik `HISTORYJKI`. Nowa historyjka to nowy wpis
z prefiksem (`b1`, `c7`) plus wiersz w `DLA_KONSPEKTU`. Karta, pasek odsłuchu
i gradacja są wspólne — dopisujesz samą treść.

**Prefiksy są obowiązkowe.** W banku wszystkie historyjki siedzą w jednym
dokumencie, więc klasy scen (`.b1s1`) i identyfikatory nagrań (`b1au0`) muszą
się różnić między opowieściami. Bez prefiksu druga historyjka podmieniłaby
obrazki i dźwięki pierwszej.

Katalogi mediów: `assets/hist_<prefiks>/kadr_01..05.png` (640 px, po kadrowaniu)
oraz `assets/audio_<prefiks>/naracja_00_wstep.mp3`, `naracja_01..05.mp3`,
`naracja_06_pytania.mp3`.

## Historia

Pięć scen ma nieść pełny łuk: **stan wyjściowy → zdarzenie → trudność → działanie
→ rozwiązanie.** Scena trzecia jest zwykle tą trudną i to ona daje dziecku o czym
mówić; bez niej historyjka rozpada się na ilustracje.

Historia musi odpowiadać na pytania z przebiegu konspektu. B1-01 pyta „kto zgubił
klucz?” i „dlaczego miś był smutny?” — więc historyjka jest o zgubionym kluczyku
i o smutku, a nie o czymkolwiek innym z tej samej półki. C7-32 uczy schematu
przeprosin „zrobiłem – poczułeś – naprawię”, więc pięć scen układa się dokładnie
w ten schemat.

## Ilustracje

`creative_generate_image`, model `gemini-2.5-flash-image`, jedna scena na
wywołanie. Wspólny początek polecenia trzyma styl:

> Soft pastel children's storybook illustration in a gentle candy palette, thin
> warm brown outlines, rounded friendly shapes. Behind the scene a pale blue
> rounded blob and a soft green ellipse of grass under the characters; the rest of
> the page is plain white. No text, no letters, no numbers, no speech bubbles,
> no frame or border. Scene: `<opis sceny>`

**Bohater musi być opisany tak samo w każdej scenie**, z ubraniem włącznie:
„a small round brown teddy bear in a light blue jumper and a red scarf”. Przy
pierwszym podejściu do „Wieży Zosi” scena 1 wyszła w innych kolorach ubrań niż
pozostałe i trzeba było ją powtórzyć — czytelnik przestaje wtedy widzieć tę samą
parę dzieci.

Obróbka kadrów: przytnij do rysunku z marginesem ~4%, przeskaluj do 640 px
szerokości i skwantyzuj do 64 kolorów (`Image.quantize`). Oryginał zostaw obok
jako `hist_0N.png` — przyda się przy ponownym przeliczeniu.

## Narracja

Siedem ścieżek: wstęp (0), pięć scen (1–5), pytania otwarte na koniec (6).
Głos wyłącznie jej — `voice_id jq4ZUryuBeDqmtkKtBZ4`, model `eleven_v3`.
Rejestr i zasady pisania tekstu: `references/pomoce.md`.

Rozkład wskazówek w historyjce:

* wstęp i scena 1 — `[warmly, smiling, telling a story to a small child]`
* sceny środkowe — `[gently]`
* scena trudna — `[gently, a little sad]`, następna `[softly]`
* rozwiązanie i pytania — `[with a smile]`

Wstęp zapowiada zadanie („kiedy skończę, ułożysz obrazki po kolei”), a ostatnia
ścieżka zadaje **pytania otwarte**, nie sprawdza pamięci: „co poczuła Zosia, kiedy
wieża się rozsypała?”, „jak myślisz, co pomogło bardziej?”.

Czasy nagrań wpisz do `czasy` — z nich liczy się etykieta „narracja głosem
nauczycielki · X min” na pasku odsłuchu.

## Po dopisaniu

Historyjka wchodzi do banku i do zeszytu tej wersji wiekowej. Sprawdź pomiarem,
że wszystkie trzy karty mieszczą się na A4 (`zmierz_a4.mjs` — grupa `zal-siatka`),
i obejrzyj kartę poziomu I, bo ona ma najwięcej kafli.
