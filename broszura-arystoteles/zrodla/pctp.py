# -*- coding: utf-8 -*-
"""Odrysowanie znaku PCTP jako plik wektorowy (napis w krzywych)."""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

WYJ = '/home/user/chatbot/broszura-arystoteles/logo'
F = TTFont('tinos.woff2'); GS = F.getGlyphSet(); CMAP = F.getBestCmap(); UPEM = F['head'].unitsPerEm

def napis(tekst, stopien, tracking=0.0):
    s = stopien / UPEM
    czesci, x = [], 0.0
    for ch in tekst:
        g = CMAP[ord(ch)]
        pen = SVGPathPen(GS); GS[g].draw(pen); d = pen.getCommands()
        if d:
            czesci.append('<path transform="translate(%.3f 0) scale(%.5f %.5f)" d="%s"/>' % (x, s, -s, d))
        x += GS[g].width * s + tracking
    return ''.join(czesci), x - tracking

D, W = napis('PCTP', 124, 6)

SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="600" height="600"
     role="img" aria-label="Znak PCTP">
<g id="logo">
  <defs>
    <radialGradient id="pctpTlo" cx="42%%" cy="30%%" r="82%%">
      <stop offset="0%%" stop-color="#6142A0"/>
      <stop offset="55%%" stop-color="#4E3288"/>
      <stop offset="100%%" stop-color="#3B2270"/>
    </radialGradient>
  </defs>
  <circle cx="300" cy="300" r="298" fill="#3B2270"/>
  <circle cx="300" cy="300" r="288" fill="#D7CBE8"/>
  <circle cx="300" cy="300" r="270" fill="#3B2270"/>
  <circle cx="300" cy="300" r="262" fill="url(#pctpTlo)"/>

  <g stroke="#C6A02A" stroke-width="9" fill="none" stroke-linecap="round">
    <path d="M300 268 V196"/>
    <path d="M300 268 C284 240, 258 222, 236 210"/>
    <path d="M300 268 C316 240, 342 222, 364 210"/>
  </g>

  <g>
    <ellipse cx="228" cy="184" rx="24" ry="48" transform="rotate(-30 228 184)" fill="#A98FCB"/>
    <ellipse cx="372" cy="184" rx="24" ry="48" transform="rotate(30 372 184)" fill="#A98FCB"/>
    <ellipse cx="256" cy="158" rx="25" ry="52" transform="rotate(-16 256 158)" fill="#F0A268"/>
    <ellipse cx="344" cy="158" rx="25" ry="52" transform="rotate(16 344 158)" fill="#F0A268"/>
    <ellipse cx="300" cy="142" rx="26" ry="55" fill="#E8722C"/>
    <circle cx="300" cy="176" r="14" fill="#FFFFFF"/>
  </g>

  <g transform="translate(%.2f 412)" fill="#F5EFE4">%s</g>
</g>
</svg>
''' % (300 - W / 2, D)
open(os.path.join(WYJ, 'pctp-logo.svg'), 'w', encoding='utf-8').write(SVG)
print('pctp-logo.svg | szerokość napisu %.0f' % W)
