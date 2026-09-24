# WOPF — Wielospecjalistyczna Ocena Poziomu Funkcjonowania

Karta scalająca ekosystemu **EduPlaner2026-MJ-PCTP**: nie ocenia ucznia od
nowa, tylko zbiera w jednym miejscu wyniki, które powstały wcześniej w innych
drukach (KSzOF, karta ABC/FBA, ToM, kwestionariusz mowy, profil sensoryczny,
profil biopsychospołeczny). Wspólna marka i konstrukcja z serii `ToM/` —
wzorem jest `klasy_1-3`.

## Status: 24 strony — przebudowa wg „Planu WOPF", do potwierdzenia

| Plik | Opis |
|---|---|
| `WOPF_karta_oceny.html` | źródło — wszystkie 24 strony |
| `WOPF_karta_oceny.pdf` | pełny wydruk (headless Chromium, druk A4) |

**Ta wersja to pełna przebudowa struktury** na podstawie przesłanego przez
Ciebie „Planu WOPF" — 19 ponumerowanych punktów (część z podpunktami a–e).
Poprzednia struktura (sekcje rzymskie I–XXVI, 21 stron) jest w historii
gita — nic nie zginęło, tylko zmienił się układ. Zachowana **dokładnie**
grafika, kolorystyka i styl (fiolet `#2D1B69` + pomarańcz `#E8450A`,
Mulish/Lora, ta sama konstrukcja `.page`/`.sec`/`.cbgrid`/`.ta` co reszta
serii) — zmieniła się tylko kolejność i grupowanie treści, oraz numeracja
(rzymskie I–XXVI → arabskie 1–23, plus podpunkty 7a–7f).

Prawie cała treść to **przeniesienie 1:1** z poprzedniej wersji, tylko
przełożone w nowe miejsce wg Twojego planu. Nowe fragmenty (patrz „Do
potwierdzenia" niżej) to: część punktu 5 i 6 (przełożone na Twoje własne
kategorie), cały punkt 8 (wskrzesza dawno usuniętą syntezę „wynik ogólny"),
cały punkt 9 (nowa synteza obserwacji pogłębionej), część punktu 10
(dołączone metody i formy pracy) i cały punkt 11 (zupełnie nowa treść —
trudności we włączeniu).

## Co jest w środku

- **Str. 1** — **1. Dane ucznia** (10 pól) i **2. Ścieżka dokumentacyjna i
  rodzaj oceny** (ścieżka A/B, 4 rodzaje oceny, tryb postępowania) — bez
  zmian względem poprzedniej wersji, tylko przenumerowane z I/Ia na 1/2.
- **Str. 2** — **3. Zespół specjalistów** (tabela 8 ról, koordynator jako
  pierwszy wiersz) i **4. Mapa dokumentów źródłowych** (11 druków) — ostatnia
  kolumna mapy zaktualizowana: zamiast „sekcja V/VI/VII..." wskazuje teraz
  nowy numer punktu (np. „7a", „7c").
- **Str. 3** — **5. Sytuacje szkolne objęte obserwacją** — przełożone z
  płaskiej listy 12 pozycji na Twoich 5 kategorii (lekcje / przerwy /
  zajęcia ppp / zajęcia rewalidacyjne / inne), każda jako osobna grupa
  checkboxów. Plus zakres i czas obserwacji.
- **Str. 4** — **6. Informacje medyczne** — przełożone na Twoich 7 kategorii
  (leki / choroby przewlekłe / dysfunkcje sensoryczne / wady genetyczne /
  diety / alergie / zachowania behawioralne). Dwie kategorie nie miały
  wcześniej żadnej pozycji na liście — **dysfunkcje sensoryczne** i **wady
  genetyczne** — dodane jako nowe pozycje checkboxów. Plus leki/zalecenia i
  procedura nagła. **Uwaga:** punkty 5 i 6 nie zmieściły się już razem na
  jednej stronie (jak w starej wersji) — nowy układ z 5–7 osobnymi grupami
  zamiast jednej płaskiej listy zajął więcej miejsca, więc dostały dwie
  osobne strony.
- **Str. 5–6** — **7. Wyniki obserwacji, 7a) Obserwacja podstawowa — KSzOF**:
  a) wyniki liczbowe (tabela stenów, **edytowalna**), b) wykres (słupkowy +
  radar, liczą się automatycznie), c) opis merytoryczny (tabela mocne
  strony/trudności) — to dokładnie dawna sekcja V + Va, tylko podpisana
  jako „7a" i z wyraźnym a)/b)/c) wg Twojego planu.
