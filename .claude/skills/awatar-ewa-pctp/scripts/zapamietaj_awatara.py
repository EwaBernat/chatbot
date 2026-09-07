#!/usr/bin/env python3
"""Zapamietuje awatara Ewa PCTP w HeyGen, zeby skille uzywaly go bez przelacznikow.

Zapisuje `heygen_avatar_id` (i opcjonalnie glos HeyGen) w tej samej pamieci, z ktorej
korzysta skill `dane-i-glos` (`~/.config/dane-i-glos/konfiguracja.json`, poza repozytorium).
Od tej chwili `heygen_awatar.py` bierze awatara Ewy sam.

Kluczy API ten plik nie przyjmuje — te zostaja w zmiennych srodowiskowych.

Przyklady:
    python3 zapamietaj_awatara.py --szukaj Ewa          # znajdz i zapamietaj (przez skill awatar-ewa; wymaga HEYGEN_API_KEY)
    python3 zapamietaj_awatara.py --avatar-id <id>      # zapamietaj
    python3 zapamietaj_awatara.py --pokaz
    python3 zapamietaj_awatara.py --zapomnij
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

SKRYPTY_DANE_I_GLOS = Path(__file__).resolve().parents[2] / "dane-i-glos" / "scripts"
SKONFIGURUJ_AWATARA = Path(__file__).resolve().parents[2] / "awatar-ewa" / "scripts" / "skonfiguruj_awatara.py"
sys.path.insert(0, str(SKRYPTY_DANE_I_GLOS))
import konfiguracja                                    # noqa: E402

POLA = ("heygen_avatar_id", "heygen_avatar_name", "heygen_voice_id", "postac")


def main() -> int:
    ap = argparse.ArgumentParser(description="Zapamietaj awatara Ewy (HeyGen) w pamieci skilli.")
    ap.add_argument("--avatar-id", help="identyfikator awatara z konta HeyGen")
    ap.add_argument("--nazwa", default="Ewa PCTP", help="nazwa awatara, jak na koncie HeyGen")
    ap.add_argument("--voice-id", help="glos HeyGen (tylko gdy nie ma klonu w ElevenLabs)")
    ap.add_argument("--szukaj", metavar="FRAZA",
                    help="wypisz awatary z konta HeyGen pasujace do frazy i zakoncz")
    ap.add_argument("--pokaz", action="store_true", help="pokaz, co skill pamieta, i zakoncz")
    ap.add_argument("--zapomnij", action="store_true", help="usun zapamietanego awatara")
    a = ap.parse_args()

    if a.pokaz:
        print(konfiguracja.opisz())
        return 0
    if a.szukaj:
        if SKONFIGURUJ_AWATARA.exists():
            # skill awatar-ewa: wypisuje awatary i glosy, sprawdza siec, przy jednym trafieniu
            # zapisuje od razu — ta sama pamiec, wiec wynik sluzy obu skillom
            return subprocess.run([sys.executable, str(SKONFIGURUJ_AWATARA),
                                   "--szukaj", a.szukaj]).returncode
        skrypt = SKRYPTY_DANE_I_GLOS / "heygen_awatar.py"
        return subprocess.run([sys.executable, str(skrypt), "--awatary", "--szukaj", a.szukaj]).returncode
    if a.zapomnij:
        dane = konfiguracja.wczytaj()
        for k in POLA:
            dane.pop(k, None)
        konfiguracja.SCIEZKA.parent.mkdir(parents=True, exist_ok=True)
        konfiguracja.SCIEZKA.write_text(json.dumps(dane, ensure_ascii=False, indent=2),
                                        encoding="utf-8")
        print("Zapomniane. Awatar na koncie HeyGen zostaje nietkniety.")
        return 0
    if not a.avatar_id:
        ap.error("podaj --avatar-id (albo --szukaj / --pokaz / --zapomnij)")

    sciezka = konfiguracja.zapisz(
        heygen_avatar_id=a.avatar_id.strip(),
        heygen_avatar_name=a.nazwa,
        heygen_voice_id=a.voice_id.strip() if a.voice_id else None,
        postac="Ewa PCTP",
        awatar_zapisano=date.today().isoformat(),
    )
    print(f"Zapamietane w {sciezka}.\n"
          f"  awatar HeyGen: {a.nazwa} ({a.avatar_id})\n"
          "Od teraz heygen_awatar.py i wstaw_ewe.py nie potrzebuja --avatar-id.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
