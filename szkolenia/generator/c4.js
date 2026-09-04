const G = require('./gen.js');
const { Paragraph, AlignmentType, BorderStyle, t, p, H1, H2, H3, bullet, numItem, spacer,
        pageBreak, box, table, modul, straznik, cw, CONTENT, PURPLE, ORANGE, LIGHT, LIGHTO } = G;

const C = [];
const add = (...x) => x.forEach(e => C.push(e));

add(pageBreak());

/* ============ M6 OBSERWACJA POGŁĘBIONA ============ */
add(modul('M6', 'Obserwacja pogłębiona — ABC, profil sensoryczny, ToM, karta mowy. Kiedy?', '45 min',
  'ustalić jednoznaczne reguły uruchamiania modułów pogłębionych'));
add(spacer(120));

add(H2('6.1  Zasada nadrzędna: moduł pogłębiony jest odpowiedzią, nie rutyną'));
add(p([t('KPOF jest przesiewem — obejmuje wszystkie dzieci i odpowiada na pytanie ')  , t('„gdzie”', { bold: true, i: true }), t('. Moduł pogłębiony obejmuje pojedyncze dzieci i odpowiada na pytanie ')  , t('„dlaczego”', { bold: true, i: true }), t('. Uruchamiamy go wtedy i tylko wtedy, gdy wynik przesiewu wskazuje konkretny kierunek — nigdy „dla wszystkich”, „dla pewności” ani „bo tak było w zeszłym roku”. Moduł pogłębiony kosztuje kilkanaście godzin pracy zespołu; uruchomiony bez przesłanki, odbiera ten czas dziecku, które go naprawdę potrzebuje.')]));

add(spacer(140));
add(H2('6.2  Reguły przekierowania — kiedy uruchamiamy moduł'));
add(p([t('Poniższe reguły są ')  , t('propozycją do przyjęcia przez radę pedagogiczną', { bold: true }), t(' i wpisania do procedury placówki (Załącznik Z4). Nie wynikają wprost z przepisu — przepis wymaga jedynie rozpoznawania potrzeb i oceny efektywności. Reguły służą temu, by decyzja nie zależała od tego, który nauczyciel danego dnia patrzy na arkusz.')]));
add(spacer(60));
add(table(['Reguła', 'Warunek uruchomienia modułu pogłębionego'], [
  ['R1 — próg obszaru', 'Średnia któregokolwiek obszaru poniżej 2,0 (Poziom III).'],
  ['R2 — skupisko', 'Dwa lub więcej twierdzeń ocenionych na 1 lub 2 w tym samym obszarze — niezależnie od średniej obszaru.'],
  ['R3 — rozbieżność', 'Różnica średniej obszaru między oceniającymi (nauczyciel / rodzic / specjalista) wynosi 1,5 pkt lub więcej.'],
  ['R4 — sygnał zdrowotny', 'W metryczce (sekcja VI) zaznaczono nadwrażliwość sensoryczną, dietę eliminacyjną, wadę wzroku lub słuchu albo ograniczenia ruchowe.'],
  ['R5 — bezpieczeństwo', 'Zachowanie zagraża dziecku lub innym, powtarza się i przerywa uczestnictwo w zajęciach — moduł ABC uruchamiamy natychmiast, bez czekania na pełny wynik KPOF.'],
  ['R6 — brak efektu', 'Mimo udzielanej pomocy p-p przez co najmniej jeden okres (ok. 3 miesiące) nie następuje poprawa funkcjonowania.'],
], [1900, CONTENT - 1900], { boldCol0: true }));