- **Str. 7** — **8. Synteza wyników — wynik podstawowy** (NOWA treść — patrz
  „Do potwierdzenia"). Wskrzesza syntezę „wynik ogólny / reguła nadrzędna",
  którą usunęłaś wcześniej w tej sesji (`git log`: „Uprość sekcję V: usuń
  panel synchronizacji i całą stronę »wynik ogólny/synteza«") — teraz Twój
  plan chce ją z powrotem jako osobny punkt 8, więc ją odtworzyłam. Przy
  okazji **ożywia dwa martwe elementy JS**, które od tamtej zmiany istniały
  tylko w kodzie bez żadnego miejsca na stronie: `#wopfAvgSten` i
  `#wopfAvgPoziom` (średni sten i poziom, liczone automatycznie z tabeli w
  7a) — teraz mają wreszcie gdzie się wyświetlić. Osobno: „Synteza wg
  poziomów" to ten sam autouzupełniany tekst co dawny `#autoOpisKszof` pod
  tabelą w 7a, tylko przeniesiony tutaj i bez duplikatu w 7a.
- **Str. 8** — **Obserwacja pogłębiona** (nagłówek), **7b) Profil
  biopsychospołeczny** — dawna sekcja X, bez zmian treści, tylko bez
  tytułowego „Kontekst biopsychospołeczny — czynniki środowiskowe ICF" (Twój
  plan nazywa to wprost „Profil biopsychospołeczny").
- **Str. 9** — **7c) Analiza ABC/FBA — zachowania trudne** — dawna sekcja
  VI, plus hipoteza funkcjonalna, plus plan pozytywnego wsparcia (PBS) i
  nota o Standardach Ochrony Małoletnich (dawniej rozdzielone między dwie
  strony, teraz razem przy ABC/FBA, bo tematycznie do siebie należą).
- **Str. 10** — **7d) Profil sensoryczny** (dawna IX + wnioski sensoryczne)
  i **7e) Ocena poziomu rozwoju mowy** (dawna VIII, początek tabeli).
- **Str. 11** — dokończenie 7e (sposób porozumiewania się, kierunki terapii
  logopedycznej) i **7f) Ocena ToM** (dawna VII). **Kolejność zmieniona**
  względem starej wersji (była: ABC/FBA → ToM → mowa → sensoryczny →
  biopsychospołeczny) na kolejność z Twojego planu (biopsychospołeczny →
  ABC/FBA → sensoryczny → mowa → ToM, czyli 7b→7c→7d→7e→7f).
