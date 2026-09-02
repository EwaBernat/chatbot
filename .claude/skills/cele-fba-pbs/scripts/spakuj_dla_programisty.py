#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Paczka modułu FBA/PBS dla programisty — dane, dokumenty, kod, media.

Ten sam układ, co paczka banku celów SMART, żeby odbiorca miał jedną konwencję
na cały ekosystem. Skrypt dzieli komplet na ponumerowane części mieszczące się
w limicie przesyłki; każda niesie własną kartkę „część N z M" z nazwami
wszystkich pozostałych — gdyby któraś zaginęła, od razu widać, czego brakuje.

Jedna rzecz jest tu inna niż w banku i łatwo ją przeoczyć: **arkusze FBA używają
symboli z banku KPOF**. Gdyby paczka niosła sam moduł FBA, ścieżki w JSON
wskazywałyby pliki, których odbiorca nie ma, i 172 symbole zniknęłyby bez
komunikatu. Dlatego skrypt dokłada te obrazki z sąsiedniego modułu — tylko te
naprawdę użyte — zachowując układ katalogów, którego trzyma się JSON.

Do środka wchodzi to, czego programista potrzebuje: dane JSON, zbudowane
dokumenty, kod źródłowy i te wersje mediów, które wchodzą do dokumentów.
Oryginały sprzed kompresji (`*.orig.mp3`, duże PNG-i) zostają w repozytorium.

Uruchomienie:
  python3 .claude/skills/cele-fba-pbs/scripts/spakuj_dla_programisty.py
  ... --korzen /sciezka/do/eduplaner_fba --cel /gdzie/zapisac --limit 28
  ... --czytaj opis_dla_odbiorcy.md
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import zlib

NAZWA = "EduPlaner2026_Modul_FBA_PBS"


def znajdz_korzen(podany=None):
    if podany:
        return os.path.abspath(podany)
    tu = os.path.abspath(__file__)
    for _ in range(8):
        tu = os.path.dirname(tu)
        k = os.path.join(tu, "eduplaner_fba")
        if os.path.isdir(os.path.join(k, "src")):
            return k
    return None


def uzyte_symbole(korzen):
    """Ścieżki symboli, które naprawdę wchodzą na arkusze — z eksportu JSON."""
    sys.path.insert(0, os.path.join(korzen, "src"))
    import eksport_json
    dane = eksport_json.materialy_do_druku()
    sciezki = set()
    for a in dane["arkusze"]:
        for pole in a["karty"] + a["pasek_kolejnosci"]:
            if pole.get("plik_symbolu"):
                sciezki.add(pole["plik_symbolu"])
    return sorted(sciezki)


