# -*- coding: utf-8 -*-
"""Ilustracje SVG do broszury 'Maly Ksiaze moim bohaterem'. Paleta zielona."""

# --- paleta ---
C = {
    "d1": "#06281E",  # najciemniejsza zielen
    "d2": "#0B3D2E",
    "d3": "#14664A",
    "m1": "#1F8A63",
    "m2": "#3FA87C",
    "m3": "#6FC5A0",
    "l1": "#A7DCC4",
    "l2": "#CFEBDD",
    "l3": "#E8F5EF",
    "gold": "#E3B23C",
    "gold2": "#F4D06F",
    "rose": "#D96D8B",
    "rose2": "#F0A9BE",
    "sand": "#F3E7C9",
    "ink": "#08251C",
    "szal": "#BFD9EF",
    "szal2": "#8FBBDD",
    "wlosy": "#F2C75C",
    "wlosy2": "#D9A93B",
    "skora": "#F7E3CE",
    "fiolet": "#4A3E7A",
    "fiolet2": "#2E2752",
}

def _wash(x, y, r, kolor, moc=".22", uid=""):
    """Miękka plama koloru — imituje lawowanie akwarelowe."""
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{kolor}" opacity="{moc}" '
            f'filter="url(#rozmyj{uid})"/>')


def _defs(uid):
    return f'''<defs>
<filter id="rozmyj{uid}" x="-40%" y="-40%" width="180%" height="180%">
<feGaussianBlur stdDeviation="14"/></filter>
<filter id="miekko{uid}" x="-25%" y="-25%" width="150%" height="150%">
<feGaussianBlur stdDeviation="3.2"/></filter>
<linearGradient id="plaszcz{uid}" x1="0" y1="0" x2="0.3" y2="1">
<stop offset="0%" stop-color="{C['m2']}"/><stop offset="100%" stop-color="{C['d3']}"/>
</linearGradient>
<linearGradient id="wlos{uid}" x1="0" y1="0" x2="0" y2="1">
<stop offset="0%" stop-color="{C['wlosy']}"/><stop offset="100%" stop-color="{C['wlosy2']}"/>
</linearGradient>
<linearGradient id="sky{uid}" x1="0" y1="0" x2="0" y2="1">
<stop offset="0%" stop-color="{C['d1']}"/><stop offset="60%" stop-color="{C['d2']}"/><stop offset="100%" stop-color="{C['d3']}"/>
</linearGradient>
<linearGradient id="pl{uid}" x1="0" y1="0" x2="1" y2="1">
<stop offset="0%" stop-color="{C['m3']}"/><stop offset="55%" stop-color="{C['m1']}"/><stop offset="100%" stop-color="{C['d3']}"/>
</linearGradient>
<radialGradient id="glow{uid}" cx="50%" cy="50%" r="50%">
<stop offset="0%" stop-color="{C['gold2']}" stop-opacity=".55"/><stop offset="100%" stop-color="{C['gold2']}" stop-opacity="0"/>
</radialGradient>
</defs>'''

_STARS = [(38,44,1.6),(96,28,1.1),(150,60,1.9),(212,36,1.3),(268,72,1.5),(330,40,1.1),
          (64,110,1.2),(286,132,1.7),(360,96,1.4),(20,150,1.0),(392,168,1.2),(124,150,1.0),
          (176,22,1.0),(248,152,1.1),(310,180,1.3),(84,190,1.0)]

def stars(op=".85", scale=1.0, dx=0, dy=0):
    out = []
    for x, y, r in _STARS:
        out.append(f'<circle cx="{x*scale+dx:.0f}" cy="{y*scale+dy:.0f}" r="{r*scale:.1f}" fill="{C["l2"]}" opacity="{op}"/>')
    return "".join(out)

def _sparkle(x, y, s, col=None):
    col = col or C["gold2"]
    return (f'<path d="M{x} {y-s} Q{x+s*.18} {y-s*.18} {x+s} {y} '
            f'Q{x+s*.18} {y+s*.18} {x} {y+s} Q{x-s*.18} {y+s*.18} {x-s} {y} '
            f'Q{x-s*.18} {y-s*.18} {x} {y-s} Z" fill="{col}"/>')

# ---------- 1. OKLADKA ----------
def cover():
    """Maly Ksiaze na swojej planecie: miekkie lawowania, zielony plaszcz, blekitny szal."""
    return f'''<svg viewBox="0 0 420 300" preserveAspectRatio="xMidYMax slice" role="img" aria-label="Maly Ksiaze na swojej planecie, ze szalem na wietrze i gwiazdka w dloni">
{_defs("cv")}
<rect width="420" height="300" fill="url(#skycv)"/>
{_wash(90, 70, 90, C['fiolet'], '.42', 'cv')}
{_wash(330, 104, 96, C['fiolet2'], '.36', 'cv')}
{_wash(210, 36, 110, C['d3'], '.28', 'cv')}
{stars()}
{_sparkle(352, 58, 7)}{_sparkle(58, 84, 5)}{_sparkle(300, 26, 4)}{_sparkle(140, 46, 4)}
<circle cx="210" cy="252" r="150" fill="url(#glowcv)"/>

<circle cx="210" cy="272" r="98" fill="url(#plcv)"/>
<path d="M112 250a98 98 0 0 1 196 0 98 98 0 0 0-196 0Z" fill="{C['m3']}" opacity=".32"/>
{_wash(170, 296, 42, C['d3'], '.32', 'cv')}
<ellipse cx="150" cy="302" rx="26" ry="11" fill="{C['d3']}" opacity=".34"/>
<ellipse cx="272" cy="310" rx="20" ry="9" fill="{C['d3']}" opacity=".28"/>
<path d="M118 268l16-22 16 22z" fill="{C['d2']}" opacity=".9"/>
<path d="M126 250q8-12 16 0z" fill="{C['gold']}" opacity=".75"/>
<path d="M290 282l13-18 13 18z" fill="{C['d2']}" opacity=".85"/>

<g transform="translate(300,210)">
<path d="M0 44V22" stroke="{C['d2']}" stroke-width="3" stroke-linecap="round"/>
<path d="M0 34c-8-2-12-8-12-8s8-3 12 3z" fill="{C['m1']}"/>
<circle cx="0" cy="16" r="8.5" fill="{C['rose']}"/><circle cx="-1" cy="14" r="4" fill="{C['rose2']}"/>
<path d="M-16 45a16 30 0 0 1 32 0z" fill="{C['l1']}" opacity=".22"/>
<path d="M-16 45a16 30 0 0 1 32 0" fill="none" stroke="{C['l2']}" stroke-width="1.5" opacity=".75"/>
<rect x="-18" y="44" width="36" height="4" rx="2" fill="{C['l2']}" opacity=".8"/>
</g>

<g transform="translate(178,146)">
<!-- rece: ciemny kontur pod spodem, zeby nie gubily sie na zielonej planecie -->
<path d="M-16 58q-16 8-24 24" stroke="{C['d1']}" stroke-width="11.5" fill="none" stroke-linecap="round"/>
<path d="M24 56q17 6 26 22" stroke="{C['d1']}" stroke-width="11.5" fill="none" stroke-linecap="round"/>
<path d="M-16 58q-16 8-24 24" stroke="{C['m3']}" stroke-width="8" fill="none" stroke-linecap="round"/>
<path d="M24 56q17 6 26 22" stroke="{C['m3']}" stroke-width="8" fill="none" stroke-linecap="round"/>
<circle cx="-41" cy="83" r="5" fill="{C['skora']}" stroke="{C['d1']}" stroke-width="1.2"/>
<circle cx="51" cy="79" r="5" fill="{C['skora']}" stroke="{C['d1']}" stroke-width="1.2"/>
<!-- plaszcz -->
<path d="M4 50c-17 0-29 15-31 36h62c-2-21-14-36-31-36z" fill="url(#plaszczcv)" stroke="{C['d1']}" stroke-width="1.5" stroke-linejoin="round"/>
<path d="M4 50v36" stroke="{C['d1']}" stroke-width="1.2" opacity=".4"/>
<circle cx="4" cy="64" r="1.7" fill="{C['gold2']}"/><circle cx="4" cy="74" r="1.7" fill="{C['gold2']}"/>
<!-- szal: na wierzchu, powiewa w bok i w gore -->
<path d="M-4 48q-24-10-42-4t-24 10" stroke="{C['szal2']}" stroke-width="10" fill="none" stroke-linecap="round" opacity=".45"/>
<path d="M-4 47q-23-9-40-3t-22 9" stroke="{C['szal']}" stroke-width="7" fill="none" stroke-linecap="round"/>
<path d="M-64 52q-9-1-14 4" stroke="{C['szal']}" stroke-width="5" fill="none" stroke-linecap="round" opacity=".85"/>
<!-- gwiazdka w dloni -->
<g transform="translate(51,79)">
<circle cx="0" cy="0" r="12" fill="{C['gold2']}" opacity=".38" filter="url(#miekkocv)"/>
{_sparkle(0, 0, 7)}
</g>
<!-- nogi -->
<path d="M-5 86v16M13 86v16" stroke="{C['l2']}" stroke-width="6" stroke-linecap="round"/>
<path d="M-9 102h8M9 102h8" stroke="{C['d2']}" stroke-width="5" stroke-linecap="round"/>
<!-- kolnierz -->
<rect x="-4" y="43" width="16" height="9" rx="4" fill="{C['szal']}"/>
<!-- glowa -->
<circle cx="4" cy="27" r="19" fill="{C['skora']}"/>
<path d="M-15 26c-2-18 7-27 19-27s21 9 19 27c1-6-3-10-8-11-6 3-16 4-22 0-5 1-9 5-8 11z" fill="url(#wloscv)"/>
<path d="M-14 16q6-8 14-9M22 16q-6-8-14-9" stroke="{C['wlosy']}" stroke-width="4" fill="none" stroke-linecap="round" opacity=".9"/>
<path d="M-13 9q8-8 17-8t17 8" stroke="{C['wlosy2']}" stroke-width="2.4" fill="none" stroke-linecap="round" opacity=".55"/>
<circle cx="-3" cy="28" r="2.1" fill="{C['ink']}"/><circle cx="11" cy="28" r="2.1" fill="{C['ink']}"/>
<path d="M-1 36q5 4 10 0" stroke="{C['ink']}" stroke-width="1.7" fill="none" stroke-linecap="round"/>
<circle cx="-8" cy="33" r="3" fill="{C['rose2']}" opacity=".42"/>
<circle cx="16" cy="33" r="3" fill="{C['rose2']}" opacity=".42"/>
</g>
</svg>'''


