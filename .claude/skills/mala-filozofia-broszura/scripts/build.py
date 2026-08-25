# -*- coding: utf-8 -*-
"""Skład broszury serii „Mała Filozofia" — makieta A4, 60 stron o stałym rozmiarze.

    python3 scripts/build.py tresc.json [katalog_wyjsciowy]

Cała treść pochodzi z pliku JSON. Ten plik odpowiada wyłącznie za układ:
paginację, żywą paginę, marginesy lustrzane i typografię polską.
Dzięki temu kolejny tom serii wymaga napisania treści, a nie grzebania w składzie.
"""
import json, os, re, sys

TU = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TU)
import gra
import infografiki as ig

SCIEZKA = sys.argv[1] if len(sys.argv) > 1 else os.path.join(TU, '..', 'assets', 'tresc-arystoteles.json')
WYJSCIE = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(SCIEZKA))
D = json.load(open(SCIEZKA, encoding='utf-8'))
M, ROZ = D['meta'], D['rozdzialy']
def _katalog_logo():
    """Znaki leżą w assets/logo (w skillu) albo w logo/ obok gotowej broszury."""
    if os.environ.get('LOGO'):
        return os.environ['LOGO']
    for kandydat in (os.path.join(TU, '..', 'assets', 'logo'), os.path.join(TU, '..', 'logo')):
        if os.path.isdir(kandydat):
            return kandydat
    raise SystemExit('Nie znalazłem katalogu ze znakami. Wskaż go zmienną LOGO=…')

LOGO_KAT = _katalog_logo()

ORD = [None, 'pierwsze', 'drugie', 'trzecie', 'czwarte', 'piąte', 'szóste',
       'siódme', 'ósme', 'dziewiąte', 'dziesiąte', 'jedenaste', 'dwunaste']
P0 = 9                                   # pierwsza strona rozdziału 1
STRONY_ROZ = {i + 1: P0 + i * 3 for i in range(12)}

# ---------------------------------------------------------------- narzędzia
def akapity(zdania, podzial, klasa='t'):
    """Łączy zdania w akapity o zadanych rozmiarach — 3–4 zdania czytają się
    jak proza, a jedno zdanie w linii rozsypuje kolumnę."""
    if sum(podzial) != len(zdania):
        raise ValueError('Podział %s nie pasuje do %d zdań' % (podzial, len(zdania)))
    out, i = [], 0
    for n in podzial:
        out.append('<p class="%s">%s</p>' % (klasa, ' '.join(zdania[i:i + n])))
        i += n
    return '\n'.join(out)

def figura(svg, etykieta=None, podpis=None, klasa=''):
    h = '<figure class="ilustracja %s">' % klasa
    if etykieta: h += '<p class="etykieta">%s</p>' % etykieta
    h += svg
    if podpis: h += '<figcaption>%s</figcaption>' % podpis
    return h + '</figure>'

def wczytaj_logo(nazwa):
    """Wstawia plik z katalogu logo/ jako kod SVG, z kolorami na tokenach palety.
    Identyfikatory dostają numer, żeby ten sam znak można było wstawić kilka razy."""
    s = open(os.path.join(LOGO_KAT, nazwa), encoding='utf-8').read()
    s = re.sub(r'<\?xml[^>]*\?>', '', s)
    s = re.sub(r'\s(?:width|height)="[^"]*"', '', s.split('>', 1)[0]) + '>' + s.split('>', 1)[1]
    s = s.replace('<g id="logo">', '<g>')
    wczytaj_logo.licznik = getattr(wczytaj_logo, 'licznik', 0) + 1
    for stary in set(re.findall(r'id="([\w-]+)"', s)):
        nowy = '%s-%d' % (stary, wczytaj_logo.licznik)
        s = s.replace('id="%s"' % stary, 'id="%s"' % nowy).replace('#%s)' % stary, '#%s)' % nowy)
    return s.strip()

ZNAK = wczytaj_logo('mala-filozofia-znak.svg')
LOGO_POZ = wczytaj_logo('mala-filozofia-logo-poziome.svg')
LOGO_PION = wczytaj_logo('mala-filozofia-logo-pionowe.svg')
PCTP = lambda: wczytaj_logo('pctp-logo.svg')

STRONY = []
def strona(html, pagina='', klasa=''):
    STRONY.append((klasa, pagina, html))

# ======================================================= 1. OKŁADKA
strona(klasa='okladka', html='''
<div class="okl-gora">
  <div class="okl-logo">%s</div>
  <p class="okl-tom">%s</p>
</div>
<div class="okl-obraz">%s</div>
<div class="okl-dol">
  <h1>%s</h1>
  <p class="okl-podtytul">%s</p>
  <div class="okl-pasek"><span>12 spotkań</span><span>12 emocji</span><span>60 pytań</span></div>
  <div class="okl-wydawca"><div class="pctp-znak">%s</div><p>Wydawca<br><strong>%s</strong></p></div>
</div>''' % (LOGO_POZ, M['tom_slownie'], D['svg']['okladka'], M['tytul'], M['podtytul'],
             PCTP(), M['wydawca_skrot']))

