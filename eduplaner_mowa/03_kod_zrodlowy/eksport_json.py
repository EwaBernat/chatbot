# -*- coding: utf-8 -*-
"""Eksport banku celów SMART — rozwój mowy (MOWA) — do plików JSON.

    python3 03_kod_zrodlowy/eksport_json.py            # zapisuje do 01_dane_json/
    python3 03_kod_zrodlowy/eksport_json.py --sprawdz  # tylko liczby, bez zapisu

Kształt plików jest ten sam co w module ABC/FBA — aplikacja czyta oba moduły
tym samym kodem. Wpina się `01_dane_json`; HTML z `02_gotowe_dokumenty` jest
wzorcem wyglądu, nie źródłem.

Ścieżki mediów liczone są od katalogu `04_media/`, dokładnie jak w FBA.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import dane_zrodlowe as dz  # noqa: E402

KATALOG = pathlib.Path(__file__).resolve().parent.parent / "01_dane_json"
KAT_SYMBOLI = "eduplaner_przedszkole/assets/symbole"   # biblioteka wspólna z bankiem KPOF
KAT_AUDIO = "eduplaner_mowa/assets/audio_mowa"
KAT_POMOCY = "eduplaner_mowa/assets/pomoce_mowa"

RZYM = {"I": "i", "II": "ii", "III": "iii", "IV": "iv", "V": "v", "VI": "vi", "VII": "vii"}


def klucz_wskaznika(w) -> tuple[str, str]:
    """VII.3 -> ('VII', '3')"""
    obszar, nr = w["nr"].split(".")
    return obszar, nr


def id_konspektu(w, wersja: str) -> str:
    obszar, nr = klucz_wskaznika(w)
    return f"kon-{wersja}-{obszar}-{nr}"


def sciezka_audio(w, wersja: str) -> str:
    obszar, nr = klucz_wskaznika(w)
    return f"{KAT_AUDIO}/{wersja.lower()}{RZYM[obszar]}_{nr}.mp3"


def sciezka_zdjecia(w) -> str:
    obszar, nr = klucz_wskaznika(w)
    return f"{KAT_POMOCY}/k_{RZYM[obszar]}_{nr}.jpg"


def tekst_do_nagrania(polecenie: str) -> str:
    """Zapis polecenia pod lektora — to NIE jest tekst, który dziecko widzi.

    Węzeł TTS nie ma pokręteł tempa ani ekspresji: jedno i drugie ustawia się
    treścią. Dlatego kropka między krokami zamienia się w wielokropek (dłuższa,
    słyszalna pauza — dziecko ma czas wykonać krok), a znacznik [warmly] mówi
    modelowi eleven_v3, jakim tonem czytać. Znacznik nie jest wypowiadany na głos;
    sprawdzone transkrypcją nagrania.

    Drukowany tekst zostaje czysty — patrz `polecenie_dla_dziecka`.
    """
    mowione = polecenie.replace(". ", "… ").replace("? ", "? … ").replace("! ", "! … ")
    return f"[warmly] {mowione}"


def plik_symbolu(symbol) -> str | None:
    return f"{KAT_SYMBOLI}/k_{symbol}.jpg" if symbol else None


def historyjka(nr: str) -> dict | None:
    """Historyjka obrazkowa, drabina albo skala — tylko przy tych wskaźnikach,
    których pomoc naprawdę ich wymaga. Rysunek jest bez tekstu, podpis polski
    dokłada dokument, więc tutaj sklejamy jedno z drugim i dopisujemy ścieżkę."""
    h = getattr(dz, "HISTORYJKI", {}).get(nr)
    if not h:
        return None

    def pole(p):
        return {**p, "plik": f"{dz.KAT_ARKUSZY}/{p['plik']}"}

    wynik = {"rodzaj": h["rodzaj"], "tytul": h["tytul"],
             "po_co_dla_doroslego": h["po_co"], "jak_uzyc_dla_doroslego": h["jak_uzyc"]}
    if "pola" in h:
        wynik["pola"] = [pole(p) for p in h["pola"]]
    else:
        wynik["wiersze"] = [{"nazwa": w["nazwa"], "poczatek": pole(w["poczatek"]),
                             "zakonczenia": [pole(z) for z in w["zakonczenia"]]}
                            for w in h["wiersze"]]
    return wynik


def poziomy_lista() -> list[dict]:
    return [{"klucz": k, "nazwa": v["nazwa"], "rzym": v["rzym"], "kryterium": v["kryterium"],
             "horyzont": v["horyzont"], "warunki": v["warunki"], "kolor_oceny": v["kolor"]}
            for k, v in dz.POZIOMY.items()]


def wersje_lista() -> list[dict]:
    return [{"klucz": k, "wiek": v["wiek"], "czas": v["czas"], "forma": v["forma"],
             "cykl": v["cykl"], "jezyk": v["jezyk"]} for k, v in dz.WERSJE.items()]


def wskazniki_obszaru(nr_k: str) -> list[dict]:
    return [w for w in dz.WSKAZNIKI if w["obszar"] == nr_k]


# --- 1. cele w trzech wersjach wiekowych i trzech poziomach (druk MOWA-T) ----
def cele_poziomy() -> dict:
    obszary = []
    for nr, z in dz.OBSZARY.items():
        wskazniki = []
        for w in wskazniki_obszaru(nr):
            wskazniki.append({
                "nr": w["nr"],
                "pozycja": w["pozycja"],
                "wskaznik": w["wskaznik"],
                # Odpowiednik `zachowanie_zastepcze` z modułu ABC/FBA — bez tego pola
                # cel opisuje zanik objawu i przestaje być celem z tego banku:
                "krok_komunikacyjny": w["krok_komunikacyjny"],
                "opis_kroku": w["opis_kroku"],
                "cele": w["cele"],
                "zalecenia": w["zalecenia"],
                "dostosowania": w["dostosowania"],
                "uwaga_rozwojowa": w["uwaga_rozwojowa"],
                "konspekty": {wersja: id_konspektu(w, wersja) for wersja in dz.WERSJE},
                "pomoc_id": w["nr"],
                "arkusz_id": w["nr"],
            })
        obszary.append({"nr": nr, "nazwa": z["nazwa"], "icf": z["icf"], "pp": z["pp"],
                           "norma_rozwojowa": z["norma"], "opis": z["opis"],
                           "zasada_mowy": z["zasada_mowy"], "wskazniki": wskazniki})
    return {
        "dokument": "EduPlaner 2026 · druk MOWA-T · cele SMART wiek × poziom wsparcia",
        "opis": ("Poziom wsparcia zmienia warunki, nie krok komunikacyjny. Kryterium na "
                 "Poziomie I zostaje 4 z 5 — rośnie trudność zachowania, nie liczba prób."),
        "modul": dz.MODUL,
        "poziomy_wsparcia": poziomy_lista(),
        "wersje_wiekowe": wersje_lista(),
        "tory_zajec": dz.TORY_ZAJEC,
        "rodzaje_zajec": dz.RODZAJE_ZAJEC,
        "liczba_celow": len(dz.WSKAZNIKI) * len(dz.WERSJE) * len(dz.POZIOMY),
        "obszary": obszary,
    }


# --- 2. cele do obserwacji pogłębionej (druk MOWA-C) ------------------------
def cele_obserwacja() -> dict:
    obszary = []
    for nr, z in dz.OBSZARY.items():
        wskazniki = []
        for w in wskazniki_obszaru(nr):
            o = w["obserwacja"]
            wskazniki.append({
                "nr": w["nr"],
                "pozycja": w["pozycja"],
                "deficyt": w["wskaznik"],
                "krok_komunikacyjny": w["krok_komunikacyjny"],
                "cel": o["cel"],
                "znaczniki": ["{proba}", "{horyzont_dopelniacz}", "{horyzont_miejscownik}"],
                "co_obserwowac": o["co_obserwowac"],
                "ile_sytuacji": o["ile_sytuacji"],
                "smart": [{"litera": k, "tresc": v} for k, v in o["smart"].items()],
                "zalecenia": w["zalecenia"],
                "dostosowania": w["dostosowania"],
                "uwaga_rozwojowa": w["uwaga_rozwojowa"],
            })
        obszary.append({"nr": nr, "nazwa": z["nazwa"], "icf": z["icf"], "skala": "wynik 0–10",
                           "norma_rozwojowa": z["norma"], "opis": z["opis"],
                           "zasada_mowy": z["zasada_mowy"], "wskazniki": wskazniki})
    return {
        "dokument": "EduPlaner 2026 · druk MOWA-C · cele SMART do obserwacji pogłębionej",
        "opis": ("Ciąg dalszy rozwoju mowy. Kryterium prób i horyzont ewaluacji NIE są "
                 "stałe — wynikają z punktacji danego zmysłu u konkretnego dziecka, według "
                 "tabeli `progi`. Horyzont jest w trzech formach gramatycznych, bo wchodzi "
                 "w trzy różne zdania."),
        "modul": dz.MODUL,
        "przelicznik_natezenia": dz.PRZELICZNIK,
        "progi": dz.PROGI,
        "liczba_celow": len(dz.WSKAZNIKI),
        "obszary": obszary,
    }


# --- 3. konspekty zajęć (druk KC-3) ----------------------------------------
def konspekty() -> dict:
    rekordy = []
    for w in dz.WSKAZNIKI:
        k = w["konspekt"]
        z = dz.OBSZARY[w["obszar"]]
        for wersja, wu in dz.WERSJE.items():
            wa = k["warianty"][wersja]
            rekordy.append({
                "id": id_konspektu(w, wersja),
                "wskaznik": w["nr"],
                "wersja_wiekowa": wersja,
                "wiek": wu["wiek"],
                "obszar": f"{w['obszar']} · {z['nazwa']}",
                "pozycja": w["pozycja"],
                "tytul": k["tytul"],
                "podtytul": wa["podtytul"],
                "sfera": (f"OBSZAR {w['obszar']} · {z['nazwa'].upper()} · pozycja {w['pozycja']} · "
                          f"krok komunikacyjny: {w['krok_komunikacyjny']} (ICF {z['icf']} · {z['pp']})"),
                "czas": wu["czas"],
                "forma": wu["forma"],
                "cykl": wu["cykl"],
                "cel_terapeutyczny": {
                    "tresc": wa["cel_ter"],
                    "smart": [{"litera": lit, "tresc": wa["smart"][lit]} for lit in "SMART"],
                    "kryterium": wa["kryterium_obs"],
                },
                # Cel edukacyjny czytany na żywo z druku MOWA-T — nie kopiujemy go tutaj:
                "cel_edukacyjny_zrodlo": {
                    "uwaga": ("Cel edukacyjny czytany jest na żywo z druku MOWA-T — nie kopiuj go "
                              "tutaj, bo rozjedzie się po poprawce autorki."),
                    "plik": "cele_mowa_poziomy.json",
                    "sciezka": f"obszary[{w['obszar']}].wskazniki[{w['nr']}].cele[{wersja}]",
                },
                "pomoce": wa["pomoce"],
                "metody": k["metody"],
                "rodzaj_zajec": k["rodzaj_zajec"],
                "przebieg": [{"lp": i, "nauczyciel": p[0], "dziecko": p[1]}
                             for i, p in enumerate(wa["przebieg"], start=1)],
                "modyfikacje": {
                    poz: {"poziom": dz.POZIOMY[poz]["nazwa"],
                          "kroki": [f"{w['cele'][wersja][poz]} — cel z kolumny tabeli",
                                    k["modyfikacje"][poz]]}
                    for poz in dz.POZIOMY
                },
                "wskazowka": k["wskazowka"],
                "bezpieczenstwo": w["uwaga_rozwojowa"],
                "arkusz_id": w["nr"],
                "pomoc_id": w["nr"],
                "nagranie": sciezka_audio(w, wersja),
            })
    return {
        "dokument": "EduPlaner 2026 · druk KC-3 · konspekty zajęć do wskaźników rozwoju mowy",
        "opis": ("Jeden konspekt obsługuje trzy poziomy wsparcia: poziom zmienia sekcję VI "
                 "(modyfikacje), nie przebieg zajęć."),
        "liczba": len(rekordy),
        "konspekty": rekordy,
    }


# --- 4. pomoce dydaktyczne i polecenia dla dziecka --------------------------
def pomoce() -> dict:
    rekordy = []
    for w in dz.WSKAZNIKI:
        p = w["pomoc"]
        rekordy.append({
            "wskaznik": w["nr"],
            "obszar": f"{w['obszar']} · {dz.OBSZARY[w['obszar']]['nazwa']}",
            "pozycja": w["pozycja"],
            "nazwa": p["nazwa"],
            "co_przygotowac": p["co_przygotowac"],
            "trzy_kroki_uzycia": p["trzy_kroki_uzycia"],
            "wskazowka_dla_doroslego": p["wskazowka_dla_doroslego"],
            "bezpieczenstwo": w["uwaga_rozwojowa"],
            "zdjecie": sciezka_zdjecia(w),
            "opis_zdjecia": p["opis_zdjecia"],
            "polecenia": {
                wersja: {"wiek": dz.WERSJE[wersja]["wiek"],
                         "polecenie_dla_dziecka": p["polecenia"][wersja],
                         "polecenie_do_nagrania": tekst_do_nagrania(p["polecenia"][wersja]),
                         "nagranie": sciezka_audio(w, wersja)}
                for wersja in dz.WERSJE
            },
            "arkusz_id": w["nr"],
            "historyjka": historyjka(w["nr"]),
        })
    return {
        "dokument": "EduPlaner 2026 · druk KC-4 · pomoce dydaktyczne do wskaźników rozwoju mowy",
        "opis": ("Trzy kroki użycia i wskazówkę czyta DOROSŁY, polecenie mówi się DZIECKU — i to "
                 "polecenie jest nagrane głosem autorki. Nagrania to dane biometryczne: nie "
                 "publikuj ich poza uzgodnionym zastosowaniem."),
        "liczba_pomocy": len(rekordy),
        "liczba_nagran": len(rekordy) * len(dz.WERSJE),
        "pomoce": rekordy,
    }


# --- 5. materiały A4 do wycięcia -------------------------------------------
def materialy_do_druku() -> dict:
    rekordy, z_obrazkiem, puste = [], 0, 0
    for w in dz.WSKAZNIKI:
        a = w["arkusz"]
        karty = []
        for karta in a["karty"]:
            plik = plik_symbolu(karta["symbol"])
            z_obrazkiem += 1 if plik else 0
            puste += 0 if plik else 1
            karty.append({
                "etykieta_dla_dziecka": karta["etykieta"],
                "opis_dla_doroslego": karta["opis"],
                "symbol": karta["symbol"],
                "plik_symbolu": plik,
            })
        pasek = []
        for pole in a["pasek_kolejnosci"]:
            plik = plik_symbolu(pole["symbol"])
            z_obrazkiem += 1 if plik else 0
            puste += 0 if plik else 1
            pasek.append({"etykieta_dla_dziecka": pole["etykieta"], "symbol": pole["symbol"],
                          "plik_symbolu": plik})
        rekordy.append({
            "wskaznik": w["nr"],
            "tytul": a["tytul"],
            "wstep_dla_doroslego": a["wstep_dla_doroslego"],
            "karty": karty,
            "pasek_kolejnosci": pasek,
            "historyjka": historyjka(w["nr"]),
            "format": "A4 pionowo, karton 200 g",
        })
    return {
        "dokument": "EduPlaner 2026 · materiały A4 do wycięcia przy konspektach rozwoju mowy",
        "opis": ("Etykiety kart widzi DZIECKO — pisane są prostym językiem. Opisy pod polami "
                 "i wstęp czyta dorosły. Symbole pochodzą z biblioteki banku KPOF: ten sam "
                 "obrazek musi być tu, na tablicy AAC i w planie dnia."),
        "biblioteka_symboli": {
            "katalog": KAT_SYMBOLI,
            "przypisanych": z_obrazkiem + puste,
            "z_obrazkiem": z_obrazkiem,
            "pol_celowo_pustych": puste,
            "uwaga": "Pole puste = miejsce na własny symbol dziecka z jego tablicy AAC.",
        },
        "liczba_arkuszy": len(rekordy),
        "arkusze": rekordy,
    }


# --- 6. kontrakt na własne konspekty nauczycielki ---------------------------
def wlasne_konspekty_kontrakt() -> dict:
    return {
        "dokument": "EduPlaner 2026 · kontrakt rekordu własnego konspektu (rozwój mowy (MOWA))",
        "opis": ("Kształt rekordu, w którym nauczycielka zapisuje własny scenariusz do celu "
                 "z tabeli MOWA-T. Druk MOWA-T zapisuje takie konspekty w pamięci przeglądarki "
                 "(klucz `eduplaner2026.moje-konspekty-mowa.v1`); aplikacja ma je czytać z tego "
                 "samego kształtu."),
        "klucz_magazynu": "eduplaner2026.moje-konspekty-mowa.v1",
        "kontrakt": {
            "id": "string — prefiks mks, nadawany przy zapisie",
            "nr": "string — wskaźnik, np. VI.2",
            "wersja": "string — A | B | C",
            "poziom": "string — p3 | p2 | p1 (poziom, z którego wyszedł formularz)",
            "obszar": "string — I…V",
            "krok_komunikacyjny": "string — krok komunikacyjny wskaźnika, kopiowany z tabeli",
            "tytul": "string — do 120 znaków",
            "podtytul": "string | pusty",
            "czas": "string — np. 15 min",
            "forma": "string",
            "cykl": "string — np. 3× w tygodniu",
            "ter": "string — cel terapeutyczny",
            "kryt": "string — kryterium obserwacji",
            "pomoce": "array[string]",
            "metody": "array[string]",
            "rodzaj": "string — rodzaj zajęć wg prawa oświatowego",
            "przebieg": "array[[nauczyciel, dziecko]] — pary tekstów",
            "mody": {"p3": "array[string]", "p2": "array[string]", "p1": "array[string]"},
            "wskazowka": "string",
            "data": "string ISO 8601",
        },
        "walidacja": [
            "nr musi istnieć w cele_mowa_poziomy.json",
            "cel edukacyjny czytany jest z tabeli po (nr, wersja, poziom) — nie zapisuje się go w rekordzie",
            "polecenie dla dziecka: krótkie zdania, bez terminów fachowych",
            "przy wskaźnikach VI i VII pole bezpieczeństwa wypełnia się obowiązkowo",
        ],
    }


PLIKI = {
    "cele_mowa_obserwacja.json": cele_obserwacja,
    "cele_mowa_poziomy.json": cele_poziomy,
    "konspekty_mowa.json": konspekty,
    "pomoce_mowa.json": pomoce,
    "materialy_do_druku.json": materialy_do_druku,
    "wlasne_konspekty_kontrakt.json": wlasne_konspekty_kontrakt,
}


def main() -> int:
    ap = argparse.ArgumentParser(description="Eksport banku celów SMART rozwoju mowy do JSON")
    ap.add_argument("--sprawdz", action="store_true", help="policz rekordy, nie zapisuj plików")
    ap.add_argument("--katalog", default=str(KATALOG), help="katalog docelowy")
    args = ap.parse_args()

    katalog = pathlib.Path(args.katalog)
    if not args.sprawdz:
        katalog.mkdir(parents=True, exist_ok=True)

    for nazwa, budowa in PLIKI.items():
        dane = budowa()
        if args.sprawdz:
            liczby = {k: v for k, v in dane.items() if k.startswith("liczba")}
            print(f"{nazwa:34} {liczby or '(kontrakt)'}")
            continue
        sciezka = katalog / nazwa
        sciezka.write_text(json.dumps(dane, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"zapisano {sciezka.relative_to(katalog.parent)}  ({sciezka.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
