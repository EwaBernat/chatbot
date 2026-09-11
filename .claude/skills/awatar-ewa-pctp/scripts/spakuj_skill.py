#!/usr/bin/env python3
"""Sklada samodzielny pakiet Skill „awatar-ewa" do wgrania na claude.ai (plik .skill).

Laczy w jeden katalog: postac (awatar-ewa-pctp), render (awatar-ewa) i potrzebne skrypty
z dane-i-glos (pamiec, HeyGen REST, ElevenLabs TTS). Sciezki miedzy skillami sa
przepisane tak, zeby wszystko dzialalo z jednego katalogu `scripts/`.

Przyklad:
    python3 spakuj_skill.py ~/pakiety          # -> ~/pakiety/awatar-ewa/ i ~/pakiety/awatar-ewa.skill
    python3 spakuj_skill.py ~/pakiety --bez-webm   # lzejszy pakiet, bez klipu intro (ok. 1,5 MB)
"""

from __future__ import annotations

import argparse
import shutil
import sys
import zipfile
from pathlib import Path

SKILLE = Path(__file__).resolve().parents[2]
PCTP = SKILLE / "awatar-ewa-pctp"
EWA = SKILLE / "awatar-ewa"
DIG = SKILLE / "dane-i-glos" / "scripts"

SKRYPTY = {
    PCTP / "scripts" / "wytnij_postac.py": "wytnij_postac.py",
    PCTP / "scripts" / "wstaw_ewe.py": "wstaw_ewe.py",
    PCTP / "scripts" / "ewa_do_prezentacji.py": "ewa_do_prezentacji.py",
    PCTP / "scripts" / "zapamietaj_awatara.py": "zapamietaj_awatara.py",
    EWA / "scripts" / "skonfiguruj_awatara.py": "skonfiguruj_awatara.py",
    DIG / "konfiguracja.py": "konfiguracja.py",
    DIG / "heygen_awatar.py": "heygen_awatar.py",
    DIG / "elevenlabs_tts.py": "elevenlabs_tts.py",
}
REFERENCJE = [PCTP / "references" / "postac.md", PCTP / "references" / "produkcja.md",
              EWA / "references" / "scenariusz.md", EWA / "references" / "prompt-agenta.md",
              EWA / "references" / "mcp.md", EWA / "references" / "lokalnie.md"]
ZASOBY = ["ewa_pctp.png", "ewa_pctp_intro.webm", "intro_tekst.txt", "ewa_kadr.jpg", "ewa_gesty.jpg"]


def przepisz_sciezki(nazwa: str, tekst: str) -> str:
    """Skrypty z roznych skilli leza teraz obok siebie — kazdy szuka sasiadow w swoim katalogu."""
    lokalnie = 'Path(__file__).resolve().parent'
    if nazwa == "skonfiguruj_awatara.py":
        tekst = tekst.replace(
            'SASIAD = Path(__file__).resolve().parents[2] / "dane-i-glos" / "scripts"',
            f'SASIAD = {lokalnie}')
        # w pakiecie sasiad zawsze istnieje — kontrola katalogu jest zbedna
        poczatek = tekst.find("if not SASIAD.is_dir():")
        koniec = tekst.find("sys.path.insert(0, str(SASIAD))")
        if poczatek != -1 and koniec != -1:
            tekst = tekst[:poczatek] + tekst[koniec:]
    if nazwa == "zapamietaj_awatara.py":
        tekst = tekst.replace(
            'SKRYPTY_DANE_I_GLOS = Path(__file__).resolve().parents[2] / "dane-i-glos" / "scripts"',
            f'SKRYPTY_DANE_I_GLOS = {lokalnie}')
        tekst = tekst.replace(
            'SKONFIGURUJ_AWATARA = Path(__file__).resolve().parents[2] / "awatar-ewa" / "scripts" / "skonfiguruj_awatara.py"',
            f'SKONFIGURUJ_AWATARA = {lokalnie} / "skonfiguruj_awatara.py"')
    if nazwa == "konfiguracja.py":
        tekst = tekst.replace("(skill awatar-ewa)", "").replace("(skill awatar-ewa-pctp)", "")
    return tekst


def zbuduj(cel: Path, bez_webm: bool) -> Path:
    if cel.exists():
        shutil.rmtree(cel)
    (cel / "scripts").mkdir(parents=True)
    (cel / "references").mkdir()
    (cel / "assets").mkdir()

    shutil.copy(PCTP / "pakiet" / "SKILL.md", cel / "SKILL.md")
    shutil.copy(PCTP / "requirements.txt", cel / "requirements.txt")
    for zrodlo, nazwa in SKRYPTY.items():
        tekst = zrodlo.read_text(encoding="utf-8")
        (cel / "scripts" / nazwa).write_text(przepisz_sciezki(nazwa, tekst), encoding="utf-8")
    for plik in REFERENCJE:
        shutil.copy(plik, cel / "references" / plik.name)
    for nazwa in ZASOBY:
        if bez_webm and nazwa.endswith(".webm"):
            continue
        shutil.copy(PCTP / "assets" / nazwa, cel / "assets" / nazwa)
    if bez_webm:
        tekst = (cel / "SKILL.md").read_text(encoding="utf-8")
        tekst = tekst.replace(
            "| `assets/ewa_pctp_intro.webm` | intro (13 s) z kanałem alfa, z oryginalnym dźwiękiem | wstawka wideo, czołówka szkolenia |\n",
            "")
        (cel / "SKILL.md").write_text(tekst, encoding="utf-8")
    return cel


def spakuj(katalog: Path) -> Path:
    plik = katalog.with_suffix(".skill")
    with zipfile.ZipFile(plik, "w", zipfile.ZIP_DEFLATED) as zf:
        for sciezka in sorted(katalog.rglob("*")):
            if sciezka.is_file() and "__pycache__" not in sciezka.parts:
                zf.write(sciezka, sciezka.relative_to(katalog.parent))
    return plik


def main() -> int:
    ap = argparse.ArgumentParser(description="Zloz pakiet Skill awatar-ewa (.skill).")
    ap.add_argument("wyjscie", type=Path, help="katalog, w ktorym powstanie awatar-ewa/ i awatar-ewa.skill")
    ap.add_argument("--bez-webm", dest="bez_webm", action="store_true",
                    help="pomin klip intro z alfa (pakiet ok. 1,5 MB zamiast ok. 6 MB)")
    a = ap.parse_args()

    brak = [str(p) for p in list(SKRYPTY) + REFERENCJE if not p.exists()]
    if brak:
        print("Brakuje plikow zrodlowych:\n  " + "\n  ".join(brak), file=sys.stderr)
        return 1
    katalog = zbuduj(a.wyjscie / "awatar-ewa", a.bez_webm)
    plik = spakuj(katalog)
    rozmiar = plik.stat().st_size / 1_048_576
    print(f"Pakiet: {plik} ({rozmiar:.1f} MB)\nKatalog: {katalog}")
    print("Wgranie: claude.ai -> Ustawienia -> Możliwości -> Skills -> Prześlij plik .skill")
    return 0


if __name__ == "__main__":
    sys.exit(main())
