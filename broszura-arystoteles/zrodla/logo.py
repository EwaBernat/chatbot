# -*- coding: utf-8 -*-
"""Generuje znak i logotypy serii „Mała Filozofia” jako czyste pliki SVG (napis w krzywych)."""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

WYJ = '/home/user/chatbot/broszura-arystoteles/logo'
os.makedirs(WYJ, exist_ok=True)
F = TTFont('wm.woff2'); GS = F.getGlyphSet(); CMAP = F.getBestCmap(); UPEM = F['head'].unitsPerEm

def napis(tekst, stopien, tracking=0.0):
    """Zwraca (d, szerokosc) — kontury napisu, baseline w y=0, start w x=0."""
    s = stopien / UPEM
    czesci, x = [], 0.0
    for ch in tekst:
        g = CMAP[ord(ch)]
        pen = SVGPathPen(GS)
        GS[g].draw(pen)
        d = pen.getCommands()
        if d:
            czesci.append('<path transform="translate(%.3f 0) scale(%.5f %.5f)" d="%s"/>'
                          % (x, s, -s, d))
        x += GS[g].width * s + tracking
    return ''.join(czesci), x - tracking

ZNAK = '''  <circle cx="32" cy="32" r="27" fill="none" stroke="{morze}" stroke-width="4.6"
          stroke-dasharray="146 23.6" stroke-dashoffset="-139" stroke-linecap="round"/>
  <path d="M24.5 27.5 C24.5 18.6, 41 18, 41 26.2 C41 32.6, 32 33.6, 32 39.4"
        fill="none" stroke="{morze}" stroke-width="5" stroke-linecap="round"/>
  <circle cx="32" cy="46.6" r="3.4" fill="{szafran}"/>
  <g fill="{oliwka}">
    <ellipse cx="25.8" cy="5.2" rx="6.4" ry="3" transform="rotate(-20 25.8 5.2)"/>
    <ellipse cx="38.2" cy="5.2" rx="6.4" ry="3" transform="rotate(20 38.2 5.2)"/>
    <circle cx="32" cy="8.6" r="2.8"/>
  </g>'''
KOLOR = dict(morze='#1E5A6B', szafran='#B07E13', oliwka='#5C7A49')
MONO  = dict(morze='currentColor', szafran='currentColor', oliwka='currentColor')
NAG = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 -4 %s" width="%s" height="%s" '
       'role="img" aria-label="%s">\n')

def zapisz(nazwa, tresc):
    tresc = tresc.replace('>\n', '>\n<g id="logo">', 1).replace('\n</svg>', '\n</g>\n</svg>')
    open(os.path.join(WYJ, nazwa), 'w', encoding='utf-8').write(tresc)
    print(' ', nazwa, '%.1f kB' % (len(tresc.encode()) / 1024))

# --- 1. sam znak
for plik, pal, opis in (('mala-filozofia-znak.svg', KOLOR, 'Znak serii Mała Filozofia'),
                        ('mala-filozofia-znak-mono.svg', MONO, 'Znak serii Mała Filozofia, jednokolorowy')):
    zapisz(plik, NAG % ('72 72', 72, 72, opis) + ZNAK.format(**pal) + '\n</svg>\n')

# --- 2. logo poziome
d1, w1 = napis('MAŁA', 20, 2.8)
d2, w2 = napis('FILOZOFIA', 20, 2.8)
szer = 78 + max(w1, w2) + 6
poz = (NAG % ('%.0f 72' % (szer + 8), '%.0f' % (szer + 8), 72, 'Logo serii Mała Filozofia') +
       ZNAK.format(**KOLOR) +
       '\n  <g transform="translate(78 29)" fill="#1F2E33">%s</g>'
       '\n  <g transform="translate(78 52)" fill="#1E5A6B">%s</g>\n</svg>\n' % (d1, d2))
zapisz('mala-filozofia-logo-poziome.svg', poz)

# --- 3. logo pionowe
d1v, w1v = napis('MAŁA', 19, 3.2)
d2v, w2v = napis('FILOZOFIA', 19, 3.2)
szerv = max(w1v, w2v) + 18
srodek = szerv / 2
pion = (NAG % ('%.0f 138' % (szerv + 8), '%.0f' % (szerv + 8), 138, 'Logo pionowe serii Mała Filozofia') +
        '  <g transform="translate(%.2f 0)">%s</g>' % (srodek - 32, ZNAK.format(**KOLOR)) +
        '\n  <g transform="translate(%.2f 98)" fill="#1F2E33">%s</g>'
        '\n  <g transform="translate(%.2f 121)" fill="#1E5A6B">%s</g>\n</svg>\n'
        % (srodek - w1v / 2, d1v, srodek - w2v / 2, d2v))
zapisz('mala-filozofia-logo-pionowe.svg', pion)

# --- 4. logo poziome jednokolorowe
pozm = (NAG % ('%.0f 72' % (szer + 8), '%.0f' % (szer + 8), 72, 'Logo serii Mała Filozofia, jednokolorowe') +
        ZNAK.format(**MONO) +
        '\n  <g transform="translate(78 29)" fill="currentColor">%s</g>'
        '\n  <g transform="translate(78 52)" fill="currentColor">%s</g>\n</svg>\n' % (d1, d2))
zapisz('mala-filozofia-logo-poziome-mono.svg', pozm)
print('szerokość logo poziomego: %.0f px' % szer)
