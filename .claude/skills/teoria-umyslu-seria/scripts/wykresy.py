#!/usr/bin/env python3
"""Generator wykresów SVG w stylu serii „Teoria umysłu".

Ręczne liczenie stroke-dasharray i pozycji etykiet na pierścieniu kończy się
przesuniętymi opisami — stąd ten skrypt. Wypisuje gotowy SVG na standardowe wyjście.

    python3 wykresy.py slupki "2;6=20,3;0=30,4;0=57,5;0=78" --prog 50
    python3 wykresy.py slupki "Rozwój typowy=85,Zespół Downa=86,Autyzm=20" --kolory tus,tuk,tue
    python3 wykresy.py pierscien "TUE=50,TUK=30,TUS=20" --srodek "100%" --pod "czasu zajęć"
    python3 wykresy.py skumulowany "Poziom I=70/20/10;Poziom II=50/30/20"

Paleta jest zwalidowana pod kątem kontrastu i daltonizmu — nie podmieniaj kolorów na oko.
"""
import argparse, sys

BARWY = {"tue": "#C4547A", "tuk": "#6553A8", "tus": "#0E8B78", "gold": "#A07A0A"}
INK, INK2, MUTED, SIATKA = "#2E2A3B", "#57516B", "#8B849D", "#F2ECE4"


def gora(x, y, w, h, r=4):
    """Prostokąt z zaokrąglonymi tylko górnymi rogami — słupek wyrasta z osi."""
    r = min(r, w / 2, h) if h > 0 else 0
    return (f"M{x} {y+h} L{x} {y+r} Q{x} {y} {x+r} {y} "
            f"L{x+w-r} {y} Q{x+w} {y} {x+w} {y+r} L{x+w} {y+h} Z")


def slupki(dane, prog=None, kolory=None):
    W, H, x0, x1, ybase, ytop = 470, 196, 44, 462, 152, 26
    sk = (ybase - ytop) / 100
    n = len(dane)
    krok = (x1 - x0) / n
    bw = krok - 14
    p = [f'<svg class="chart" viewBox="0 0 {W} {H}" role="img" aria-label="Wykres słupkowy">']
    for g in (0, 25, 50, 75, 100):
        y = ybase - g * sk
        p.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="{SIATKA}" stroke-width="1"/>')
        p.append(f'<text x="{x0-7}" y="{y+3:.1f}" text-anchor="end" font-size="8" fill="{MUTED}">{g}%</text>')
    if prog is not None:
        y = ybase - prog * sk
        p.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="{BARWY["gold"]}" stroke-width="1" stroke-dasharray="4 4"/>')
    for i, (lab, v) in enumerate(dane):
        x = x0 + i * krok + 7
        h = v * sk
        y = ybase - h
        col = kolory[i] if kolory else (BARWY["tuk"] if (prog and v < prog) else BARWY["tus"])
        p.append(f'<path d="{gora(x, y, bw, h)}" fill="{col}"/>')
        p.append(f'<text x="{x+bw/2:.1f}" y="{y-5:.1f}" text-anchor="middle" font-size="9.5" font-weight="800" fill="{INK}">{v}%</text>')
        for j, w in enumerate(lab.split("\n")):
            p.append(f'<text x="{x+bw/2:.1f}" y="{ybase+13+j*10}" text-anchor="middle" font-size="8.5" font-weight="700" fill="{INK2}">{w}</text>')
    p.append(f'<line x1="{x0}" y1="{ybase}" x2="{x1}" y2="{ybase}" stroke="{INK2}" stroke-width="1.5"/>')
    p.append("</svg>")
    return "\n".join(p)


