# -*- coding: utf-8 -*-
"""Skład broszury 'Spotkanie z Arystotelesem' — makieta A4, strony o stałym rozmiarze."""
import json, re, sys, io
import os
TU = os.path.dirname(os.path.abspath(__file__))
WYJSCIE = os.path.dirname(TU)
CACHE = os.path.join(TU, 'fonty')

D = json.load(open(os.path.join(TU,'tresc.json'), encoding='utf-8'))
ROZ, SVGS = D['rozdzialy'], D['svgs']
def svg(pref):
    for k, v in SVGS.items():
        if k.startswith(pref): return v
    raise KeyError(pref)

def wczytaj_logo(nazwa):
    """Wstawia plik z katalogu logo/ jako kod SVG, z kolorami na tokenach palety."""
    s = open(os.path.join(WYJSCIE, 'logo', nazwa), encoding='utf-8').read()
    s = re.sub(r'<\?xml[^>]*\?>', '', s)
    s = re.sub(r'\s(?:width|height)="[^"]*"', '', s.split('>', 1)[0]) + '>' + s.split('>', 1)[1]
    s = s.replace('<g id="logo">', '<g>')
    wczytaj_logo.licznik = getattr(wczytaj_logo, 'licznik', 0) + 1
    for stary in set(re.findall(r'id="([\w-]+)"', s)):
        nowy = '%s-%d' % (stary, wczytaj_logo.licznik)
        s = s.replace('id="%s"' % stary, 'id="%s"' % nowy).replace('#%s)' % stary, '#%s)' % nowy)
    for hexa, token in (('#1E5A6B', 'var(--morze)'), ('#B07E13', 'var(--szafran)'),
                        ('#5C7A49', 'var(--oliwka)'), ('#1F2E33', 'var(--atrament)')):
        s = s.replace(hexa, token)
    return s.strip()

ZNAK = wczytaj_logo('mala-filozofia-znak.svg')
LOGO_POZ = wczytaj_logo('mala-filozofia-logo-poziome.svg')
LOGO_PION = wczytaj_logo('mala-filozofia-logo-pionowe.svg')
PCTP = lambda: wczytaj_logo('pctp-logo.svg')

ORNAMENT = """<svg viewBox="0 0 160 24" role="img" aria-label="Ozdobnik: trzy listki oliwne">
  <g fill="var(--oliwka)" opacity=".8">
    <ellipse cx="80" cy="12" rx="11" ry="5"/>
    <ellipse cx="60" cy="12" rx="8" ry="4" transform="rotate(-14 60 12)"/>
    <ellipse cx="100" cy="12" rx="8" ry="4" transform="rotate(14 100 12)"/>
  </g>
  <g stroke="var(--linia)" stroke-width="1.4"><path d="M4 12 H44"/><path d="M116 12 H156"/></g>
</svg>"""

ORD = [None,'pierwsze','drugie','trzecie','czwarte','piąte','szóste',
       'siódme','ósme','dziewiąte','dziesiąte','jedenaste','dwunaste']

def akapity(zdania, podzial, klasa='t'):
    """Łączy zdania w akapity o zadanych rozmiarach."""
    assert sum(podzial) == len(zdania), (sum(podzial), len(zdania))
    out, i = [], 0
    for n in podzial:
        out.append('<p class="%s">%s</p>' % (klasa, ' '.join(zdania[i:i+n])))
        i += n
    return '\n'.join(out)

# ---------------------------------------------------------------- strony
STRONY = []      # (klasa, zywa_pagina_prawa, html)
def strona(html, pagina='', klasa=''):
    STRONY.append((klasa, pagina, html))

def figura(s, etykieta=None, podpis=None, klasa=''):
    h = '<figure class="ilustracja %s">' % klasa
    if etykieta: h += '<p class="etykieta">%s</p>' % etykieta
    h += s
    if podpis: h += '<figcaption>%s</figcaption>' % podpis
    return h + '</figure>'

