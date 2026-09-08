# Buduje materiał „Komentarz ze skryptu — część 6: obserwacja pogłębiona” (HTML, A4) na bazie stylu materiału części 5.
# Użycie: python3 skrypty/komentarz_obserwacja.py  -> out/sp/Obserwacja_komentarz_ze_skryptu_czesc6.html
import re, html as H

BAZA = 'out/sp/KSzOF_komentarz_ze_skryptu_czesc5.html'
WY = 'out/sp/Obserwacja_komentarz_ze_skryptu_czesc6.html'
src = open(BAZA, encoding='utf-8').read()
head = src[:src.index('</style>') + 8]
head = head.replace('KSzOF — komentarz ze skryptu · EduPlaner 2026', 'Obserwacja pogłębiona — komentarz ze skryptu · EduPlaner 2026')
# dodatkowe style tej części
head = head.replace('</style>', '''.two{display:grid;grid-template-columns:1fr 1fr;gap:10px} .ok{border-left:4px solid #2E7D46} .zle{border-left:4px solid #C0392B}
.box p{margin:0;font-size:9px;line-height:1.5} .box .q{font-style:italic} .mark{background:#fbe6e3;color:#C0392B;padding:0 3px;border-radius:3px}
.dod{border-left:3px solid var(--orange);padding-left:8px} .dod .nr{background:var(--orange)!important;color:#fff!important}
</style>''')

t = open('public/sp-obserwacja-scenariusz.txt', encoding='utf-8').read()
ps = [re.sub(r'\[(warmly|cherfully|cheerfully)\]\s*', '', p.strip()) for p in t.split('\n\n') if p.strip()]
skrypt = ps[:31]      # 01–31: część 6 skryptu, dosłownie
dodatek = ps[31]      # uzupełnienie EduPlaner: do czego służą obserwacje
straznik = ps[32]
final = ps[33]

def e(s):
    return H.escape(s, quote=False)

def strona(nr, tresc, razem):
    return ('<section class="sheet"><div class="head"><div class="brand"><div class="logo">PCTP</div><div><div class="h1">EduPlaner 2026</div>'
            '<div class="sub">Materiał dla nauczycieli · szkoła podstawowa · komentarz ze skryptu</div></div></div>'
            '<div class="badge"><span class="pill">CZĘŚĆ 6</span><div class="tag">Obserwacja pogłębiona · 12:26 · S6.mp4</div></div></div><div class="rule"></div>'
            f'<div class="sbody">{tresc}</div>'
            f'<div class="foot"><span>EduPlaner 2026 · PCTP · Skrypt dla nauczycieli — szkoła podstawowa, część 6 · autorka: mgr Mirosława Ewa Jurczyszyn</span><span><b>Strona {nr} z {razem}</b></span></div></section>')

def sec(n, tyt):
    return f'<div class="sec"><div class="n">{n}</div><h2>{tyt}</h2><div class="line"></div></div>'

def tr(od, do, klasa=''):
    out = f'<div class="tr {klasa}">'
    for i in range(od, do):
        out += f'<div class="p"><span class="nr">{i+1:02d}</span><div>{e(skrypt[i])}</div></div>'
    return out + '</div>'

# ---------- strona 1 ----------
s1 = ('<div class="eyebrow"><span>Komentarz ze skryptu · transkrypcja narracji · podstawy prawne</span></div>'
      '<h1>Obserwacja pogłębiona — kiedy, jakim narzędziem i gdzie kończy się kompetencja nauczyciela</h1>'
      '<div class="lead">ABC i FBA · profil sensoryczny (Dunn) · teoria umysłu · karta mowy i komunikacji · profil biopsychospołeczny · karta decyzyjna</div>'
      + sec('§', 'Podstawa prawna części') +
      '<ul class="prawo">'
      '<li>Rozpoznawanie indywidualnych potrzeb rozwojowych i edukacyjnych oraz możliwości psychofizycznych uczniów, ocena efektywności udzielanej pomocy — rozporządzenie MEN z 9.08.2017 r. o pomocy psychologiczno-pedagogicznej (t.j. Dz.U. 2023 poz. 1798).</li>'
      '<li>Arkusze obserwacji pogłębionej (ABC/FBA, profil sensoryczny, karta mowy, profil biopsychospołeczny, karta decyzyjna) jako dokumentacja badań i czynności uzupełniających — rozporządzenie o dokumentacji przebiegu nauczania (t.j. Dz.U. 2024 poz. 50). ⚑</li>'
      '<li>Wielospecjalistyczna ocena poziomu funkcjonowania ucznia i IPET — rozporządzenie MEN z 9.08.2017 r. o kształceniu specjalnym (t.j. Dz.U. 2020 poz. 1309, § 6); Prawo oświatowe, art. 127 (t.j. Dz.U. 2026 poz. 820).</li>'
      '<li>Opis funkcjonowania w kategoriach aktywności i uczestniczenia (ICF), informacja szkoły dla poradni — rozporządzenie ME z 2.03.2026 r. o orzeczeniach i opiniach (Dz.U. 2026 poz. 428). ⚑</li>'
      '<li>Siedem reguł przekierowania i karta decyzyjna są decyzją rady pedagogicznej wpisaną do procedury szkoły — nie wynikają wprost z przepisu. Granica kompetencji: nauczyciel opisuje obserwowane zachowanie; rozpoznanie i kwalifikacja do terapii należą do specjalisty (terapeuta SI, logopeda, psycholog, poradnia).</li>'
      '</ul>'
      + sec('1', 'Transkrypcja narracji — komentarz (część 1: kiedy uruchamiamy, siedem reguł)') + tr(0, 7))

