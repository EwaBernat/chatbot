#!/usr/bin/env python3
"""Wstawia pauzy SSML do narracji i dzieli ją na części < limit znaków.
Użycie: pauzy.py narracja.txt [--limit 2600] → drukuje części rozdzielone linią =====
"""
import re, sys, argparse
ap=argparse.ArgumentParser(); ap.add_argument('plik'); ap.add_argument('--limit',type=int,default=2600)
ap.add_argument('--zdanie',default='0.45s'); ap.add_argument('--akapit',default='0.9s')
a=ap.parse_args()
txt=open(a.plik,encoding='utf-8').read()
akapity=[b.strip() for b in re.split(r'\n\s*\n',txt) if b.strip()]
out=[]
for ak in akapity:
    zd=re.split(r'(?<=[.?!])\s+',ak)
    out.append(f' <break time="{a.zdanie}" /> '.join(z.strip() for z in zd if z.strip()))
pelny=f'\n\n<break time="{a.akapit}" />\n\n'.join(out)
# podział na części po akapitach
czesci,biez=[],''
for blok in pelny.split('\n\n'):
    if len(biez)+len(blok)+2>a.limit and biez:
        czesci.append(biez.strip()); biez=''
    biez+=blok+'\n\n'
if biez.strip(): czesci.append(biez.strip())
for i,c in enumerate(czesci,1):
    print(f'===== CZĘŚĆ {i} · {len(c)} znaków =====')
    print(c)