# ======================================================= 1. OKŁADKA
strona(klasa='okladka', html='''
<div class="okl-gora">
  <div class="okl-logo">%s</div>
  <p class="okl-tom">Tom pierwszy</p>
</div>
<div class="okl-obraz">%s</div>
<div class="okl-dol">
  <h1>Spotkanie<br>z Arystotelesem</h1>
  <p class="okl-podtytul">Opowiadanie o filozofie, który uczył ludzi nazywać to, co czują</p>
  <div class="okl-pasek">
    <span>12 spotkań</span><span>12 emocji</span><span>60 pytań</span>
  </div>
  <div class="okl-wydawca"><div class="pctp-znak">%s</div><p>Wydawca<br><strong>PCTP</strong></p></div>
</div>''' % (LOGO_POZ, svg('Portret Arystotelesa'), PCTP()))

# ======================================================= 2. STRONA TYTUŁOWA
strona(klasa='tytulowa', html='''
<div class="tyt-blok">
  <div class="tyt-logo">%s</div>
  <p class="tyt-seria">Tom pierwszy</p>
  <h1 class="tyt-glowny">Spotkanie<br>z Arystotelesem</h1>
  <div class="tyt-ornament">%s</div>
  <p class="tyt-pod">Opowiadanie o filozofie,<br>który uczył ludzi nazywać to, co czują</p>
  <p class="tyt-adres">Broszura edukacyjna dla młodzieży w spektrum autyzmu</p>
</div>
<div class="tyt-stopka"><span>12 spotkań</span><span>12 emocji</span><span>60 pytań</span></div>
<div class="tyt-wydawca"><div class="pctp-znak">%s</div>
  <p><strong>PCTP</strong><br>miejsce na pełną nazwę i adres wydawcy</p></div>''' % (LOGO_PION, '''
<svg viewBox="0 0 300 60" role="img" aria-label="Gałązka oliwna">
  <path d="M20 30 H280" stroke="var(--linia)" stroke-width="2"/>
  <g fill="var(--oliwka)">
    <ellipse cx="122" cy="22" rx="15" ry="7" transform="rotate(-22 122 22)"/>
    <ellipse cx="150" cy="16" rx="15" ry="7"/>
    <ellipse cx="178" cy="22" rx="15" ry="7" transform="rotate(22 178 22)"/>
    <ellipse cx="134" cy="40" rx="13" ry="6" transform="rotate(20 134 40)"/>
    <ellipse cx="166" cy="40" rx="13" ry="6" transform="rotate(-20 166 40)"/>
  </g>
  <circle cx="150" cy="30" r="5" fill="var(--szafran)"/>
</svg>''', PCTP()))

# ======================================================= 3. STRONA REDAKCYJNA
strona(klasa='redakcyjna', html='''
<div class="red-gora">
  <div class="red-znak">%s</div>
  <div>
    <p class="red-tytul">Spotkanie z Arystotelesem</p>
    <p class="red-seria">Seria „Mała Filozofia”, tom 1</p>
  </div>
</div>
<dl class="metryka">
  <dt>Przeznaczenie</dt><dd>Broszura edukacyjna dla młodzieży w spektrum autyzmu oraz dla osób,
    które z nią pracują: rodziców, nauczycieli, terapeutów.</dd>
  <dt>Zawartość</dt><dd>12 rozdziałów · 450 zdań opowiadania · 60 pytań · 8 infografik ·
    karta emocji do wycięcia · słowniczek.</dd>
  <dt>Wydanie</dt><dd>Pierwsze</dd>
  <dt>Tekst i opracowanie</dt><dd>&nbsp;</dd>
  <dt>Ilustracje i skład</dt><dd>&nbsp;</dd>
  <dt>Wydawca</dt><dd class="dd-wydawca"><span class="pctp-znak">%s</span>
    <span><strong>PCTP</strong> · miejsce na pełną nazwę, adres i stronę internetową</span></dd>
  <dt>ISBN</dt><dd>&nbsp;</dd>
</dl>
<div class="red-nota">
  <p class="t">Sceny w rozdziałach są opowiadaniem. Fakty z życia Arystotelesa – daty, miejsca,
  tytuły ksiąg, treść testamentu – są zgodne z relacjami starożytnych. Dialogi zostały napisane
  na potrzeby tej broszury. Pełną notę o cytatach znajdziesz na stronie 50.</p>
</div>
<div class="red-kroje">
  <p><strong>Kroje pisma:</strong> Atkinson Hyperlegible (Braille Institute of America) –
  zaprojektowany dla osób z trudnościami w czytaniu; Alegreya Sans (Huerta Tipográfica).
  Oba na licencji SIL Open Font License 1.1.</p>
  <p><strong>Format:</strong> A4, 52 strony, druk dwustronny.</p>
</div>
<p class="red-copy">© Wszystkie prawa zastrzeżone. Kopiowanie całości lub fragmentów
w celach komercyjnych wymaga zgody wydawcy. Karty i strony do wypełnienia wolno
kopiować na własny użytek.</p>''' % (ZNAK, PCTP()))