def zbierz(korzen, robocze):
    """Drzewo paczki: dane, dokumenty, kod, media."""
    baza = os.path.join(robocze, NAZWA)
    dol = lambda *c: os.path.join(baza, *c)
    for k in ("01_dane_json", "02_gotowe_dokumenty/html", "02_gotowe_dokumenty/pdf",
              "03_kod_zrodlowy/src", "04_media"):
        os.makedirs(dol(*k.split("/")), exist_ok=True)

    # dane — świeży eksport, żeby JSON nie rozjechał się z dokumentami
    sys.path.insert(0, os.path.join(korzen, "src"))
    import eksport_json
    eksport_json.main(dol("01_dane_json"))

    # dokumenty
    for plik in sorted(os.listdir(korzen)):
        p = os.path.join(korzen, plik)
        if not os.path.isfile(p):
            continue
        if plik.endswith(".html"):
            shutil.copy2(p, dol("02_gotowe_dokumenty", "html", plik))
        elif plik.endswith(".pdf"):
            shutil.copy2(p, dol("02_gotowe_dokumenty", "pdf", plik))

    # kod
    for plik in sorted(os.listdir(os.path.join(korzen, "src"))):
        if plik.endswith((".py", ".mjs", ".sh")):
            shutil.copy2(os.path.join(korzen, "src", plik), dol("03_kod_zrodlowy", "src", plik))
    czytaj = os.path.join(korzen, "README.md")
    if os.path.exists(czytaj):
        shutil.copy2(czytaj, dol("03_kod_zrodlowy", "README_projektu.md"))

    # media modułu — tylko wersje wchodzące do dokumentów.
    # Układ katalogów mirroruje repozytorium, bo dokładnie tak liczy ścieżki JSON:
    # katalogiem bazowym dla wszystkich ścieżek jest `04_media/`.
    rodzic = os.path.dirname(korzen)
    A = os.path.join(korzen, "assets")
    for kat in sorted(os.listdir(A)) if os.path.isdir(A) else []:
        zrodlo = os.path.join(A, kat)
        if not os.path.isdir(zrodlo):
            continue
        cel = dol("04_media", os.path.basename(korzen), "assets", kat)
        for plik in sorted(os.listdir(zrodlo)):
            bierz = (plik.endswith(".mp3") and not plik.endswith(".orig.mp3")) \
                if kat.startswith("audio") else plik.startswith("k_")
            if bierz:
                os.makedirs(cel, exist_ok=True)
                shutil.copy2(os.path.join(zrodlo, plik), os.path.join(cel, plik))

    # symbole z banku KPOF — bez nich arkusze w JSON wskazują w próżnię
    braki = []
    for wzgledna in uzyte_symbole(korzen):
        zrodlo = os.path.join(rodzic, wzgledna)
        if not os.path.exists(zrodlo):
            braki.append(wzgledna)
            continue
        docelowy = dol("04_media", *wzgledna.split("/"))
        os.makedirs(os.path.dirname(docelowy), exist_ok=True)
        shutil.copy2(zrodlo, docelowy)
    if braki:
        print(f"  UWAGA: {len(braki)} symboli nie znalazłem — arkusze będą bez obrazków")
        for b in braki[:5]:
            print(f"    · {b}")
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


def na_czesci(baza, limit_mb):
    """Grupuje elementy paczki w części mieszczące się w limicie.

    Dzielimy dopiero, gdy trzeba. Moduł FBA jest mniejszy od banku i zwykle
    mieści się w jednym archiwum — a jedna przesyłka jest dla odbiorcy o całą
    klasę wygodniejsza niż dwie, których obie trzeba rozpakować w to samo
    miejsce, żeby cokolwiek działało.
    """
    wszystko = sorted(os.listdir(baza))
    if po_spakowaniu(baza, wszystko) <= limit_mb * 1024 * 1024:
        return [("komplet", "Komplet: dane JSON, dokumenty, kod, media", wszystko)]

    D = "02_gotowe_dokumenty"
    czesci = [("dane_kod_media", "Dane JSON, kod źródłowy, media",
               ["SPIS_ZAWARTOSCI.txt", "01_dane_json", "03_kod_zrodlowy", "04_media"])]
    html = os.path.join(baza, D, "html")
    dokumenty = []
    for plik in sorted(os.listdir(html)) if os.path.isdir(html) else []:
        para = [f"{D}/html/{plik}"]
        pdf = plik.replace(".html", ".pdf")
        if os.path.exists(os.path.join(baza, D, "pdf", pdf)):
            para.append(f"{D}/pdf/{pdf}")
        dokumenty.append((os.path.splitext(plik)[0], para))
    pdfy = os.path.join(baza, D, "pdf")
    uzyte = {s for _, para in dokumenty for s in para}
    luzem = [f"{D}/pdf/{p}" for p in sorted(os.listdir(pdfy))
             if f"{D}/pdf/{p}" not in uzyte] if os.path.isdir(pdfy) else []

    limit = limit_mb * 1024 * 1024
    biezaca, opis = [], []
    for nazwa, para in dokumenty:
        # Miarą jest rozmiar PO spakowaniu, nie na dysku: HTML z data-URI kurczy
        # się o jedną czwartą, a PDF prawie wcale.
        if biezaca and po_spakowaniu(baza, biezaca + para) > limit:
            czesci.append((etykieta(opis), ", ".join(opis), biezaca))
            biezaca, opis = [], []
        if not biezaca:
            biezaca = list(luzem); luzem = []
        biezaca += para
        opis.append(nazwa)
    if biezaca or luzem:
        czesci.append((etykieta(opis) or "dokumenty", ", ".join(opis) or "PDF-y",
                       biezaca + luzem))
    return czesci


