const G = require('./gen.js');
const { Paragraph, AlignmentType, BorderStyle, t, p, H1, H2, H3, bullet, numItem, spacer,
        pageBreak, box, table, tableIn, modul, straznik, cw, CONTENT, PURPLE, ORANGE, LIGHT, LIGHTO } = G;

const C = [];
const add = (...x) => x.forEach(e => C.push(e));

/* ============ STRONA TYTUŁOWA ============ */
add(
  spacer(600),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 },
    children: [t('PCTP  ·  EduPlaner 2026', { bold: true, size: 20, color: ORANGE, sp: 40 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 },
    children: [t('SCENARIUSZ SZKOLENIA RADY PEDAGOGICZNEJ', { bold: true, size: 20, color: PURPLE, sp: 30 })] }),
  spacer(200),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120, line: 620 },
    children: [t('Od czego zacząć dokumentację', { bold: true, size: 44, color: PURPLE })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 240, line: 620 },
    children: [t('w nowym roku szkolnym 2026 / 2027', { bold: true, size: 44, color: PURPLE })] }),
  new Paragraph({ alignment: AlignmentType.CENTER,
    border: { top: { style: BorderStyle.SINGLE, size: 12, color: ORANGE, space: 10 } },
    spacing: { before: 120, after: 240 }, children: [t('')] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 100 },
    children: [t('METRYCZKA  ·  KPOF  ·  WOPF  ·  IPET  ·  CELE SMART  ·  EWALUACJA', { bold: true, size: 22, color: ORANGE })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 400, line: 300 },
    children: [t('Szkolenie oparte na nowej podstawie programowej wychowania przedszkolnego', { size: 20, color: '4A4A4A' })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60, line: 300 },
    children: [t('(Dz.U. 2026 poz. 378) oraz na rozporządzeniu o ocenie funkcjonalnej', { size: 20, color: '4A4A4A' })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 500, line: 300 },
    children: [t('z 2 marca 2026 r. (Dz.U. 2026 poz. 428)', { size: 20, color: '4A4A4A' })] }),
);

add(new Paragraph({ spacing: { before: 200, after: 100 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: ORANGE, space: 5 } },
  children: [t('KARTA SZKOLENIA', { bold: true, size: 20, color: PURPLE, caps: true, sp: 14 })] }));
add(table(null, [
    ['Adresaci', 'Rada pedagogiczna przedszkola: nauczyciele wychowania przedszkolnego, nauczyciele współorganizujący kształcenie specjalne, specjaliści (psycholog, pedagog specjalny, logopeda, terapeuta SI), dyrektor.'],
    ['Forma', 'Szkolenie warsztatowe — wykład interaktywny, praca na autentycznych drukach, praca w zespołach 3–4-osobowych, kazusy.'],
    ['Czas trwania', '2 sesje po 4 jednostki dydaktyczne (2 × 180 min zajęć + przerwy) = 8 × 45 min. Wersja skrócona: 3 × 45 min — moduły M1, M4, M7.'],
    ['Cel główny', 'Uporządkowanie dokumentacji dziecka od pierwszego dnia września 2026 r. w logicznym ciągu: PRAWO → METRYCZKA → KPOF → OBSERWACJA POGŁĘBIONA → WOPF → IPET → CELE SMART → EWALUACJA → INFORMACJA DO PORADNI.'],
    ['Materiały', 'Metryczka dziecka 2026/27; KPOF wersja A (3–4 lata), B (5 lat), C (6 lat); druk WOPF; druk IPET; karta celów SMART; karta ewaluacji; wzór informacji o funkcjonowaniu dziecka. Załączniki Z1–Z8 do niniejszego scenariusza.'],
    ['Prowadzący', 'Dyrektor / pedagog specjalny / koordynator pomocy psychologiczno-pedagogicznej.'],
    ['Produkt szkolenia', 'Przyjęty przez radę pedagogiczną kalendarz dokumentacji na rok 2026/2027 (Załącznik Z6) oraz reguły uruchamiania obserwacji pogłębionej (Załącznik Z4).'],
], [1900, CONTENT - 1900], { boldCol0: true, zebra: true }));

