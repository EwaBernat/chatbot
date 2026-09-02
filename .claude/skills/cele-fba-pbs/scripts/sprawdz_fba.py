#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kontrola spójności modułu FBA/PBS — jedno polecenie zamiast pięciu sprawdzeń.

Po każdej rozbudowie wracają te same pytania: czy każdy wskaźnik ma komplet celów,
czy każdy konspekt ma pomoc, czy każda pomoc ma zdjęcie i nagranie, czy któryś
arkusz nie czeka na nienarysowany symbol, czy w poleceniu do dziecka nie został
wyraz, którego przedszkolak nie rozumie.

Żadne z tych pytań nie zada się samo. Brak nie wysypuje budowania: karta bez
zdjęcia dostaje pole zastępcze, karta bez nagrania — wyłączony przycisk, arkusz
z brakującym symbolem jest po cichu pomijany. Dokument wygląda dobrze, a nauczyciel
dowiaduje się w sali, przy dziecku.

Skrypt niczego nie naprawia. Wypisuje stan i kończy się kodem 1, gdy znalazł brak
— dzięki temu nadaje się i do czytania, i do warunku w skrypcie.

Uruchomienie:  python3 .claude/skills/cele-fba-pbs/scripts/sprawdz_fba.py
               ... --korzen /sciezka/do/eduplaner_fba
               ... --cicho          # tylko problemy i podsumowanie
