#!/usr/bin/env python3
"""Wstawia osadzone fonty Mulish do szablonu i tworzy wersję offline do druku.

Użycie:  python3 narzedzia/osadz-fonty.py
Wejście: szablon-broszury-A4.html + narzedzia/mulish-osadzony.css
Wyjście: szablon-broszury-A4-druk.html  (samodzielny plik, działa bez internetu)
"""
import pathlib

katalog = pathlib.Path(__file__).resolve().parent.parent
fonty = (katalog / 'narzedzia' / 'mulish-osadzony.css').read_text(encoding='utf-8')
html = (katalog / 'szablon-broszury-A4.html').read_text(encoding='utf-8')

start = html.index('<link rel="preconnect"')
koniec = html.index('<style>')
wynik = (
    html[:start]
    + '<!-- Mulish osadzony w pliku (latin + latin-ext) — działa bez internetu -->\n'
    + '<style>\n' + fonty + '\n</style>\n'
    + html[koniec:]
).replace(
    '<title>Szablon broszury A4 — wzór</title>',
    '<title>Szablon broszury A4 — wersja do druku (fonty osadzone)</title>', 1)

(katalog / 'szablon-broszury-A4-druk.html').write_text(wynik, encoding='utf-8')
print('Zapisano: szablon-broszury-A4-druk.html')
