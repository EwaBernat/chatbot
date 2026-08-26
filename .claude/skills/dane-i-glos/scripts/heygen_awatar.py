#!/usr/bin/env python3
"""Awatar HeyGen dla skilla `dane-i-glos`.

Zamienia scenariusz narracji w film z Twoim awatarem i Twoim glosem z konta HeyGen.
Dwa tryby glosu:

  * tekst  — HeyGen sam czyta scenariusz wybranym glosem (--voice-id)
  * audio  — HeyGen porusza ustami awatara do gotowego MP3 (--audio),
             np. tego wygenerowanego przez elevenlabs_tts.py

Klucz API: zmienna srodowiskowa HEYGEN_API_KEY (nigdy w kodzie ani w repo).
Zaleznosci: tylko biblioteka standardowa.

Przyklady:
    python3 heygen_awatar.py --awatary
    python3 heygen_awatar.py --glosy --jezyk polish
    python3 heygen_awatar.py narracja.txt --avatar-id <id> --voice-id <id> --czekaj
    python3 heygen_awatar.py --audio raport.mp3 --avatar-id <id> --czekaj -o film.mp4
"""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import konfiguracja                                    # noqa: E402

API = "https://api.heygen.com"
UPLOAD = "https://upload.heygen.com"
TIMEOUT = 120
ODSTEP_ODPYTANIA = 10          # sekund miedzy sprawdzeniami statusu
MAKS_CZEKANIA = 1800           # 30 minut


def klucz() -> str:
    k = os.environ.get("HEYGEN_API_KEY", "").strip()
    if not k:
        raise SystemExit(
            "Brak klucza API HeyGen.\n"
            "  export HEYGEN_API_KEY=\"...\"\n"
            "Klucz znajdziesz na app.heygen.com -> Settings -> Subscriptions & API "
            "(albo Space Settings -> API Token)."
        )
    return k


def zapytaj(url: str, *, metoda="GET", cialo=None, typ_tresci=None, surowe=False):
    naglowki = {"X-Api-Key": klucz(), "accept": "application/json"}
    if isinstance(cialo, (bytes, bytearray)):
        dane = bytes(cialo)
        naglowki["content-type"] = typ_tresci or "application/octet-stream"
    elif cialo is not None:
        dane = json.dumps(cialo).encode("utf-8")
        naglowki["content-type"] = "application/json"
    else:
        dane = None
    req = urllib.request.Request(url, data=dane, headers=naglowki, method=metoda)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as odp:
            tresc = odp.read()
    except urllib.error.HTTPError as e:
        raise SystemExit(_komunikat_bledu(e))
    except urllib.error.URLError as e:
        raise SystemExit(f"Brak polaczenia z HeyGen: {e.reason}")
    if surowe:
        return tresc
    odpowiedz = json.loads(tresc.decode("utf-8"))
    # HeyGen sygnalizuje bledy takze w tresci odpowiedzi, nie tylko kodem HTTP
    blad = odpowiedz.get("error")
    if blad:
        raise SystemExit(f"HeyGen zwrocil blad: {json.dumps(blad, ensure_ascii=False)}")
    return odpowiedz


def _komunikat_bledu(e: urllib.error.HTTPError) -> str:
    try:
        szczegol = json.dumps(json.loads(e.read().decode("utf-8")), ensure_ascii=False)[:600]
    except Exception:
        szczegol = ""
    podpowiedzi = {
        401: "Klucz API jest niewazny — sprawdz HEYGEN_API_KEY.",
        400: "Bledne parametry — najczesciej zle avatar_id albo voice_id. Uruchom --awatary / --glosy.",
        402: "Brak kredytow na koncie HeyGen.",
        404: "Nie ma takiego zasobu — sprawdz identyfikator.",
        429: "Za duzo zapytan albo wyczerpany limit planu. Odczekaj chwile.",
    }
    return (f"HeyGen odrzucil zapytanie ({e.code} {e.reason}). "
            f"{podpowiedzi.get(e.code, '')}\n{szczegol}").strip()