add(spacer(160));
add(H2('6.3  Który moduł — tabela decyzyjna'));
add(table(['Sygnał z KPOF', 'Moduł', 'Czego szukamy'], [
  ['Niskie d2 (zwłaszcza radzenie sobie ze stresem i zmianą) i/lub d7; zachowania trudne powtarzalne; reguła R5.',
   'MODEL ABC — analiza behawioralna',
   'Funkcji zachowania: co je poprzedza, co po nim następuje, co dziecko przez nie uzyskuje.'],
  ['Niskie d5 (jedzenie, ubieranie, higiena) i/lub d4; nietypowe reakcje na dźwięk, dotyk, konsystencję, ruch; reguła R4.',
   'PROFIL SENSORYCZNY',
   'Wzorca przetwarzania sensorycznego: nadreaktywność, podreaktywność, poszukiwanie bodźców.'],
  ['Niskie d7 przy zachowanym d1 i d4; brak zabawy „na niby”; dosłowność; trudność z perspektywą drugiej osoby.',
   'OBSERWACJA ToM — teoria umysłu',
   'Zdolności do przypisywania innym stanów umysłu: wiedzy, przekonań, intencji, emocji.'],
  ['Niskie d3 (porozumiewanie się); dziecko nie mówi albo rozumie je tylko najbliższa rodzina; nie wykonuje prostych poleceń mimo prawidłowego słuchu; zachowania trudne, za którymi może stać brak możliwości porozumienia się.',
   'KARTA OBSERWACJI ROZWOJU MOWY I KOMUNIKACJI',
   'Poziomu rozumienia i mówienia w 5 obszarach (0–10 pkt): co dziecko rozumie, jak mówi, jak się porozumiewa — i podstaw do skierowania na diagnozę logopedyczną.'],
], [3400, 2200, CONTENT - 3400 - 2200], { boldCol0: true }));

add(pageBreak());
add(H2('6.4  Model ABC — analiza poprzedników i następstw'));
add(p([t('Co to jest: ', { bold: true }), t('ABC to schemat zapisu zdarzenia behawioralnego w trzech kolumnach — ')  ,
  t('A (antecedent) ', { bold: true }), t('poprzednik: co działo się bezpośrednio przed zachowaniem; '),
  t('B (behavior) ', { bold: true }), t('zachowanie: co dokładnie zrobiło dziecko, opisane obserwowalnie i mierzalnie; '),
  t('C (consequence) ', { bold: true }), t('następstwo: co stało się bezpośrednio po zachowaniu, w tym reakcja dorosłych i rówieśników.')]));
add(spacer(60));
add(table(['Element', 'Zapis błędny', 'Zapis poprawny'], [
  ['A', 'Był zdenerwowany.', 'Nauczycielka ogłosiła sprzątanie zabawek; dziecko budowało wieżę z klocków od 6 minut; w sali grała muzyka.'],
  ['B', 'Zachowywał się agresywnie.', 'Rzucił dwa klocki w kierunku półki, krzyczał przez ok. 40 sekund, położył się na podłodze.'],
  ['C', 'Uspokoił się.', 'Nauczycielka podeszła, przykucnęła, nie odbierała klocków; po 2 minutach dziecko wstało i dokończyło wieżę; sprzątanie odroczono o 3 minuty.'],
], [1150, 2700, CONTENT - 1150 - 2700], { boldCol0: true }));
add(spacer(80));
add(bullet([t('Kiedy uruchamiamy: ', { bold: true }), t('zachowanie trudne jest powtarzalne (nie jednorazowe), zagraża dziecku lub innym, przerywa uczestnictwo dziecka w zajęciach albo utrzymuje się mimo udzielanego wsparcia.')]));
add(bullet([t('Ile zdarzeń: ', { bold: true }), t('minimum 10–15 zapisów w ciągu 2–3 tygodni, prowadzonych przez wszystkie osoby pracujące z dzieckiem. Poniżej dziesięciu zdarzeń nie widać wzorca, tylko anegdoty.')]));
add(bullet([t('Czego szukamy: ', { bold: true }), t('powtarzalnej funkcji zachowania. Najczęstsze cztery: uzyskanie uwagi dorosłego, uzyskanie przedmiotu lub aktywności, uniknięcie trudnego zadania lub sytuacji, autostymulacja / regulacja pobudzenia.')]));
add(bullet([t('Produkt: ', { bold: true }), t('hipoteza funkcji zachowania oraz plan zastąpienia go zachowaniem alternatywnym pełniącym tę samą funkcję. To zdanie trafia wprost do IPET jako cel SMART.')]));
add(bullet([t('Czego NIE robimy: ', { bold: true }), t('nie zapisujemy interpretacji („chciał zwrócić uwagę”) w kolumnie B. Interpretacja powstaje dopiero przy analizie wielu zdarzeń, na spotkaniu zespołu.')]));