# ======================================================= 2. STRONA TYTUŁOWA
strona(klasa='tytulowa', html='''
<div class="tyt-blok">
  <div class="tyt-logo">%s</div>
  <p class="tyt-seria">%s</p>
  <h1 class="tyt-glowny">%s</h1>
  <div class="tyt-ornament">%s</div>
  <p class="tyt-pod">%s</p>
  <p class="tyt-adres">%s</p>
</div>
<div class="tyt-stopka"><span>12 spotkań</span><span>12 emocji</span><span>60 pytań</span></div>
<div class="tyt-wydawca"><div class="pctp-znak">%s</div>
  <p><strong>%s</strong><br>%s</p></div>''' % (
  LOGO_PION, M['tom_slownie'], M['tytul'], ig.GALAZKA, M['podtytul'], M['odbiorca'],
  PCTP(), M['wydawca_skrot'], M['wydawca_opis']))

# ======================================================= 3. STRONA REDAKCYJNA
strona(klasa='redakcyjna', html='''
<div class="red-gora">
  <div class="red-znak">%s</div>
  <div>
    <p class="red-tytul">%s</p>
    <p class="red-seria">Seria „%s”, tom %s</p>
  </div>
</div>
<dl class="metryka">
  <dt>Przeznaczenie</dt><dd>%s oraz dla osób, które z nią pracują: rodziców, nauczycieli, terapeutów.</dd>
  <dt>Zawartość</dt><dd>12 rozdziałów · 450 zdań opowiadania · 60 pytań · 8 infografik ·
    karta emocji do wycięcia · słowniczek · załącznik z grą planszową.</dd>
  <dt>Wydanie</dt><dd>Pierwsze</dd>
  <dt>Tekst i opracowanie</dt><dd>&nbsp;</dd>
  <dt>Ilustracje i skład</dt><dd>&nbsp;</dd>
  <dt>Wydawca</dt><dd class="dd-wydawca"><span class="pctp-znak">%s</span>
    <span><strong>%s</strong> · miejsce na pełną nazwę, adres i stronę internetową</span></dd>
  <dt>ISBN</dt><dd>&nbsp;</dd>
</dl>
<div class="red-nota">
  <p class="t">Sceny w rozdziałach są opowiadaniem. Fakty z życia bohatera – daty, miejsca, tytuły ksiąg –
  są zgodne z relacjami źródeł. Dialogi zostały napisane na potrzeby tej broszury.
  Pełną notę o cytatach znajdziesz na stronie 50.</p>
</div>
<div class="red-kroje">
  <p><strong>Kroje pisma:</strong> Atkinson Hyperlegible (Braille Institute of America) –
  zaprojektowany dla osób z trudnościami w czytaniu; Alegreya Sans (Huerta Tipográfica).
  Oba na licencji SIL Open Font License 1.1.</p>
  <p><strong>Format:</strong> A4, 60 stron, druk dwustronny.</p>
</div>
<p class="red-copy">© Wszystkie prawa zastrzeżone. Kopiowanie całości lub fragmentów
w celach komercyjnych wymaga zgody wydawcy. Karty, plansza i strony do wypełnienia wolno
kopiować na własny użytek.</p>''' % (ZNAK, M['tytul_plaski'], M['seria'], M['tom'],
                                     M['odbiorca'], PCTP(), M['wydawca_skrot']))

# ======================================================= 4. SPIS TREŚCI
def poz(t, s, klasa=''):
    return ('<li class="tresc-poz %s"><span class="tresc-nazwa">%s</span>'
            '<span class="kropki"></span><span class="str">%s</span></li>') % (klasa, t, s)

spis = ['<li class="tresc-dzial">Zanim zaczniesz</li>',
        poz(D['wstep']['tytul'], 5),
        poz('Każdy rozdział ma te same pięć części', 6),
        poz('%s <em>· infografika</em>' % D['os_czasu']['tytul'], 7),
        poz('Termometr emocji <em>· infografika</em>', 8),
        '<li class="tresc-dzial">Dwanaście spotkań</li>']
for r in ROZ:
    spis.append(poz('<span class="tresc-nr">%d</span> %s <em>· %s</em>'
                    % (r['nr'], r['tytul'], r['emocja_label'].lower()), STRONY_ROZ[r['nr']], 'roz'))
spis += ['<li class="tresc-dzial">Dodatki</li>',
         poz('Dwanaście zdań na dwanaście emocji', 45),
         poz('Moja karta emocji <em>· do wycięcia</em>', 47),
         poz('Słowniczek', 48),
         poz('Jak pracować z tą broszurą <em>· dla dorosłych</em>', 49),
         poz('Nota o cytatach i źródłach', 50),
         poz('Moje notatki', 51),
         '<li class="tresc-dzial">Załącznik · gra</li>',
         poz('%s <em>· o grze</em>' % D['gra']['tytul'], 52),
         poz('Zasady gry krok po kroku', 53),
         poz('Plansza <em>· dwadzieścia pól</em>', 54),
         poz('Kostki do wycięcia', 55),
         poz('Karty do wycięcia', 57)]