def etykieta(nazwy):
    """Krótka, czytelna nazwa grupy — wspólny przedrostek zamiast sklejki nazw."""
    if not nazwy:
        return ""
    if len(nazwy) == 1:
        return nazwy[0][:44]
    czlony = [n.split("_")[0] for n in nazwy]
    if len(set(czlony)) == 1:
        return f"{czlony[0]}_x{len(nazwy)}"
    return "_".join(czlony)[:44]


def kartka(nr, ile, opis, pliki, nazwy):
    L = [f"{NAZWA} · EduPlaner 2026", "=" * 60]
    if ile == 1:
        L += ["KOMPLET W JEDNYM ARCHIWUM", "",
              "Wszystko jest tutaj — nie ma dalszych części do czekania.",
              "Zacznij od CZYTAJ_TO_NAJPIERW.md.", "", "ZAWARTOŚĆ", "-" * 60]
    else:
        L += [f"CZĘŚĆ {nr} Z {ile} — {opis}", "",
              f"Komplet ma {ile} archiwów. Rozpakuj WSZYSTKIE {ile} do tego samego",
              "katalogu — ułożą się w jedno drzewo katalogów.",
              "Opis całości: CZYTAJ_TO_NAJPIERW.md", "", "WSZYSTKIE CZĘŚCI", "-" * 60]
        for n, (o, plik) in enumerate(nazwy, 1):
            L += [f"{'▶' if n == nr else ' '} część {n} z {ile} — {o}", f"    {plik}"]
        L += ["", "W TEJ CZĘŚCI", "-" * 60]
    L += [f"  · {p}" for p in pliki]
    L += ["", "Autorka treści: mgr Mirosława Ewa Jurczyszyn",
          "pedagog specjalny · PCTP Koszalin", ""]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="Paczka modułu FBA/PBS dla programisty")
    ap.add_argument("--korzen", help="katalog eduplaner_fba")
    ap.add_argument("--cel", default=".", help="gdzie zapisać archiwa")
    ap.add_argument("--limit", type=float, default=28, help="limit części w MB (domyślnie 28)")
    ap.add_argument("--czytaj", help="plik CZYTAJ_TO_NAJPIERW.md do dołożenia")
    args = ap.parse_args()

    korzen = znajdz_korzen(args.korzen)
    if not korzen:
        print("Nie znalazłem katalogu eduplaner_fba. Podaj --korzen.")
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
    nazwy = ([(czesci[0][1], f"{NAZWA}.zip")] if ile == 1 else
             [(opis, f"{NAZWA}_CZESC_{n}_z_{ile}_{suf}.zip")
              for n, (suf, opis, _) in enumerate(czesci, 1)])

    print(f"\nSkładam {ile} archiwum" if ile == 1
          else f"\nDzielę na {ile} części (limit {args.limit:g} MB):")
    for nr, ((suf, opis, pliki), (_, plik_zip)) in enumerate(zip(czesci, nazwy), 1):
        kat = os.path.join(robocze, f"_b{nr}", NAZWA)
        os.makedirs(kat, exist_ok=True)
        czytaj = os.path.join(baza, "CZYTAJ_TO_NAJPIERW.md")
        if os.path.exists(czytaj):
            shutil.copy2(czytaj, kat)
        etykieta_pliku = "ZAWARTOSC.txt" if ile == 1 else f"CZESC_{nr}_z_{ile}.txt"
        with open(os.path.join(kat, etykieta_pliku), "w", encoding="utf-8") as f:
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
    if ile > 1:
        print("Odbiorca rozpakowuje WSZYSTKIE części do jednego katalogu.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