add(pageBreak());

/* ============ SPIS / MAPA SZKOLENIA ============ */
add(H1('▌', 'Mapa szkolenia — przebieg dwóch sesji'));
add(p('Szkolenie prowadzi uczestników jedną linią: od przepisu, przez narzędzie obserwacyjne, do gotowego dokumentu i jego ewaluacji. Kolejność modułów nie jest dowolna — każdy kolejny moduł korzysta z produktu poprzedniego.'));

add(spacer(100));
add(H3('SESJA I  ·  PRAWO I WSPÓLNY JĘZYK  ·  4 × 45 min'));
add(table(['Moduł', 'Temat', 'Czas', 'Produkt modułu'], [
  ['M0', 'Otwarcie, kontrakt, diagnoza wstępna „co nas boli w dokumentacji”', '15 min', 'Lista problemów zespołu'],
  ['M1', 'Strażnik Prawa: co było, a co jest od 1 września 2026 r.', '60 min', 'Tabela porównawcza Z2 + karty Z1'],
  ['—', 'Przerwa', '10 min', '—'],
  ['M2', 'ICF — czym jest i dlaczego stał się językiem dokumentacji', '45 min', 'Ściąga ICF d1–d9 (Z3)'],
  ['—', 'Przerwa', '10 min', '—'],
  ['M3', 'Metryczka dziecka — pierwszy dokument września', '25 min', 'Uzupełniona metryczka wzorcowa'],
  ['M4', 'KPOF — budowa narzędzia, skala, siedem zasad obserwacji', '35 min', 'Zrozumienie arkusza A/B/C'],
], [900, CONTENT - 900 - 1000 - 2600, 1000, 2600], { boldCol0: true }));

add(spacer(160));
add(H3('SESJA II  ·  NARZĘDZIA I DOKUMENTY  ·  4 × 45 min'));
add(table(['Moduł', 'Temat', 'Czas', 'Produkt modułu'], [
  ['M5', 'KPOF w praktyce — liczenie wyniku, odczyt profilu, kwalifikacja', '35 min', 'Policzony profil dziecka'],
  ['M6', 'Obserwacja pogłębiona: ABC, profil sensoryczny, ToM — kiedy?', '45 min', 'Reguły przekierowania (Z4)'],
  ['—', 'Przerwa', '10 min', '—'],
  ['M7', 'WOPF i IPET oraz cele SMART — od danych do zobowiązania', '55 min', 'Trzy cele SMART na piśmie'],
  ['—', 'Przerwa', '10 min', '—'],
  ['M8', 'Ewaluacja — ile razy w roku i co po niej robimy', '20 min', 'Karta ewaluacji'],
  ['M9', 'Informacja o funkcjonowaniu dziecka dla poradni', '20 min', 'Szkic informacji'],
  ['M10', 'Kalendarz wdrożenia, przydział zadań, zamknięcie', '05 min', 'Kalendarz Z6 przyjęty'],
], [900, CONTENT - 900 - 1000 - 2600, 1000, 2600], { boldCol0: true }));

add(spacer(200));
add(box('ZASADA PROWADZĄCEGO', [
  p([t('Nie zaczynamy od druku. Zaczynamy od przepisu. ', { bold: true }),
     t('Nauczyciel, który wie, z czego wynika rubryka, wypełnia ją sensownie. Nauczyciel, który tego nie wie, wypełnia ją „żeby było”. Cała pierwsza sesja służy temu, by żaden druk omawiany w sesji drugiej nie był dla zespołu zagadką administracyjną.')]),
], { fill: LIGHTO, bar: ORANGE }));

add(pageBreak());

