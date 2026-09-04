const G = require('./gen.js');
const { Paragraph, AlignmentType, BorderStyle, t, p, H1, H2, H3, bullet, numItem, spacer,
        pageBreak, box, table, modul, straznik, cw, CONTENT, PURPLE, ORANGE, LIGHT, LIGHTO } = G;

const C = [];
const add = (...x) => x.forEach(e => C.push(e));

add(pageBreak());

/* ============ M8 EWALUACJA ============ */
add(modul('M8', 'Ewaluacja — ile razy w roku i co po niej robimy', '20 min',
  'ustalić częstotliwość, wskaźniki i konsekwencje ewaluacji'));
add(spacer(120));

add(H2('8.1  Ile razy w roku — odpowiedź wprost, dokument po dokumencie'));
add(p('To pytanie pada najczęściej i najczęściej otrzymuje odpowiedź „to zależy”. Poniżej odpowiedź konkretna, z rozróżnieniem na to, co wynika z przepisu, i to, co jest decyzją placówki.'));
add(spacer(60));
add(table(['Dokument / działanie', 'Ile razy w roku', 'Kiedy', 'Źródło obowiązku'], [
  ['WOPF (wielospecjalistyczna ocena poziomu funkcjonowania)',
   'CO NAJMNIEJ 2 RAZY',
   'I — wrzesień/październik (przed opracowaniem lub modyfikacją IPET); II — styczeń/luty (półrocze). Zalecana III — maj/czerwiec, podsumowująca rok.',
   'Rozp. MEN 09.08.2017, tekst jedn. Dz.U. 2020 poz. 1309 — obowiązek prawny.'],
  ['IPET — modyfikacja',
   'Zgodnie z potrzebami, nie rzadziej niż po każdej WOPF',
   'Bezpośrednio po spotkaniu zespołu dokonującego WOPF. Modyfikację odnotowujemy z datą i uzasadnieniem.',
   'Ten sam akt — WOPF jest podstawą modyfikacji programu.'],
  ['Ocena efektywności pomocy p-p (dzieci bez orzeczenia)',
   'Na bieżąco + na zakończenie każdej formy pomocy; praktycznie 2 razy w roku',
   'Styczeń i czerwiec, plus każdorazowo przy zakończeniu cyklu zajęć.',
   'Rozp. MEN 09.08.2017, tekst jedn. Dz.U. 2023 poz. 1798 — obowiązek oceny efektywności i formułowania wniosków.'],
  ['KPOF',
   '2 RAZY (decyzja placówki)',
   'I — wrzesień (pomiar bazowy, także grupy 3-latków — przed IPET); II — kwiecień/maj (pomiar kontrolny, na tym samym arkuszu, innym kolorem).',
   'Decyzja rady pedagogicznej — narzędzie wewnętrzne. Zapisujemy w procedurze placówki.'],
  ['Moduł pogłębiony (ABC / sensoryczny / ToM / karta mowy)',
   'Wyłącznie na uruchomienie reguły R1–R6',
   'W ciągu 3 tygodni od decyzji zespołu. Powtórzenie tylko wtedy, gdy zmieniły się warunki albo minęło pół roku od poprzedniego.',
   'Decyzja zespołu — nie jest badaniem cyklicznym.'],
  ['Informacja o gotowości do podjęcia nauki w szkole',
   '1 RAZ',
   'Do końca kwietnia roku szkolnego poprzedzającego rozpoczęcie nauki w szkole. Wydawana rodzicom.',
   'Przepisy o świadectwach i drukach szkolnych — sprawdzić aktualny wzór na dany rok szkolny.'],
], [2100, 1700, 3100, CONTENT - 2100 - 1700 - 3100], { boldCol0: true }));

add(spacer(140));
add(box('DWA RAZY TO MINIMUM, NIE OPTIMUM', [
  p([t('Przepis mówi „co najmniej dwa razy”. Zespół, który robi dokładnie dwa razy — we wrześniu i w czerwcu — dowiaduje się o nieskuteczności programu po dziesięciu miesiącach. ')  , t('Rekomendacja: trzy WOPF-y w roku', { bold: true }), t(' (wrzesień, styczeń, maj) oraz krótki, piętnastominutowy przegląd wskaźników w listopadzie i marcu, bez sporządzania pełnego dokumentu. Przegląd nie jest WOPF-em i nie wymaga zwoływania pełnego zespołu — wystarczy notatka nauczyciela prowadzącego i specjalisty w dzienniku. Ta jedna decyzja organizacyjna zmienia więcej niż jakiekolwiek nowe narzędzie.')]),
], { fill: LIGHTO, bar: ORANGE }));