strona(klasa='spis', pagina='Spis treści',
       html='<h2 class="dzial-tytul">Spis treści</h2><ol class="tresc">%s</ol>' % '\n'.join(spis))

# ======================================================= 5. ZANIM ZACZNIESZ
strona(pagina='Zanim zaczniesz', html='''
<h2 class="dzial-tytul">%s</h2>
%s
<figure class="frontispis">%s<figcaption>%s · %s</figcaption></figure>
<div class="zasady">
  <p class="etykieta">Zasady, które obowiązują w tej broszurze</p>
  <ul class="lista">%s</ul>
</div>''' % (D['wstep']['tytul'], akapity(D['wstep']['zdania'], [3, 3]), D['svg']['okladka'],
             M['bohater'], M['lata'],
             ''.join('<li>%s</li>' % z for z in D['wstep']['zasady'])))

# ======================================================= 6. STRUKTURA ROZDZIAŁU
strona(pagina='Zanim zaczniesz', html='''
<h2 class="dzial-tytul">Każdy rozdział ma te same pięć części</h2>
<p class="lead">Kolejność nigdy się nie zmienia. Zawsze wiesz, co będzie dalej.</p>
<ol class="kroki">
  <li><span class="krok-cyfra">1</span><span class="krok-nazwa">Scena</span>
      <span class="krok-opis">Krótka historia z życia bohatera.</span></li>
  <li><span class="krok-cyfra">2</span><span class="krok-nazwa">Myśl</span>
      <span class="krok-opis">Jedno jego zdanie, wytłumaczone prostymi słowami.</span></li>
  <li><span class="krok-cyfra">3</span><span class="krok-nazwa">Emocja</span>
      <span class="krok-opis">Uczucie, o którym mówi ta scena – z nazwą i opisem sygnałów z ciała.</span></li>
  <li><span class="krok-cyfra">4</span><span class="krok-nazwa">W Twoim życiu</span>
      <span class="krok-opis">Zwykła sytuacja, która może zdarzyć się dzisiaj.</span></li>
  <li><span class="krok-cyfra">5</span><span class="krok-nazwa">Pięć pytań</span>
      <span class="krok-opis">Pytania bez ocen. Nie ma złych odpowiedzi.</span></li>
</ol>
<p class="podsum">12 rozdziałów × 5 pytań = <strong>60 pytań</strong></p>
<div class="na-koncu">
  <p class="etykieta">Co znajdziesz na końcu książeczki</p>
  <ol>
    <li><span>Dwanaście zdań bohatera do wycięcia</span><span>str. 45</span></li>
    <li><span>Moja karta emocji – do noszenia w piórniku</span><span>str. 47</span></li>
    <li><span>Słowniczek trudnych słów</span><span>str. 48</span></li>
    <li><span>Miejsce na Twoje notatki</span><span>str. 51</span></li>
    <li><span>Gra planszowa „%s”</span><span>str. 52</span></li>
  </ol>
</div>''' % D['gra']['tytul'])

# ======================================================= 7. OŚ CZASU
oc = D['os_czasu']
strona(pagina='Zanim zaczniesz', html='''
<h2 class="dzial-tytul">%s</h2>
<p class="lead">%s</p>
%s
<div class="karty-4">%s</div>''' % (
  oc['tytul'], oc['lead'],
  figura(ig.os_czasu(oc), None, oc['podpis']),
  ''.join('<div class="karta-mini"><p class="km-t">%s</p><p class="km-o">%s</p></div>'
          % (k['tytul'], k['opis']) for k in oc['karty'])))

# ======================================================= 8. TERMOMETR
strona(pagina='Zanim zaczniesz', html='''
<h2 class="dzial-tytul">Termometr emocji</h2>
<p class="lead">Emocja to nie tylko „jest” albo „nie ma”. Emocja ma siłę, a siłę można zmierzyć.</p>
%s
<div class="ramka-wskazowka">
  <p class="etykieta">Jak używać skali</p>
  <p class="t">Zanim nazwiesz emocję, pokaż jej siłę liczbą od 0 do 10. Możesz pokazać ją na palcach
  zamiast mówić – to też jest pełna odpowiedź. Ta sama skala wraca w wielu rozdziałach tej broszury,
  więc warto ustalić ją raz i używać jej także poza książeczką.</p>
</div>
<div class="tabela-blok">
  <p class="etykieta">Moja własna skala – wpisz, co znaczy u Ciebie każdy poziom</p>
  <table class="moja-skala">
    <thead><tr><th>Poziom</th><th>Co to znaczy u mnie</th></tr></thead>
    <tbody>%s</tbody>
  </table>
</div>''' % (figura(ig.termometr(D['termometr']['podpis'])),
             ''.join('<tr><td>%s</td><td class="pole">&nbsp;</td></tr>' % p for p in
                     ['0–2 · spokój', '3–4 · lekko czuję', '5–6 · wyraźnie czuję',
                      '7–8 · bardzo mocno', '9–10 · za dużo, proszę o pomoc'])))

