# -*- coding: utf-8 -*-
"""Osadzanie zdjęć i grafik rastrowych w broszurze.

Obrazy wchodzą do pliku HTML jako `data:` URI, żeby broszura pozostała jednym
samodzielnym dokumentem — bez folderu z grafikami, który łatwo zgubić przy
przesyłaniu nauczycielom.

Wymiary czytamy z nagłówka pliku, bez żadnej biblioteki zewnętrznej: proporcje
są potrzebne, bo skład wymusza je pudełkiem `padding-bottom`, a bez nich
strona rozjeżdża się przy druku.
"""
import base64
import os
import struct

MIME = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
        ".webp": "image/webp", ".gif": "image/gif", ".svg": "image/svg+xml"}


def wymiary(dane):
    """Zwraca (szerokość, wysokość) z nagłówka PNG, JPEG, GIF albo WebP."""
    if dane[:8] == b"\x89PNG\r\n\x1a\n":
        w, h = struct.unpack(">II", dane[16:24])
        return w, h
    if dane[:3] == b"\xff\xd8\xff":                       # JPEG
        i = 2
        while i < len(dane) - 9:
            if dane[i] != 0xFF:
                i += 1
                continue
            znacznik = dane[i + 1]
            if znacznik in (0xD8, 0xD9) or 0xD0 <= znacznik <= 0xD7:
                i += 2
                continue
            dlugosc = struct.unpack(">H", dane[i + 2:i + 4])[0]
            if znacznik in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                            0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                h, w = struct.unpack(">HH", dane[i + 5:i + 9])
                return w, h
            i += 2 + dlugosc
        return None
    if dane[:6] in (b"GIF87a", b"GIF89a"):
        w, h = struct.unpack("<HH", dane[6:10])
        return w, h
    if dane[:4] == b"RIFF" and dane[8:12] == b"WEBP":
        f = dane[12:16]
        if f == b"VP8 ":
            w, h = struct.unpack("<HH", dane[26:30])
            return w & 0x3FFF, h & 0x3FFF
        if f == b"VP8L":
            b0, b1, b2, b3 = dane[21], dane[22], dane[23], dane[24]
            w = ((b1 & 0x3F) << 8 | b0) + 1
            h = ((b3 & 0x0F) << 10 | b2 << 2 | (b1 & 0xC0) >> 6) + 1
            return w, h
        if f == b"VP8X":
            w = int.from_bytes(dane[24:27], "little") + 1
            h = int.from_bytes(dane[27:30], "little") + 1
            return w, h
    return None


def osadz(sciezka, katalog=None):
    """Wczytuje plik graficzny i zwraca (data_uri, szerokość, wysokość).

    Rzuca czytelnym błędem, gdy pliku nie ma albo formatu nie da się zmierzyć —
    lepiej zatrzymać skład niż wypuścić broszurę z rozjechaną stroną.
    """
    p = sciezka
    if katalog and not os.path.isabs(p):
        kandydat = os.path.join(katalog, p)
        if os.path.exists(kandydat):
            p = kandydat
    if not os.path.exists(p):
        raise SystemExit(f"BŁĄD: nie znaleziono pliku graficznego „{sciezka}”"
                         + (f" (szukałem też w {katalog})" if katalog else ""))
    rozsz = os.path.splitext(p)[1].lower()
    if rozsz not in MIME:
        raise SystemExit(f"BŁĄD: nieobsługiwany format „{rozsz}”. "
                         f"Użyj: {', '.join(sorted(MIME))}")
    dane = open(p, "rb").read()
    if rozsz == ".svg":
        return ("data:image/svg+xml;base64," + base64.b64encode(dane).decode(), 4, 3)
    wym = wymiary(dane)
    if not wym:
        raise SystemExit(f"BŁĄD: nie umiem odczytać wymiarów pliku „{p}”. "
                         "Zapisz go ponownie jako PNG albo JPEG.")
    return ("data:" + MIME[rozsz] + ";base64," + base64.b64encode(dane).decode(), wym[0], wym[1])


def rozmiar_mb(sciezka, katalog=None):
    p = os.path.join(katalog, sciezka) if katalog and not os.path.isabs(sciezka) else sciezka
    return os.path.getsize(p) / 1024 / 1024 if os.path.exists(p) else 0.0