/* ============ M0 ============ */
add(modul('M0', 'Otwarcie, kontrakt i diagnoza wstępna', '15 min',
  'ustalić zasady pracy i zebrać realne trudności zespołu z dokumentacją'));
add(spacer(120));

add(H2('Przebieg'));
add(numItem([t('Powitanie i cel spotkania (2 min). ', { bold: true }), t('Prowadzący podaje jedno zdanie: „Wychodzimy z tego spotkania z kalendarzem dokumentacji na cały rok i z wiedzą, który przepis stoi za każdym drukiem”.')]));
add(numItem([t('Kontrakt (3 min). ', { bold: true }), t('Cztery zasady zapisane na flipcharcie: (a) nie oceniamy dotychczasowej dokumentacji kolegów, (b) mówimy o zachowaniach dzieci, nie o rodzinach, (c) telefony wyciszone — pracujemy na drukach, (d) każde pytanie o przepis jest dobre.')]));
add(numItem([t('Diagnoza wstępna — „trzy karteczki” (10 min). ', { bold: true }), t('Każdy uczestnik zapisuje na trzech karteczkach: 1) dokument, którego nie rozumiem; 2) dokument, który zajmuje mi najwięcej czasu; 3) pytanie, na które chcę dziś odpowiedź. Karteczki lądują na trzech arkuszach na ścianie. Prowadzący czyta na głos 5–6 z nich i zapowiada, w którym module padnie odpowiedź. Do arkuszy wracamy w module M10.')]));

add(spacer(140));
add(box('WSKAZÓWKA METODYCZNA', [
  p('Arkusz „pytania” jest kontraktem prowadzącego wobec rady. Jeżeli na koniec zostanie na nim pytanie bez odpowiedzi, prowadzący zapisuje je jako zadanie do wyjaśnienia z organem prowadzącym lub poradnią i podaje termin. Nie zostawiamy pytań bez losu — to najczęstsza przyczyna, dla której rada nie ufa kolejnym szkoleniom.'),
], { fill: LIGHT, bar: PURPLE }));

add(pageBreak());

/* ============ M1 STRAŻNIK PRAWA ============ */
add(modul('M1', 'Strażnik Prawa — co było, a co jest od 1 września 2026 r.', '60 min',
  'osadzić każdy druk w konkretnym przepisie i pokazać, co realnie się zmieniło'));
add(spacer(120));

add(p([t('Rola Strażnika Prawa. ', { bold: true }),
  t('W każdym module jedna osoba z zespołu pełni funkcję Strażnika Prawa. Jej zadaniem nie jest znać przepisy na pamięć, lecz zadawać jedno pytanie za każdym razem, gdy zespół podejmuje decyzję dokumentacyjną: '),
  t('„Z czego to wynika i gdzie to jest zapisane?”. ', { bold: true, i: true }),
  t('Strażnik ma prawo zatrzymać pracę zespołu do czasu wskazania podstawy. Funkcja jest rotacyjna — w ciągu roku pełni ją każdy nauczyciel. To najtańszy znany mechanizm chroniący przed dokumentacją tworzoną „z przyzwyczajenia”.')]));

add(H2('1.1  Sześć aktów prawnych, na których stoi teczka dziecka'));
add(p('Poniższe sześć pozycji wystarcza, by uzasadnić każdy dokument omawiany na tym szkoleniu. Uczestnicy otrzymują je jako Załącznik Z1 — karty Strażnika Prawa do laminowania i powieszenia w pokoju nauczycielskim.'));

