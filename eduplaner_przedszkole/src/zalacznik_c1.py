# -*- coding: utf-8 -*-
"""Załącznik KC-3/C1-01 — historyjki obrazkowe do konspektu Warsztat historyjek (6 lat).
Trzy historyjki w gradacji: Poziom III (3 obrazki) → II (4) → I (5).
Rysunek wektorowy SVG, styl cukierkowy, do wydruku A4."""

PAL = dict(
    niebo="#DCEEFF", trawa="#BFE9C8", slonce="#FFD86B", slonce2="#FFB84D",
    donica="#F4A26B", donica2="#D9793F", ziemia="#8C6242", lodyga="#5FBF7A",
    lisc="#77D48C", platek="#FF9FC2", platek2="#FF7BAA", srodek="#FFE08A",
    konewka="#8FD3F4", konewka2="#5BB6E0", woda="#7FC7F0",
    kubek="#FFC7DE", ciasto="#F7C99B", mleko="#FFFFFF", jajko="#FFE9A8",
    miska="#C9B3F0", piek="#E7A6C8", serce="#FF8FB1",
    kot="#FFB784", kot2="#E8935C", pudlo="#D9A87A", pudlo2="#B5834F",
    kokarda="#FF7BAA", drzewo="#7AA86B", pien="#9A6B4A",
    skora="#FFDCC2", wlosy="#8C5A3C", wlosy2="#4A3728", ubranie="#8FB8F0",
    ubranie2="#F49BC1", kontur="#4A3B6B", biel="#FFFFFF",
)

def _postac(x, y, s=1.0, ubr=None, wlos=None, mina="usmiech"):
    """Prosta, cukierkowa postać dziecka."""
    ubr = ubr or PAL["ubranie"]; wlos = wlos or PAL["wlosy"]
    usta = {"usmiech": f'M {x-7*s} {y-30*s} q {7*s} {7*s} {14*s} 0',
            "smutek":  f'M {x-7*s} {y-25*s} q {7*s} {-7*s} {14*s} 0',
            "o":       f'M {x-4*s} {y-28*s} a {4*s} {4*s} 0 1 0 {8*s} 0 a {4*s} {4*s} 0 1 0 {-8*s} 0'}[mina]
    return f'''
  <g>
    <ellipse cx="{x}" cy="{y+34*s}" rx="{26*s}" ry="{7*s}" fill="#000" opacity=".08"/>
    <rect x="{x-18*s}" y="{y-8*s}" width="{36*s}" height="{40*s}" rx="{14*s}" fill="{ubr}"/>
    <rect x="{x-11*s}" y="{y+26*s}" width="{9*s}" height="{12*s}" rx="{4*s}" fill="{PAL['skora']}"/>
    <rect x="{x+2*s}" y="{y+26*s}" width="{9*s}" height="{12*s}" rx="{4*s}" fill="{PAL['skora']}"/>
    <circle cx="{x}" cy="{y-32*s}" r="{24*s}" fill="{PAL['skora']}"/>
    <path d="M {x-24*s} {y-36*s} a {24*s} {24*s} 0 0 1 {48*s} 0 q {-24*s} {-14*s} {-48*s} 0 z" fill="{wlos}"/>
    <circle cx="{x-9*s}" cy="{y-34*s}" r="{3.2*s}" fill="{PAL['kontur']}"/>
    <circle cx="{x+9*s}" cy="{y-34*s}" r="{3.2*s}" fill="{PAL['kontur']}"/>
    <circle cx="{x-16*s}" cy="{y-26*s}" r="{4.5*s}" fill="#FFB3C7" opacity=".65"/>
    <circle cx="{x+16*s}" cy="{y-26*s}" r="{4.5*s}" fill="#FFB3C7" opacity=".65"/>
    <path d="{usta}" stroke="{PAL['kontur']}" stroke-width="{2.4*s}" fill="none" stroke-linecap="round"/>
  </g>'''