# ======================================================= 9–44. ROZDZIAŁY
for r in ROZ:
    n, tyt, pagina = r['nr'], r['tytul'], '%d · %s' % (r['nr'], r['tytul'])
    fig = figura(r['svg'], r.get('fig_etykieta'), r.get('fig_caption'),
                 'ilu-rozdzial ' + ('ilu-info' if r.get('fig_etykieta') else 'ilu-scena'))
    strona(klasa='otwarcie-strona', pagina=pagina, html='''
<header class="otwarcie">
  <p class="otw-nad">Spotkanie %s</p>
  <div class="otw-linia"><span class="otw-cyfra">%d</span><span class="otw-kreska"></span></div>
  <h2 class="otw-tytul">%s</h2>
  <p class="otw-emocja">Emocja: <strong>%s</strong></p>
</header>
%s
<section class="czesc">
  <h3 class="czesc-tytul"><span class="cz-nr">1</span>Scena</h3>
  %s
</section>
%s''' % (ORD[n], n, tyt, r['emocja_label'].lower(), fig, akapity(r['scena'], [4, 4, 3, 3]),
         '' if r.get('fig_etykieta') else '<div class="ornament">%s</div>' % ig.ORNAMENT))

    tabela = ''
    if r.get('tabela'):
        head = re.search(r'<thead>.*?</thead>', r['tabela'], re.S).group(0)
        body = re.search(r'<tbody>(.*?)</tbody>', r['tabela'], re.S).group(1)
        rows = re.findall(r'<tr>.*?</tr>', body, re.S)[:3]
        tabela = ('<div class="tabela-blok"><p class="etykieta">Ten sam pomysł w codziennych sprawach</p>'
                  '<table class="tab-srodek">%s<tbody>%s</tbody></table></div>' % (head, ''.join(rows)))
    strona(pagina=pagina, html='''
<blockquote class="cytat">
  <p class="cytat-tekst">%s</p>
  <p class="cytat-zrodlo">%s</p>
</blockquote>
<section class="czesc">
  <h3 class="czesc-tytul"><span class="cz-nr">2</span>Myśl bohatera</h3>
  %s
</section>
<section class="czesc blok-emocja">
  <h3 class="czesc-tytul"><span class="cz-nr">3</span>Emocja</h3>
  <p class="emocja-nazwa">%s</p>
  %s
</section>''' % (r['cytat'], r['cytat_zrodlo'], akapity(r['mysl'], [4, 3, 3]),
                 r['emocja_nazwa'], akapity(r['emocja'], [4, 3])))

    pyt = '\n'.join('<li><span class="p-nr">%s</span><span class="p-tresc">%s</span></li>' % (a, b)
                    for a, b in r['pytania'])
    # rozdział z tabelą oddaje jej miejsce na linie do pisania — obie rzeczy naraz
    # nie mieszczą się na stronie, a tabela niesie treść, więc ma pierwszeństwo
    dopelnienie = tabela or ('<div class="odpowiedzi"><p class="etykieta">Miejsce na Twoją odpowiedź</p>'
                             '<div class="linie-odp">%s</div></div>'
                             % ('<span class="linia-do-pisania"></span>' * 5))
    strona(pagina=pagina, html='''
<section class="czesc blok-zycie">
  <h3 class="czesc-tytul"><span class="cz-nr">4</span>W Twoim życiu</h3>
  %s
</section>
<section class="czesc blok-pytania">
  <h3 class="czesc-tytul"><span class="cz-nr">5</span>Pięć pytań</h3>
  <ol class="pytania">%s</ol>
</section>
%s''' % (akapity(r['zycie'], [3, 3]), pyt, dopelnienie))

# ======================================================= 45–46. HASŁA
def karta_hasla(h):
    return ('<li class="haslo"><span class="h-nr">%d</span><p class="h-emocja">%s</p>'
            '<p class="h-cytat">„%s”</p><p class="h-po">%s</p></li>') % tuple(h)
for i, lead in ((0, 'Spotkania 1–6. Możesz wyciąć jedno pole i powiesić je na ścianie.'),
                (6, 'Spotkania 7–12. Wybierz to zdanie, które dziś do Ciebie pasuje.')):
    strona(pagina='Dodatki', html='''
<h2 class="dzial-tytul">Dwanaście zdań na dwanaście emocji</h2>
<p class="lead">%s</p>
<ol class="hasla">%s</ol>''' % (lead, '\n'.join(karta_hasla(h) for h in D['hasla'][i:i + 6])))

