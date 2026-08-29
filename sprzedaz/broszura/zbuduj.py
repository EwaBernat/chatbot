#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Buduje broszurę sprzedażową „Kolorowy Świat Emocji".

Ze źródła `broszura.src.html` (czytelnego, z krótkimi znacznikami zamiast
grafik) robi dwa pliki:

  Broszura-Kolorowy-Swiat-Emocji.html  — kompletny dokument do otwarcia
                                          i wydrukowania (Ctrl+P → A4)
  broszura-artifact.html                — ten sam materiał bez <html>/<body>,
                                          do publikacji jako Artifact

Wszystko jest wklejone w środek: zdjęcia jako data:URI, kroje pisma jako
base64. Plik działa bez internetu i bez katalogu z grafikami.

Uruchomienie:   python3 zbuduj.py
"""

import base64
import pathlib
import re
import sys

KATALOG = pathlib.Path(__file__).resolve().parent
ZRODLO = KATALOG / "broszura.src.html"
GRAFIKI = KATALOG / "grafiki"
KROJE = KATALOG / "fonts.css"

WYNIK_PELNY = KATALOG / "Broszura-Kolorowy-Swiat-Emocji.html"
WYNIK_ARTIFACT = KATALOG / "broszura-artifact.html"

SZKIELET = """<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Broszura sprzedażowa zeszytu „Kolorowy Świat Emocji” — pięć stref koloru, osiem kącików rozdziału i dostosowania dla piętnastu grup uczniów. PCTP Koszalin.">
<meta name="author" content="Mirosława Ewa Jurczyszyn">
<style>*{{box-sizing:border-box}}html,body{{margin:0}}img{{max-width:100%}}</style>
{tresc}
</body>
</html>
"""


def wstaw_grafike(dopasowanie):
    nazwa, _, opis = dopasowanie.group(1).partition("|")
    plik = GRAFIKI / f"{nazwa}.jpg"
    if not plik.exists():
        sys.exit(f"Brak grafiki: {plik}")
    dane = base64.b64encode(plik.read_bytes()).decode()
    alt = (opis or nazwa).replace('"', "&quot;")
    return f'<img src="data:image/jpeg;base64,{dane}" alt="{alt}" loading="lazy">'


def main():
    if not ZRODLO.exists():
        sys.exit(f"Brak źródła: {ZRODLO}")

    tresc = ZRODLO.read_text(encoding="utf-8")
    tresc = tresc.replace("{{FONTS}}", KROJE.read_text(encoding="utf-8"))

    tresc, ile = re.subn(r"\{\{IMG:([^}]+)\}\}", wstaw_grafike, tresc)

    WYNIK_ARTIFACT.write_text(tresc, encoding="utf-8")
    WYNIK_PELNY.write_text(SZKIELET.format(tresc=tresc), encoding="utf-8")

    stron = tresc.count('<section class="page')
    print(f"Wklejono grafik: {ile}")
    print(f"Stron A4:        {stron}")
    for p in (WYNIK_PELNY, WYNIK_ARTIFACT):
        print(f"{p.name:38s} {p.stat().st_size / 1_048_576:5.2f} MB")


if __name__ == "__main__":
    main()