def _tlo(w, h):
    return f'''
  <rect x="0" y="0" width="{w}" height="{h}" fill="{PAL['niebo']}"/>
  <circle cx="{w-46}" cy="40" r="24" fill="{PAL['slonce']}"/>
  <circle cx="{w-46}" cy="40" r="16" fill="{PAL['slonce2']}" opacity=".55"/>
  <path d="M 0 {h-46} q {w*0.25} -22 {w*0.5} 0 q {w*0.25} 22 {w*0.5} 0 L {w} {h} L 0 {h} z" fill="{PAL['trawa']}"/>'''

def _donica(x, y, s=1.0):
    return f'''
  <path d="M {x-30*s} {y} L {x+30*s} {y} L {x+22*s} {y+40*s} L {x-22*s} {y+40*s} z" fill="{PAL['donica']}"/>
  <rect x="{x-34*s}" y="{y-10*s}" width="{68*s}" height="{14*s}" rx="{6*s}" fill="{PAL['donica2']}"/>
  <ellipse cx="{x}" cy="{y-4*s}" rx="{28*s}" ry="{6*s}" fill="{PAL['ziemia']}"/>'''

def _serce(x, y, s=1.0):
    return (f'<path d="M {x} {y+9*s} C {x-16*s} {y-4*s} {x-9*s} {y-20*s} {x} {y-11*s} '
            f'C {x+9*s} {y-20*s} {x+16*s} {y-4*s} {x} {y+9*s} Z" fill="{PAL["serce"]}"/>')

def _kwiat(x, y, s=1.0, etap=3):
    """etap: 1 nasionko, 2 kiełek, 3 pełny kwiat"""
    if etap == 1:
        return f'<ellipse cx="{x}" cy="{y-2*s}" rx="{5*s}" ry="{4*s}" fill="{PAL["ziemia"]}"/>'
    if etap == 2:
        return f'''
  <path d="M {x} {y} L {x} {y-26*s}" stroke="{PAL['lodyga']}" stroke-width="{5*s}" stroke-linecap="round"/>
  <ellipse cx="{x-11*s}" cy="{y-22*s}" rx="{10*s}" ry="{6*s}" fill="{PAL['lisc']}" transform="rotate(-25 {x-11*s} {y-22*s})"/>'''
    platki = "".join(
        f'<ellipse cx="{x}" cy="{y-58*s}" rx="{9*s}" ry="{16*s}" fill="{PAL["platek"] if i%2==0 else PAL["platek2"]}" transform="rotate({i*60} {x} {y-58*s})"/>'
        for i in range(6))
    return f'''
  <path d="M {x} {y} L {x} {y-44*s}" stroke="{PAL['lodyga']}" stroke-width="{6*s}" stroke-linecap="round"/>
  <ellipse cx="{x-14*s}" cy="{y-28*s}" rx="{13*s}" ry="{7*s}" fill="{PAL['lisc']}" transform="rotate(-25 {x-14*s} {y-28*s})"/>
  <ellipse cx="{x+14*s}" cy="{y-20*s}" rx="{13*s}" ry="{7*s}" fill="{PAL['lisc']}" transform="rotate(25 {x+14*s} {y-20*s})"/>
  {platki}
  <circle cx="{x}" cy="{y-58*s}" r="{10*s}" fill="{PAL['srodek']}"/>'''

