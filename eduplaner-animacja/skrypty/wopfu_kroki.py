# Kroki pełnego wypełnienia druku WOPFU (public/wopfu.html) danymi Zofii Lewandowskiej (klasa III A)
# zebranymi z metryczki, KSzOF, obserwacji pogłębionej (ABC/FBA, Dunn, karta mowy I–III, profil biopsychospołeczny).
# Użycie: python3 skrypty/wopfu_kroki.py  -> public/wopfu-kroki.json  (format wypelnij_druk.mjs: {sel,t} | {sel,k:1})
import json

DATA = '29.09.2026'
K = []
def t(sel, tekst): K.append({'sel': sel, 't': tekst})
def k(sel): K.append({'sel': sel, 'k': 1})

# data w nagłówku każdego arkusza
for n in range(1, 22): t(f'@{n} .student .blank #0', DATA)

# ---------- I · dane ucznia, I a · rodzaj oceny, II · zespół ----------
t('@1 .fg .v #1', '14.03.2017')
t('@1 .blankline #0', 'I etap edukacyjny (klasy I–III)')
t('@1 .blankline #1', 'PPP.4223.18.2026 z 12.06.2026 · Poradnia Psychologiczno-Pedagogiczna w Koszalinie')
t('@1 .blankline #2', 'niepełnosprawność sprzężona: autyzm + niepełnosprawność ruchowa (orzeczenie o potrzebie kształcenia specjalnego)')
t('@1 .blankline #3', 'mgr Anna Nowak — pedagog specjalny')
t('@1 .fg .v #3', '29.09.2026 · rok szkolny 2026/2027')
k('@1 .opt #0')
t('@1 .fg .v #4', 'nie dotyczy — pierwsza ocena w szkole (ścieżka: IPET)')
t('@1 .blankline #4', 'PPP Koszalin (opinia — 10 dni), SCWEW Koszalin, terapeuta SI, alergolog')
ZESPOL = [('mgr Anna Nowak', 'pedagog specjalny'), ('mgr Katarzyna Wiśniewska', 'nauczyciel edukacji wczesnoszkolnej'),
          ('mgr Marta Zielińska', 'psycholog szkolny'), ('mgr Ewa Sikora', 'nauczyciel współorganizujący kształcenie'),
          ('mgr Piotr Kowalczyk', 'neurologopeda'), ('mgr Joanna Malinowska', 'terapeuta integracji sensorycznej (konsultacja)')]
for i, (a, b) in enumerate(ZESPOL):
    t(f'@1 .dline #{2*i}', a); t(f'@1 .dline #{2*i+1}', b)

# ---------- III · kontekst i metoda ----------
for i in [0, 1, 2, 3, 4]: k(f'@2 .opt #{i}')
for i in range(6, 14): k(f'@2 .opt #{i}')
t('@2 .blankline #0', '01–26.09.2026 · 4 tygodnie · 14 sesji + wywiad z rodzicem 05.09')
KONT = [('Lekcje: matematyka, j. polski — praca przy tablicy i w ławce', 'praca samodzielna ok. 8 min przy zadaniu w 3 krokach; przy zadaniu wieloetapowym bez podziału — ok. 2 min, głowa na ławce'),
        ('Przerwy międzylekcyjne, korytarz', 'przebywa sama lub z Olą; nie inicjuje kontaktu; przy hałasie zakrywa uszy'),
        ('Stołówka — przerwa obiadowa', '23.09: zakryła uszy, krzyknęła, wybiegła; po 5 min w strefie wyciszenia wróciła na obiad'),
        ('Praca w parach, zmiana miejsca (sytuacje przejściowe)', 'siedzi bez ruchu, nie odpowiada partnerowi ok. 4 min; karta zadania w 3 krokach pomaga')]
for i, (a, b) in enumerate(KONT):
    t(f'@2 .dline #{2*i}', a); t(f'@2 .dline #{2*i+1}', b)