add(spacer(150));
add(H2('6.5  Profil sensoryczny — obserwacja przetwarzania bodźców'));
add(p([t('Co to jest: ', { bold: true }), t('ustrukturyzowana obserwacja reakcji dziecka na bodźce w siedmiu układach: słuchowym, wzrokowym, dotykowym, węchowym, smakowym, przedsionkowym (równowaga i ruch obrotowy) oraz proprioceptywnym (czucie głębokie, nacisk, napięcie mięśni). Opisujemy wzorzec, nie stawiamy rozpoznania.')]));
add(spacer(60));
add(table(['Wzorzec', 'Jak wygląda w sali przedszkolnej', 'Kierunek wsparcia'], [
  ['Nadreaktywność (unikanie)', 'Zakrywa uszy przy odkurzaczu i głośnej muzyce; odsuwa się w kolejce; nie znosi metek, farb, plasteliny; odmawia potraw o określonej konsystencji; płacze przy myciu rąk.', 'Redukcja bodźców, zapowiadanie, słuchawki wygłuszające, wybór miejsca w sali, stopniowe oswajanie faktur.'],
  ['Podreaktywność (niska rejestracja)', 'Nie reaguje na wołanie po imieniu mimo prawidłowego słuchu; wydaje się „nieobecny”; nie zauważa zabrudzenia, mokrych rękawów, skaleczenia; wolno rozpoczyna czynności.', 'Wzmocnienie bodźca, kontakt dotykowy przed poleceniem, kontrast, aktywizacja przed zadaniem.'],
  ['Poszukiwanie bodźców', 'Wspina się i zeskakuje, wpada na przedmioty i osoby, kręci się, gryzie ubrania, ciągle czegoś dotyka, mówi bardzo głośno.', 'Zaplanowana „dieta sensoryczna”: przerwy ruchowe, dźwiganie, przepychanie, ciężki koc, aktywność proprioceptywna przed zajęciem przy stoliku.'],
], [2200, 4100, CONTENT - 2200 - 4100], { boldCol0: true }));
add(spacer(80));
add(bullet([t('Kiedy uruchamiamy: ', { bold: true }), t('reguła R4 (sygnał z metryczki) lub R2 w obszarze d5/d4; reakcje na bodźce są nietypowe, powtarzalne i wpływają na uczestnictwo dziecka w zajęciach, posiłkach lub czynnościach samoobsługowych.')]));
add(bullet([t('Granica kompetencji — powiedzieć wprost: ', { bold: true, color: ORANGE }), t('nauczyciel przedszkola opisuje obserwowane reakcje. Rozpoznanie zaburzeń przetwarzania sensorycznego i kwalifikacja do terapii integracji sensorycznej należą do terapeuty SI z odpowiednim przygotowaniem. W dokumentacji piszemy: „obserwowany wzorzec poszukiwania bodźców przedsionkowo-proprioceptywnych — wskazana konsultacja terapeuty SI”, a nie „dziecko ma zaburzenia SI”.')]));

add(pageBreak());
add(H2('6.6  Obserwacja ToM — teoria umysłu'));
add(p([t('Co to jest: ', { bold: true }), t('teoria umysłu (Theory of Mind) to zdolność przypisywania sobie i innym ludziom stanów umysłu — wiedzy, przekonań, intencji, pragnień i emocji — oraz rozumienia, że stany te mogą różnić się od naszych własnych i od stanu faktycznego. To fundament zabawy „na niby”, współpracy, kłamstwa, żartu i empatii.')]));
add(spacer(60));
add(H3('Kiedy taka obserwacja jest potrzebna — odpowiedź wprost'));
add(p('To pytanie pada na każdym szkoleniu i wymaga jednoznacznej odpowiedzi. Obserwację ToM uruchamiamy, gdy spełniony jest przynajmniej jeden z poniższych warunków:'));
add(bullet('Profil KPOF pokazuje wyraźnie niższy obszar d7 (wzajemne kontakty i związki międzyludzkie) przy zachowanych lub wysokich obszarach d1 (uczenie się) i d4 (poruszanie się) — czyli dziecko poznawczo i ruchowo radzi sobie, a relacyjnie nie.'));
add(bullet('Niskie d7 współwystępuje z niskim d3 (porozumiewanie się) w pozycjach dotyczących rozumienia komunikatów pozawerbalnych — mimiki, gestu, tonu głosu.'));
add(bullet('Dziecko nie podejmuje zabawy „na niby” i nie przyjmuje ról w zabawie tematycznej, mimo odpowiedniego wieku (obszar d8).'));
add(bullet('Rozumie język dosłownie: nie odczytuje żartu, ironii, metafory, przenośni; reaguje na treść, nie na intencję.'));
add(bullet('Nie kieruje uwagi rozmówcy na obiekt (brak wskazywania protodeklaratywnego), rzadko dzieli radość z odkrycia, nie sprawdza wzrokiem reakcji dorosłego.'));
add(bullet('Zespół rozważa wystąpienie do poradni w związku z podejrzeniem całościowych zaburzeń rozwoju — obserwacja ToM porządkuje wtedy materiał obserwacyjny przekazywany poradni.'));

