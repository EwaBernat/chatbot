#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Paczka banku celów SMART dla programisty — dane, dokumenty, kod, media.

Komplet waży ponad sto megabajtów, a kanały, którymi się go przekazuje, mają
zwykle limit rzędu 25–30 MB. Skrypt składa paczkę i dzieli ją na ponumerowane
części, z których każda mieści się w limicie, a każda niesie własną kartkę
„część N z M" — gdyby któraś przesyłka zaginęła, od razu widać, czego brakuje
i jak się nazywa.

Do środka wchodzi tylko to, czego programista naprawdę potrzebuje: dane JSON,
zbudowane dokumenty, kod źródłowy i te wersje mediów, które faktycznie wchodzą
do dokumentów. Oryginały sprzed kompresji (duże PNG-i, `*.orig.mp3`) zostają
w repozytorium — do niczego poza ponownym przeliczeniem nie są potrzebne.

Uruchomienie:
  python3 .claude/skills/bank-celow-smart/scripts/spakuj_dla_programisty.py
  ... --korzen /sciezka/do/eduplaner_przedszkole --cel /gdzie/zapisac --limit 28
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import zlib

NAZWA = "EduPlaner2026_Bank_celow_SMART"


def znajdz_korzen(podany=None):
    if podany:
        return os.path.abspath(podany)
    tu = os.path.abspath(__file__)
    for _ in range(8):
        tu = os.path.dirname(tu)
        k = os.path.join(tu, "eduplaner_przedszkole")
        if os.path.isdir(os.path.join(k, "src")):
            return k
    return None


def zbierz(korzen, robocze):
    """Drzewo paczki: dane, dokumenty, kod, media, podstawa."""
    baza = os.path.join(robocze, NAZWA)
    dol = lambda *c: os.path.join(baza, *c)
    for k in ("01_dane_json", "02_gotowe_dokumenty/html", "02_gotowe_dokumenty/pdf",
              "03_kod_zrodlowy/src", "04_media/assets", "05_podstawa_programowa"):
        os.makedirs(dol(*k.split("/")), exist_ok=True)

    # dane — świeży eksport, żeby JSON nie rozjechał się z dokumentami
    sys.path.insert(0, os.path.join(korzen, "src"))
    import eksport_json
    eksport_json.main(dol("01_dane_json"))

    # dokumenty — bez druków podzielonych na obszary, bo bywają nieaktualne
    for plik in sorted(os.listdir(korzen)):
        p = os.path.join(korzen, plik)
        if not os.path.isfile(p) or plik.startswith(("Konspekty_KC3_", "Pomoce_KC4_")):
            continue
        if plik.endswith(".html"):
            shutil.copy2(p, dol("02_gotowe_dokumenty", "html", plik))
        elif plik.endswith(".pdf"):
            shutil.copy2(p, dol("02_gotowe_dokumenty", "pdf", plik))

    # kod
    for plik in sorted(os.listdir(os.path.join(korzen, "src"))):
        if plik.endswith((".py", ".mjs")):
            shutil.copy2(os.path.join(korzen, "src", plik), dol("03_kod_zrodlowy", "src", plik))
    czytaj = os.path.join(korzen, "README.md")
    if os.path.exists(czytaj):
        shutil.copy2(czytaj, dol("03_kod_zrodlowy", "README_projektu.md"))

    # media — tylko wersje wchodzące do dokumentów
    A = os.path.join(korzen, "assets")
    for kat in sorted(os.listdir(A)):
        zrodlo = os.path.join(A, kat)
        if os.path.isfile(zrodlo):
            shutil.copy2(zrodlo, dol("04_media", "assets", kat))
            continue
        cel = dol("04_media", "assets", kat)
        wzorce = ("k_", "kadr_") if not kat.startswith("audio") else ()
        for plik in sorted(os.listdir(zrodlo)):
            bierz = (plik.endswith(".mp3") and not plik.endswith(".orig.mp3")) \
                if kat.startswith("audio") else plik.startswith(wzorce)
            if bierz:
                os.makedirs(cel, exist_ok=True)
                shutil.copy2(os.path.join(zrodlo, plik), os.path.join(cel, plik))

    # podstawa programowa
    pp = os.path.join(korzen, "podstawa_2026")
    if os.path.isdir(pp):
        for plik in sorted(os.listdir(pp)):
            if plik.endswith(".pdf"):
                shutil.copy2(os.path.join(pp, plik), dol("05_podstawa_programowa", plik))
    return baza