# ---------- 2. BARANEK W SKRZYNCE ----------
def sheep_box():
    return f'''<svg viewBox="0 0 200 160" role="img" aria-label="Skrzynka z dziurkami, w srodku baranek">
<rect x="30" y="52" width="140" height="86" rx="8" fill="{C['l2']}" stroke="{C['d3']}" stroke-width="3"/>
<path d="M30 76h140" stroke="{C['d3']}" stroke-width="2.4"/>
<path d="M30 60l70-34 70 34" fill="{C['l1']}" stroke="{C['d3']}" stroke-width="3" stroke-linejoin="round"/>
<circle cx="70" cy="104" r="7" fill="{C['d2']}"/><circle cx="100" cy="104" r="7" fill="{C['d2']}"/><circle cx="130" cy="104" r="7" fill="{C['d2']}"/>
<g opacity=".95">
<ellipse cx="100" cy="46" rx="26" ry="17" fill="#FFFFFF" stroke="{C['d3']}" stroke-width="2.4"/>
<circle cx="82" cy="36" r="9" fill="#FFFFFF" stroke="{C['d3']}" stroke-width="2"/>
<circle cx="118" cy="36" r="9" fill="#FFFFFF" stroke="{C['d3']}" stroke-width="2"/>
<circle cx="100" cy="30" r="10" fill="#FFFFFF" stroke="{C['d3']}" stroke-width="2"/>
<ellipse cx="128" cy="52" rx="11" ry="9" fill="{C['sand']}" stroke="{C['d3']}" stroke-width="2"/>
<circle cx="132" cy="50" r="1.8" fill="{C['ink']}"/>
</g>
<path d="M46 132h108" stroke="{C['m2']}" stroke-width="3" stroke-linecap="round" opacity=".6"/>
</svg>'''

# ---------- 3. BAOBABY ----------
def baobabs():
    return f'''<svg viewBox="0 0 200 160" role="img" aria-label="Mala planeta rozrywana przez trzy baobaby">
<circle cx="100" cy="120" r="58" fill="{C['m1']}"/>
<path d="M42 116a58 58 0 0 1 116 0 58 58 0 0 0-116 0Z" fill="{C['m3']}" opacity=".4"/>
<g stroke="{C['d2']}" stroke-width="6" stroke-linecap="round" fill="none">
<path d="M70 92V56M70 66l-14-12M70 70l16-14M70 56l-8-14M70 56l10-12"/>
<path d="M128 96V62M128 72l14-12M128 76l-15-12M128 62l9-13M128 62l-9-13"/>
<path d="M100 74V34M100 46l-16-14M100 50l18-16M100 34l-10-14M100 34l12-14"/>
</g>
<circle cx="70" cy="49" r="4" fill="{C['m3']}"/><circle cx="128" cy="55" r="4" fill="{C['m3']}"/><circle cx="100" cy="27" r="4" fill="{C['m3']}"/>
<path d="M60 148c8-6 20-6 28 0M112 150c8-6 20-6 28 0" stroke="{C['d3']}" stroke-width="2.5" fill="none" opacity=".5"/>
</svg>'''

# ---------- 4. ZACHOD SLONCA ----------
def sunsets():
    return f'''<svg viewBox="0 0 200 160" role="img" aria-label="Maly Ksiaze oglada zachod slonca siedzac na krzeselku">
<rect width="200" height="160" rx="10" fill="{C['d2']}"/>
<circle cx="100" cy="112" r="34" fill="{C['gold']}" opacity=".85"/>
<circle cx="100" cy="112" r="20" fill="{C['gold2']}"/>
{stars(".5",.45,10,4)}
<path d="M0 118h200" stroke="{C['m1']}" stroke-width="0" />
<path d="M0 130q50-22 100-2t100-6v38H0z" fill="{C['d3']}"/>
<path d="M0 142q54-14 100 2t100-4v20H0z" fill="{C['d1']}"/>
<g transform="translate(56,104)">
<rect x="0" y="14" width="20" height="4" rx="2" fill="{C['l2']}"/>
<rect x="1" y="0" width="4" height="16" rx="2" fill="{C['l2']}"/>
<rect x="1" y="17" width="3" height="12" rx="1.5" fill="{C['l2']}"/><rect x="16" y="17" width="3" height="12" rx="1.5" fill="{C['l2']}"/>
<circle cx="12" cy="4" r="7" fill="{C['sand']}"/>
<path d="M5 3a7 7 0 0 1 14 0c0-5-3-8-7-8s-7 3-7 8z" fill="{C['gold2']}"/>
</g>
<text x="152" y="34" font-family="Verdana,sans-serif" font-size="20" font-weight="bold" fill="{C['gold2']}">44</text>
</svg>'''

# ---------- 5. ROZA POD KLOSZEM ----------
def rose():
    return f'''<svg viewBox="0 0 200 160" role="img" aria-label="Roza z czterema kolcami pod szklanym kloszem">
<ellipse cx="100" cy="146" rx="60" ry="8" fill="{C['l1']}" opacity=".5"/>
<g transform="translate(100,0)">
<path d="M0 140V70" stroke="{C['d3']}" stroke-width="5" stroke-linecap="round"/>
<path d="M0 112c-20-4-28-16-28-16s18-8 28 6z" fill="{C['m1']}"/>
<path d="M0 96c18-4 26-15 26-15s-17-8-26 5z" fill="{C['m2']}"/>
<g stroke="{C['d2']}" stroke-width="2.6" stroke-linecap="round">
<path d="M0 128l-8-6M0 120l8-6M0 106l-8-5M0 84l8-5"/></g>
<g>
<ellipse cx="0" cy="56" rx="24" ry="20" fill="{C['rose']}"/>
<ellipse cx="0" cy="52" rx="16" ry="14" fill="{C['rose2']}"/>
<ellipse cx="0" cy="50" rx="8" ry="7" fill="{C['rose']}"/>
<path d="M-24 56q24-22 48 0" fill="none" stroke="{C['rose2']}" stroke-width="2"/>
</g>
</g>
<path d="M40 142a62 116 0 0 1 120 0z" fill="{C['l2']}" opacity=".32"/>
<path d="M40 142a62 116 0 0 1 120 0" fill="none" stroke="{C['m2']}" stroke-width="3"/>
<rect x="34" y="140" width="132" height="7" rx="3.5" fill="{C['m2']}"/>
<circle cx="82" cy="46" r="4" fill="{C['l3']}" opacity=".55"/>
</svg>'''

# ---------- 6. LIS ----------
def fox():
    return f"""<svg viewBox="0 0 200 160" role="img" aria-label="Lis siedzacy w zbozu, patrzy na widza">
<rect width="200" height="160" rx="10" fill="{C['l3']}"/>
<g stroke="{C['m3']}" stroke-width="2" opacity=".5">
<path d="M14 150v-42M27 150v-54M40 150v-46M160 150v-50M174 150v-42M187 150v-54" fill="none"/>
</g>
<ellipse cx="100" cy="150" rx="72" ry="7" fill="{C['m3']}" opacity=".3"/>
<path d="M128 142q34 6 46-18t-6-38q-6 18-20 24t-24 16z" fill="{C['m2']}" stroke="{C['d3']}" stroke-width="2.4" stroke-linejoin="round"/>
<path d="M168 86q14 12 8 30-14-2-16-14z" fill="{C['l2']}" stroke="{C['d3']}" stroke-width="2.2" stroke-linejoin="round"/>
<path d="M66 148q4-42 34-42t34 42z" fill="{C['m1']}" stroke="{C['d3']}" stroke-width="2.6"/>
<path d="M86 148q2-26 14-26t14 26z" fill="{C['l2']}" opacity=".5"/>
<path d="M79 64L69 36l26 12z" fill="{C['m1']}" stroke="{C['d3']}" stroke-width="2.6" stroke-linejoin="round"/>
<path d="M78 56l-3-12 12 6z" fill="{C['d3']}" opacity=".5"/>
<path d="M121 64l10-28-26 12z" fill="{C['m1']}" stroke="{C['d3']}" stroke-width="2.6" stroke-linejoin="round"/>
<path d="M122 56l3-12-12 6z" fill="{C['d3']}" opacity=".5"/>
<path d="M100 110c-18 0-29-13-29-28 0-16 13-26 29-26s29 10 29 26c0 15-11 28-29 28z" fill="{C['m2']}" stroke="{C['d3']}" stroke-width="2.6"/>
<path d="M100 114c-9 0-16-5-19-13-2-6 6-11 19-11s21 5 19 11c-3 8-10 13-19 13z" fill="{C['l2']}" stroke="{C['d3']}" stroke-width="2"/>
<circle cx="87" cy="76" r="4.4" fill="{C['ink']}"/><circle cx="113" cy="76" r="4.4" fill="{C['ink']}"/>
<circle cx="88.6" cy="74.4" r="1.5" fill="#fff"/><circle cx="114.6" cy="74.4" r="1.5" fill="#fff"/>
<path d="M100 97l-6-5h12z" fill="{C['ink']}"/>
<path d="M100 99v4M100 103q-5 4-9 1M100 103q5 4 9 1" stroke="{C['ink']}" stroke-width="1.8" fill="none" stroke-linecap="round"/>
</svg>"""

