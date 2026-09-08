#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kontrola spójności banku celów SMART — jedno polecenie zamiast dziesięciu.

Po każdej rozbudowie trzeba odpowiedzieć na te same pytania: czy każdy konspekt
ma materiał, czy każda karta pomocy ma zdjęcie i nagranie, czy któryś arkusz nie
czeka na nienarysowany symbol, czy podstawa nadal jest pokryta w 113/113. Ręczne
sprawdzanie tego w kilku miejscach kończy się przeoczeniem — a przeoczony brak
nie wysypuje budowania, tylko po cichu pomija arkusz i nauczyciel zostaje bez
materiału.

Skrypt niczego nie naprawia. Wypisuje stan i kończy się kodem 1, gdy znalazł
brak — dzięki temu nadaje się i do czytania, i do warunku w skrypcie.

Uruchomienie:  python3 .claude/skills/bank-celow-smart/scripts/sprawdz_bank.py
               ... --korzen /sciezka/do/eduplaner_przedszkole
"""

from __future__ import annotations

import argparse
import os
import sys
from collections import Counter


def znajdz_korzen(podany=None):
    """Katalog eduplaner_przedszkole — podany, obok skilla albo w górę drzewa."""
    if podany:
        return os.path.abspath(podany)
    tu = os.path.abspath(__file__)
    for _ in range(8):
        tu = os.path.dirname(tu)
        kandydat = os.path.join(tu, "eduplaner_przedszkole")
        if os.path.isdir(os.path.join(kandydat, "src")):
            return kandydat
    return None


def main():
    ap = argparse.ArgumentParser(description="Kontrola spójności banku celów SMART")
    ap.add_argument("--korzen", help="katalog eduplaner_przedszkole")
    ap.add_argument("--cicho", action="store_true", help="tylko problemy i podsumowanie")
    args = ap.parse_args()

    korzen = znajdz_korzen(args.korzen)
    if not korzen:
        print("Nie znalazłem katalogu eduplaner_przedszkole. Podaj --korzen.")
        return 2
    sys.path.insert(0, os.path.join(korzen, "src"))

    import build, karty_druk, symbole
    import pomoce_a, pomoce_b, pomoce_c, pomoce_u

    problemy = []
    mow = (lambda *a: None) if args.cicho else print

    def naglowek(t):
        mow(f"\n{t}\n" + "─" * len(t))

    # ——— konspekty ———————————————————————————————————————————————————————
    naglowek("KONSPEKTY")
    per_wersja = Counter(w for w, _ in build.KONSPEKTY)
    mow(f"  razem: {len(build.KONSPEKTY)} · " +
        " · ".join(f"{w} {per_wersja[w]}" for w in sorted(per_wersja)))

    bez_materialu = [K["nr"] for K in build.KONSPEKTY.values()
                     if not karty_druk.ma_karty(K["nr"])]
    mow(f"  z materiałem do wydruku: {len(build.KONSPEKTY) - len(bez_materialu)}"
        f" / {len(build.KONSPEKTY)}")
    if bez_materialu:
        problemy.append(f"{len(bez_materialu)} konspektów bez materiału do wydruku: "
                        + ", ".join(sorted(bez_materialu)[:12]))

    # Konspekt musi wisieć przy istniejącym twierdzeniu — literówka w kluczu
    # nie wysypuje budowania, tylko cicho gubi konspekt.
    numery = {(m.WERSJA["kod"], it["n"]) for m in build.WERSJE
              for a in m.AREAS for it in a["items"]}
    sieroty = [f"{w}/{n}" for (w, n) in build.KONSPEKTY if (w, n) not in numery]
    if sieroty:
        problemy.append("konspekty przy nieistniejących twierdzeniach: " + ", ".join(sieroty))

    # ——— arkusze i symbole ————————————————————————————————————————————————
    naglowek("ARKUSZE DO WYDRUKU I SYMBOLE")
    gotowych, wszystkich, narysowanych, symboli = karty_druk.stan()
    mow(f"  arkusze gotowe do złożenia: {gotowych} / {wszystkich}")
    mow(f"  symbole narysowane: {narysowanych} / {symboli}")
    if gotowych < wszystkich:
        czekaja = {s for nr in karty_druk.ARKUSZE for a in karty_druk.ARKUSZE[nr]
                   for s in (a.get("symbole") or []) if not symbole.jest(s)}
        problemy.append(f"{wszystkich - gotowych} arkuszy pomijanych przy budowaniu — "
                        f"czekają na symbole: " + ", ".join(sorted(czekaja)[:12]))

    # Symbol używany w arkuszu, ale nieopisany w bibliotece — arkusz zniknie
    # bez śladu, bo `jest()` nie ma czego szukać.
    uzyte = {s for nr in karty_druk.ARKUSZE for a in karty_druk.ARKUSZE[nr]
             for s in (a.get("symbole") or [])}
    obce = sorted(uzyte - set(symbole.SYMBOLE))
    if obce:
        problemy.append("symbole użyte w arkuszach, ale nieopisane w symbole.py: "
                        + ", ".join(obce[:12]))
    osierocone = sorted(set(symbole.SYMBOLE) - uzyte)
    if osierocone and not args.cicho:
        mow(f"  symbole w bibliotece, których nie używa żaden arkusz: {len(osierocone)}"
            + (" (" + ", ".join(osierocone[:6]) + "…)" if osierocone else ""))

    # ——— karty pomocy ————————————————————————————————————————————————————
    naglowek("KARTY POMOCY DYDAKTYCZNEJ")
    for kod, Z in (("A", pomoce_a.ZESTAW), ("B", pomoce_b.ZESTAW),
                   ("C", pomoce_c.ZESTAW), ("U", pomoce_u.ZESTAW)):
        bez_foto = [k for k in Z.pomoce if not Z.ma_foto(k)]
        bez_audio = [k for k in Z.pomoce if not Z.ma_dzwiek(k)]
        mow(f"  {kod} · {Z.wiek:<14} {len(Z.pomoce):>3} kart"
            f" · bez zdjęcia {len(bez_foto)} · bez nagrania {len(bez_audio)}")
        if bez_foto:
            problemy.append(f"wersja {kod}: {len(bez_foto)} kart bez zdjęcia — "
                            + ", ".join(bez_foto[:8]))
        if bez_audio:
            problemy.append(f"wersja {kod}: {len(bez_audio)} kart bez nagrania — "
                            + ", ".join(bez_audio[:8]))

    # ——— podstawa programowa ——————————————————————————————————————————————
    naglowek("PODSTAWA PROGRAMOWA 2026")
    punkty = set()
    for m in build.WERSJE:
        for a in m.AREAS:
            for it in a["items"]:
                for kod in it["pp"].replace("PP ", "").split("·"):
                    kod = kod.strip()
                    if kod and kod[0].isdigit() and "." in kod:
                        punkty.add(kod)
    mow(f"  punktów osiągnięć pokrytych celami: {len(punkty)} ze 113")
    if len(punkty) < 113:
        problemy.append(f"podstawa pokryta w {len(punkty)}/113 — brakuje "
                        f"{113 - len(punkty)} punktów")

    # ——— podsumowanie ————————————————————————————————————————————————————
    print("\n" + "═" * 66)
    if problemy:
        print(f"ZNALEZIONE BRAKI: {len(problemy)}")
        for p in problemy:
            print(f"  ✗ {p}")
        print("\nDopóki brak istnieje, dokumenty zbudują się poprawnie, ale bez tego\n"
              "elementu — nauczyciel zostanie bez materiału, nie zobaczywszy błędu.")
        return 1
    print("BANK SPÓJNY — każdy konspekt ma materiał, każda karta zdjęcie i nagranie,")
    print("każdy arkusz komplet symboli, podstawa pokryta w 113/113.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
