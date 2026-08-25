# -*- coding: utf-8 -*-
"""Grafiki gry „Emocje według Arystotelesa": plansza, siatki kostek, żetony."""

MORZE, SZAFRAN, OLIWKA, GLINA = 'var(--morze)', 'var(--szafran)', 'var(--oliwka)', 'var(--glina)'
TLA = {'e': ['var(--morze-jasne)', 'var(--oliwka-tlo)', 'var(--szafran-tlo)', 'var(--glina-tlo)'],
       'w': 'var(--papier-cien)', 'p': 'var(--papier-cien)'}

POLA = [
    ('start', 'START', ''),
    ('e', '1', 'ciekawość'), ('e', '2', 'niepewność'), ('w', '', ''), ('e', '3', 'napięcie sporu'),
    ('e', '4', 'zachwyt'), ('p', '', ''), ('e', '5', 'duma'), ('e', '6', 'ulga'), ('w', '', ''),
    ('e', '7', 'strach'), ('e', '8', 'zniechęcenie'), ('p', '', ''), ('e', '9', 'samotność'),
    ('e', '10', 'gniew'),
    ('w', '', ''), ('e', '11', 'nadzieja'), ('e', '12', 'wdzięczność'), ('w', '', ''),
    ('meta', 'META', ''),
]

def _lamacz(tekst, maks=13):
    slowa, linie, biez = tekst.split(), [], ''
    for s in slowa:
        if len(biez) + len(s) + 1 <= maks:
            biez = (biez + ' ' + s).strip()
        else:
            linie.append(biez); biez = s
    if biez: linie.append(biez)
    return linie

