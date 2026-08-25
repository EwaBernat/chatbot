#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kontrola składu przed oddaniem broszury.

Sprawdza trzy rzeczy, które psują druk i których nie widać w przeglądarce:
  1. czy HTML jest domknięty,
  2. czy któraś sekcja przekracza wysokość A4 (wtedy rozleje się na dwa arkusze),
  3. czy PDF ma dokładnie tyle stron, ile jest sekcji (czyli zero pustych stron).

    python sprawdz_sklad.py broszura.html
    python sprawdz_sklad.py broszura.html --pdf broszura.pdf
    python sprawdz_sklad.py broszura.html --dopasuj-linie linie.json

`--dopasuj-linie` mierzy wolne miejsce na stronach „część 3 z 3” i zapisuje liczbę
linii na notatki dla każdego rozdziału. Potem złóż broszurę ponownie z tym plikiem.
"""
import argparse, glob, json, os, re, shutil, subprocess, sys, tempfile
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source",
        "track", "wbr", "path", "circle", "rect", "ellipse", "line", "polygon", "polyline",
        "stop", "use", "text"}


def znajdz_chrome():
    for wzor in ("/opt/pw-browsers/chromium-*/chrome-linux/chrome",
                 "/opt/pw-browsers/chromium/chrome-linux/chrome"):
        t = sorted(glob.glob(wzor))
        if t:
            return t[-1]
    for nazwa in ("chromium", "chromium-browser", "google-chrome", "google-chrome-stable"):
        p = shutil.which(nazwa)
        if p:
            return p
    return None


def sprawdz_html(sciezka):
    s = open(sciezka, encoding="utf-8").read()
    stack, errs = [], []

    class P(HTMLParser):
        def handle_starttag(self, t, a):
            if t not in VOID:
                stack.append(t)

        def handle_endtag(self, t):
            if t in VOID:
                return
            if stack and stack[-1] == t:
                stack.pop()
            elif t in stack:
                i = len(stack) - 1 - stack[::-1].index(t)
                errs.append(f"niedopasowany </{t}>")
                del stack[i:]
            else:
                errs.append(f"osierocone </{t}>")

    P(convert_charrefs=True).feed(s)
    if stack:
        errs.append("niezamknięte: " + ", ".join(stack[:5]))
    return s.count('<section class="page'), errs


SONDA = """<style>.page{min-height:0 !important}.okladka{height:auto !important;padding:0 !important}</style>
<script>window.addEventListener('load',function(){
 var mm=document.createElement('div');mm.style.cssText='height:100mm;position:absolute';
 document.body.appendChild(mm);var px=mm.getBoundingClientRect().height/100;mm.remove();
 var out=[];document.querySelectorAll('%SEL%').forEach(function(p){
  out.push((p.id||'?')+':'+(p.getBoundingClientRect().height/px).toFixed(1));});
 document.body.innerHTML='<pre id=RES>'+out.join(' ')+'</pre>';});</script>"""


def zmierz(chrome, sciezka, selektor=".page"):
    s = open(sciezka, encoding="utf-8").read()
    tmp = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8",
                                      dir=os.path.dirname(os.path.abspath(sciezka)))
    tmp.write(s.replace("</body>", SONDA.replace("%SEL%", selektor) + "</body>"))
    tmp.close()
    try:
        r = subprocess.run([chrome, "--headless", "--no-sandbox", "--disable-gpu",
                            "--window-size=1400,1200", "--virtual-time-budget=10000",
                            "--dump-dom", "file://" + tmp.name],
                           capture_output=True, text=True, timeout=180)
        m = re.search(r'<pre id="RES">([^<]*)</pre>', r.stdout)
        if not m:
            return {}
        return {k: float(v) for k, v in (x.split(":") for x in m.group(1).split() if ":" in x)}
    finally:
        os.unlink(tmp.name)


def do_pdf(chrome, sciezka, pdf):
    subprocess.run([chrome, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    "--virtual-time-budget=30000", "--print-to-pdf=" + pdf,
                    "file://" + os.path.abspath(sciezka)],
                   capture_output=True, timeout=300)
    d = open(pdf, "rb").read()
    return d.count(b"/Type /Page") - d.count(b"/Type /Pages")


def main():
    ap = argparse.ArgumentParser(description="Kontrola składu broszury")
    ap.add_argument("html")
    ap.add_argument("--pdf", help="dodatkowo wygeneruj PDF pod tą ścieżką")
    ap.add_argument("--dopasuj-linie", dest="dopasuj",
                    help="zapisz tu liczbę linii na notatki dla każdego rozdziału")
    ap.add_argument("--limit", type=float, default=297.0, help="wysokość strony w mm (domyślnie A4)")
    a = ap.parse_args()

    sekcji, errs = sprawdz_html(a.html)
    print(f"Sekcji (stron A4): {sekcji}")
    print("HTML: " + ("OK" if not errs else "BŁĘDY -> " + "; ".join(errs[:4])))

    chrome = znajdz_chrome()
    if not chrome:
        print("Nie znalazłem Chromium — pomijam pomiar wysokości i PDF.")
        print("Zainstaluj Chromium albo sprawdź wydruk ręcznie: Ctrl+P → A4, marginesy brak.")
        sys.exit(1 if errs else 0)

    h = zmierz(chrome, a.html)
    za_wysokie = {k: v for k, v in h.items() if v > a.limit}
    if za_wysokie:
        print(f"\nZA WYSOKIE ({len(za_wysokie)}) — te sekcje rozleją się na dwa arkusze:")
        for k, v in sorted(za_wysokie.items(), key=lambda x: -x[1]):
            print(f"   {k:<18} {v:6.1f} mm   (nadmiar {v-a.limit:.1f} mm)")
        print("   Skróć treść, zmniejsz ilustrację albo przenieś blok na inną stronę.")
    else:
        print(f"Wysokość stron: OK — najwyższa {max(h.values()):.1f} mm z {a.limit:.0f} mm")

    if a.dopasuj:
        wys = zmierz(chrome, a.html, "section[id$=c]")
        linie = {}
        for ident, v in wys.items():
            m = re.match(r"r(\d+)c$", ident)
            if m:
                linie[m.group(1)] = max(4, min(16, 8 + int(max(0, 287.0 - v) // 7)))
        json.dump(linie, open(a.dopasuj, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"\nZapisano {a.dopasuj} — złóż broszurę ponownie z --linie {a.dopasuj}")

    if a.pdf:
        stron = do_pdf(chrome, a.html, a.pdf)
        ok = stron == sekcji
        print(f"\nPDF: {stron} stron / {sekcji} sekcji — " +
              ("OK, zero pustych stron" if ok else "NIEZGODNOŚĆ, są puste lub rozlane strony"))
        if not ok:
            print("   Najczęstsza przyczyna: sekcja przekracza 297 mm (patrz wyżej).")
        sys.exit(0 if (ok and not errs and not za_wysokie) else 1)
    sys.exit(1 if (errs or za_wysokie) else 0)


if __name__ == "__main__":
    main()
