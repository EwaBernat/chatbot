const G = require('./gen.js');
const { Paragraph, AlignmentType, BorderStyle, t, p, H1, H2, H3, bullet, numItem, spacer,
        pageBreak, box, table, modul, straznik, cw, CONTENT, PURPLE, ORANGE, LIGHT, LIGHTO } = G;

const C = [];
const add = (...x) => x.forEach(e => C.push(e));

add(pageBreak());

/* ============ M7 WOPF + IPET + SMART ============ */
add(modul('M7', 'WOPF i IPET oraz cele SMART — od danych do zobowiązania', '55 min',
  'przejść całą ścieżkę od arkusza obserwacji do mierzalnego celu w programie'));
add(spacer(120));

add(H2('7.1  Ścieżka danych — jeden obieg, sześć przystanków'));
add(p('Najważniejszy komunikat całego szkolenia: żaden z tych dokumentów nie powstaje osobno. Każdy bierze dane z poprzedniego. Jeżeli którykolwiek przystanek wypadnie, kolejny trzeba wypełniać z pamięci — i wtedy zaczyna się dokumentacja pozorna.'));
add(spacer(60));
add(table(['#', 'Przystanek', 'Skąd bierze dane', 'Co przekazuje dalej'], [
  ['1', 'METRYCZKA', 'Rodzic, rekrutacja, dokumenty wsparcia.', 'Dane formalne, sygnały zdrowotne (reguła R4), informację o orzeczeniu i datę jego złożenia.'],
  ['2', 'KPOF', 'Niezależna obserwacja nauczyciela, rodzica i specjalisty przez 2–4 tygodnie.', 'Profil funkcjonowania w 9 obszarach ICF, poziom wsparcia, listę twierdzeń 1–2.'],
  ['3', 'MODUŁ POGŁĘBIONY', 'Reguły R1–R6 uruchomione wynikiem KPOF.', 'Odpowiedź na pytanie „dlaczego”: funkcję zachowania, wzorzec sensoryczny albo opis rozumienia stanów umysłu.'],
  ['4', 'WOPF', 'KPOF + moduły + orzeczenie/opinia + informacje rodziców + wyniki dotychczasowego wsparcia.', 'Uporządkowany opis mocnych stron, trudności, barier i ułatwień — językiem funkcjonalnym.'],
  ['5', 'IPET', 'WOPF — wprost, zdanie po zdaniu.', 'Cele SMART, dostosowania, formy i wymiar wsparcia, zintegrowane działania, zakres współpracy z rodzicami.'],
  ['6', 'EWALUACJA', 'Wskaźniki wpisane wcześniej do celów SMART.', 'Decyzję: kontynuujemy, modyfikujemy, kończymy albo występujemy do poradni. Wraca do przystanku 4.'],
], [500, 1700, 3300, CONTENT - 500 - 1700 - 3300], { boldCol0: true }));