add(spacer(120));
add(straznik(1, 'PODSTAWA PROGRAMOWA WYCHOWANIA PRZEDSZKOLNEGO', [
  p([t('Akt: ', { bold: true }), t('Rozporządzenie Ministra Edukacji z dnia 11 marca 2026 r. w sprawie podstawy programowej wychowania przedszkolnego oraz kształcenia ogólnego — '), t('Dz.U. 2026 poz. 378', { bold: true }), t('. Obowiązuje od 1 września 2026 r.')]),
  p([t('Co się zmieniło: ', { bold: true }), t('poprzednia podstawa (rozporządzenie MEN z 14 lutego 2017 r., Dz.U. 2017 poz. 356, załącznik nr 1) opisywała rozwój dziecka w czterech obszarach: fizycznym, emocjonalnym, społecznym i poznawczym. Nowa podstawa porządkuje osiągnięcia dziecka w dziewięciu obszarach: społecznym, osobistym, językowym, matematycznym, przyrodniczym, technicznym, cyfrowym, artystycznym i ruchowym, dodaje kategorię doświadczeń edukacyjnych oraz zadania przedszkola i warunki realizacji.')]),
  p([t('Ważne: ', { bold: true }), t('w przedszkolach nie ma wdrażania etapowego — od 1 września 2026 r. nowa podstawa obejmuje wszystkie grupy wiekowe jednocześnie.')]),
  p([t('Skutek dokumentacyjny: ', { bold: true }), t('każde narzędzie obserwacyjne używane w placówce musi odsyłać do punktów NOWEJ podstawy. Arkusze KPOF mają kolumnę „ICF · PP”, w której zapis w rodzaju „d130 · PP 9.1” oznacza: kod ICF oraz punkt podstawy w formacie obszar.punkt. Arkusze obserwacyjne z zeszłego roku, odsyłające do czterech starych obszarów, tracą aktualność.')]),
]));

add(spacer(140));
add(straznik(2, 'OCENA FUNKCJONALNA, ORZECZENIA I OPINIE PORADNI', [
  p([t('Akt: ', { bold: true }), t('Rozporządzenie Ministra Edukacji z dnia 2 marca 2026 r. w sprawie orzeczeń i opinii wydawanych przez zespoły orzekające działające w publicznych poradniach psychologiczno-pedagogicznych — '), t('Dz.U. 2026 poz. 428', { bold: true }), t(' (ogłoszone 30 marca 2026 r.). Zmiany dotyczące składów zespołów orzekających — od 1 kwietnia 2026 r.; ocena funkcjonalna — od 1 września 2026 r.')]),
  p([t('Co było: ', { bold: true }), t('na gruncie rozporządzenia MEN z 7 września 2017 r. (Dz.U. 2017 poz. 1743 ze zm.) przedszkole przekazywało poradni informacje o dziecku, ale bez ustawowo określonego standardu treści i bez wyznaczonego terminu. W praktyce była to dowolnie skonstruowana „opinia o dziecku”, często deficytowa i pisana w ostatniej chwili.')]),
  p([t('Co jest: ', { bold: true }), t('ocena funkcjonalna dziecka staje się obowiązkowym etapem procesu diagnostycznego poprzedzającego wydanie orzeczenia. Przedszkole ma obowiązek sporządzić i przekazać poradni ')  , t('informację o funkcjonowaniu dziecka', { bold: true }), t(' — dokument stanowiący element oceny funkcjonalnej. Informację przygotowuje się w terminie ')  , t('14 dni', { bold: true }), t(' od dnia otrzymania wystąpienia poradni. Informacja obejmuje trudności dziecka ORAZ jego mocne strony i uzdolnienia rozpoznane przez nauczycieli i specjalistów pracujących z dzieckiem. Uproszczono wzory orzeczeń i opinii; orzeczenie podpisują wszyscy członkowie zespołu orzekającego, zgodnie z wymogami Kodeksu postępowania administracyjnego.')]),
  p([t('Podział ról: ', { bold: true }), t('formalną ocenę funkcjonalną sporządza zespół działający w poradni. Rolą przedszkola pozostaje obserwacja dziecka w codziennych sytuacjach oraz opisanie jego aktywności, mocnych stron, trudności i efektów udzielanego wsparcia. Przedszkole nie stawia diagnoz — dostarcza rzetelnych danych z obserwacji.')]),
  p([t('Skutek dokumentacyjny: ', { bold: true }), t('czternastodniowy termin jest nie do dotrzymania, jeżeli obserwacja zaczyna się dopiero po wpłynięciu pisma z poradni. To jest właściwy powód, dla którego KPOF wypełniamy we wrześniu dla wszystkich dzieci — nie po to, by mieć arkusz w segregatorze, lecz po to, by w dowolnym momencie roku móc odpowiedzieć poradni w ciągu dwóch tygodni na podstawie danych, a nie wspomnień.')]),
]));

