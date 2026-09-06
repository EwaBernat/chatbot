#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pobiera kroje z Google Fonts i zapisuje je jako arkusz z osadzonymi plikami.

Po co: broszura jest jednym plikiem HTML, a PDF powstaje w przeglądarce bez
dostępu do sieci. Kiedy kroje wiszą pod adresem `fonts.googleapis.com`,
w druku podstawiają się zastępniki — DejaVu Sans zamiast Lato — i cały tekst
wygląda na zbyt gruby. Osadzone `@font-face` usuwają ten problem i przy okazji
kasują jedyne odwołanie broszury na zewnątrz.

    python pobierz_kroje.py --out assets/kroje.css

Zostawiamy tylko zakresy `latin` i `latin-ext` — ten drugi niesie polskie znaki.
"""
import argparse
import base64
import re
import urllib.request

# Chrome w nagłówku, bo Google Fonts odsyła woff2 tylko nowym przeglądarkom.
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/120.0.0.0 Safari/537.36")
ZAKRESY = ("latin", "latin-ext")
DOMYSLNE = ("Poppins:ital,wght@0,400;0,600;0,700;1,600",
            "Lato:ital,wght@0,400;0,700;1,400")


def pobierz(url):
    zad = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(zad, timeout=60) as odp:
        return odp.read()


def arkusz(rodziny):
    url = "https://fonts.googleapis.com/css2?" + "&".join(f"family={r}" for r in rodziny)
    return pobierz(url + "&display=swap").decode("utf-8")


def osadz(css):
    """Zamienia adresy plików na `data:` i wycina zakresy, których nie używamy."""
    bloki, zostawione, pominiete = re.split(r"(?=/\*\s*[a-z-]+\s*\*/)", css), [], 0
    for blok in bloki:
        m = re.match(r"/\*\s*([a-z-]+)\s*\*/", blok.strip())
        if not m:
            continue
        if m.group(1) not in ZAKRESY:
            pominiete += 1
            continue
        for adres in re.findall(r"url\((https://[^)]+\.woff2)\)", blok):
            dane = base64.b64encode(pobierz(adres)).decode("ascii")
            blok = blok.replace(adres, f"data:font/woff2;base64,{dane}")
        zostawione.append(blok.strip())
    return "\n".join(zostawione), len(zostawione), pominiete


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    ap.add_argument("--rodzina", action="append", default=None,
                    help="np. 'Lato:wght@400;700'; można podać wiele razy")
    a = ap.parse_args()

    css, ile, bez = osadz(arkusz(a.rodzina or list(DOMYSLNE)))
    naglowek = ("/* Kroje osadzone w pliku — patrz scripts/pobierz_kroje.py.\n"
                "   Bez tego PDF drukuje się zastępnikami i tekst wygląda na pogrubiony. */\n")
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(naglowek + css + "\n")
    kb = round(len(css.encode()) / 1024)
    print(f"Zapisano {a.out} — {ile} krojów ({kb} KB), pominięto {bez} zakresów")


if __name__ == "__main__":
    main()
