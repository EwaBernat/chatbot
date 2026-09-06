#!/usr/bin/env python3
"""Buduje dwa samodzielne pliki na stronę WWW z pliku źródłowego index.html.

    python3 plan-szkolenia/build.py

Powstają:
    plan-szkolenia/przedszkole.html   — plan + warsztat, tylko ścieżka przedszkolna
    plan-szkolenia/szkola.html        — plan + warsztat, tylko ścieżka szkolna

Każdy plik jest samodzielny: bez przełącznika ścieżek, bez treści drugiej ścieżki,
z własnym tytułem. Jedyne zasoby zewnętrzne to kroje pisma z Google Fonts.
"""

import pathlib
import re

HERE = pathlib.Path(__file__).parent
SRC = HERE / 'index.html'

WARIANTY = {
    'przedszkole.html': {
        'track': 'p',
        'usun': ['TRACK-S', 'DATA-S'],
        'title': 'Plan szkolenia EduPlaner 2026 — przedszkole',
        'podpis': 'PCTP · plan szkolenia rady pedagogicznej · przedszkole',
        'hash_plan': '#plan',
        'hash_warsztat': '#warsztat',
    },
    'szkola.html': {
        'track': 's',
        'usun': ['TRACK-P', 'DATA-P'],
        'title': 'Plan szkolenia EduPlaner 2026 — szkoła podstawowa',
        'podpis': 'PCTP · plan szkolenia rady pedagogicznej · szkoła podstawowa',
        'hash_plan': '#plan',
        'hash_warsztat': '#warsztat',
    },
}


def wytnij(tekst, nazwa):
    """Usuwa blok między znacznikami NAZWA-START i NAZWA-END (HTML albo JS)."""
    for start, end in (('<!--%s-START-->', '<!--%s-END-->'), ('/*%s-START*/', '/*%s-END*/')):
        a, b = start % nazwa, end % nazwa
        while a in tekst and b in tekst:
            i, j = tekst.index(a), tekst.index(b) + len(b)
            tekst = tekst[:i] + tekst[j:]
    return tekst


GLOWA = """<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  :root { color-scheme: light dark; }
  html, body { margin: 0; }
  img { max-width: 100%%; }
  [hidden] { display: none !important; }
</style>
%s</head>
<body>
"""

STOPA = "\n</body>\n</html>\n"


def zbuduj(zrodlo, cfg):
    out = zrodlo
    for nazwa in cfg['usun']:
        out = wytnij(out, nazwa)

    # przełącznik ścieżek jest zbędny w pliku jednościeżkowym
    out = wytnij(out, 'SWITCH')

    # tytuł strony i podpis w pasku górnym
    out = re.sub(r'<title>.*?</title>', '<title>%s</title>' % cfg['title'], out, count=1)
    out = out.replace('<span>PCTP · plan szkolenia rady pedagogicznej</span>',
                      '<span>%s</span>' % cfg['podpis'])

    # ścieżka ustawiona na sztywno + proste kotwice #plan / #warsztat
    out = out.replace("var state = { track: 'p', view: 'plan' };",
                      "var state = { track: '%s', view: 'plan' };" % cfg['track'])
    out = out.replace(
        """    var h = location.hash.replace('#', '');
    if (h === 'szkola') { state.track = 's'; state.view = 'plan'; }
    else if (h === 'warsztat-szkola') { state.track = 's'; state.view = 'warsztat'; }
    else if (h === 'warsztat-przedszkole' || h === 'warsztat') { state.view = 'warsztat'; }""",
        """    var h = location.hash.replace('#', '');
    if (h.indexOf('warsztat') === 0) { state.view = 'warsztat'; }
    else if (h === 'plan') { state.view = 'plan'; }""")
    out = out.replace(
        """    if (state.view === 'warsztat') { return state.track === 's' ? '#warsztat-szkola' : '#warsztat-przedszkole'; }
    return state.track === 's' ? '#szkola' : '#przedszkole';""",
        """    return state.view === 'warsztat' ? '#warsztat' : '#plan';""")

    # osobny klucz pamięci na ścieżkę — odpowiedzi z jednego pliku nie mieszają się z drugim
    out = out.replace("var STORE = 'eduplaner-warsztat-v1';",
                      "var STORE = 'eduplaner-warsztat-%s-v1';" % cfg['track'])

    # samodzielny dokument: <head> z deklaracją kodowania i podstawowym resetem.
    # Bez <meta charset> polskie znaki rozsypują się na serwerach bez nagłówka HTTP.
    znacznik = '<div class="topbar">'
    czolo, reszta = out.split(znacznik, 1)
    return GLOWA % czolo + znacznik + reszta + STOPA


def main():
    zrodlo = SRC.read_text(encoding='utf-8')
    for nazwa, cfg in WARIANTY.items():
        wynik = zbuduj(zrodlo, cfg)
        for slad in ('TRACK-P', 'TRACK-S', 'DATA-P', 'DATA-S', 'SWITCH'):
            wynik = wynik.replace('<!--%s-START-->' % slad, '').replace('<!--%s-END-->' % slad, '')
            wynik = wynik.replace('/*%s-START*/' % slad, '').replace('/*%s-END*/' % slad, '')
        (HERE / nazwa).write_text(wynik, encoding='utf-8')
        print('%-20s %6.1f kB' % (nazwa, len(wynik.encode('utf-8')) / 1024))


if __name__ == '__main__':
    main()
