#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Składa gotowe PDF-y modułu EduPlaner — takie, jak wygląda ekran.

    python3 narzedzia/zrob_pdf.py mowa
    python3 narzedzia/zrob_pdf.py fba
    python3 narzedzia/zrob_pdf.py tom --katalog ~/Pulpit/PDF

Po co to jest: wydruk z przeglądarki zależy od jej ustawień — nagłówka z adresem
i datą, skali, marginesów i tego, która zakładka wersji wiekowej była akurat
otwarta. Ten skrypt nie zależy od żadnego z nich. Rozmiar strony bierze z reguły
@page w dokumencie, tła drukuje zawsze, a przed złożeniem tabeli sam ustawia
wybraną wersję wiekową — więc kartka wygląda tak, jak podgląd na ekranie.

Powstaje osiem plików: karty pracy, cele SMART, tabela w trzech wersjach
wiekowych i trzy zeszyty konspektów (po 25 konspektów każdy).
"""
from __future__ import annotations

import argparse
import asyncio
import pathlib
import re
import sys

MM = 96 / 25.4
KORZEN = pathlib.Path(__file__).resolve().parent.parent
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

# Tabela idzie poziomo, reszta pionowo — tak stoi w @page każdego dokumentu.
A4_PION, A4_POZIOM = (210, 297), (279, 192)


def kartek(plik: pathlib.Path) -> int:
    """Liczba kartek w gotowym PDF — po to, żeby porównać ją z podglądem."""
    return len(re.findall(rb"/Type\s*/Page[^s]", plik.read_bytes()))


async def otworz(przegladarka, plik: pathlib.Path, rozmiar):
    szer, wys = rozmiar
    p = await przegladarka.new_page(viewport={"width": round(szer * MM), "height": round(wys * MM)})
    await p.goto(f"file://{plik.resolve()}")
    await p.wait_for_timeout(1800)
    return p


async def zloz(modul: str, katalog: pathlib.Path) -> int:
    from playwright.async_api import async_playwright

    kod = modul.upper()
    zrodla = KORZEN / f"eduplaner_{modul}" / "02_gotowe_dokumenty"
    dok = {
        "karty": zrodla / f"Karty_pracy_{kod}.html",
        "cele": zrodla / f"Cele_SMART_{kod}_obserwacja_poglebiona.html",
        "tabela": zrodla / f"Tabela_celow_{kod}_wiek_poziom.html",
    }
    brak = [str(x) for x in dok.values() if not x.exists()]
    if brak:
        print("Brak dokumentów — uruchom najpierw buildy modułu:", *brak, sep="\n  ")
        return 1

    katalog.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as pw:
        b = await pw.chromium.launch(executable_path=CHROME)

        # ——— dokumenty stronicowane: co strona w podglądzie, to kartka w PDF ———
        for nazwa, plik in [(f"Karty_pracy_{kod}", dok["karty"]), (f"Cele_SMART_{kod}", dok["cele"])]:
            p = await otworz(b, plik, A4_PION)
            stron = await p.evaluate("document.querySelectorAll('.strona').length")
            cel = katalog / f"{nazwa}.pdf"
            await p.pdf(path=str(cel), format="A4", print_background=True, prefer_css_page_size=True)
            zgodne = stron == kartek(cel)
            print(f"{cel.name:<40} podgląd {stron:>3} · PDF {kartek(cel):>3} kartek "
                  f"{'✓' if zgodne else '✗ ROZJAZD'}")
            await p.close()

        # ——— wersje wiekowe czyta się z samego dokumentu, nie z listy w kodzie ———
        p = await otworz(b, dok["tabela"], A4_POZIOM)
        wersje = await p.evaluate("""() => [...document.querySelectorAll('.wersja')].map(s => ({
            klucz: s.dataset.wersja,
            opis: (s.querySelector('caption')?.textContent || s.dataset.wersja).trim()}))""")
        await p.close()

        def slug(opis: str) -> str:
            return re.sub(r"[^0-9A-Za-zĄąĆćĘęŁłŃńÓóŚśŹźŻż]+", "_",
                          opis.split("·")[-1].strip()).strip("_")

        # ——— tabela: osobny plik na wersję, bo na ekranie widać jedną naraz ———
        for w in wersje:
            p = await otworz(b, dok["tabela"], A4_POZIOM)
            await p.evaluate("""w => {
                document.querySelectorAll('.tab').forEach(x =>
                    x.setAttribute('aria-selected', String(x.dataset.wersja === w)));
                document.querySelectorAll('.wersja').forEach(s => { s.hidden = s.dataset.wersja !== w; });
            }""", w["klucz"])
            await p.wait_for_timeout(500)
            cel = katalog / f"Tabela_celow_{kod}_wersja_{w['klucz']}_{slug(w['opis'])}.pdf"
            await p.pdf(path=str(cel), format="A4", landscape=True, print_background=True,
                        prefer_css_page_size=True)
            print(f"{cel.name:<40} {w['opis']} · PDF {kartek(cel)} kartek")
            await p.close()

        # ——— zeszyty konspektów: wszystkie konspekty danej wersji, A4 pionowo ———
        for w in wersje:
            p = await otworz(b, dok["tabela"], A4_PION)
            ile = await p.evaluate("""w => {
                const m = [...document.querySelectorAll('.kmodal[data-wersja="' + w + '"]')];
                m.forEach(x => {
                  x.classList.add('open');
                  // Cel edukacyjny konspekt czyta na żywo z tabeli — przed drukiem
                  // trzeba go wpisać, bo w PDF nie ma już czego czytać.
                  x.querySelectorAll('.kvar').forEach(v => {
                    const t = zTabeli(w, x.dataset.wsk, v.dataset.lvl);
                    v.querySelector('.kon-cel').textContent = t.cel;
                    v.querySelector('.kon-kryt').textContent = t.ram;
                  });
                });
                document.documentElement.classList.add('druk-konspektu');
                return m.length;
            }""", w["klucz"])
            await p.wait_for_timeout(900)
            cel = katalog / f"Konspekty_{kod}_wersja_{w['klucz']}_{slug(w['opis'])}.pdf"
            await p.pdf(path=str(cel), format="A4", print_background=True, prefer_css_page_size=True)
            print(f"{cel.name:<40} {ile} konspektów · PDF {kartek(cel)} kartek")
            await p.close()

        await b.close()
    print(f"\nGotowe — {katalog}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Gotowe PDF-y modułu EduPlaner 2026")
    ap.add_argument("modul", choices=["mowa", "tom", "sens", "fba"], help="który moduł złożyć")
    ap.add_argument("--katalog", default=None,
                    help="katalog docelowy (domyślnie /tmp/<modul>_pdf — POZA repozytorium, "
                         "bo PDF-y odtwarza ten skrypt)")
    a = ap.parse_args()
    kat = pathlib.Path(a.katalog) if a.katalog else pathlib.Path(f"/tmp/{a.modul}_pdf")
    return asyncio.run(zloz(a.modul, kat))


if __name__ == "__main__":
    raise SystemExit(main())