add(spacer(140));
add(box('WIEK MA ZNACZENIE — INACZEJ NARZĘDZIE WPROWADZI NAS W BŁĄD', [
  p([t('Klasyczne zadania fałszywego przekonania pierwszego rzędu (typu Sally–Anne, „nieoczekiwana zawartość”) rozwiązywane są przez dzieci typowo rozwijające się mniej więcej ')  , t('od 4.–4,5 roku życia', { bold: true }), t('. Niepowodzenie u trzylatka jest zjawiskiem rozwojowo typowym i ')  , t('nie stanowi żadnej przesłanki diagnostycznej', { bold: true }), t('.')]),
  p([t('U dzieci młodszych obserwujemy wyłącznie wskaźniki wczesne: ')  , t('uwagę wspólną', { bold: true }), t(' (podążanie za wzrokiem i gestem dorosłego), ')  , t('wskazywanie protodeklaratywne', { bold: true }), t(' („zobacz!” — dzielenie się uwagą, nie proszenie o przedmiot), ')  , t('odwoływanie społeczne', { bold: true }), t(' (sprawdzanie miny dorosłego w sytuacji niejasnej) oraz ')  , t('początki zabawy symbolicznej', { bold: true }), t(' (klocek jako telefon). Dla trzylatka to są jedyne uprawnione wskaźniki.')]),
  p([t('Granica kompetencji: ', { bold: true, color: ORANGE }), t('obserwacja ToM w przedszkolu opisuje zachowania. Nie jest testem, nie daje wyniku i nie prowadzi do rozpoznania spektrum autyzmu. Prowadzi wyłącznie do rzetelnego opisu przekazywanego poradni w opinii o funkcjonowaniu dziecka.')]),
], { fill: LIGHTO, bar: ORANGE }));