# ---------- strona 2 ----------
s2 = sec('1', 'Transkrypcja narracji — komentarz (część 2: ABC i FBA, profil sensoryczny)') + tr(7, 18)

# ---------- strona 3 ----------
s3 = (sec('1', 'Transkrypcja narracji — komentarz (część 3: teoria umysłu, karta mowy, karta decyzyjna)') + tr(18, 31)
      + '<div class="tr dod" style="margin-top:6px"><div class="p"><span class="nr">+</span><div><b>Uzupełnienie EduPlaner (poza skryptem) — do czego służą te obserwacje:</b> ' + e(dodatek) + '</div></div></div>')

# ---------- strona 4: tabele ----------
REGULY = [
    ('1', 'Wynik któregokolwiek obszaru KSzOF ≤ 8 pkt w skali 0–20 (Poziom III)', 'narzędzie zależne od obszaru (tabela poniżej)'),
    ('2', 'Dwa lub więcej twierdzeń ocenionych na 1–2 w tym samym obszarze', 'narzędzie zależne od obszaru'),
    ('3', 'Rozbieżność między oceniającymi ≥ 2 steny w wyniku ogólnym', 'rozmowa z rodzicem · obserwacja w obu środowiskach'),
    ('4', 'Sygnał zdrowotny z metryczki (np. nadwrażliwość sensoryczna, choroba przewlekła)', 'profil sensoryczny · konsultacja specjalisty'),
    ('5', 'Zachowanie powtarzalne zagrażające uczniowi lub innym — NATYCHMIAST, bez czekania na zespół', 'ABC + arkusz analizy funkcjonalnej'),
    ('6', 'Brak poprawy mimo udzielanej pomocy przez ok. 3 miesiące', 'karta oceny efektywności + narzędzie dla obszaru'),
    ('7', 'Nagła zmiana: oceny niżej w ≥ 3 przedmiotach albo nieobecności > 20 % zajęć w miesiącu', 'wywiad z uczniem i rodzicem · konsultacja psychologa'),
]
NARZ = [
    ('Model ABC + arkusz analizy funkcjonalnej (FBA)', '„Dlaczego to zachowanie się powtarza?” — funkcja: uwaga, przedmiot/aktywność, unikanie, regulacja pobudzenia',
     'zachowanie powtarzalne, zagrażające lub przerywające uczestnictwo; reguła 5', 'wychowawca + psycholog / pedagog specjalny; 10–15 zapisów w 2–3 tyg.',
     'hipoteza funkcji, dane, plan zachowania zastępczego; bez interpretacji w rejestrze'),
    ('Profil sensoryczny (model Dunn) — 7 układów', '„Jak uczeń reaguje na bodźce i czego potrzebuje jego układ nerwowy?” — nadreaktywność, podreaktywność, poszukiwanie bodźców',
     'sygnał z metryczki; skupisko niskich ocen w obszarach dbania o siebie i poruszania się; reguła 4', 'wychowawca (+ terapeuta SI w konsultacji); korytarz, stołówka, sala gimnastyczna',
     '„obserwowany wzorzec …, wskazana konsultacja terapeuty integracji sensorycznej”'),
    ('Obserwacja poznania społecznego i teorii umysłu', '„Czy uczeń rozumie intencje, przekonania i emocje innych?” — ironia, żart, obietnica, kłamstwo uprzejmościowe, intencja rówieśnika',
     'obszar VII (kontakty) wyraźnie niższy przy zachowanych I i IV; trudność z mimiką, gestem, tonem; rozważane wystąpienie do poradni (CZR)', 'psycholog + wychowawca; opis zachowań, nie test',
     'rzetelny opis zachowań dla poradni — bez rozpoznania'),
    ('Karta obserwacji rozwoju mowy i komunikacji', '„Czy uczeń nas rozumie i czy potrafi się porozumieć?” — 5 obszarów, 25 wskaźników 0–2, po 0–10 pkt na obszar (+ technika czytania i pisania)',
     'obszar III (porozumiewanie się) niski; zachowanie wyglądające na nieposłuszeństwo lub krzyk/wychodzenie z sali', 'wychowawca + logopeda; naturalne sytuacje',
     '„obserwowane trudności w wyodrębnianiu głosek i budowaniu wypowiedzi, wskazana diagnoza logopedyczna”'),
    ('Profil biopsychospołeczny (ICF) — uzupełnienie', '„Co wiemy o uczniu w czterech grupach czynników: biologicznych, środowiskowych, psychologicznych, społecznych?” — zasoby, bariery, ułatwiacze',
     'przed WOPFU i IPET; porządkuje wnioski z pozostałych narzędzi', 'zespół (wychowawca, specjaliści, rodzic)',
     'synteza: zasoby · bariery · ułatwiacze → sekcje VI–IX WOPFU → IPET → opinia dla poradni'),
]
tab1 = '<table class="tbl"><thead><tr><th>Reguła</th><th>Przesłanka (decyzja rady pedagogicznej, wpisana do procedury)</th><th>Co uruchamiamy</th></tr></thead><tbody>'
for n, t_, nar in REGULY:
    tab1 += f'<tr><td class="c b">{n}</td><td>{e(t_)}</td><td>{e(nar)}</td></tr>'