add(spacer(150));
add(H2('8.2  Co mierzymy — wskaźnik był już zapisany w celu'));
add(p([t('Jeżeli cel został sformułowany według formuły z modułu M7, ewaluacja nie wymaga wymyślania niczego nowego. Kryterium mierzalności („w 4 z 5 kolejnych dni, przy jednej podpowiedzi słownej”) ')  , t('jest', { bold: true, i: true }), t(' wskaźnikiem. Ewaluacja polega na wpisaniu obok niego wartości osiągniętej i na wyciągnięciu jednej z czterech decyzji.')]));
add(spacer(60));
add(table(['Wynik pomiaru', 'Interpretacja', 'Decyzja zespołu'], [
  ['Cel osiągnięty w pełni', 'Umiejętność ukształtowana i utrwalona w typowych sytuacjach.', 'Zamykamy cel. Stawiamy kolejny — o jeden krok wyżej albo w sytuacji nowej (generalizacja).'],
  ['Cel osiągnięty częściowo (postęp widoczny, kryterium niespełnione)', 'Kierunek dobry, tempo wolniejsze niż zakładaliśmy.', 'Kontynuujemy bez zmiany metody; przesuwamy termin i zapisujemy, o ile. Nie obniżamy kryterium.'],
  ['Brak postępu', 'Metoda, poziom wsparcia albo sam cel są nietrafione.', 'Modyfikujemy IPET: zmieniamy metodę lub obniżamy stopień trudności celu (nie samo kryterium pomiaru). Sprawdzamy bariery środowiskowe.'],
  ['Regres', 'Coś się zmieniło — zdrowie, sytuacja rodzinna, warunki w grupie.', 'Pilne spotkanie zespołu z rodzicem. Rozważamy wystąpienie do poradni; przy dziecku bez orzeczenia — ścieżka z § dotyczącym braku poprawy mimo udzielanej pomocy.'],
], [2400, 2700, CONTENT - 2400 - 2700], { boldCol0: true }));

add(spacer(140));
add(box('DWA GRZECHY EWALUACJI', [
  p([t('Grzech pierwszy — ewaluacja opisowa. ', { bold: true }), t('Zapis „dziecko czyni postępy, cel realizowany” nie jest ewaluacją. Nie zawiera liczby, więc nie da się go porównać z niczym za pół roku.')]),
  p([t('Grzech drugi — ewaluacja bez konsekwencji. ', { bold: true }), t('Zespół stwierdza brak postępu i wpisuje „kontynuować dotychczasowe działania”. To jest decyzja o powtórzeniu przez kolejne pół roku czegoś, o czym właśnie ustalono, że nie działa. Jeżeli ewaluacja nie prowadzi do zmiany w IPET albo do świadomej, uzasadnionej decyzji o kontynuacji, jest wyłącznie kosztem czasu.')]),
], { fill: LIGHT, bar: PURPLE }));

add(pageBreak());

/* ============ M9 INFORMACJA DO PORADNI ============ */
add(modul('M9', 'Opinia o funkcjonowaniu dziecka dla poradni', '20 min',
  'przygotować placówkę na opinię o funkcjonowaniu dziecka i 10-dniowy termin z § 7 ust. 3'));
add(spacer(120));

