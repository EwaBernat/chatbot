#!/usr/bin/env python3
"""Klonowanie glosu w ElevenLabs dla skilla `dane-i-glos`.

Robi jedna rzecz, jednorazowo: z Twoich nagran wzorcowych tworzy glos (Instant Voice
Cloning) i zwraca `voice_id`, ktorego pozniej uzywa `elevenlabs_tts.py`.

Klonuj wylacznie wlasny glos albo glos osoby, ktora wyrazila na to zgode.

Klucz API: zmienna srodowiskowa ELEVENLABS_API_KEY.
Zaleznosci: tylko biblioteka standardowa.

Przyklady:
    python3 elevenlabs_klon_glosu.py --sprawdz-nagrania probki/*.mp3
    python3 elevenlabs_klon_glosu.py "Ewa - narracja PL" probki/*.mp3
    python3 elevenlabs_klon_glosu.py --moje-glosy
"""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
import sys
import urllib.error
import urllib.request
import uuid
import wave
from pathlib import Path

API = "https://api.elevenlabs.io"
TIMEOUT = 300
MAKS_LACZNIE_MB = 10          # limit wysylki dla Instant Voice Cloning
MAKS_PLIKOW = 25
MIN_SEKUND_ZALECANE = 60      # ponizej minuty klon brzmi plasko
OPT_SEKUND = 180              # trzy minuty to dobry punkt docelowy


def klucz() -> str:
    k = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not k:
        raise SystemExit(
            "Brak klucza API.\n"
            "  export ELEVENLABS_API_KEY=\"...\"\n"
            "Klucz znajdziesz na elevenlabs.io -> ikona profilu -> API Keys "
            "(potrzebne uprawnienie voices_write)."
        )
    return k


def _komunikat_bledu(e: urllib.error.HTTPError) -> str:
    try:
        szczegol = json.dumps(json.loads(e.read().decode("utf-8")), ensure_ascii=False)[:700]
    except Exception:
        szczegol = ""
    podpowiedzi = {
        400: "Najczesciej: plik za duzy, zly format albo nagranie za krotkie.",
        401: "Klucz API jest niewazny — sprawdz ELEVENLABS_API_KEY.",
        403: "Klucz nie ma uprawnienia voices_write albo plan nie obejmuje klonowania "
             "glosu. Instant Voice Cloning wymaga planu Starter lub wyzszego.",
        422: "Bledne parametry wysylki — sprawdz nazwe glosu i pliki.",
        429: "Przekroczony limit zapytan. Odczekaj chwile.",
    }
    return (f"ElevenLabs odrzucil zapytanie ({e.code} {e.reason}). "
            f"{podpowiedzi.get(e.code, '')}\n{szczegol}").strip()


