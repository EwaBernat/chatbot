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
}

def _defs(uid):
    return f'''<defs>
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
    return f'''<svg viewBox="0 0 420 300" preserveAspectRatio="xMidYMax slice" role="img" aria-label="Maly Ksiaze na swojej planecie z roza pod kloszem, gwiazdziste niebo">
{_defs("cv")}
<rect width="420" height="300" fill="url(#skycv)"/>
{stars()}
{_sparkle(352,58,7)}{_sparkle(58,84,5)}{_sparkle(300,26,4)}
<circle cx="210" cy="252" r="150" fill="url(#glowcv)"/>
<!-- planeta -->
<circle cx="210" cy="268" r="96" fill="url(#plcv)"/>
<path d="M124 244a96 96 0 0 1 172 0 96 96 0 0 0-172 0Z" fill="{C['m3']}" opacity=".35"/>
<ellipse cx="156" cy="290" rx="22" ry="10" fill="{C['d3']}" opacity=".4"/>
<ellipse cx="256" cy="300" rx="16" ry="8" fill="{C['d3']}" opacity=".35"/>
<!-- wulkany -->
<path d="M120 262l15-21 15 21z" fill="{C['d2']}"/><path d="M128 244q7-11 14 0z" fill="{C['gold']}" opacity=".75"/>
<path d="M286 276l12-16 12 16z" fill="{C['d2']}"/>
<!-- roza pod kloszem -->
<g transform="translate(268,196)">
<path d="M0 46V22" stroke="{C['d2']}" stroke-width="3" stroke-linecap="round"/>
<path d="M0 34c-9-2-13-8-13-8s9-3 13 3z" fill="{C['m1']}"/>
<circle cx="0" cy="16" r="9" fill="{C['rose']}"/><circle cx="0" cy="16" r="4.5" fill="{C['rose2']}"/>
<path d="M-17 46a17 30 0 0 1 34 0z" fill="{C['l1']}" opacity=".28"/>
<path d="M-17 46a17 30 0 0 1 34 0" fill="none" stroke="{C['l2']}" stroke-width="1.6" opacity=".8"/>
<rect x="-19" y="45" width="38" height="4" rx="2" fill="{C['l2']}" opacity=".8"/>
</g>
<!-- maly ksiaze -->
<g transform="translate(178,140)">
<!-- szal -->
<path d="M4 54q-26 2-40 22" stroke="{C['l2']}" stroke-width="7" fill="none" stroke-linecap="round" opacity=".92"/>
<!-- plaszcz -->
<path d="M4 48c-17 0-29 14-31 34h62c-2-20-14-34-31-34z" fill="{C['gold']}" stroke="{C['d2']}" stroke-width="1.6" stroke-linejoin="round"/>
<path d="M4 48v34" stroke="{C['d2']}" stroke-width="1.4" opacity=".5"/>
<!-- rece -->
<path d="M-22 60q-14 6-18 20M30 60q14 6 18 20" stroke="{C['gold2']}" stroke-width="7" fill="none" stroke-linecap="round"/>
<!-- nogi -->
<path d="M-6 82v16M14 82v16" stroke="{C['l2']}" stroke-width="6" stroke-linecap="round"/>
<path d="M-10 98h8M10 98h8" stroke="{C['d2']}" stroke-width="5" stroke-linecap="round"/>
<!-- kolnierz -->
<rect x="-4" y="42" width="16" height="10" rx="4" fill="{C['l2']}"/>
<!-- glowa -->
<circle cx="4" cy="26" r="20" fill="{C['sand']}"/>
<path d="M-16 22a20 20 0 0 1 40 0c0-15-9-24-20-24s-20 9-20 24z" fill="{C['gold2']}"/>
<path d="M-18 21q22-13 44 0" stroke="{C['gold']}" stroke-width="3" fill="none" stroke-linecap="round"/>
<circle cx="-3" cy="27" r="2.2" fill="{C['ink']}"/><circle cx="11" cy="27" r="2.2" fill="{C['ink']}"/>
<path d="M-1 35q5 4 10 0" stroke="{C['ink']}" stroke-width="1.8" fill="none" stroke-linecap="round"/>
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
def thermometer():
    rows = [("5","BARDZO MOCNO","#B23A48"),("4","MOCNO","#D97A45"),("3","ŚREDNIO",C['gold']),
            ("2","TROCHĘ",C['m2']),("1","LEDWO CZUJĘ",C['m3'])]
    out=[]
    for i,(n,t,c) in enumerate(rows):
        y=24+i*50
        out.append(f'<rect x="96" y="{y}" width="290" height="42" rx="8" fill="{c}"/>')
        out.append(f'<text x="112" y="{y+28}" font-family="Verdana,sans-serif" font-size="17" font-weight="bold" fill="#fff">{n}</text>')
        out.append(f'<text x="140" y="{y+27}" font-family="Verdana,sans-serif" font-size="14" fill="#fff">{t}</text>')
    return f'''<svg viewBox="0 0 420 300" role="img" aria-label="Termometr emocji od 1 do 5">
<rect width="420" height="300" rx="12" fill="{C['l3']}"/>
{"".join(out)}
<rect x="46" y="24" width="30" height="242" rx="15" fill="{C['l2']}" stroke="{C['d3']}" stroke-width="2.5"/>
<rect x="52" y="120" width="18" height="140" rx="9" fill="#B23A48"/>
<circle cx="61" cy="264" r="22" fill="#B23A48" stroke="{C['d3']}" stroke-width="2.5"/>
</svg>'''

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
