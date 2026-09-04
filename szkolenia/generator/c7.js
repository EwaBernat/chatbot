const G = require('./gen.js');
const { Paragraph, AlignmentType, BorderStyle, t, p, H1, H2, H3, bullet, numItem, spacer,
        pageBreak, box, table, lines, modul, straznik, cw, CONTENT, PURPLE, ORANGE, LIGHT, LIGHTO } = G;

const C = [];
const add = (...x) => x.forEach(e => C.push(e));
const BLANK = '';

add(pageBreak());
add(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 200, after: 60 },
  children: [t('ZAŁĄCZNIKI  Z1 – Z8', { bold: true, size: 34, color: PURPLE, sp: 30 })] }));
add(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 240 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: ORANGE, space: 8 } },
  children: [t('materiały do powielenia dla uczestników', { size: 20, color: '4A4A4A' })] }));
add(p('Załączniki Z2 (tabela porównawcza „co było / co jest”) oraz Z3 (mapa obszarów ICF d1–d9) znajdują się w treści modułów M1 i M2 — powielamy je bezpośrednio z tych stron.'));

/* ---- Z1 ---- */
add(spacer(160));
add(H1('Z1', 'Ściąga podstaw prawnych — jedna strona do laminowania'));
add(table(['Zagadnienie', 'Akt prawny', 'Publikator', 'Status · wejście w życie'], [
  ['Podstawa programowa wychowania przedszkolnego',
   'Rozporządzenie Ministra Edukacji z dnia 11 marca 2026 r. w sprawie podstawy programowej wychowania przedszkolnego oraz podstawy programowej kształcenia ogólnego dla szkoły podstawowej, w tym dla uczniów z niepełnosprawnością intelektualną w stopniu umiarkowanym lub znacznym',
   'Dz.U. 2026 poz. 378', 'obowiązuje · od 01.09.2026'],
  ['Ocena funkcjonalna; orzeczenia i opinie zespołów orzekających',
   'Rozporządzenie Ministra Edukacji z dnia 2 marca 2026 r. w sprawie orzeczeń i opinii wydawanych przez zespoły orzekające działające w publicznych poradniach psychologiczno-pedagogicznych',
   'Dz.U. 2026 poz. 428', 'obowiązuje · od 14.04.2026, a § 7 ust. 6–7 i § 8 — od 01.09.2026'],
  ['Zasady organizacji i udzielania pomocy psychologiczno-pedagogicznej',
   'Rozporządzenie Ministra Edukacji Narodowej z dnia 9 sierpnia 2017 r. w sprawie zasad organizacji i udzielania pomocy psychologiczno-pedagogicznej w publicznych przedszkolach, szkołach i placówkach',
   'Dz.U. 2017 poz. 1591; tekst jedn. Dz.U. 2023 poz. 1798', 'obowiązuje · tekst jednolity z 05.09.2023'],
  ['Kształcenie specjalne — WOPFU, IPET, dostosowania',
   'Rozporządzenie Ministra Edukacji Narodowej z dnia 9 sierpnia 2017 r. w sprawie warunków organizowania kształcenia, wychowania i opieki dla dzieci i młodzieży niepełnosprawnych, niedostosowanych społecznie i zagrożonych niedostosowaniem społecznym',
   'Dz.U. 2017 poz. 1578; tekst jedn. Dz.U. 2020 poz. 1309', 'obowiązuje · tekst jednolity z 2020 r.'],
  ['Dokumentacja przebiegu nauczania, działalności wychowawczej i opiekuńczej',
   'Rozporządzenie Ministra Edukacji Narodowej z dnia 25 sierpnia 2017 r. w sprawie sposobu prowadzenia przez publiczne przedszkola, szkoły i placówki dokumentacji przebiegu nauczania, działalności wychowawczej i opiekuńczej oraz rodzajów tej dokumentacji',
   'Dz.U. 2017 poz. 1646; tekst jedn. Dz.U. 2024 poz. 50', 'obowiązuje · tekst jednolity z 2024 r.'],
  ['Ustrój szkolnictwa, zadania przedszkola, prawa rodziców',
   'Ustawa z dnia 14 grudnia 2016 r. — Prawo oświatowe',
   'tekst jedn. Dz.U. 2026 poz. 820', 'obowiązuje · tekst jednolity ogł. 22.06.2026'],
  ['Ochrona danych osobowych, w tym danych o zdrowiu dziecka',
   'Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 (RODO) — art. 6 ust. 1 lit. c i e; art. 9 ust. 2 lit. g',
   'Dz.Urz. UE L 119 z 04.05.2016 · CELEX 32016R0679', 'obowiązuje · inny typ publikatora niż Dz.U.'],
  ['WYJĄTEK HISTORYCZNY — poprzednia podstawa programowa (stan do 31.08.2026, przywołana wyłącznie w tabeli porównawczej modułu M1)',
   'Rozporządzenie Ministra Edukacji Narodowej z dnia 14 lutego 2017 r., załącznik nr 1',
   'Dz.U. 2017 poz. 356', 'utraciło moc z dniem 31.08.2026 · zakres rozdzielony na Dz.U. 2026 poz. 378 i Dz.U. 2026 poz. 1012'],
  ['WYJĄTEK HISTORYCZNY — poprzednie rozporządzenie o orzeczeniach i opiniach (stan do 13.04.2026, przywołane wyłącznie w tabeli porównawczej modułu M1)',
   'Rozporządzenie Ministra Edukacji Narodowej z dnia 7 września 2017 r.',
   'Dz.U. 2017 poz. 1743 ze zm.', 'zastąpione przez Dz.U. 2026 poz. 428'],
], [2100, 3200, 2100, CONTENT - 2100 - 3200 - 2100], { boldCol0: true }));
add(spacer(80));
add(box('SZEŚĆ REGUŁ STRAŻNIKA PRAWA', [
  p([t('L1 · ', { bold: true, color: ORANGE }), t('Każdy cytowany akt istnieje w rejestrze. Akt w druku, a nie w rejestrze, jest naruszeniem — nie „przepisem do dopisania przy okazji”.')]),
  p([t('L2 · ', { bold: true, color: ORANGE }), t('Jeden akt, jedno brzmienie. Cytujemy dokładnie tak, jak stoi w zapisie kanonicznym — nie „Dz.U. z 2017 r. poz.” raz, a „Dz.U. 2017 poz.” drugi raz.')]),
  p([t('L3 · ', { bold: true, color: ORANGE }), t('Dopasowanie po parze rok–pozycja, nigdy po tekście tytułu. Uwaga na inne typy publikatorów: RODO ma sygnaturę Dz.Urz. UE i numer CELEX, nie pozycję Dz.U.')]),
  p([t('L4 · ', { bold: true, color: ORANGE }), t('Akt uchylony nie stoi w druku bez jawnego wyjątku z powodem i datą. W tym scenariuszu dwa takie wyjątki są oznaczone w tabeli powyżej — oba dotyczą wyłącznie tabeli porównawczej „co było / co jest”.')]),
  p([t('L5 · ', { bold: true, color: ORANGE }), t('Sygnatura musi zgadzać się z opisem. Najgroźniejszy błąd to prawidłowa sygnatura pod nieprawidłową nazwą. Dwa rozporządzenia z 9 sierpnia 2017 r. różnią się tylko pozycją: 1578 to kształcenie specjalne, 1591 to pomoc psychologiczno-pedagogiczna.')]),
  p([t('L6 · ', { bold: true, color: ORANGE }), t('Zmiana prawa jest jedną edycją, nie polowaniem: zmieniamy status jednej pozycji w rejestrze, uruchamiamy sondę, dostajemy listę druków do poprawy.')]),
  p([t('Termin przeglądu: ', { bold: true }), t('co trzy miesiące, obowiązkowo 1 września i 1 stycznia, oraz zawsze przed wydaniem dokumentacji placówce. Nie cytujemy przepisów z pamięci ani z materiałów szkoleniowych — także z tego.')]),
], { fill: LIGHTO, bar: ORANGE }));

