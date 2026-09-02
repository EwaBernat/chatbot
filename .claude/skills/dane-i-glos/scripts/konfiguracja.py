#!/usr/bin/env python3
"""Pamiec skilla `dane-i-glos` — identyfikatory glosu i awatara.

Skill zapamietuje raz ustalone identyfikatory, zeby nie trzeba ich bylo podawac
przy kazdym uruchomieniu. Plik lezy poza repozytorium (w katalogu domowym), wiec
nie trafia do gita nawet przez przypadek.

Nie trzymamy tu zadnych kluczy API — te zostaja w zmiennych srodowiskowych.
Identyfikator glosu nie jest tajemnica; klucz jest.

Kolejnosc pierwszenstwa w skryptach:
    argument wiersza polecen  >  zmienna srodowiskowa  >  ten plik  >  domyslna
"""

from __future__ import annotations

import json
import os
from pathlib import Path

SCIEZKA = Path(
    os.environ.get("DANE_I_GLOS_KONFIGURACJA")
    or Path.home() / ".config" / "dane-i-glos" / "konfiguracja.json"
)

KLUCZE_ZABRONIONE = ("api_key", "apikey", "klucz", "secret", "token")


def wczytaj() -> dict:
    try:
        dane = json.loads(SCIEZKA.read_text(encoding="utf-8"))
        return dane if isinstance(dane, dict) else {}
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as e:
        print(f"Uwaga: {SCIEZKA} jest uszkodzony ({e}). Pomijam.", file=__import__("sys").stderr)
        return {}


def zapisz(**pola) -> Path:
    """Dopisuje pola do konfiguracji, zachowujac te juz zapisane."""
    for nazwa in pola:
        if any(z in nazwa.lower() for z in KLUCZE_ZABRONIONE):
            raise ValueError(
                f"Odmawiam zapisania `{nazwa}` — kluczy API nie trzymamy w pliku. "
                "Uzyj zmiennej srodowiskowej."
            )
    dane = wczytaj()
    dane.update({k: v for k, v in pola.items() if v is not None})
    SCIEZKA.parent.mkdir(parents=True, exist_ok=True)
    SCIEZKA.write_text(json.dumps(dane, ensure_ascii=False, indent=2), encoding="utf-8")
    try:
        SCIEZKA.chmod(0o600)
    except OSError:
        pass
    return SCIEZKA


def ustal(z_wiersza, zmienna: str, klucz: str, domyslna=None):
    """Zwraca pierwsza niepusta wartosc wedlug kolejnosci pierwszenstwa."""
    if z_wiersza:
        return z_wiersza
    ze_srodowiska = os.environ.get(zmienna, "").strip()
    if ze_srodowiska:
        return ze_srodowiska
    z_pliku = wczytaj().get(klucz)
    if z_pliku:
        return z_pliku
    return domyslna


def opisz() -> str:
    dane = wczytaj()
    if not dane:
        return (f"Skill nie ma jeszcze zapamietanego glosu.\n"
                f"  (spodziewany plik: {SCIEZKA})\n"
                f"  Ustaw go: python3 skonfiguruj_glos.py <plik audio lub wideo>")
    linie = [f"Zapamietane w {SCIEZKA}:"]
    etykiety = {
        "elevenlabs_voice_id": "glos ElevenLabs",
        "elevenlabs_voice_name": "  nazwa",
        "elevenlabs_model": "model mowy",
        "elevenlabs_styl": "styl narracji",
        "heygen_avatar_id": "awatar HeyGen",
        "heygen_voice_id": "glos HeyGen",
        "utworzono": "zapisano",
    }
    for klucz, wartosc in dane.items():
        linie.append(f"  {etykiety.get(klucz, klucz):<18} {wartosc}")
    return "\n".join(linie)


if __name__ == "__main__":
    print(opisz())
