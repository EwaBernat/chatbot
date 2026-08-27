# -*- coding: utf-8 -*-
"""
Przygotowuje zdjęcia do broszury: zmniejsza je i zapisuje jako JPEG,
żeby plik HTML był lekki, a wydruk pozostał ostry.

Wrzuć oryginały (PNG albo JPG) do broszura/zdjecia/ i uruchom:
    python3 broszura/przygotuj_zdjecia.py

Nazwy plików decydują o tym, gdzie zdjęcie trafi w broszurze — spis nazw
znajdziesz w broszura/README.md.
"""
import os
from PIL import Image

BAZA = os.path.dirname(os.path.abspath(__file__))
ZRODLO = os.path.join(BAZA, "zdjecia")
GOTOWE = os.path.join(BAZA, "zdjecia-gotowe")

SZEROKOSC = 1400   # px — wystarcza na wydruk 150 dpi w pełnej szerokości kolumny
JAKOSC = 82


def main():
    os.makedirs(GOTOWE, exist_ok=True)
    if not os.path.isdir(ZRODLO):
        print("Brak katalogu", ZRODLO)
        return

    zrobione = 0
    for nazwa in sorted(os.listdir(ZRODLO)):
        podstawa, rozsz = os.path.splitext(nazwa)
        if rozsz.lower() not in (".png", ".jpg", ".jpeg", ".webp"):
            continue
        cel = os.path.join(GOTOWE, podstawa + ".jpg")
        zrodlo = os.path.join(ZRODLO, nazwa)
        if os.path.exists(cel) and os.path.getmtime(cel) > os.path.getmtime(zrodlo):
            continue

        with Image.open(zrodlo) as im:
            im = im.convert("RGB")
            if im.width > SZEROKOSC:
                wys = round(im.height * SZEROKOSC / im.width)
                im = im.resize((SZEROKOSC, wys), Image.LANCZOS)
            im.save(cel, "JPEG", quality=JAKOSC, optimize=True, progressive=True)
        zrobione += 1
        print(f"  · {podstawa}: {im.width}×{im.height}, "
              f"{os.path.getsize(cel)//1024} KB")

    suma = sum(os.path.getsize(os.path.join(GOTOWE, f))
               for f in os.listdir(GOTOWE) if f.endswith(".jpg"))
    print(f"Przygotowano {zrobione} nowych. Razem w katalogu: "
          f"{len(os.listdir(GOTOWE))} zdjęć, {suma//1024} KB.")


if __name__ == "__main__":
    main()
