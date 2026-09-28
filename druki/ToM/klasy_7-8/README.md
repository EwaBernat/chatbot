# ToM — Karta oceny Teorii Umysłu — klasy VII–VIII

Arkusz obserwacji Teorii Umysłu (ToM) dla klas VII–VIII szkoły podstawowej,
ekosystem **EduPlaner2026-MJ-PCTP**. Ta sama seria co `klasy_1-3/` i
`klasy_4-6/` — wspólna marka, wspólny układ, treść dopasowana do wieku.

## Pliki

| Plik | Opis |
|---|---|
| `ToM_karta_oceny.html` | źródło — przebudowane z oryginału 11-stronicowego na wzór klasy 1-3 (patrz niżej) |
| `ToM_karta_oceny.pdf` | wydruk wygenerowany z powyższego HTML (headless Chromium, druk A4) |

## Status: 7 stron (było 11) — dokładnie tyle, co klasa 1-3

Autorka przysłała świeży, oryginalny 11-stronicowy plik
(`EduPlaner2026_ToM_szkola_klasy_7_8.html`) i poprosiła o dokładnie taką
samą przebudowę, jaką klasa 4-6 przeszła krok po kroku w tej samej sesji —
tu zrobioną od razu w całości, na bazie już gotowego, sprawdzonego pliku
klasy 4-6 jako szablonu konstrukcji, z podmienioną wyłącznie treścią
klasy 7-8 (komponenty, 25 pozycji obserwacji, ICF, wykres, tabele).

**Żaden tekst kliniczny nie został zmieniony ani skrócony** — wszystkie 25
pozycji obserwacji, kody ICF, opisy „Aktualny poziom funkcjonowania",
„Zalecenia do pracy" i „Cel SMART" dla 5 komponentów (Subtelne stany
umysłu i empatia poznawcza, Perspektywa społeczna i decentracja w sporze,
Sarkazm, aluzja i podtekst społeczny, Mentalizowanie wyższego rzędu i
atrybucje, Faux pas, reputacja i ocena intencji) są przepisane słowo w
słowo z oryginału.

**Usunięte w całości** (nie ma tego wcale we wzorze klasy 1-3, tak samo jak
w klasie 4-6):
- cały cykl re-ewaluacji — tabele „Postęp wg komponentów", „Wnioski i
  decyzja", „Nowe zalecenia po ewaluacji" (dawne str. 9–10),
- sekcja „Synchronizacja druków — przeniesienie wyników" z WOPF (dawne
  str. 10–11),
- tabela „Poziom rozwoju Teorii umysłu — norma rozwojowa a obecne
  funkcjonowanie" (klasa 1-3 nie ma takiej tabeli),
- osobne opisowe akapity „Zalecenia do pracy" dla każdego komponentu jako
  własne strony — **ale nie stracone na dobre**: przeniesione do sekcji
  „Więcej" na str. 1 (patrz niżej), tak jak w klasie 4-6.

Podpis prowadzącego (dawna końcówka str. 9) jest teraz w bloku podpisów na
str. 5 „Cele SMART", tak jak w klasie 1-3 — nie zostaje na osobnej stronie.
Naukowa podstawa narzędzia (Wellman i Liu / Baron-Cohen / Perner / Premack
i Woodruff — identyczna treść co w klasie 4-6, to ta sama, uniwersalna
podstawa teoretyczna ToM) jest w sekcji „Więcej" na str. 1, ekranowej
(nie drukuje się), tak jak w klasie 1-3 i 4-6.

## Konstrukcja — identyczna z klasą 4-6, tylko dane klasy 7-8

Wszystkie poprawki konstrukcji, które klasa 4-6 przeszła iteracyjnie w tej
sesji, zostały tu zastosowane od razu, w oparciu o już gotowy plik
klasy 4-6 jako wzorzec 1:1:

- **Strona 1**: metryczka (2 pola), „Czym jest ToM", skala, „Więcej"
  (ekranowe: jak wypełniać, naukowa podstawa, „Zalecenia do pracy" wg
  komponentu), nagłówek „Arkusz obserwacji", tabela „Zastosowanie ToM w
  KSzOF". Tej tabeli oryginał nie miał wcale — zbudowana od podstaw, tak
  jak dla klasy 4-6, na bazie **tego samego, realnego** kwestionariusza
  KSzOF_IV-VI (52 pozycje, 9 obszarów, kody ICF) — dla klas VII–VIII nie
  ma osobnego KSzOF, więc to jedyny dostępny, realny punkt odniesienia.
  Opisy w kolumnie „Zakres zachowań i umiejętności" rozszerzone pod kątem
  bardziej zaawansowanych komponentów klasy 7-8 (empatia poznawcza,
  mentalizowanie wyższego rzędu, sarkazm) — **interpretacja wymagająca
  sprawdzenia przez autorkę**, tak jak przy klasie 4-6.
- **Strony 2-3 (arkusz obserwacji)**: jedna ciągła tabela `table.qtable`
  na stronę z wierszami-nagłówkami obszarów wewnątrz tabeli (jak w klasie
  1-3), zamiast osobnych tabel na obszar. Kółeczka oceny neutralnie szare,
  kolorują się dopiero po kliknięciu (`.sel.v0/v1/v2`) — bez automatycznego
  zaznaczania przykładowych ocen przy starcie.
- **Strona 4 („IV Wynik i priorytety")**: wykres słupkowy w konstrukcji
  klasy 1-3 (kompaktowy `viewBox`, siatka tylko 0/5/10), automatyczny opis
  wyników (`#autoOpis`) w stałym miejscu pod wykresem, tabela „Profil
  komponentów — katalog barier i trudności" w 5 kategoriach treningu
  (Profil ToM ogólny / TUE / TUS / TUK / Rekomendacje ogólne) zamiast wg
  numeru komponentu — TUE z komponentu I, TUS z komponentów II i V, TUK
  z komponentów III i IV. Ta sama kompaktująca poprawka CSS co w klasie
  4-6 (blokada rozciągania `.blk`/`table.tb` na całą stronę), więc
  wykres i tabela mieszczą się razem na jednej stronie.
- **Strona 5 „Cele SMART"**: cel główny (nowe zdanie łączące 5
  komponentów — **do sprawdzenia przez autorkę**), tabela `#tab-smart`
  wypełniona 5 gotowymi celami przepisanymi z oryginału, przyciski
  „Zasugeruj cele wg wyników" / „+ Dodaj cel" (te same, ogólne funkcje co
  w klasie 4-6 — zadziałały bez zmian), podpisy.
- **Strona 6 „Proponowane formy wsparcia"**: treść identyczna z klasą 4-6
  — to samo polskie prawo oświatowe, niezależne od wieku ucznia.
- **Strona 7 „Zastosowanie ToM w ocenie ABC i FBA"**: tabela 8 funkcji
  zachowania — kolumny „Funkcja zachowania"/„Definicja operacyjna" to
  ogólna metodyka ABC/FBA, bez zmian; kolumna „Związek z deficytami teorii
  umysłu" przepisana pod komponenty klasy 7-8.

Zweryfikowane po całej przebudowie: brak resztek treści/nazw klasy 4-6 w
pliku (sprawdzone programowo), zero błędów JS, testem interaktywnym
(zaznaczenie ocen → poprawne sumy/wykres/opis automatyczny/sugestie celów).

## Logo PCTP

To samo prawdziwe logo (kwiat lawendy + napis PCTP, `logo-lawenda.webp` z
korzenia repo) co w klasie 1-3 i 4-6 — osadzone wcześniej, w poprzednim
kroku tej sesji, zanim doszło do pełnej przebudowy opisanej wyżej.

## Jak powstał PDF

Tak jak reszta serii: `@page{size:A4}` + `@media print` w HTML, PDF to
odpowiednik **Ctrl+P → Zapisz jako PDF**, wygenerowany tu automatycznie
(headless Chromium, `print_background` + `prefer_css_page_size`).
Zweryfikowane renderem: 7 fizycznych stron, żadna nie ucina treści.