def plansza():
    KOL, WIE = 5, 4
    W, H, ODST = 122, 132, 10
    X0, Y0 = 6, 48
    czesci = []
    srodki = []
    for i, (typ, nr, nazwa) in enumerate(POLA):
        r, c = divmod(i, KOL)
        if r % 2: c = KOL - 1 - c                      # wąż: co drugi rząd w lewo
        x, y = X0 + c * (W + ODST), Y0 + r * (H + ODST)
        srodki.append((x + W / 2, y + H / 2, r, c))
        if typ == 'start':
            czesci.append('<rect x="%d" y="%d" width="%d" height="%d" rx="10" fill="%s"/>' % (x, y, W, H, MORZE))
            czesci.append('<text x="%d" y="%d" text-anchor="middle" font-family="Alegreya Sans, sans-serif" '
                          'font-weight="800" font-size="26" fill="#F7F4EC">START</text>' % (x + W/2, y + H/2 + 2))
            czesci.append('<text x="%d" y="%d" text-anchor="middle" font-family="Atkinson Hyperlegible, sans-serif" '
                          'font-size="14" fill="#F7F4EC">tu stawiasz pionek</text>' % (x + W/2, y + H/2 + 26))
        elif typ == 'meta':
            czesci.append('<rect x="%d" y="%d" width="%d" height="%d" rx="10" fill="%s"/>' % (x, y, W, H, SZAFRAN))
            czesci.append('<text x="%d" y="%d" text-anchor="middle" font-family="Alegreya Sans, sans-serif" '
                          'font-weight="800" font-size="28" fill="#F7F4EC">META</text>' % (x + W/2, y + H/2 + 2))
            czesci.append('<text x="%d" y="%d" text-anchor="middle" font-family="Atkinson Hyperlegible, sans-serif" '
                          'font-size="14" fill="#F7F4EC">nikt nie wygrywa</text>' % (x + W/2, y + H/2 + 26))
        elif typ == 'w':
            czesci.append('<rect x="%d" y="%d" width="%d" height="%d" rx="10" fill="%s" stroke="%s" '
                          'stroke-width="2.5" stroke-dasharray="7 5"/>' % (x, y, W, H, TLA['w'], OLIWKA))
            cx, cy = x + W/2, y + 52
            czesci.append('<g fill="%s"><ellipse cx="%d" cy="%d" rx="19" ry="9" transform="rotate(-20 %d %d)"/>'
                          '<ellipse cx="%d" cy="%d" rx="19" ry="9" transform="rotate(20 %d %d)"/>'
                          '<circle cx="%d" cy="%d" r="8"/></g>'
                          % (OLIWKA, cx - 17, cy, cx - 17, cy, cx + 17, cy, cx + 17, cy, cx, cy + 11))
            for j, l in enumerate(['kostka', 'emocji']):
                czesci.append('<text x="%d" y="%d" text-anchor="middle" font-family="Alegreya Sans, sans-serif" '
                              'font-weight="800" font-size="19" fill="%s">%s</text>' % (cx, y + 92 + j * 21, OLIWKA, l))
        elif typ == 'p':
            czesci.append('<rect x="%d" y="%d" width="%d" height="%d" rx="10" fill="%s" stroke="var(--linia)" '
                          'stroke-width="2.5"/>' % (x, y, W, H, TLA['p']))
            cx = x + W/2
            czesci.append('<g fill="var(--atrament-3)"><rect x="%d" y="%d" width="11" height="34" rx="4"/>'
                          '<rect x="%d" y="%d" width="11" height="34" rx="4"/></g>' % (cx - 17, y + 32, cx + 6, y + 32))
            for j, l in enumerate(['PRZERWA', 'nic nie robisz']):
                czesci.append('<text x="%d" y="%d" text-anchor="middle" font-family="%s" font-weight="%s" '
                              'font-size="%d" fill="%s">%s</text>'
                              % (cx, y + 92 + j * 22, 'Alegreya Sans, sans-serif' if j == 0 else 'Atkinson Hyperlegible, sans-serif',
                                 '800' if j == 0 else '400', 19 if j == 0 else 14,
                                 'var(--atrament)' if j == 0 else 'var(--atrament-3)', l))
        else:
            tlo = TLA['e'][(int(nr) - 1) % 4]
            czesci.append('<rect x="%d" y="%d" width="%d" height="%d" rx="10" fill="%s" stroke="%s" '
                          'stroke-width="2.5"/>' % (x, y, W, H, tlo, MORZE))
            cx = x + W/2
            czesci.append('<circle cx="%d" cy="%d" r="21" fill="%s"/>' % (cx, y + 34, MORZE))
            czesci.append('<text x="%d" y="%d" text-anchor="middle" font-family="Alegreya Sans, sans-serif" '
                          'font-weight="800" font-size="22" fill="#F7F4EC">%s</text>' % (cx, y + 42, nr))
            linie = _lamacz(nazwa, 12)
            for j, l in enumerate(linie):
                czesci.append('<text x="%d" y="%d" text-anchor="middle" font-family="Alegreya Sans, sans-serif" '
                              'font-weight="800" font-size="20" fill="var(--atrament)">%s</text>'
                              % (cx, y + 82 + j * 22, l))
            czesci.append('<text x="%d" y="%d" text-anchor="middle" font-family="Atkinson Hyperlegible, sans-serif" '
                          'font-size="13" fill="var(--atrament-3)">spotkanie %s</text>' % (cx, y + H - 12, nr))
    # strzałki zawracania między rzędami
    strzalki = []
    for r in range(3):
        y = Y0 + r * (H + ODST) + H + ODST / 2
        if r % 2 == 0:
            x = X0 + 4 * (W + ODST) + W / 2
            strzalki.append('<path d="M%d %d v%d" stroke="var(--linia)" stroke-width="4" fill="none"/>'
                            '<path d="M%d %d l-8 -12 h16 z" fill="var(--linia)" transform="rotate(180 %d %d)"/>'
                            % (x, y - ODST/2 - 4, ODST + 8, x, y + 6, x, y + 6))
        else:
            x = X0 + W / 2
            strzalki.append('<path d="M%d %d v%d" stroke="var(--linia)" stroke-width="4" fill="none"/>'
                            '<path d="M%d %d l-8 -12 h16 z" fill="var(--linia)" transform="rotate(180 %d %d)"/>'
                            % (x, y - ODST/2 - 4, ODST + 8, x, y + 6, x, y + 6))
    naglowek = ('<text x="6" y="24" font-family="Alegreya Sans, sans-serif" font-weight="800" font-size="24" '
                'fill="%s">Plansza · dwadzieścia pól</text>'
                '<text x="654" y="24" text-anchor="end" font-family="Atkinson Hyperlegible, sans-serif" '
                'font-size="15" fill="var(--atrament-3)">idź po strzałkach: w prawo, potem w lewo</text>' % MORZE)
    return ('<svg viewBox="0 0 660 622" role="img" aria-label="Plansza gry: dwadzieścia pól od startu do mety">'
            + naglowek + ''.join(strzalki) + ''.join(czesci) + '</svg>')


def _zakladka(x1, y1, x2, y2, glebokosc=15):
    """Trapezowa klapka do klejenia po zewnętrznej stronie odcinka (x1,y1)-(x2,y2)."""
    dx, dy = x2 - x1, y2 - y1
    dl = (dx ** 2 + dy ** 2) ** .5
    nx, ny = dy / dl, -dx / dl                      # normalna na zewnątrz
    ux, uy = dx / dl, dy / dl
    a = (x1 + ux * 8 + nx * glebokosc, y1 + uy * 8 + ny * glebokosc)
    b = (x2 - ux * 8 + nx * glebokosc, y2 - uy * 8 + ny * glebokosc)
    return ('<path d="M%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f Z" fill="var(--papier-cien)" '
            'stroke="var(--atrament-3)" stroke-width="1.6"/>' % (x1, y1, a[0], a[1], b[0], b[1], x2, y2))