# ---------- 7. WAZ ----------
def snake():
    return f'''<svg viewBox="0 0 200 160" role="img" aria-label="Zolty waz na piasku pustyni">
<rect width="200" height="160" rx="10" fill="{C['d2']}"/>
<path d="M0 118q50-16 100 0t100-6v48H0z" fill="{C['d3']}"/>
{stars(".45",.42,6,2)}
<path d="M22 132q26-30 52-6t54-14 44-16" fill="none" stroke="{C['gold']}" stroke-width="10" stroke-linecap="round"/>
<path d="M22 132q26-30 52-6t54-14 44-16" fill="none" stroke="{C['gold2']}" stroke-width="4" stroke-linecap="round" opacity=".7"/>
<circle cx="172" cy="96" r="8" fill="{C['gold']}"/>
<circle cx="175" cy="94" r="2" fill="{C['ink']}"/>
<path d="M180 97l10-2-10-2" fill="none" stroke="{C['rose']}" stroke-width="1.8" stroke-linecap="round"/>
</svg>'''

# ---------- 8. OGROD ROZ ----------
def rose_garden():
    roses = ""
    import math
    pos = [(30,96),(60,84),(90,98),(120,82),(150,96),(180,86),(45,120),(75,112),(105,124),(135,110),(165,122)]
    for i,(x,y) in enumerate(pos):
        r = 9 if i % 2 == 0 else 8
        roses += (f'<path d="M{x} {y+30}V{y+6}" stroke="{C["d3"]}" stroke-width="3" stroke-linecap="round"/>'
                  f'<ellipse cx="{x}" cy="{y}" rx="{r+2}" ry="{r}" fill="{C["rose"]}"/>'
                  f'<circle cx="{x}" cy="{y}" r="{r-4}" fill="{C["rose2"]}"/>')
    return f'''<svg viewBox="0 0 200 160" role="img" aria-label="Ogrod pelen piecu tysiecy takich samych roz">
<rect width="200" height="160" rx="10" fill="{C['l3']}"/>
<rect y="126" width="200" height="34" fill="{C['m3']}" opacity=".45"/>
{roses}
<g transform="translate(100,138)"><circle cx="0" cy="-4" r="7" fill="{C['sand']}"/>
<path d="M-7 -5a7 7 0 0 1 14 0c0-5-3-8-7-8s-7 3-7 8z" fill="{C['gold2']}"/>
<path d="M0 3v10" stroke="{C['gold']}" stroke-width="6" stroke-linecap="round"/></g>
</svg>'''

# ---------- 9. STUDNIA ----------
def well():
    return f'''<svg viewBox="0 0 200 160" role="img" aria-label="Stara studnia z kolowrotem i wiadrem na pustyni">
<rect width="200" height="160" rx="10" fill="{C['d2']}"/>
{stars(".5",.45,8,2)}
<path d="M0 126q50-12 100 2t100-8v40H0z" fill="{C['d3']}"/>
<circle cx="100" cy="52" r="30" fill="url(#glowwell)"/>
<defs><radialGradient id="glowwell"><stop offset="0%" stop-color="{C['gold2']}" stop-opacity=".45"/><stop offset="100%" stop-color="{C['gold2']}" stop-opacity="0"/></radialGradient></defs>
<rect x="62" y="112" width="76" height="30" rx="5" fill="{C['l2']}" stroke="{C['d1']}" stroke-width="2.5"/>
<path d="M62 122h76M84 112v30M116 112v30" stroke="{C['d1']}" stroke-width="2"/>
<rect x="70" y="60" width="7" height="56" fill="{C['m2']}"/><rect x="123" y="60" width="7" height="56" fill="{C['m2']}"/>
<path d="M60 62l40-22 40 22z" fill="{C['m1']}" stroke="{C['d1']}" stroke-width="2.5" stroke-linejoin="round"/>
<rect x="68" y="74" width="64" height="7" rx="3.5" fill="{C['d1']}"/>
<path d="M100 81v18" stroke="{C['l2']}" stroke-width="2"/>
<rect x="90" y="99" width="20" height="16" rx="3" fill="{C['gold']}" stroke="{C['d1']}" stroke-width="2"/>
<path d="M132 78q10 0 10 8t-8 6" fill="none" stroke="{C['l2']}" stroke-width="3" stroke-linecap="round"/>
</svg>'''

# ---------- 10. GWIAZDY / POZEGNANIE ----------
def stars_laugh():
    bells = ""
    for x, y, s in [(52,46,1),(100,32,1.2),(150,50,.9),(74,74,.8),(128,72,.85)]:
        bells += (f'<g transform="translate({x},{y}) scale({s})">'
                  f'<circle cx="0" cy="0" r="13" fill="{C["gold2"]}"/>'
                  f'<circle cx="-4.5" cy="-2" r="1.7" fill="{C["ink"]}"/><circle cx="4.5" cy="-2" r="1.7" fill="{C["ink"]}"/>'
                  f'<path d="M-5 4q5 5 10 0" stroke="{C["ink"]}" stroke-width="1.6" fill="none" stroke-linecap="round"/></g>')
    return f'''<svg viewBox="0 0 200 160" role="img" aria-label="Gwiazdy, ktore sie smieja jak piecset milionow dzwoneczkow">
<rect width="200" height="160" rx="10" fill="{C['d1']}"/>
{stars(".7",.46,4,4)}
{bells}
<path d="M0 132q50-14 100 0t100-6v34H0z" fill="{C['d3']}"/>
<g transform="translate(100,116)">
<circle cx="0" cy="-8" r="8" fill="{C['sand']}"/>
<path d="M-8 -9a8 8 0 0 1 16 0c0-6-3-9-8-9s-8 3-8 9z" fill="{C['gold2']}"/>
<path d="M0 0v12" stroke="{C['gold']}" stroke-width="7" stroke-linecap="round"/>
<path d="M-7 4l-8 8M7 4l8 8" stroke="{C['gold']}" stroke-width="4" stroke-linecap="round"/>
</g>
</svg>'''