"""

from __future__ import annotations

import argparse
import os
import re
import sys

# Wyrazy, których przedszkolak nie rozumie — terminy dorosłego, które trafiły
# kiedyś do polecenia nagrywanego dla dziecka. Lista jest celowo krótka i twarda;
# nazwy przedmiotów ze stolika (minutnik, klepsydra) do niej nie należą, bo
# dziecko uczy się ich jak każdego innego słowa.
TRUDNE = ["strategi", "sygnał", "sekwencj", "komunikat", "instrukcj", "procedur",
          "technik", "regulacj", "identyfik", "alternatyw", "konsekwencj",
          "koncentr", "wizualiz", "termometr", "licznik"]
DLUGIE_ZDANIE = 14          # słów; powyżej tego polecenie robi się nie do powtórzenia


def znajdz_korzen(podany=None):
    """Katalog eduplaner_fba — podany, obok skilla albo w górę drzewa."""
    if podany:
        return os.path.abspath(podany)
    tu = os.path.abspath(__file__)
    for _ in range(8):
        tu = os.path.dirname(tu)
        kandydat = os.path.join(tu, "eduplaner_fba")
        if os.path.isdir(os.path.join(kandydat, "src")):
            return kandydat
    return None


def main():
    ap = argparse.ArgumentParser(description="Kontrola spójności modułu FBA/PBS")
    ap.add_argument("--korzen", help="katalog eduplaner_fba")
    ap.add_argument("--cicho", action="store_true", help="tylko problemy i podsumowanie")
    args = ap.parse_args()

    korzen = znajdz_korzen(args.korzen)
    if not korzen:
        print("Nie znalazłem katalogu eduplaner_fba. Podaj --korzen.")
        return 2
    sys.path.insert(0, os.path.join(korzen, "src"))

    import dane_poziomy as P
    import konspekty_fba as KF
    import pomoce_fba as PF
    import karta_pomocy as KP
    import symbole_fba as SF

    problemy = []
    mow = (lambda *a: None) if args.cicho else print

    def naglowek(t):
        mow(f"\n{t}\n" + "─" * len(t))

    # ——— cele ————————————————————————————————————————————————————————————
    naglowek("Cele SMART")
    funkcji, wskaznikow, celow = P.stan()
    mow(f"  {funkcji} funkcje · {wskaznikow} wskaźników · {celow} celów "
        f"({wskaznikow} × {len(P.POZIOMY)} poziomy × {len(P.WERSJE)} wersje)")
    oczekiwane = wskaznikow * len(P.POZIOMY) * len(P.WERSJE)
    if celow != oczekiwane:
        problemy.append(f"celów jest {celow}, a powinno {oczekiwane}")
    for rzym, f in P.CELE.items():
        for i, wsk in enumerate(f["wskazniki"], 1):
            nr = f"{rzym}.{i}"
            if not wsk.get("zastepcze"):
                problemy.append(f"{nr}: brak zachowania zastępczego")
            for kod_w, _n in P.WERSJE:
                teksty = wsk.get(kod_w) or ()
                if len(teksty) != len(P.POZIOMY) or not all(teksty):
                    problemy.append(f"{nr} wersja {kod_w}: niekompletne cele")

    # ——— konspekty ———————————————————————————————————————————————————————
    naglowek("Konspekty (KC-3)")
    klucze = KF.klucze()
    mow(f"  {len(klucze)} konspektów · rdzeni: {len(KF.RDZEN)}")
    for rzym, f in P.CELE.items():
        for i in range(1, len(f["wskazniki"]) + 1):
            nr = f"{rzym}.{i}"
            if nr not in KF.RDZEN:
                problemy.append(f"{nr}: brak konspektu (rdzenia)")
                continue
            for kod_w, _n in P.WERSJE:
                if (nr, kod_w) not in KF.WARIANTY:
                    problemy.append(f"{nr} wersja {kod_w}: brak wariantu konspektu")

    # ——— pomoce i nagrania ————————————————————————————————————————————————
    naglowek("Pomoce dydaktyczne (KC-4)")
    bez_zdjecia, bez_nagrania = KP.braki()
    mow(f"  {len(PF.POMOCE)} pomocy · {len(PF.POLECENIA)} poleceń")
    mow(f"  bez zdjęcia: {len(bez_zdjecia)} · bez nagrania: {len(bez_nagrania)}")
    for nr in bez_zdjecia:
        problemy.append(f"pomoc {nr}: brak zdjęcia")
    for nr, w in bez_nagrania:
        problemy.append(f"polecenie {w}{PF.kod(nr)}: brak nagrania")
    for nr in KF.RDZEN:
        if nr not in PF.POMOCE:
            problemy.append(f"{nr}: konspekt bez pomocy dydaktycznej")

    # ——— język poleceń ————————————————————————————————————————————————————
    naglowek("Język poleceń do dziecka")
    trudne, dlugie = [], []
    for (nr, w), tekst in sorted(PF.POLECENIA.items()):
        maly = tekst.lower()
        trafienia = [x for x in TRUDNE if x in maly]
        if trafienia:
            trudne.append((f"{w}{PF.kod(nr)}", trafienia, tekst))
        zdania = [z for z in re.split(r"[.!?]", tekst) if len(z.split()) > DLUGIE_ZDANIE]
        if zdania:
            dlugie.append((f"{w}{PF.kod(nr)}", len(zdania)))
    if trudne:
        for kod, trafienia, tekst in trudne:
            mow(f"  {kod}: {', '.join(trafienia)} — „{tekst}”")
            problemy.append(f"polecenie {kod}: trudne słowo ({', '.join(trafienia)})")
    else:
        mow("  bez trudnych słów")
    if dlugie:
        mow(f"  zdania dłuższe niż {DLUGIE_ZDANIE} słów: "
            + ", ".join(k for k, _ in dlugie))
        mow("  (to nie jest błąd — do rozważenia przy nagraniu, dziecko nie powtórzy"
            " długiego zdania)")

    # ——— symbole ——————————————————————————————————————————————————————————
    naglowek("Symbole na arkuszach")
    # `stan()` zwraca (przypisanych, z obrazkiem, pól celowo pustych). Puste pole
    # to nie brak: część kart ma miejsce, w które nauczyciel wkleja własny symbol.
    # Brakiem jest symbol przypisany, który nie ma pliku — arkusz go używający
    # zostaje wtedy po cichu pominięty.
    przypisanych, z_obrazkiem, puste_pola = SF.stan()
    mow(f"  {przypisanych} przypisanych · {z_obrazkiem} z obrazkiem "
        f"· {puste_pola} pól celowo pustych")
    if z_obrazkiem < przypisanych:
        problemy.append(f"{przypisanych - z_obrazkiem} symboli czeka na rysunek "
                        f"(dorysuj w bibliotece banku KPOF, nie tutaj)")

    # ——— podsumowanie —————————————————————————————————————————————————————
    print()
    if problemy:
        print(f"ZNALEZIONE BRAKI ({len(problemy)}):")
        for p in problemy:
            print(f"  • {p}")
        print("\nBrak nie wysypuje budowania — dokument złoży się i będzie wyglądał")
        print("dobrze. Uzupełnij, zanim materiał trafi do sali.")
        return 1
    print("Moduł FBA/PBS kompletny: cele, konspekty, pomoce, nagrania, symbole.")
    print("Zostaje pomiar druku:  node src/zmierz_konspekty.mjs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