- **Str. 12** — **9. Synteza wszystkich wyników z obserwacji pogłębionej
  oraz z zaleceń poradni pp** (CAŁKOWICIE NOWA treść — patrz „Do
  potwierdzenia"). Tabela: jeden wiersz na każde z pięciu narzędzi 7b–7f,
  edytowalna komórka na najważniejszy wniosek; osobno notatka na zalecenia
  z poradni i notatka na samą syntezę.
- **Str. 13–14** — **10. Synteza wyników zintegrowanych** — łączy dawną
  sekcję XI (tabela synteza 8 obszarów: mocne strony/trudności) i dawną
  XIII (przyczyny niepowodzeń, bariery, ograniczenia — 8-wierszowa tabela),
  plus **metody i formy pracy** dołączone tutaj w skróconej formie (Twój
  plan wymienia „metody i formy pracy" jako element tej syntezy, a nie jako
  osobny punkt — więc dawna, pełna sekcja XV ze szczegółową tabelą
  metoda/przedmiot **zniknęła**, został tylko skrócony checklist metod i
  form). „Zintegrowane działania" mają tu tylko jednozdaniowy skrót — pełny
  zakres jest w punkcie 15.
- **Str. 15** — **11. Trudności w zakresie włączenia ucznia** w zajęciach
  wspólnych z oddziałem (CAŁKOWICIE NOWA treść — patrz „Do potwierdzenia").
  Checklist sytuacji grupowych, opis obserwowalny, checklist wsparcia
  ułatwiającego włączenie.
- **Str. 16** — **12. Decyzja zespołu** — poziom wsparcia (dawna XX) i
  **13. Zalecenia i cele do realizacji w IPET/programie** — początek tabeli
  celów SMART (dawna XXI).
- **Str. 17** — dokończenie 13 (2 przykładowe karty SMART) i **14. Zakres
  dostosowań wymagań edukacyjnych** — początek (dawna XVI, tabela 4
  kanałów).
- **Str. 18** — dokończenie 14 (checklist sprawdzania wiedzy, dostosowania
  egzaminu ósmoklasisty) i **15. Zintegrowane działania nauczycieli i
  specjalistów** — początek (dawna XVIII, tabela).
- **Str. 19** — dokończenie 15 (wspólne strategie, ustalenia, termin
  spotkań) i **16. Zakres proponowanego wsparcia** — początek: checklist
  „kto wspiera ucznia" (dawna Vb/XIV — teraz scalona w jednym miejscu,
  patrz „Do potwierdzenia").
- **Str. 20** — dokończenie 16 (zajęcia rewalidacyjne, zajęcia z ppp,
  programy terapeutyczne — dawna XVII).
- **Str. 21** — **17. Współpraca z rodzicami** i **18. Współpraca
  międzysektorowa** — obie połowy dawnej sekcji XIX, teraz jako dwa osobne
  punkty wg Twojego planu.
- **Str. 22** — **19. Plan modyfikacji w ciągu roku szkolnego** — terminy
  ewaluacji i oceny efektywności (dawna XXII), z odsyłaczami do nowych
  numerów punktów zamiast starych sekcji rzymskich.
- **Str. 23** — **20. Przeniesienie informacji — do IPET albo do PWES**
  (dawna XXIII, tabela 9 wierszy + dokończenie: dokument wynikowy,
  priorytety na półrocze) — odsyłacze w tabeli zaktualizowane do nowych
  numerów punktów.
- **Str. 24** — **21. Podpisy zespołu ds. WOPF**, **22. Wykaz załączników**,
  **23. Klauzula informacyjna RODO i ważność dokumentu** — dawne XXIV–XXVI,
  bez zmian treści, tylko przenumerowane (kontynuacja 1–23, żeby cała
  numeracja w dokumencie była jednym ciągiem, a nie mieszanką cyfr i liter).

## Interaktywność

Tabela stenów w **7a** ma pełne przeliczanie automatyczne — jedyne miejsce,
gdzie WOPF prezentuje liczby. Wpisanie stenu 1–10 w dowolnym z 9 wierszy
automatycznie liczy: poziom wsparcia w tym samym wierszu, słupek i punkt na
mapie radarowej (oba w 7a), **a teraz też średni sten i poziom ogólny w
punkcie 8** (`#wopfAvgSten`/`#wopfAvgPoziom` — martwe od poprzedniej sesji,
ożywione tym razem) oraz syntezę wg poziomów pod nimi (zamraża się po
pierwszej ręcznej poprawce, jak poprzednio `#autoOpisKszof`). Pozostałe
punkty to pola i tabele do ręcznego wypełnienia.

## Znaleziony i naprawiony błąd konstrukcyjny (z poprzednich wersji, nadal aktualny)

Współdzielony arkusz stylów (ten sam co w całej serii ToM) ma regułę, która
automatycznie rozciąga JEDYNĄ tabelę na stronie na 100% wysokości karty
(`flex:1 1 auto;height:100%`). Na stronach, gdzie po tabeli jest jeszcze
dużo innej treści, ta reguła konfliktowała z `table-layout:fixed` i
powodowała, że **ostatni wiersz tabeli był rysowany, ale zasłaniany przez
następny blok**. Naprawione przez jawne wyłączenie tego rozciągania
(`flex:0 0 auto;height:auto`) na każdej tabeli budowanej dla WOPF —
zachowane we wszystkich tabelach tej przebudowy.

## Do potwierdzenia przez autorkę

Ta przebudowa jest większa niż poprzednie zmiany w tej sesji — przełożyłam
prawie cały dokument w nowy układ na podstawie Twojego planu, ale kilka
miejsc wymagało decyzji, których plan wprost nie rozstrzygał. Zaznaczam je
tu, żebyś mogła sprawdzić, czy trafiłam:

- **Punkt 8 „Synteza — wynik podstawowy" (str. 7) — czy dobrze odtworzyłam
  usuniętą wcześniej treść.** Twój plan wymienia to jako osobny punkt, ale
  nie opisuje go szczegółowo. Odtworzyłam średni sten + poziom ogólny +
  „regułę nadrzędną" (progi 8–10/5–7/1–4) — to była dokładnie treść, którą
  usunęłaś w tej sesji wcześniej pod nazwą „wynik ogólny / reguła
  nadrzędna / synteza wg poziomów". Jeśli chodziło Ci o coś innego pod tą
  nazwą — daj znać.
- **Punkt 9 „Synteza obserwacji pogłębionej i zaleceń poradni" (str. 12) —
  całkiem nowa treść, moja interpretacja.** Zbudowałam to jako tabelę z
  jednym wierszem na każde z 5 narzędzi z punktu 7 (7b–7f) plus osobną
  notatkę na zalecenia z poradni psychologiczno-pedagogicznej. To jest
  szkielet do wypełnienia, nie gotowa treść — sprawdź, czy taki układ
  (tabela + 2 notatki) Ci odpowiada, czy wolisz inną formę.
- **Punkt 10 — „metody i formy pracy" bez osobnej, szczegółowej sekcji
  (str. 13–14).** Twój plan wymienia metody i formy pracy jako SKŁADNIK
  syntezy w punkcie 10, a nie jako osobny punkt — więc dawna sekcja XV (ze
  szczegółową tabelą metoda/forma/kto na każdy przedmiot) zniknęła, a
  został tylko skrócony checklist metod i form. Jeśli to za duża strata
  szczegółowości — mogę dodać skróconą wersję tamtej tabeli z powrotem.
- **Punkt 11 „Trudności w zakresie włączenia" (str. 15) — cała treść nowa,
  moja propozycja.** Nic w poprzedniej wersji WOPF nie odpowiadało temu
  punktowi wprost, więc checklist sytuacji grupowych i wsparcia
  ułatwiającego napisałam od zera, wzorując się stylistycznie na
  analogicznych checklistach gdzie indziej w dokumencie — to nie jest
  przepisane z żadnego istniejącego druku źródłowego, tak jak reszta
  dokumentu. Do sprawdzenia najbardziej ze wszystkich nowych fragmentów.
- **Punkt 16 „Zakres proponowanego wsparcia" (str. 19–20) łączy trzy dawne
  fragmenty w jeden punkt** — checklist „kto wspiera" (dawna Vb/XIV, do tej
  pory duplikowana w dwóch miejscach dokumentu — teraz jest tylko tutaj,
  raz), zajęcia rewalidacyjne i zajęcia z ppp (dawna XVII). To rozwiązuje
  przy okazji dawny „dualizm" Vb/XIV, który wcześniej flagowałam do
  potwierdzenia — teraz jest tylko jedno miejsce z tym pytaniem.
- **Sekcja VII / punkt 7f, komponenty ToM (K1–K5) — nierozwiązane z
  poprzednich sesji.** Oryginalny PDF autorki używa innego zestawu
  komponentów niż którykolwiek z trzech gotowych wariantów ToM w tym
  repozytorium. Przepisane tu **dosłownie z oryginału WOPF**, bez zmian w
  tej przebudowie — nadal wymaga Twojej decyzji, czy to osobny, uproszczony
  zestaw K1–K5, czy pomyłka do poprawienia.
- **Odsyłacze do numerów punktów w tekście** (np. w tabeli mapy dokumentów
  na str. 2, w tabeli przeniesienia informacji na str. 23, w tabeli oceny
  efektywności na str. 22) zostały zaktualizowane ze starych sekcji
  rzymskich na nowe numery — sprawdziłam wszystkie tabele i tagi nagłówków,
  ale przy dokumencie tej wielkości niewykluczone, że gdzieś w treści
  notatek zostało przeoczone odwołanie do starego numeru sekcji. Daj znać,
  jeśli coś takiego zauważysz.
- Żaden z czterech wariantów ToM ani WOPF nie jest jeszcze przeniesiony do
  `Zatwierdzone/` — czeka na Twoje potwierdzenie powyższych punktów.

## Jak powstał PDF

Tak jak reszta serii: `@page{size:A4}` + `@media print` w HTML, PDF to
odpowiednik **Ctrl+P → Zapisz jako PDF**, wygenerowany tu automatycznie
(headless Chromium, `print_background` + `prefer_css_page_size`).
Zweryfikowane renderem: 24 fizyczne strony, żadna nie ucina treści
(sprawdzone programowo — margines do stopki dodatni na każdej stronie, i
zbalansowane tagi `<div>` w całym dokumencie), zero błędów JS,
interaktywność stenów i nowo ożywionej średniej (punkt 8) przetestowana.
