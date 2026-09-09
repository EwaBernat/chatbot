#!/usr/bin/env python3
"""Pobiera fonty z Google Fonts i zapisuje je jako fonts.css z osadzonymi data URI.

build.py wymaga tego pliku obok siebie — przeglądarka renderująca PDF nie ma
dostępu do sieci, więc fonty muszą siedzieć w samym HTML-u.
"""
import base64
import os
import re
import urllib.request

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/131.0.0.0 Safari/537.36")
URL = ("https://fonts.googleapis.com/css2?"
       "family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800"
       "&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600"
       "&family=IBM+Plex+Mono:wght@500;600&display=swap")


def get(url):
    return urllib.request.urlopen(
        urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60).read()


def main():
    css = get(URL).decode()
    for u in sorted(set(re.findall(r"url\((https://[^)]+)\)", css))):
        css = css.replace(u, "data:font/woff2;base64," + base64.b64encode(get(u)).decode())
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts.css")
    open(out, "w", encoding="utf-8").write(css)
    print("zapisano", out, round(os.path.getsize(out) / 1048576, 2), "MB")


if __name__ == "__main__":
    main()