# ======================================================= 4. SPIS TREŚCI
def poz(t, s, klasa=''):
    return ('<li class="tresc-poz %s"><span class="tresc-nazwa">%s</span>'
            '<span class="kropki"></span><span class="str">%s</span></li>') % (klasa, t, s)

P0 = 9                       # pierwsza strona rozdziału 1
strony_roz = {r['nr']: P0 + (r['nr'] - 1) * 3 for r in ROZ}
spis = ['<li class="tresc-dzial">Zanim zaczniesz</li>',
        poz('Ta książeczka czyta się powoli', 5),
        poz('Każdy rozdział ma te same pięć części', 6),
        poz('Życie Arystotelesa w ośmiu punktach <em>· infografika</em>', 7),
        poz('Termometr emocji <em>· infografika</em>', 8),
        '<li class="tresc-dzial">Dwanaście spotkań</li>']
for r in ROZ:
    spis.append(poz('<span class="tresc-nr">%d</span> %s <em>· %s</em>'
                    % (r['nr'], r['tytul'], r['emocja_label'].lower()), strony_roz[r['nr']], 'roz'))
spis += ['<li class="tresc-dzial">Dodatki</li>',
         poz('Dwanaście zdań na dwanaście emocji', 45),
         poz('Moja karta emocji <em>· do wycięcia</em>', 47),
         poz('Słowniczek', 48),
         poz('Jak pracować z tą broszurą <em>· dla dorosłych</em>', 49),
         poz('Nota o cytatach i źródłach', 50),
         poz('Moje notatki', 51)]
strona(klasa='spis', pagina='Spis treści', html=
       '<h2 class="dzial-tytul">Spis treści</h2><ol class="tresc">%s</ol>' % '\n'.join(spis))

# ======================================================= 5. ZANIM ZACZNIESZ
INTRO = ['Ta broszura jest opowiadaniem.',
 'Poznasz w niej człowieka, który żył bardzo dawno temu i nazywał się Arystoteles.',
 'Arystoteles całe życie przyglądał się światu i ludziom.',
 'Najbardziej ciekawiło go to, co czujemy w środku.',
 'W każdym rozdziale spotkasz jedną jego myśl i jedną emocję.',
 'Czytaj w swoim tempie i wracaj do miejsc, które Ci się spodobały.']
strona(pagina='Zanim zaczniesz', html='''
<h2 class="dzial-tytul">Ta książeczka czyta się powoli</h2>
%s
<figure class="frontispis">%s<figcaption>Arystoteles ze Stagiry · 384–322 p.n.e.</figcaption></figure>
<div class="zasady">
  <p class="etykieta">Zasady, które obowiązują w tej broszurze</p>
  <ul class="lista">
    <li>Możesz nie odpowiadać na pytanie. Wolno przejść dalej.</li>
    <li>Możesz odpowiedzieć jednym słowem. To jest pełna odpowiedź.</li>
    <li>Możesz czytać z kimś dorosłym albo całkiem sam.</li>
    <li>Możesz zrobić przerwę po każdym rozdziale. Przerwa nie jest porażką.</li>
    <li>Nie musisz nic czuć „na zawołanie”. Emocje przychodzą same.</li>
  </ul>
</div>''' % (akapity(INTRO, [3, 3]), svg('Portret Arystotelesa')))

