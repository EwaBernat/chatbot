# -*- coding: utf-8 -*-
K = {'tue':'#C4547A','tuk':'#6553A8','tus':'#0E8B78','gold':'#A07A0A','ink':'#2E2A3B'}

def twarz(emocja, kolor='#2E2A3B', tlo='#FFFFFF'):
    """Prosta, czytelna buźka do wycięcia. viewBox 0 0 100 100."""
    g = ['<svg class="buzka" viewBox="0 0 100 100" role="img" aria-label="Twarz: %s">' % emocja,
         '<circle cx="50" cy="50" r="41" fill="%s" stroke="%s" stroke-width="3"/>' % (tlo, kolor)]
    o = 'fill="%s"' % kolor
    s = 'fill="none" stroke="%s" stroke-width="3.4" stroke-linecap="round"' % kolor
    if emocja == 'radosc':
        g += ['<circle cx="36" cy="43" r="4.2" %s/>' % o, '<circle cx="64" cy="43" r="4.2" %s/>' % o,
              '<path d="M31 58 Q50 75 69 58" %s/>' % s]
    elif emocja == 'smutek':
        g += ['<circle cx="36" cy="45" r="4.2" %s/>' % o, '<circle cx="64" cy="45" r="4.2" %s/>' % o,
              '<path d="M31 70 Q50 55 69 70" %s/>' % s,
              '<path d="M28 36 Q34 32 41 35" %s/>' % s, '<path d="M59 35 Q66 32 72 36" %s/>' % s,
              '<path d="M36 52 q-3 6 0 8 q3 -2 0 -8" fill="%s" opacity="0.55"/>' % kolor]
    elif emocja == 'zlosc':
        g += ['<circle cx="36" cy="47" r="4.2" %s/>' % o, '<circle cx="64" cy="47" r="4.2" %s/>' % o,
              '<path d="M27 35 L45 43" %s/>' % s, '<path d="M73 35 L55 43" %s/>' % s,
              '<path d="M33 68 Q50 60 67 68" %s/>' % s]
    elif emocja == 'strach':
        g += ['<circle cx="36" cy="45" r="6.2" fill="none" stroke="%s" stroke-width="3"/>' % kolor,
              '<circle cx="64" cy="45" r="6.2" fill="none" stroke="%s" stroke-width="3"/>' % kolor,
              '<path d="M27 31 Q35 25 44 30" %s/>' % s, '<path d="M56 30 Q65 25 73 31" %s/>' % s,
              '<ellipse cx="50" cy="68" rx="9" ry="11" fill="none" stroke="%s" stroke-width="3.2"/>' % kolor]
    elif emocja == 'zdziwienie':
        g += ['<circle cx="36" cy="46" r="5.6" %s/>' % o, '<circle cx="64" cy="46" r="5.6" %s/>' % o,
              '<path d="M27 30 Q36 24 45 29" %s/>' % s, '<path d="M55 29 Q64 24 73 30" %s/>' % s,
              '<circle cx="50" cy="69" r="8.5" fill="none" stroke="%s" stroke-width="3.2"/>' % kolor]
    g.append('</svg>')
    return "\n".join(g)

if __name__ == '__main__':
    import sys
    print(twarz(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else '#2E2A3B'))


def intensywnosc(n, kolor='#2E2A3B', tlo='#FFFFFF'):
    """Twarz pokazująca NATĘŻENIE odczucia (1 = spokój, 5 = bardzo mocno).
    Termometr mierzy siłę emocji, nie jej rodzaj — dlatego osobny zestaw min."""
    g = ['<svg viewBox="0 0 100 100" role="img" aria-label="Natężenie %d z 5">' % n,
         '<circle cx="50" cy="50" r="41" fill="%s" stroke="%s" stroke-width="3"/>' % (tlo, kolor)]
    s = 'fill="none" stroke="%s" stroke-width="3.4" stroke-linecap="round"' % kolor
    o = 'fill="%s"' % kolor
    usta = {1: 'M34 63 L66 63',
            2: 'M34 66 Q50 60 66 66',
            3: 'M34 68 Q50 58 66 68',
            4: 'M33 70 Q50 55 67 70',
            5: 'M33 71 Q50 53 67 71'}[n]
    g += ['<circle cx="36" cy="45" r="4.2" %s/>' % o, '<circle cx="64" cy="45" r="4.2" %s/>' % o,
          '<path d="%s" %s/>' % (usta, s)]
    if n >= 3:
        g += ['<path d="M27 33 L44 38" %s/>' % s, '<path d="M73 33 L56 38" %s/>' % s]
    if n >= 4:
        g += ['<path d="M18 44 q-4 5 0 9" %s/>' % s, '<path d="M82 44 q4 5 0 9" %s/>' % s]
    if n == 5:
        g += ['<path d="M13 38 q-5 6 0 12" %s/>' % s, '<path d="M87 38 q5 6 0 12" %s/>' % s]
    g.append('</svg>')
    return "\n".join(g)
