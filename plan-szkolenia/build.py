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
        'wariant': 'A',
        'marka': True,
        'usun': ['TRACK-S', 'DATA-S'],
        'title': 'Plan szkolenia EduPlaner 2026 — przedszkole',
        'podpis': 'PCTP · plan szkolenia rady pedagogicznej · przedszkole',
        'hash_plan': '#plan',
        'hash_warsztat': '#warsztat',
    },
    'szkola.html': {
        'track': 's',
        'wariant': 'A',
        'marka': True,
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



# Paleta z logo PCTP (lawenda): fiolet pola #55377D, obręcz #E7DAF3,
# pomarańcz płatków #EA7A35, lawenda płatków #9B7BC3, złoto łodyg #CBA242.
# Pomarańcz w tekście przyciemniony do #C0561A, żeby trzymał kontrast na bieli.
PALETA_PCTP = """
<style>
:root{
  --paper:#F7F4FB; --surface:#FFFFFF; --surface-2:#F0EAF8;
  --ink:#241A38; --ink-2:#4C4166; --muted:#71678C;
  --line:#E0D6EF; --line-soft:#EDE7F6;
  --brand:#55377D; --brand-soft:#EDE5F7;
  --accent:#C0561A; --accent-soft:#FBEADD;
  --good:#2A6B4F; --bad:#A8261A; --on-track:#FFFFFF;
  --shadow:0 1px 2px rgba(36,26,56,.06);
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --paper:#17122B; --surface:#201936; --surface-2:#291F44;
    --ink:#F2EEF9; --ink-2:#CCC3E0; --muted:#9A90B6;
    --line:#362A56; --line-soft:#2C2249;
    --brand:#B79AE6; --brand-soft:#2A2048;
    --accent:#F09355; --accent-soft:#362320;
    --good:#5CC79C; --bad:#FF9A8F; --on-track:#1A1330;
    --shadow:0 1px 2px rgba(0,0,0,.35);
  }
}
:root[data-theme="dark"]{
  --paper:#17122B; --surface:#201936; --surface-2:#291F44;
  --ink:#F2EEF9; --ink-2:#CCC3E0; --muted:#9A90B6;
  --line:#362A56; --line-soft:#2C2249;
  --brand:#B79AE6; --brand-soft:#2A2048;
  --accent:#F09355; --accent-soft:#362320;
  --good:#5CC79C; --bad:#FF9A8F; --on-track:#1A1330;
  --shadow:0 1px 2px rgba(0,0,0,.35);
}
.mark .logo{
  width:34px;height:34px;border-radius:50%;display:block;flex:none;
  box-shadow:0 0 0 1px var(--line);
}
.mark{gap:12px;align-items:center}
.hero .rule{background:linear-gradient(90deg,var(--track) 0 60%,#CBA242 60% 100%)}
</style>
"""

LOGO_IMG = '<img class="logo" alt="PCTP" src="data:image/webp;base64,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">'

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

    if cfg.get('wariant') == 'A':
        # Wariant A to sama projekcja: bez modułu warsztatowego, bez wariantów B i C.
        # Zostaje czysty HTML — żadnego skryptu, nic się nie zepsuje na serwerze.
        for blok in ('WK', 'VIEW', 'HARM-BC', 'FACT-BC'):
            out = wytnij(out, blok)
        out = re.sub(r'<script>.*?</script>', '', out, flags=re.S)
        out = out.replace('<main id="panel-s" data-track="s" aria-label="Plan szkolenia — szkoła podstawowa" hidden>',
                          '<main id="panel-s" data-track="s" aria-label="Plan szkolenia — szkoła podstawowa">')
        out = out.replace('<div class="navs">\n    </div>', '')
    else:
        out = wytnij(out, 'HARM-A')
        out = wytnij(out, 'FACT-A')

    if cfg.get('marka'):
        out = out.replace('<!--LOGO-->', LOGO_IMG)
        out = out.replace('</style>\n\n<div class="topbar">', '</style>\n' + PALETA_PCTP + '\n<div class="topbar">')
    else:
        out = out.replace('<!--LOGO-->', '')

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