# ======================================================= 47. KARTA EMOCJI
strona(pagina='Dodatki', html='''
<h2 class="dzial-tytul">Moja karta emocji</h2>
<p class="lead">Cztery kroki w wersji kieszonkowej. Wytnij wzdłuż przerywanej linii –
karta mieści się w piórniku. Możesz ją pokazać zamiast mówić.</p>
%s
<div class="ramka-wskazowka">
  <p class="t">Kroki wykonuje się po kolei. Jeśli któryś jest dziś za trudny, wolno go pominąć
  i przejść do następnego. Sam pierwszy krok – nazwanie – zwykle już trochę pomaga.</p>
</div>
<div class="karta-instrukcja">
  <p><strong>Kiedy jej użyć.</strong> Wtedy, gdy czujesz, że coś się dzieje w ciele,
  ale nie umiesz jeszcze powiedzieć co.</p>
  <p><strong>Gdy nie idzie mówienie.</strong> Wskaż palcem pole numer 1 i pokaż liczbę
  na palcach. To wystarczy, żeby ktoś Cię zrozumiał.</p>
  <p><strong>Krok trzeci bywa najtrudniejszy.</strong> Jeśli nie wiesz, co się stało tuż przed,
  napisz po prostu „nie wiem”. To też jest informacja.</p>
  <p><strong>Po wszystkim.</strong> Wróć do kroku drugiego i sprawdź, czy liczba się zmieniła.
  Zwykle spada o jeden albo dwa punkty.</p>
</div>''' % figura(ig.karta_emocji()))

# ======================================================= 48. SŁOWNICZEK
strona(pagina='Dodatki', html='''
<h2 class="dzial-tytul">Słowniczek</h2>
<p class="lead">Trudne słowa z tej broszury, wyjaśnione po kolei.</p>
<dl class="slownik">%s</dl>''' % '\n'.join('<dt>%s</dt><dd>%s</dd>' % tuple(s) for s in D['slownik']))

# ======================================================= 49. DLA DOROSŁYCH
strona(pagina='Dodatki', html='''
<h2 class="dzial-tytul">Jak pracować z tą broszurą</h2>
<p class="lead">Strona dla rodziców, nauczycieli i terapeutów.</p>
<ul class="lista lista-dorosli">
  <li><strong>Jeden rozdział to jedno spotkanie.</strong> Nie trzeba czytać więcej niż jeden na raz.</li>
  <li><strong>Struktura jest stała.</strong> Pięć kroków wraca w tej samej kolejności – to obniża
      napięcie i pozwala przewidzieć, co będzie dalej.</li>
  <li><strong>Pytania nie są sprawdzianem.</strong> „Nie wiem” jest pełną odpowiedzią. Można
      odpowiadać pisemnie, ustnie, rysunkiem albo liczbą pokazaną na palcach.</li>
  <li><strong>Emocje opisano przez ciało</strong>, a nie przez mimikę innych osób. To celowe:
      rozpoznawanie emocji zaczyna się od sygnałów z własnego ciała.</li>
  <li><strong>Język jest dosłowny.</strong> Bez ironii, bez przenośni bez wyjaśnienia,
      bez pytań podchwytliwych.</li>
  <li><strong>Skala 0–10</strong> ze strony 8 wraca w wielu rozdziałach. Warto ustalić ją raz
      i używać także poza broszurą.</li>
  <li><strong>Tempo należy do czytelnika.</strong> Przerwa w połowie rozdziału nie psuje pracy.</li>
  <li><strong>Wracanie do rozdziału</strong> jest wskazane. Ta broszura nie jest do przeczytania raz.</li>
</ul>
<div class="uwaga-panel">
  <p class="etykieta">Na co zwrócić uwagę podczas czytania</p>
  <p>Jeśli czytelnik przerywa w połowie zdania, odwraca wzrok albo zaczyna się kołysać –
  to nie jest brak zainteresowania. To zwykle sygnał, że bodźców jest za dużo. Wtedy pomaga
  przerwa, ruch albo zamknięcie książeczki do jutra.</p>
  <p>Jeśli wraca do jednego rozdziału wiele razy – to dobry znak. Powtarzanie jest tu formą
  uczenia się, dokładnie tak, jak opisuje to rozdział ósmy.</p>
  <p>Jeśli odpowiada „nie wiem” na wszystkie pytania – nie naciskaj. Można wrócić do nich
  za tydzień albo odpowiedzieć razem, na głos, zaczynając od własnej odpowiedzi dorosłego.</p>
</div>''')

# ======================================================= 50. NOTA
strona(pagina='Dodatki', html='''
<h2 class="dzial-tytul">Nota o cytatach i źródłach</h2>
<p class="lead">Uczciwie o tym, co pochodzi wprost od bohatera, a co zostało mu przypisane.</p>
%s''' % ''.join('<div class="nota-grupa"><p class="etykieta">%s</p><p class="t">%s</p></div>'
                % (t, o) for t, o in D['nota']))

# ======================================================= 51. NOTATKI
strona(pagina='Dodatki', html='''
<h2 class="dzial-tytul">Moje notatki</h2>
<p class="lead">Miejsce na Twoje zdanie, Twój rysunek albo jedną liczbę od 0 do 10.</p>
<div class="linie">%s</div>''' % ('<span class="linia-do-pisania"></span>' * 22))

