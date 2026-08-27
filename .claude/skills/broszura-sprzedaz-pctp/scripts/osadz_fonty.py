#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Buduje wersję HTML gotową do druku: bez odwołań do sieci, z fontami marki
osadzonymi w pliku.

Użycie:
    python3 osadz_fonty.py broszura.html Broszura_DRUK.html "Tytuł publikacji"

Dlaczego to jest konieczne: przeglądarka renderująca PDF często nie ma dostępu
do fonts.googleapis.com. Bez osadzenia PDF wychodzi krojami zastępczymi
(Liberation, DejaVu) i nie wygląda jak wersja na ekranie.

Dlaczego pobieramy statyczne, a nie zmienne: z fontów zmiennych przeglądarka
robi w PDF-ie glify typu Type3 — tekst przestaje być normalnie zaznaczalny,
a naświetlarnie obsługują je źle. Statyczne instancje dają poprawny Type0.
"""
import re, subprocess, base64, io, sys, os

# UA starszej przeglądarki wymusza serwowanie statycznych plików na wagę
UA = "Mozilla/5.0 (Windows NT 6.1; rv:27.0) Gecko/20100101 Firefox/27.0"

# Kroje marki PCTP — patrz skill eduplaner-pctp
RODZINY = [
    "Fraunces:ital,wght@0,400;0,500;0,600;0,700;0,900;1,400",
    "DM+Sans:wght@400;500;700",
    "JetBrains+Mono:wght@400;500;700",
]

WEJSCIE = sys.argv[1] if len(sys.argv) > 1 else 'broszura.html'
WYJSCIE = sys.argv[2] if len(sys.argv) > 2 else 'Broszura_DRUK.html'
TYTUL   = sys.argv[3] if len(sys.argv) > 3 else None
AUTOR   = os.environ.get('BROSZURA_AUTOR', 'mgr Mirosława Jurczyszyn — PCTP Koszalin')
OPIS    = os.environ.get('BROSZURA_OPIS', '')


def pobierz(url, binarnie=False):
    r = subprocess.run(['curl', '-sS', '--max-time', '60', '-A', UA, url], capture_output=True)
    if r.returncode:
        raise SystemExit('Nie udało się pobrać: %s\n%s' % (url, r.stderr.decode()[:300]))
    return r.stdout if binarnie else r.stdout.decode('utf-8')


def zbuduj_css():
    pole = lambda blok, k: (re.search(k + r':\s*([^;]+);', blok) or [None, ''])[1].strip()
    deklaracje, bajty = [], 0
    for rodzina in RODZINY:
        css = pobierz("https://fonts.googleapis.com/css2?family=%s&display=swap" % rodzina)
        for blok in re.findall(r'@font-face\s*\{[^}]*\}', css):
            m = re.search(r'url\((https://[^)]+)\)', blok)
            if not m:
                continue
            dane = pobierz(m.group(1), True); bajty += len(dane)
            deklaracje.append(
                "@font-face{font-family:%s;font-style:%s;font-weight:%s;font-display:block;"
                "src:url(data:font/woff;base64,%s) format('woff');}"
                % (pole(blok, 'font-family'), pole(blok, 'font-style'),
                   pole(blok, 'font-weight'), base64.b64encode(dane).decode()))
    print('osadzono %d krojów · %.0f kB' % (len(deklaracje), bajty / 1024))
    return '\n'.join(deklaracje)


tresc = io.open(WEJSCIE, encoding='utf-8').read()

# 1. usuń odwołania do Google Fonts — kroje będą w pliku
tresc = re.sub(r'<link rel="preconnect"[^>]*>\s*', '', tresc)
tresc = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>\s*', '', tresc)

# 2. układ mobilny nie może obowiązywać przy druku (strona ma tylko 210 mm)
if re.search(r'@media\s*\(max-width', tresc):
    tresc = re.sub(r'@media\s*\(max-width', '@media screen and (max-width', tresc)
    print('ograniczono reguły wąskiego ekranu do @media screen')

if TYTUL:
    tresc = re.sub(r'<title>.*?</title>', '<title>%s</title>' % TYTUL, tresc, count=1, flags=re.S)

glowa = ('<!DOCTYPE html>\n<html lang="pl">\n<head>\n<meta charset="UTF-8">\n'
         '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
         '<meta name="author" content="%s">\n'
         '<meta name="description" content="%s">\n'
         '<style>@page{size:210mm 297mm;margin:0;}</style>\n'
         '<style>\n%s</style>\n' % (AUTOR, OPIS, zbuduj_css()))

i = tresc.index('<title>')
ciało = tresc[i:]
# domknij <head> tam, gdzie zaczyna się treść strony
ciało = re.sub(r'</style>\s*\n\s*(<div class="(?:toolbar|page))',
               r'</style>\n</head>\n<body>\n\n\1', ciało, count=1)

io.open(WYJSCIE, 'w', encoding='utf-8').write(glowa + ciało + '\n</body>\n</html>\n')
print('zapisano %s · %.0f kB' % (WYJSCIE, os.path.getsize(WYJSCIE) / 1024))
