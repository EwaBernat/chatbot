#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Druk FBA-C — cele SMART do obserwacji pogłębionej. Osiem stron A4 pionowo.

    python3 eduplaner_fba/03_kod_zrodlowy/build_cele_fba.py
    python3 ... --uczen "Imię Nazwisko" --klasa "III A" --wyniki 7,8,13,7,13

Ten druk składa oryginalny program autorki z zrodlo_autorki/. Nie przepisałam go
na wzór pozostałych modułów z jednego powodu: w FBA im wyższy wynik funkcji, tym
gorzej — funkcja dominująca ma najkrótszy horyzont, bo jest priorytetem planu.
W SENS, ToM i MOWIE jest odwrotnie. Przepisany na tamtą logikę druk mówiłby
o tym samym wyniku dokładnie na odwrót, a to jest dokument, który idzie do
rodzica i do zespołu.

Uruchamiam jej program takim, jaki jest — tylko z katalogu, w którym leży,
i z wyjściem w 02_gotowe_dokumenty/.
"""
from __future__ import annotations

import pathlib
import subprocess
import sys

KORZEN = pathlib.Path(__file__).resolve().parent.parent
ZRODLO = KORZEN / "03_kod_zrodlowy" / "zrodlo_autorki"
WYJSCIE = KORZEN / "02_gotowe_dokumenty" / "Cele_SMART_FBA_obserwacja_poglebiona.html"


def main() -> int:
    WYJSCIE.parent.mkdir(parents=True, exist_ok=True)
    wynik = subprocess.run(
        [sys.executable, "build_cele_fba.py", "--wyjscie", str(WYJSCIE), *sys.argv[1:]],
        cwd=ZRODLO)
    if wynik.returncode:
        return wynik.returncode
    print(f"zapisano 02_gotowe_dokumenty/{WYJSCIE.name} "
          f"({WYJSCIE.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