tab1 += '</tbody></table><p class="note">Wystarczy jedna reguła, aby zespół usiadł nad kartą decyzyjną. Kartę wpinamy do teczki także wtedy, gdy decyzja brzmi: nie uruchamiamy.</p>'
tab2 = '<table class="tbl"><thead><tr><th>Narzędzie</th><th>Na jakie pytanie odpowiada</th><th>Kiedy</th><th>Kto obserwuje</th><th>Co piszemy w dokumentacji</th></tr></thead><tbody>'
for r in NARZ:
    tab2 += '<tr>' + ''.join(f'<td>{e(x)}</td>' for x in r) + '</tr>'
tab2 += '</tbody></table>'
s4 = sec('2', 'Siedem reguł przekierowania — od wyniku kwestionariusza do decyzji zespołu') + tab1 + sec('3', 'Cztery narzędzia (plus profil biopsychospołeczny) — pytanie, przesłanka, obserwator, zapis') + tab2

# ---------- strona 5 ----------
abc = ('<div class="two"><div class="box ok"><div class="blk">Zapis poprawny — same fakty (skrypt, pkt 10)</div><p class="q">„Na trzeciej lekcji matematyki nauczyciel polecił przepisać z tablicy zadanie o sześciu linijkach. Uczeń pisał przez około dwie minuty, po czym odłożył ołówek, położył głowę na ławce i przestał reagować na polecenia przez około sześć minut. Nauczyciel podszedł, podzielił zadanie na trzy części i zaznaczył pierwszą. Uczeń przepisał zaznaczoną część.”</p><p class="note">A — polecenie: przepisać 6 linijek · B — pisał ok. 2 min, odłożył ołówek, głowa na ławce, brak reakcji ok. 6 min · C — nauczyciel dzieli zadanie na 3 części · funkcja (hipoteza): unikanie trudnego zadania.</p></div>'
       '<div class="box zle"><div class="blk">Zapis wadliwy — interpretacja zamiast faktu (skrypt, pkt 11)</div><p class="q">„Uczeń <span class="mark">zniechęcił się</span>, bo <span class="mark">nie chciało mu się pracować</span>, i <span class="mark">zamanifestował swoją niechęć</span> do przedmiotu.”</p><p class="note">Trzy interpretacje w jednym zdaniu i ani jednego faktu, który dałoby się policzyć. Interpretację formułujemy dopiero na spotkaniu zespołu, po analizie 10–15 zdarzeń — w arkuszu analizy funkcjonalnej.</p></div></div>')