# ---------- IV · informacje medyczne ----------
for i in [2, 6, 7]: k(f'@3 .opt #{i}')
MED = [('Alergia na orzechy (zaświadczenie alergologa 20.08.2026)', 'adrenalina w autostrzykawce — gabinet pielęgniarki, szafka nr 3', 'przy objawach reakcji: adrenalina → 112 → rodzice; bez orzechów na stołówce i w klasie'),
       ('Nadwrażliwość słuchowa (profil sensoryczny 22.09.2026)', 'nie dotyczy — bez leków', 'hałas skraca czas pracy z ok. 8 do 1 min; słuchawki wyciszające, strefa wyciszenia'),
       ('Niepełnosprawność ruchowa (orzeczenie)', 'nie dotyczy', 'wolne tempo pisania, męczliwość ręki; nakładki na przybory, wydłużony czas')]
for i, (a, b, c) in enumerate(MED):
    t(f'@3 .dline #{3*i}', a); t(f'@3 .dline #{3*i+1}', b); t(f'@3 .dline #{3*i+2}', c)
t('@3 .box #0', 'Nie — udział w WF bez zwolnienia; dostosowanie: ćwiczenia bez rywalizacji i nagłych zmian, ograniczony hałas w sali (zaświadczenie lekarskie 20.08.2026).')
t('@3 .box #1', 'Reakcja alergiczna: adrenalina (autostrzykawka) → 112 → mama 600 100 200 → tata 600 300 400. Przeciążenie sensoryczne: wyjście do strefy wyciszenia z p. Ewą Sikorą, powrót po 5–10 min.')

# ---------- V · diagnoza funkcjonalna (pkt 0–20; sten i poziom z druku autorki) ----------
PKT = [6, 7, 11, 12, 10, 8, 11, 7, 12]
for i, p in enumerate(PKT): t(f'@4 td.ex #{3*i}', f'{p} / 20')

# ---------- V a · mocne strony i trudności ----------
VA = [('pamięć wzrokowa, czytanie globalne ok. 20 wyrazów, interpretuje obrazki i proste wykresy', 'nie zapisuje kilkuzdaniowej wypowiedzi, nie kończy zadania wieloetapowego bez podziału na kroki; 23/75 pkt'),
      ('wykonuje pojedyncze polecenie ze wsparciem wizualnym, przestrzega rutyny', 'nie planuje zadania złożonego, przerywa pracę przy zmianie planu; 10/30 pkt'),
      ('rozumie polecenia do klasy, utrzymuje temat rozmowy z dorosłym, buduje zdania złożone', 'głoski szumiące i słuch fonematyczny (sten 3); rzadko inicjuje rozmowę z rówieśnikiem; 22/40 pkt'),
      ('sprawna w znanych zadaniach ruchowych, samodzielnie porusza się po szkole', 'wolne tempo pisania, męczliwość ręki (motoryka mała); 12/20 pkt'),
      ('samodzielna przy posiłku i ubieraniu się', 'nie sygnalizuje przeciążenia i potrzeby przerwy; wybiórczość pokarmowa przy hałasie; 10/20 pkt'),
      ('spójne rutyny domowe, obowiązki wykonuje po przypomnieniu (arkusz rodzica)', 'brak okazji do samodzielnych obowiązków w szkole; 4/10 pkt (rodzic)'),
      ('jedna stała koleżanka (Ola), akceptacja klasy', 'nie inicjuje kontaktu, nie przyjmuje perspektywy partnera w pracy w parach; 22/40 pkt'),
      ('przestrzega zasad klasowych, korzysta z pomocy p. Ewy', 'nie prosi o pomoc, nie pełni ról klasowych; 5/15 pkt'),
      ('chętnie uczestniczy w wyjściach przyrodniczych', 'brak zajęć pozalekcyjnych; unika dużych zgromadzeń (hałas); 6/10 pkt')]
for i, (a, b) in enumerate(VA):
    t(f'@5 .dline #{2*i}', a); t(f'@5 .dline #{2*i+1}', b)