add(spacer(150));
add(H2('7.2  WOPF — zasadność i zawartość'));
add(p([t('Podstawa: ', { bold: true }), t('rozporządzenie MEN z dnia 9 sierpnia 2017 r. (tekst jedn. Dz.U. 2020 poz. 1309). Wielospecjalistycznej oceny poziomu funkcjonowania dokonuje zespół ')  , t('co najmniej dwa razy w roku szkolnym', { bold: true }), t('. Ocena jest podstawą opracowania i modyfikacji IPET.')]));
add(spacer(60));
add(H3('Po co nam WOPF — cztery odpowiedzi dla sceptyka'));
add(bullet([t('Bo bez niej IPET jest zgadywanką. ', { bold: true }), t('Cel można postawić tylko wtedy, gdy wiadomo, od jakiego punktu startujemy. WOPF wyznacza punkt startu i jednocześnie punkt odniesienia dla ewaluacji.')]));
add(bullet([t('Bo scala perspektywy. ', { bold: true }), t('Nauczyciel, logopeda, psycholog i rodzic widzą inne dziecko. WOPF jest jedynym dokumentem, w którym te obrazy stają się jednym.')]));
add(bullet([t('Bo chroni dziecko przed etykietą. ', { bold: true }), t('Orzeczenie mówi, co dziecku przysługuje. WOPF mówi, jak dziecko funkcjonuje. Dwoje dzieci z tym samym orzeczeniem ma dwa zupełnie różne WOPF-y — i dwa różne IPET-y.')]));
add(bullet([t('Bo jest dowodem pracy przedszkola. ', { bold: true }), t('W razie kontroli, sporu z rodzicem lub wystąpienia do poradni to WOPF pokazuje, co i z jakim skutkiem robiliśmy.')]));
add(spacer(80));
add(H3('Zawartość WOPF — siedem bloków'));
add(table(['Blok', 'Treść', 'Źródło'], [
  ['1. Mocne strony i zasoby', 'Co dziecko robi samodzielnie i pewnie; zainteresowania; co je motywuje.', 'KPOF: twierdzenia ocenione na 5 i obszary z kwalifikacją „zasób”.'],
  ['2. Funkcjonowanie w obszarach', 'Opis w 9 obszarach ICF — co robi, w jakiej sytuacji, z jakim wsparciem.', 'KPOF: średnie obszarów + obserwacje jakościowe.'],
  ['3. Trudności i ich uwarunkowania', 'Konkretne zachowania, ich częstotliwość i kontekst — bez etykiet.', 'KPOF: twierdzenia 1–2 + moduł pogłębiony.'],
  ['4. Bariery i ułatwienia w środowisku', 'Co w sali, w rytmie dnia, w grupie utrudnia, a co ułatwia funkcjonowanie.', 'Komponent „e” ICF; analiza ABC; obserwacja sensoryczna.'],
  ['5. Efekty dotychczasowego wsparcia', 'Co robiliśmy, jak długo, z jakim skutkiem — z liczbami.', 'Poprzednia ewaluacja; dzienniki zajęć specjalistycznych.'],
  ['6. Potrzeby rozwojowe i edukacyjne', 'Czego dziecko potrzebuje, żeby uczestniczyć — nie czego mu brakuje.', 'Synteza bloków 2–5.'],
  ['7. Wnioski i rekomendacje', 'Kierunki pracy, propozycje form pomocy, ewentualne wystąpienie do poradni.', 'Ustalenia zespołu z udziałem rodzica.'],
], [2100, 4000, CONTENT - 2100 - 4000], { boldCol0: true }));

add(pageBreak());
add(H2('7.3  IPET — zasadność i terminy'));
add(p([t('Podstawa: ', { bold: true }), t('rozporządzenie MEN z dnia 9 sierpnia 2017 r. (tekst jedn. Dz.U. 2020 poz. 1309). IPET opracowuje się dla dziecka posiadającego ')  , t('orzeczenie o potrzebie kształcenia specjalnego', { bold: true }), t(' — i tylko dla takiego dziecka. Dziecko z opinią poradni albo objęte pomocą p-p bez orzeczenia nie ma IPET; ma pomoc psychologiczno-pedagogiczną dokumentowaną w inny sposób. To rozróżnienie musi być na szkoleniu powiedziane wprost, bo jest źródłem połowy błędów formalnych.')]));
add(spacer(60));
add(table(['Termin', 'Zdarzenie'], [
  ['do 30 września', 'Opracowanie IPET dla dziecka, które rozpoczyna kształcenie w przedszkolu z orzeczeniem złożonym przed rozpoczęciem roku.'],
  ['30 dni', 'Opracowanie IPET od dnia złożenia w przedszkolu orzeczenia o potrzebie kształcenia specjalnego — dotyczy każdego orzeczenia wpływającego w trakcie roku, także w maju.'],
  ['co najmniej 2 razy w roku', 'Wielospecjalistyczna ocena poziomu funkcjonowania — podstawa modyfikacji IPET.'],
  ['okres orzeczenia', 'Czas, na jaki opracowuje się program — nie dłużej niż etap edukacyjny.'],
], [2300, CONTENT - 2300], { boldCol0: true }));
add(spacer(80));
add(p([t('Prawa rodzica — trzy rzeczy, o których zapominamy: ', { bold: true }), t('rodzice mają prawo uczestniczyć w spotkaniach zespołu, mają prawo otrzymać kopię IPET i kopię wielospecjalistycznej oceny, a dyrektor zawiadamia ich o terminie spotkania w sposób przyjęty w placówce. Brak zawiadomienia jest uchybieniem formalnym niezależnie od tego, czy rodzic i tak by nie przyszedł.')]));

