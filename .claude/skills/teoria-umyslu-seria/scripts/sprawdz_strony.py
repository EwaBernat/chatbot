#!/usr/bin/env python3
"""Sprawdza, czy każda strona broszury mieści się na arkuszu A4.

Strona A4 nie rozciąga się — treść, która się nie mieści, zostaje ucięta przy druku
bez żadnego ostrzeżenia. Ten skrypt otwiera plik w headless Chromium, zdejmuje ze stron
sztywną wysokość i mierzy ich naturalną wysokość.

    python3 sprawdz_strony.py broszura.html
    python3 sprawdz_strony.py broszura.html --numeruj   # przypisz numery stron w stopkach

Wynik: dla każdej strony zapas w pikselach. Ujemny = przepełnienie.

Pomiar leci przy szerokości okna 1400 px. To nie jest kosmetyka: poniżej 820 px arkusz
stylów przełącza układ na jednokolumnowy i wszystkie wyniki są bezużyteczne.
"""
import argparse, os, re, shutil, subprocess, sys, tempfile

LIMIT_PX = 296.4 / 25.4 * 96  # wysokość strony w druku, w pikselach CSS

PROBE = """<script>window.addEventListener('load',function(){
var o=[],LIM=%f;
document.querySelectorAll('.page').forEach(function(p,i){
  p.style.height='auto';p.style.minHeight='0';p.style.overflow='visible';
  o.push((i+1)+':'+Math.round(LIM-p.offsetHeight));});
var d=document.createElement('pre');d.id='RAPORT';d.textContent=o.join(' ');
document.body.prepend(d);});</script>""" % LIMIT_PX


def znajdz_chromium():
    for kandydat in ("chromium", "chromium-browser", "google-chrome", "chrome"):
        sciezka = shutil.which(kandydat)
        if sciezka:
            return sciezka
    import glob
    for wzor in ("/opt/pw-browsers/chromium-*/chrome-linux/chrome",
                 "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"):
        trafienia = sorted(glob.glob(wzor))
        if trafienia:
            return trafienia[-1]
    sys.exit("Nie znalazłem przeglądarki Chromium/Chrome — bez niej nie zmierzę stron.")


def zmierz(plik):
    html = open(plik, encoding="utf-8").read()
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False,
                                     dir=os.path.dirname(os.path.abspath(plik)),
                                     encoding="utf-8") as f:
        f.write(html + PROBE)
        tmp = f.name
    try:
        out = subprocess.run(
            [znajdz_chromium(), "--headless", "--no-sandbox", "--disable-gpu",
             "--virtual-time-budget=8000", "--window-size=1400,1200",
             "--dump-dom", "file://" + tmp],
            capture_output=True, text=True, timeout=180).stdout
    finally:
        os.unlink(tmp)
    m = re.search(r'id="RAPORT">([^<]*)', out)
    if not m:
        sys.exit("Przeglądarka nie zwróciła pomiaru — sprawdź, czy plik otwiera się poprawnie.")
    return [(int(a), int(b)) for a, b in
            (para.split(":") for para in m.group(1).split())]


def numeruj(plik):
    """Przypisuje numery stron kolejnym stopkom (okładka = 1, nie ma stopki)."""
    s = open(plik, encoding="utf-8").read()
    wzor = re.compile(r'(<span class="num">)([^<]*)(</span>)')
    trafienia = list(wzor.finditer(s))
    wynik, ostatni = [], 0
    for i, m in enumerate(trafienia):
        wynik.append(s[ostatni:m.start()])
        wynik.append(m.group(1) + str(i + 2) + m.group(3))
        ostatni = m.end()
    wynik.append(s[ostatni:])
    open(plik, "w", encoding="utf-8").write("".join(wynik))

    print(f"Ponumerowano {len(trafienia)} stopek (strony 2–{len(trafienia) + 1}).")
    print("\nMapa stron do spisu treści:")
    for i, m in enumerate(trafienia):
        # opis czytamy z ORYGINALNEGO tekstu, bo po przenumerowaniu przesunęłyby się offsety
        kontekst = re.search(r"<b>([^<]*)</b>([^<]*)", s[max(0, m.start() - 400):m.start()])
        opis = (kontekst.group(1) + kontekst.group(2)).strip() if kontekst else "?"
        print(f"  {i + 2:>3}  {opis}")
    print("\nOdsylacze w tresci (np. 'karta obserwacji ze s. 22') popraw recznie -"
          " skrypt ich nie zna.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("plik")
    ap.add_argument("--numeruj", action="store_true",
                    help="przypisz numery stron w stopkach i wypisz mapę do spisu treści")
    a = ap.parse_args()

    if a.numeruj:
        numeruj(a.plik)
        print()

    strony = zmierz(a.plik)
    zle = [(n, v) for n, v in strony if v < 0]
    # okładkę pomijamy: jej blok górny rozciąga się elastycznie na całą stronę
    puste = [(n, v) for n, v in strony if v > 350 and n != 1]

    for n, v in strony:
        if v < 0:
            stan = f"PRZEPEŁNIENIE o {-v} px"
        elif v > 350 and n != 1:
            stan = f"dużo wolnego miejsca ({v} px) — rozważ dołożenie bloku"
        else:
            stan = f"ok, zapas {v} px"
        print(f"  strona {n:>3}: {stan}")

    print()
    if zle:
        print(f"UWAGA: {len(zle)} stron nie mieści się na A4 — przy druku treść zostanie ucięta.")
        print("Przy przepełnieniu powyżej ~250 px przenieś blok na stronę z zapasem")
        print("albo podziel stronę na dwie, zamiast skracać tekst.")
        print("W układzie dwukolumnowym skracaj WYŻSZĄ kolumnę — niższa nie wpływa na wysokość.")
        sys.exit(1)
    print(f"Wszystkie {len(strony)} stron mieści się na A4.")
    if puste:
        print(f"Stron z dużym zapasem: {', '.join(str(n) for n, _ in puste)}.")


if __name__ == "__main__":
    main()