# ---------- VI · potrzeby, mocne strony, zainteresowania, predyspozycje ----------
t('@6 .box #0', 'Przewidywalna struktura dnia z zapowiedzią zmian; polecenia krótkie, dzielone na 3 kroki z piktogramami; czas wydłużony o połowę; ochrona przed hałasem (słuchawki, strefa wyciszenia, miejsce w pierwszej ławce); nauka sygnalizowania potrzeby przerwy i pomocy (karta „proszę o przerwę”); wsparcie nauczyciela współorganizującego w bieżącej pracy; terapia logopedyczna (głoski szumiące, słuch fonematyczny); trening umiejętności społecznych w małej grupie.')
t('@6 .box #1', 'Pamięć wzrokowa i czytanie globalne (ok. 20 wyrazów); rozumie polecenia kierowane do klasy; utrzymuje temat rozmowy z dorosłym; przestrzega rutyny i zasad; sprawna ruchowo w znanych zadaniach; samodzielna w samoobsłudze; pracuje samodzielnie ok. 8 minut przy zadaniu w 3 krokach.')
t('@6 .box #2', 'Zwierzęta i przyroda („chcę mieć psa i czytać książki o zwierzętach”); obrazki, układanki i zadania oparte na obrazie; motywuje pochwała opisowa, wybór zadania i przerwa, kiedy jest za głośno (ankieta „Mój głos”, 04.09.2026).')
t('@6 .box #3', 'Predyspozycje do pracy na materiale wzrokowym i konkretnym; kierunki: samodzielność w zadaniu wieloetapowym, sygnalizowanie potrzeb (komunikacja funkcjonalna), inicjowanie kontaktu z rówieśnikami, regulacja przeciążenia sensorycznego, technika pisania.')

# ---------- VII · przyczyny niepowodzeń, bariery ----------
VII = ['Obszary I (6/20) i VIII (7/20): zadania wieloetapowe bez podziału, wolne tempo pisania, nieproszenie o pomoc; w hałasie czas pracy spada do ok. 1 min',
       'Obszar II (7/20): przerywa pracę przy zmianie planu; ABC: przy zadaniu trudnym odkłada ołówek i kładzie głowę na ławce (funkcja: unikanie — 15/15)',
       'Artykulacja i słuch fonematyczny — sten 3 (Poziom III): głoski szumiące, różnicowanie p–b, s–sz; rozumienie i pragmatyka w normie (sten 8); AAC nie dotyczy',
       'Rejestr ABC 22–26.09 (6 zdarzeń): unikanie zadania (głowa na ławce), przeciążenie sensoryczne (zakrywa uszy, wybiega), bezruch przy pracy w parach; bez agresji',
       'Hałas na stołówce, korytarzu i sali gimnastycznej; zmiana miejsca i partnera; brak przyjmowania perspektywy kolegi (ToM K3 niski); brak strefy wyciszenia przy sali',
       'Nadwrażliwość słuchowa 6/10, dotykowa 5/10, podwrażliwość proprioceptywna 6/10 (profil Dunn 22.09.2026); wzrok i słuch fizjologicznie w normie',
       'Alergia na orzechy (adrenalina w szkole); niepełnosprawność ruchowa — męczliwość ręki; bez leków stałych',
       'Pracuje w parze tylko z Olą; w grupie 4+ milknie; na przerwie sama; w wyjściach klasowych uczestniczy, w hałaśliwych uroczystościach — ze słuchawkami',
       'Po 3 tygodniach (pierwsza ławka, słuchawki, zadania w 3 krokach) czas samodzielnej pracy wzrósł z ok. 2 do ok. 8 min; relacje rówieśnicze bez zmian (KSzOF, 22.09.2026)']
for i, s in enumerate(VII): t(f'@7 .dline #{i}', s)

# ---------- VIII · zakres i charakter wsparcia ----------
for i in [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]: k(f'@8 .opt #{i}')
W8 = [('Nauczyciel współorganizujący — cały czas zajęć (§ 7 ust. 2)', 'mgr Ewa Sikora', 'wsparcie w zadaniach wieloetapowych, karta „proszę o przerwę”, wyjście do strefy wyciszenia'),
      ('Rewalidacja (2 godz./tydz.) · logopedia (1) · TUS w małej grupie (1)', 'mgr Anna Nowak · mgr Piotr Kowalczyk · mgr Marta Zielińska', 'wymiar ustala dyrektor w IPET; łącznie 4 godz./tydz.'),
      ('Konsultacja terapeuty SI i dieta sensoryczna w klasie', 'mgr Joanna Malinowska (SI) · wychowawczyni', 'przerwy proprioceptywne co 20–30 min, słuchawki, miejsce dobrane do profilu')]
