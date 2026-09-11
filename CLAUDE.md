# EduPlaner 2026 · zasady dokumentów (PCTP Koszalin)

Pliki raportów: `eduplaner2026/raport_oceny_funkcjonalnej/`. **Jedno źródło treści:** `raport_data.json` (sekcje 4–16). HTML buduje `build_html.py` (styles.css + part1_pages.html + JSON), PDF powstaje z HTML przez Chromium, Word buduje `generate_raport_docx.js` (czyta ten sam JSON). Zmiana treści = edycja JSON i przebudowa trzech plików.

## Struktura raportu (16 sekcji, bez dublowania – ustalona na życzenie autorki)

- **Część I · Podstawa:** strona „Podstawy prawne i jak czytać raport” (tabela aktów prawnych + 5 kroków) · 1 metryczka · 2 obserwacja wstępna · 3 narzędzia obserwacji pogłębionej.
- **Część II · Wyniki oceny:** 4 funkcjonowanie w placówce · 5 wyniki liczbowe KPOF/KSzOF · 6 wyniki arkuszy (ABC, sensoryczny, biopsychospołeczny, mowa, ToM) · 7 Mój głos (perspektywa dziecka) · 8 działania dotychczas podjęte · 9 analiza jakościowa 9 domen z kierunkami pracy · 10 decyzja Zespołu o poziomie wsparcia (I/II/III) z uzasadnieniem.
- **Część III · Program wsparcia:** 11 zakres i sposób dostosowania programu wychowania przedszkolnego / podstawy programowej + dostosowania organizacyjne + nowe technologie · 12 zintegrowane działania nauczycieli i specjalistów · 13 zajęcia: A rewalidacja, B pomoc psychologiczno-pedagogiczna (forma, czas, termin, okres, miejsce), C mapa zaleceń poradni → sekcje raportu · 14 uzasadnienie wsparcia dodatkowej osoby · 15 współpraca z rodzicami (zakres, konkretne działania wspierające rodziców) i z poradnią · 16 terminy okresowej oceny efektywności · podpisy.
- **Podstawy prawne przy każdej sekcji 4–16** (plakietka „§ Podstawa prawna”): rozp. ME z 2.03.2026 (Dz. U. 2026 poz. 428, § 7 ust. 6–7), Prawo oświatowe art. 127, rozp. MEN z 9.08.2017 o kształceniu specjalnym (Dz. U. 2020 poz. 1309: § 6 ust. 1 pkt 1–8, ust. 9–10, § 7), rozp. MEN z 9.08.2017 o PPP (Dz. U. 2023 poz. 1798), rozp. o podstawie programowej (Dz. U. 2017 poz. 356), ICF, RODO. Numery paragrafów pochodzą z JSON (`law`) – przy zmianie przepisów aktualizować tam.
- Zasada „bez dualizmu”: każde zalecenie poradni jest opisane raz, w sekcji, która je realizuje; sekcja 13 C tylko odsyła do właściwej sekcji.

## Zasady merytoryczne – Raport Oceny Funkcjonalnej (zapamiętane na życzenie autorki)

- **Narzędzie bazowe zależy od etapu:** przedszkole = **KPOF**, szkoła = **KSzOF**.
- **Steny tylko dla szkoły (KSzOF).** KPOF (przedszkole) nie ma norm stenowych – nie podaje się stenów, kolumnę „Sten” zostawia się pustą lub ukrywa.
- **Przy średniej nigdy nie pisze się stenu.** Sten może pojawić się wyłącznie w kolumnie „Sten (KSzOF)” dla poszczególnych domen d1–d9.
- **Analiza jakościowa (sekcja 6) obejmuje wszystkie 9 domen ICF** (d1–d9), każda z opisem funkcjonowania i zaleceniami do IPE.
- Raport zawiera sekcję **„Zalecenia z poradni i sposoby ich realizacji w placówce”** rozbitą na trzy bloki: **A) zajęcia rewalidacyjne** (rodzaj, zakres, prowadzący, forma, wymiar tygodniowy, suma godzin; godzina = 60 min), **B) zajęcia z pomocy psychologiczno-pedagogicznej** (rodzaj, forma, wymiar, suma; godzina = 45 min), **C) pozostałe zalecenia** (zalecenie · sposób realizacji · realizator i wymiar · status). Rewalidacja i PPP zawsze osobno i z wymiarem czasowym.
- Podpisy (koordynator, dyrektor, specjalista, rodzic) zawsze na końcu dokumentu.

## Styl graficzny

Wzór IPET EduPlaner 2026: biały papier, lawendowe pola `#EFE9F9`, linie `#D9D0F0`, fiolet `#2D1B69` tylko w akcentach, pomarańczowe plakietki `#E74509`, tytuł wyśrodkowany w jednej linii, nagłówek strony z polami „Dotyczy dziecka / Grupa / Data”. Word: Arial, A4. Nie zmieniać struktury druku bez wyraźnego polecenia.