add(spacer(140));
add(H3('Co musi być w IPET — zalecenia z orzeczenia i z WOPF'));
add(p([t('§ 6 rozporządzenia (Dz.U. 2020 poz. 1309): ', { bold: true }), t('zespół opracowuje program po dokonaniu wielospecjalistycznej oceny poziomu funkcjonowania, uwzględniając diagnozę i wnioski sformułowane na jej podstawie oraz zalecenia zawarte w orzeczeniu o potrzebie kształcenia specjalnego. W praktyce: do IPET wpisujemy zalecenia poradni z orzeczenia jedno po drugim, a przy każdym — sposób realizacji (forma, kto, wymiar, od kiedy). To samo robimy z zaleceniami z WOPF. Orzeczenie mówi, co dziecku zalecono; WOPF mówi, co widzimy w przedszkolu; IPET pokazuje, jak jedno i drugie zamieniamy w działanie, a karta ewaluacji — czy zadziałało.')]));
add(table(['Element IPET (§ 6)', 'Skąd bierzemy', 'Jak zapisujemy'], [
  ['Zalecenia z orzeczenia i ich realizacja', 'orzeczenie poradni', 'tabela: zalecenie → forma realizacji → kto → wymiar → od kiedy → ocena realizacji'],
  ['Zalecenia z WOPF i ich realizacja', 'blok 7 WOPF (wnioski i rekomendacje)', 'to samo — każde zalecenie ma swój wiersz i swojego właściciela'],
  ['Zakres i sposób dostosowania wymagań i warunków', 'blok 4 WOPF (bariery i ułatwienia)', 'dostosowanie = odpowiedź na konkretną barierę z WOPF'],
  ['Zintegrowane działania nauczycieli i specjalistów', 'cele SMART z IPET', 'jeden cel, jeden plan, wiele rąk — kto, co, kiedy'],
  ['Formy i okres pomocy p-p, zajęcia rewalidacyjne, wsparcie rodziców', 'orzeczenie + WOPF', 'wymiar godzin, prowadzący, okres'],
], [3000, 2600, CONTENT - 3000 - 2600], { boldCol0: true }));
add(spacer(100));
add(H3('Dostosowania w przedszkolu — zmieniamy JAK, nie CZEGO'));
add(p('Podstawa programowa pozostaje ta sama. Dostosowanie to zmiana sposobu, w jaki dziecko dociera do treści i pokazuje, co umie:'));
add(bullet([t('Sposób podania: ', { bold: true }), t('polecenie krótkie, poparte gestem i obrazkiem; jedna instrukcja naraz; modelowanie.')]));
add(bullet([t('Czas: ', { bold: true }), t('dłuższa chwila na reakcję, dodatkowa próba, przewidywalne przejścia między aktywnościami.')]));
add(bullet([t('Przestrzeń: ', { bold: true }), t('miejsce w kole blisko nauczyciela, kącik wyciszenia, wizualny plan dnia, ograniczenie bodźców.')]));
add(bullet([t('Sposób sprawdzania: ', { bold: true }), t('dziecko pokazuje zamiast mówić, wskazuje obrazek, wykonuje zamiast opowiadać.')]));
add(bullet([t('Pomoce: ', { bold: true }), t('sztućce z grubym uchwytem, słuchawki wyciszające, obrazki do komunikacji (AAC), podkładki antypoślizgowe.')]));
add(p([t('Zasada: ', { bold: true }), t('każde dostosowanie ma źródło w WOPF — w barierze, którą tam opisaliśmy. Dostosowanie bez bariery jest przypadkowe; bariera bez dostosowania jest zaniechaniem.')]));
add(spacer(100));
add(H3('Zintegrowane działania nauczycieli i specjalistów — jak to wygląda w przedszkolu'));
add(bullet('Jeden zestaw celów SMART z IPET dla wszystkich: logopeda, psycholog, terapeuta i nauczyciel grupy pracują nad tymi samymi celami, każdy w swoim czasie i swoimi metodami.'));
add(bullet('Strategia z gabinetu przechodzi do sali i do domu: jeśli logopeda uczy dziecko prosić gestem o picie, nauczycielka honoruje ten gest przy śniadaniu, a rodzice w domu.'));
add(bullet('Stały rytm spotkań zespołu (np. co 6 tygodni, 20 minut), wspólny zeszyt komunikacji w teczce dziecka, jedna karta ewaluacji (Z5) dla wszystkich prowadzących.'));
add(bullet('Żaden specjalista nie prowadzi celów w oderwaniu od IPET — zajęcia specjalistyczne realizują program, a nie własny plan.'));
add(spacer(100));
add(H3('Sala pod nową podstawę programową (Dz.U. 2026 poz. 378)'));
add(p('Podstawa opisuje osiągnięcia dziecka w dziewięciu obszarach i kładzie nacisk na doświadczenia edukacyjne. Przestrzeń sali ma to umożliwiać — i jednocześnie realizować dostosowania z IPET:'));
add(bullet('Wyraźne strefy: ruch · zabawa tematyczna · badanie przyrody i techniki · książka i język · sztuka · kącik wyciszenia.'));
add(bullet('Materiały dostępne na wysokości dziecka i opisane obrazkiem — dziecko samo wybiera i odkłada.'));
add(bullet('Wizualny plan dnia; miejsce w kole i przy stoliku dobrane do potrzeb sensorycznych.'));
add(bullet('Hałas i światło pod kontrolą — to najczęstsze bariery środowiskowe w ocenie według ICF.'));
add(p([t('Uniwersalne projektowanie: ', { bold: true }), t('sala urządzona tak, że dostosowanie dla jednego dziecka jest dobrym środowiskiem dla całej grupy.')]));

