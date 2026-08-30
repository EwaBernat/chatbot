#!/usr/bin/env python3
"""Jedno polecenie, zeby skill zapamietal Twoj glos.

Bierze nagrania (albo film — sam wyciagnie sciezke dzwiekowa), sprawdza je,
klonuje glos w ElevenLabs i zapisuje `voice_id` w konfiguracji skilla. Od tej
chwili `elevenlabs_tts.py` uzywa Twojego glosu bez zadnych przelacznikow.

Klucz API: zmienna srodowiskowa ELEVENLABS_API_KEY (uprawnienie voices_write).
Zaleznosci: biblioteka standardowa; do filmow potrzebny ffmpeg.

Przyklady:
    python3 skonfiguruj_glos.py nagranie.mp4
    python3 skonfiguruj_glos.py probka1.wav probka2.wav --nazwa "Ewa - narracja PL"
    python3 skonfiguruj_glos.py --pokaz
    python3 skonfiguruj_glos.py --voice-id abc123 --nazwa "Ewa - narracja PL"
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import konfiguracja                                    # noqa: E402
from elevenlabs_klon_glosu import (                    # noqa: E402
    sprawdz_nagrania, zbuduj_multipart, zapytaj, klucz,
)

WIDEO = (".mp4", ".mov", ".mkv", ".webm", ".avi", ".m4v")


# --- kontrola srodowiska ---------------------------------------------------

def znajdz_ffmpeg() -> str | None:
    if szukany := shutil.which("ffmpeg"):
        return szukany
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return None


def siec_przepuszcza() -> tuple[bool, str]:
    """Odroznia blokade sieciowa od problemu z kluczem — te bledy wygladaja tak samo."""
    try:
        urllib.request.urlopen("https://api.elevenlabs.io/", timeout=10)
        return True, ""
    except urllib.error.HTTPError:
        return True, ""                                 # serwer odpowiedzial, wiec siec dziala
    except urllib.error.URLError as e:
        return False, str(e.reason)
    except Exception as e:
        return False, str(e)


def wyciagnij_dzwiek(film: Path, katalog: Path) -> Path:
    ffmpeg = znajdz_ffmpeg()
    if not ffmpeg:
        raise SystemExit(
            f"`{film.name}` to film, a do wyciagniecia dzwieku potrzebny jest ffmpeg.\n"
            "  Zainstaluj: pip install imageio-ffmpeg   (albo systemowy ffmpeg)\n"
            "  Albo podaj gotowy plik audio."
        )
    wyjscie = katalog / f"{film.stem}.wav"
    print(f"Wyciagam sciezke dzwiekowa z {film.name}...", file=sys.stderr)
    wynik = subprocess.run(
        [ffmpeg, "-hide_banner", "-loglevel", "error", "-y", "-i", str(film),
         "-vn", "-ac", "1", "-ar", "44100", "-c:a", "pcm_s16le", str(wyjscie)],
        capture_output=True, text=True,
    )
    if wynik.returncode != 0 or not wyjscie.exists():
        raise SystemExit(f"Nie udalo sie wyciagnac dzwieku z {film.name}:\n{wynik.stderr[:400]}")
    return wyjscie


# --- klonowanie ------------------------------------------------------------

def sklonuj(nazwa: str, pliki: list[Path], opis: str | None, odszum: bool) -> dict:
    pola = {"name": nazwa,
            "labels": json.dumps({"language": "pl", "use_case": "narration"},
                                 ensure_ascii=False)}
    if opis:
        pola["description"] = opis
    if odszum:
        pola["remove_background_noise"] = "true"
    cialo, typ = zbuduj_multipart(pola, pliki)
    print(f"Wysylam {len(pliki)} plikow ({len(cialo) / 1_048_576:.2f} MB) do ElevenLabs...",
          file=sys.stderr)
    return zapytaj("/v1/voices/add", metoda="POST", cialo=cialo, typ_tresci=typ)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Zapamietuje Twoj glos w skillu dane-i-glos (jedno polecenie).")
    ap.add_argument("nagrania", nargs="*", type=Path,
                    help="pliki audio lub wideo z Twoim glosem")
    ap.add_argument("--nazwa", default="Moj glos - narracja PL")
    ap.add_argument("--opis", help="krotki opis glosu")
    ap.add_argument("--odszum", action="store_true",
                    help="popros o usuniecie szumu tla (tylko gdy nagranie szumi)")
    ap.add_argument("--pokaz", action="store_true",
                    help="pokaz, co skill juz pamieta, i zakoncz")
    ap.add_argument("--zapomnij", action="store_true",
                    help="usun zapamietany glos z konfiguracji")
    ap.add_argument("--tylko-sprawdz", action="store_true",
                    help="sprawdz nagrania i zakoncz — nic nie zostanie wyslane")
    ap.add_argument("--voice-id",
                    help="zapamietaj glos juz sklonowany na koncie ElevenLabs, "
                         "bez wysylania nagran (voice_id z panelu albo z --glosy)")
    a = ap.parse_args()

    if a.pokaz:
        print(konfiguracja.opisz())
        return 0
    if a.zapomnij:
        dane = konfiguracja.wczytaj()
        for k in ("elevenlabs_voice_id", "elevenlabs_voice_name"):
            dane.pop(k, None)
        konfiguracja.SCIEZKA.parent.mkdir(parents=True, exist_ok=True)
        konfiguracja.SCIEZKA.write_text(json.dumps(dane, ensure_ascii=False, indent=2),
                                        encoding="utf-8")
        print("Zapomniane. Nagrania na dysku i glos na koncie ElevenLabs zostaja nietkniete.")
        return 0
    if a.voice_id:
        # Glos jest juz na koncie — zapamietujemy sam identyfikator. Zadne nagrania
        # nie wychodza z komputera i nie powstaje drugi klon tego samego glosu.
        if a.nagrania:
            ap.error("--voice-id i nagrania wykluczaja sie: albo klonujemy, albo "
                     "zapamietujemy gotowy glos")
        sciezka = konfiguracja.zapisz(
            elevenlabs_voice_id=a.voice_id.strip(),
            elevenlabs_voice_name=a.nazwa,
            utworzono=str(date.today()),
        )
        print(f"Skill pamieta juz Twoj glos.\n"
              f"  nazwa:    {a.nazwa}\n"
              f"  voice_id: {a.voice_id.strip()}\n"
              f"  zapisane: {sciezka}")
        return 0
    if not a.nagrania:
        ap.error("podaj pliki z nagraniami (albo --voice-id / --pokaz / --zapomnij)")

    with tempfile.TemporaryDirectory() as tymczasowy:
        katalog = Path(tymczasowy)
        pliki: list[Path] = []
        for sciezka in a.nagrania:
            if not sciezka.exists():
                print(f"Nie ma pliku: {sciezka}", file=sys.stderr)
                return 1
            pliki.append(wyciagnij_dzwiek(sciezka, katalog)
                         if sciezka.suffix.lower() in WIDEO else sciezka)

        print("\nKontrola nagran:\n")
        ok, _ = sprawdz_nagrania(pliki)
        if not ok:
            print("\nNie wysylam — popraw powyzsze bledy.", file=sys.stderr)
            return 1
        if a.tylko_sprawdz:
            print("\n(--tylko-sprawdz: nic nie zostalo wyslane)")
            return 0

        klucz()                                        # czytelny blad, gdy brak klucza
        dziala, powod = siec_przepuszcza()
        if not dziala:
            print(f"\nSiec nie przepuszcza polaczen do api.elevenlabs.io ({powod}).\n"
                  "To blokada srodowiska, nie problem z kluczem — klonowanie tutaj sie nie uda.\n"
                  "Uruchom to polecenie na wlasnym komputerze albo zmien polityke sieciowa.",
                  file=sys.stderr)
            return 3

        print()
        odp = sklonuj(a.nazwa, pliki, a.opis, a.odszum)

    voice_id = odp.get("voice_id")
    if not voice_id:
        print(f"ElevenLabs nie zwrocil voice_id: {json.dumps(odp, ensure_ascii=False)[:400]}",
              file=sys.stderr)
        return 1

    sciezka = konfiguracja.zapisz(
        elevenlabs_voice_id=voice_id,
        elevenlabs_voice_name=a.nazwa,
        utworzono=str(date.today()),
    )
    print(f"\nGotowe. Skill pamieta juz Twoj glos.\n"
          f"  nazwa:    {a.nazwa}\n"
          f"  voice_id: {voice_id}\n"
          f"  zapisane: {sciezka}")
    if odp.get("requires_verification"):
        print("\n  UWAGA: ElevenLabs wymaga weryfikacji tego glosu przed uzyciem.\n"
              "  Wejdz na elevenlabs.io -> Voices -> ten glos i przejdz weryfikacje.")
    print(f"\nOd teraz wystarczy:\n"
          f"  python3 elevenlabs_tts.py narracja.txt -o nagranie.mp3\n"
          f"— bez podawania glosu. Sprawdzic, co skill pamieta: --pokaz")
    return 0


if __name__ == "__main__":
    sys.exit(main())