for i, (a, b, c) in enumerate(W8):
    t(f'@8 .dline #{3*i}', a); t(f'@8 .dline #{3*i+1}', b); t(f'@8 .dline #{3*i+2}', c)

# ---------- IX · czynniki środowiskowe, IX a · dobrostan ----------
for i in [0, 1, 2, 3, 6, 7]: k(f'@9 .opt #{i}')
t('@9 .box #0', 'Zaangażowani rodzice i spójne rutyny domowe (e310); akceptacja klasy i koleżanka Ola (e320); nauczyciel współorganizujący, pierwsza ławka, słuchawki, piktogramy, zadania w 3 krokach (e130, e330); strefa wyciszenia w sali 12; wsparcie PPP i SCWEW (e585).')
t('@9 .box #1', 'Hałas w klasie, na stołówce i korytarzu (e250) skraca czas pracy z ok. 8 do 1 min; zbyt liczna klasa (26 uczniów); zadania wieloetapowe bez wsparcia wizualnego; brak strefy wyciszenia w pobliżu sali; nagłe zmiany planu.')
t('@9 .box #2', 'Czuje się bezpiecznie przy p. Ewie i z Olą; lubi przyrodę i obrazki; najtrudniejsze: hałas na stołówce i długie zadania („Mój głos”, 04.09.2026); poczucie sprawczości rośnie, gdy może wybrać zadanie i poprosić o przerwę.')

# ---------- X · analiza ABC ----------
ABC = [('22.09, matematyka: polecenie przepisania 6 linijek z tablicy', 'pisała ok. 2 min, odłożyła ołówek, głowa na ławce, brak reakcji ok. 6 min', 'nauczyciel podzielił zadanie na 3 części; przepisała pierwszą', 'unikanie zadania', '3–4 × w tyg.'),
       ('23.09, stołówka: hałas, kolejka, ok. 60 osób', 'zakryła uszy, krzyknęła, wybiegła na korytarz', 'p. Ewa wyprowadziła do strefy wyciszenia; po 5 min wróciła', 'przeciążenie sensoryczne', '2 × w tyg.'),
       ('24.09, j. polski: praca w parach, zmiana miejsca', 'siedziała bez ruchu, nie odpowiadała partnerowi ok. 4 min', 'karta zadania w 3 krokach; wykonała swoją część', 'unikanie / regulacja', '1–2 × w tyg.'),
       ('25.09, przerwa: nagła zmiana planu (odwołana lekcja)', 'płacz, pytania „co teraz?” przez ok. 3 min', 'plan dnia z piktogramami, zapowiedź zmiany; uspokoiła się', 'regulacja napięcia', '1 × w tyg.')]
for i, row in enumerate(ABC):
    for j, s in enumerate(row): t(f'@10 .dline #{5*i+j}', s)
t('@10 .box #0', 'Gdy zadanie jest długie lub wieloetapowe albo otoczenie głośne, Zofia przerywa aktywność (głowa na ławce, wyjście), w efekcie unika wymagania lub obniża pobudzenie — funkcja: unikanie (15/15) + regulacja napięcia (10/15). Plan PBS: zadania w 3 krokach, karta „proszę o przerwę” honorowana natychmiast, uprzedzanie o zmianach, spójna reakcja wszystkich dorosłych; bez kar.')

# ---------- XI · profil sensoryczny ----------
for i in [0, 5, 8, 9, 12, 16, 18]: k(f'@11 .chk #{i}')
SENS = ['1/10 — bez trudności przy tablicy i ekranie', '6/10 — zakrywa uszy przy dzwonku i na stołówce; hałas skraca pracę do ok. 1 min',
        '5/10 — unika metek i niespodziewanego dotyku; sfera oralna: wybiórczość konsystencji', '1/10 — w normie', '1/10 — w normie',
        '6/10 — poszukuje docisku: opiera się o ławkę, gryzie rękaw; męczliwość ręki przy pisaniu', '3/10 — w normie; lubi huśtawkę, unika WF z nagłymi zmianami']