def pierscien(dane, srodek="", pod="", kolory=None):
    import math
    cx, cy, r, szer = 88, 80, 54, 30
    obwod = 2 * math.pi * r
    p = [f'<svg class="chart" viewBox="0 0 210 172" role="img" aria-label="Wykres kołowy">',
         f'<g transform="translate({cx},{cy})">',
         f'<circle r="{r}" fill="none" stroke="{SIATKA}" stroke-width="{szer}"></circle>']
    suma = sum(v for _, v in dane) or 100
    biegnie = 0.0
    etykiety = []
    dom = kolory or [BARWY[k] for k in ("tue", "gold", "tuk", "tus")]
    for i, (lab, v) in enumerate(dane):
        frakcja = v / suma
        dlug = obwod * frakcja - 2          # 2 px przerwy między segmentami
        p.append(f'<circle r="{r}" fill="none" stroke="{dom[i % len(dom)]}" stroke-width="{szer}" '
                 f'stroke-dasharray="{dlug:.1f} {obwod-dlug:.1f}" stroke-dashoffset="{-obwod*biegnie:.1f}" '
                 f'transform="rotate(-90)"></circle>')
        srodkowa = biegnie + frakcja / 2
        kat = 2 * math.pi * srodkowa
        etykiety.append((cx + r * math.sin(kat), cy - r * math.cos(kat), v))
        biegnie += frakcja
    if srodek:
        p.append(f'<text y="-1" text-anchor="middle" font-family="Fraunces,serif" font-size="14" font-weight="800" fill="{INK}">{srodek}</text>')
    if pod:
        p.append(f'<text y="12" text-anchor="middle" font-size="7.2" fill="{MUTED}">{pod}</text>')
    p.append("</g>")
    p.append('<g font-size="9.5" font-weight="800" fill="#FFFFFF" text-anchor="middle">')
    for x, y, v in etykiety:
        p.append(f'<text x="{x:.1f}" y="{y+3.5:.1f}">{v}%</text>')
    p.append("</g></svg>")
    return "\n".join(p)


def skumulowany(wiersze, kolory=None):
    W, x0, x1, wys, odstep = 640, 104, 624, 30, 14
    dom = kolory or [BARWY[k] for k in ("tue", "tuk", "tus")]
    H = 16 + len(wiersze) * (wys + odstep)
    p = [f'<svg class="chart" viewBox="0 0 {W} {H}" role="img" aria-label="Wykres słupkowy skumulowany">']
    y = 16
    for nazwa, czesci in wiersze:
        p.append(f'<text x="{x0-10}" y="{y+wys/2+3.5}" text-anchor="end" font-size="10.5" font-weight="700" fill="{INK2}">{nazwa}</text>')
        x, total = x0, x1 - x0
        for i, v in enumerate(czesci):
            w = total * v / 100
            p.append(f'<rect x="{x}" y="{y}" width="{max(w-2,1):.1f}" height="{wys}" rx="5" fill="{dom[i % len(dom)]}"/>')
            if w > 44:
                p.append(f'<text x="{x+(w-2)/2:.1f}" y="{y+wys/2+3.5}" text-anchor="middle" font-size="10" font-weight="800" fill="#FFFFFF">{v}%</text>')
            x += w
        y += wys + odstep
    p.append("</svg>")
    return "\n".join(p)


def pary(tekst):
    out = []
    for kawalek in tekst.split(","):
        lab, _, v = kawalek.rpartition("=")
        out.append((lab.strip(), float(v) if "." in v else int(v)))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("typ", choices=["slupki", "pierscien", "skumulowany"])
    ap.add_argument("dane")
    ap.add_argument("--prog", type=float, default=None, help="linia odniesienia, np. 50")
    ap.add_argument("--srodek", default="", help="napis w środku pierścienia")
    ap.add_argument("--pod", default="", help="mniejszy napis pod środkiem")
    ap.add_argument("--kolory", default="", help="np. tus,tuk,tue")
    a = ap.parse_args()

    kolory = [BARWY[k.strip()] for k in a.kolory.split(",")] if a.kolory else None

    if a.typ == "slupki":
        print(slupki(pary(a.dane), a.prog, kolory))
    elif a.typ == "pierscien":
        print(pierscien(pary(a.dane), a.srodek, a.pod, kolory))
    else:
        wiersze = []
        for w in a.dane.split(";"):
            nazwa, _, wart = w.rpartition("=")
            wiersze.append((nazwa.strip(), [int(x) for x in wart.split("/")]))
        print(skumulowany(wiersze, kolory))


if __name__ == "__main__":
    main()