add(spacer(140));
add(H2('6.7  Karta obserwacji rozwoju mowy i komunikacji'));
add(p([t('Dlaczego czwarte narzędzie: ', { bold: true }), t('trudności w komunikacji bywają przyczyną wielu innych problemów. Dziecko, które nie rozumie polecenia, wygląda na nieposłuszne. Dziecko, które nie potrafi powiedzieć, czego chce, krzyczy albo uderza. Zanim uznamy, że problem leży w zachowaniu, sprawdzamy, czy dziecko nas rozumie i czy potrafi się z nami porozumieć — brak mowy albo brak rozumienia mowy trzeba wykluczyć w pierwszej kolejności.')]));
add(p([t('Co to jest: ', { bold: true }), t('karta obserwacji rozwoju mowy i komunikacji (narzędzie EduPlaner 2026) porządkuje mowę dziecka w pięciu obszarach: rozumienie mowy (recepcja), mowa czynna i artykulacja (ekspresja), słuch fonematyczny i percepcja słuchowa, słownictwo i gramatyka oraz komunikacja i budowanie wypowiedzi (pragmatyka). 25 wskaźników w skali 0–2: 0 — zachowanie nieobecne, 1 — częściowo lub z pomocą dorosłego, 2 — samodzielnie. Każdy obszar daje wynik 0–10 pkt; średni poziom mowy to średnia z pięciu obszarów. Wskaźniki mają kody ICF (d310, b320, b1560, b16700, d330 i in.).')]));
add(table(['Wynik obszaru', 'Odczyt', 'Co robimy'], [
  ['8–10', 'Zasób — mocna strona, fundament do pracy', 'Wykorzystujemy w celach SMART jako punkt oparcia.'],
  ['4–7', 'Wymaga wsparcia — częściowo opanowane', 'Cel SMART w tym obszarze; wsparcie w bieżącej pracy.'],
  ['0–3', 'Priorytet — obszar do intensywnej pracy', 'Cel SMART + wskazanie diagnozy logopedycznej w dokumentacji.'],
], [1400, 3600, CONTENT - 1400 - 3600], { boldCol0: true }));
add(spacer(60));
add(H3('Kiedy uruchamiamy kartę mowy'));
add(bullet('Obszar d3 (porozumiewanie się) w KPOF jest niski albo zawiera twierdzenia ocenione na 1–2 (reguły R1, R2).'));
add(bullet('Dziecko nie mówi, mówi pojedynczymi słowami albo mówi tak, że rozumie je wyłącznie najbliższa rodzina.'));
add(bullet('Nie wykonuje prostych poleceń mimo prawidłowego słuchu — sprawdzamy rozumienie, zanim uznamy to za brak współpracy.'));
add(bullet('Zespół podejrzewa, że za zachowaniem trudnym (R5) stoi brak możliwości porozumienia się — wtedy karta mowy wyprzedza ABC albo idzie z nim równolegle.'));
add(spacer(60));
add(box('GRANICA KOMPETENCJI', [
  p([t('Nauczyciel opisuje to, co słyszy i widzi w naturalnych sytuacjach: w zabawie, rozmowie, słuchaniu bajek. ', { bold: true }), t('Karta nie jest testem i nie zastępuje diagnozy logopedycznej. Wynik zasila cele SMART, WOPF oraz opinię o funkcjonowaniu dziecka i stanowi podstawę do skierowania na diagnozę logopedyczną. W dokumentacji piszemy np.: „obserwowane trudności w wyodrębnianiu głosek i w budowaniu wypowiedzi, wskazana diagnoza logopedyczna”.')]),
], { fill: LIGHTO, bar: ORANGE }));

add(spacer(150));
add(cw('KAZUS ZESPOŁOWY  ·  20 min', [
  p([t('Materiał: ', { bold: true }), t('trzy opisy dzieci (po jednym na zespół), zawierające fragment profilu KPOF i krótką notatkę nauczyciela.')]),
  p([t('Zadanie: ', { bold: true }), t('wskazać (1) którą regułę R1–R6 spełnia opis, (2) który moduł pogłębiony uruchamiamy i dlaczego, (3) którego modułu NIE uruchamiamy i dlaczego, (4) kto i w jakim terminie prowadzi obserwację.')]),
  p([t('Kazus 1: ', { bold: true }), t('czterolatek, d1 = 4,1; d4 = 4,3; d7 = 1,6; nie przyjmuje ról w zabawie tematycznej; nie odczytuje żartu; wskazuje palcem wyłącznie po to, by dostać przedmiot. → R1 + R2; moduł ToM; nie uruchamiamy ABC, bo nie ma zachowań trudnych.')]),
  p([t('Kazus 2: ', { bold: true }), t('pięciolatek, wszystkie obszary 3,1–4,0; w ostatnim miesiącu siedem incydentów uderzenia rówieśnika, wszystkie w szatni i przy kolejce do łazienki. → R5; moduł ABC natychmiast, bez czekania na komplet arkuszy; nie uruchamiamy modułu sensorycznego wyłącznie na podstawie miejsca zdarzeń — dopiero analiza ABC pokaże, czy tłok i hałas są poprzednikiem.')]),
  p([t('Kazus 3: ', { bold: true }), t('trzylatek, d5 = 1,9; odmawia potraw o konsystencji papkowatej, płacze przy myciu rąk, zdejmuje skarpetki; w metryczce zaznaczono nadwrażliwość sensoryczną. → R1 + R4; profil sensoryczny; nie uruchamiamy ToM — trzylatek, brak przesłanek relacyjnych, wiek poniżej progu zadań fałszywego przekonania.')]),
  p([t('Kazus 4: ', { bold: true }), t('czterolatek, d3 = 1,8; mówi pojedynczymi słowami, rozumie go tylko mama; w kole odchodzi i przewraca zabawki, gdy nie może się porozumieć. → R1 + R2; karta obserwacji mowy jako pierwsza; ABC dopiero po sprawdzeniu, czy zachowanie nie wynika z braku możliwości porozumienia się.')]),
]));

module.exports = C;
