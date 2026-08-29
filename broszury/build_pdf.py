#!/usr/bin/env python3
"""Składa broszurę do PDF-a gotowego do druku A4.

Chromium renderuje strony wg arkusza @media print, a potem doklejana jest
żywa pagina: sygnatura po lewej i „Strona X z Y" po prawej. Pagina powstaje
tu, a nie w HTML-u, bo przeglądarka nie potrafi powtórzyć elementu na każdej
stronie ani pominąć go na okładce. Numeracja pomija okładkę i tył broszury —
tam pagina tylko brudziłaby kompozycję.

    python3 broszury/build_pdf.py
"""
import pathlib, sys
import pymupdf
from playwright.sync_api import sync_playwright

BASE   = pathlib.Path(__file__).resolve().parent
SRC    = BASE / "cele-smart-przedszkole.html"
OUT    = BASE / "Cele_SMART_w_przedszkolu_PCTP.pdf"
TMP    = BASE / ".preview.html"

SYGNATURA = "EduPlaner 2026 · PCTP Koszalin · Cele SMART w przedszkolu · SMART-P1"
FONT      = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"   # ma polskie znaki
FIOLET    = (0x2D/255, 0x1B/255, 0x69/255)
SZARY     = (0x5B/255, 0x5B/255, 0x72/255)


def render():
    """HTML → PDF przez Chromium, w opakowaniu takim jak w artefakcie."""
    raw = SRC.read_text(encoding="utf-8")
    TMP.write_text(
        '<!doctype html><html lang="pl"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<style>*{box-sizing:border-box}html{color-scheme:light}'
        'body{margin:0;font:14px system-ui}img{max-width:100%}'
        '[hidden]{display:none!important}</style>' + raw + "</body></html>",
        encoding="utf-8")
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
        pg = b.new_page(viewport={"width": 1180, "height": 1200})
        pg.goto(TMP.as_uri())
        pg.wait_for_timeout(3500)          # czas na fonty osadzone w pliku
        pg.emulate_media(media="print")
        pg.pdf(path=str(OUT), format="A4", print_background=True,
               margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        b.close()
    TMP.unlink(missing_ok=True)


def paginate():
    """Dokleja żywą paginę na stronach środka (bez okładki i tyłu broszury)."""
    doc = pymupdf.open(OUT)
    last = doc.page_count - 1                      # tył broszury
    numerowane = [i for i in range(1, last)]
    for nr, i in enumerate(numerowane, start=2):
        p = doc[i]
        y = p.rect.height - 34
        p.draw_line(pymupdf.Point(40, y - 12), pymupdf.Point(p.rect.width - 40, y - 12),
                    color=(0xC9/255, 0xC0/255, 0xDC/255), width=0.5)
        p.insert_text((40, y), SYGNATURA, fontsize=7,
                      fontname="pl", fontfile=FONT, color=SZARY)
        etykieta = f"Strona {nr} z {doc.page_count}"
        szer = pymupdf.get_text_length(etykieta, fontname="helv", fontsize=8)
        p.insert_text((p.rect.width - 40 - szer, y), etykieta, fontsize=8,
                      fontname="pl", fontfile=FONT, color=FIOLET)
    doc.saveIncr()
    return doc.page_count


if __name__ == "__main__":
    render()
    n = paginate()
    print(f"{OUT.name}: {n} stron A4")