/* ---- Z4 ---- */
add(pageBreak());
add(H1('Z4', 'Karta decyzyjna — czy uruchamiamy moduł pogłębiony?'));
add(p('Kartę wypełnia zespół po analizie arkuszy KPOF. Jedna karta na jedno dziecko. Kartę wpina się do teczki dziecka niezależnie od podjętej decyzji — także wtedy, gdy zdecydowano nie uruchamiać modułu. Zapis decyzji odmownej jest równie ważny jak zapis decyzji pozytywnej.'));
add(spacer(80));
add(table(null, [
  ['Dziecko / grupa', BLANK], ['Data analizy / skład zespołu', BLANK],
  ['Wersja KPOF (A / B / C)', BLANK], ['Wynik ogólny i kwalifikacja', BLANK],
], [2600, CONTENT - 2600], { boldCol0: true, zebra: false }));
add(spacer(120));
add(H3('Krok 1 — sprawdź reguły'));
add(table(['Reguła', 'Warunek', 'Spełniona?'], [
  ['R1', 'Średnia któregokolwiek obszaru poniżej 2,0.', '☐ TAK   ☐ NIE'],
  ['R2', 'Dwa lub więcej twierdzeń ocenionych na 1 lub 2 w tym samym obszarze.', '☐ TAK   ☐ NIE'],
  ['R3', 'Rozbieżność średniej obszaru między oceniającymi ≥ 1,5 pkt.', '☐ TAK   ☐ NIE'],
  ['R4', 'Sygnał zdrowotny z metryczki (sekcja VI).', '☐ TAK   ☐ NIE'],
  ['R5', 'Zachowanie powtarzalne, zagrażające lub przerywające uczestnictwo.', '☐ TAK   ☐ NIE'],
  ['R6', 'Brak poprawy mimo udzielanej pomocy p-p przez ok. 3 miesiące.', '☐ TAK   ☐ NIE'],
], [900, 5900, CONTENT - 900 - 5900], { boldCol0: true }));
add(spacer(120));
add(H3('Krok 2 — wybierz moduł'));
add(table(['Moduł', 'Uruchamiamy?', 'Uzasadnienie (obszar, twierdzenia, obserwacje)'], [
  ['ABC — analiza behawioralna', '☐ TAK  ☐ NIE', BLANK],
  ['Profil sensoryczny', '☐ TAK  ☐ NIE', BLANK],
  ['Obserwacja ToM', '☐ TAK  ☐ NIE', BLANK],
], [2600, 1700, CONTENT - 2600 - 1700], { boldCol0: true, zebra: false }));
add(spacer(120));
add(H3('Krok 3 — organizacja'));
add(table(null, [
  ['Osoba prowadząca obserwację', BLANK],
  ['Termin rozpoczęcia i zakończenia', BLANK],
  ['Liczba planowanych zapisów / zdarzeń', BLANK],
  ['Data spotkania zespołu omawiającego wynik', BLANK],
  ['Poinformowano rodzica — data i forma', BLANK],
  ['Podpisy członków zespołu', BLANK],
], [3400, CONTENT - 3400], { boldCol0: true, zebra: false }));