def _konewka(x, y, s=1.0, leje=True):
    woda = f'''
  <path d="M {x-42*s} {y+4*s} q {-10*s} {16*s} {-4*s} {30*s}" stroke="{PAL['woda']}" stroke-width="{4*s}" fill="none" stroke-linecap="round" opacity=".85"/>
  <circle cx="{x-50*s}" cy="{y+40*s}" r="{3*s}" fill="{PAL['woda']}"/>
  <circle cx="{x-44*s}" cy="{y+30*s}" r="{2.4*s}" fill="{PAL['woda']}"/>''' if leje else ""
    return f'''
  <rect x="{x-18*s}" y="{y-14*s}" width="{40*s}" height="{34*s}" rx="{8*s}" fill="{PAL['konewka']}"/>
  <path d="M {x-18*s} {y-6*s} L {x-44*s} {y+4*s} L {x-40*s} {y+10*s} L {x-16*s} {y+2*s} z" fill="{PAL['konewka2']}"/>
  <path d="M {x+4*s} {y-14*s} q {18*s} {2*s} {14*s} {22*s}" stroke="{PAL['konewka2']}" stroke-width="{5*s}" fill="none" stroke-linecap="round"/>
  {woda}'''

# ---------------------------------------------------------------- historyjki
def historyjka_p3():
    """Poziom III — 3 obrazki: sadzę · podlewam · wyrósł kwiat."""
    W, H = 300, 240
    o1 = _tlo(W,H) + _donica(150,130) + _kwiat(150,126,1,1) + _postac(60,120,.72,PAL["ubranie2"],PAL["wlosy"]) + \
         f'<circle cx="88" cy="96" r="6" fill="{PAL["ziemia"]}"/>'
    o2 = _tlo(W,H) + _donica(150,130) + _kwiat(150,126,1,2) + _postac(62,118,.72,PAL["ubranie2"],PAL["wlosy"]) + _konewka(112,104,.8,True)
    o3 = _tlo(W,H) + _donica(150,142) + _kwiat(150,138,1,3) + _postac(58,120,.72,PAL["ubranie2"],PAL["wlosy"]) + \
         _serce(228, 80, 1.15)
    return [("Zasadziłam nasionko", o1), ("Podlewam codziennie", o2), ("Wyrósł piękny kwiat", o3)]

def historyjka_p2():
    """Poziom II — 4 obrazki: nasionko · kiełek · podlewanie · kwiat i radość."""
    W, H = 300, 240
    o1 = _tlo(W,H) + _donica(150,132) + _kwiat(150,128,1,1) + _postac(60,120,.7,PAL["ubranie"],PAL["wlosy2"])
    o2 = _tlo(W,H) + _donica(150,132) + _kwiat(150,128,1,2) + _postac(60,120,.7,PAL["ubranie"],PAL["wlosy2"])
    o3 = _tlo(W,H) + _donica(150,132) + _kwiat(150,128,1,2) + _postac(62,118,.7,PAL["ubranie"],PAL["wlosy2"]) + _konewka(112,102,.78,True)
    o4 = _tlo(W,H) + _donica(150,146) + _kwiat(150,142,1,3) + _postac(56,122,.7,PAL["ubranie"],PAL["wlosy2"],"o") + \
         _serce(228, 82, 1.15)
    return [("Mam nasionko", o1), ("Wykiełkował zielony pęd", o2),
            ("Podlewam roślinkę", o3), ("Zakwitł kwiat — cieszę się", o4)]