add(spacer(150));
add(H2('7.4  Cele SMART — dlaczego przez nie realizujemy IPET'));
add(p([t('Zapis „rozwijanie samodzielności” nie jest celem. Jest życzeniem. Nie da się go zrealizować, bo nie wiadomo, co miałoby się stać, i nie da się go zewaluować, bo nie wiadomo, po czym poznamy, że się stało. ')  , t('Cel SMART jest jedynym formatem, który jednocześnie planuje działanie i przygotowuje ewaluację', { bold: true }), t(' — kryterium mierzalności zapisane w celu jest gotowym wskaźnikiem w karcie ewaluacji. To jest cała odpowiedź na pytanie, po co komu SMART w IPET.')]));
add(spacer(60));
add(table(['Litera', 'Kryterium', 'Pytanie kontrolne', 'W praktyce przedszkolnej'], [
  ['S', 'Konkretny (Specific)', 'Jakie dokładnie zachowanie i w jakiej sytuacji?', 'Nie „samoobsługa”, lecz „zakłada buty na rzepy w szatni przed wyjściem na dwór”.'],
  ['M', 'Mierzalny (Measurable)', 'Ile razy z ilu prób i przy jakim poziomie wsparcia?', '„W 4 z 5 kolejnych dni, przy jednej podpowiedzi słownej.” Poziom wsparcia jest miarą równie dobrą jak liczba powtórzeń.'],
  ['A', 'Osiągalny (Achievable)', 'Czy to jest jeden krok od tego, co dziecko robi dziś?', 'Punktem wyjścia jest ocena z KPOF. Cel przesuwa dziecko z 2 na 3 albo z 3 na 4 — nigdy z 1 na 5.'],
  ['R', 'Istotny (Relevant)', 'Czy ten cel zwiększa uczestnictwo dziecka i wynika z WOPF?', 'Cel musi dać się wskazać palcem w WOPF. Cel bez źródła w WOPF jest celem wymyślonym.'],
  ['T', 'Określony w czasie (Time-bound)', 'Do kiedy i kiedy sprawdzamy?', 'Data osiągnięcia + data pomiaru pośredniego. Domyślnie: pomiar w terminie najbliższej WOPF.'],
], [700, 2200, 2400, CONTENT - 700 - 2200 - 2400], { boldCol0: true }));

add(spacer(140));
add(box('FORMUŁA CELU — DO PRZEPISANIA NA TABLICĘ', [
  p([t('[Imię dziecka] w [konkretna sytuacja / miejsce / pora dnia] będzie [obserwowalne zachowanie] w [kryterium ilościowe: ile razy z ilu prób] przy [poziom wsparcia] w terminie do [data]; pomiar: [narzędzie / kto i jak sprawdza].', { bold: true, size: 21 })]),
  p('Cel, który nie mieści się w tej formule, nie jest gotowy. Nauczyciel, który nie potrafi wypełnić nawiasu „pomiar”, nie postawił celu — postawił intencję.'),
], { fill: LIGHT, bar: PURPLE }));