/* ---- Z5 ---- */
add(pageBreak());
add(H1('Z5', 'Karta celu SMART z wbudowaną ewaluacją'));
add(p('Jedna karta na jeden cel. Karta służy jednocześnie do zaplanowania celu i do jego ewaluacji — dolna część wypełniana jest w terminie pomiaru, bez tworzenia osobnego dokumentu.'));
add(spacer(100));
add(table(['Element', 'Zapis'], [
  ['Dziecko / grupa', BLANK],
  ['Źródło celu w WOPF (blok, strona, cytat)', BLANK],
  ['Obszar ICF (d1–d9) i punkt podstawy programowej', BLANK],
  ['Poziom wyjściowy — ocena KPOF dla tego zachowania', BLANK],
], [3600, CONTENT - 3600], { boldCol0: true, zebra: false }));
add(spacer(100));
add(box('TREŚĆ CELU — WYPEŁNIJ WEDŁUG FORMUŁY', [
  p([t('[Imię] w [sytuacja] będzie [zachowanie] w [ile razy z ilu prób] przy [poziom wsparcia] do [data]; pomiar: [narzędzie].', { i: true, color: '6B6B6B' })]),
  ...lines(4),
], { fill: 'FFFFFF', bar: PURPLE }));
add(spacer(100));
add(table(['Kontrola SMART', 'Sprawdzenie', 'OK?'], [
  ['S — konkretny', 'Czy wskazano zachowanie i sytuację?', '☐'],
  ['M — mierzalny', 'Czy jest liczba i poziom wsparcia?', '☐'],
  ['A — osiągalny', 'Czy to jeden krok od poziomu wyjściowego z KPOF?', '☐'],
  ['R — istotny', 'Czy da się wskazać źródło w WOPF?', '☐'],
  ['T — określony w czasie', 'Czy jest data osiągnięcia i data pomiaru?', '☐'],
], [2200, 5900, CONTENT - 2200 - 5900], { boldCol0: true }));
add(spacer(120));
add(H3('Ewaluacja celu — wypełnia zespół w terminie pomiaru'));
const opcje = (arr) => arr.map(x => new Paragraph({ spacing: { before: 40, after: 40 },
  children: [t(x, { size: 17 })] }));
const wynikOpc = () => opcje(['☐ osiągnięty w pełni', '☐ osiągnięty częściowo', '☐ brak postępu', '☐ regres']);
const decyzjaOpc = () => opcje(['☐ zamykamy cel', '☐ kontynuujemy bez zmian', '☐ modyfikujemy IPET', '☐ zespół z rodzicem']);
add(table(['Data pomiaru', 'Wartość osiągnięta', 'Wynik', 'Decyzja'], [
  [BLANK, BLANK, wynikOpc(), decyzjaOpc()],
  [BLANK, BLANK, wynikOpc(), decyzjaOpc()],
], [1500, 1900, 2900, CONTENT - 1500 - 1900 - 2900], { zebra: false }));
add(spacer(80));
add(table(null, [['Uzasadnienie decyzji i zmiany wprowadzone w IPET', lines(3)]], [3600, CONTENT - 3600], { boldCol0: true, zebra: false }));

