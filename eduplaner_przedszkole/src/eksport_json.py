#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Eksport banku celów SMART do JSON — dla aplikacji, nie dla drukarki.

Dokumenty HTML są gotowe do wydruku, ale programista wpinający bank w aplikację
potrzebuje treści, a nie layoutu. Ten skrypt wyjmuje z modułów Pythona całą
zawartość merytoryczną i zapisuje ją w czterech plikach JSON o stabilnym,
opisanym kształcie:

  bank_celow_smart.json  — wersje wiekowe → obszary ICF → twierdzenia → 3 cele
  konspekty.json         — 178 konspektów w pełnej strukturze druku KC-3
  pomoce_dydaktyczne.json— karty pomocy: co przygotować, trzy kroki, polecenie
  materialy_do_druku.json— arkusze A4 przypisane do konspektów + biblioteka symboli

Media zostają plikami. JSON podaje **ścieżki względne** do zdjęć, nagrań i kadrów,
bo wrzucanie kilkunastu megabajtów base64 do pliku danych utrudniłoby i podgląd,
i wersjonowanie. Ścieżki liczone są od katalogu `eduplaner_przedszkole/`.

Uruchomienie:  python3 src/eksport_json.py [katalog_docelowy]
"""

from __future__ import annotations

import json
import os
import sys

import build
import karty_druk
import symbole
import pomoce_a, pomoce_b, pomoce_c, pomoce_u
import moje_konspekty

KORZEN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Poziomy wsparcia — klucz w danych, nazwa dla człowieka i horyzont ewaluacji.
POZIOMY = [
    ("p3", "Poziom III", "4 tygodnie", "g3"),
    ("p2", "Poziom II", "8 tygodni", "g2"),
    ("p1", "Poziom I", "12 tygodni", "g1"),
]

ZESTAWY_POMOCY = {"A": pomoce_a.ZESTAW, "B": pomoce_b.ZESTAW,
                  "C": pomoce_c.ZESTAW, "U": pomoce_u.ZESTAW}


def _wzgledna(sciezka):
    """Ścieżka względem katalogu eduplaner_przedszkole, zawsze ze slashami."""
    return os.path.relpath(str(sciezka), KORZEN).replace(os.sep, "/")


def bank_celow():
    wersje = []
    for mod in build.WERSJE:
        w = mod.WERSJA
        obszary = []
        for a in mod.AREAS:
            twierdzenia = []
            for it in a["items"]:
                twierdzenia.append({
                    "nr": it["n"],
                    "twierdzenie": it["t"],
                    "miara": it["m"],
                    "icf": it["icf"],
                    "podstawa": it["pp"].replace("PP ", ""),
                    "cele": [{"poziom": kod, "nazwa": nazwa, "horyzont": hor,
                              "cel": it[pole]} for kod, nazwa, hor, pole in POZIOMY],
                    "konspekt": build.KONSPEKTY.get((w["kod"], it["n"]), {}).get("nr"),
                })
            obszary.append({
                "rzymski": a["rom"], "icf": a["icf"], "nazwa": a["name"],
                "punktow_kpof": a["pts"], "zasob": a["zasob"],
                "twierdzenia": twierdzenia,
            })
        wersje.append({
            "kod": w["kod"], "etykieta": w["etykieta"], "zakres": w["zakres"],
            "dziecko": w["dziecko"], "opis": w["opis"], "obszary": obszary,
        })
    ile_tw = sum(len(o["twierdzenia"]) for w in wersje for o in w["obszary"])
    return {
        "dokument": "EduPlaner 2026 · Bank celów SMART KPOF · druk KC-1",
        "autorka": "mgr Mirosława Ewa Jurczyszyn · PCTP Koszalin",
        "podstawa_prawna": "Rozporządzenie Ministra Edukacji z 11 marca 2026 r. "
                           "(Dz. U. 2026 poz. 378), obowiązuje od 1 września 2026 r.",
        "uwaga_wersja_U": "Wersja U to cele uzupełniające, dopisane po to, by domknąć "
                          "pokrycie podstawy do 113/113 punktów. To NIE są twierdzenia "
                          "z arkuszy KPOF i nie wolno ich do nich dopisywać.",
        "poziomy_wsparcia": [{"kod": k, "nazwa": n, "horyzont_ewaluacji": h}
                             for k, n, h, _ in POZIOMY],
        "liczba_twierdzen": ile_tw,
        "liczba_celow": ile_tw * 3,
        "wersje": wersje,
    }


def konspekty():
    poz = []
    for (wk, nr), K in sorted(build.KONSPEKTY.items(), key=lambda x: (x[0][0], x[0][1])):
        poz.append({
            "nr": K["nr"], "wersja": wk, "twierdzenie": nr,
            "tytul": K["tytul"], "podtytul": K["podtytul"], "sfera": K["sfera"],
            "czas": K["czas"], "forma": K["forma"], "cykl": K["cykl"],
            "cel_terapeutyczny": K["ter"],
            "cel_smart": [{"litera": L, "tresc": t} for L, t in K["ter_smart"]],
            "kryterium": K["ter_kryt"],
            "pomoce": list(K["pomoce"]), "metody": list(K["metody"]),
            "rodzaj_zajec": K["rodzaj"],
            "przebieg": [{"nauczyciel": n, "dziecko": d} for n, d in K["przebieg"]],
            "modyfikacje": {"p3_czerwona": list(K["mod3"]),
                            "p2_zolta": list(K["mod2"]),
                            "p1_zielona": list(K.get("mod1", []))},
            "wskazowka": K["wskazowka"],
            "ma_karte_pomocy": bool(build.wskaz_pomoc(K["nr"])),
            "ma_material_do_druku": bool(karty_druk.ma_karty(K["nr"])),
        })
    return {"dokument": "EduPlaner 2026 · Konspekty zajęć · druk KC-3",
            "liczba": len(poz), "konspekty": poz}


def pomoce_dydaktyczne():
    zestawy = []
    for kod, Z in ZESTAWY_POMOCY.items():
        karty = []
        for klucz, (nr, tytul, przygotowac, kroki, polecenie, wskazowka) in Z.pomoce.items():
            karty.append({
                "konspekt": nr, "klucz_pliku": klucz, "tytul": tytul,
                "przygotowac": list(przygotowac), "kroki": list(kroki),
                "polecenie_do_dziecka": polecenie, "wskazowka": wskazowka,
                "zdjecie": _wzgledna(Z.foto / f"k_{klucz}.jpg") if Z.ma_foto(klucz) else None,
                "nagranie": _wzgledna(Z.audio / f"{klucz}.mp3") if Z.ma_dzwiek(klucz) else None,
            })
        zestawy.append({"wersja": kod, "etykieta": Z.wiek,
                        "zeszyt_html": Z.dokument, "liczba_kart": len(karty), "karty": karty})
    return {
        "dokument": "EduPlaner 2026 · Pomoce dydaktyczne · druk KC-4",
        "uwaga_o_nagraniach": "Polecenia czyta własny, sklonowany głos autorki "
                              "(ElevenLabs, model eleven_v3). Nie wolno ich zastępować "
                              "innym głosem ani generować nowych bez jej zgody.",
        "liczba_kart": sum(z["liczba_kart"] for z in zestawy),
        "zestawy": zestawy,
    }


def materialy_do_druku():
    arkusze = []
    for nr, lista in sorted(karty_druk.ARKUSZE.items()):
        for i, ark in enumerate(lista, 1):
            wpis = {"konspekt": nr, "lp": i, "rodzaj": ark.get("rodzaj"),
                    "tytul": ark.get("tytul"), "wstep": ark.get("wstep")}
            # Każdy rodzaj arkusza niesie własne pola; przepisujemy je wprost,
            # żeby JSON nie zgubił nic, co potrafi zbudować `karty_druk.arkusz()`.
            for pole, wartosc in ark.items():
                if pole not in wpis:
                    wpis[pole] = wartosc
            arkusze.append(wpis)
    biblioteka = [{"kod": k, "podpis": p, "opis_dla_rysownika": o,
                   "plik": f"assets/symbole/k_{k}.jpg", "narysowany": symbole.jest(k)}
                  for k, (p, o) in symbole.SYMBOLE.items()]
    return {
        "dokument": "EduPlaner 2026 · Materiały do wydruku przy konspektach",
        "rodzaje_arkusza": {
            "karty": "kafle do wycięcia", "pasek": "sekwencja z numerami",
            "tablica": "plansza bez rozcinania", "tabela": "tabela do wypełniania",
            "pola": "puste pola z etykietami", "etykiety": "karteczki z polem koloru",
            "sciezki": "pasy do przecięcia albo szlaczki do obrysowania (SVG)",
        },
        "format": "A4 pionowo, jedna strona na arkusz",
        "liczba_arkuszy": len(arkusze),
        "liczba_symboli": len(biblioteka),
        "arkusze": arkusze,
        "biblioteka_symboli": biblioteka,
    }


def wlasne_konspekty_format():
    """Kontrakt danych edytora własnych konspektów — to czyta i pisze bank."""
    return {
        "opis": "Format pliku, który zapisuje i wczytuje panel „Moje konspekty” "
                "w banku celów. Ten sam kształt trzyma przeglądarka w localStorage.",
        "klucz_localstorage": moje_konspekty.KLUCZ,
        "pola_rekordu": {
            "id": "identyfikator nadawany przy zapisie, unikalny",
            "wersja": "kod wersji wiekowej: A | B | C | U",
            "nr": "numer twierdzenia w tej wersji (liczba)",
            "poziom": "p3 | p2 | p1 — poziom wsparcia, do którego konspekt należy",
            "twierdzenie/icf/pp/obszar/rzym/etykieta": "kontekst celu, przepisany przy zapisie",
            "tytul": "wymagany",
            "podtytul/czas/forma/cykl/rodzaj/wskazowka": "pola tekstowe",
            "ter": "cel terapeutyczny", "kryt": "kryterium pomiaru",
            "pomoce/metody/mod3/mod2/mod1": "listy tekstów",
            "przebieg": "lista par [czynność nauczyciela, reakcja dziecka]",
            "utworzono/zmieniono": "znaczniki czasu ISO 8601",
        },
        "uwaga": "Cel edukacyjny NIE jest przechowywany w rekordzie — bank czyta go "
                 "na żywo z tabeli po (wersja, nr, poziom). Dzięki temu poprawka celu "
                 "w banku nie zostawia w konspekcie starej wersji.",
        "przyklad": {
            "dokument": "EduPlaner 2026 · moje konspekty", "wersjaZapisu": 1,
            "zapisano": "2026-08-31T10:00:00.000Z",
            "konspekty": [{
                "id": "mkprzyklad1", "wersja": "A", "nr": 1, "poziom": "p2",
                "twierdzenie": "Przygląda się i przysłuchuje z zainteresowaniem temu, "
                               "co pokazuje i mówi nauczyciel",
                "icf": "d110–d115", "pp": "3.5",
                "obszar": "Uczenie się i stosowanie wiedzy", "rzym": "I",
                "etykieta": "3–4 lata",
                "tytul": "Kącik uważnego słuchania",
                "podtytul": "Krótkie polecenia i sygnał dźwiękowy",
                "czas": "20 min", "forma": "para dzieci", "cykl": "2× w tygodniu",
                "ter": "Dziecko wykona dwuelementowe polecenie po jednym powtórzeniu "
                       "w 3 z 5 prób w ciągu 8 tygodni.",
                "kryt": "arkusz obserwacji · 5 prób w tygodniu",
                "pomoce": ["bębenek", "karty z obrazkami czynności"],
                "metody": ["modelowanie", "polecenie z sygnałem"],
                "rodzaj": "Zajęcia rozwijające kompetencje emocjonalno-społeczne",
                "przebieg": [["N — uderza w bębenek i podaje polecenie.",
                              "D — zatrzymuje się i patrzy na nauczyciela."]],
                "mod3": ["polecenie z obrazkiem"], "mod2": ["polecenie jednoelementowe"],
                "mod1": ["trzyelementowe polecenie"],
                "wskazowka": "Sygnał dźwiękowy daje dziecku sekundę na przełączenie uwagi.",
                "utworzono": "2026-08-31T10:00:00.000Z",
                "zmieniono": "2026-08-31T10:00:00.000Z",
            }],
        },
    }


PLIKI = {
    "bank_celow_smart.json": bank_celow,
    "konspekty.json": konspekty,
    "pomoce_dydaktyczne.json": pomoce_dydaktyczne,
    "materialy_do_druku.json": materialy_do_druku,
    "format_wlasnych_konspektow.json": wlasne_konspekty_format,
}


def main(cel):
    os.makedirs(cel, exist_ok=True)
    for nazwa, fn in PLIKI.items():
        sciezka = os.path.join(cel, nazwa)
        with open(sciezka, "w", encoding="utf-8") as f:
            json.dump(fn(), f, ensure_ascii=False, indent=2)
        print(f"  {nazwa:36} {os.path.getsize(sciezka)/1024:8.1f} kB")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(KORZEN, "eksport_json"))