add(pageBreak());
add(straznik(3, 'POMOC PSYCHOLOGICZNO-PEDAGOGICZNA', [
  p([t('Akt: ', { bold: true }), t('Rozporządzenie Ministra Edukacji Narodowej z dnia 9 sierpnia 2017 r. w sprawie zasad organizacji i udzielania pomocy psychologiczno-pedagogicznej w publicznych przedszkolach, szkołach i placówkach — Dz.U. 2017 poz. 1591; tekst jednolity: '), t('Dz.U. 2023 poz. 1798', { bold: true }), t('.')]),
  p([t('Sprostowanie terminologiczne. ', { bold: true, color: ORANGE }), t('W obiegu funkcjonuje potoczne określenie „rozporządzenie z 23 lipca 2023 r.”. Aktu o takiej dacie nie ma. Tekst jednolity ogłoszono obwieszczeniem Ministra Edukacji i Nauki z dnia 25 lipca 2023 r., opublikowanym 5 września 2023 r. pod pozycją 1798. W dokumentacji dziecka powołujemy się na: „rozporządzenie MEN z dnia 9 sierpnia 2017 r. … (tekst jedn. Dz.U. z 2023 r. poz. 1798)”. Data obwieszczenia nie jest datą rozporządzenia — to typowy i łatwy do wychwycenia błąd w podstawach prawnych IPET-ów.')]),
  p([t('Co z tego wynika dla przedszkola: ', { bold: true }), t('pomoc psychologiczno-pedagogiczna jest udzielana z inicjatywy m.in. nauczyciela i rodzica; nauczyciele i specjaliści rozpoznają indywidualne potrzeby rozwojowe i edukacyjne dziecka oraz jego możliwości psychofizyczne, prowadzą obserwację pedagogiczną i informują dyrektora o potrzebie objęcia dziecka pomocą. W przedszkolu pomoc udzielana jest w trakcie bieżącej pracy oraz w formach określonych rozporządzeniem (m.in. zajęcia rozwijające uzdolnienia, zajęcia specjalistyczne: korekcyjno-kompensacyjne, logopedyczne, rozwijające kompetencje emocjonalno-społeczne oraz inne o charakterze terapeutycznym, zajęcia z zakresu wczesnego wspomagania w odrębnym trybie, porady i konsultacje dla rodziców).')]),
  p([t('Kluczowe dla ewaluacji: ', { bold: true }), t('nauczyciele i specjaliści oceniają efektywność udzielanej pomocy i formułują wnioski dotyczące dalszych działań; jeżeli mimo udzielanej pomocy nie następuje poprawa funkcjonowania dziecka, dyrektor — za zgodą rodziców — występuje do poradni psychologiczno-pedagogicznej o przeprowadzenie diagnozy. To właśnie ta ścieżka spina KPOF z modułami pogłębionymi i z wnioskiem do poradni.')]),
]));

