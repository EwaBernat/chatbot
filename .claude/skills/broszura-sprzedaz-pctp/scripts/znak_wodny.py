#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tworzy egzemplarz imienny broszury — z danymi nabywcy w stopce każdej strony.

Użycie:
    python3 znak_wodny.py "Anna Kowalska · anna@szkola.pl" "indywidualna"
    python3 znak_wodny.py "SP nr 4 w Koszalinie" "placówki" 2026-09-01

Znak wodny jest dyskretny: jedna linia szarym tekstem u dołu, poza obszarem
treści. Nie utrudnia czytania ani druku, ale pozwala ustalić źródło pliku
udostępnionego niezgodnie z licencją.
"""
import sys, os, hashlib
import pymupdf

ZRODLO = 'Echolalia_i_rozumienie_jej_funkcji.pdf'
MM = 72 / 25.4

if len(sys.argv) < 2:
    print(__doc__); sys.exit(1)

nabywca  = sys.argv[1]
licencja = sys.argv[2] if len(sys.argv) > 2 else 'indywidualna'
data     = sys.argv[3] if len(sys.argv) > 3 else ''

# krótki, powtarzalny identyfikator egzemplarza — do powiązania z zamówieniem
odcisk = hashlib.sha256((nabywca + licencja + data).encode('utf-8')).hexdigest()[:10].upper()
podpis = 'Egzemplarz: %s · licencja %s · nr %s' % (nabywca, licencja, odcisk)

d = pymupdf.open(ZRODLO)
for n, strona in enumerate(d):
    if n == 0:                       # okładki nie znakujemy
        continue
    strona.insert_textbox(
        pymupdf.Rect(15 * MM, strona.rect.height - 4.6 * MM,
                     strona.rect.width - 15 * MM, strona.rect.height - 1.2 * MM),
        podpis, fontsize=5.6, fontname='helv',
        color=(0.62, 0.60, 0.66), align=pymupdf.TEXT_ALIGN_CENTER)

d.set_metadata({**d.metadata, 'keywords': (d.metadata.get('keywords') or '') + ' | ' + podpis})
bezpieczna = ''.join(c if c.isalnum() else '_' for c in nabywca)[:40]
wynik = 'egzemplarze/Echolalia_%s_%s.pdf' % (bezpieczna, odcisk)
os.makedirs('egzemplarze', exist_ok=True)
d.save(wynik, garbage=4, deflate=True)
print('zapisano: %s' % wynik)
print('numer egzemplarza: %s  (zanotuj przy zamówieniu)' % odcisk)