def spis(baza):
    wiersze = []
    for root, kat, pliki in os.walk(baza):
        kat.sort()
        for n in sorted(pliki):
            p = os.path.join(root, n)
            wiersze.append((os.path.relpath(p, baza).replace(os.sep, "/"), os.path.getsize(p)))
    razem = sum(s for _, s in wiersze)
    with open(os.path.join(baza, "SPIS_ZAWARTOSCI.txt"), "w", encoding="utf-8") as f:
        f.write(f"{NAZWA} — spis zawartości\n")
        f.write(f"{len(wiersze)} plików · {razem/1048576:.1f} MB rozpakowane\n")
        f.write("=" * 78 + "\n\n")
        for s, b in wiersze:
            f.write(f"{s:<62}{b/1024:>10.1f} kB\n")
    return len(wiersze) + 1, razem


def na_czesci(baza, limit_mb):
    """Grupuje elementy paczki w części mieszczące się w limicie."""
    D = "02_gotowe_dokumenty"
    kandydaci = [
        ("dane_kod_media", "Dane JSON, kod źródłowy, media, podstawa programowa",
         ["SPIS_ZAWARTOSCI.txt", "01_dane_json", "03_kod_zrodlowy",
          "04_media", "05_podstawa_programowa"]),
    ]
    # dokumenty dokładamy pojedynczo, parami HTML+PDF, i tniemy po limicie
    html = os.path.join(baza, D, "html")
    dokumenty = []
    for plik in sorted(os.listdir(html)) if os.path.isdir(html) else []:
        pdf = plik.replace(".html", ".pdf")
        para = [f"{D}/html/{plik}"]
        if os.path.exists(os.path.join(baza, D, "pdf", pdf)):
            para.append(f"{D}/pdf/{pdf}")
        dokumenty.append((os.path.splitext(plik)[0], para))
    # PDF-y bez pary (np. załączniki) dołączamy do pierwszej grupy dokumentów
    pdfy = os.path.join(baza, D, "pdf")
    uzyte = {s for _, para in dokumenty for s in para}
    luzem = [f"{D}/pdf/{p}" for p in sorted(os.listdir(pdfy))
             if f"{D}/pdf/{p}" not in uzyte] if os.path.isdir(pdfy) else []

    limit = limit_mb * 1024 * 1024
    biezaca, opis_biezacej = [], []
    for nazwa, para in dokumenty:
        # Miarą jest rozmiar PO spakowaniu, nie na dysku: HTML z data-URI kurczy
        # się o jedną czwartą, a PDF prawie wcale. Pakowanie po rozmiarze surowym
        # dzieliło paczkę na więcej części, niż trzeba.
        if biezaca and po_spakowaniu(baza, biezaca + para) > limit:
            kandydaci.append((etykieta(opis_biezacej), ", ".join(opis_biezacej), biezaca))
            biezaca, opis_biezacej = [], []
        if not biezaca:
            biezaca = list(luzem); luzem = []
        biezaca += para
        opis_biezacej.append(nazwa)
    if biezaca:
        kandydaci.append((etykieta(opis_biezacej), ", ".join(opis_biezacej), biezaca))
    return kandydaci


def po_spakowaniu(baza, sciezki):
    """Szacunek rozmiaru po spakowaniu — próbka pliku, przeliczona na całość."""
    razem = 0
    for s in sciezki:
        p = os.path.join(baza, s)
        pliki = ([os.path.join(r, f) for r, _, fs in os.walk(p) for f in fs]
                 if os.path.isdir(p) else [p])
        for f in pliki:
            n = os.path.getsize(f)
            if n == 0:
                continue
            with open(f, "rb") as fh:
                probka = fh.read(min(n, 8 << 20))
            wsp = len(zlib.compress(probka, 6)) / len(probka)
            razem += int(n * wsp)
    return razem


def etykieta(nazwy):
    """Krótka, czytelna nazwa grupy — wspólny przedrostek zamiast sklejki nazw."""
    if len(nazwy) == 1:
        return nazwy[0][:44]
    czlony = [n.split("_")[0] for n in nazwy]
    if len(set(czlony)) == 1:
        return f"{czlony[0]}_x{len(nazwy)}"
    return "_".join(n.split("_")[0] for n in nazwy)[:44]