for i, s in enumerate(SENS): t(f'@11 .dline #{i}', s)
WSK = ['miejsce z ograniczonymi bodźcami w polu widzenia; plan dnia wizualny', 'słuchawki wyciszające dostępne bez proszenia; stołówka w mniejszej turze; uprzedzanie o dzwonku',
       'uprzedzanie o dotyku, podchodzenie od przodu; bez przymusu przy jedzeniu', 'bez wskazań', 'bez wskazań',
       'przerwy proprioceptywne co 20–30 min (noszenie, pchanie), poduszka sensoryczna, nakładki na przybory', 'ruch przed zadaniami wymagającymi skupienia; WF bez rywalizacji']
for i, s in enumerate(WSK): t(f'@11 .dline #{7+i}', s)

# ---------- XII · teoria umysłu ----------
TOM = [('4 / 6 pkt', 'przeciętny'), ('3 / 6 pkt', 'przeciętny'), ('1 / 6 pkt', 'niski'), ('2 / 6 pkt', 'niski'), ('1 / 6 pkt', 'niski')]
for i, (a, b) in enumerate(TOM): t(f'@12 td.ex #{2*i}', a); t(f'@12 td.ex #{2*i+1}', b)
TOMW = ['termometr emocji, nazywanie emocji przez dorosłego w sytuacji napięcia', 'historyjki społeczne z rozpoznawaniem mimiki i tonu głosu (TUS 1 godz./tydz.)',
        'trening perspektywy: „co widzi / wie Ola?” — zadania fałszywego przekonania I rzędu, praca w parze z rolami',
        'rozróżnianie potrącenia przypadkowego i celowego — scenki, komiksy społeczne', 'żart i ironia w tekstach czytanych — omawianie znaczenia dosłownego i niedosłownego']
for i, s in enumerate(TOMW): t(f'@12 .dline #{i}', s)

# ---------- XII b · profil mowy ----------
for i in [2, 4, 6, 9, 13, 16, 19, 22, 26]: k(f'@13 .chk #{i}')
MOWA = ['sten 8 — rozumie polecenia do klasy i polecenia złożone', 'sten 6 — zdania złożone; wypowiedź wymaga rozbudowy', 'sten 3 — głoski szumiące (sz, ż, cz, dż) wymawiane jako syczące',
        'sten 3 — nie różnicuje p–b, s–sz; analiza i synteza prostych słów z pomocą', 'adekwatny do wieku', 'poprawna fleksja i składnia',
        'sten 6 — prawidłowy tor oddechowy; utrwalać emisję', 'płynna, bez cech jąkania', 'sten 8 — dialog z dorosłym, utrzymuje temat; z rówieśnikiem rzadziej']
for i, s in enumerate(MOWA): t(f'@13 .dline #{i}', s)
t('@13 .box #1', 'Rozumienie mowy i pragmatyka (sten 8): rozumie polecenia kierowane do klasy, utrzymuje temat rozmowy, zasób słownictwa adekwatny do wieku, mowa zrozumiała dla nowych rozmówców.')
t('@13 .box #2', 'PRIORYTET: artykulacja głosek szumiących i słuch fonematyczny (sten 3) — bariera w czytaniu i pisaniu (opuszczanie liter); rozbudowa wypowiedzi (mowa czynna, sten 6). Wskazana standaryzowana diagnoza logopedyczna.')

# ---------- XII c · wskazania logopedyczne ----------
for i in [0, 1, 4, 6, 9]: k(f'@14 .opt #{i}')
LOGO = [('Wywołanie i utrwalenie głosek szumiących (sz, ż, cz, dż)', 'terapia indywidualna 45 min · 1×/tydz.; metoda słuchowo-wzrokowa: sylaby → wyrazy → zdania', 'kryterium: poprawna wymowa w wyrazach w 8 z 10 prób do 29.01.2027'),
        ('Różnicowanie słuchowe głosek opozycyjnych (p–b, s–sz) i analiza głoskowa', 'ćwiczenia słuchu fonematycznego na lekcji i w domu (10 min dziennie)', 'kryterium: analiza słów 3–4-głoskowych bez pomocy w 4 z 5 prób do 29.01.2027'),
        ('Rozbudowa wypowiedzi (opowiadanie historyjki 4-obrazkowej)', 'historyjki obrazkowe, pytania pomocnicze, nagranie wypowiedzi', 'kryterium: wypowiedź 4-zdaniowa z 1 podpowiedzią do 30.04.2027')]