# ======================================================= 6. STRUKTURA ROZDZIAŁU
strona(pagina='Zanim zaczniesz', html='''
<h2 class="dzial-tytul">Każdy rozdział ma te same pięć części</h2>
<p class="lead">Kolejność nigdy się nie zmienia. Zawsze wiesz, co będzie dalej.</p>
<ol class="kroki">
  <li><span class="krok-cyfra">1</span><span class="krok-nazwa">Scena</span>
      <span class="krok-opis">Krótka historia z życia Arystotelesa.</span></li>
  <li><span class="krok-cyfra">2</span><span class="krok-nazwa">Myśl Arystotelesa</span>
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
    <li><span>Dwanaście zdań Arystotelesa do wycięcia</span><span>str. 45</span></li>
    <li><span>Moja karta emocji – do noszenia w piórniku</span><span>str. 47</span></li>
    <li><span>Słowniczek trudnych słów</span><span>str. 48</span></li>
    <li><span>Miejsce na Twoje notatki</span><span>str. 51</span></li>
  </ol>
</div>''')

# ======================================================= 7. OŚ CZASU
strona(pagina='Zanim zaczniesz', html='''
<h2 class="dzial-tytul">Życie Arystotelesa w ośmiu punktach</h2>
<p class="lead">Skrót „p.n.e.” znaczy: przed naszą erą. Im większa liczba, tym dawniej.</p>
%s
<div class="karty-4">
  <div class="karta-mini"><p class="km-t">Skąd pochodził</p><p class="km-o">Ze Stagiry – małego miasta na północy Grecji, blisko morza.</p></div>
  <div class="karta-mini"><p class="km-t">Kim był jego ojciec</p><p class="km-o">Lekarzem. Dlatego Arystoteles od dziecka oglądał kości, zioła i narzędzia.</p></div>
  <div class="karta-mini"><p class="km-t">Co robił najczęściej</p><p class="km-o">Patrzył, liczył, zapisywał. Opisał ponad 500 gatunków zwierząt.</p></div>
  <div class="karta-mini"><p class="km-t">Dlaczego jest tu ważny</p><p class="km-o">Ułożył pierwszą w Europie listę emocji i wyjaśnił, skąd się biorą.</p></div>
</div>''' % figura(svg('Oś czasu życia'), None,
    'Oś czasu czyta się od lewej do prawej. Lewa strona to początek życia, prawa – jego koniec.'))

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
    <tbody>
      <tr><td>0–2 · spokój</td><td class="pole">&nbsp;</td></tr>
      <tr><td>3–4 · lekko czuję</td><td class="pole">&nbsp;</td></tr>
      <tr><td>5–6 · wyraźnie czuję</td><td class="pole">&nbsp;</td></tr>
      <tr><td>7–8 · bardzo mocno</td><td class="pole">&nbsp;</td></tr>
      <tr><td>9–10 · za dużo, proszę o pomoc</td><td class="pole">&nbsp;</td></tr>
    </tbody>
  </table>