# ======================================================= 52–59. ZAŁĄCZNIK: GRA
G = D['gra']
def karta_gry(k):
    return ('<li class="karta-gry"><div class="kg-gora"><span class="kg-nr">%d</span>'
            '<span class="kg-emocja">%s</span></div><p class="kg-pytanie">%s</p>'
            '<div class="kg-dol"><span>Nie chcesz? Powiedz <strong>PAS</strong>.</span>'
            '<span>str. %d</span></div></li>') % tuple(k)

strona(pagina='Załącznik · gra', html='''
<p class="etykieta">Załącznik</p>
<h2 class="dzial-tytul">%s</h2>
<p class="lead">%s</p>
%s
<div class="karty-4 karty-plaskie">
  <div class="karta-mini"><p class="km-t">Dla kogo</p><p class="km-o">Dla młodzieży w spektrum autyzmu,
    samodzielnie albo z osobą dorosłą.</p></div>
  <div class="karta-mini"><p class="km-t">Ile osób</p><p class="km-o">Od 1 do 4. Wersja dla jednej osoby
    jest na stronie 59.</p></div>
  <div class="karta-mini"><p class="km-t">Ile trwa</p><p class="km-o">Około 20–30 minut. Można przerwać
    w dowolnym momencie i wrócić później.</p></div>
  <div class="karta-mini"><p class="km-t">Co potrzebujesz</p><p class="km-o">Nożyczek, kleju i pionków —
    pionkiem może być gumka, moneta albo klocek.</p></div>
</div>
<div class="na-koncu">
  <p class="etykieta">Co wytniesz z tego załącznika</p>
  <ol>
    <li><span>Plansza — dwadzieścia pól</span><span>str. 54</span></li>
    <li><span>Kostka miary — do sklejenia</span><span>str. 55</span></li>
    <li><span>Kostka emocji — do sklejenia</span><span>str. 56</span></li>
    <li><span>Dwanaście kart z pytaniami</span><span>str. 57–58</span></li>
    <li><span>Żetony w kształcie listków</span><span>str. 56</span></li>
  </ol>
</div>''' % (G['tytul'], G['lead'], figura(gra.kostka_ilustracja(), None, None, 'ilu-scena')))

strona(pagina='Załącznik · gra', html='''
<h2 class="dzial-tytul">Zasady gry krok po kroku</h2>
<p class="lead">Kolejność jest zawsze taka sama. Możesz do niej wracać w trakcie gry.</p>
<ol class="zasady-gry">
  <li><span class="zg-nr">1</span><span>Każdy stawia swój pionek na polu <strong>START</strong>.</span></li>
  <li><span class="zg-nr">2</span><span>Zaczyna osoba, która ostatnia miała urodziny. Potem kolej idzie w prawo.</span></li>
  <li><span class="zg-nr">3</span><span>Rzuć <strong>kostką miary</strong>. Liczba mówi, o ile pól przesuwasz pionek.</span></li>
  <li><span class="zg-nr">4</span><span>Przeczytaj, jakie to pole. Na polu z numerem weź <strong>kartę</strong>
      o tym samym numerze.</span></li>
  <li><span class="zg-nr">5</span><span>Przeczytaj pytanie z karty i odpowiedz. Możesz też powiedzieć
      <strong>„pas”</strong> — to jest ruch zgodny z zasadami.</span></li>
  <li><span class="zg-nr">6</span><span>Spójrz na słowo z kostki: <em>za mało</em>, <em>właściwa miara</em>
      albo <em>za dużo</em>. Powiedz jedno zdanie o tym, ile tej emocji było w Twojej sytuacji.
      Jeśli słowo z kostki pasuje do Twojej odpowiedzi — weź dodatkowy listek.</span></li>
  <li><span class="zg-nr">7</span><span>Za każdą turę bierzesz <strong>jeden listek</strong>. Za „pas” też.</span></li>
  <li><span class="zg-nr">8</span><span>Gra kończy się, gdy wszyscy dojdą do <strong>METY</strong>.
      Każdy mówi, ile ma listków — i to wszystko. Nikt nie wygrywa i nikt nie przegrywa.</span></li>
</ol>
<div class="uwaga-panel">
  <p class="etykieta">Zasady wsparcia — obowiązują wszystkich</p>
  <p>Nie ma limitu czasu. Można myśleć długo i nikt nie pogania.</p>
  <p>„Pas” nic nie kosztuje i nikt o niego nie dopytuje.</p>
  <p>Można odpowiedzieć jednym słowem, liczbą albo pokazać ją na palcach.</p>
  <p>Nikt nie komentuje cudzej odpowiedzi. Wolno powiedzieć tylko „dziękuję”.</p>
  <p>Można przerwać grę i wrócić później — zaznacz ołówkiem pole, na którym stoisz.</p>
</div>''')