sens = ('<table class="tbl"><thead><tr><th>Wzorzec</th><th>Jak wygląda w szkole (skrypt, pkt 16)</th><th>Gdzie najczęściej</th></tr></thead><tbody>'
        '<tr><td class="b">Nadreaktywność</td><td>zakrywa uszy przy dzwonku, unika tłoku na korytarzu, nie znosi metek, odmawia potraw o określonej konsystencji</td><td rowspan="3">korytarz na przerwie · stołówka · sala gimnastyczna — tam natężenie bodźców jest największe</td></tr>'
        '<tr><td class="b">Podreaktywność</td><td>nie reaguje na wołanie mimo prawidłowego słuchu, nie zauważa zabrudzonych rąk, wolno rozpoczyna czynności</td></tr>'
        '<tr><td class="b">Poszukiwanie bodźców</td><td>buja się na krześle, wpada na przedmioty, gryzie ubrania, mówi bardzo głośno</td></tr></tbody></table>')
mowa = ('<table class="tbl"><thead><tr><th>Wynik obszaru (0–10)</th><th>Odczyt (skrypt, pkt 28)</th><th>Co dalej</th></tr></thead><tbody>'
        '<tr><td class="c b g">8–10</td><td>zasób</td><td>opisujemy w mocnych stronach, wykorzystujemy w terapii i na lekcji</td></tr>'
        '<tr><td class="c b y">4–7</td><td>obszar wymagający wsparcia</td><td>cel w IPET/planie pomocy, dostosowania na lekcji</td></tr>'
        '<tr><td class="c b r">0–3</td><td>priorytet</td><td>cel terapeutyczny (SMART), wskazana diagnoza logopedyczna</td></tr></tbody></table>'
        '<p class="note">Skala wskaźnika: 0 — zachowanie nie występuje · 1 — częściowo lub z pomocą dorosłego · 2 — samodzielnie. Pięć obszarów × 5 wskaźników = 25 wskaźników; w szkole dodatkowo technika czytania i pisania w powiązaniu ze słuchem fonematycznym.</p>')
kroki = ('<ol class="kroki"><li>Po przesiewie KSzOF sprawdź siedem reguł przekierowania — wystarczy jedna.</li>'
         '<li>Zespół siada nad kartą decyzyjną (jedna na jednego ucznia): reguła, narzędzie, kto obserwuje, od kiedy, termin spotkania zespołu.</li>'
         '<li>Wypełnij metryczkę arkusza: uczeń, klasa, okres obserwacji, osoby obserwujące; wpisz tylko fakty, bez interpretacji.</li>'
         '<li>ABC: 10–15 zapisów w 2–3 tygodnie z różnych lekcji i pór dnia; kwestionariusz FBA i hipoteza funkcji dopiero na spotkaniu zespołu; zaplanuj zachowanie zastępcze i honoruj je natychmiast.</li>'
         '<li>Profil sensoryczny: obserwuj także korytarz, stołówkę i salę gimnastyczną; opisz wzorzec, nie rozpoznanie; wskaż konsultację terapeuty SI.</li>'
         '<li>Teoria umysłu: opisz zachowania (ironia, żart, obietnica, intencja rówieśnika); bez testu i bez rozpoznania — opis dla poradni.</li>'
         '<li>Karta mowy: 25 wskaźników 0–2, wynik 0–10 na obszar; odczyt 8–10 / 4–7 / 0–3; wskaż diagnozę logopedyczną.</li>'
         '<li>Profil biopsychospołeczny: uporządkuj zasoby, bariery i ułatwiacze w czterech grupach czynników ICF.</li>'
         '<li>Wnioski przenieś do sekcji VI–IX WOPFU, do IPET (cel ze źródłem w obserwacji) i do opinii dla poradni (informacja szkoły w 10 dni).</li>'
         '<li>Zapisz także decyzję odmowną — pokazuje, że zespół sprawę rozważył. Arkusze wpinamy do teczki ucznia (dokumentacja badań i czynności uzupełniających).</li></ol>')
s5 = (sec('4', 'ABC — zapis poprawny a zapis wadliwy') + abc
      + sec('5', 'Profil sensoryczny — trzy wzorce i trzy miejsca') + sens
      + sec('6', 'Karta mowy i komunikacji — odczyt wyniku obszaru') + mowa
      + sec('7', 'Obserwacja pogłębiona krok po kroku') + kroki)

strony = [s1, s2, s3, s4, s5]
doc = head + '<body>' + ''.join(strona(i + 1, s, len(strony)) for i, s in enumerate(strony)) + '</body></html>'
open(WY, 'w', encoding='utf-8').write(doc)
print('zapisano', WY, len(doc))
