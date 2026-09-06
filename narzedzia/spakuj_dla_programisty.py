#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Paczka modułu dla programisty — dane, dokumenty, kod i media.

    python3 narzedzia/spakuj_dla_programisty.py                 # wszystkie moduły
    python3 narzedzia/spakuj_dla_programisty.py fba mowa
    python3 narzedzia/spakuj_dla_programisty.py --cel ~/Pulpit --limit 27

Ten sam układ, co paczka FBA, którą autorka wysyłała wcześniej — odbiorca ma
jedną konwencję na cały ekosystem:

    01_dane_json/          ← TO SIĘ WPINA
    02_gotowe_dokumenty/   ← tak ma wyglądać efekt (HTML + PDF)
    03_kod_zrodlowy/       ← jak to powstaje
    04_media/              ← zdjęcia, nagrania i symbole

Dwie rzeczy, które łatwo przeoczyć, a bez których paczka jest niepełna:

**Symbole na arkuszach idą ze wspólnej biblioteki.** Ścieżki w JSON wskazują
`eduplaner_przedszkole/assets/symbole/…`, a te pliki leżą w media_wspolne/,
nie w module. Gdyby paczka niosła sam moduł, kilkaset symboli zniknęłoby
z arkuszy bez żadnego komunikatu — brak nie wysypuje budowania. Skrypt dokłada
te obrazki, które naprawdę wchodzą na arkusze, w układzie katalogów z JSON-a.

**Dokumenty HTML linkują media, a nie noszą ich w sobie.** Otwarte z rozpakowanej
paczki działają, bo `04_media/` leży obok. Przeniesione same, bez katalogu —
pokażą puste pola zamiast zdjęć i wyłączone przyciski zamiast nagrań.

Komplet bywa większy niż limit przesyłki, więc dzieli się na ponumerowane części.
Każda niesie kartkę „część N z M" z nazwami pozostałych — gdyby któraś zaginęła,
od razu widać, czego brakuje.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import shutil
import subprocess
import sys

KORZEN = pathlib.Path(__file__).resolve().parent.parent
MODULY = ["sens", "tom", "mowa", "fba"]
WSPOLNE = KORZEN / "media_wspolne"


def uzyte_symbole(modul: str) -> set[str]:
    """Ścieżki symboli, które naprawdę wchodzą na arkusze — z JSON-a, nie z katalogu."""
    plik = KORZEN / f"eduplaner_{modul}" / "01_dane_json" / "materialy_do_druku.json"
    if not plik.exists():
        return set()
    dane = json.loads(plik.read_text(encoding="utf-8"))
    sciezki = set()
    for a in dane.get("arkusze", []):
        for pole in list(a.get("karty", [])) + list(a.get("pasek_kolejnosci", [])):
            if pole.get("plik_symbolu"):
                sciezki.add(pole["plik_symbolu"])
        h = a.get("historyjka") or {}
        for kadr in h.get("kadry", []) if isinstance(h, dict) else []:
            if kadr.get("plik"):
                sciezki.add(kadr["plik"])
    return sciezki


def zbierz(modul: str, robocze: pathlib.Path) -> list[pathlib.Path]:
    zrodlo = KORZEN / f"eduplaner_{modul}"
    baza = robocze / f"EduPlaner2026_Modul_{modul.upper()}"
    if baza.exists():
        shutil.rmtree(baza)
    zebrane = []

    for czesc in ("01_dane_json", "02_gotowe_dokumenty", "03_kod_zrodlowy", "04_media"):
        skad = zrodlo / czesc
        if not skad.exists():
            continue
        dokad = baza / czesc
        shutil.copytree(skad, dokad,
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "uczen_*",
                                                      "*.orig.mp3", "*.orig.png"))

    # symbole ze wspólnej biblioteki — w układzie katalogów, którego trzyma się JSON
    dolozone = 0
    for wzgledna in uzyte_symbole(modul):
        cel = baza / "04_media" / wzgledna
        if cel.exists():
            continue
        for kandydat in (WSPOLNE / wzgledna, WSPOLNE / pathlib.Path(wzgledna).name):
            if kandydat.exists():
                cel.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(kandydat, cel)
                dolozone += 1
                break
    logo = WSPOLNE / "logo_pctp.png"
    if logo.exists():
        (baza / "04_media").mkdir(parents=True, exist_ok=True)
        shutil.copy2(logo, baza / "04_media" / "logo_pctp.png")

    (baza / "CZYTAJ_TO_NAJPIERW.md").write_text(czytaj(modul, dolozone), encoding="utf-8")
    zebrane = sorted(p for p in baza.rglob("*") if p.is_file())
    return zebrane