add(H2('9.1  Nowy obowiązek — co dokładnie się zmieniło'));
add(p([t('Od 1 września 2026 r., na gruncie rozporządzenia Ministra Edukacji z dnia 2 marca 2026 r. (Dz.U. 2026 poz. 428), ocena funkcjonalna staje się obowiązkowym etapem procesu diagnostycznego poprzedzającego wydanie orzeczenia. Na prośbę przewodniczącego zespołu orzekającego dyrektor przekazuje poradni ')  , t('opinię o funkcjonowaniu dziecka w przedszkolu', { bold: true }), t(' (§ 7 ust. 2). Termin wynika z § 7 ust. 3: ')  , t('„Opinię, o której mowa w ust. 2, wydaje się w terminie 10 dni od dnia otrzymania przez dyrektora prośby o jej wydanie.”', { bold: true, italics: true }), t(' Kopię opinii przekazuje się rodzicom. Opinia obligatoryjnie obejmuje trudności dziecka ')  , t('oraz jego mocne strony i uzdolnienia', { bold: true }), t(' rozpoznane przez nauczycieli i specjalistów pracujących z dzieckiem.')]));
add(spacer(60));
add(box('DLACZEGO TO JEST NAJWAŻNIEJSZY SLAJD CAŁEGO SZKOLENIA', [
  p('Dziesięć dni to mniej, niż trwa rzetelna obserwacja. Jeżeli w dniu wpłynięcia prośby z poradni przedszkole nie ma o dziecku żadnych danych, ma do wyboru dwie złe drogi: napisać opinię z pamięci albo uchybić terminowi. Wypełnienie KPOF we wrześniu dla wszystkich dzieci jest jedynym rozwiązaniem, które tę sytuację likwiduje — w dniu wpłynięcia pisma zespół ma już profil, obserwacje jakościowe i ewentualny moduł pogłębiony, a dziesięć dni wystarcza na złożenie tego w jeden dokument i na spotkanie z rodzicem.'),
], { fill: LIGHTO, bar: ORANGE }));

add(spacer(140));
add(H2('9.2  Struktura informacji — siedem punktów'));
add(table(['#', 'Punkt', 'Skąd bierzemy treść'], [
  ['1', 'Dane formalne: dziecko, grupa, okres uczęszczania, autorzy informacji i ich role.', 'Metryczka, sekcje I i II.'],
  ['2', 'Mocne strony i uzdolnienia dziecka — obowiązkowy element.', 'KPOF: twierdzenia ocenione na 5, obszary z kwalifikacją „zasób”, obserwacje jakościowe.'],
  ['3', 'Funkcjonowanie w obszarach: uczenie się, komunikacja, ruch, samoobsługa, relacje, uczestnictwo w zajęciach i zabawie.', 'KPOF: średnie obszarów d1–d9 przełożone na opis słowny.'],
  ['4', 'Trudności — opis zachowań z częstotliwością i kontekstem, bez etykiet i bez hipotez diagnostycznych.', 'KPOF: twierdzenia 1–2 + moduł pogłębiony (ABC / sensoryczny / ToM).'],
  ['5', 'Bariery i ułatwienia w środowisku przedszkolnym.', 'Komponent „e” ICF; wnioski z analizy ABC i obserwacji sensorycznej.'],
  ['6', 'Udzielone wsparcie i jego efekty — co, jak długo, z jakim skutkiem, z liczbami.', 'Karta ewaluacji celów SMART; dzienniki zajęć specjalistycznych.'],
  ['7', 'Współpraca z rodzicami: ustalenia, konsultacje, przekazane zalecenia.', 'Metryczka, sekcja XI — rejestr kontaktów i ustaleń.'],
], [500, 4300, CONTENT - 500 - 4300], { boldCol0: true }));

add(spacer(150));
add(H2('9.3  Czego w informacji nie piszemy'));
add(bullet([t('Rozpoznań i hipotez diagnostycznych. ', { bold: true }), t('„Podejrzenie spektrum autyzmu”, „cechy ADHD”, „zaburzenia SI” — to nie należy do przedszkola. Piszemy obserwacje; wnioski diagnostyczne wyciąga poradnia.')]));
add(bullet([t('Ocen rodziny i stylu wychowania. ', { bold: true }), t('„Matka niewydolna wychowawczo”, „rodzice nie współpracują”. Jeżeli współpraca faktycznie nie następuje, opisujemy fakty: ile spotkań zaproponowano, ile się odbyło, jakie zalecenia przekazano — z datami z rejestru kontaktów.')]));
add(bullet([t('Sformułowań niesprawdzalnych. ', { bold: true }), t('„Często”, „rzadko”, „ma problemy”, „słabo funkcjonuje”. Zamiast tego liczba, częstotliwość, sytuacja.')]));
add(bullet([t('Cudzych ocen bez wskazania źródła. ', { bold: true }), t('Jeżeli informacja pochodzi od rodzica albo od terapeuty spoza przedszkola, zapisujemy to wprost: „według relacji matki…”, „zgodnie z opinią logopedy z dnia…”.')]));
add(bullet([t('Załączonych arkuszy KPOF w oryginale. ', { bold: true }), t('KPOF jest naszym materiałem roboczym. Do poradni przekazujemy informację sporządzoną na jego podstawie — chyba że poradnia wprost poprosi o arkusz, a rodzic wyrazi na to zgodę.')]));