# ---------- IKONY PLANET / MIEJSC ----------
def icon(name, size=64):
    b = f'<svg viewBox="0 0 64 64" width="{size}" height="{size}" aria-hidden="true">'
    e = '</svg>'
    g, d, l, m, w = C['gold'], C['d2'], C['l2'], C['m1'], C['l1']
    P = {
    "plane": f'<circle cx="32" cy="32" r="30" fill="{m}"/><path d="M14 36l36-14-8 18 6 8-10-4-8 6-2-10z" fill="{l}"/>',
    "sheep": f'<circle cx="32" cy="32" r="30" fill="{m}"/><ellipse cx="30" cy="36" rx="15" ry="10" fill="#fff"/><circle cx="20" cy="28" r="7" fill="#fff"/><circle cx="32" cy="24" r="7" fill="#fff"/><circle cx="43" cy="30" r="6" fill="#fff"/><ellipse cx="45" cy="40" rx="7" ry="6" fill="{C["sand"]}"/><circle cx="47" cy="39" r="1.4" fill="{d}"/>',
    "question": f'<circle cx="32" cy="32" r="30" fill="{m}"/><path d="M24 24a8 8 0 1 1 12 8c-3 2-4 4-4 7" stroke="{l}" stroke-width="5" fill="none" stroke-linecap="round"/><circle cx="32" cy="47" r="3.2" fill="{l}"/>',
    "asteroid": f'<circle cx="32" cy="32" r="30" fill="{d}"/><circle cx="32" cy="34" r="17" fill="{m}"/><ellipse cx="32" cy="34" rx="27" ry="8" fill="none" stroke="{g}" stroke-width="3" transform="rotate(-18 32 34)"/><circle cx="26" cy="30" r="3" fill="{C["d3"]}"/>',
    "baobab": f'<circle cx="32" cy="32" r="30" fill="{m}"/><path d="M32 50V22M32 30l-10-8M32 32l11-9M32 22l-7-8M32 22l8-8" stroke="{d}" stroke-width="4.5" fill="none" stroke-linecap="round"/><path d="M16 52h32" stroke="{l}" stroke-width="4" stroke-linecap="round"/>',
    "sun": f'<circle cx="32" cy="32" r="30" fill="{d}"/><circle cx="32" cy="38" r="14" fill="{g}"/><path d="M6 44h52" stroke="{C["d3"]}" stroke-width="6"/><g stroke="{C["gold2"]}" stroke-width="3" stroke-linecap="round"><path d="M32 14v6M14 24l4 4M50 24l-4 4"/></g>',
    "thorn": f'<circle cx="32" cy="32" r="30" fill="{m}"/><path d="M32 52V20" stroke="{d}" stroke-width="4" stroke-linecap="round"/><g stroke="{l}" stroke-width="3" stroke-linecap="round"><path d="M32 44l-8-6M32 36l8-6M32 28l-8-5"/></g><circle cx="32" cy="18" r="6" fill="{C["rose"]}"/>',
    "rose": f'<circle cx="32" cy="32" r="30" fill="{m}"/><path d="M32 54V32" stroke="{d}" stroke-width="4" stroke-linecap="round"/><ellipse cx="32" cy="24" rx="13" ry="11" fill="{C["rose"]}"/><circle cx="32" cy="24" r="5" fill="{C["rose2"]}"/><path d="M32 42c-9-2-13-8-13-8s9-4 13 3z" fill="{C["d3"]}"/>',
    "volcano": f'<circle cx="32" cy="32" r="30" fill="{m}"/><path d="M14 48l12-20 12 20z" fill="{d}"/><path d="M36 50l8-14 8 14z" fill="{C["d3"]}"/><path d="M22 30q4-8 8 0z" fill="{g}"/>',
    "crown": f'<circle cx="32" cy="32" r="30" fill="{m}"/><path d="M16 42l-4-18 10 7 10-13 10 13 10-7-4 18z" fill="{g}" stroke="{d}" stroke-width="2" stroke-linejoin="round"/><rect x="16" y="42" width="32" height="6" rx="3" fill="{d}"/>',
    "hat": f'<circle cx="32" cy="32" r="30" fill="{m}"/><ellipse cx="32" cy="44" rx="24" ry="6" fill="{l}"/><path d="M20 44V26a12 8 0 0 1 24 0v18z" fill="{C["d3"]}"/><path d="M20 34h24" stroke="{g}" stroke-width="4"/>',
    "bottle": f'<circle cx="32" cy="32" r="30" fill="{m}"/><path d="M27 16h10v8l6 10v20H21V34l6-10z" fill="{C["d3"]}" stroke="{d}" stroke-width="2"/><rect x="21" y="40" width="22" height="14" fill="{C["d2"]}"/><rect x="25" y="12" width="14" height="5" rx="2" fill="{g}"/>',
    "coins": f'<circle cx="32" cy="32" r="30" fill="{m}"/><ellipse cx="32" cy="44" rx="16" ry="6" fill="{g}"/><ellipse cx="32" cy="36" rx="16" ry="6" fill="{C["gold2"]}"/><ellipse cx="32" cy="28" rx="16" ry="6" fill="{g}"/><ellipse cx="32" cy="20" rx="16" ry="6" fill="{C["gold2"]}"/>',
    "lamp": f'<circle cx="32" cy="32" r="30" fill="{d}"/><path d="M24 26h16l-3 22H27z" fill="{g}"/><path d="M22 26l10-12 10 12z" fill="{C["d3"]}"/><rect x="28" y="48" width="8" height="8" fill="{C["d3"]}"/><circle cx="32" cy="34" r="16" fill="{C["gold2"]}" opacity=".22"/>',
    "book": f'<circle cx="32" cy="32" r="30" fill="{m}"/><path d="M14 20h16a4 4 0 0 1 4 4v24a6 6 0 0 0-6-4H14z" fill="{l}"/><path d="M50 20H34a4 4 0 0 0-4 4v24a6 6 0 0 1 6-4h14z" fill="{C["l1"]}"/><path d="M32 24v24" stroke="{d}" stroke-width="2"/>',
    "earth": f'<circle cx="32" cy="32" r="30" fill="{C["d3"]}"/><circle cx="32" cy="32" r="22" fill="{C["m2"]}"/><path d="M16 26q10 6 20 0t12 4-10 10-14-2-8-12z" fill="{C["d2"]}" opacity=".6"/><ellipse cx="32" cy="32" rx="22" ry="8" fill="none" stroke="{l}" stroke-width="1.6" opacity=".6"/>',
    "snake": f'<circle cx="32" cy="32" r="30" fill="{d}"/><path d="M12 44q10-14 20-4t20-10" fill="none" stroke="{g}" stroke-width="7" stroke-linecap="round"/><circle cx="52" cy="30" r="5" fill="{g}"/><circle cx="53" cy="29" r="1.6" fill="{d}"/>',
    "flower3": f'<circle cx="32" cy="32" r="30" fill="{m}"/><path d="M32 52V28" stroke="{d}" stroke-width="4" stroke-linecap="round"/><circle cx="32" cy="22" r="6" fill="{C["l2"]}"/><circle cx="22" cy="28" r="5" fill="{C["l1"]}"/><circle cx="42" cy="28" r="5" fill="{C["l1"]}"/>',
    "echo": f'<circle cx="32" cy="32" r="30" fill="{m}"/><path d="M8 50l16-26 10 16 8-12 14 22z" fill="{C["d3"]}"/><g fill="none" stroke="{l}" stroke-width="2.6" stroke-linecap="round"><path d="M40 18a10 10 0 0 1 0 12M46 14a16 16 0 0 1 0 20"/></g>',
    "garden": f'<circle cx="32" cy="32" r="30" fill="{m}"/><g fill="{C["rose"]}"><circle cx="18" cy="28" r="6"/><circle cx="32" cy="22" r="6"/><circle cx="46" cy="28" r="6"/><circle cx="25" cy="40" r="6"/><circle cx="39" cy="40" r="6"/></g><path d="M12 52h40" stroke="{C["d3"]}" stroke-width="4" stroke-linecap="round"/>',
    "fox": f'<circle cx="32" cy="32" r="30" fill="{C["d3"]}"/><path d="M32 48c-11 0-18-8-18-17s7-15 18-15 18 6 18 15-7 17-18 17z" fill="{C["m2"]}"/><path d="M18 20l-4-10 12 5zM46 20l4-10-12 5z" fill="{m}"/><circle cx="25" cy="31" r="3" fill="{d}"/><circle cx="39" cy="31" r="3" fill="{d}"/><path d="M32 38l-4-3h8z" fill="{d}"/>',
    "train": f'<circle cx="32" cy="32" r="30" fill="{m}"/><rect x="14" y="20" width="36" height="22" rx="5" fill="{l}"/><rect x="19" y="25" width="10" height="9" fill="{C["d3"]}"/><rect x="35" y="25" width="10" height="9" fill="{C["d3"]}"/><circle cx="22" cy="46" r="5" fill="{d}"/><circle cx="42" cy="46" r="5" fill="{d}"/>',
    "pill": f'<circle cx="32" cy="32" r="30" fill="{m}"/><rect x="14" y="26" width="36" height="14" rx="7" fill="{l}" transform="rotate(-20 32 33)"/><path d="M32 33m0 0" fill="none"/><rect x="14" y="26" width="18" height="14" rx="7" fill="{g}" transform="rotate(-20 32 33)"/>',
    "walk": f'<circle cx="32" cy="32" r="30" fill="{d}"/><path d="M6 48q26-10 52 0" stroke="{C["d3"]}" stroke-width="8" fill="none"/><circle cx="26" cy="22" r="5" fill="{C["sand"]}"/><path d="M26 27v12l-6 10M26 39l7 10M20 32l12-4 8 6" stroke="{g}" stroke-width="3.5" fill="none" stroke-linecap="round"/>',
    "well": f'<circle cx="32" cy="32" r="30" fill="{m}"/><rect x="20" y="36" width="24" height="16" rx="3" fill="{l}"/><path d="M18 32l14-10 14 10z" fill="{C["d3"]}"/><rect x="22" y="35" width="20" height="4" fill="{d}"/><path d="M32 39v6" stroke="{d}" stroke-width="2"/>',
    "star": f'<circle cx="32" cy="32" r="30" fill="{d}"/><path d="M32 12l6 14 15 1-11 10 3 15-13-8-13 8 3-15-11-10 15-1z" fill="{g}"/><circle cx="27" cy="30" r="1.8" fill="{d}"/><circle cx="37" cy="30" r="1.8" fill="{d}"/><path d="M27 36q5 5 10 0" stroke="{d}" stroke-width="1.8" fill="none" stroke-linecap="round"/>',
    "letter": f'<circle cx="32" cy="32" r="30" fill="{m}"/><rect x="14" y="22" width="36" height="24" rx="4" fill="{l}"/><path d="M14 24l18 14 18-14" fill="none" stroke="{C["d3"]}" stroke-width="3"/>',
    }
    return b + P.get(name, P["star"]) + e

# ---------- DRABINA TEORII UMYSLU ----------
def tom_ladder():
    kolory = [C['l1'], C['m3'], C['m2'], C['m1'], C['d3']]
    krotkie = ["co widzę?", "co czuje?", "czego chce?", "co myśli?", "co myśli o mnie?"]
    out = []
    for i in range(5):
        x = 26 + i * 74
        w = 88
        y = 236 - i * 42
        col = kolory[i]
        ciemny = i >= 3
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{236 - y + 46:.0f}" rx="10" fill="{col}" opacity=".28"/>')
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="42" rx="10" fill="{col}" stroke="{C["d2"]}" stroke-width="1.6"/>')
        tc = "#FFFFFF" if ciemny else C['d1']
        out.append(f'<text x="{x+14}" y="{y+27}" font-family="Verdana,sans-serif" font-size="17" font-weight="bold" fill="{tc}">E{i+1}</text>')
        out.append(f'<text x="{x+44}" y="{y+26}" font-family="Verdana,sans-serif" font-size="9" fill="{tc}">{krotkie[i]}</text>')
    return f"""<svg viewBox="0 0 420 300" role="img" aria-label="Schody teorii umyslu: piec stopni od E1 na dole do E5 na gorze">
<rect width="420" height="300" rx="12" fill="{C['l3']}"/>
<text x="24" y="30" font-family="Verdana,sans-serif" font-size="12" font-weight="bold" fill="{C['d2']}">CORAZ TRUDNIEJ</text>
<path d="M170 24l14 0m-4-5 5 5-5 5" stroke="{C['gold']}" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
{"".join(out)}
<g transform="translate(360,34)">
<circle cx="0" cy="0" r="11" fill="{C['sand']}"/>
<path d="M-11 -1a11 11 0 0 1 22 0c0-8-4-12-11-12s-11 4-11 12z" fill="{C['gold2']}"/>
<path d="M0 12v16" stroke="{C['gold']}" stroke-width="8" stroke-linecap="round"/>
<path d="M-9 18l-9 7M9 18l9 7" stroke="{C['gold']}" stroke-width="5" stroke-linecap="round"/>
</g>
<path d="M24 288h372" stroke="{C['m3']}" stroke-width="3" stroke-linecap="round"/>
<text x="24" y="282" font-family="Verdana,sans-serif" font-size="9" fill="{C['szary'] if 'szary' in C else C['d3']}">start</text>
</svg>"""

# ---------- TERMOMETR EMOCJI ----------
# Piec poziomow natezenia. Kazdy poziom ma cztery niezalezne sygnaly:
# kolor, wysokosc slupka, mine i liczbe kropek. Uczen, ktory nie czyta,
# korzysta z trzech ostatnich - slowo jest wtedy podpowiedzia dla doroslego.
POZIOMY = [
    (5, "BARDZO MOCNO", "#B23A48", "trudno mi teraz myśleć"),
    (4, "MOCNO",        "#D97A45", "czuję to w całym ciele"),
    (3, "ŚREDNIO",      C["gold"], "czuję to wyraźnie"),
    (2, "TROCHĘ",       C["m2"],   "czuję to lekko"),
    (1, "LEDWO CZUJĘ",  C["m3"],   "prawie nic nie czuję"),
]