add(spacer(140));
add(straznik(4, 'KSZTAŁCENIE SPECJALNE — WOPFU I IPET', [
  p([t('Akt: ', { bold: true }), t('Rozporządzenie Ministra Edukacji Narodowej z dnia 9 sierpnia 2017 r. w sprawie warunków organizowania kształcenia, wychowania i opieki dla dzieci i młodzieży niepełnosprawnych, niedostosowanych społecznie i zagrożonych niedostosowaniem społecznym — Dz.U. 2017 poz. 1578; tekst jednolity: '), t('Dz.U. 2020 poz. 1309', { bold: true }), t(' ze zm.')]),
  p([t('Co z niego bierzemy wprost: ', { bold: true }), t('obowiązek opracowania indywidualnego programu edukacyjno-terapeutycznego (IPET) dla dziecka posiadającego orzeczenie o potrzebie kształcenia specjalnego; obowiązek dokonywania przez zespół ')  , t('wielospecjalistycznej oceny poziomu funkcjonowania (WOPFU) co najmniej dwa razy w roku szkolnym', { bold: true }), t('; obowiązkową zawartość IPET (zakres i sposób dostosowania wymagań, zintegrowane działania nauczycieli i specjalistów, formy i okres udzielanego wsparcia oraz wymiar godzin, działania wspierające rodziców, zakres współpracy, rodzaj i sposób dostosowania warunków); udział rodziców w pracach zespołu oraz prawo do otrzymania kopii dokumentów.')]),
  p([t('Terminy opracowania IPET: ', { bold: true }), t('program opracowuje się na okres, na jaki wydano orzeczenie, nie dłuższy niż etap edukacyjny — w terminie do 30 września roku szkolnego, w którym dziecko rozpoczyna kształcenie, albo w terminie 30 dni od dnia złożenia w przedszkolu orzeczenia o potrzebie kształcenia specjalnego. Ten drugi termin dotyczy każdego orzeczenia, które wpływa w ciągu roku — także w maju.')]),
  p([t('Uwaga nazewnicza: ', { bold: true, color: ORANGE }), t('przepis posługuje się skrótem WOPFU (wielospecjalistyczna ocena poziomu funkcjonowania ucznia). W dokumentacji przedszkolnej EduPlaner używana jest robocza nazwa WOPF, ponieważ w przedszkolu mówimy o dziecku, nie o uczniu. Nazwa robocza jest dopuszczalna wewnętrznie, ale ')  , t('w dokumencie wpinanym do teczki dziecka należy zachować pełną nazwę ustawową albo wprost wskazać jej równoważność', { bold: true }), t(' (np. w nagłówku: „Wielospecjalistyczna ocena poziomu funkcjonowania dziecka (WOPF / WOPFU)”). Organ nadzoru sprawdza zgodność z nazwą z rozporządzenia.')]),
]));

add(pageBreak());
add(straznik(5, 'DOKUMENTACJA PRZEBIEGU WYCHOWANIA PRZEDSZKOLNEGO', [
  p([t('Akt: ', { bold: true }), t('Rozporządzenie Ministra Edukacji Narodowej z dnia 25 sierpnia 2017 r. w sprawie sposobu prowadzenia przez publiczne przedszkola, szkoły i placówki dokumentacji przebiegu nauczania, działalności wychowawczej i opiekuńczej — Dz.U. 2017 poz. 1646 ze zm.')]),
  p([t('Co z niego wynika: ', { bold: true }), t('przedszkole prowadzi księgę dzieci, dzienniki zajęć przedszkola, dzienniki zajęć specjalistycznych oraz dokumentację badań i czynności uzupełniających prowadzonych w szczególności przez psychologa, pedagoga, logopedę i innych specjalistów. To w tej ostatniej kategorii mieszczą się arkusze obserwacji, w tym KPOF i moduły pogłębione.')]),
  p([t('Uczciwe rozróżnienie — powiedzieć radzie wprost: ', { bold: true, color: ORANGE }), t('metryczka dziecka nie jest dokumentem wymienionym z nazwy w rozporządzeniu. Jest ')  , t('dokumentem pomocniczym placówki', { bold: true }), t(', porządkującym dane, które i tak musimy posiadać z innych tytułów (rekrutacja, upoważnienia do odbioru, dane o zdrowiu, ewidencja dokumentów wsparcia). Nie mówimy nauczycielom, że „prawo nakazuje metryczkę”, bo to nieprawda i podważa wiarygodność pozostałych argumentów. Mówimy: metryczka jest narzędziem wewnętrznym, wprowadzonym zarządzeniem dyrektora, które chroni nas przed rozproszeniem danych po siedmiu segregatorach.')]),
]));