def historyjka_p1():
    """Poziom I — 5 obrazków: pełna sekwencja z problemem i rozwiązaniem."""
    W, H = 300, 240
    o1 = _tlo(W,H) + _donica(150,132) + _kwiat(150,128,1,1) + _postac(60,120,.7,PAL["ubranie2"],PAL["wlosy"])
    o2 = _tlo(W,H) + _donica(150,132) + _kwiat(150,128,1,2) + _postac(60,120,.7,PAL["ubranie2"],PAL["wlosy"])
    # obrazek 3: zapomniane podlewanie — zwiędnięty pęd, smutna mina
    o3 = _tlo(W,H) + _donica(150,132) + f'''
  <path d="M 150 128 q 2 -18 -14 -24" stroke="#A8B88A" stroke-width="5" fill="none" stroke-linecap="round"/>
  <ellipse cx="130" cy="108" rx="12" ry="6" fill="#A8B88A" transform="rotate(55 130 108)"/>
  <ellipse cx="143" cy="118" rx="10" ry="5" fill="#A8B88A" transform="rotate(70 143 118)"/>
  <g opacity=".8">
    <circle cx="214" cy="82" r="17" fill="#FFF" stroke="{PAL['konewka2']}" stroke-width="3"/>
    <path d="M 214 74 q 6 8 0 12 q -6 -4 0 -12 z" fill="{PAL['woda']}"/>
    <path d="M 203 71 L 225 93" stroke="{PAL['p3lin'] if 'p3lin' in PAL else '#D9534F'}" stroke-width="3.5" stroke-linecap="round"/>
  </g>''' + \
         _postac(60,120,.7,PAL["ubranie2"],PAL["wlosy"],"smutek")
    o4 = _tlo(W,H) + _donica(150,132) + _kwiat(150,128,1,2) + _postac(62,118,.7,PAL["ubranie2"],PAL["wlosy"]) + _konewka(112,102,.78,True)
    o5 = _tlo(W,H) + _donica(150,146) + _kwiat(150,142,1,3) + _postac(56,122,.7,PAL["ubranie2"],PAL["wlosy"],"o") + \
         _serce(228, 82, 1.15)
    return [("Sadzę nasionko w doniczce", o1), ("Wyrasta mały pęd", o2),
            ("Zapomniałam podlać — roślinka zwiędła", o3),
            ("Podlewam ją i stawiam w słońcu", o4),
            ("Roślinka odżyła i zakwitła", o5)]

# ---------------------------------------------------------------- karty A4
def karta_a4(poziom, kod_poziomu, obrazki, nr_zal):
    """Jedna strona A4 z historyjką do wycięcia (styl cukierkowy, marka EduPlaner)."""
    n = len(obrazki)
    kol = 2 if n <= 4 else 3
    kafle = []
    for i, (podpis, svg) in enumerate(obrazki, 1):
        kafle.append(f'''      <figure class="kafel">
        <span class="numer">{i}</span>
        <svg viewBox="0 0 300 240" role="img" aria-label="{podpis}">{svg}
        </svg>
        <figcaption>{podpis}</figcaption>
        <span class="linia-ciecia" aria-hidden="true"></span>
      </figure>''')
    return f'''<section class="zal" data-poziom="{kod_poziomu}">
  <header class="zal-head">
    <span class="mark" role="img" aria-label="Logo PCTP"></span>
    <div>
      <div class="zal-w">EduPlaner 2026</div>
      <div class="zal-s">Załącznik {nr_zal} · konspekt C1-01 · Warsztat historyjek · 6 lat</div>
    </div>
    <span class="zal-pill {kod_poziomu}">{poziom} · {n} obrazki</span>
  </header>
  <div class="zal-tytul">
    <span class="zal-kp">Pomoc dydaktyczna · historyjka obrazkowa</span>
    <h3>Jak rośnie kwiatek</h3>
    <p>Wytnij obrazki wzdłuż linii, rozsyp je na dywanie i poproś dziecko o ułożenie kolejności.
    Podpisy zostaw przy obrazkach albo odetnij — zależnie od tego, czy dziecko już czyta.</p>
  </div>
  <div class="zal-siatka k{kol}">
{chr(10).join(kafle)}
  </div>
  <div class="zal-stopka">
    <span><b>Polecenie dla dziecka:</b> „Ułóż obrazki po kolei i opowiedz, co się wydarzyło.”</span>
    <span class="mono">EduPlaner 2026 · PCTP · druk KC-3 · załącznik {nr_zal}</span>
  </div>
</section>'''

def zalaczniki_c1():
    return (karta_a4("Poziom III", "p3", historyjka_p3(), "Z1") +
            karta_a4("Poziom II", "p2", historyjka_p2(), "Z2") +
            karta_a4("Poziom I", "p1", historyjka_p1(), "Z3"))
