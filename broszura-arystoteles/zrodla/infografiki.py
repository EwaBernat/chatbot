# -*- coding: utf-8 -*-
"""Infografiki stron wstępnych: oś czasu, termometr emocji, karta kieszonkowa, ozdobnik.

Wszystko rysowane z danych, żeby kolejny tom serii nie wymagał grzebania w SVG.
Kolory podawane są jako zmienne CSS — dzięki temu ta sama grafika działa
na papierze broszury i w podglądzie na ekranie.
"""

KOLORY = {'morze': 'var(--morze)', 'szafran': 'var(--szafran)',
          'oliwka': 'var(--oliwka)', 'glina': 'var(--glina)'}
DISPLAY = 'Alegreya Sans, sans-serif'
TEKST = 'Atkinson Hyperlegible, sans-serif'


def os_czasu(dane):
    """dane: słownik z kluczami 'punkty' (lista) i 'stopka'.
    Każdy punkt: rok, opcjonalnie jednostka, opis (1–2 linie), kolor, duzy."""
    punkty = dane['punkty']
    n = len(punkty)
    x0, x1 = 60, 965
    krok = (x1 - x0) / max(n - 1, 1)
    czesci = ['<line x1="40" y1="140" x2="980" y2="140" stroke="var(--linia)" stroke-width="6" stroke-linecap="round"/>',
              '<line x1="40" y1="140" x2="980" y2="140" stroke="var(--morze)" stroke-width="6" '
              'stroke-linecap="round" stroke-dasharray="2 18"/>']
    for i, p in enumerate(punkty):
        x = x0 + i * krok
        r = 17 if p.get('duzy') else 14
        kolor = KOLORY.get(p.get('kolor', 'morze'), KOLORY['morze'])
        czesci.append('<g transform="translate(%.1f,0)">' % x)
        czesci.append('<circle cx="0" cy="140" r="%d" fill="%s" stroke="var(--karta)" stroke-width="4"/>' % (r, kolor))
        czesci.append('<text x="0" y="102" text-anchor="middle" font-size="24" font-weight="800" '
                      'fill="var(--atrament)">%s</text>' % p['rok'])
        if p.get('jednostka'):
            czesci.append('<text x="0" y="80" text-anchor="middle" font-size="13" '
                          'fill="var(--atrament-2)">%s</text>' % p['jednostka'])
        for j, linia in enumerate(p['opis'][:2]):
            czesci.append('<text x="0" y="%d" text-anchor="middle" font-size="16" '
                          'fill="var(--atrament)">%s</text>' % (190 + j * 22, linia))
        czesci.append('</g>')
    stopka = ('<text x="40" y="285" font-size="15" fill="var(--atrament-2)" font-family="%s">%s</text>'
              % (TEKST, dane.get('stopka', '')))
    return ('<svg viewBox="0 0 1020 320" role="img" aria-label="Oś czasu życia" style="min-width:640px">'
            + czesci[0] + czesci[1] + '<g font-family="%s">' % DISPLAY + ''.join(czesci[2:]) + '</g>'
            + stopka + '</svg>')


def termometr(podpis=''):
    """Skala 0–10. Treść jest uniwersalna dla całej serii — zmienia się tylko podpis."""
    poziomy = [('0–2', ['spokój', 'nic mnie nie', 'rusza'], 'var(--morze-jasne)'),
               ('3–4', ['lekko czuję', 'mogę dalej', 'robić swoje'], 'var(--oliwka-tlo)'),
               ('5–6', ['wyraźnie czuję', 'trudniej mi się', 'skupić'], 'var(--szafran-tlo)'),
               ('7–8', ['bardzo mocno', 'ciało reaguje,', 'chce mi się wyjść'], 'var(--glina-tlo)'),
               ('9–10', ['za dużo', 'nie umiem już', 'mówić i myśleć'], None)]
    czesci = ['<rect x="40" y="96" width="700" height="56" rx="28" fill="var(--papier-cien)" '
              'stroke="var(--linia)" stroke-width="3"/>']
    x = 46
    srodki = []
    for i, (etykieta, opis, tlo) in enumerate(poziomy):
        w = 144 if i == 4 else 130
        rx = 22 if i in (0, 4) else 6
        fill = tlo if tlo else 'var(--glina)'
        op = '' if tlo else ' opacity=".55"'
        czesci.append('<rect x="%d" y="102" width="%d" height="44" rx="%d" fill="%s"%s/>' % (x, w, rx, fill, op))
        srodki.append((x + w / 2, etykieta, opis))
        x += w + 6
    czesci.append('<circle cx="770" cy="124" r="42" fill="var(--glina-tlo)" stroke="var(--glina)" stroke-width="4"/>')
    czesci.append('<g font-family="%s" font-weight="800" font-size="22" fill="var(--atrament)" text-anchor="middle">' % DISPLAY)
    for cx, etykieta, _ in srodki:
        czesci.append('<text x="%.0f" y="132">%s</text>' % (cx, etykieta))
    czesci.append('<text x="770" y="132">STOP</text></g>')
    czesci.append('<g font-family="%s" font-size="16" fill="var(--atrament)" text-anchor="middle">' % TEKST)
    for cx, _, opis in srodki:
        for j, l in enumerate(opis):
            czesci.append('<text x="%.0f" y="%d">%s</text>' % (cx, 190 + j * 22, l))
    for j, l in enumerate(['tu proszę', 'o pomoc albo', 'idę w ciszę']):
        czesci.append('<text x="770" y="%d">%s</text>' % (190 + j * 22, l))
    czesci.append('</g>')
    czesci.append('<text x="40" y="70" font-family="%s" font-size="17" fill="var(--atrament-2)">'
                  'Zanim nazwiesz emocję, pokaż jej siłę: od 0 do 10.</text>' % TEKST)
    if podpis:
        czesci.append('<text x="40" y="284" font-family="%s" font-size="15" fill="var(--atrament-2)">%s</text>'
                      % (TEKST, podpis))
    return ('<svg viewBox="0 0 900 300" role="img" aria-label="Termometr emocji z pięcioma poziomami siły" '
            'style="min-width:600px">' + ''.join(czesci) + '</svg>')