strona(pagina='Załącznik · plansza', klasa='plansza-strona', html='''
<h2 class="dzial-tytul">Plansza</h2>
%s
<div class="siatka-pola">
  <div class="pole-opis pole-e"><p class="po-t">Pole z numerem</p>
    <p class="po-o">Weź kartę o tym samym numerze i odpowiedz na pytanie.</p></div>
  <div class="pole-opis pole-w"><p class="po-t">Pole z wieńcem</p>
    <p class="po-o">Rzuć kostką emocji i opowiedz o emocji, która wypadła. Karty nie bierzesz.</p></div>
  <div class="pole-opis pole-p"><p class="po-t">Pole PRZERWA</p>
    <p class="po-o">Nic nie robisz. To pełnoprawny ruch, a nie strata tury.</p></div>
</div>''' % figura(gra.plansza(G['plansza_emocje']), None,
   'Dwadzieścia pól. Dwanaście z nich to spotkania z tej książeczki, cztery to pola z wieńcem, dwa to przerwy.',
   'ilu-info'))

strona(pagina='Załącznik · kostki', html='''
<h2 class="dzial-tytul">Kostka miary</h2>
<p class="lead">%s</p>
%s
<div class="ramka-wskazowka">
  <p class="etykieta">Jak skleić</p>
  <p class="t">Wytnij po linii ciągłej. Zegnij po wszystkich liniach przerywanych — najpierw w jedną stronę,
  potem w drugą, żeby papier się zmiękczył. Posmaruj klejem tylko szare klapki i sklejaj po kolei:
  najpierw pierścień z czterech ścian, potem górę, na końcu dół. Przytrzymaj każdą krawędź przez chwilę.</p>
</div>''' % (G['kostka_miary_lead'], figura(gra.siatka_kostki(
    [('2 · właściwa miara', 'idziesz o 2 pola'), ('1 · za mało', 'idziesz o 1 pole'),
     ('3 · za dużo', 'idziesz o 3 pola'), ('2 · za dużo', 'idziesz o 2 pola'),
     ('1 · właściwa miara', 'idziesz o 1 pole'), ('3 · za mało', 'idziesz o 3 pola')],
    'Kostka miary — wytnij i sklej', 'var(--szafran-tlo)'), None, None, 'ilu-info')))

strona(pagina='Załącznik · kostki', html='''
<h2 class="dzial-tytul">Kostka emocji i żetony</h2>
<p class="lead">Kostki emocji używasz na polach z wieńcem. Listki to żetony — jeden za każdą turę.</p>
%s
%s''' % (figura(gra.siatka_kostki([tuple(x) for x in G['kostka_emocji']],
                                  'Kostka emocji — wytnij i sklej', 'var(--oliwka-tlo)'),
                None, None, 'ilu-info kostka-mala'),
         figura(gra.zetony(18), 'Żetony · listki',
                'Wytnij osiemnaście listków. Jeśli zabraknie, użyjcie guzików albo fasolek.', 'ilu-info')))

for i, zakres in ((0, 'Karty 1–6'), (6, 'Karty 7–12')):
    strona(pagina='Załącznik · karty', html='''
<h2 class="dzial-tytul">%s</h2>
<p class="lead">Wytnij wzdłuż przerywanych linii. Odłóż karty numerem do góry, w jednym stosie.</p>
<ol class="karty-gry">%s</ol>''' % (zakres, ''.join(karta_gry(k) for k in G['karty'][i:i + 6])))

strona(pagina='Załącznik · gra', html='''
<h2 class="dzial-tytul">Gra dla jednej osoby</h2>
<p class="lead">Wszystko działa tak samo, tylko rzucasz sam. Zamiast opowiadać komuś — zapisujesz.
Możesz przejść całą planszę jednego dnia albo po jednym polu dziennie.</p>
<div class="przewijalne">
<table class="tabela-solo">
  <thead><tr><th>Pole</th><th>Emocja</th><th>Moja odpowiedź — jedno słowo wystarczy</th><th>Siła 0–10</th></tr></thead>
  <tbody>%s</tbody>
</table>
</div>
<div class="uwaga-panel">
  <p class="etykieta">Po skończonej grze</p>
  <p>Popatrz na kolumnę z liczbami. Która emocja miała u Ciebie najwyższą siłę? Która najniższą?</p>
  <p>Nie musisz nic z tym robić. Sama wiedza o tym, co i jak mocno czujesz, jest już wynikiem gry —
  filozofowie nazwaliby ją poznaniem samego siebie.</p>
</div>''' % ''.join('<tr><td>%d</td><td class="pole-pisania">&nbsp;</td>'
                    '<td class="pole-pisania">&nbsp;</td><td class="pole-pisania">&nbsp;</td></tr>' % n
                    for n in range(1, 13)))

