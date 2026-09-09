#!/usr/bin/env python3
"""Dzieli opowiadanie na scenariusz do nagrania: jeden plik .txt na rozdział.

Uruchomienie:
    python3 opowiadania/skrypty/przygotuj_scenariusz.py           # obie części
    python3 opowiadania/skrypty/przygotuj_scenariusz.py 2         # tylko część druga

Pliki trafiają do opowiadania/audio/scenariusz (część 1)
i opowiadania/audio/scenariusz-czesc-2 (część druga).
"""
import re
import sys
import unicodedata
from pathlib import Path

KATALOG = Path(__file__).resolve().parent.parent

CZESCI = {
    "1": {"zrodlo": "rajmund-i-arystoteles.md", "wyjscie": "audio/scenariusz"},
    "2": {"zrodlo": "rajmund-i-arystoteles-czesc-2.md", "wyjscie": "audio/scenariusz-czesc-2"},
}

LICZEBNIKI = {
    1: "pierwszy", 2: "drugi", 3: "trzeci", 4: "czwarty", 5: "piąty", 6: "szósty",
    7: "siódmy", 8: "ósmy", 9: "dziewiąty", 10: "dziesiąty", 11: "jedenasty",
    12: "dwunasty", 13: "trzynasty", 14: "czternasty", 15: "piętnasty",
    16: "szesnasty", 17: "siedemnasty", 18: "osiemnasty", 19: "dziewiętnasty",
    20: "dwudziesty", 21: "dwudziesty pierwszy", 22: "dwudziesty drugi",
    23: "dwudziesty trzeci", 24: "dwudziesty czwarty", 25: "dwudziesty piąty",
    26: "dwudziesty szósty", 27: "dwudziesty siódmy", 28: "dwudziesty ósmy",
    29: "dwudziesty dziewiąty", 30: "trzydziesty", 31: "trzydziesty pierwszy",
    32: "trzydziesty drugi", 33: "trzydziesty trzeci", 34: "trzydziesty czwarty",
    35: "trzydziesty piąty", 36: "trzydziesty szósty", 37: "trzydziesty siódmy",
}


def slug(tekst: str) -> str:
    bez_ogonkow = unicodedata.normalize("NFKD", tekst.lower().replace("ł", "l"))
    bez_ogonkow = "".join(z for z in bez_ogonkow if not unicodedata.combining(z))
    czysty = re.sub(r"[^a-z0-9]+", "-", bez_ogonkow).strip("-")
    return "-".join(czysty.split("-")[:3])


def rozdzialy(md: str):
    opowiadanie = md.split("\n# Słowniczek")[0]
    for kawalek in re.split(r"\n## ", opowiadanie)[1:]:
        naglowek, tekst = kawalek.split("\n", 1)
        if not re.match(r"^\d+\.\s", naglowek):
            continue
        nr, tytul = naglowek.split(". ", 1)
        tresc = tekst.split("\n---")[0]
        tresc = " ".join(l.strip() for l in tresc.split("\n") if l.strip())
        tresc = tresc.replace('"', "").replace("—", "-")
        yield int(nr), tytul.strip(), tresc


def main() -> int:
    wybor = sys.argv[1] if len(sys.argv) > 1 else "wszystkie"
    klucze = list(CZESCI) if wybor == "wszystkie" else [wybor]
    for klucz in klucze:
        cfg = CZESCI[klucz]
        katalog = KATALOG / cfg["wyjscie"]
        katalog.mkdir(parents=True, exist_ok=True)
        md = (KATALOG / cfg["zrodlo"]).read_text(encoding="utf-8")
        ile = 0
        for nr, tytul, tresc in rozdzialy(md):
            plik = katalog / f"rozdzial-{nr:02d}-{slug(tytul)}.txt"
            plik.write_text(f"Rozdział {LICZEBNIKI[nr]}. {tytul}.\n\n{tresc}\n", encoding="utf-8")
            ile += 1
        print(f"część {klucz}: {ile} plików w {katalog}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