</div>''' % figura(svg('Termometr emocji'), None,
    'Arystoteles pisał to samo innymi słowami: liczy się nie to, że czujesz, ale ile i kiedy.'))

# ======================================================= 9–44. ROZDZIAŁY
for r in ROZ:
    n, tyt = r['nr'], r['tytul']
    pagina = '%d · %s' % (n, tyt)
    # --- strona A: otwarcie + ilustracja + scena
    tabela_html = ''
    fig = figura(r['svg'], r['fig_etykieta'], r['fig_caption'],
                 'ilu-rozdzial ' + ('ilu-info' if r['fig_etykieta'] else 'ilu-scena'))
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
%s''' % (ORD[n], n, tyt, r['emocja_label'].lower(), fig,
     akapity(r['scena'], [4, 4, 3, 3]),
     '' if r['fig_etykieta'] else '<div class="ornament">%s</div>' % ORNAMENT))

    # --- strona B: cytat + myśl (+ tabela w rozdz. 7)
    if r['tabela']:
        t = r['tabela']
        # skracamy do trzech wierszy, żeby strona oddychała
        wiersze = re.findall(r'<tr>(?!.*?<th).*?</tr>', t, re.S)
        body = re.search(r'<tbody>(.*?)</tbody>', t, re.S).group(1)
        rows = re.findall(r'<tr>.*?</tr>', body, re.S)[:3]
        head = re.search(r'<thead>.*?</thead>', t, re.S).group(0)
        tabela_html = ('<div class="tabela-blok"><p class="etykieta">Ten sam pomysł w codziennych sprawach</p>'
                       '<table class="tab-srodek">%s<tbody>%s</tbody></table></div>' % (head, ''.join(rows)))
    strona(pagina=pagina, html='''
<blockquote class="cytat">
  <p class="cytat-tekst">%s</p>
  <p class="cytat-zrodlo">%s</p>
</blockquote>
<section class="czesc">
  <h3 class="czesc-tytul"><span class="cz-nr">2</span>Myśl Arystotelesa</h3>
  %s
</section>
<section class="czesc blok-emocja">
  <h3 class="czesc-tytul"><span class="cz-nr">3</span>Emocja</h3>
  <p class="emocja-nazwa">%s</p>
  %s
</section>''' % (r['cytat'], r['cytat_zrodlo'], akapity(r['mysl'], [4, 3, 3]),
                 r['emocja_nazwa'], akapity(r['emocja'], [4, 3])))

    # --- strona C: emocja + w Twoim życiu + pytania
    pyt = '\n'.join('<li><span class="p-nr">%s</span><span class="p-tresc">%s</span></li>' % (a, b)
                    for a, b in r['pytania'])
    dopelnienie = tabela_html if tabela_html else ('''
<div class="odpowiedzi">
  <p class="etykieta">Miejsce na Twoją odpowiedź</p>
  <div class="linie-odp">%s</div>
</div>''' % ('<span class="linia-do-pisania"></span>' * 5))
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
HASLA = [
 (1,'ciekawość','Wszyscy ludzie z natury dążą do poznania.','Chcieć wiedzieć to normalne.'),
 (2,'niepewność','Poznanie samego siebie jest początkiem mądrości.','Wolno być na początku drogi.'),
 (3,'napięcie sporu','Przyjacielem Platon, lecz większym przyjacielem prawda.','Można kogoś lubić i mieć inne zdanie.'),
 (4,'zachwyt','W każdej rzeczy naturalnej jest coś godnego podziwu.','Twoja dziedzina jest ważna.'),
 (5,'duma','Korzenie edukacji są gorzkie, ale owoc słodki.','Trudny początek to jeszcze nie porażka.'),
 (6,'ulga','Tego, czego mamy się nauczyć, uczymy się, robiąc to.','Pierwsze próby mają prawo być niezgrabne.'),
 (7,'strach','Cnota jest środkiem między dwiema wadami.','Sprawdź miarę, nie samą emocję.'),
 (8,'zniechęcenie','Stajemy się odważni, czyniąc rzeczy odważne.','Sto prób zmienia bardzo dużo.'),
 (9,'samotność','Przyjaciel to jedna dusza mieszkająca w dwóch ciałach.','Jeden prawdziwy przyjaciel to dużo.'),
 (10,'gniew','Rozgniewać się dobrze – to nie jest łatwe.','Zapytaj siebie: po co jestem zły?'),
 (11,'nadzieja','Jedna jaskółka nie czyni wiosny.','Jeden zły dzień to jeszcze nie całe życie.'),
 (12,'smutek','Nie pozwolę zgrzeszyć przeciw filozofii po raz drugi.','Odejście też bywa mądrą decyzją.')]
