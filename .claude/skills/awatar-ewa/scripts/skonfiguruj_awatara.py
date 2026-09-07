#!/usr/bin/env python3
"""Jedno polecenie, zeby skill zapamietal Twojego awatara i Twoj glos w HeyGen.

Przeglada awatary i glosy na Twoim koncie HeyGen, znajduje te, ktore nosza Twoje
imie, i zapisuje ich identyfikatory w pamieci skilla. Od tej chwili ani Ty, ani
Claude nie musicie ich szukac przy kazdym filmie — a przede wszystkim zaden film
nie powstanie przypadkiem na cudzym awatarze.

Pamiec to ten sam plik, ktorego uzywa skill `dane-i-glos`
(`~/.config/dane-i-glos/konfiguracja.json`) — glos z ElevenLabs i awatar z HeyGen
leza obok siebie, poza repozytorium. Kluczy API ten plik nie przyjmuje.

Klucz API: zmienna srodowiskowa HEYGEN_API_KEY.
Zaleznosci: biblioteka standardowa.

Przyklady:
    python3 skonfiguruj_awatara.py                     # szuka "Ewa" wsrod awatarow i glosow
    python3 skonfiguruj_awatara.py --szukaj "Ewa PL"
    python3 skonfiguruj_awatara.py --awatar-id <id> --glos-id <id>
    python3 skonfiguruj_awatara.py --pokaz
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

# Pamiec i warstwa HTTP sa wspolne ze skillem `dane-i-glos` — nie powielamy ich,
# zeby oba skille pamietaly to samo i zeby bledy HeyGen mialy jeden opis.
SASIAD = Path(__file__).resolve().parents[2] / "dane-i-glos" / "scripts"
if not SASIAD.is_dir():
    raise SystemExit(
        f"Nie znajduje skilla `dane-i-glos` w {SASIAD}.\n"
        "Ten skrypt korzysta z jego pamieci i warstwy HTTP. Sprawdz, czy oba skille\n"
        "leza obok siebie w .claude/skills/."
    )
sys.path.insert(0, str(SASIAD))
import konfiguracja                                     # noqa: E402
from heygen_awatar import API, klucz, zapytaj           # noqa: E402

DOMYSLNE_IMIE = "Ewa"


def siec_przepuszcza() -> tuple[bool, str]:
    """Odroznia blokade sieciowa od problemu z kluczem — te bledy wygladaja tak samo."""
    try:
        urllib.request.urlopen("https://api.heygen.com/", timeout=10)
        return True, ""
    except urllib.error.HTTPError:
        return True, ""                                 # serwer odpowiedzial, wiec siec dziala
    except urllib.error.URLError as e:
        return False, str(e.reason)
    except Exception as e:                              # noqa: BLE001
        return False, str(e)


def pobierz_awatary() -> list[dict]:
    """Awatary i zdjecia mowiace sprowadzone do jednego ksztaltu."""
    dane = zapytaj(f"{API}/v2/avatars").get("data", {})
    lista = [
        {"id": a.get("avatar_id", ""), "nazwa": a.get("avatar_name") or "",
         "rodzaj": "avatar", "opis": a.get("gender", "?")}
        for a in (dane.get("avatars") or [])
    ]
    lista += [
        {"id": z.get("talking_photo_id", ""), "nazwa": z.get("talking_photo_name") or "",
         "rodzaj": "talking_photo", "opis": "zdjecie mowiace"}
        for z in (dane.get("talking_photos") or [])
    ]
    return [p for p in lista if p["id"]]


def pobierz_glosy() -> list[dict]:
    glosy = zapytaj(f"{API}/v2/voices").get("data", {}).get("voices") or []
    return [
        {"id": g.get("voice_id", ""), "nazwa": g.get("name") or "",
         "rodzaj": "voice", "opis": f"{g.get('language', '?')} / {g.get('gender', '?')}"}
        for g in glosy if g.get("voice_id")
    ]


def pasujace(pozycje: list[dict], imie: str) -> list[dict]:
    return [p for p in pozycje if imie.lower() in p["nazwa"].lower()]


def wypisz(naglowek: str, pozycje: list[dict]) -> None:
    print(f"\n{naglowek}")
    if not pozycje:
        print("  (nic nie pasuje)")
        return
    for p in pozycje:
        print(f"  {p['id']:<40} {p['nazwa']}  [{p['rodzaj']}, {p['opis']}]")


def wybierz(pozycje: list[dict], imie: str, co: str) -> dict | None:
    """Jednoznaczne trafienie zapisujemy same; przy wielu decyzja nalezy do czlowieka."""
    trafienia = pasujace(pozycje, imie)
    if len(trafienia) == 1:
        return trafienia[0]
    if not trafienia:
        print(f"\nZaden {co} na koncie nie ma w nazwie „{imie}”.")
        wypisz(f"Wszystkie {co}y na koncie:", pozycje[:40])
        print(f"\n  Wskaz recznie: --{'awatar' if co == 'awatar' else 'glos'}-id <id>")
        return None
    print(f"\nWiecej niz jeden {co} pasuje do „{imie}” — nie zgaduje, ktory jest Twoj.")
    wypisz("Kandydaci:", trafienia)
    print(f"\n  Wskaz recznie: --{'awatar' if co == 'awatar' else 'glos'}-id <id>")
    return None


def zapomnij() -> int:
    dane = konfiguracja.wczytaj()
    usuniete = [k for k in ("heygen_avatar_id", "heygen_avatar_name", "heygen_avatar_rodzaj",
                            "heygen_voice_id", "heygen_voice_name") if dane.pop(k, None)]
    konfiguracja.SCIEZKA.parent.mkdir(parents=True, exist_ok=True)
    konfiguracja.SCIEZKA.write_text(json.dumps(dane, ensure_ascii=False, indent=2),
                                    encoding="utf-8")
    print("Zapomniane: " + (", ".join(usuniete) if usuniete else "nie bylo czego zapominac") +
          ".\nAwatar i glos na koncie HeyGen zostaja nietkniete.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Zapamietuje Twojego awatara i glos HeyGen w pamieci skilla.")
    ap.add_argument("--szukaj", default=DOMYSLNE_IMIE,
                    help=f"fragment nazwy awatara i glosu (domyslnie „{DOMYSLNE_IMIE}”)")
    ap.add_argument("--awatar-id", dest="awatar_id",
                    help="zapisz ten avatar_id (albo talking_photo_id) bez szukania po nazwie")
    ap.add_argument("--glos-id", dest="glos_id",
                    help="zapisz ten voice_id bez szukania po nazwie")
    ap.add_argument("--tylko-pokaz-konto", action="store_true",
                    help="wypisz awatary i glosy z konta, niczego nie zapisuj")
    ap.add_argument("--pokaz", action="store_true",
                    help="pokaz, co skill juz pamieta, i zakoncz")
    ap.add_argument("--zapomnij", action="store_true",
                    help="usun zapamietanego awatara i glos HeyGen z pamieci skilla")
    a = ap.parse_args()

    if a.pokaz:
        print(konfiguracja.opisz())
        return 0
    if a.zapomnij:
        return zapomnij()

    klucz()                                             # czytelny blad, gdy brak klucza
    dziala, powod = siec_przepuszcza()
    if not dziala:
        print(f"Siec nie przepuszcza polaczen do api.heygen.com ({powod}).\n"
              "To blokada srodowiska, nie problem z kluczem — tutaj sie nie uda.\n"
              "Uruchom to polecenie na wlasnym komputerze albo zmien polityke sieciowa\n"
              "srodowiska. Zlacze MCP HeyGen dziala mimo tej blokady, bo laczy sie spoza\n"
              "kontenera.", file=sys.stderr)
        return 3

    awatary, glosy = pobierz_awatary(), pobierz_glosy()

    if a.tylko_pokaz_konto:
        wypisz("AWATARY I ZDJECIA MOWIACE", awatary)
        wypisz("GLOSY", glosy)
        return 0

    if a.awatar_id:
        awatar = next((p for p in awatary if p["id"] == a.awatar_id), None)
        if not awatar:
            print(f"Na koncie nie ma awatara o id {a.awatar_id}.", file=sys.stderr)
            wypisz("Dostepne:", awatary)
            return 1
    else:
        awatar = wybierz(awatary, a.szukaj, "awatar")

    if a.glos_id:
        glos = next((p for p in glosy if p["id"] == a.glos_id), None)
        if not glos:
            print(f"Na koncie nie ma glosu o id {a.glos_id}.", file=sys.stderr)
            wypisz("Dostepne:", glosy)
            return 1
    else:
        glos = wybierz(glosy, a.szukaj, "glos")

    if not awatar and not glos:
        return 1

    pola = {}
    if awatar:
        pola.update(heygen_avatar_id=awatar["id"], heygen_avatar_name=awatar["nazwa"],
                    heygen_avatar_rodzaj=awatar["rodzaj"])
    if glos:
        pola.update(heygen_voice_id=glos["id"], heygen_voice_name=glos["nazwa"])
    sciezka = konfiguracja.zapisz(utworzono=str(date.today()), **pola)

    print("\nGotowe. Skill pamieta:")
    if awatar:
        print(f"  awatar: {awatar['nazwa']}  ({awatar['rodzaj']}, {awatar['id']})")
    if glos:
        print(f"  glos:   {glos['nazwa']}  ({glos['id']})")
    print(f"  plik:   {sciezka}")
    if not glos:
        print("\n  Glosu nie zapisalam — awatar bedzie mowil dzwiekiem z ElevenLabs\n"
              "  (`--audio`) albo wskaz glos recznie: --glos-id <id>")
    print("\nOd teraz film robisz tak:\n"
          "  python3 ../../dane-i-glos/scripts/heygen_awatar.py narracja.txt --czekaj -o film.mp4\n"
          "— awatar i glos ida z pamieci. Sprawdzic pamiec: --pokaz")
    return 0


if __name__ == "__main__":
    sys.exit(main())