# --- listy zasobow ---------------------------------------------------------

def wypisz_awatary(szukaj: str | None) -> int:
    dane = zapytaj(f"{API}/v2/avatars").get("data", {})
    awatary = dane.get("avatars") or []
    zdjecia = dane.get("talking_photos") or []
    if not awatary and not zdjecia:
        print("Konto HeyGen nie ma zadnych awatarow.")
        return 1

    def pasuje(nazwa: str) -> bool:
        return not szukaj or szukaj.lower() in (nazwa or "").lower()

    print("AWATARY (character.type = avatar)")
    print(f"{'avatar_id':<40} nazwa / plec")
    print("-" * 78)
    ile = 0
    for a in awatary:
        nazwa = a.get("avatar_name") or ""
        if not pasuje(nazwa):
            continue
        ile += 1
        print(f"{a.get('avatar_id',''):<40} {nazwa} ({a.get('gender','?')})")
    if zdjecia:
        print("\nTALKING PHOTOS (character.type = talking_photo)")
        print(f"{'talking_photo_id':<40} nazwa")
        print("-" * 78)
        for z in zdjecia:
            nazwa = z.get("talking_photo_name") or ""
            if not pasuje(nazwa):
                continue
            ile += 1
            print(f"{z.get('talking_photo_id',''):<40} {nazwa}")
    print(f"\nRazem pasujacych: {ile}. Twoj wlasny awatar ma zwykle nazwe, ktora sama nadalas "
          "przy tworzeniu Instant Avatar.")
    return 0


def wypisz_glosy(jezyk: str | None, szukaj: str | None) -> int:
    glosy = zapytaj(f"{API}/v2/voices").get("data", {}).get("voices") or []
    if not glosy:
        print("Konto HeyGen nie ma zadnych glosow.")
        return 1
    wybrane = []
    for g in glosy:
        jez = (g.get("language") or "")
        nazwa = (g.get("name") or "")
        if jezyk and jezyk.lower() not in jez.lower():
            continue
        if szukaj and szukaj.lower() not in nazwa.lower():
            continue
        wybrane.append(g)
    if not wybrane:
        dostepne = sorted({(g.get("language") or "?") for g in glosy})
        print(f"Zaden glos nie pasuje do filtru. Jezyki na koncie: {', '.join(dostepne)}")
        return 1
    print(f"{'voice_id':<40} {'nazwa':<28} jezyk / plec")
    print("-" * 92)
    for g in wybrane:
        print(f"{g.get('voice_id',''):<40} {(g.get('name') or '')[:27]:<28} "
              f"{g.get('language','?')} / {g.get('gender','?')}")
    print(f"\nRazem: {len(wybrane)} z {len(glosy)}. Twoj sklonowany glos ma nadana przez "
          "Ciebie nazwe i zwykle jezyk zgodny z nagraniem wzorcowym.")
    return 0


# --- wysylka audio ---------------------------------------------------------

def wyslij_audio(sciezka: Path) -> str:
    if not sciezka.exists():
        raise SystemExit(f"Nie ma pliku audio: {sciezka}")
    typ = mimetypes.guess_type(str(sciezka))[0] or "audio/mpeg"
    if not typ.startswith("audio/"):
        raise SystemExit(f"To nie jest plik audio ({typ}): {sciezka}")
    print(f"Wysylam audio do HeyGen ({sciezka.stat().st_size / 1024:.0f} kB)...",
          file=sys.stderr)
    odp = zapytaj(f"{UPLOAD}/v1/asset", metoda="POST",
                  cialo=sciezka.read_bytes(), typ_tresci=typ)
    dane = odp.get("data") or {}
    asset_id = dane.get("id") or dane.get("asset_id")
    if not asset_id:
        raise SystemExit(f"HeyGen nie zwrocil identyfikatora zasobu: "
                         f"{json.dumps(odp, ensure_ascii=False)[:400]}")
    return asset_id


