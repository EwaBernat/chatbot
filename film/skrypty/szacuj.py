#!/usr/bin/env python3
"""Wstępne czasy scen z długości akapitów — zanim powstanie nagranie.

Tempo lektora z M1: ok. 16,4 znaku na sekundę plus ok. 0,8 s pauzy po akapicie.
Po nagraniu uruchom wyrownaj.py, który nadpisze te czasy rzeczywistymi.
"""
import argparse, json, re
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument('--narracja', required=True)
ap.add_argument('--sceny', required=True)
ap.add_argument('--tempo', type=float, default=16.4)
ap.add_argument('--pauza', type=float, default=0.8)
a = ap.parse_args()

aka = [b.strip() for b in re.split(r'\n\s*\n', Path(a.narracja).read_text(encoding='utf-8')) if b.strip()]
t, pocz = 0.0, {}
for i, ak in enumerate(aka, 1):
    pocz[i] = t
    t += len(ak) / a.tempo + a.pauza
koniec = t

sc = json.loads(Path(a.sceny).read_text(encoding='utf-8'))
L = sc['sceny']
for s in L:
    if 'akapit' in s:
        s['odSek'] = round(pocz.get(s['akapit'], 0.0), 2)
L[0]['odSek'] = 0.0
for i, s in enumerate(L):
    s['doSek'] = L[i + 1]['odSek'] if i + 1 < len(L) else round(koniec, 2)
Path(a.sceny).write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding='utf-8')
print(f"{sc['id']}: akapitów {len(aka)} · szacowana długość {koniec/60:.1f} min · scen {len(L)}")