add(spacer(140));
add(straznik(6, 'OCHRONA DANYCH I PRZECHOWYWANIE DOKUMENTACJI', [
  p([t('Akty: ', { bold: true }), t('rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 (RODO) — w szczególności art. 6 ust. 1 lit. c i e oraz art. 9 ust. 2 lit. g; ustawa z dnia 14 grudnia 2016 r. — Prawo oświatowe; ustawa z dnia 14 lipca 1983 r. o narodowym zasobie archiwalnym i archiwach wraz z instrukcją kancelaryjną i jednolitym rzeczowym wykazem akt przyjętym w placówce.')]),
  p([t('Trzy zdania, które muszą wybrzmieć na szkoleniu: ', { bold: true }), t('(1) dane o zdrowiu i rozwoju dziecka są danymi szczególnej kategorii z art. 9 RODO — teczka dziecka nie leży na parapecie i nie jeździ do domu nauczyciela; (2) klauzula informacyjna z metryczki musi być realnie podpisana przez rodzica, a nie tylko wydrukowana; (3) zakres danych zbieranych w metryczce musi być adekwatny — pytamy tylko o to, co jest nam potrzebne do realizacji zadań dydaktycznych, wychowawczych i opiekuńczych oraz do organizacji pomocy psychologiczno-pedagogicznej.')]),
  p([t('Praktyka: ', { bold: true }), t('każda placówka wskazuje w zarządzeniu dyrektora miejsce przechowywania teczek, osobę odpowiedzialną i zasady udostępniania — w tym poradni psychologiczno-pedagogicznej, organowi prowadzącemu i organowi nadzoru.')]),
]));

add(pageBreak());