add(pageBreak());
add(H2('7.5  Warsztat: sześć celów przed i po'));
add(table(['Cel „życzeniowy” — do wyrzucenia', 'Cel SMART — do wpisania do IPET'], [
  ['Rozwijanie samodzielności w czynnościach samoobsługowych.',
   'Zosia podczas przygotowania do wyjścia na dwór założy samodzielnie buty na rzepy w 4 z 5 kolejnych dni, przy najwyżej jednej podpowiedzi słownej, w terminie do 19.12.2026. Pomiar: karta obserwacji szatni prowadzona przez nauczyciela grupy.'],
  ['Poprawa komunikacji.',
   'Antek podczas śniadania i podwieczorku poprosi o dokładkę, wskazując symbol na tablicy komunikacyjnej, w 3 z 5 posiłków tygodniowo, przy modelowaniu przez dorosłego, w terminie do 30.01.2027. Pomiar: tygodniowa karta zliczeń prowadzona przez nauczyciela i logopedę.'],
  ['Wydłużenie koncentracji uwagi.',
   'Marysia podczas zajęć przy stoliku w małej grupie (do 4 dzieci) pozostanie przy zadaniu przez 8 minut bez opuszczania miejsca, w 3 z 4 zajęć w tygodniu, przy uprzedzeniu o czasie trwania i użyciu klepsydry, do 27.02.2027. Pomiar: zapis czasu w karcie obserwacji.'],
  ['Eliminowanie zachowań agresywnych.',
   'Kuba w sytuacji oczekiwania w kolejce do łazienki użyje karty „czekam” zamiast uderzenia rówieśnika — w 4 z 5 zaobserwowanych sytuacji tygodniowo, przy obecności dorosłego w zasięgu wzroku, do 27.03.2027. Pomiar: karta ABC prowadzona przez wszystkie osoby pracujące z dzieckiem.'],
  ['Rozwijanie umiejętności społecznych.',
   'Lena podejmie wspólną zabawę w parze z wyznaczonym rówieśnikiem, przyjmując przydzieloną rolę, przez co najmniej 5 minut, w 3 z 5 dni w tygodniu, przy wprowadzeniu do zabawy przez dorosłego, do 30.04.2027. Pomiar: karta obserwacji zabawy swobodnej.'],
  ['Usprawnianie motoryki małej.',
   'Filip w zajęciach plastycznych chwyci kredkę chwytem trójpalcowym i pokoloruje pole o wymiarach ok. 5 × 5 cm bez wychodzenia poza kontur w 3 z 5 prac tygodniowo, przy nasadce na kredkę i pochylonej podkładce, do 20.03.2027. Pomiar: teczka prac z datami.'],
], [3000, CONTENT - 3000]));

add(spacer(150));
add(cw('NAPISZ TRZY CELE  ·  25 min  ·  zespoły 3-osobowe', [
  p([t('Materiał wejściowy: ', { bold: true }), t('trzy wnioski zespołowe zapisane na flipcharcie w module M5 (kazusy A, B, C) oraz formuła celu z ramki 7.4.')]),
  p([t('Zadanie: ', { bold: true }), t('każdy zespół pisze trzy cele SMART dla swojego kazusu — po jednym z obszaru najsłabszego, jednym z obszaru granicznego i jednym wykorzystującym zasób dziecka jako dźwignię. Cele zapisujemy na kartach A5 dużymi literami.')]),
  p([t('Kontrola krzyżowa (10 min): ', { bold: true }), t('zespoły wymieniają się kartami. Zespół sprawdzający przykłada do każdego celu pięć pytań kontrolnych z tabeli 7.4 i zaznacza literę, której cel nie spełnia. Najczęściej brakuje ')  , t('M', { bold: true }), t(' (nie ma liczby) oraz ')  , t('R', { bold: true }), t(' (nie da się wskazać źródła w WOPF).')]),
  p([t('Zamknięcie: ', { bold: true }), t('poprawione cele zostają na ścianie do końca szkolenia — w module M8 dopisujemy do nich wskaźniki ewaluacyjne, a w M9 wykorzystujemy je jako materiał do informacji dla poradni. To ten sam materiał niesiony przez trzy moduły; uczestnicy widzą wtedy, że dokumentacja jest jednym obiegiem, a nie zbiorem druków.')]),
]));

module.exports = C;