add(spacer(150));
add(cw('SZKIC W 12 MINUT  ·  pary', [
  p([t('Zadanie: ', { bold: true }), t('na podstawie kazusu z modułu M5 i celów napisanych w M7 pary redagują punkty 2, 4 i 6 opinii o funkcjonowaniu dziecka — po trzy–cztery zdania każdy.')]),
  p([t('Wymóg formalny ćwiczenia: ', { bold: true }), t('punkt 2 (mocne strony) musi być napisany PIERWSZY i musi być co najmniej tak samo obszerny jak punkt 4 (trudności). Prowadzący pilnuje tego rygorystycznie — proporcja między tymi punktami jest najprostszym testem, czy zespół rzeczywiście przeszedł na język funkcjonalny, czy tylko zmienił nagłówki w starym druku.')]),
  p([t('Sprawdzenie: ', { bold: true }), t('pary czytają swój punkt 4 na głos. Sala ma wychwycić każde słowo niesprawdzalne i każdą hipotezę diagnostyczną. Za każde takie słowo zespół dopisuje przy nim liczbę albo je wykreśla.')]),
]));

add(pageBreak());

/* ============ M10 ============ */
add(modul('M10', 'Kalendarz wdrożenia, przydział zadań, zamknięcie', '5 min',
  'wyjść ze szkolenia z przyjętym harmonogramem i przypisaną odpowiedzialnością'));
add(spacer(120));

add(H2('10.1  Przebieg'));
add(numItem([t('Powrót do arkusza pytań z modułu M0. ', { bold: true }), t('Prowadzący czyta karteczki po kolei i przy każdej wskazuje moduł, w którym padła odpowiedź. Pytania bez odpowiedzi przepisuje na osobną kartę „do wyjaśnienia”, z nazwiskiem osoby odpowiedzialnej i terminem.')]));
add(numItem([t('Przyjęcie kalendarza dokumentacji (Załącznik Z6). ', { bold: true }), t('Rada przyjmuje harmonogram; dyrektor wskazuje koordynatora zbierania arkuszy KPOF oraz osobę odpowiedzialną za obieg wystąpień z poradni.')]));
add(numItem([t('Przyjęcie reguł przekierowania R1–R6 (Załącznik Z4). ', { bold: true }), t('Reguły wchodzą do procedury placówki. Rada może je zmodyfikować — ważne, żeby zostały zapisane, a nie pozostały w głowach.')]));
add(numItem([t('Jedno zdanie od każdego uczestnika: ', { bold: true }), t('„od poniedziałku robię inaczej to, że…”. Bez komentarzy prowadzącego.')]));
add(numItem([t('Rozdanie ankiet ewaluacyjnych szkolenia (Załącznik Z7).', { bold: true })]));

add(spacer(150));
add(H2('10.2  Trzy zdania, z którymi rada ma wyjść'));
add(box(null, [
  p([t('1.  ', { bold: true, color: ORANGE, size: 22 }), t('Każdy druk ma swój przepis. ', { bold: true, size: 21 }), t('Jeżeli nie umiemy go wskazać, pytamy — nie wypełniamy „na wszelki wypadek”.', { size: 21 })]),
  p([t('2.  ', { bold: true, color: ORANGE, size: 22 }), t('Obserwacja wyprzedza pismo z poradni. ', { bold: true, size: 21 }), t('Wrześniowy KPOF to nie biurokracja — to jedyny sposób, by dotrzymać dziesięciodniowego terminu z § 7 ust. 3.', { size: 21 })]),
  p([t('3.  ', { bold: true, color: ORANGE, size: 22 }), t('Cel bez liczby nie jest celem. ', { bold: true, size: 21 }), t('Ewaluacja bez konsekwencji nie jest ewaluacją.', { size: 21 })]),
], { fill: LIGHT, bar: PURPLE }));

module.exports = C;