def karta_hasla(h):
    return ('<li class="haslo"><span class="h-nr">%d</span><p class="h-emocja">%s</p>'
            '<p class="h-cytat">„%s”</p><p class="h-po">%s</p></li>') % h
for i, tytul in ((0, 'Dwanaście zdań na dwanaście emocji'), (6, 'Dwanaście zdań na dwanaście emocji')):
    strona(pagina='Dodatki', html='''
<h2 class="dzial-tytul">%s</h2>
<p class="lead">%s</p>
<ol class="hasla">%s</ol>''' % (tytul,
      'Spotkania 1–6. Możesz wyciąć jedno pole i powiesić je na ścianie.' if i == 0
      else 'Spotkania 7–12. Wybierz to zdanie, które dziś do Ciebie pasuje.',
      '\n'.join(karta_hasla(h) for h in HASLA[i:i+6])))

# ======================================================= 47. KARTA EMOCJI
strona(pagina='Dodatki', html='''
<h2 class="dzial-tytul">Moja karta emocji</h2>
<p class="lead">Cztery kroki Arystotelesa w wersji kieszonkowej. Wytnij wzdłuż przerywanej linii –
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
</div>''' % figura(svg('Karta kieszonkowa')))

# ======================================================= 48. SŁOWNICZEK
SLOWNIK = [
 ('Filozofia','Zadawanie pytań o to, jak wygląda świat i jak dobrze żyć. Po grecku: „miłość mądrości”.'),
 ('Akademia','Szkoła Platona w Atenach. Arystoteles uczył się w niej dwadzieścia lat.'),
 ('Likejon','Szkoła założona przez Arystotelesa. Uczono się w niej, spacerując.'),
 ('Perypatetycy','Uczniowie Arystotelesa. Nazwa znaczy mniej więcej „ci, którzy chodzą”.'),
 ('Cnota','Dobra cecha charakteru, wyćwiczona przez powtarzanie. Nie jest darem ani przypadkiem.'),
 ('Złoty środek','Właściwa miara między „za mało” a „za dużo”. Po grecku: mesotes.'),
 ('Hexis','Trwały nawyk. Coś, co robisz automatycznie, bo powtarzałeś to wiele razy.'),
 ('Eudajmonia','Szczęście rozumiane jako całe życie, które idzie dobrze. Nie chwilowy dobry humor.'),
 ('Retoryka','Sztuka mówienia. Arystoteles opisał w niej listę ludzkich emocji.'),
 ('Kitara','Starożytny instrument strunowy, podobny do liry.'),
 ('Zwój','Dawna książka: długi pas papirusu zwinięty w rulon.'),
 ('p.n.e.','Przed naszą erą. Im większa liczba, tym dawniej.')]
strona(pagina='Dodatki', html='''
<h2 class="dzial-tytul">Słowniczek</h2>
<p class="lead">Trudne słowa z tej broszury, wyjaśnione po kolei.</p>
<dl class="slownik">%s</dl>''' % '\n'.join('<dt>%s</dt><dd>%s</dd>' % s for s in SLOWNIK))

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