# ======================================================= 60. TYLNA OKŁADKA
T = D['tyl_okladki']
strona(klasa='tyl', html='''
<div class="tyl-gora">
  <div class="tyl-logo">%s</div>
  <h2 class="tyl-tytul">%s</h2>
</div>
<div class="tyl-tresc">
  <p class="tyl-lead">%s</p>
  <ul class="tyl-lista">%s</ul>
  <blockquote class="tyl-cytat"><p>„%s”</p><cite>%s</cite></blockquote>
  <div class="tyl-emocje">
    <p class="etykieta">Dwanaście emocji tej książeczki</p>
    <ul>%s</ul>
  </div>
</div>
<div class="tyl-dol">
  <div class="tyl-kod">
    <svg viewBox="0 0 200 80" role="img" aria-label="Miejsce na kod kreskowy">
      <rect x="0" y="0" width="200" height="80" fill="#FFFFFF" stroke="var(--linia)" stroke-width="2"/>
      <g fill="var(--atrament)">%s</g>
    </svg>
    <p class="tyl-isbn">ISBN · cena</p>
  </div>
  <div class="tyl-wydawca"><div class="pctp-znak">%s</div>
    <p><strong>%s</strong><br>miejsce na adres<br>i stronę internetową</p></div>
</div>''' % (LOGO_POZ, M['tytul_plaski'], T['lead'],
             ''.join('<li>%s</li>' % p for p in T['punkty']), T['cytat'], T['cytat_zrodlo'],
             ''.join('<li>%s</li>' % e for e in G['plansza_emocje']),
             ''.join('<rect x="%d" y="12" width="%d" height="48"/>' % (12 + i * 9, 2 + (i % 3))
                     for i in range(20)),
             PCTP(), M['wydawca_skrot']))

# ---------------------------------------------------------------- typografia polska
def _tekst(s, in_svg):
    if not s.strip(): return s
    s = s.replace('—', '–').replace('...', '…')
    if in_svg: return s
    s = re.sub(r'(?<![\w„”])([aiouwzAIOUWZ])\s+(?=[\wĄĆĘŁŃÓŚŹŻąćęłńóśźż„])', '\\1\u00A0', s)
    s = re.sub(r'(\d)\s+(?=(?:p\.n\.e\.|lat|roku|zdań|pytań|stron))', '\\1\u00A0', s)
    return s

def popraw_typografie(html):
    """Wiąże jednoliterowe wyrazy z następnym słowem (polska zasada „bez sierotek”),
    zamienia pauzę na półpauzę i skleja wielokropek. Omija atrybuty i wnętrze <svg>,
    bo twarda spacja w danych ścieżki zepsułaby rysunek."""
    out, i, n, in_svg = [], 0, len(html), False
    while i < n:
        lt = html.find('<', i)
        if lt == -1:
            out.append(_tekst(html[i:], in_svg)); break
        out.append(_tekst(html[i:lt], in_svg))
        gt = html.find('>', lt)
        tag = html[lt:gt + 1]
        low = tag.lower()
        if low.startswith('<svg'): in_svg = True
        elif low.startswith('</svg'): in_svg = False
        out.append(tag)
        i = gt + 1
    return ''.join(out)

# ---------------------------------------------------------------- montaż
CSS = open(os.path.join(TU, 'styl.css'), encoding='utf-8').read()
strony_html = []
for idx, (klasa, pagina, tresc) in enumerate(STRONY):
    numer = idx + 1
    kl = 'strona ' + klasa + (' prawa' if numer % 2 else ' lewa')
    if klasa in ('okladka', 'tyl'):
        strony_html.append('<section class="%s" data-nr="%d">%s</section>' % (kl, numer, tresc))
        continue
    if klasa in ('tytulowa', 'redakcyjna'):
        glowa, stopka = '<div class="zywa-pagina pusta"></div>', '<div class="stopka-strony pusta"></div>'
    else:
        glowa = ('<div class="zywa-pagina"><span class="zp-l">'
                 '<span class="zp-znak"><svg viewBox="-4 -4 72 72" aria-hidden="true">'
                 '<use href="#znak-serii"/></svg></span>%s · %s</span>'
                 '<span class="zp-p">%s</span></div>' % (M['seria'], M['tytul_plaski'], pagina))
        stopka = ('<div class="stopka-strony"><span class="ss-znak">·</span>'
                  '<span class="ss-nr">%d</span></div>' % numer)
    strony_html.append('<section class="%s" data-nr="%d">%s<div class="strona-tresc">%s</div>%s</section>'
                       % (kl, numer, glowa, tresc, stopka))

SYMBOL = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true">'
          '<symbol id="znak-serii" viewBox="-4 -4 72 72">%s</symbol></svg>'
          % re.sub(r'</?svg[^>]*>', '', ZNAK))
body = popraw_typografie('<div class="ksiazka">\n%s\n%s\n</div>' % (SYMBOL, '\n'.join(strony_html)))
FRAG = ('<title>%s</title>\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
        'family=Alegreya+Sans:ital,wght@0,400;0,500;0,700;0,800;1,400&'
        'family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&display=swap">\n'
        '<style>\n%s</style>\n\n%s\n' % (M['tytul_plaski'], CSS, body))
os.makedirs(WYJSCIE, exist_ok=True)
open(os.path.join(WYJSCIE, 'broszura.html'), 'w', encoding='utf-8').write(FRAG)

zdan = sum(len(r[k]) for r in ROZ for k in ('scena', 'mysl', 'emocja', 'zycie')) + len(D['wstep']['zdania'])
print('stron: %d | zdań opowiadania: %d | pytań: %d' %
      (len(STRONY), zdan, sum(len(r['pytania']) for r in ROZ)))
print('zapisano:', os.path.join(WYJSCIE, 'broszura.html'))
