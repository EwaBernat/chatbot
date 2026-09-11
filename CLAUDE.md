# EduPlaner 2026 · zasady dokumentów (PCTP Koszalin)

Pliki raportów: `eduplaner2026/raport_oceny_funkcjonalnej/`. **Jedno źródło treści:** `raport_data.json` (sekcje 4–16). HTML buduje `build_html.py` (styles.css + part1_pages.html + JSON), PDF powstaje z HTML przez Chromium, Word buduje `generate_raport_docx.js` (czyta ten sam JSON). Zmiana treści = edycja JSON i przebudowa trzech plików.

## Struktura raportu (16 sekcji, bez dublowania – ustalona na życzenie autorki)

- **Część I · Podstawa:** strona „Jak czytać raport” (5 kroków) + **matryca wariantów A/B** (które sekcje dla dziecka z orzeczeniem, a które bez) · strona „Podstawy prawne” · 1 metryczka · 2 obserwacja wstępna (KPOF/KSzOF rozwinięte) · 3 narzędzia obserwacji pogłębionej.
- **Część II · Wyniki oceny:** 4 funkcjonowanie w placówce **w 5 obszarach w kolejności z rozporządzenia**: 1 uczenie się i stosowanie wiedzy · 2 przystosowanie społeczne i emocjonalne · 3 porozumiewanie się · 4 aktywność ruchowa i poruszanie się · 5 dbanie o siebie – samoobsługa i autonomia (z kodami domen ICF jako odnośnikiem do sekcji 5) · 5 wyniki liczbowe KPOF/KSzOF · 6 wyniki arkuszy **w ustalonej kolejności (ta sama w sekcji 3)**: 1 Profil Biopsychospołeczny · 2 ABC · 3 Profil Sensoryczny · 4 Mowa i komunikacja · 5 ToM · 7 Mój głos · 8 działania dotychczas podjęte · 9 analiza jakościowa 9 domen: opis + **cel na rok szkolny** (bez metod – metody tylko w Części III) · 10 wnioski Zespołu: A poziom wsparcia (I/II/III) z uzasadnieniem, B **rekomendacje placówki dla zespołu orzekającego**.
- **Część III · Program wsparcia:** 11 zakres i sposób dostosowania programu wychowania przedszkolnego / podstawy programowej + dostosowania organizacyjne + nowe technologie · 12 zintegrowane działania nauczycieli i specjalistów · 13 zajęcia: A rewalidacja, B pomoc psychologiczno-pedagogiczna (forma, czas, termin, okres, miejsce), C mapa zaleceń poradni → sekcje raportu · 14 uzasadnienie wsparcia dodatkowej osoby · 15 współpraca z rodzicami (zakres, konkretne działania wspierające rodziców) i z poradnią · 16 terminy okresowej oceny efektywności · podpisy.
- **Podstawy prawne przy każdej sekcji 4–16** (plakietka „§ Podstawa prawna”): rozp. ME z 2.03.2026 (Dz. U. 2026 poz. 428, § 7 ust. 6–7), Prawo oświatowe art. 127, rozp. MEN z 9.08.2017 o kształceniu specjalnym (Dz. U. 2020 poz. 1309: § 6 ust. 1 pkt 1–8, ust. 9–10, § 7), rozp. MEN z 9.08.2017 o PPP (Dz. U. 2023 poz. 1798), **nowa podstawa programowa: rozp. ME z 11.03.2026 (Dz. U. 2026 poz. 378, zm. poz. 958)** oraz przejściowo rozp. z 14.02.2017 (Dz. U. 2017 poz. 356) dla klas nieobjętych jeszcze nową podstawą, ICF, RODO. Numery paragrafów pochodzą z JSON (`law`) – przy zmianie przepisów aktualizować tam.
- Zasada „bez dualizmu”: każde zalecenie poradni jest opisane raz, w sekcji, która je realizuje; sekcja 13 C tylko odsyła do właściwej sekcji. Sekcja 9 = CO ma się zmienić (cele), Część III = JAK (metody, zajęcia, osoby).
- **Dwa cele dokumentu, jeden układ:** Wariant A (orzeczenie) = WOPF + elementy IPET; Wariant B (bez orzeczenia) = opinia dla zespołu orzekającego + plan PPP; rewalidacja (13 A) i dodatkowa osoba (14) w Wariancie B tylko jako rekomendacja w 10 B.
- Nazewnictwo: zawsze **IPET** (nie „IPE”). Sumy godzin: rewalidacja w godzinach zegarowych (60 min), PPP jako liczba zajęć × 45 min + konsultacje – nie mieszać jednostek.

## Opinia o funkcjonowaniu dziecka / ucznia dla poradni (§ 7 rozp. ME z 2.03.2026, poz. 428) – wymagania zapamiętane na życzenie autorki

