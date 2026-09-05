# -*- coding: utf-8 -*-
"""Eksport banku celów SMART — profil sensoryczny — do plików JSON.

    python3 03_kod_zrodlowy/eksport_json.py            # zapisuje do 01_dane_json/
    python3 03_kod_zrodlowy/eksport_json.py --sprawdz  # tylko liczby, bez zapisu

To jest jedyna droga, którą treść autorki wchodzi do aplikacji. Wpina się
`01_dane_json`; HTML z `02_gotowe_dokumenty` jest wzorcem wyglądu, nie źródłem.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import dane_zrodlowe as dz  # noqa: E402

KATALOG = pathlib.Path(__file__).resolve().parent.parent / "01_dane_json"
MEDIA = "04_media/eduplaner_sens/assets"
SYMBOLE = "04_media/eduplaner_przedszkole/assets/symbole"   # biblioteka wspólna z bankiem KPOF


def numer(wskaznik) -> str:
    """SENS-07 -> 07"""
    return wskaznik["id"].split("-")[1]


def kontekst_zdanie(wskaznik) -> str:
    k = wskaznik["kontekst"]
    return k[0].upper() + k[1:]


def sciezka_nagrania(wskaznik, poziom) -> str:
    return f"{MEDIA}/audio_sens/as_{numer(wskaznik)}_{poziom}.mp3"


def opis_zmyslu(wskaznik) -> dict:
    z = dz.ZMYSLY[wskaznik["zmysl"]]
    return {"klucz": wskaznik["zmysl"], "nazwa": z["nazwa"], "rzymska": z["rzymska"], "icf": z["icf"]}


def opis_sektora(wskaznik) -> dict:
    s = dz.SEKTORY[wskaznik["sektor"]]
    return {"klucz": wskaznik["sektor"], "nazwa": s["nazwa"], "skrot": s["skrot"], "kierunek": s["kierunek"]}


# --- 1. cele do obserwacji pogłębionej (druk SENS-C) ------------------------
def cele_obserwacja() -> dict:
    cele = []
    for w in dz.WSKAZNIKI:
        strategia = w["strategia_sensoryczna"].rstrip(". ")
        cel = (
            f"{strategia}. Kryterium: {{proba}} obserwowanych sytuacji "
            f"w ciągu {{horyzont_dopelniacz}}; weryfikacja po {{horyzont_miejscownik}}."
        )
        cele.append({
            "id": f"{w['id']}-C",
            "wskaznik_id": w["id"],
            "kod": w["kod"],
            "zmysl": opis_zmyslu(w),
            "sektor": opis_sektora(w),
            "nazwa": w["nazwa"],
            "objawy_z_druku": w["objawy"],
            "opis_dla_doroslego": w["opis_dla_doroslego"],
            # POLE, KTÓREGO NIE WOLNO ZGUBIĆ — bez niego cel traci sens terapeutyczny:
            "strategia_sensoryczna": w["strategia_sensoryczna"],
            "sygnal_dziecka": w["sygnal_dziecka"],
            "kontekst": w["kontekst"],
            "cel": cel,
            "znaczniki_do_podstawienia": ["{proba}", "{horyzont_dopelniacz}", "{horyzont_miejscownik}"],
            "wskaznik_obserwacji": w["wskaznik_obserwacji"],
            "dieta_sensoryczna": w["dieta_sensoryczna"],
            "dostosowania": w["dostosowania"],
            "ryzyko": w["ryzyko"],
            "pomoc_id": f"P-{w['id']}",
            "arkusz_id": f"A-{w['id']}",
        })
    return {
        "modul": dz.MODUL,
        "druk": "SENS-C — cele do obserwacji pogłębionej (profil sensoryczny)",
        "jak_liczyc_kryterium": (
            "Kryterium i horyzont NIE są stałe. Wynikają z sumy punktów zmysłu (0–24) z druku "
            "obserwacji: znajdź pasmo w tabeli `progi` i podstaw `proba` oraz trzy formy "
            "gramatyczne horyzontu w miejsce znaczników w polu `cel`. Horyzont jest w trzech "
            "formach, bo wchodzi w trzy różne zdania — jedna forma dawała w druku dla rodzica "
            "„weryfikacja po 4 tygodni”."
        ),
        "przelicznik_natezenia": "natężenie (0–10) = zaokrąglone (suma zmysłu × 10 / 24)",
        "progi": dz.PROGI,
        "zmysly": dz.ZMYSLY,
        "sektory": dz.SEKTORY,
        "liczba_celow": len(cele),
        "cele": cele,
    }


# --- 2. cele w trzech poziomach wsparcia i trzech wersjach wiekowych (SENS-T)
def cele_poziomy() -> dict:
    cele = []
    for w in dz.WSKAZNIKI:
        for poziom_kod, poziom in dz.POZIOMY.items():
            kryt = dz.KRYTERIA_POZIOMOW[poziom_kod]
            for wiek_kod, wiek in dz.WIEK.items():
                czynnosc = w["czynnosc"][wiek_kod]
                cel = (
                    f"{kontekst_zdanie(w)}, dziecko {czynnosc}, {poziom['wsparcie']}, "
                    f"w {kryt['proba']} obserwowanych sytuacji, "
                    f"w ciągu {kryt['horyzont']['dopelniacz']} "
                    f"(weryfikacja po {kryt['horyzont']['miejscownik']})."
                )
                cele.append({
                    "id": f"{w['id']}-{poziom_kod}-{wiek_kod}",
                    "wskaznik_id": w["id"],
                    "kod": w["kod"],
                    "zmysl": opis_zmyslu(w),
                    "sektor": opis_sektora(w),
                    "nazwa": w["nazwa"],
                    "poziom_wsparcia": {"kod": poziom_kod, "nazwa": poziom["nazwa"],
                                        "wsparcie": poziom["wsparcie"], "podpowiedz": poziom["podpowiedz"],
                                        "rola_doroslego": poziom["rola_doroslego"]},
                    "wersja_wiekowa": {"kod": wiek_kod, "nazwa": wiek["nazwa"], "opis": wiek["opis"]},
                    "cel": cel,
                    "smart": {
                        "S_konkretny": f"{czynnosc} ({w['nazwa'].lower()})",
                        "M_mierzalny": f"{kryt['proba']} — {w['wskaznik_obserwacji']}",
                        "A_osiagalny": poziom["wsparcie"],
                        "R_istotny": w["strategia_sensoryczna"],
                        "T_okreslony_w_czasie": (
                            f"w ciągu {kryt['horyzont']['dopelniacz']}; "
                            f"weryfikacja po {kryt['horyzont']['miejscownik']}"
                        ),
                    },
                    "kryterium": kryt["proba"],
                    "horyzont": kryt["horyzont"],
                    "uzasadnienie_kryterium": kryt["uzasadnienie"],
                    "strategia_sensoryczna": w["strategia_sensoryczna"],
                    "sygnal_dziecka": w["sygnal_dziecka"],
                    "wskaznik_obserwacji": w["wskaznik_obserwacji"],
                    # instrukcja słowna dorosłego i polecenie dla dziecka — NIE zamieniać miejscami:
                    "instrukcja_slowna_doroslego": w["instrukcja_slowna"][poziom_kod],
                    "polecenie_dla_dziecka": w["pomoc"]["polecenia"][poziom_kod],
                    "nagranie_polecenia": sciezka_nagrania(w, poziom_kod),
                    "dieta_sensoryczna": w["dieta_sensoryczna"],
                    "dostosowania": w["dostosowania"],
                    "ryzyko": w["ryzyko"],
                    "pomoc_id": f"P-{w['id']}",
                    "arkusz_id": f"A-{w['id']}",
                    "konspekt_id": f"KS-{w['id']}-{poziom_kod}",
                    "tor_zajec_domyslny": dz.DOMYSLNE_ZAJECIA["tor"],
                    "rodzaj_zajec_domyslny": dz.DOMYSLNE_ZAJECIA["rodzaj"],
                    "icf": dz.ZMYSLY[w["zmysl"]]["icf"],
                })
    return {
        "modul": dz.MODUL,
        "druk": "SENS-T — tabela celów w trzech poziomach wsparcia i trzech wersjach wiekowych",
        "jak_liczyc_kryterium": (
            "W tym druku kryterium i horyzont biorą się z POZIOMU WSPARCIA (tabela "
            "`kryteria_poziomow`), a nie z punktacji zmysłu. Na Poziomie I kryterium zostaje "
            "4 z 5 — rośnie trudność samego zachowania, nie liczba prób."
        ),
        "poziomy_wsparcia": dz.POZIOMY,
        "kryteria_poziomow": dz.KRYTERIA_POZIOMOW,
        "wersje_wiekowe": dz.WIEK,
        "tory_zajec": dz.TORY_ZAJEC,
        "rodzaje_zajec": dz.RODZAJE_ZAJEC,
        "liczba_celow": len(cele),
        "cele": cele,
    }


# --- 3. konspekty zajęć (struktura druku KC-3) ------------------------------
def konspekty() -> dict:
    rekordy = []
    for w in dz.WSKAZNIKI:
        k = w["konspekt"]
        for poziom_kod, poziom in dz.POZIOMY.items():
            rekordy.append({
                "id": f"KS-{w['id']}-{poziom_kod}",
                "wskaznik_id": w["id"],
                "kod": w["kod"],
                "zmysl": opis_zmyslu(w),
                "sektor": opis_sektora(w),
                "poziom_wsparcia": {"kod": poziom_kod, "nazwa": poziom["nazwa"]},
                "temat": k["temat"],
                # Cel edukacyjny NIE jest kopiowany do konspektu — czyta się go na żywo:
                "cel_edukacyjny_zrodlo": {
                    "plik": "cele_sens_poziomy.json",
                    "sciezka": "cele[]",
                    "wzor_id": f"{w['id']}-{poziom_kod}-{{wersja_wiekowa}}",
                    "identyfikatory": [f"{w['id']}-{poziom_kod}-{wk}" for wk in dz.WIEK],
                    "pole": "cel",
                    "uwaga": "skopiowanie treści celu do konspektu rozjedzie się przy pierwszej poprawce autorki",
                },
                "czas_trwania_min": 30 if poziom_kod == "III" else 35 if poziom_kod == "II" else 40,
                "forma": k["formy"],
                "metody": k["metody"],
                "miejsce": "sala przedszkolna / plac zabaw — zgodnie z kontekstem wskaźnika",
                "pomoce": {
                    "pomoc_glowna_id": f"P-{w['id']}",
                    "arkusz_id": f"A-{w['id']}",
                    "dodatkowe": k.get("pomoce_dodatkowe", []),
                    "symbole": [f"{SYMBOLE}/{s}" for s in w["arkusz"]["symbole"]],
                },
                "przebieg": {
                    "wprowadzenie": {
                        "czas_min": 5,
                        "czynnosci": k["wprowadzenie"],
                        "instrukcja_slowna_doroslego": w["instrukcja_slowna"][poziom_kod],
                        "polecenie_dla_dziecka": w["pomoc"]["polecenia"][poziom_kod],
                        "nagranie": sciezka_nagrania(w, poziom_kod),
                    },
                    "czesc_glowna": {
                        "czas_min": 20 if poziom_kod == "III" else 22 if poziom_kod == "II" else 25,
                        "czynnosci": k["glowna"],
                        "wsparcie_na_tym_poziomie": poziom["wsparcie"],
                        "rola_doroslego": poziom["rola_doroslego"],
                        "trzy_kroki_uzycia_pomocy": w["pomoc"]["trzy_kroki_uzycia"],
                    },
                    "zakonczenie": {
                        "czas_min": 5 if poziom_kod == "III" else 8,
                        "czynnosci": k["zakonczenie"],
                        "utrwalenie": f"umieszczenie pomocy w stałym miejscu: {w['pomoc']['nazwa']}",
                    },
                },
                "dieta_sensoryczna_po_zajeciach": w["dieta_sensoryczna"],
                "dostosowania": w["dostosowania"],
                "ewaluacja": {
                    "co_liczymy": w["wskaznik_obserwacji"],
                    "kryterium": dz.KRYTERIA_POZIOMOW[poziom_kod]["proba"],
                    "uwaga_autorki": k["ewaluacja_uwaga"],
                },
                "bezpieczenstwo": w["ryzyko"],
                "wskazowka_dla_doroslego": w["pomoc"]["wskazowka_dla_doroslego"],
            })
    return {
        "modul": dz.MODUL,
        "druk": "KC-3 — konspekt zajęć",
        "zasada": (
            "Cel edukacyjny konspektu nie leży w konspekcie. Czyta się go na żywo z "
            "cele_sens_poziomy.json — pole `cel_edukacyjny_zrodlo` mówi, gdzie dokładnie."
        ),
        "liczba_konspektow": len(rekordy),
        "konspekty": rekordy,
    }


# --- 4. pomoce dydaktyczne + polecenia dla dziecka --------------------------
def pomoce() -> dict:
    rekordy, polecenia = [], []
    for w in dz.WSKAZNIKI:
        p = w["pomoc"]
        rekordy.append({
            "id": f"P-{w['id']}",
            "wskaznik_id": w["id"],
            "kod": w["kod"],
            "zmysl": opis_zmyslu(w),
            "sektor": opis_sektora(w),
            "nazwa": p["nazwa"],
            # teksty dla DOROSŁEGO — trudne słowa są tu na miejscu:
            "opis_dla_doroslego": p["opis_dla_doroslego"],
            "trzy_kroki_uzycia": p["trzy_kroki_uzycia"],
            "wskazowka_dla_doroslego": p["wskazowka_dla_doroslego"],
            "bezpieczenstwo": w["ryzyko"],
            # teksty dla DZIECKA — krótkie zdania, bez trudnych słów, nagrywane głosem autorki:
            "etykieta_dla_dziecka": p["etykieta_dla_dziecka"],
            "zdjecie": f"{MEDIA}/pomoce_sens/p_{numer(w)}.jpg",
            "arkusz_id": f"A-{w['id']}",
            "symbole": [f"{SYMBOLE}/{s}" for s in w["arkusz"]["symbole"]],
        })
        for poziom_kod, poziom in dz.POZIOMY.items():
            polecenia.append({
                "id": f"POL-{w['id']}-{poziom_kod}",
                "pomoc_id": f"P-{w['id']}",
                "wskaznik_id": w["id"],
                "poziom_wsparcia": {"kod": poziom_kod, "nazwa": poziom["nazwa"]},
                "polecenie_dla_dziecka": p["polecenia"][poziom_kod],
                "instrukcja_slowna_doroslego": w["instrukcja_slowna"][poziom_kod],
                "nagranie": sciezka_nagrania(w, poziom_kod),
                "czyta": "dziecko słucha nagrania; instrukcję słowną czyta dorosły",
            })
    return {
        "modul": dz.MODUL,
        "zasada_jezyka": (
            "Kto co czyta, decyduje o języku. `polecenie_dla_dziecka` i `etykieta_dla_dziecka` "
            "mówi się DZIECKU — krótkimi zdaniami, bez trudnych słów; to są teksty nagrane głosem "
            "autorki. `trzy_kroki_uzycia`, `wskazowka_dla_doroslego`, `opis_dla_doroslego` i "
            "`instrukcja_slowna_doroslego` czyta NAUCZYCIEL. Nie wolno zamienić ich miejscami."
        ),
        "liczba_pomocy": len(rekordy),
        "liczba_polecen": len(polecenia),
        "pomoce": rekordy,
        "polecenia_dla_dziecka": polecenia,
    }


# --- 5. materiały do druku (arkusze A4) -------------------------------------
def materialy_do_druku() -> dict:
    rekordy = []
    for w in dz.WSKAZNIKI:
        a = w["arkusz"]
        rekordy.append({
            "id": f"A-{w['id']}",
            "wskaznik_id": w["id"],
            "kod": w["kod"],
            "zmysl": opis_zmyslu(w),
            "tytul": a["tytul"],
            "format": "A4, druk jednostronny, karton 200 g",
            "elementy_do_wyciecia": a["elementy"],
            "symbole": [{"plik": s, "sciezka": f"{SYMBOLE}/{s}"} for s in a["symbole"]],
            "etykieta_dla_dziecka": w["pomoc"]["etykieta_dla_dziecka"],
            "wstep_dla_doroslego": w["pomoc"]["opis_dla_doroslego"],
            "pomoc_id": f"P-{w['id']}",
        })
    return {
        "modul": dz.MODUL,
        "biblioteka_symboli": (
            "Symbole leżą w katalogu banku KPOF i to nie jest bałagan, tylko wymóg merytoryczny: "
            "dziecko korzystające z komunikacji obrazkowej musi widzieć TEN SAM obrazek na karcie "
            "z zajęć, na tablicy AAC i w planie dnia. Jeśli wpinasz kilka modułów, biblioteka "
            "symboli ma zostać JEDNA."
        ),
        "sciezka_symboli": SYMBOLE,
        "liczba_arkuszy": len(rekordy),
        "arkusze": rekordy,
    }


# --- 6. kontrakt na własne konspekty nauczycielki ---------------------------
def wlasne_konspekty_kontrakt() -> dict:
    return {
        "modul": dz.MODUL,
        "opis": (
            "Kształt rekordu, w którym nauczycielka zapisuje własny scenariusz. Aplikacja "
            "przechowuje go obok konspektów autorskich i wyświetla w tej samej tabeli."
        ),
        "kontrakt": {
            "id": "string — nadawany przez aplikację, prefiks WK-",
            "autor": "string — imię i nazwisko nauczyciela",
            "data_utworzenia": "string ISO 8601 (RRRR-MM-DD)",
            "wskaznik_id": "string — jeden z 21 identyfikatorów SENS-01…SENS-21",
            "poziom_wsparcia": "string — III | II | I",
            "wersja_wiekowa": "string — 3-4 | 5 | 6",
            "temat": "string — do 120 znaków",
            "cel_edukacyjny_zrodlo": {
                "plik": "cele_sens_poziomy.json",
                "cel_id": "string — np. SENS-04-II-5",
                "pole": "cel",
                "uwaga": "cel czytany na żywo; nie kopiować treści do rekordu",
            },
            "czas_trwania_min": "int — 15…60",
            "forma": "string",
            "metody": "array[string]",
            "pomoce": {"pomoc_glowna_id": "string | null", "wlasne": "array[string]"},
            "przebieg": {
                "wprowadzenie": {"czas_min": "int", "czynnosci": "string",
                                 "polecenie_dla_dziecka": "string — krótkie zdania, bez trudnych słów"},
                "czesc_glowna": {"czas_min": "int", "czynnosci": "string"},
                "zakonczenie": {"czas_min": "int", "czynnosci": "string"},
            },
            "ewaluacja": {"co_liczymy": "string", "kryterium": "string — np. 4 z 5"},
            "bezpieczenstwo": "string | null",
            "zalaczniki": "array[string] — ścieżki względem 04_media/",
        },
        "walidacja": [
            "wskaznik_id musi istnieć w cele_sens_poziomy.json",
            "cel_edukacyjny_zrodlo.cel_id musi zgadzać się z wskaznik_id, poziomem i wersją wiekową",
            "polecenie_dla_dziecka: maksymalnie 12 słów w zdaniu, bez terminów fachowych",
            "pole bezpieczenstwo wymagane, gdy wskaźnik dotyczy propriocepcji lub równowagi",
        ],
    }


PLIKI = {
    "cele_sens_obserwacja.json": cele_obserwacja,
    "cele_sens_poziomy.json": cele_poziomy,
    "konspekty_sens.json": konspekty,
    "pomoce_sens.json": pomoce,
    "materialy_do_druku.json": materialy_do_druku,
    "wlasne_konspekty_kontrakt.json": wlasne_konspekty_kontrakt,
}


def main() -> int:
    ap = argparse.ArgumentParser(description="Eksport banku celów SMART profilu sensorycznego do JSON")
    ap.add_argument("--sprawdz", action="store_true", help="policz rekordy, nie zapisuj plików")
    ap.add_argument("--katalog", default=str(KATALOG), help="katalog docelowy")
    args = ap.parse_args()

    katalog = pathlib.Path(args.katalog)
    if not args.sprawdz:
        katalog.mkdir(parents=True, exist_ok=True)

    for nazwa, budowa in PLIKI.items():
        dane = budowa()
        if args.sprawdz:
            liczby = {k: v for k, v in dane.items() if k.startswith("liczba_")}
            print(f"{nazwa:34} {liczby or '(kontrakt)'}")
            continue
        sciezka = katalog / nazwa
        sciezka.write_text(json.dumps(dane, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"zapisano {sciezka.relative_to(katalog.parent)}  ({sciezka.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
