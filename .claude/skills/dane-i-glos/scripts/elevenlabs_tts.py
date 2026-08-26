#!/usr/bin/env python3
"""Generator lektora ElevenLabs dla skilla `dane-i-glos`.

Zamienia plik tekstowy (scenariusz narracji) na MP3, opcjonalnie z napisami SRT
o rzeczywistych znacznikach czasu. Dlugi tekst dzieli na fragmenty i skleja
wynik, zachowujac ciaglosc brzmienia (previous_text / next_text).

Klucz API: zmienna srodowiskowa ELEVENLABS_API_KEY (nigdy w kodzie ani w repo).
Zaleznosci: tylko biblioteka standardowa.

Przyklady:
    python3 elevenlabs_tts.py --glosy
    python3 elevenlabs_tts.py narracja.txt -o raport.mp3
    python3 elevenlabs_tts.py narracja.txt -o raport.mp3 --srt napisy.srt
    python3 elevenlabs_tts.py narracja.txt --suchy-bieg
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

API = "https://api.elevenlabs.io"
MODEL_DOMYSLNY = "eleven_multilingual_v2"      # najlepszy dla polszczyzny
GLOS_DOMYSLNY = "21m00Tcm4TlvDq8ikWAM"          # Rachel — bezpieczny fallback
LIMIT_ZNAKOW = 2400                             # z zapasem ponizej limitu modelu
FORMAT_DOMYSLNY = "mp3_44100_128"
TIMEOUT = 180


def klucz() -> str:
    k = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not k:
        raise SystemExit(
            "Brak klucza API.\n"
            "  export ELEVENLABS_API_KEY=\"...\"\n"
            "Klucz znajdziesz na elevenlabs.io -> ikona profilu -> API Keys."
        )
    return k


def zapytaj(sciezka: str, *, metoda="GET", cialo: dict | None = None, surowe=False):
    dane = json.dumps(cialo).encode("utf-8") if cialo is not None else None
    naglowki = {"xi-api-key": klucz(), "accept": "*/*"}
    if dane:
        naglowki["content-type"] = "application/json"
    req = urllib.request.Request(API + sciezka, data=dane, headers=naglowki, method=metoda)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as odp:
            tresc = odp.read()
    except urllib.error.HTTPError as e:
        raise SystemExit(_komunikat_bledu(e))
    except urllib.error.URLError as e:
        raise SystemExit(f"Brak polaczenia z api.elevenlabs.io: {e.reason}")
    return tresc if surowe else json.loads(tresc.decode("utf-8"))


def _komunikat_bledu(e: urllib.error.HTTPError) -> str:
    try:
        szczegol = json.loads(e.read().decode("utf-8"))
        szczegol = json.dumps(szczegol, ensure_ascii=False)[:600]
    except Exception:
        szczegol = ""
    podpowiedzi = {
        401: "Klucz API jest niewazny albo pusty — sprawdz ELEVENLABS_API_KEY.",
        403: "Klucz nie ma uprawnien do text_to_speech. Wlacz je przy kluczu na elevenlabs.io.",
        404: "Nie ma takiego voice_id. Uruchom `--glosy`, zeby zobaczyc dostepne glosy.",
        422: "Bledne parametry — najczesciej zly model_id albo za dlugi tekst.",
        429: "Przekroczony limit zapytan albo znakow w planie. Poczekaj lub zmniejsz tekst.",
    }
    return (f"ElevenLabs odrzucil zapytanie ({e.code} {e.reason}). "
            f"{podpowiedzi.get(e.code, '')}\n{szczegol}").strip()


# --- glosy -----------------------------------------------------------------

def wypisz_glosy() -> int:
    try:
        dane = zapytaj("/v2/voices?page_size=100")
    except SystemExit:
        dane = zapytaj("/v1/voices")
    glosy = dane.get("voices", [])
    if not glosy:
        print("Konto nie ma zadnych glosow.")
        return 1
    print(f"{'voice_id':<24} {'nazwa':<24} kategoria / opis")
    print("-" * 78)
    for g in glosy:
        opis = (g.get("labels") or {}).get("description") or g.get("category") or ""
        jezyki = ", ".join(
            sorted({j.get("language", "") for j in (g.get("verified_languages") or [])} - {""})
        )
        print(f"{g.get('voice_id',''):<24} {(g.get('name') or '')[:23]:<24} "
              f"{opis}{(' | ' + jezyki) if jezyki else ''}")
    print(f"\nRazem: {len(glosy)}. Uzyj: --voice-id <id> albo export ELEVENLABS_VOICE_ID=<id>")
    return 0


# --- dzielenie tekstu ------------------------------------------------------

def podziel(tekst: str, limit: int = LIMIT_ZNAKOW) -> list[str]:
    """Dzieli po akapitach, potem po zdaniach — nigdy w srodku zdania."""
    tekst = tekst.strip()
    if len(tekst) <= limit:
        return [tekst]
    fragmenty, biezacy = [], ""
    for akapit in re.split(r"\n\s*\n", tekst):
        akapit = akapit.strip()
        if not akapit:
            continue
        kandydaci = [akapit]
        if len(akapit) > limit:
            kandydaci = re.findall(r"[^.!?…]+[.!?…]*\s*", akapit) or [akapit]
        for czesc in kandydaci:
            czesc = czesc.strip()
            if not czesc:
                continue
            if len(czesc) > limit:                       # awaryjnie: twardy podzial
                if biezacy:
                    fragmenty.append(biezacy.strip())
                    biezacy = ""
                for i in range(0, len(czesc), limit):
                    fragmenty.append(czesc[i:i + limit].strip())
                continue
            if len(biezacy) + len(czesc) + 1 > limit:
                fragmenty.append(biezacy.strip())
                biezacy = czesc
            else:
                biezacy = f"{biezacy} {czesc}".strip()
    if biezacy.strip():
        fragmenty.append(biezacy.strip())
    return [f for f in fragmenty if f]


# --- synteza ---------------------------------------------------------------

def ustawienia(a) -> dict:
    u = {
        "stability": a.stability,
        "similarity_boost": a.similarity,
        "style": a.style,
        "use_speaker_boost": True,
    }
    if a.speed != 1.0:
        u["speed"] = a.speed
    return u


def syntezuj(fragment: str, poprzedni: str, nastepny: str, a, ze_znacznikami: bool):
    sciezka = (f"/v1/text-to-speech/{a.voice_id}"
               f"{'/with-timestamps' if ze_znacznikami else ''}"
               f"?output_format={a.format}")
    cialo = {
        "text": fragment,
        "model_id": a.model,
        "voice_settings": ustawienia(a),
        "language_code": a.jezyk,
    }
    if poprzedni:
        cialo["previous_text"] = poprzedni[-500:]
    if nastepny:
        cialo["next_text"] = nastepny[:500]
    if a.jezyk is None:
        cialo.pop("language_code")

    if not ze_znacznikami:
        return zapytaj(sciezka, metoda="POST", cialo=cialo, surowe=True), None
    odp = zapytaj(sciezka, metoda="POST", cialo=cialo)
    audio = base64.b64decode(odp["audio_base64"])
    return audio, odp.get("normalized_alignment") or odp.get("alignment")


# --- napisy ----------------------------------------------------------------

def _czas(sekundy: float) -> str:
    ms = int(round(sekundy * 1000))
    g, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{g:02d}:{m:02d}:{s:02d},{ms:03d}"


def srt_ze_znacznikow(bloki: list[tuple[dict, float]], maks_znakow=90) -> str:
    """Skleja znaczniki znakowe w linie napisow lamane na koncach zdan."""
    linie, nr = [], 1
    for wyrownanie, przesuniecie in bloki:
        if not wyrownanie:
            continue
        znaki = wyrownanie["characters"]
        start = wyrownanie["character_start_times_seconds"]
        koniec = wyrownanie["character_end_times_seconds"]
        buf, t0 = "", None
        for i, znak in enumerate(znaki):
            if t0 is None:
                t0 = start[i] + przesuniecie
            buf += znak
            koniec_zdania = znak in ".!?…"
            if koniec_zdania or len(buf) >= maks_znakow:
                if koniec_zdania or buf.endswith(" "):
                    tekst = buf.strip()
                    if tekst:
                        linie.append(f"{nr}\n{_czas(t0)} --> "
                                     f"{_czas(koniec[i] + przesuniecie)}\n{tekst}\n")
                        nr += 1
                    buf, t0 = "", None
        if buf.strip():
            linie.append(f"{nr}\n{_czas(t0 or przesuniecie)} --> "
                         f"{_czas(koniec[-1] + przesuniecie)}\n{buf.strip()}\n")
            nr += 1
    return "\n".join(linie)


# --- main ------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(
        description="Scenariusz narracji -> MP3 (ElevenLabs). Skill dane-i-glos.")
    ap.add_argument("tekst", nargs="?", type=Path,
                    help="plik .txt ze scenariuszem (albo '-' dla stdin)")
    ap.add_argument("-o", "--output", type=Path, default=Path("narracja.mp3"))
    ap.add_argument("--glosy", action="store_true", help="wypisz glosy z konta i zakoncz")
    ap.add_argument("--voice-id", default=os.environ.get("ELEVENLABS_VOICE_ID", GLOS_DOMYSLNY))
    ap.add_argument("--model", default=MODEL_DOMYSLNY,
                    help=f"domyslnie {MODEL_DOMYSLNY}; alternatywy: eleven_v3, "
                         "eleven_turbo_v2_5, eleven_flash_v2_5")
    ap.add_argument("--jezyk", default=None,
                    help="wymus kod jezyka, np. pl (dziala z modelami turbo/flash v2.5)")
    ap.add_argument("--format", default=FORMAT_DOMYSLNY,
                    help=f"domyslnie {FORMAT_DOMYSLNY}")
    ap.add_argument("--srt", type=Path, help="zapisz takze napisy SRT z API")
    ap.add_argument("--stability", type=float, default=0.5)
    ap.add_argument("--similarity", type=float, default=0.75)
    ap.add_argument("--style", type=float, default=0.0)
    ap.add_argument("--speed", type=float, default=1.0, help="0.7–1.2")
    ap.add_argument("--suchy-bieg", dest="suchy", action="store_true",
                    help="policz znaki i fragmenty bez wywolania API")
    a = ap.parse_args()

    if a.glosy:
        return wypisz_glosy()
    if not a.tekst:
        ap.error("podaj plik ze scenariuszem albo uzyj --glosy")

    tresc = (sys.stdin.read() if str(a.tekst) == "-"
             else a.tekst.read_text(encoding="utf-8")).strip()
    if not tresc:
        print("Scenariusz jest pusty — nie ma czego czytac.", file=sys.stderr)
        return 2

    fragmenty = podziel(tresc)
    slowa = len(tresc.split())
    print(f"Znakow: {len(tresc)} | slow: {slowa} | fragmentow: {len(fragmenty)} "
          f"| szacowany czas: ~{slowa / 150:.1f} min", file=sys.stderr)
    if a.suchy:
        for i, f in enumerate(fragmenty, 1):
            print(f"  [{i}] {len(f)} znakow: {f[:70]}...", file=sys.stderr)
        return 0

    kawalki, bloki, przesuniecie = [], [], 0.0
    for i, fragment in enumerate(fragmenty):
        print(f"  fragment {i + 1}/{len(fragmenty)}...", file=sys.stderr)
        audio, wyrownanie = syntezuj(
            fragment,
            fragmenty[i - 1] if i else "",
            fragmenty[i + 1] if i + 1 < len(fragmenty) else "",
            a,
            ze_znacznikami=bool(a.srt),
        )
        kawalki.append(audio)
        if a.srt and wyrownanie:
            bloki.append((wyrownanie, przesuniecie))
            przesuniecie += wyrownanie["character_end_times_seconds"][-1]

    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_bytes(b"".join(kawalki))
    print(f"Audio: {a.output} ({a.output.stat().st_size / 1024:.0f} kB)", file=sys.stderr)

    if a.srt:
        if bloki:
            a.srt.write_text(srt_ze_znacznikow(bloki), encoding="utf-8")
            print(f"Napisy: {a.srt}", file=sys.stderr)
        else:
            print("API nie zwrocilo znacznikow czasu — napisy nie powstaly.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