- **Procedura:** przewodniczący zespołu orzekającego (lub rodzic / wnioskodawca) zwraca się do dyrektora; dyrektor wydaje opinię w **10 dni**; **kopia obowiązkowo dla rodziców / pełnoletniego ucznia**.
- **Treść obowiązkowa (§ 7 ust. 6 pkt 1–7, tekst oryginalny):** 1 data wydania · 2 imię i nazwisko · 3 informacja o funkcjonowaniu w placówce (trudności, mocne strony, uzdolnienia rozpoznane przez nauczycieli, wychowawców, specjalistów) · 4 aktualna WOPF (kształcenie specjalne) · 5 aktualna okresowa ocena (zajęcia rewalidacyjno-wychowawcze) · 6 działania podjęte, formy i zakres pomocy (WWR / PPP), okres udzielania, efekty · 7 wnioski dotyczące dalszej pracy. Opinia uwzględnia wyniki obserwacji i działań diagnostycznych w placówce. Ust. 7: pkt 3 dotyczy aktywności i uczestniczenia (ICF) oraz zakresu i rodzaju trudności w realizacji programu wychowania przedszkolnego / programów nauczania w oddziale.
- **Załączniki ewaluacyjne:** dziecko z orzeczeniem – aktualna **WOPFU**; dziecko objęte zajęciami rewalidacyjno-wychowawczymi – aktualna **okresowa ocena funkcjonowania**.
- **Obszary ICF (§ 7 ust. 7 pkt 1, dokładne brzmienie):** dziecko do ukończenia wychowania przedszkolnego – 5: uczenie się i stosowanie wiedzy · zachowania społeczne we wzajemnych kontaktach – przystosowanie społeczne i emocjonalne · porozumiewanie się · aktywność ruchowa – poruszanie się · dbanie o siebie. Uczeń – **7**: uczenie się i stosowanie wiedzy · ogólne zadania i obowiązki · porozumiewanie się · motoryka, poruszanie się, w tym mobilność i aktywność manualna · dbanie o siebie, samoobsługa i samodzielność · życie domowe · wzajemne kontakty i związki międzyludzkie, życie w społeczności szkolnej i lokalnej.
- **§ 8 to ocena zespołu PORADNI, nie opinia placówki:** bariery i ułatwienia, funkcje i struktury ciała, informacje od rodziców, nauczycieli i dziecka, nagrania rodziców, transmisja / nagranie za zgodą. W opinii placówki te treści są tylko fakultatywną częścią „informacje uzupełniające”.
- **Bez reklam – zasada stała:** wszystkie druki, które idą do rodziców lub do poradni, są „wordowskie” (edytowalne DOCX) z danymi placówki (nazwa, adres, pieczęć) w nagłówku; żadnego brandowania EduPlaner w treści ani nagłówkach. Dopuszczalny jedynie maleńki znak w rogu / stopce („sporządzono w EduPlaner 2026”, ok. 6–8 pt), że to nasz druk. Opinia jako osobny, czysty załącznik na końcu raportu (i osobny plik `Opinia_dla_poradni.docx`); sekcja 4 raportu ma tabelę A (przedszkole 5) i B (uczeń 7).

## Zasady merytoryczne – Raport Oceny Funkcjonalnej (zapamiętane na życzenie autorki)

- **Narzędzie bazowe zależy od etapu:** przedszkole = **KPOF**, szkoła = **KSzOF**.
- **Steny tylko dla szkoły (KSzOF).** KPOF (przedszkole) nie ma norm stenowych – nie podaje się stenów, kolumnę „Sten” zostawia się pustą lub ukrywa.
- **Przy średniej nigdy nie pisze się stenu.** Sten może pojawić się wyłącznie w kolumnie „Sten (KSzOF)” dla poszczególnych domen d1–d9.
- **Analiza jakościowa (sekcja 6) obejmuje wszystkie 9 domen ICF** (d1–d9), każda z opisem funkcjonowania i zaleceniami do IPE.
- Raport zawiera sekcję **„Zalecenia z poradni i sposoby ich realizacji w placówce”** rozbitą na trzy bloki: **A) zajęcia rewalidacyjne** (rodzaj, zakres, prowadzący, forma, wymiar tygodniowy, suma godzin; godzina = 60 min), **B) zajęcia z pomocy psychologiczno-pedagogicznej** (rodzaj, forma, wymiar, suma; godzina = 45 min), **C) pozostałe zalecenia** (zalecenie · sposób realizacji · realizator i wymiar · status). Rewalidacja i PPP zawsze osobno i z wymiarem czasowym.
- Podpisy (koordynator, dyrektor, specjalista, rodzic) zawsze na końcu dokumentu.

- **Tytuł druku:** „Ocena Funkcjonalna” z podtytułem „Raport – podsumowanie WOPF i IPET · obszary ICF”. Nagłówki stron: „Ocena Funkcjonalna · …”.

## Czytelność

- **Czcionka treści 11 pt, jednolita** (HTML/PDF 15 px dla akapitów, tabel, list; Word 22 half-points; etykiety 18, nagłówki sekcji 26). 12 pt rozjeżdżało układ – autorka wybrała 11 pt z równym, czytelnym składem. Nie mieszać rozmiarów w treści.
- **Trzy edycje w roku i trzy rodzaje dokumentu:** tabelka edycji na okładce (01 wrzesień – start, 02 styczeń – ocena działań, 03 czerwiec – ocena końcowa); rodzaje: całościowy, sama ocena funkcjonalna (Część I–II + opinia), sam IPET (sekcja 10 + Część III). HTML ma przełączniki, Word `--tryb=`, PDF przez `#tryb=`.
- **Druk ciągły bez pustych stron:** sekcje płyną jedna po drugiej; nowa strona tylko po okładce, na początku Części II i III (PDF) i przed załącznikiem z opinią. Kontekst strony (placówka, dziecko) w marginesie: PDF przez `@page` margin boxes (Chromium), Word przez nagłówek sekcji. Numer strony liczy przeglądarka / Word.
- **Jednolita czcionka w Wordzie:** treść i tabele 24 half-points (12 pt), etykiety 20 (10 pt), nagłówki sekcji 28 (14 pt); nie mieszać rozmiarów w treści.

## Styl graficzny

Wzór IPET EduPlaner 2026: biały papier, lawendowe pola `#EFE9F9`, linie `#D9D0F0`, fiolet `#2D1B69` tylko w akcentach, pomarańczowe plakietki `#E74509`, tytuł wyśrodkowany w jednej linii, nagłówek strony z polami „Dotyczy dziecka / Grupa / Data”. Word: Arial, A4. Nie zmieniać struktury druku bez wyraźnego polecenia.