def siatka_kostki(sciany, tytul, kolor_tla):
    """sciany: 6 x (glowny_napis, podpis) w kolejności: góra, lewa, przód, prawa, tył, dół."""
    S = 108
    poz = {0: (S, 0), 1: (0, S), 2: (S, S), 3: (2 * S, S), 4: (3 * S, S), 5: (S, 2 * S)}
    OX, OY = 26, 34
    czesci = []
    # klapki
    for (x1, y1, x2, y2) in [
        (OX, OY + S, OX, OY + 2 * S),                                   # lewa krawędź ściany 1
        (OX + 4 * S, OY + 2 * S, OX + 4 * S, OY + S),                   # prawa krawędź ściany 4
        (OX + S, OY, OX + 2 * S, OY),                                   # góra ściany 0
        (OX + S, OY + S, OX + S, OY),                                   # lewa ściany 0
        (OX + 2 * S, OY, OX + 2 * S, OY + S),                           # prawa ściany 0
        (OX + 2 * S, OY + 3 * S, OX + S, OY + 3 * S),                   # dół ściany 5
        (OX + S, OY + 3 * S, OX + S, OY + 2 * S),                       # lewa ściany 5
        (OX + 2 * S, OY + 2 * S, OX + 2 * S, OY + 3 * S)]:              # prawa ściany 5
        czesci.append(_zakladka(x1, y1, x2, y2))
    # ściany
    for i, (glowny, podpis) in enumerate(sciany):
        px, py = poz[i]
        x, y = OX + px, OY + py
        czesci.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" stroke="var(--atrament)" '
                      'stroke-width="2.2"/>' % (x, y, S, S, kolor_tla))
        linie = _lamacz(glowny, 11)
        start_y = y + S / 2 - (len(linie) - 1) * 13 - (6 if podpis else -4)
        for j, l in enumerate(linie):
            czesci.append('<text x="%d" y="%d" text-anchor="middle" font-family="Alegreya Sans, sans-serif" '
                          'font-weight="800" font-size="21" fill="var(--atrament)">%s</text>'
                          % (x + S / 2, start_y + j * 26, l))
        if podpis:
            czesci.append('<text x="%d" y="%d" text-anchor="middle" font-family="Atkinson Hyperlegible, sans-serif" '
                          'font-size="14" fill="var(--atrament-2)">%s</text>' % (x + S / 2, y + S - 18, podpis))
    # linie zagięć
    zagiecia = [(OX + S, OY + S, OX + 2 * S, OY + S), (OX + S, OY + 2 * S, OX + 2 * S, OY + 2 * S),
                (OX + S, OY + S, OX + S, OY + 2 * S), (OX + 2 * S, OY + S, OX + 2 * S, OY + 2 * S),
                (OX + 3 * S, OY + S, OX + 3 * S, OY + 2 * S)]
    for (x1, y1, x2, y2) in zagiecia:
        czesci.append('<path d="M%d %d L%d %d" stroke="%s" stroke-width="2" stroke-dasharray="6 5"/>'
                      % (x1, y1, x2, y2, SZAFRAN))
    czesci.append('<text x="%d" y="22" font-family="Alegreya Sans, sans-serif" font-weight="800" font-size="22" '
                  'fill="%s">%s</text>' % (OX, MORZE, tytul))
    czesci.append('<text x="%d" y="%d" font-family="Atkinson Hyperlegible, sans-serif" font-size="14" '
                  'fill="var(--atrament-3)">ciągła linia — tniesz · przerywana — zaginasz · szare pola — kleisz</text>'
                  % (OX, OY + 3 * S + 42))
    return ('<svg viewBox="0 0 %d %d" role="img" aria-label="%s — siatka do wycięcia">%s</svg>'
            % (4 * S + 2 * OX + 20, 3 * S + OY + 58, tytul, ''.join(czesci)))