for i, (a, b, c) in enumerate(LOGO):
    t(f'@14 .dline #{3*i}', a); t(f'@14 .dline #{3*i+1}', b); t(f'@14 .dline #{3*i+2}', c)

# ---------- XIII · ocena efektywności (pierwsza WOPFU — poziom wyjściowy) ----------
START = ['dostosowania od 08.09: pierwsza ławka, słuchawki, zadania w 3 krokach', 'zespół 6 osób, spotkania co 4 tyg.; zeszyt komunikacji od 08.09',
         'planowane: logopedia 1 godz., TUS 1 godz. (tydz.)', 'planowane: rewalidacja 2 godz./tydz. od 01.10.2026',
         'wywiad 05.09; konsultacja SCWEW — X 2026', 'start: praca samodzielna ok. 8 min; karta przerwy 0/5']
for i, s in enumerate(START):
    t(f'@15 .dline #{3*i}', s); t(f'@15 .dline #{3*i+1}', '— (29.01.2027)'); t(f'@15 .dline #{3*i+2}', '— (28.05.2027)')
t('@15 .fg .v #0', '29.09.2026'); t('@15 .fg .v #1', '29.01.2027 (planowana)'); t('@15 .fg .v #2', '28.05.2027 (planowana)')
t('@15 .box #0', 'Pierwsza WOPFU — poziom wyjściowy. Ocena efektywności przy WOPFU śródrocznej (29.01.2027) i rocznej (28.05.2027); przeglądy wskaźników: listopad 2026 i marzec 2027 (15 min na ucznia, notatka w dzienniku).')

# ---------- XIV · decyzja zespołu ----------
k('@16 .chk #2')
t('@16 .fg .v #0', 'III (obszary I, II, VI, VIII) · II w pozostałych'); t('@16 .fg .v #1', '29.09.2026')
t('@16 .blankline #0', 'protokół zespołu nr 3/2026/2027')
t('@16 .box #0', 'Zespół rekomenduje Poziom III (wsparcie specjalistyczne, IPET) w obszarach I, II, VI, VIII oraz Poziom II w obszarach III, IV, V, VII, IX. Cele kluczowe do IPET: (1) technika pisania — przepisanie zdania do 8 wyrazów bez opuszczeń liter w 4 z 5 prób, zadanie w 3 krokach, czas +50% — do 18.12.2026; (2) karta „proszę o przerwę” zamiast położenia głowy na ławce w 3 z 5 sytuacji — do 31.03.2027; (3) inicjowanie kontaktu z rówieśnikiem w 3 z 5 przerw (TUS) — do 29.01.2027; (4) głoski szumiące i słuch fonematyczny — logopedia 1 godz./tydz. Spotkania zespołu: 29.01.2027 i 28.05.2027; przeglądy wskaźników XI 2026 i III 2027; konsultacje: SI (X 2026), SCWEW (X 2026); PPP — opinia o funkcjonowaniu w 10 dni od prośby.')

