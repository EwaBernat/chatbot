#!/usr/bin/env python3
"""Napisy i czasy scen BEZ nagrania — z samego tekstu scenariusza.

Gdy nie ma jeszcze MP3 (np. wyczerpany limit ElevenLabs), liczymy czas każdego zdania
z liczby sylab (0,20 s/sylabę + pauzy na znakach przestankowych) i odstępy 0,6 s.
Wynik ma ten sam kształt co public/<film>.json z wyrownaj.py, więc po dograniu głosu
wystarczy `python3 skrypty/wyrownaj.py <film>` i sceny same się przesuną.

Użycie: python3 skrypty/napisy_z_tekstu.py wopf
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wyrownaj import zdania, sylaby  # noqa: E402

KATALOG = Path(__file__).resolve().parent.parent
film = sys.argv[1] if len(sys.argv) > 1 else "wopf"
tekst = (KATALOG / "public" / f"{film}-scenariusz.txt").read_text(encoding="utf-8")
zd = zdania(tekst)
akapity = [a for a in tekst.split("\n\n") if a.strip()]
konce_akapitow = set()
n = 0
for a in akapity:
    n += len(zdania(a))
    konce_akapitow.add(n - 1)

t = 0.8
napisy = []
for i, z in enumerate(zd):
    dl = round(sylaby(z) * 0.20 + 0.4, 2)
    napisy.append({"odSek": round(t, 2), "doSek": round(t + dl, 2), "tekst": z})
    t += dl + (1.0 if i in konce_akapitow else 0.6)
dane = {"audio": None, "napisy": napisy, "dlugosc": round(t + 1.5, 2)}
(KATALOG / "public" / f"{film}.json").write_text(json.dumps(dane, ensure_ascii=False, indent=1), encoding="utf-8")
for i, nap in enumerate(napisy):
    print(f"{i:2d} {nap['odSek']:6.2f} {nap['doSek']:6.2f}  {nap['tekst'][:80]}")
print(f"\nZapisano public/{film}.json — {len(napisy)} zdań, {dane['dlugosc']} s (bez nagrania)")