def _buzka(cx, cy, r, poziom):
    """Mina rosnaca z natezeniem - od spokojnej do bardzo napietej."""
    s = r / 34.0
    ox, oy = 12.4 * s, 5.0 * s
    ro = (3.4 + poziom * 0.85) * s
    brew = (poziom - 1) * 1.9 * s        # brwi unosza sie symetrycznie
    by, bw = (13.0 + poziom * 1.1) * s, 8.6 * s
    mw = (8.5 + poziom * 2.0) * s
    mh = (1.3 + (poziom - 1) * 3.6) * s
    my = 15.0 * s
    k = C["ink"]
    g = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#FFFFFF" opacity=".95"/>',
         f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{k}" '
         f'stroke-width="{2.1 * s:.2f}" opacity=".5"/>']
    for zn in (-1, 1):
        x = cx + zn * ox
        g.append(f'<circle cx="{x:.1f}" cy="{cy - oy:.1f}" r="{ro:.2f}" fill="{k}"/>')
        xw, xz = x + zn * bw, x - zn * bw          # koniec zewnetrzny i wewnetrzny
        g.append(f'<path d="M{xw:.1f} {cy - by + brew:.1f} L{xz:.1f} {cy - by - brew:.1f}" '
                 f'stroke="{k}" stroke-width="{2.4 * s:.2f}" stroke-linecap="round" fill="none"/>')
    g.append(f'<ellipse cx="{cx}" cy="{cy + my:.1f}" rx="{mw:.2f}" ry="{mh:.2f}" fill="{k}"/>')
    if poziom >= 4:                      # kreski "az mnie rozsadza"
        for zn in (-1, 1):
            for dx, dy in ((1.16, -0.62), (1.30, -0.05), (1.16, 0.52)):
                x1, y1 = cx + zn * dx * r, cy + dy * r
                x2, y2 = cx + zn * (dx + 0.24) * r, cy + dy * 1.22 * r
                g.append(f'<path d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}" stroke="{k}" '
                         f'stroke-width="{2.2 * s:.2f}" stroke-linecap="round" opacity=".5"/>')
    return "".join(g)


def _kropki(x, y, ile, kolor, r=4.2, odstep=13.0):
    """Tyle kropek, ile stopni - liczenie dziala bez czytania."""
    out = []
    for i in range(5):
        wypelnienie = kolor if i < ile else "none"
        przezr = "1" if i < ile else ".5"
        out.append(f'<circle cx="{x + i * odstep:.1f}" cy="{y:.1f}" r="{r}" '
                   f'fill="{wypelnienie}" stroke="{kolor}" stroke-width="1.6" '
                   f'opacity="{przezr}"/>')
    return "".join(out)


def _rurka(x, y0, y1, sz, uid):
    """Szklana rurka z banka i barwnym slupkiem."""
    r = sz / 2.0
    banka = r * 1.42
    cy = y1 + banka * 0.62
    czesci = [
        f'<defs><linearGradient id="slup{uid}" x1="0" y1="1" x2="0" y2="0">'
        f'<stop offset="0" stop-color="{C["m3"]}"/><stop offset=".28" stop-color="{C["m2"]}"/>'
        f'<stop offset=".52" stop-color="{C["gold"]}"/><stop offset=".76" stop-color="#D97A45"/>'
        f'<stop offset="1" stop-color="#B23A48"/></linearGradient>'
        f'<linearGradient id="szklo{uid}" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0" stop-color="#FFFFFF" stop-opacity=".85"/>'
        f'<stop offset=".45" stop-color="#FFFFFF" stop-opacity=".12"/>'
        f'<stop offset="1" stop-color="{C["d3"]}" stop-opacity=".2"/></linearGradient></defs>',
        f'<circle cx="{x + r:.1f}" cy="{cy:.1f}" r="{banka + 4:.1f}" fill="{C["l2"]}" '
        f'stroke="{C["d3"]}" stroke-width="2.6"/>',
        f'<rect x="{x - 3:.1f}" y="{y0 - 3:.1f}" width="{sz + 6:.1f}" height="{y1 - y0 + 10:.1f}" '
        f'rx="{r + 3:.1f}" fill="{C["l2"]}" stroke="{C["d3"]}" stroke-width="2.6"/>',
        f'<circle cx="{x + r:.1f}" cy="{cy:.1f}" r="{banka:.1f}" fill="#B23A48"/>',
        f'<rect x="{x + 2.6:.1f}" y="{y0 + 3:.1f}" width="{sz - 5.2:.1f}" '
        f'height="{y1 - y0 + banka * 0.6:.1f}" rx="{r - 2.6:.1f}" fill="url(#slup{uid})"/>',
        f'<rect x="{x - 3:.1f}" y="{y0 - 3:.1f}" width="{sz + 6:.1f}" height="{y1 - y0 + 10:.1f}" '
        f'rx="{r + 3:.1f}" fill="url(#szklo{uid})"/>',
        f'<rect x="{x + 4.5:.1f}" y="{y0 + 8:.1f}" width="{max(3.0, sz * 0.16):.1f}" '
        f'height="{y1 - y0 - 14:.1f}" rx="2" fill="#FFFFFF" opacity=".45"/>',
    ]
    return "".join(czesci)


def thermometer():
    """Wersja podreczna do czesci B - zwarta, zeby napisy zostaly czytelne w druku."""
    W, H = 400, 232
    y0, wys = 8, 43
    out = [_rurka(24, y0 + 6, y0 + 5 * wys - 40, 34, "t1")]
    for i, (n, slowo, kol, _cialo) in enumerate(POZIOMY):
        y = y0 + i * wys
        cy = y + wys / 2 - 3
        out.append(f'<path d="M70 {cy:.0f}h14" stroke="{C["d3"]}" stroke-width="2.6" stroke-linecap="round"/>')
        out.append(f'<rect x="88" y="{y:.0f}" width="{W - 106}" height="{wys - 9}" rx="11" '
                   f'fill="#FFFFFF" stroke="{C["l1"]}" stroke-width="1.5"/>')
        out.append(f'<rect x="88" y="{y:.0f}" width="8" height="{wys - 9}" rx="4" fill="{kol}"/>')
        out.append(f'<circle cx="122" cy="{cy:.0f}" r="17" fill="{kol}" opacity=".18"/>')
        out.append(_buzka(122, cy, 15, n))
        out.append(f'<text x="146" y="{cy + 8:.0f}" font-family="Verdana,sans-serif" font-size="23" '
                   f'font-weight="bold" fill="{kol}">{n}</text>')
        out.append(f'<text x="172" y="{cy + 6:.0f}" font-family="Verdana,sans-serif" font-size="16" '
                   f'font-weight="bold" fill="{C["d2"]}">{slowo}</text>')
        out.append(_kropki(W - 86, cy, n, kol, 4.0, 12.0))
    return (f'<svg viewBox="0 0 {W} {H}" role="img" '
            f'aria-label="Termometr emocji: piec poziomow natezenia od 1 do 5">'
            f'<rect width="{W}" height="{H}" rx="12" fill="{C["l3"]}"/>'
            f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="11" fill="none" '
            f'stroke="{C["l1"]}" stroke-width="2"/>{"".join(out)}</svg>')


def thermometer_cut():
    """Wersja do wyciecia: duza plansza + osobny pasek wskaznikow."""
    W, KARTA = 430, 500
    H = KARTA + 112
    y0, wys = 92, 76
    out = [
        f'<rect x="6" y="6" width="{W - 12}" height="{KARTA - 12}" rx="20" fill="#FFFFFF" '
        f'stroke="{C["d3"]}" stroke-width="2.4" stroke-dasharray="9 7"/>',
        f'<rect x="16" y="16" width="{W - 32}" height="{KARTA - 32}" rx="14" fill="{C["l3"]}"/>',
        f'<text x="{W / 2:.0f}" y="52" text-anchor="middle" font-family="Verdana,sans-serif" '
        f'font-size="23" font-weight="bold" fill="{C["d1"]}">TERMOMETR EMOCJI</text>',
        f'<text x="{W / 2:.0f}" y="76" text-anchor="middle" font-family="Verdana,sans-serif" '
        f'font-size="15" fill="{C["d3"]}">Jak mocno to czuję?</text>',
        f'<path d="M60 88h{W - 120}" stroke="{C["l1"]}" stroke-width="2.4" stroke-linecap="round"/>',
        _rurka(40, y0 + 6, y0 + 5 * wys - 48, 44, "t2"),
    ]
    for i, (n, slowo, kol, cialo) in enumerate(POZIOMY):
        y = y0 + i * wys
        cy = y + wys / 2 - 7
        out.append(f'<path d="M108 {cy:.0f}h16" stroke="{C["d3"]}" stroke-width="3.4" stroke-linecap="round"/>')
        out.append(f'<rect x="128" y="{y:.0f}" width="{W - 160}" height="{wys - 12}" rx="16" '
                   f'fill="#FFFFFF" stroke="{kol}" stroke-width="2.2"/>')
        out.append(f'<circle cx="170" cy="{cy:.0f}" r="25" fill="{kol}" opacity=".16"/>')
        out.append(_buzka(170, cy, 22, n))
        out.append(f'<text x="210" y="{cy + 11:.0f}" font-family="Verdana,sans-serif" font-size="33" '
                   f'font-weight="bold" fill="{kol}">{n}</text>')
        out.append(f'<text x="248" y="{cy - 7:.0f}" font-family="Verdana,sans-serif" font-size="15" '
                   f'font-weight="bold" fill="{C["d2"]}">{slowo}</text>')
        out.append(f'<text x="248" y="{cy + 10:.0f}" font-family="Verdana,sans-serif" font-size="11.5" '
                   f'fill="{C["d3"]}">{cialo}</text>')
        out.append(_kropki(249, cy + 25, n, kol, 4.4, 13.5))
    py = KARTA + 10
    out.append(f'<rect x="6" y="{py:.0f}" width="{W - 12}" height="96" rx="16" fill="#FFFFFF" '
               f'stroke="{C["d3"]}" stroke-width="2.4" stroke-dasharray="9 7"/>')
    out.append(f'<text x="26" y="{py + 26:.0f}" font-family="Verdana,sans-serif" font-size="12.5" '
               f'font-weight="bold" fill="{C["d2"]}">WSKAŹNIKI — wytnij i przypnij spinaczem</text>')
    for j, kol in enumerate((C["d3"], C["gold"], "#B23A48")):
        x, yy = 30 + j * 132, py + 40
        out.append(f'<path d="M{x} {yy + 18:.0f} L{x + 30} {yy:.0f} L{x + 108} {yy:.0f} '
                   f'L{x + 108} {yy + 36:.0f} L{x + 30} {yy + 36:.0f} Z" fill="{kol}" '
                   f'stroke="{C["d1"]}" stroke-width="1.8" stroke-dasharray="6 4"/>')
        out.append(f'<text x="{x + 72}" y="{yy + 24:.0f}" text-anchor="middle" '
                   f'font-family="Verdana,sans-serif" font-size="13" font-weight="bold" '
                   f'fill="#FFFFFF">TERAZ</text>')
    return (f'<svg viewBox="0 0 {W} {H}" role="img" '
            f'aria-label="Termometr emocji do wyciecia wraz ze wskaznikami">'
            f'{"".join(out)}</svg>')