/* ---- TABELA PORÓWNAWCZA ---- */
add(H2('1.2  Tabela porównawcza — co było i co jest'));
add(p('Tabela jest sercem modułu M1 i jednocześnie Załącznikiem Z2. Prowadzący wyświetla ją w całości, następnie omawia wiersz po wierszu, za każdym razem pytając zespół: „co to zmienia w naszym kalendarzu?”.'));
add(spacer(100));
add(table(['Obszar', 'Stan do 31.08.2026 r.', 'Stan od 1.09.2026 r.', 'Co robimy inaczej'], [
  ['Podstawa programowa',
   '4 obszary rozwoju: fizyczny, emocjonalny, społeczny, poznawczy (rozp. MEN z 14.02.2017, Dz.U. 2017 poz. 356).',
   '9 obszarów: społeczny, osobisty, językowy, matematyczny, przyrodniczy, techniczny, cyfrowy, artystyczny, ruchowy; doświadczenia edukacyjne (rozp. z 11.03.2026, Dz.U. 2026 poz. 378).',
   'Wymieniamy odsyłacze w arkuszach obserwacji na nowe punkty PP. KPOF ma je już wpisane w kolumnie „ICF · PP”.'],
  ['Wdrożenie podstawy',
   '—',
   'Bez etapowania — wszystkie grupy wiekowe od 1.09.2026 r.',
   'Nie ma grup „na starych zasadach”. Jeden komplet narzędzi dla całego przedszkola.'],
  ['Ocena funkcjonalna',
   'Pojęcie nieobecne w przepisach o orzecznictwie; poradnia diagnozowała bez ustawowego udziału przedszkola.',
   'Obowiązkowy etap procesu diagnostycznego przed wydaniem orzeczenia (rozp. z 02.03.2026, Dz.U. 2026 poz. 428).',
   'Obserwacja przedszkolna przestaje być dobrą praktyką, a staje się wkładem do procedury administracyjnej.'],
  ['Informacja przedszkola dla poradni',
   'Dowolna „opinia o dziecku”, bez standardu treści i bez terminu.',
   'Informacja o funkcjonowaniu dziecka — element oceny funkcjonalnej; obowiązek sporządzenia i przekazania; 14 dni od otrzymania wystąpienia; obligatoryjnie trudności ORAZ mocne strony i uzdolnienia.',
   'Wprowadzamy jeden wzór dla całej placówki i procedurę obiegu. Dane bierzemy z KPOF, nie z pamięci.'],
  ['Zespoły orzekające',
   'Dotychczasowe składy i wzory orzeczeń.',
   'Nowe składy zespołów (od 01.04.2026), uproszczone wzory orzeczeń i opinii, orzeczenie podpisywane przez wszystkich członków zespołu (k.p.a.).',
   'Sprawdzamy, czy orzeczenia wpływające po 1 kwietnia 2026 r. mają nowy układ — inaczej wypełnia się z nich WOPF.'],
  ['Pomoc psychologiczno-pedagogiczna',
   'Rozp. MEN z 09.08.2017, Dz.U. 2017 poz. 1591.',
   'Ten sam akt — tekst jednolity Dz.U. 2023 poz. 1798. Zasady bez zmian.',
   'Poprawiamy podstawę prawną w szablonach: cytujemy tekst jednolity z 2023 r., nie datę obwieszczenia.'],
  ['WOPFU i IPET',
   'Rozp. MEN z 09.08.2017, tekst jedn. Dz.U. 2020 poz. 1309.',
   'Bez zmian co do konstrukcji dokumentów — zmienia się źródło danych wejściowych (ocena funkcjonalna, ICF).',
   'IPET zostaje w dotychczasowym kształcie, ale WOPF pisany jest językiem funkcjonalnym, nie deficytowym.'],
  ['Język opisu dziecka',
   'Opis potoczny lub diagnostyczny, często deficytowy: „nie potrafi”, „słabo”, „ma problemy”.',
   'Opis funkcjonalny w paradygmacie ICF: co dziecko robi, w jakiej sytuacji, z jakim wsparciem, co ułatwia, co utrudnia.',
   'Cała sesja II jest treningiem tego języka.'],
], [1450, 2500, 2900, CONTENT - 1450 - 2500 - 2900], { boldCol0: true }));

add(spacer(180));
add(cw('SĄD NAD DOKUMENTEM  ·  20 min  ·  zespoły 3–4-osobowe', [
  p([t('Materiał: ', { bold: true }), t('prowadzący rozdaje trzy anonimowe fragmenty dokumentacji z lat ubiegłych (zanonimizowane, za zgodą dyrektora) — fragment WOPF, fragment IPET z celami i fragment opinii do poradni.')]),
  p([t('Zadanie: ', { bold: true }), t('każdy zespół pracuje w trzech rolach. ')  ,
     t('Strażnik Prawa ', { bold: true }), t('szuka podstawy: który przepis wymaga tego zapisu i czy jest on poprawnie zacytowany. '),
     t('Adwokat dziecka ', { bold: true }), t('sprawdza, czy z dokumentu da się wyczytać, co dziecko potrafi, a nie tylko czego nie potrafi. '),
     t('Kontroler ', { bold: true }), t('zaznacza każdy zapis, którego nie da się sprawdzić (np. „poprawa funkcjonowania”, „większa samodzielność”).')]),
  p([t('Efekt: ', { bold: true }), t('każdy zespół przedstawia jedno zdanie z dokumentu w wersji „było” i „poprawiamy tak”. Prowadzący zapisuje poprawki — wracamy do nich w module M7 przy celach SMART.')]),
  p([t('Uwaga: ', { bold: true }), t('ćwiczenie ma sens tylko przy zachowaniu zasady z kontraktu — nie szukamy autora, szukamy wzorca błędu.')]),
]));

module.exports = C;