# ======================================================= 50. NOTA O CYTATACH
strona(pagina='Dodatki', html='''
<h2 class="dzial-tytul">Nota o cytatach i źródłach</h2>
<p class="lead">Uczciwie o tym, co pochodzi wprost od Arystotelesa, a co zostało mu przypisane.</p>
<div class="nota-grupa">
  <p class="etykieta">Cytaty z zachowanych dzieł</p>
  <p class="t">Zdania otwierające rozdziały <strong>1, 4, 6, 7, 8, 9, 10 i 11</strong> pochodzą
  z ksiąg Arystotelesa: „Metafizyki”, „O częściach zwierząt” oraz „Etyki nikomachejskiej”.
  Podano je w uproszczonym przekładzie, bliższym mowie codziennej niż przekładom naukowym.</p>
</div>
<div class="nota-grupa">
  <p class="etykieta">Myśli przypisywane</p>
  <p class="t">Zdania z rozdziałów <strong>2, 3, 5 i 12</strong> to myśli przypisywane Arystotelesowi
  przez późniejszych autorów. Nie ma ich dosłownie w jego księgach. Zaznaczono to pod każdym z nich.</p>
</div>
<div class="nota-grupa">
  <p class="etykieta">Sceny</p>
  <p class="t">Sceny w rozdziałach są opowiadaniem. Fakty – daty, miejsca, tytuły ksiąg, liczba
  opisanych gatunków, treść testamentu – pochodzą z relacji starożytnych, głównie od Diogenesa
  Laertiosa. Dialogi napisano na potrzeby tej broszury.</p>
</div>
<div class="nota-grupa">
  <p class="etykieta">Jeśli chcesz czytać dalej</p>
  <p class="t">Arystoteles, „Etyka nikomachejska” – księgi I, II, VIII i IX. To w nich znajdziesz
  złoty środek, naukę o nawyku, zdanie o gniewie i cały wykład o przyjaźni.</p>
</div>''')

# ======================================================= 51. NOTATKI
strona(pagina='Dodatki', html='''
<h2 class="dzial-tytul">Moje notatki</h2>
<p class="lead">Miejsce na Twoje zdanie, Twój rysunek albo jedną liczbę od 0 do 10.</p>
<div class="linie">%s</div>''' % ('<span class="linia-do-pisania"></span>' * 22))

# ======================================================= 52. TYLNA OKŁADKA
strona(klasa='tyl', html='''
<div class="tyl-gora">
  <div class="tyl-logo">%s</div>
  <h2 class="tyl-tytul">Spotkanie z Arystotelesem</h2>
</div>
<div class="tyl-tresc">
  <p class="tyl-lead">Dwa i pół tysiąca lat temu chłopiec ze Stagiry zapytał ojca, dlaczego kość
  ptaka jest lekka. Ojciec nie znał odpowiedzi. Tak zaczęła się historia człowieka, który pierwszy
  w Europie spisał listę ludzkich emocji.</p>
  <ul class="tyl-lista">
    <li>Dwanaście spotkań: od ciekawości, przez strach i gniew, aż po wdzięczność.</li>
    <li>Każdy rozdział ma zawsze te same pięć części – zawsze wiesz, co będzie dalej.</li>
    <li>Sześćdziesiąt pytań bez ocen. „Nie wiem” jest pełną odpowiedzią.</li>
    <li>Duże litery, dosłowny język, emocje opisane przez sygnały z własnego ciała.</li>
  </ul>
  <blockquote class="tyl-cytat">
    <p>„Każdy może się rozgniewać – to łatwe. Ale rozgniewać się na właściwą osobę,
    we właściwym stopniu, we właściwym czasie, we właściwym celu i we właściwy sposób –
    to nie jest łatwe.”</p>
    <cite>Arystoteles, „Etyka nikomachejska”</cite>
  </blockquote>
  <div class="tyl-emocje">
    <p class="etykieta">Dwanaście emocji tej książeczki</p>
    <ul><li>ciekawość</li><li>niepewność</li><li>napięcie sporu</li><li>zachwyt</li><li>duma</li><li>ulga</li><li>strach</li><li>zniechęcenie</li><li>samotność</li><li>gniew</li><li>nadzieja</li><li>wdzięczność</li></ul>
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
    <p><strong>PCTP</strong><br>miejsce na adres<br>i stronę internetową</p></div>
</div>''' % (LOGO_POZ,
       ''.join('<rect x="%d" y="12" width="%d" height="48"/>' % (12 + i * 9, 2 + (i % 3))
               for i in range(20)),
       PCTP()))