# --- generowanie -----------------------------------------------------------

def zbuduj_wejscie(a, tekst: str | None, asset_id: str | None) -> dict:
    if a.talking_photo_id:
        postac = {"type": "talking_photo", "talking_photo_id": a.talking_photo_id}
    else:
        postac = {"type": "avatar", "avatar_id": a.avatar_id, "avatar_style": a.styl}

    if asset_id:
        glos = {"type": "audio", "audio_asset_id": asset_id}
    else:
        glos = {"type": "text", "input_text": tekst, "voice_id": a.voice_id}
        if a.speed != 1.0:
            glos["speed"] = a.speed

    wejscie = {"character": postac, "voice": glos}
    if a.tlo:
        wejscie["background"] = ({"type": "image", "url": a.tlo}
                                 if a.tlo.startswith("http")
                                 else {"type": "color", "value": a.tlo})
    return wejscie


def generuj(a, tekst: str | None, asset_id: str | None) -> str:
    cialo = {
        "video_inputs": [zbuduj_wejscie(a, tekst, asset_id)],
        "dimension": {"width": a.szerokosc, "height": a.wysokosc},
    }
    if a.tytul:
        cialo["title"] = a.tytul
    if a.napisy:
        cialo["caption"] = True
    odp = zapytaj(f"{API}/v2/video/generate", metoda="POST", cialo=cialo)
    video_id = (odp.get("data") or {}).get("video_id")
    if not video_id:
        raise SystemExit(f"HeyGen nie zwrocil video_id: "
                         f"{json.dumps(odp, ensure_ascii=False)[:400]}")
    return video_id


def status(video_id: str) -> dict:
    return zapytaj(f"{API}/v1/video_status.get?video_id={video_id}").get("data", {})


