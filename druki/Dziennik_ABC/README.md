# Dziennik Obserwacji ABC oraz Arkusz Samooceny Obserwatora

Narzędzie do rejestrowania obserwacji zachowań trudnych metodą ABC
(Antecedent-Behaviour-Consequence) przez 3–4 tygodnie w różnych środowiskach
(lekcje, przerwy, świetlica), plus arkusz samooceny obserwatora sprawdzający
rzetelność przeprowadzonej obserwacji. Wspólna marka i konstrukcja z serii
`WOPF/`, `ToM/`, `Profil_biopsychospoleczny/`, `Profil_sensoryczny/`.

## Skąd ten druk

Przesłałaś `.docx` — „projekt Dziennika Obserwacji ABC oraz Arkusza
Samooceny Obserwatora" — wyekstrahowany w całości (python-docx + weryfikacja
wobec surowego OOXML) przed budową. Źródło zawierało 3 bloki: CZĘŚĆ 1
(rejestr ABC), CZĘŚĆ 2 (samoocena obserwatora) i „Podsumowanie jakościowe"
(wnioski do planu wsparcia) — bez metryczki i bez podpisów. Przebudowany na
wspólny system PCTP (`.page`/`.phead`/`.pmeta`/`.pbody`/`.pfoot`,
`base_css.html`), **2 strony**, zaprojektowane od razu tak, żeby obie karty
były dobrze wypełnione (bez dużych pustych obszarów na dole, jak w
poprzednich dwóch drukach tej serii, zanim to poprawiłam).

- **Str. 1** — Metryczka (I), Rejestr obserwacji funkcjonalnej ABC (II):
  cel i zasada obserwacji, ramka z przykładowymi antecedentami/zachowaniami/
  skutkami/interpretacjami (inspiracja do wypełniania, nie sztywna lista
  checkboxów), tabela dziennika — 9 wierszy do wypełniania na bieżąco przez
  cały okres obserwacji (z notką „skopiuj stronę, jeśli zabraknie wierszy").
- **Str. 2** — Arkusz samooceny i refleksji obserwatora (III): instrukcja
  skali 1–5, 6 kryteriów rzetelności obserwacji (dokładny tekst z Twojego
  pliku, łącznie z pogrubieniami — „zasobach i talentach", „rodzicami",
  „poziom wsparcia" — dokładnie tam, gdzie były w oryginale), ocena jako 5
  klikalnych kółek zamiast statycznych kwadracików z docx. Podsumowanie
  jakościowe (IV): 3 pola do wpisania (mocne strony / bariery środowiskowe /
  cel priorytetowy) + notka „Ważne" + podpisy.

## Co zmieniłam względem oryginału

- **Usunięte zerwane odnośniki/cytowania.** Oryginalny `.docx` miał
  porozrzucane w tekście i w komórkach tabel ciągi cyfr (np. „17171717",
  „19191919") oraz osobne akapity „+1"/„+2" — to artefakty narzędzia, które
  wygenerowało szkic (prawdopodobnie eksport z asystenta AI z przypisami),
  bez żadnego rzeczywistego przypisu w pliku (brak footnotes.xml/
  endnotes.xml w paczce docx — sprawdzone). Usunęłam je wszystkie jako
  szum, nie treść.
- **„IPE" → „IPET".** Oryginał dwukrotnie nazywał plan wsparcia „IPE" —
  ujednoliciłam do „IPET" (Indywidualny Program Edukacyjno-Terapeutyczny),
  tak jak w reszcie serii.
- **Dodana metryczka (Sekcja I) i podpisy na końcu** — oryginał nie miał ani
  jednego, ani drugiego (jedyne pole z datą to nagłówek kolumny „Data i
  Miejsce" w tabeli ABC). Dodane dla spójności z resztą serii, w której
  każdy dokument ma pasek „Dotyczy ucznia/Klasa/Data" i miejsce na podpisy
  na końcu — do potwierdzenia, czy to pasuje do sposobu, w jaki chcesz z
  tego korzystać.
- **Kwadraciki „□" z przykładów zamienione na listę tekstową** (nie
  osobne checkboxy w tabeli) — w oryginale każdy z ok. 20 przykładowych
  antecedentów/zachowań/skutków/interpretacji miał własny checkbox
  wewnątrz jednego wiersza „menu" tabeli. Zebrałam je w kompaktową ramkę
  nad tabelą dziennika (jak legenda), bo w praktyce obserwator i tak wpisuje
  do tabeli własnymi słowami, co się wydarzyło o konkretnej dacie —
  zaznaczanie 4 niezależnych checkboxów na wiersz nie odzwierciedlałoby
  jednego zdarzenia. Cała treść przykładów zachowana.

Jeszcze nie przeniesiony do `Zatwierdzone/` — czeka na Twoje potwierdzenie
punktów wyżej.