# ---------- SYGNALIZATOR OCENY SYTUACJI ----------
def traffic():
    return f'''<svg viewBox="0 0 420 160" role="img" aria-label="Sygnalizator oceny sytuacji: zielone, zolte, czerwone">
<rect width="420" height="160" rx="12" fill="{C['l3']}"/>
<g>
<circle cx="70" cy="80" r="34" fill="#2E9E5B"/><text x="70" y="87" text-anchor="middle" font-family="Verdana" font-size="26" fill="#fff">&#10003;</text>
<text x="118" y="74" font-family="Verdana" font-size="14" font-weight="bold" fill="{C['d2']}">W PORZĄDKU</text>
<text x="118" y="94" font-family="Verdana" font-size="12.5" fill="{C['d3']}">Nikomu nie stała się krzywda.</text>
</g>
<g transform="translate(0,0)">
<circle cx="70" cy="80" r="34" fill="#2E9E5B" opacity="0"/>
</g>
<g transform="translate(0,0)"></g>
<g transform="translate(0,0)">
<circle cx="248" cy="44" r="0" fill="none"/>
</g>
</svg>'''

# ---------- SCENY NA KARTY BEZ ZDJEC ----------
# Rysowane w proporcji paska karty (200x96). Postacie z profilu - sylwetka
# z boku czyta sie czytelniej niz twarz na front przy tej wielkosci.

def _postac_profil(x, y, s=1.0, plaszcz=None, wlosy=None, pochylona=False):
    """Sylwetka z profilu. Nos i czupryna wystarcza, zeby profil byl czytelny."""
    plaszcz = plaszcz or C["d3"]
    wlosy = wlosy or C["wlosy"]
    kat = "rotate(10)" if pochylona else ""
    return f'''<g transform="translate({x},{y}) scale({s}) {kat}">
<path d="M-7 0c0-11 3-17 7-17s7 6 7 17z" fill="{plaszcz}" stroke="{C['d1']}" stroke-width="1"/>
<circle cx="0" cy="-21" r="5.4" fill="{C['skora']}" stroke="{C['d1']}" stroke-width=".9"/>
<path d="M5.2 -21.6l2.2 1.6-2.2 1.4z" fill="{C['skora']}" stroke="{C['d1']}" stroke-width=".7" stroke-linejoin="round"/>
<path d="M-5.6 -22.6c.6-5.4 9-5.4 10.2-1-3-2.6-7.4-3-10.2 1z" fill="{wlosy}"/>
</g>'''


def geograf_scena():
    """Geograf przy biurku: ksiegi, globus, lupa - i kwiat, ktorego nie zapisuje."""
    L = 72                                   # linia blatu
    return f'''<svg viewBox="0 0 200 96" role="img" aria-label="Geograf przy biurku pelnym ksiag i globusie">
{_defs("gg")}
<rect width="200" height="96" fill="{C['sand']}"/>
{_wash(52, 24, 44, C['gold'], ".22", "gg")}
{_wash(166, 36, 40, C['m3'], ".20", "gg")}
<g>
  <circle cx="162" cy="42" r="22" fill="{C['m1']}" stroke="{C['d1']}" stroke-width="1.4"/>
  <path d="M144 34c11 4 25 4 36 0M144 50c11-4 25-4 36 0" stroke="{C['l2']}" stroke-width="1.1" fill="none" opacity=".8"/>
  <path d="M162 20v44" stroke="{C['l2']}" stroke-width="1.1" opacity=".6"/>
  <path d="M151 28c-5 10-5 19 0 24 6-10 6-16 0-24z" fill="{C['l1']}" opacity=".65"/>
  <path d="M170 36c4 4 4 11 1 15-3-5-3-11-1-15z" fill="{C['l1']}" opacity=".5"/>
  <path d="M162 64v6h-9v2h18v-2h-9z" fill="{C['d1']}"/>
</g>
{_postac_profil(74, L, 1.9, C['d3'], C['wlosy2'], True)}
<path d="M84 {L - 22}c12 2 20 8 24 14" stroke="{C['d3']}" stroke-width="7"
      stroke-linecap="round" fill="none"/>
<circle cx="110" cy="{L - 7}" r="3.4" fill="{C['skora']}" stroke="{C['d1']}" stroke-width=".8"/>
<path d="M0 {L}h200v{96 - L}H0z" fill="{C['d2']}"/>
<path d="M0 {L - 2}h200v4H0z" fill="{C['d1']}"/>
<g>
  <path d="M112 {L - 1}c9-7 18-7 24 0 6-7 15-7 24 0-9 4-15 4-24 1-9 3-15 3-24-1z"
        fill="#FFFFFF" stroke="{C['d1']}" stroke-width="1.2" stroke-linejoin="round"/>
  <path d="M136 {L - 1}v-7" stroke="{C['d1']}" stroke-width="1.1"/>
  <path d="M118 {L - 6}h13M141 {L - 6}h13" stroke="{C['d3']}" stroke-width=".8" opacity=".6"/>
</g>
<g>
  <path d="M14 {L}V{L - 10}h28v10z" fill="{C['l1']}" stroke="{C['d1']}" stroke-width="1.1"/>
  <path d="M18 {L - 10}v-8h28v8z" fill="{C['gold2']}" stroke="{C['d1']}" stroke-width="1.1"/>
  <path d="M22 {L - 18}v-7h26v7z" fill="{C['rose2']}" stroke="{C['d1']}" stroke-width="1.1"/>
</g>
<g>
  <path d="M190 {L}V{L - 12}" stroke="{C['m1']}" stroke-width="1.6"/>
  <circle cx="190" cy="{L - 15}" r="4.4" fill="{C['rose']}"/>
  <path d="M184 {L - 7}c4-4 8-4 12 0" stroke="{C['m1']}" stroke-width="1.4" fill="none"/>
</g>
</svg>'''


def ziemia_scena():
    """Ziemia z kosmosu i maly punkt na pustyni: siodma planeta, a jednak samotnie."""
    gw = "".join(
        f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C["l2"]}" opacity=".8"/>'
        for x, y, r in [(14, 14, 1.2), (34, 30, .9), (58, 10, 1.1), (86, 24, .8),
                        (172, 12, 1.3), (188, 34, 1.0), (152, 30, .9), (24, 46, 1.0),
                        (196, 62, .9), (8, 62, 1.1), (120, 8, 1.0), (104, 34, .8)])
    return f'''<svg viewBox="0 0 200 96" role="img" aria-label="Ziemia widziana z kosmosu i maly punkt na pustyni">
{_defs("zz")}
<defs><radialGradient id="niebozz" cx="50%" cy="34%" r="78%">
<stop offset="0%" stop-color="{C['d3']}"/><stop offset="100%" stop-color="{C['d1']}"/></radialGradient>
<radialGradient id="kulazz" cx="36%" cy="32%" r="72%">
<stop offset="0%" stop-color="{C['m2']}"/><stop offset="70%" stop-color="{C['m1']}"/>
<stop offset="100%" stop-color="{C['d2']}"/></radialGradient></defs>
<rect width="200" height="96" fill="url(#niebozz)"/>
{_wash(150, 26, 40, C['m2'], ".18", "zz")}
{_wash(40, 20, 34, C['fiolet'], ".22", "zz")}
{gw}
<g>
  <circle cx="136" cy="38" r="30" fill="{C['l1']}" opacity=".14"/>
  <circle cx="136" cy="38" r="25" fill="url(#kulazz)" stroke="{C['l1']}" stroke-width="1.2"/>
  <path d="M121 25c7-2 12 1 11 5-1 5-9 4-12 8-3 4 2 7 7 6 6-1 10 3 8 7"
        fill="none" stroke="{C['l2']}" stroke-width="2.4" stroke-linecap="round" opacity=".85"/>
  <path d="M145 29c6 0 9 3 8 7-1 4-7 4-8 8" fill="none" stroke="{C['l2']}"
        stroke-width="2.2" stroke-linecap="round" opacity=".7"/>
  <path d="M130 54c5 3 12 3 17-1" fill="none" stroke="{C['l2']}" stroke-width="2"
        stroke-linecap="round" opacity=".6"/>
  <ellipse cx="127" cy="29" rx="9" ry="5" fill="#FFFFFF" opacity=".22"/>
</g>
<path d="M0 76c22-9 40-4 58 1s38 7 56 1 52-6 86 4v14H0z" fill="{C['sand']}" opacity=".95"/>
<path d="M0 84c26-6 44 0 66 4s44 2 68-2 44-2 66 3v7H0z" fill="{C['gold2']}" opacity=".5"/>
{_postac_profil(40, 84, .78, C['m1'], C['wlosy'])}
<path d="M45 74c6 1 9 3 10 5" stroke="{C['szal']}" stroke-width="1.8" fill="none" stroke-linecap="round"/>
</svg>'''