def czekaj_i_pobierz(video_id: str, wyjscie: Path) -> int:
    print(f"video_id: {video_id} — czekam na render...", file=sys.stderr)
    poczatek = time.monotonic()
    while True:
        d = status(video_id)
        stan = d.get("status")
        if stan == "completed":
            url = d.get("video_url")
            if not url:
                print("Render gotowy, ale HeyGen nie podal adresu pliku.", file=sys.stderr)
                return 1
            wyjscie.parent.mkdir(parents=True, exist_ok=True)
            with urllib.request.urlopen(url, timeout=TIMEOUT) as odp:
                wyjscie.write_bytes(odp.read())
            print(f"Film: {wyjscie} ({wyjscie.stat().st_size / 1_048_576:.1f} MB)",
                  file=sys.stderr)
            if d.get("duration"):
                print(f"Czas trwania: {d['duration']} s", file=sys.stderr)
            return 0
        if stan == "failed":
            blad = d.get("error") or {}
            print(f"Render nie powiodl sie: {json.dumps(blad, ensure_ascii=False)}",
                  file=sys.stderr)
            return 1
        if time.monotonic() - poczatek > MAKS_CZEKANIA:
            print(f"Minelo {MAKS_CZEKANIA // 60} minut, a status to nadal `{stan}`.\n"
                  f"Sprawdz pozniej: --status {video_id}", file=sys.stderr)
            return 2
        print(f"  status: {stan}...", file=sys.stderr)
        time.sleep(ODSTEP_ODPYTANIA)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Scenariusz narracji -> film z awatarem HeyGen. Skill dane-i-glos.")
    ap.add_argument("tekst", nargs="?", type=Path,
                    help="plik .txt ze scenariuszem (pomin przy --audio)")
    ap.add_argument("-o", "--output", type=Path, default=Path("awatar.mp4"))
    ap.add_argument("--awatary", action="store_true", help="wypisz awatary z konta i zakoncz")
    ap.add_argument("--glosy", action="store_true", help="wypisz glosy z konta i zakoncz")
    ap.add_argument("--szukaj", help="filtr nazwy przy --awatary / --glosy")
    ap.add_argument("--jezyk", help="filtr jezyka przy --glosy, np. polish")
    ap.add_argument("--status", dest="video_id", help="sprawdz status wczesniejszego renderu")
    ap.add_argument("--avatar-id", default=None,
                    help="domyslnie awatar zapamietany przez skill")
    ap.add_argument("--talking-photo-id", default="",
                    help="uzyj zdjecia mowiacego zamiast awatara")
    ap.add_argument("--voice-id", default=None,
                    help="domyslnie glos HeyGen zapamietany przez skill")
    ap.add_argument("--audio", type=Path,
                    help="gotowe MP3 (np. z elevenlabs_tts.py) zamiast czytania tekstu")
    ap.add_argument("--styl", default="normal", help="avatar_style: normal / circle / closeUp")
    ap.add_argument("--tlo", help="kolor #RRGGBB albo adres URL obrazu tla")
    ap.add_argument("--szerokosc", type=int, default=1920)
    ap.add_argument("--wysokosc", type=int, default=1080)
    ap.add_argument("--speed", type=float, default=1.0)
    ap.add_argument("--napisy", action="store_true", help="wypal napisy w filmie")
    ap.add_argument("--tytul", help="nazwa filmu na koncie HeyGen")
    ap.add_argument("--czekaj", action="store_true",
                    help="czekaj na koniec renderu i pobierz plik")
    ap.add_argument("--suchy-bieg", dest="suchy", action="store_true",
                    help="pokaz zapytanie bez wysylania go do API")
    a = ap.parse_args()

    a.avatar_id = konfiguracja.ustal(a.avatar_id, "HEYGEN_AVATAR_ID", "heygen_avatar_id", "")
    a.voice_id = konfiguracja.ustal(a.voice_id, "HEYGEN_VOICE_ID", "heygen_voice_id", "")

    if a.awatary:
        return wypisz_awatary(a.szukaj)
    if a.glosy:
        return wypisz_glosy(a.jezyk, a.szukaj)
    if a.video_id:
        print(json.dumps(status(a.video_id), ensure_ascii=False, indent=2))
        return 0

    if not a.avatar_id and not a.talking_photo_id:
        print("Podaj --avatar-id albo --talking-photo-id.\n"
              "Nie znasz swojego? Uruchom: --awatary", file=sys.stderr)
        return 2

    tekst = asset_id = None
    if a.audio:
        if a.tekst:
            print("Podano i scenariusz, i --audio. Uzywam audio; "
                  "tekst posluzy tylko jako podglad.", file=sys.stderr)
        if not a.suchy:
            asset_id = wyslij_audio(a.audio)
    else:
        if not a.tekst:
            ap.error("podaj plik ze scenariuszem albo --audio")
        if not a.voice_id:
            print("Podaj --voice-id (glos, ktorym awatar ma mowic).\n"
                  "Nie znasz swojego? Uruchom: --glosy --jezyk polish", file=sys.stderr)
            return 2
        tekst = a.tekst.read_text(encoding="utf-8").strip()
        if not tekst:
            print("Scenariusz jest pusty — nie ma czego czytac.", file=sys.stderr)
            return 2
        slowa = len(tekst.split())
        print(f"Znakow: {len(tekst)} | slow: {slowa} | szacowany czas: ~{slowa / 150:.1f} min",
              file=sys.stderr)

    if a.suchy:
        print(json.dumps({
            "video_inputs": [zbuduj_wejscie(a, tekst, "(asset po wyslaniu audio)"
                                            if a.audio else None)],
            "dimension": {"width": a.szerokosc, "height": a.wysokosc},
        }, ensure_ascii=False, indent=2))
        return 0

    video_id = generuj(a, tekst, asset_id)
    if not a.czekaj:
        print(f"Render ruszyl. video_id: {video_id}\n"
              f"Sprawdz pozniej: --status {video_id}", file=sys.stderr)
        return 0
    return czekaj_i_pobierz(video_id, a.output)


if __name__ == "__main__":
    sys.exit(main())