# ---------------------------------------------------------------- typografia PL
def popraw_typografie(html):
    """Wiąże jednoliterowe wyrazy z następnym słowem, myślniki, wielokropki.
    Działa wyłącznie na tekście – omija atrybuty i wnętrze <svg>."""
    out, i, n = [], 0, len(html)
    in_svg = False
    while i < n:
        lt = html.find('<', i)
        if lt == -1:
            out.append(_tekst(html[i:], in_svg)); break
        out.append(_tekst(html[i:lt], in_svg))
        gt = html.find('>', lt)
        tag = html[lt:gt+1]
        low = tag.lower()
        if low.startswith('<svg'): in_svg = True
        elif low.startswith('</svg'): in_svg = False
        out.append(tag)
        i = gt + 1
    return ''.join(out)

def _tekst(s, in_svg):
    if not s.strip(): return s
    s = s.replace('—', '–').replace('...', '…')
    if in_svg: return s
    s = re.sub(r'(?<![\w„”])([aiouwzAIOUWZ])\s+(?=[\wĄĆĘŁŃÓŚŹŻąćęłńóśźż„])', '\\1\u00A0', s)
    s = re.sub(r'(\d)\s+(?=(?:p\.n\.e\.|lat|roku|zdań|pytań|stron))', '\\1\u00A0', s)
    return s

# ---------------------------------------------------------------- montaż
CSS = open(os.path.join(TU,'styl.css'), encoding='utf-8').read()
strony_html = []
for idx, (klasa, pagina, tresc) in enumerate(STRONY):
    numer = idx + 1
    strona_klasa = 'strona ' + klasa + (' prawa' if numer % 2 else ' lewa')
    if klasa in ('okladka', 'tyl'):
        strony_html.append('<section class="%s" data-nr="%d">%s</section>' % (strona_klasa, numer, tresc))
        continue
    glowa = ''
    stopka = ''
    if klasa not in ('tytulowa', 'redakcyjna'):
        lewy = 'Mała Filozofia · Spotkanie z Arystotelesem'
        glowa = ('<div class="zywa-pagina"><span class="zp-l">'
                 '<span class="zp-znak"><svg viewBox="-4 -4 72 72" aria-hidden="true">'
                 '<use href="#znak-serii"/></svg></span>%s</span>'
                 '<span class="zp-p">%s</span></div>' % (lewy, pagina))
        stopka = ('<div class="stopka-strony"><span class="ss-znak">·</span>'
                  '<span class="ss-nr">%d</span></div>' % numer)
    else:
        glowa = '<div class="zywa-pagina pusta"></div>'
        stopka = '<div class="stopka-strony pusta"></div>'
    strony_html.append('<section class="%s" data-nr="%d">%s<div class="strona-tresc">%s</div>%s</section>'
                       % (strona_klasa, numer, glowa, tresc, stopka))

SYMBOL = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true">'
          '<symbol id="znak-serii" viewBox="-4 -4 72 72">%s</symbol></svg>'
          % re.sub(r'</?svg[^>]*>', '', ZNAK))
body = '<div class="ksiazka">\n%s\n%s\n</div>' % (SYMBOL, '\n'.join(strony_html))
body = popraw_typografie(body)
FRAG = ('<title>Spotkanie z Arystotelesem</title>\n'
 '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
 '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alegreya+Sans:ital,wght@0,400;0,500;0,700;0,800;1,400&family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&display=swap">\n'
 '<style>\n%s</style>\n\n%s\n' % (CSS, body))
open(os.path.join(WYJSCIE,'broszura.html'), 'w', encoding='utf-8').write(FRAG)
print('stron:', len(STRONY))
print('zdań opowiadania:', sum(len(r[k]) for r in ROZ for k in ('scena','mysl','emocja','zycie')) + len(INTRO))
print('pytań:', sum(len(r['pytania']) for r in ROZ))