def studnia_scena():
    """Studnia na pustyni: kamienny krag, kolowrot, dwie sylwetki pod gwiazdami."""
    gw = "".join(
        f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C["l2"]}" opacity=".8"/>'
        for x, y, r in [(16, 16, 1.1), (44, 8, .9), (70, 20, 1.2), (176, 14, 1.2),
                        (192, 40, .9), (150, 10, 1.0), (30, 38, .9), (110, 12, .9)])
    return f'''<svg viewBox="0 0 200 96" role="img" aria-label="Studnia na pustyni pod gwiazdami">
{_defs("sw")}
<defs><linearGradient id="niebosw" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="{C['d1']}"/><stop offset="1" stop-color="{C['d3']}"/></linearGradient></defs>
<rect width="200" height="96" fill="url(#niebosw)"/>
{_wash(150, 24, 38, C['fiolet'], ".26", "sw")}
{_wash(48, 30, 34, C['m2'], ".16", "sw")}
{gw}
<path d="M150 22a11 11 0 1 0 8 18 13 13 0 0 1-8-18z" fill="{C['gold2']}" opacity=".9"/>
<path d="M0 62c26-8 46-2 68 3s46 4 70-2 42-3 62 4v29H0z" fill="{C['sand']}" opacity=".92"/>
<path d="M0 74c30-7 50 0 74 4s48 1 66-3 42-1 60 4v17H0z" fill="{C['gold2']}" opacity=".45"/>
<g>
  <path d="M78 62h44l-4 26H82z" fill="{C['l1']}" stroke="{C['d1']}" stroke-width="1.3"/>
  <path d="M82 70h36M84 78h32" stroke="{C['d2']}" stroke-width=".9" opacity=".6"/>
  <ellipse cx="100" cy="62" rx="22" ry="5.4" fill="{C['d2']}" stroke="{C['d1']}" stroke-width="1.3"/>
  <ellipse cx="100" cy="62" rx="16" ry="3.4" fill="{C['d1']}"/>
  <path d="M82 60V42M118 60V42" stroke="{C['d2']}" stroke-width="2.4" stroke-linecap="round"/>
  <path d="M76 42h48l-24-13z" fill="{C['d3']}" stroke="{C['d1']}" stroke-width="1.2" stroke-linejoin="round"/>
  <path d="M86 47h28" stroke="{C['gold']}" stroke-width="2.2" stroke-linecap="round"/>
  <path d="M100 47v11" stroke="{C['l2']}" stroke-width="1.1"/>
  <path d="M96 58h8v5h-8z" fill="{C['gold']}" stroke="{C['d1']}" stroke-width="1"/>
</g>
{_postac_profil(44, 84, .95, C['m1'], C['wlosy'])}
{_postac_profil(150, 86, 1.15, C['d3'], C['wlosy2'])}
<path d="M49 74c6 1 9 3 10 5" stroke="{C['szal']}" stroke-width="1.8" fill="none" stroke-linecap="round"/>
</svg>'''


def gora_echo_scena():
    """Gora i echo: trzy grzbiety, sylwetka na szczycie, fale glosu."""
    fale = "".join(
        f'<path d="M{72 + i * 11} {24 - i * 5}a{9 + i * 5} {9 + i * 5} 0 0 1 0 {18 + i * 10}" '
        f'fill="none" stroke="{C["l3"]}" stroke-width="{3.0 - i * 0.5:.1f}" '
        f'stroke-linecap="round" opacity="{0.95 - i * 0.18:.2f}"/>' for i in range(3))
    return f'''<svg viewBox="0 0 200 96" role="img" aria-label="Chlopiec wola ze szczytu gory, echo wraca">
{_defs("ge")}
<defs><linearGradient id="nieboge" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="{C['l3']}"/><stop offset="1" stop-color="{C['l1']}"/></linearGradient></defs>
<rect width="200" height="96" fill="url(#nieboge)"/>
{_wash(40, 20, 36, C['gold2'], ".35", "ge")}
{_wash(168, 30, 40, C['m3'], ".28", "ge")}
<circle cx="44" cy="24" r="10" fill="{C['gold2']}" opacity=".85"/>
<path d="M120 96 168 34l46 62z" fill="{C['m3']}" opacity=".55"/>
<path d="M96 96 148 30l52 66z" fill="{C['m2']}" opacity=".7"/>
<path d="M-8 96 58 18l70 78z" fill="{C['m1']}" stroke="{C['d2']}" stroke-width="1.2"/>
<path d="M58 18 44 34c6 2 12 2 18 0l6 8c5-2 9-2 13 0z" fill="{C['l3']}" opacity=".9"/>
<path d="M148 30l-10 12c5 2 10 2 15 0z" fill="{C['l3']}" opacity=".75"/>
{fale}
{_postac_profil(58, 20, .62, C['d3'], C['wlosy'])}
<path d="M61 12c5 0 8 2 9 4" stroke="{C['szal']}" stroke-width="1.5" fill="none" stroke-linecap="round"/>
</svg>'''


def sklep_pigulki_scena():
    """Kupiec i pigulki na pragnienie: lada, sloje, zegar z zaoszczedzonym czasem."""
    sloje = "".join(
        f'<g><rect x="{18 + i * 26}" y="{26 - (i % 2) * 4}" width="18" height="22" rx="4" '
        f'fill="{[C["l2"], C["gold2"], C["rose2"], C["l1"]][i % 4]}" stroke="{C["d1"]}" stroke-width="1.1"/>'
        f'<rect x="{16 + i * 26}" y="{22 - (i % 2) * 4}" width="22" height="5" rx="2.4" '
        f'fill="{C["d3"]}"/></g>' for i in range(4))
    return f'''<svg viewBox="0 0 200 96" role="img" aria-label="Kupiec za lada ze slojami pigulek i zegar">
{_defs("sp")}
<rect width="200" height="96" fill="{C['l3']}"/>
{_wash(40, 26, 38, C['m3'], ".22", "sp")}
{_wash(166, 40, 36, C['gold'], ".22", "sp")}
<path d="M0 50h108v3H0z" fill="{C['d3']}"/>
{sloje}
<g>
  <circle cx="168" cy="30" r="15" fill="#FFFFFF" stroke="{C['d1']}" stroke-width="1.6"/>
  <path d="M168 30V20M168 30l7 5" stroke="{C['d1']}" stroke-width="1.8" stroke-linecap="round"/>
  <path d="M168 15v-4M183 30h4M168 45v4M153 30h-4" stroke="{C['d2']}" stroke-width="1.4" stroke-linecap="round"/>
</g>
{_postac_profil(120, 70, 1.35, C['d3'], C['wlosy2'])}
<path d="M0 70h200v26H0z" fill="{C['d2']}"/>
<path d="M0 68h200v4H0z" fill="{C['gold']}"/>
<path d="M0 82h200v2H0z" fill="{C['d1']}" opacity=".5"/>
<g>
  <rect x="26" y="74" width="30" height="12" rx="6" fill="#FFFFFF" stroke="{C['d1']}" stroke-width="1.2"/>
  <path d="M41 74v12" stroke="{C['d1']}" stroke-width="1.1"/>
  <path d="M26 80a6 6 0 0 1 6-6h9v12h-9a6 6 0 0 1-6-6z" fill="{C['gold2']}"/>
  <rect x="62" y="76" width="22" height="9" rx="4.5" fill="#FFFFFF" stroke="{C['d1']}" stroke-width="1.1"/>
  <path d="M62 80.5a4.5 4.5 0 0 1 4.5-4.5H73v9h-6.5a4.5 4.5 0 0 1-4.5-4.5z" fill="{C['rose2']}"/>
</g>
</svg>'''


# ---------- PLANSZA DO GRY ----------
def board():
    cols = 6
    x0, y0, w, h = 30, 46, 60, 44
    palette = [C['m3'], C['gold'], C['m1'], C['rose']]
    out, centers = [], []
    for i in range(30):
        r, c = divmod(i, cols)
        if r % 2 == 1:
            c = cols - 1 - c
        centers.append((x0 + c*w + w/2, y0 + r*h + h/2))
    path = "M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in centers)
    out.append(f'<path d="{path}" fill="none" stroke="{C["l1"]}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>')
    out.append(f'<path d="{path}" fill="none" stroke="{C["l2"]}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="1 12"/>')
    special = {7: "&#9888;", 14: "&#9208;", 21: "&#9829;", 25: "&#9748;", 30: "&#9733;"}
    for i, (cx, cy) in enumerate(centers):
        n = i + 1
        col = C['d1'] if n in special else palette[i % 4]
        out.append(f'<rect x="{cx-19:.0f}" y="{cy-15:.0f}" width="38" height="30" rx="9" fill="{col}" stroke="{C["d2"]}" stroke-width="1.8"/>')
        tc = C['d1'] if col in (C['m3'], C['gold'], C['rose']) else "#FFFFFF"
        dy = -1 if n in special else 4
        out.append(f'<text x="{cx:.0f}" y="{cy+dy:.0f}" text-anchor="middle" font-family="Verdana,sans-serif" font-size="12" font-weight="bold" fill="{tc}">{n}</text>')
        if n in special:
            out.append(f'<text x="{cx:.0f}" y="{cy+11:.0f}" text-anchor="middle" font-size="9" fill="{C["gold2"]}">{special[n]}</text>')
    leg, lx = "", 30
    for name, col in [("EMOCJE", C['m3']), ("WNIOSKI", C['gold']), ("OCENA", C['m1']),
                      ("CO MYŚLI?", C['rose']), ("POLE SPECJALNE", C["d1"])]:
        leg += f'<rect x="{lx}" y="280" width="14" height="12" rx="4" fill="{col}" stroke="{C["d2"]}" stroke-width="1.2"/>'
        leg += f'<text x="{lx+19}" y="290" font-family="Verdana,sans-serif" font-size="9" fill="{C["d2"]}">{name}</text>'
        lx += int(30 + len(name) * 6.0)
    return f"""<svg viewBox="0 0 420 316" role="img" aria-label="Plansza do gry: 30 pol ulozonych wezem w szesciu kolumnach i pieciu rzedach">
<rect width="420" height="316" rx="12" fill="{C['l3']}"/>
<text x="30" y="28" font-family="Verdana,sans-serif" font-size="13" font-weight="bold" fill="{C['d2']}">START &#8594;</text>
<text x="390" y="28" text-anchor="end" font-family="Verdana,sans-serif" font-size="13" font-weight="bold" fill="{C['gold']}">META &#9733;</text>
<path d="M30 34h360" stroke="{C['l1']}" stroke-width="2"/>
{"".join(out)}
<path d="M30 268h360" stroke="{C['l1']}" stroke-width="2"/>
{leg}
</svg>"""

