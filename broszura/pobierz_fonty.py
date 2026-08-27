# -*- coding: utf-8 -*-
"""
Pobiera kroje pisma z Google Fonts i zapisuje je w pliku broszura/fonty.py
jako CSS z osadzonymi danymi. Dzięki temu broszura wygląda tak samo
bez dostępu do internetu — także przy drukowaniu i tworzeniu PDF.

Uruchom raz:  python3 broszura/pobierz_fonty.py
"""
import base64
import os
import re
import urllib.request

BAZA = os.path.dirname(os.path.abspath(__file__))
URL = ("https://fonts.googleapis.com/css2?"
       "family=Atkinson+Hyperlegible:wght@400;700&"
       "family=Nunito:wght@700;800;900&display=swap")
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/120.0.0.0 Safari/537.36")
# polskie znaki mieszczą się w latin + latin-ext
ZAKRESY = ("latin", "latin-ext")


def pobierz(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def main():
    arkusz = pobierz(URL).decode("utf-8")
    bloki = re.split(r"/\*\s*([a-z0-9-]+)\s*\*/", arkusz)
    wynik, wagi = [], []
    for i in range(1, len(bloki) - 1, 2):
        nazwa_zakresu, blok = bloki[i], bloki[i + 1]
        if nazwa_zakresu not in ZAKRESY:
            continue
        m = re.search(r"url\((https://[^)]+\.woff2)\)", blok)
        if not m:
            continue
        dane = base64.b64encode(pobierz(m.group(1))).decode("ascii")
        blok = blok.replace(m.group(1), f"data:font/woff2;base64,{dane}")
        blok = re.sub(r"\s*\n\s*", " ", blok).strip()
        wynik.append(blok)
        rodzina = re.search(r"font-family:\s*'([^']+)'", blok).group(1)
        waga = re.search(r"font-weight:\s*([0-9 ]+)", blok).group(1).strip()
        wagi.append(f"{rodzina} {waga} ({nazwa_zakresu})")

    css = "\n".join(wynik)
    sciezka = os.path.join(BAZA, "fonty.py")
    with open(sciezka, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""Kroje pisma osadzone w pliku. Generowane przez pobierz_fonty.py."""\n')
        f.write("CSS_FONTY = " + repr(css) + "\n")

    print(f"Zapisano {len(wynik)} krojów ({os.path.getsize(sciezka)//1024} KB):")
    for w in wagi:
        print("  ·", w)


if __name__ == "__main__":
    main()