def kartka(nr, ile, opis, pliki, nazwy):
    L = [f"{NAZWA} · EduPlaner 2026", "=" * 60, f"CZĘŚĆ {nr} Z {ile} — {opis}", "",
         f"Komplet ma {ile} archiwów. Rozpakuj WSZYSTKIE {ile} do tego samego",
         "katalogu — ułożą się w jedno drzewo katalogów.",
         "Opis całości: CZYTAJ_TO_NAJPIERW.md", "", "WSZYSTKIE CZĘŚCI", "-" * 60]
    for n, (o, plik) in enumerate(nazwy, 1):
        L += [f"{'▶' if n == nr else ' '} część {n} z {ile} — {o}", f"    {plik}"]
    L += ["", "W TEJ CZĘŚCI", "-" * 60] + [f"  · {p}" for p in pliki]
    L += ["", "Autorka treści: mgr Mirosława Ewa Jurczyszyn",
          "pedagog specjalny · PCTP Koszalin", ""]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="Paczka banku dla programisty")
    ap.add_argument("--korzen", help="katalog eduplaner_przedszkole")
    ap.add_argument("--cel", default=".", help="gdzie zapisać archiwa")
    ap.add_argument("--limit", type=float, default=28, help="limit części w MB (domyślnie 28)")
    ap.add_argument("--czytaj", help="plik CZYTAJ_TO_NAJPIERW.md do dołożenia")
    args = ap.parse_args()

    korzen = znajdz_korzen(args.korzen)
    if not korzen:
        print("Nie znalazłem katalogu eduplaner_przedszkole. Podaj --korzen.")
        return 2
    cel = os.path.abspath(args.cel)
    os.makedirs(cel, exist_ok=True)
    robocze = os.path.join(cel, "_paczka_robocza")
    shutil.rmtree(robocze, ignore_errors=True)
    os.makedirs(robocze)

    print("Zbieram zawartość…")
    baza = zbierz(korzen, robocze)
    if args.czytaj and os.path.exists(args.czytaj):
        shutil.copy2(args.czytaj, os.path.join(baza, "CZYTAJ_TO_NAJPIERW.md"))
    ile_plikow, razem = spis(baza)
    print(f"  {ile_plikow} plików · {razem/1048576:.1f} MB")

    czesci = na_czesci(baza, args.limit)
    ile = len(czesci)
    nazwy = [(opis, f"{NAZWA}_CZESC_{n}_z_{ile}_{suf}.zip")
             for n, (suf, opis, _) in enumerate(czesci, 1)]

    print(f"\nDzielę na {ile} części (limit {args.limit:g} MB):")
    for nr, ((suf, opis, pliki), (_, plik_zip)) in enumerate(zip(czesci, nazwy), 1):
        kat = os.path.join(robocze, f"_b{nr}", NAZWA)
        os.makedirs(kat, exist_ok=True)
        czytaj = os.path.join(baza, "CZYTAJ_TO_NAJPIERW.md")
        if os.path.exists(czytaj):
            shutil.copy2(czytaj, kat)
        with open(os.path.join(kat, f"CZESC_{nr}_z_{ile}.txt"), "w", encoding="utf-8") as f:
            f.write(kartka(nr, ile, opis, pliki, nazwy))
        for s in pliki:
            zrodlo, docelowy = os.path.join(baza, s), os.path.join(kat, s)
            os.makedirs(os.path.dirname(docelowy), exist_ok=True)
            (shutil.copytree if os.path.isdir(zrodlo) else shutil.copy2)(zrodlo, docelowy)
        wynik = os.path.join(cel, plik_zip)
        if os.path.exists(wynik):
            os.remove(wynik)
        subprocess.run(["zip", "-q", "-r", "-9", wynik, NAZWA],
                       cwd=os.path.join(robocze, f"_b{nr}"), check=True)
        mb = os.path.getsize(wynik) / 1048576
        znak = "✗ NAD LIMIT" if mb > args.limit else "✓"
        print(f"  {znak} {plik_zip}  {mb:.1f} MB")

    shutil.rmtree(robocze, ignore_errors=True)
    print(f"\nGotowe w: {cel}")
    print("Odbiorca rozpakowuje WSZYSTKIE części do jednego katalogu.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
