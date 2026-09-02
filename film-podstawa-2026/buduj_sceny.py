#!/usr/bin/env python3
"""Zamienia narrację na public/film.json — scenariusz jest źródłem czasów.

Każdy nagłówek `# SCENA n · TYTUŁ` zaczyna nową scenę, a jej długość wynika
z liczby słów (polski lektor czyta ok. 150 słów na minutę) plus pauza na
przejście. Dzięki temu poprawka w tekście sama przelicza montaż — nie trzeba
ręcznie pilnować, żeby obraz zmieniał się razem ze zdaniem.

Gdy pojawi się prawdziwe nagranie, uruchom z --audio narracja.mp3: długości
scen zostaną przeskalowane do rzeczywistego czasu trwania pliku.
"""
import argparse, json, pathlib, re, subprocess, sys

SLOW_NA_MINUTE = 150
PAUZA_S = 1.4

# przypisanie scen do typów wizualnych i danych dodatkowych
UKLAD = {
 1:  ("intro",       {}),
 2:  ("fakt",        {"znak": "1 IX 2026", "podpis": "wszystkie grupy jednocześnie"}),
 3:  ("prawo",       {}),
 4:  ("konstrukcja", {}),
 5:  ("przejscie",   {}),
 6:  ("obszar",      {"klucz": "spoleczny",    "nrObszaru": 1}),
 7:  ("obszar",      {"klucz": "osobisty",     "nrObszaru": 2}),
 8:  ("obszar",      {"klucz": "jezykowy",     "nrObszaru": 3}),
 9:  ("obszar",      {"klucz": "matematyczny", "nrObszaru": 4}),
 10: ("obszar",      {"klucz": "przyrodniczy", "nrObszaru": 5}),
 11: ("obszar",      {"klucz": "techniczny",   "nrObszaru": 6}),
 12: ("obszar",      {"klucz": "cyfrowy",      "nrObszaru": 7}),
 13: ("obszar",      {"klucz": "artystyczny",  "nrObszaru": 8}),
 14: ("obszar",      {"klucz": "ruchowy",      "nrObszaru": 9}),
 15: ("filary",      {}),
 16: ("praktyka",    {}),
 17: ("arkusz",      {}),
 18: ("koniec",      {}),
}

def czytaj(sciezka):
    sceny, biezaca = [], None
    for linia in pathlib.Path(sciezka).read_text(encoding="utf-8").splitlines():
        naglowek = re.match(r"#\s*SCENA\s+(\d+)\s*·\s*(.+?)\s*\(", linia)
        if naglowek:
            biezaca = {"nr": int(naglowek.group(1)),
                       "tytul": naglowek.group(2).strip(),
                       "zdania": []}
            sceny.append(biezaca)
        elif linia.strip() and not linia.startswith("#") and biezaca:
            biezaca["zdania"].append(linia.strip())
    return sceny

def dlugosc_audio(sciezka):
    """Czyta długość nagrania. Woli ffprobe, a gdy go nie ma — wyciąga czas
    z komunikatu ffmpeg, bo w kontenerach częściej jest sam ffmpeg."""
    import re, shutil
    if shutil.which("ffprobe"):
        w = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                            "-of","csv=p=0", sciezka], capture_output=True, text=True)
        if not w.returncode:
            return float(w.stdout.strip())
    ff = shutil.which("ffmpeg")
    if not ff:
        try:
            import imageio_ffmpeg; ff = imageio_ffmpeg.get_ffmpeg_exe()
        except ImportError:
            sys.exit("Nie znalazłem ffprobe ani ffmpeg — zainstaluj jedno z nich.")
    w = subprocess.run([ff, "-i", sciezka], capture_output=True, text=True)
    m = re.search(r"Duration: (\d+):(\d+):(\d+\.?\d*)", w.stderr)
    if not m: sys.exit(f"Nie odczytałem długości {sciezka}")
    return int(m.group(1))*3600 + int(m.group(2))*60 + float(m.group(3))

def main():
    a = argparse.ArgumentParser()
    a.add_argument("--narracja", default="public/narracja.txt")
    a.add_argument("--audio", help="MP3 z narracją — przeskaluje sceny do jego długości")
    a.add_argument("-o", "--wyjscie", default="public/film.json")
    arg = a.parse_args()

    sceny = czytaj(arg.narracja)
    if not sceny: sys.exit("Nie znalazłem żadnej sceny — sprawdź nagłówki '# SCENA n · ...'")

    for s in sceny:
        slowa = sum(len(z.split()) for z in s["zdania"])
        s["sekundy"] = round(slowa / SLOW_NA_MINUTE * 60 + PAUZA_S, 2)
        s["slowa"] = slowa
        typ, dodatki = UKLAD.get(s["nr"], ("fakt", {}))
        s["typ"] = typ
        s.update(dodatki)

    laczny = sum(s["sekundy"] for s in sceny)
    if arg.audio:
        rzeczywisty = dlugosc_audio(arg.audio)
        wsp = rzeczywisty / laczny
        for s in sceny: s["sekundy"] = round(s["sekundy"] * wsp, 2)
        laczny = rzeczywisty
        print(f"Przeskalowano do nagrania: {rzeczywisty:.1f} s (współczynnik {wsp:.3f})")

    dane = {"fps": 30, "szerokosc": 1920, "wysokosc": 1080,
            "audio": "narracja.mp3", "napisy": "napisy.srt",
            "lacznieSekund": round(laczny, 2), "sceny": sceny}
    pathlib.Path(arg.wyjscie).write_text(
        json.dumps(dane, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{arg.wyjscie}: {len(sceny)} scen, {laczny/60:.1f} min")

if __name__ == "__main__":
    main()