def zapytaj(sciezka: str, *, metoda="GET", cialo=None, typ_tresci=None):
    naglowki = {"xi-api-key": klucz(), "accept": "application/json"}
    if typ_tresci:
        naglowki["content-type"] = typ_tresci
    req = urllib.request.Request(API + sciezka, data=cialo, headers=naglowki, method=metoda)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as odp:
            return json.loads(odp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise SystemExit(_komunikat_bledu(e))
    except urllib.error.URLError as e:
        raise SystemExit(f"Brak polaczenia z api.elevenlabs.io: {e.reason}")


# --- kontrola nagran -------------------------------------------------------

def dlugosc_wav(sciezka: Path) -> float | None:
    try:
        with wave.open(str(sciezka), "rb") as w:
            return w.getnframes() / float(w.getframerate())
    except Exception:
        return None


def sprawdz_nagrania(pliki: list[Path], cicho=False) -> tuple[bool, float]:
    """Zwraca (czy_mozna_wyslac, laczne_sekundy_jesli_dalo_sie_policzyc)."""
    problemy: list[str] = []
    uwagi: list[str] = []
    lacznie_bajtow = 0
    lacznie_sekund = 0.0
    znane_sekundy = True

    if not pliki:
        return False, 0.0
    if len(pliki) > MAKS_PLIKOW:
        problemy.append(f"Za duzo plikow: {len(pliki)} (limit {MAKS_PLIKOW}).")

    for p in pliki:
        if not p.exists():
            problemy.append(f"Nie ma pliku: {p}")
            continue
        typ = mimetypes.guess_type(str(p))[0] or ""
        if not typ.startswith("audio/") and p.suffix.lower() not in (".m4a", ".ogg", ".flac"):
            problemy.append(f"To nie wyglada na plik audio ({typ or 'nieznany typ'}): {p.name}")
            continue
        rozmiar = p.stat().st_size
        lacznie_bajtow += rozmiar
        if rozmiar < 20_000:
            uwagi.append(f"{p.name} ma tylko {rozmiar / 1024:.0f} kB — to prawie na pewno "
                         "za krotkie nagranie.")
        sek = dlugosc_wav(p) if p.suffix.lower() == ".wav" else None
        if sek is None:
            znane_sekundy = False
        else:
            lacznie_sekund += sek
        if not cicho:
            czas = f"{sek:.0f} s" if sek is not None else "czas nieznany"
            print(f"  {p.name:<38} {rozmiar / 1_048_576:>6.2f} MB  {czas}")

    mb = lacznie_bajtow / 1_048_576
    if mb > MAKS_LACZNIE_MB:
        problemy.append(f"Laczny rozmiar {mb:.1f} MB przekracza limit {MAKS_LACZNIE_MB} MB. "
                        "Skroc nagrania albo zapisz je w mp3 128 kb/s.")
    if znane_sekundy and lacznie_sekund:
        if lacznie_sekund < MIN_SEKUND_ZALECANE:
            uwagi.append(f"Lacznie tylko {lacznie_sekund:.0f} s materialu. Klon z tak krotkiej "
                         f"probki brzmi plasko — dograj do {OPT_SEKUND} s.")
        elif lacznie_sekund < OPT_SEKUND:
            uwagi.append(f"Lacznie {lacznie_sekund:.0f} s. Zadziala, ale {OPT_SEKUND} s "
                         "daje wyraznie lepszy klon.")

    if not cicho:
        print(f"\nRazem: {len(pliki)} plikow, {mb:.2f} MB"
              + (f", {lacznie_sekund:.0f} s" if znane_sekundy and lacznie_sekund else ""))
        for u in uwagi:
            print(f"  uwaga: {u}")
        for p in problemy:
            print(f"  BLAD: {p}", file=sys.stderr)
        if not problemy:
            print("\nNagrania nadaja sie do wyslania.")
    return not problemy, lacznie_sekund


# --- wysylka multipart -----------------------------------------------------

def zbuduj_multipart(pola: dict[str, str], pliki: list[Path]) -> tuple[bytes, str]:
    granica = f"----daneiglos{uuid.uuid4().hex}"
    czesci: list[bytes] = []
    for nazwa, wartosc in pola.items():
        czesci.append(
            f"--{granica}\r\nContent-Disposition: form-data; name=\"{nazwa}\"\r\n\r\n"
            f"{wartosc}\r\n".encode("utf-8"))
    for p in pliki:
        typ = mimetypes.guess_type(str(p))[0] or "audio/mpeg"
        czesci.append(
            f"--{granica}\r\nContent-Disposition: form-data; name=\"files\"; "
            f"filename=\"{p.name}\"\r\nContent-Type: {typ}\r\n\r\n".encode("utf-8"))
        czesci.append(p.read_bytes())
        czesci.append(b"\r\n")
    czesci.append(f"--{granica}--\r\n".encode("utf-8"))
    return b"".join(czesci), f"multipart/form-data; boundary={granica}"


def klonuj(nazwa: str, pliki: list[Path], opis: str | None, odszum: bool) -> int:
    pola = {"name": nazwa}
    if opis:
        pola["description"] = opis
    if odszum:
        pola["remove_background_noise"] = "true"
    pola["labels"] = json.dumps({"language": "pl", "use_case": "narration"},
                                ensure_ascii=False)

    cialo, typ = zbuduj_multipart(pola, pliki)
    print(f"Wysylam {len(pliki)} plikow ({len(cialo) / 1_048_576:.2f} MB)...", file=sys.stderr)
    odp = zapytaj("/v1/voices/add", metoda="POST", cialo=cialo, typ_tresci=typ)

    voice_id = odp.get("voice_id")
    if not voice_id:
        print(f"ElevenLabs nie zwrocil voice_id: {json.dumps(odp, ensure_ascii=False)[:400]}",
              file=sys.stderr)
        return 1

    print(f"\nGlos utworzony.\n  nazwa:    {nazwa}\n  voice_id: {voice_id}")
    if odp.get("requires_verification"):
        print("\n  UWAGA: ElevenLabs wymaga weryfikacji tego glosu przed uzyciem.\n"
              "  Wejdz na elevenlabs.io -> Voices -> ten glos i przejdz weryfikacje "
              "(nagranie zdania potwierdzajacego).")
    print(f"\nZapisz go na stale:\n  export ELEVENLABS_VOICE_ID=\"{voice_id}\"\n\n"
          f"Sprawdz brzmienie:\n  python3 elevenlabs_tts.py narracja.txt "
          f"--voice-id {voice_id} -o proba.mp3")
    return 0


def moje_glosy() -> int:
    try:
        dane = zapytaj("/v2/voices?page_size=100")
    except SystemExit:
        dane = zapytaj("/v1/voices")
    wlasne = [g for g in dane.get("voices", [])
              if g.get("category") in ("cloned", "generated", "professional")]
    if not wlasne:
        print("Na koncie nie ma zadnego wlasnego glosu — sa tylko glosy gotowe (premade).\n"
              "Zeby miec swoj, uruchom ten skrypt z nazwa i nagraniami.")
        return 1
    print(f"{'voice_id':<24} {'nazwa':<30} kategoria")
    print("-" * 70)
    for g in wlasne:
        print(f"{g.get('voice_id',''):<24} {(g.get('name') or '')[:29]:<30} "
              f"{g.get('category','')}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Klonuje Twoj glos w ElevenLabs (jednorazowo). Skill dane-i-glos.")
    ap.add_argument("nazwa", nargs="?", help="nazwa glosu, np. \"Ewa - narracja PL\"")
    ap.add_argument("nagrania", nargs="*", type=Path, help="pliki audio z Twoim glosem")
    ap.add_argument("--sprawdz-nagrania", dest="tylko_sprawdz", nargs="+", type=Path,
                    metavar="PLIK", help="sprawdz pliki bez wysylania czegokolwiek")
    ap.add_argument("--moje-glosy", action="store_true",
                    help="wypisz wlasne (nie-gotowe) glosy z konta")
    ap.add_argument("--opis", help="krotki opis glosu")
    ap.add_argument("--odszum", action="store_true",
                    help="popros ElevenLabs o usuniecie szumu tla z probek")
    a = ap.parse_args()

    if a.moje_glosy:
        return moje_glosy()
    if a.tylko_sprawdz:
        print("Kontrola nagran (nic nie zostanie wyslane):\n")
        ok, _ = sprawdz_nagrania(a.tylko_sprawdz)
        return 0 if ok else 1
    if not a.nazwa or not a.nagrania:
        ap.error("podaj nazwe glosu i pliki z nagraniami "
                 "(albo --sprawdz-nagrania / --moje-glosy)")

    print("Kontrola nagran:\n")
    ok, _ = sprawdz_nagrania(a.nagrania)
    if not ok:
        print("\nNie wysylam — popraw powyzsze bledy.", file=sys.stderr)
        return 1
    print()
    return klonuj(a.nazwa, a.nagrania, a.opis, a.odszum)


if __name__ == "__main__":
    sys.exit(main())
