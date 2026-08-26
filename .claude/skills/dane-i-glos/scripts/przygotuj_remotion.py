#!/usr/bin/env python3
"""Sklada projekt Remotion z danych, narracji i napisow — skill `dane-i-glos`.

Bierze trzy rzeczy, ktore powstaly we wczesniejszych etapach:
  * profil danych z `dane_do_narracji.py --json` (liczby do wykresu),
  * scenariusz narracji `.txt` (podzial na sceny wedlug akapitow),
  * nagranie `.mp3` i napisy `.srt` z `elevenlabs_tts.py` (dzwiek i czasy),
i buduje gotowy do renderu katalog Remotion.

Granice scen wypadaja tam, gdzie konczy sie akapit narracji: skrypt dzieli czas
proporcjonalnie do dlugosci akapitow, a potem dosuwa kazda granice do najblizszego
konca napisu, zeby scena nie zmieniala sie w polowie zdania.

Zaleznosci: tylko biblioteka standardowa.

Przyklad:
    python3 dane_do_narracji.py dane.csv --grupuj klasa --agreguj frekwencja_proc --json > profil.json
    python3 elevenlabs_tts.py narracja.txt -o narracja.mp3 --srt napisy.srt
    python3 przygotuj_remotion.py film/ --profil profil.json --narracja narracja.txt \\
            --audio narracja.mp3 --napisy napisy.srt --tytul "Frekwencja — I półrocze"
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

SZABLON = Path(__file__).resolve().parent.parent / "assets" / "remotion"
TYPY_SCEN = ("tytul", "liczba", "wykres", "wniosek")
CZAS_SRT = re.compile(r"(\d{2}):(\d{2}):(\d{2})[,.](\d{3})")


# --- wejscie ---------------------------------------------------------------

def czytaj_napisy(sciezka: Path) -> list[tuple[float, float, str]]:
    """Zwraca listę (od, do, tekst) w sekundach."""
    napisy = []
    for blok in sciezka.read_text(encoding="utf-8").replace("\r\n", "\n").strip().split("\n\n"):
        linie = [l for l in blok.split("\n") if l.strip()]
        linijka = next((l for l in linie if "-->" in l), None)
        if not linijka:
            continue
        znaczniki = CZAS_SRT.findall(linijka)
        if len(znaczniki) < 2:
            continue
        na_sek = lambda z: int(z[0]) * 3600 + int(z[1]) * 60 + int(z[2]) + int(z[3]) / 1000
        tekst = " ".join(linie[linie.index(linijka) + 1:]).strip()
        napisy.append((na_sek(znaczniki[0]), na_sek(znaczniki[1]), tekst))
    return napisy


def akapity(sciezka: Path) -> list[str]:
    tresc = sciezka.read_text(encoding="utf-8").strip()
    return [a.strip() for a in re.split(r"\n\s*\n", tresc) if a.strip()]


def granice_scen(akapity_: list[str], napisy, calosc: float) -> list[tuple[float, float]]:
    """Dzieli czas proporcjonalnie do długości akapitów, potem dosuwa do napisów."""
    znaki = [len(a) for a in akapity_]
    suma = sum(znaki) or 1
    granice, biezaca = [0.0], 0.0
    for z in znaki[:-1]:
        biezaca += calosc * z / suma
        granice.append(biezaca)
    granice.append(calosc)

    if napisy:
        konce = [n[1] for n in napisy]
        # pierwsza granica zostaje w zerze, ostatnia na końcu nagrania
        for i in range(1, len(granice) - 1):
            granice[i] = min(konce, key=lambda k: abs(k - granice[i]))
        # granice muszą rosnąć nawet po dosunięciu
        for i in range(1, len(granice)):
            if granice[i] <= granice[i - 1]:
                granice[i] = granice[i - 1] + 0.5
        granice[-1] = max(granice[-1], calosc)
    return list(zip(granice[:-1], granice[1:]))


# --- budowa scen -----------------------------------------------------------

def slupki_z_profilu(profil: dict) -> tuple[list[dict], str, str | None]:
    """Wyciąga słupki z sekcji `grupy` profilu. Zwraca (słupki, jednostka, do_wyróżnienia)."""
    grupy = profil.get("grupy")
    if not grupy or not grupy.get("pozycje"):
        return [], "", None
    klucz = "srednia" if any("srednia" in p for p in grupy["pozycje"]) else "liczebnosc"
    slupki = [
        {"etykieta": str(p["grupa"]), "wartosc": round(float(p[klucz]), 1)}
        for p in grupy["pozycje"] if klucz in p
    ]
    slupki.sort(key=lambda s: -s["wartosc"])
    jednostka = "%" if "proc" in (grupy.get("agreguj") or "").lower() else ""
    najnizszy = slupki[-1]["etykieta"] if slupki else None
    return slupki, jednostka, najnizszy


def zbuduj_sceny(a, akapity_, przedzialy, profil) -> list[dict]:
    typy = [t.strip() for t in a.typy.split(",")]
    if len(typy) < len(akapity_):
        typy += ["wniosek"] * (len(akapity_) - len(typy))

    slupki, jednostka, najnizszy = slupki_z_profilu(profil)
    sceny = []
    for i, (akapit, (od, do)) in enumerate(zip(akapity_, przedzialy)):
        typ = typy[i] if typy[i] in TYPY_SCEN else "wniosek"
        wspolne = {"typ": typ, "odSek": round(od, 2), "doSek": round(do, 2)}

        if typ == "tytul":
            sceny.append({**wspolne,
                          "tytul": a.tytul or akapit.split(".")[0],
                          "podtytul": a.podtytul or ""})
        elif typ == "liczba":
            sceny.append({**wspolne,
                          "wartosc": a.liczba or "—",
                          "opis": a.opis or akapit.split(".")[0],
                          "kontekst": a.kontekst or ""})
        elif typ == "wykres":
            if not slupki:
                print("Uwaga: profil nie ma sekcji `grupy`, wiec wykres bedzie pusty.\n"
                      "  Uruchom profiler z --grupuj i --agreguj.", file=sys.stderr)
            sceny.append({**wspolne,
                          "tytul": a.tytul_wykresu or "Podzial wedlug grup",
                          "jednostka": jednostka,
                          "slupki": slupki,
                          "wyroznij": a.wyroznij or najnizszy,
                          **({"maks": 100} if jednostka == "%" else {})})
        else:
            sceny.append({**wspolne, "tekst": akapit.replace("\n", " ")})
    return sceny


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Sklada projekt Remotion z danych, narracji i napisow.")
    ap.add_argument("katalog", type=Path, help="dokad zlozyc projekt")
    ap.add_argument("--profil", type=Path, required=True,
                    help="JSON z dane_do_narracji.py --json")
    ap.add_argument("--narracja", type=Path, required=True, help="scenariusz .txt")
    ap.add_argument("--audio", type=Path, help="nagranie .mp3")
    ap.add_argument("--napisy", type=Path, help="napisy .srt")
    ap.add_argument("--tytul", help="tytul filmu")
    ap.add_argument("--podtytul", help="podtytul sceny tytulowej")
    ap.add_argument("--liczba", help="glowna liczba, np. \"85%%\"")
    ap.add_argument("--opis", help="podpis pod glowna liczba")
    ap.add_argument("--kontekst", help="drobny podpis pod opisem")
    ap.add_argument("--tytul-wykresu", dest="tytul_wykresu")
    ap.add_argument("--wyroznij", help="etykieta slupka do wyroznienia "
                                       "(domyslnie najnizsza wartosc)")
    ap.add_argument("--stopka", default="PCTP Koszalin · EduPlaner 2026")
    ap.add_argument("--typy", default="tytul,liczba,wykres,wniosek",
                    help="typy scen po przecinku, po jednym na akapit narracji")
    ap.add_argument("--nadpisz", action="store_true",
                    help="nadpisz istniejacy katalog projektu")
    a = ap.parse_args()

    for etykieta, sciezka in (("profil", a.profil), ("narracja", a.narracja),
                              ("audio", a.audio), ("napisy", a.napisy)):
        if sciezka and not sciezka.exists():
            print(f"Nie ma pliku ({etykieta}): {sciezka}", file=sys.stderr)
            return 1
    if not SZABLON.exists():
        print(f"Brak szablonu Remotion: {SZABLON}", file=sys.stderr)
        return 1

    profil = json.loads(a.profil.read_text(encoding="utf-8"))
    akapity_ = akapity(a.narracja)
    if not akapity_:
        print("Scenariusz jest pusty.", file=sys.stderr)
        return 2

    napisy = czytaj_napisy(a.napisy) if a.napisy else []
    calosc = napisy[-1][1] if napisy else len(a.narracja.read_text(
        encoding="utf-8").split()) / 150 * 60
    przedzialy = granice_scen(akapity_, napisy, calosc)

    if a.katalog.exists() and not a.nadpisz:
        print(f"Katalog `{a.katalog}` juz istnieje. Uzyj --nadpisz albo wskaz inny.",
              file=sys.stderr)
        return 1
    if a.katalog.exists():
        shutil.rmtree(a.katalog)
    shutil.copytree(SZABLON, a.katalog,
                    ignore=shutil.ignore_patterns("node_modules", "out", "film.json"))

    publiczne = a.katalog / "public"
    publiczne.mkdir(exist_ok=True)
    film = {
        "tytul": a.tytul or "Raport z danych",
        "stopka": a.stopka,
        "sceny": zbuduj_sceny(a, akapity_, przedzialy, profil),
    }
    if a.audio:
        shutil.copy(a.audio, publiczne / a.audio.name)
        film["audio"] = a.audio.name
    if a.napisy:
        shutil.copy(a.napisy, publiczne / a.napisy.name)
        film["napisy"] = a.napisy.name
    (publiczne / "film.json").write_text(
        json.dumps(film, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Projekt zlozony w: {a.katalog}")
    print(f"  scen: {len(film['sceny'])}, dlugosc: {calosc:.1f} s")
    for s in film["sceny"]:
        print(f"    {s['odSek']:>6.1f}–{s['doSek']:>6.1f} s  {s['typ']}")
    print(f"\nPodejrzyj i popraw tresc scen: {publiczne / 'film.json'}")
    print(f"\nDalej:\n  cd {a.katalog}\n  npm install\n  npx remotion studio"
          f"        # podglad na zywo\n"
          f"  npx remotion render RaportWideo out/film.mp4")
    return 0


if __name__ == "__main__":
    sys.exit(main())