def karta_emocji():
    """Kieszonkowa karta czterech kroków. Uniwersalna dla całej serii."""
    kroki = [('NAZWIJ', ['„czuję…”', 'jedno słowo', 'wystarczy'], 'var(--oliwka-tlo)', 'var(--oliwka)'),
             ('ZMIERZ', ['od 0 do 10', 'możesz pokazać', 'na palcach'], 'var(--morze-jasne)', 'var(--morze)'),
             ('ZNAJDŹ', ['co się stało', 'tuż przed tym', 'uczuciem?'], 'var(--glina-tlo)', 'var(--glina)'),
             ('WYBIERZ', ['ruch, cisza,', 'woda, prośba', 'o pomoc'], 'var(--szafran-tlo)', 'var(--szafran)')]
    czesci = ['<rect x="14" y="14" width="832" height="312" rx="10" fill="var(--karta)" stroke="var(--morze)" '
              'stroke-width="5" stroke-dasharray="14 10"/>',
              '<text x="48" y="66" font-family="%s" font-weight="800" font-size="28" fill="var(--morze)">'
              'CO SIĘ ZE MNĄ TERAZ DZIEJE?</text>' % DISPLAY]
    for i, (nazwa, opis, tlo, ramka) in enumerate(kroki):
        x = 48 + i * 200
        cx = x + 90
        czesci.append('<rect x="%d" y="92" width="180" height="196" rx="8" fill="%s" stroke="%s" stroke-width="3"/>'
                      % (x, tlo, ramka))
        czesci.append('<text x="%d" y="146" text-anchor="middle" font-family="%s" font-weight="800" font-size="46" '
                      'fill="var(--atrament)" opacity="0.25">%d</text>' % (cx, DISPLAY, i + 1))
        czesci.append('<text x="%d" y="188" text-anchor="middle" font-family="%s" font-weight="800" font-size="22" '
                      'fill="var(--atrament)">%s</text>' % (cx, DISPLAY, nazwa))
        for j, l in enumerate(opis):
            czesci.append('<text x="%d" y="%d" text-anchor="middle" font-family="%s" font-size="16" '
                          'fill="var(--atrament)">%s</text>' % (cx, 222 + j * 26, TEKST, l))
    return ('<svg viewBox="0 0 860 340" role="img" aria-label="Karta kieszonkowa z czterema krokami" '
            'style="min-width:600px">' + ''.join(czesci) + '</svg>')


ORNAMENT = """<svg viewBox="0 0 160 24" role="img" aria-label="Ozdobnik: trzy listki oliwne">
  <g fill="var(--oliwka)" opacity=".8">
    <ellipse cx="80" cy="12" rx="11" ry="5"/>
    <ellipse cx="60" cy="12" rx="8" ry="4" transform="rotate(-14 60 12)"/>
    <ellipse cx="100" cy="12" rx="8" ry="4" transform="rotate(14 100 12)"/>
  </g>
  <g stroke="var(--linia)" stroke-width="1.4"><path d="M4 12 H44"/><path d="M116 12 H156"/></g>
</svg>"""

GALAZKA = """<svg viewBox="0 0 300 60" role="img" aria-label="Gałązka oliwna">
  <path d="M20 30 H280" stroke="var(--linia)" stroke-width="2"/>
  <g fill="var(--oliwka)">
    <ellipse cx="122" cy="22" rx="15" ry="7" transform="rotate(-22 122 22)"/>
    <ellipse cx="150" cy="16" rx="15" ry="7"/>
    <ellipse cx="178" cy="22" rx="15" ry="7" transform="rotate(22 178 22)"/>
    <ellipse cx="134" cy="40" rx="13" ry="6" transform="rotate(20 134 40)"/>
    <ellipse cx="166" cy="40" rx="13" ry="6" transform="rotate(-20 166 40)"/>
  </g>
  <circle cx="150" cy="30" r="5" fill="var(--szafran)"/>
</svg>"""