# ---------- SCENA TEATRALNA ----------
def stage():
    return f'''<svg viewBox="0 0 420 220" role="img" aria-label="Scena teatralna z kurtyna i gwiazdami">
<rect width="420" height="220" rx="12" fill="{C['d1']}"/>
{stars(".5",.55,10,6)}
<path d="M0 0h420v34q-24 10-40 0T340 34 300 24 260 34 220 24 180 34 140 24 100 34 60 24 20 34 0 30z" fill="{C['d3']}"/>
<path d="M0 0h74q6 60-14 96T18 190 0 210z" fill="{C['m1']}"/>
<path d="M420 0h-74q-6 60 14 96t42 94 18 20z" fill="{C['m1']}"/>
<rect y="188" width="420" height="32" fill="{C['d2']}"/>
<ellipse cx="210" cy="188" rx="120" ry="14" fill="{C['gold2']}" opacity=".16"/>
<g transform="translate(210,120)">
<circle cx="0" cy="0" r="15" fill="{C['sand']}"/>
<path d="M-15 -1a15 15 0 0 1 30 0c0-11-6-17-15-17s-15 6-15 17z" fill="{C['gold2']}"/>
<path d="M0 16v34" stroke="{C['gold']}" stroke-width="12" stroke-linecap="round"/>
<path d="M-14 26l-16 12M14 26l16 12" stroke="{C['gold']}" stroke-width="7" stroke-linecap="round"/>
<path d="M-8 50l-6 30M8 50l6 30" stroke="{C['l2']}" stroke-width="7" stroke-linecap="round"/>
</g>
{_sparkle(96,64,9)}{_sparkle(330,52,7)}{_sparkle(60,120,5)}{_sparkle(362,124,6)}
</svg>'''

# ---------- LOGO PCTP ----------
LOGO = {
    "brzeg":   "#2A1A52",
    "obwodka": "#E7E2F3",
    "tlo1":    "#6B4B9E",
    "tlo2":    "#4A2D7C",
    "tlo3":    "#3A2263",
    "lawenda": "#A294D2",
    "brzoskw": "#F0A96C",
    "pomar":   "#E4703C",
    "zloto":   "#C9A22B",
    "tekst":   "#F7F2E9",
}

def logo_pctp(napis=True):
    L = LOGO
    platki = [
        # (cx, cy, rx, ry, obrot, kolor)
        (76, 62, 8.5, 15, -30, L["lawenda"]),
        (124, 62, 8.5, 15, 30, L["lawenda"]),
        (86, 51, 8.5, 17, -11, L["brzoskw"]),
        (114, 51, 8.5, 17, 11, L["brzoskw"]),
        (100, 46, 9, 18, 0, L["pomar"]),
    ]
    p = "".join(
        f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{col}" '
        f'transform="rotate({rot} {cx} {cy})"/>' for cx, cy, rx, ry, rot, col in platki)
    tekst = (f'<text x="100" y="146" text-anchor="middle" fill="{L["tekst"]}" '
             f'font-family="Georgia,\'Times New Roman\',serif" font-size="46" '
             f'font-weight="700" letter-spacing="1.5">PCTP</text>') if napis else ""
    return f'''<svg viewBox="0 0 200 200" role="img" aria-label="Logo Pomorskiego Centrum Terapii Pedagogicznej">
<defs><radialGradient id="pctpBg" cx="35%" cy="28%" r="78%">
<stop offset="0%" stop-color="{L['tlo1']}"/><stop offset="58%" stop-color="{L['tlo2']}"/>
<stop offset="100%" stop-color="{L['tlo3']}"/></radialGradient></defs>
<circle cx="100" cy="100" r="99" fill="{L['brzeg']}"/>
<circle cx="100" cy="100" r="94" fill="{L['obwodka']}"/>
<circle cx="100" cy="100" r="88" fill="url(#pctpBg)"/>
<g stroke="{L['zloto']}" stroke-width="3.4" fill="none" stroke-linecap="round">
<path d="M100 90V58"/>
<path d="M100 88q-10-10-14-24"/>
<path d="M100 88q10-10 14-24"/>
<path d="M100 90q-16-6-24-20"/>
<path d="M100 90q16-6 24-20"/>
</g>
{p}
<circle cx="100" cy="57" r="5.6" fill="#FFFFFF"/>
{tekst}
</svg>'''


def logo_symbol():
    """Jednorazowa definicja znaku PCTP; stopki odwolują się do niej przez <use>."""
    pelny = logo_pctp(napis=False)
    wnetrze = pelny.split(">", 1)[1].rsplit("</svg>", 1)[0]
    wnetrze = wnetrze.replace("pctpBg", "pctpMarkBg")
    return ('<svg width="0" height="0" aria-hidden="true" focusable="false" '
            'style="position:absolute">'
            f'<symbol id="pctp-mark" viewBox="0 0 200 200">{wnetrze}</symbol></svg>')

def logo_use(kl="mark"):
    return f'<svg class="{kl}" viewBox="0 0 200 200" aria-hidden="true"><use href="#pctp-mark"/></svg>'

# ---------- OKLADKA NEUTRALNA (domyslna dla nowej lektury) ----------
def cover_neutral():
    """Okladka niezwiazana z konkretna lektura: otwarta ksiazka, z ktorej wznosza sie gwiazdy.

    Uzywana, gdy `meta.okladka_svg` nie jest podane. Do konkretnej lektury warto napisac
    wlasny rysunek - ten ma byc poprawnym zapasem, nie docelowa okladka.
    """
    g = []
    for x, y, s in [(120, 96, 7), (168, 62, 9), (214, 44, 11), (262, 66, 8), (306, 100, 6),
                    (146, 138, 5), (286, 140, 5)]:
        g.append(_sparkle(x, y, s))
    return f'''<svg viewBox="0 0 420 300" preserveAspectRatio="xMidYMax slice" role="img" aria-label="Otwarta ksiazka, z ktorej wznosza sie gwiazdy">
{_defs("cn")}
<rect width="420" height="300" fill="url(#skycn)"/>
{stars()}
<circle cx="210" cy="250" r="150" fill="url(#glowcn)"/>
{"".join(g)}
<!-- ksiazka -->
<g transform="translate(210,236)">
<path d="M0 -18C-26 -44 -74 -50 -122 -42v112C-74 62 -26 68 0 90z" fill="{C['m1']}" stroke="{C['d1']}" stroke-width="3" stroke-linejoin="round"/>
<path d="M0 -18C26 -44 74 -50 122 -42v112C74 62 26 68 0 90z" fill="{C['m2']}" stroke="{C['d1']}" stroke-width="3" stroke-linejoin="round"/>
<g stroke="{C['l2']}" stroke-width="3" stroke-linecap="round" opacity=".55">
<path d="M-104 -22h64M-104 -4h70M-104 14h58M-104 32h66"/>
<path d="M40 -22h64M34 -4h70M46 14h58M38 32h66"/>
</g>
<path d="M0 -18v108" stroke="{C['d1']}" stroke-width="4"/>
<path d="M-128 70q128 24 256 0v10q-128 24-256 0z" fill="{C['d3']}"/>
</g>
</svg>'''

# ---------- KARTA PLANETY (zalaczniki do wyciecia) ----------
def karta_planety(ikona):
    """Gorna czesc karty do wyciecia: gwiazdziste niebo z planeta na srodku."""
    wnetrze = icon(ikona, 64)
    wnetrze = wnetrze.replace('<svg viewBox="0 0 64 64" width="64" height="64"',
                              '<svg x="58" y="6" width="84" height="84" viewBox="0 0 64 64"')
    gw = "".join(
        f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C["l2"]}" opacity=".75"/>'
        for x, y, r in [(20, 20, 1.5), (46, 10, 1.0), (170, 18, 1.4), (186, 48, 1.1),
                        (14, 58, 1.2), (178, 76, 1.3), (32, 82, 1.0), (152, 6, 1.0),
                        (10, 38, 1.0), (194, 32, 1.2)])
    return f'''<svg viewBox="0 0 200 96" role="img" aria-label="Planeta na gwiezdzistym niebie">
<defs><radialGradient id="kp{abs(hash(ikona))%9973}" cx="50%" cy="45%" r="62%">
<stop offset="0%" stop-color="{C['d3']}"/><stop offset="100%" stop-color="{C['d1']}"/>
</radialGradient></defs>
<rect width="200" height="96" fill="url(#kp{abs(hash(ikona))%9973})"/>
{gw}
<ellipse cx="100" cy="48" rx="46" ry="46" fill="{C['gold2']}" opacity=".10"/>
{wnetrze}
</svg>'''
