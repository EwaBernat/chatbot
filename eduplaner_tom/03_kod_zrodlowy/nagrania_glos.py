#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Nagrania poleceń dla dziecka — 75 plików MP3 głosem autorki.

Buduje manifest nagrań z `pomoce_tom.json` i — na żądanie — generuje pliki MP3
przez ElevenLabs, wyłącznie z klonu głosu autorki wskazanego w ELEVENLABS_VOICE_ID.

    python3 03_kod_zrodlowy/nagrania_glos.py --manifest
    python3 03_kod_zrodlowy/nagrania_glos.py --suchy-bieg
    export ELEVENLABS_API_KEY="..."  ELEVENLABS_VOICE_ID="<klon głosu autorki>"
    python3 03_kod_zrodlowy/nagrania_glos.py --generuj

GŁOS JEST DANĄ BIOMETRYCZNĄ. Pliki z katalogu audio_tom/ to sklonowany głos
autorki: nie publikuj ich i nie używaj poza uzgodnionym zastosowaniem w
aplikacji. Skrypt celowo NIE MA głosu domyślnego — brak ELEVENLABS_VOICE_ID
zatrzymuje pracę, zamiast podstawić cudzy głos.

Nagrywane są wyłącznie teksty `polecenie_dla_dziecka`. Instrukcji słownych
dorosłego, opisów i wskazówek się NIE nagrywa — to teksty dla nauczyciela.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import shutil
import subprocess
import sys
import urllib.error
import urllib.request

KORZEN = pathlib.Path(__file__).resolve().parent.parent
POMOCE = KORZEN / "01_dane_json" / "pomoce_tom.json"
MANIFEST = KORZEN / "01_dane_json" / "nagrania_tom.json"

API = "https://api.elevenlabs.io"
MODEL = "eleven_multilingual_v2"          # najlepszy dla polszczyzny
FORMAT_ZRODLOWY = "mp3_44100_64"
BITRATE_DOCELOWY = "40k"                  # 40 kbps mono — głośnik tabletu w sali
TIMEOUT = 180


def wpisy() -> list[dict]:
    """75 nagrań: 21 pomocy × 3 wersje wiekowe. Nagrywamy WYŁĄCZNIE
    `polecenie_dla_dziecka` — instrukcji dla nauczyciela się nie nagrywa."""
    if not POMOCE.exists():
        raise SystemExit(f"Brak {POMOCE}. Uruchom najpierw: python3 03_kod_zrodlowy/eksport_json.py")
    dane = json.loads(POMOCE.read_text(encoding="utf-8"))
    lista = []
    for pomoc in dane["pomoce"]:
        for wersja, pol in pomoc["polecenia"].items():
            lista.append({
                "wskaznik": pomoc["wskaznik"],
                "wersja_wiekowa": wersja,
                "wiek": pol["wiek"],
                "pomoc": pomoc["nazwa"],
                "tekst": pol["polecenie_dla_dziecka"],
                "plik": pol["nagranie"],
                "czyta": "sklonowany głos autorki (dana biometryczna)",
            })
    return lista


def zapisz_manifest(lista: list[dict]) -> None:
    MANIFEST.write_text(json.dumps({
        "opis": ("Manifest nagrań poleceń dla dziecka — teoria umysłu (ToM). Ścieżki liczone od katalogu 04_media/, tak jak w module ABC/FBA."),
        "uwaga_prawna": (
            "Pliki audio to sklonowany głos autorki. Głos jest daną biometryczną: nie publikuj "
            "nagrań i nie używaj ich poza uzgodnionym zastosowaniem w aplikacji EduPlaner 2026."
        ),
        "parametry": {"model": MODEL, "format_zrodlowy": FORMAT_ZRODLOWY, "bitrate_docelowy": BITRATE_DOCELOWY,
                      "kanaly": "mono"},
        "liczba_nagran": len(lista),
        "nagrania": lista,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"zapisano {MANIFEST.relative_to(KORZEN)} ({len(lista)} nagrań)")


def klucz_i_glos() -> tuple[str, str]:
    klucz = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    glos = os.environ.get("ELEVENLABS_VOICE_ID", "").strip()
    if not klucz:
        raise SystemExit('Brak klucza. export ELEVENLABS_API_KEY="..."')
    if not glos:
        raise SystemExit(
            'Brak głosu autorki. export ELEVENLABS_VOICE_ID="<id klonu głosu autorki>"\n'
            "Skrypt nie podstawia cudzego głosu — nagrania mają być w jednym, znanym dziecku głosie."
        )
    return klucz, glos


def synteza(tekst: str, klucz: str, glos: str) -> bytes:
    cialo = json.dumps({
        "text": tekst,
        "model_id": MODEL,
        "voice_settings": {"stability": 0.55, "similarity_boost": 0.85, "style": 0.15},
    }).encode("utf-8")
    req = urllib.request.Request(
        f"{API}/v1/text-to-speech/{glos}?output_format={FORMAT_ZRODLOWY}",
        data=cialo,
        headers={"xi-api-key": klucz, "content-type": "application/json", "accept": "audio/mpeg"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as odp:
            return odp.read()
    except urllib.error.HTTPError as e:
        raise SystemExit(f"ElevenLabs {e.code}: {e.read().decode('utf-8', 'replace')[:400]}")


def przekoduj(sciezka: pathlib.Path) -> None:
    """40 kbps mono — tyle wystarcza na głośnik tabletu i trzyma wagę paczki."""
    if not shutil.which("ffmpeg"):
        print("  (ffmpeg niedostępny — zostawiam plik w formacie źródłowym)")
        return
    tmp = sciezka.with_suffix(".tmp.mp3")
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-i", str(sciezka),
         "-ac", "1", "-b:a", BITRATE_DOCELOWY, str(tmp)], check=True)
    tmp.replace(sciezka)


def main() -> int:
    ap = argparse.ArgumentParser(description="Nagrania poleceń dla dziecka — teoria umysłu (ToM)")
    ap.add_argument("--manifest", action="store_true", help="zapisz manifest nagrań")
    ap.add_argument("--suchy-bieg", action="store_true", help="policz znaki i pliki, nic nie wysyłaj")
    ap.add_argument("--generuj", action="store_true", help="wygeneruj MP3 głosem autorki")
    ap.add_argument("--nadpisz", action="store_true", help="nagraj też pliki, które już istnieją")
    args = ap.parse_args()

    lista = wpisy()
    if args.manifest or not (args.suchy_bieg or args.generuj):
        zapisz_manifest(lista)

    if args.suchy_bieg:
        znaki = sum(len(w["tekst"]) for w in lista)
        print(f"nagrań: {len(lista)} · znaków do syntezy: {znaki} "
              f"· najdłuższe polecenie: {max(len(w['tekst']) for w in lista)} znaków")
        print("Nic nie wysłano — limit ElevenLabs nietknięty.")
        return 0

    if args.generuj:
        klucz, glos = klucz_i_glos()
        print("Głos jest daną biometryczną — nagrania zostają w uzgodnionym użyciu aplikacji.\n")
        for w in lista:
            cel = KORZEN / "04_media" / w["plik"]
            cel.parent.mkdir(parents=True, exist_ok=True)
            if cel.exists() and not args.nadpisz:
                print(f"pomijam {cel.name} (istnieje)")
                continue
            cel.write_bytes(synteza(w["tekst"], klucz, glos))
            przekoduj(cel)
            print(f"nagrano {cel.name}  „{w['tekst']}”")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