/* ---- Z6 ---- */
add(pageBreak());
add(H1('Z6', 'Kalendarz dokumentacji — rok szkolny 2026 / 2027'));
add(p('Kalendarz przyjmuje rada pedagogiczna w module M10. Kolumna „odpowiedzialny” wypełniana jest na szkoleniu — bez nazwisk harmonogram pozostaje deklaracją.'));
add(spacer(80));
add(table(['Termin', 'Zadanie', 'Dokument', 'Odpowiedzialny'], [
  ['1–15 września', 'Zebranie i uzupełnienie metryczek; odbiór podpisów pod klauzulą RODO i upoważnieniami do odbioru.', 'Metryczka dziecka', BLANK],
  ['do 15 września', 'Weryfikacja orzeczeń i opinii złożonych w przedszkolu; uruchomienie zegara 30 dni dla nowych orzeczeń.', 'Metryczka, sekcja VII', BLANK],
  ['15–30 września', 'Wypełnienie KPOF przez nauczycieli i specjalistów we wszystkich grupach, także u 3-latków (dziecko z orzeczeniem musi mieć IPET do 30 września); przekazanie arkuszy rodzicom.', 'KPOF A / B / C', BLANK],
  ['do 30 września', 'Opracowanie IPET dla dzieci rozpoczynających kształcenie z orzeczeniem.', 'IPET', BLANK],
  ['wrzesień / październik', 'Pierwsza WOPF w roku szkolnym; spotkania zespołów z rodzicami.', 'WOPF', BLANK],
  ['1–15 października', 'Analiza profili, karty decyzyjne, uruchomienie modułów pogłębionych.', 'Karta decyzyjna Z4', BLANK],
  ['październik / listopad', 'Prowadzenie modułów pogłębionych (2–3 tygodnie obserwacji).', 'ABC / sensoryczny / ToM', BLANK],
  ['listopad', 'Przegląd wskaźników — 15 minut na dziecko, notatka w dzienniku. Bez pełnej WOPF.', 'Karta celu Z5', BLANK],
  ['grudzień / styczeń', 'Wystąpienia do poradni za zgodą rodziców dla dzieci bez poprawy mimo udzielanej pomocy.', 'Opinia o funkcjonowaniu', BLANK],
  ['styczeń / luty', 'Druga WOPF; ewaluacja półroczna celów SMART; modyfikacja IPET.', 'WOPF + IPET + Z5', BLANK],
  ['styczeń / luty', 'Ocena efektywności pomocy p-p dla dzieci bez orzeczenia; wnioski o dalszych działaniach.', 'Dokumentacja pomocy p-p', BLANK],
  ['marzec', 'Przegląd wskaźników — notatka w dzienniku.', 'Karta celu Z5', BLANK],
  ['do 30 kwietnia', 'Informacja o gotowości dziecka do podjęcia nauki w szkole podstawowej — wydanie rodzicom.', 'Informacja o gotowości', BLANK],
  ['kwiecień / maj', 'KPOF — pomiar kontrolny na tym samym arkuszu, innym kolorem; porównanie profili.', 'KPOF', BLANK],
  ['maj / czerwiec', 'Trzecia WOPF (zalecana) — podsumowanie roku; wnioski do organizacji pracy na kolejny rok.', 'WOPF', BLANK],
  ['czerwiec', 'Ocena efektywności pomocy p-p na zakończenie form; wnioski dla nowych zespołów.', 'Dokumentacja pomocy p-p', BLANK],
  ['czerwiec', 'Przegląd i uporządkowanie teczek; przekazanie dokumentacji zgodnie z instrukcją kancelaryjną.', 'Teczki dzieci', BLANK],
  ['cały rok — 10 dni', 'Wydanie opinii o funkcjonowaniu dziecka od dnia otrzymania przez dyrektora prośby przewodniczącego zespołu orzekającego (§ 7 ust. 3).', 'Opinia o funkcjonowaniu', BLANK],
  ['cały rok — 30 dni', 'Opracowanie IPET od dnia złożenia w przedszkolu orzeczenia o potrzebie kształcenia specjalnego.', 'IPET', BLANK],
], [1750, 4000, 2000, CONTENT - 1750 - 4000 - 2000], { boldCol0: true }));

module.exports = C;