# ---------- XV · raport opisowy ----------
t('@17 .dline #0', '01.09.2026'); t('@17 .dline #1', '26.09.2026'); t('@17 .dline #2', '4 (114/260)'); t('@17 .dline #3', 'III / II')
t('@17 .dline #4', 'w dniu 29.09.2026'); t('@17 .dline #5', 'otrzymał(a) jej kopię')
t('@17 .box #0', 'III porozumiewanie się (11/20), IV motoryka (12/20), IX życie w społeczności (12/20) — rozumienie mowy i pragmatyka sten 8; pamięć wzrokowa, czytanie globalne, rutyna.')
t('@17 .box #1', 'I uczenie się (6/20), VIII edukacja szkolna (7/20), II zadania i obowiązki (7/20), VI życie domowe (8/20) — zadania wieloetapowe, technika pisania, proszenie o pomoc, planowanie.')
t('@17 .box #2', 'Zasoby: pamięć wzrokowa, rozumienie mowy, rutyna, koleżanka Ola, zaangażowani rodzice. Trudności: unikanie zadań długich (funkcja: unikanie 15/15), przeciążenie hałasem (słuch 6/10), słuch fonematyczny i głoski szumiące (sten 3), przyjmowanie perspektywy (ToM K3 niski). Ułatwienia: nauczyciel współorganizujący, pierwsza ławka, słuchawki, zadania w 3 krokach, strefa wyciszenia. Bariery: hałas na stołówce i korytarzu, klasa 26 osób, nagłe zmiany planu.')
t('@17 .box #3', 'nauczyciel współorganizujący w bieżącej pracy; rewalidacja 2 godz./tydz.; logopedia 1 godz./tydz.; TUS w małej grupie 1 godz./tydz.; dieta sensoryczna i dostosowania (słuchawki, przerwy proprioceptywne, zadania w 3 krokach, czas +50%); konsultacje z rodzicami co 4 tygodnie; konsultacja SI i SCWEW.')

# ---------- XVI · przeniesienie do IPET ----------
P18 = ['Pamięć wzrokowa, czytanie globalne, zainteresowanie przyrodą, rutyna → materiał obrazkowy, zadania o zwierzętach, pochwała opisowa, wybór zadania (sekcja VI, KSzOF obszary I i IV).',
       'Cel 1: przepisanie zdania do 8 wyrazów bez opuszczeń liter w 4 z 5 prób do 18.12.2026 (sfera poznawcza). Cel 2: karta „proszę o przerwę” w 3 z 5 sytuacji do 31.03.2027 (społeczno-emocjonalna). Cel 3: inicjowanie kontaktu w 3 z 5 przerw do 29.01.2027. Cel 4: głoski szumiące w 8 z 10 prób do 29.01.2027 (komunikacja).',
       'Poziom III — obszary I, II, VI, VIII (priorytet: uczenie się i edukacja szkolna); Poziom II — III, IV, V, VII, IX (decyzja zespołu 29.09.2026).',
       'Polecenia krótkie, w 3 krokach z piktogramami; czas wydłużony o 50%; miejsce w pierwszej ławce; ocena treści bez błędów zapisu; odpowiedź ustna lub wybór zamiast długiego pisania — szczegóły w kartach dostosowań przedmiotowych.',
       'Jeden cel, jeden plan: karta „proszę o przerwę” uczona przez psychologa, honorowana na każdej lekcji i w domu; zeszyt komunikacji; spotkania zespołu co 4 tygodnie; AAC nie dotyczy.']
for i, s in enumerate(P18): t(f'@18 .box #{i}', s)
P19 = ['Rewalidacja 2 godz./tydz. (funkcje wykonawcze, technika pisania); logopedia 1 godz./tydz.; zajęcia rozwijające kompetencje emocjonalno-społeczne (TUS) 1 godz./tydz. w grupie do 5 osób — wymiar ustala dyrektor.',
       'Plan PBS: zadania w 3 krokach, uprzedzanie o zmianach, karta „proszę o przerwę” honorowana natychmiast, strefa wyciszenia dostępna bez proszenia, spójna reakcja dorosłych, bez kar; rejestr ABC prowadzony dalej (ocena 29.01.2027).',
       'Słuchawki wyciszające, stołówka w mniejszej turze, przerwy proprioceptywne co 20–30 min, nakładki na przybory, plan dnia wizualny, nauczyciel współorganizujący przez cały czas zajęć (§ 7 ust. 2).',
       'Konsultacje z rodzicami co 4 tygodnie + zeszyt komunikacji; instruktaż: dieta sensoryczna i ćwiczenia logopedyczne w domu (10 min dziennie); PPP Koszalin — opinia o funkcjonowaniu w 10 dni; SCWEW — konsultacja X 2026; terapeuta SI.']
for i, s in enumerate(P19): t(f'@19 .box #{i}', s)

# ---------- XIX · załączniki ----------
for i in range(0, 8): k(f'@21 .opt #{i}')

json.dump(K, open('public/wopfu-kroki.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print('kroków', len(K))