def zetony(ile=24):
    W, H, K = 76, 62, 6
    czesci = []
    for i in range(ile):
        r, c = divmod(i, K)
        x, y = 8 + c * W, 8 + r * H
        czesci.append('<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="var(--linia)" '
                      'stroke-width="1.4" stroke-dasharray="5 4"/>' % (x, y, W - 6, H - 6))
        cx, cy = x + (W - 6) / 2, y + (H - 6) / 2
        czesci.append('<g fill="%s"><ellipse cx="%.0f" cy="%.0f" rx="17" ry="8" transform="rotate(-22 %.0f %.0f)"/>'
                      '<ellipse cx="%.0f" cy="%.0f" rx="17" ry="8" transform="rotate(22 %.0f %.0f)"/></g>'
                      '<path d="M%.0f %.0f v13" stroke="%s" stroke-width="2.4" stroke-linecap="round"/>'
                      % (OLIWKA, cx - 13, cy - 4, cx - 13, cy - 4, cx + 13, cy - 4, cx + 13, cy - 4,
                         cx, cy + 2, SZAFRAN))
    return ('<svg viewBox="0 0 %d %d" role="img" aria-label="Żetony w kształcie listków do wycięcia">%s</svg>'
            % (W * K + 10, H * ((ile + K - 1) // K) + 10, ''.join(czesci)))


def kostka_ilustracja():
    """Kostka, pionek i listek — winieta otwierająca załącznik."""
    return '''<svg viewBox="0 0 640 200" role="img" aria-label="Kostka miary, pionek i żeton w kształcie listka">
  <rect x="0" y="0" width="640" height="200" fill="var(--papier-cien)"/>
  <g transform="translate(74 34)">
    <path d="M0 34 L58 0 L116 34 L58 68 Z" fill="var(--szafran-tlo)" stroke="var(--szafran)" stroke-width="3"/>
    <path d="M0 34 L0 106 L58 140 L58 68 Z" fill="var(--szafran)" opacity=".22" stroke="var(--szafran)" stroke-width="3"/>
    <path d="M116 34 L116 106 L58 140 L58 68 Z" fill="var(--szafran)" opacity=".38" stroke="var(--szafran)" stroke-width="3"/>
    <text x="58" y="40" text-anchor="middle" font-family="Alegreya Sans, sans-serif" font-weight="800"
          font-size="26" fill="var(--atrament)">2</text>
    <text x="28" y="82" text-anchor="middle" font-family="Alegreya Sans, sans-serif" font-weight="800"
          font-size="13" fill="var(--atrament)">właściwa</text>
    <text x="28" y="100" text-anchor="middle" font-family="Alegreya Sans, sans-serif" font-weight="800"
          font-size="13" fill="var(--atrament)">miara</text>
    <text x="88" y="90" text-anchor="middle" font-family="Alegreya Sans, sans-serif" font-weight="800"
          font-size="13" fill="var(--atrament)">za dużo</text>
  </g>
  <g transform="translate(280 52)">
    <ellipse cx="30" cy="106" rx="30" ry="9" fill="var(--linia)"/>
    <path d="M12 100 q-2 -30 18 -44 q20 14 18 44 z" fill="var(--morze-jasne)" stroke="var(--morze)" stroke-width="3.5"/>
    <circle cx="30" cy="42" r="17" fill="var(--morze)"/>
  </g>
  <g transform="translate(400 60)">
    <ellipse cx="34" cy="44" rx="34" ry="16" transform="rotate(-22 34 44)" fill="var(--oliwka)"/>
    <ellipse cx="86" cy="44" rx="34" ry="16" transform="rotate(22 86 44)" fill="var(--oliwka)"/>
    <path d="M60 56 v34" stroke="var(--szafran)" stroke-width="5" stroke-linecap="round"/>
  </g>
  <g font-family="Atkinson Hyperlegible, sans-serif" font-size="15" fill="var(--atrament-3)" text-anchor="middle">
    <text x="132" y="192">kostka miary</text>
    <text x="310" y="192">pionek</text>
    <text x="460" y="192">listek — żeton</text>
  </g>
  <g transform="translate(520 74)" opacity=".9">
    <rect x="0" y="0" width="86" height="60" rx="7" fill="var(--glina-tlo)" stroke="var(--glina)"
          stroke-width="3" stroke-dasharray="7 5"/>
    <circle cx="20" cy="18" r="10" fill="var(--morze)"/>
    <text x="20" y="23" text-anchor="middle" font-family="Alegreya Sans, sans-serif" font-weight="800"
          font-size="12" fill="#F7F4EC">7</text>
    <g stroke="var(--glina)" stroke-width="2.4" stroke-linecap="round">
      <path d="M12 40 h62"/><path d="M12 50 h44"/>
    </g>
  </g>
  <text x="563" y="192" text-anchor="middle" font-family="Atkinson Hyperlegible, sans-serif"
        font-size="15" fill="var(--atrament-3)">karta</text>
</svg>'''