def czytaj(modul: str, symboli: int) -> str:
    kod = modul.upper()
    dane = KORZEN / f"eduplaner_{modul}" / "01_dane_json"
    pliki = "\n".join(f"| `{p.name}` | {p.stat().st_size // 1024} KB |"
                      for p in sorted(dane.glob("*.json")))
    return f"""# Moduł {kod} — EduPlaner 2026

Autorka treści: **mgr Mirosława Ewa Jurczyszyn**, pedagog specjalny, PCTP Koszalin.

## Od czego zacząć

**Wpina się `01_dane_json`. HTML jest wzorcem docelowym, nie źródłem.**

Dokumenty w `02_gotowe_dokumenty/` pokazują, jak materiał ma wyglądać
u nauczyciela. Treść wyjęta z HTML-a nigdy się już nie zsynchronizuje
z poprawkami autorki — JSON eksportuje się jednym poleceniem i jest
przeznaczony do maszyny.

| plik | rozmiar |
|---|---|
{pliki}

## Ścieżki do mediów

Wszystkie ścieżki w JSON liczone są od katalogu **`04_media/`**:

```
04_media/eduplaner_{modul}/assets/pomoce_{modul}/…jpg     zdjęcia pomocy
04_media/eduplaner_{modul}/assets/audio_{modul}/…mp3      nagrania poleceń
04_media/eduplaner_przedszkole/assets/symbole/…jpg   symbole na arkusze
```

Symbole na arkuszach pochodzą ze **wspólnej biblioteki** całego ekosystemu —
ten sam obrazek ma być na tablicy AAC dziecka, w planie dnia i na wyciętej
karcie. Do tej paczki dołożono {symboli} plików, które naprawdę wchodzą na
arkusze tego modułu.

## Dokumenty HTML linkują media, nie noszą ich w sobie

Otwarte z rozpakowanej paczki działają, bo `04_media/` leży obok. Przeniesione
same, bez tego katalogu, pokażą puste pola zamiast zdjęć i wyłączony przycisk
zamiast nagrania. **Brak nie wysypuje budowania** — dokument złoży się i będzie
wyglądał dobrze, a nauczyciel dowie się przy drukarce.

## Jak przebudować dokumenty

```bash
python3 03_kod_zrodlowy/eksport_json.py      # dane → 01_dane_json/
python3 03_kod_zrodlowy/build_tabela.py      # tabela celów + konspekty
python3 03_kod_zrodlowy/build_karty_pracy.py # karty pracy A4
python3 narzedzia/zrob_pdf.py {modul}            # PDF-y (z repozytorium)
```

## Nagrania

`04_media/…/audio_{modul}/` to polecenia dla dziecka przeczytane **własnym,
sklonowanym głosem autorki**. To dana biometryczna: nie publikuj ich osobno,
nie używaj do innych materiałów i nie zastępuj innym głosem.
"""


def na_czesci(pliki: list[pathlib.Path], baza: pathlib.Path, limit_mb: int):
    """Podział na paczki mieszczące się w limicie — po katalogach najwyższego rzędu."""
    limit = limit_mb * 1024 * 1024
    grupy: dict[str, list[pathlib.Path]] = {}
    for p in pliki:
        grupy.setdefault(p.relative_to(baza).parts[0], []).append(p)
    czesci, biezaca, waga = [], [], 0
    for _, lista in sorted(grupy.items()):
        # Katalog trzymam w jednej części, dopóki się w niej mieści. Same
        # dokumenty MOWY ważą 43 MB, więc gdy katalog przerasta limit, dzielę
        # go plik po pliku — inaczej powstaje „część”, której nie da się wysłać.
        for p in lista if sum(x.stat().st_size for x in lista) > limit else [lista]:
            grupa = p if isinstance(p, list) else [p]
            rozmiar = sum(x.stat().st_size for x in grupa)
            if biezaca and waga + rozmiar > limit:
                czesci.append(biezaca); biezaca, waga = [], 0
            biezaca += grupa; waga += rozmiar
    if biezaca:
        czesci.append(biezaca)
    return czesci


def spakuj(modul: str, cel: pathlib.Path, limit: int) -> list[pathlib.Path]:
    robocze = cel / "_robocze"
    robocze.mkdir(parents=True, exist_ok=True)
    pliki = zbierz(modul, robocze)
    baza = robocze / f"EduPlaner2026_Modul_{modul.upper()}"
    czesci = na_czesci(pliki, baza, limit)
    ile = len(czesci)
    wyniki = []
    for nr, lista in enumerate(czesci, 1):
        nazwa = (f"EduPlaner2026_Modul_{modul.upper()}.zip" if ile == 1 else
                 f"EduPlaner2026_Modul_{modul.upper()}_czesc_{nr}_z_{ile}.zip")
        plik = cel / nazwa
        plik.unlink(missing_ok=True)
        wzgledne = [str(p.relative_to(robocze)) for p in lista]
        subprocess.run(["zip", "-q", "-9", str(plik), *wzgledne],
                       cwd=robocze, check=True)
        wyniki.append(plik)
        print(f"  {plik.name:<52} {plik.stat().st_size / 1024 / 1024:5.1f} MB · "
              f"{len(lista)} plików")
    shutil.rmtree(robocze)
    return wyniki


def main() -> int:
    ap = argparse.ArgumentParser(description="Paczki modułów dla programisty")
    ap.add_argument("moduly", nargs="*", default=None, help="które moduły (domyślnie wszystkie)")
    ap.add_argument("--cel", default="/tmp/paczki_arek", help="katalog docelowy")
    ap.add_argument("--limit", type=int, default=27, help="limit części w MB")
    a = ap.parse_args()
    cel = pathlib.Path(a.cel)
    cel.mkdir(parents=True, exist_ok=True)
    for m in (a.moduly or MODULY):
        print(f"\n{m.upper()}")
        spakuj(m, cel, a.limit)
    print(f"\nGotowe — {cel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
