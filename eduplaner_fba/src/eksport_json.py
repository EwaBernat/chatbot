#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Eksport modułu FBA/PBS do JSON — dla aplikacji, nie dla drukarki.

Druki HTML są gotowe do wydruku, ale programista wpinający moduł w aplikację
potrzebuje treści, a nie layoutu. Ten skrypt wyjmuje z modułów Pythona całą
zawartość merytoryczną i zapisuje ją w pięciu plikach JSON o stabilnym,
opisanym kształcie — takim samym jak eksport banku celów SMART KPOF, żeby
obie części ekosystemu wpinało się jedną konwencją:

  cele_fba_obserwacja.json — 25 celów do obserwacji pogłębionej (druk FBA-C)
                             + progi punktacji funkcji
  cele_fba_poziomy.json    — 225 celów: wskaźnik × poziom wsparcia × wiek (FBA-T)
  konspekty_fba.json       — 75 konspektów w pełnej strukturze druku KC-3
  pomoce_fba.json          — 25 kart pomocy KC-4 + 75 poleceń dla dziecka
  materialy_do_druku.json  — 25 arkuszy A4 + mapowanie na bibliotekę symboli

Media zostają plikami. JSON podaje **ścieżki względne** do zdjęć, nagrań
i symboli, bo wrzucanie megabajtów base64 do pliku danych utrudniłoby i podgląd,
i wersjonowanie. Wszystkie ścieżki liczone są od katalogu **nadrzędnego wobec
obu modułów**: `eduplaner_fba/assets/…` dla zdjęć i nagrań,
`eduplaner_przedszkole/assets/symbole/…` dla symboli. Arkusze FBA korzystają
z **tej samej** biblioteki symboli co bank i to nie jest przypadek — dziecko musi
widzieć ten sam obrazek w obu materiałach.

Uruchomienie:  python3 src/eksport_json.py [katalog_docelowy]
"""

from __future__ import annotations

import json
import os
import sys

import dane_fba as DF
import dane_poziomy as DP
import konspekty_fba as KF
import pomoce_fba as PF
import karta_pomocy as KP
import symbole_fba as SF
import moje_konspekty_fba as MK

KORZEN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _wzgledna(sciezka):
    """Ścieżka liczona od katalogu, w którym leżą oba moduły.

    Jedna konwencja dla wszystkiego: zdjęcia i nagrania FBA zaczynają się od
    `eduplaner_fba/`, symbole od `eduplaner_przedszkole/`. Dzięki temu odbiorca
    ma jeden katalog bazowy zamiast dwóch reguł do zapamiętania.
    """
    if sciezka is None:
        return None
    return os.path.relpath(os.path.abspath(str(sciezka)),
                           os.path.dirname(KORZEN)).replace(os.sep, "/")


def _media_pomocy(nr, wersja):
    obraz = KP.OBRAZY / f"k_{PF.kod(nr)}.jpg"
    audio = KP.AUDIO / f"{wersja.lower()}{PF.kod(nr)}.mp3"
    return (_wzgledna(obraz) if obraz.exists() else None,
            _wzgledna(audio) if audio.exists() else None)


def cele_obserwacja():
    """Druk FBA-C: 25 celów do obserwacji pogłębionej + progi punktacji."""
    return {
        "dokument": "EduPlaner 2026 · druk FBA-C · cele SMART do obserwacji pogłębionej",
        "opis": ("Ciąg dalszy karty ABC/FBA. Kryterium prób i horyzont ewaluacji "
                 "NIE są stałe — wynikają z punktacji danej funkcji u konkretnego "
                 "dziecka, według tabeli `progi`."),
        "progi": [
            {"od_punktow": prog, "ocena": nazwa, "kryterium": proba,
             "horyzont": {"dopelniacz": dop, "miejscownik": msc, "mianownik": mian},
             "dlaczego": opis}
            for prog, nazwa, proba, dop, msc, mian, opis in DF.PROGI
        ],
        "funkcje": [
            {"nr": f["rzym"], "nazwa": f["nazwa"], "skrot": f["skrot"],
             "opis": f["opis"], "zasada_pbs": f["pbs"],
             "wskazniki": [
                 {"nr": f'{f["rzym"]}.{i}',
                  "deficyt": wsk["deficyt"],
                  "cel": wsk["cel"],
                  "co_obserwowac": wsk["obs"],
                  "ile_sytuacji": wsk["ile"],
                  "smart": [{"litera": L, "tresc": t} for L, t in wsk["smart"]]}
                 for i, wsk in enumerate(f["wskazniki"], 1)
             ]}
            for f in DF.FUNKCJE
        ],
    }


def cele_poziomy():
    """Druk FBA-T: 225 celów — wskaźnik × poziom wsparcia × wersja wiekowa."""
    poziomy = [{"klucz": kod, "nazwa": nazwa, "kryterium": kryt,
                "horyzont": hor, "warunki": opis}
               for kod, nazwa, kryt, hor, opis in DP.POZIOMY]
    wersje = [{"klucz": kod, "wiek": nazwa} for kod, nazwa in DP.WERSJE]
    funkcje = []
    for rzym, f in DP.CELE.items():
        wskazniki = []
        for i, wsk in enumerate(f["wskazniki"], 1):
            nr = f"{rzym}.{i}"
            wskazniki.append({
                "nr": nr,
                "wskaznik": wsk["wskaznik"],
                "zachowanie_zastepcze": wsk["zastepcze"],
                "cele": {
                    kod_w: {p["klucz"]: tekst
                            for p, tekst in zip(poziomy, wsk[kod_w])}
                    for kod_w, _ in DP.WERSJE
                },
            })
        funkcje.append({"nr": rzym, "nazwa": f["nazwa"], "wskazniki": wskazniki})
    return {
        "dokument": "EduPlaner 2026 · druk FBA-T · cele SMART wiek × poziom wsparcia",
        "opis": ("Poziom wsparcia zmienia warunki zadania, nie funkcję zachowania. "
                 "Kryterium na Poziomie I zostaje 4 z 5 — rośnie trudność zachowania, "
                 "nie liczba prób."),
        "poziomy_wsparcia": poziomy,
        "wersje_wiekowe": wersje,
        "funkcje": funkcje,
    }


def konspekty():
    """75 konspektów w strukturze druku KC-3."""
    poz = {kod: nazwa for kod, nazwa, *_ in DP.POZIOMY}
    out = []
    for nr, wersja in KF.klucze():
        K = KF.konspekt(nr, wersja)
        out.append({
            "id": KF.kid(nr, wersja),
            "wskaznik": nr,
            "wersja_wiekowa": wersja,
            "wiek": K["wiek"],
            "funkcja": K["funkcja"],
            "tytul": K["tytul"],
            "podtytul": K["podtytul"],
            "sfera": K["sfera"],
            "czas": K["czas"], "forma": K["forma"], "cykl": K["cykl"],
            "cel_terapeutyczny": {
                "tresc": K["ter"],
                "smart": [{"litera": L, "tresc": t} for L, t in K["ter_smart"]],
                "kryterium": K["ter_kryt"],
            },
            "cel_edukacyjny_zrodlo": {
                "uwaga": ("Cel edukacyjny czytany jest na żywo z druku FBA-T — "
                          "nie kopiuj go tutaj, bo rozjedzie się po poprawce."),
                "plik": "cele_fba_poziomy.json",
                "sciezka": f"funkcje[{nr.split('.')[0]}].wskazniki[{nr}].cele[{wersja}]",
            },
            "pomoce": K["pomoce"],
            "metody": K["metody"],
            "rodzaj_zajec": K["rodzaj"],
            "przebieg": [{"lp": i, "nauczyciel": n, "dziecko": d}
                         for i, (n, d) in enumerate(K["przebieg"], 1)],
            "modyfikacje": {kod: {"poziom": poz[kod], "kroki": K["mody"][kod]}
                            for kod in poz},
            "wskazowka": K["wskazowka"],
            "arkusz_id": nr,
        })
    return {
        "dokument": "EduPlaner 2026 · druk KC-3 · konspekty zajęć do wskaźników FBA",
        "opis": ("Jeden konspekt obsługuje trzy poziomy wsparcia: poziom zmienia "
                 "sekcję VI (modyfikacje), nie przebieg zajęć."),
        "liczba": len(out),
        "konspekty": out,
    }


def pomoce():
    """25 kart pomocy KC-4 z poleceniami i ścieżkami do mediów."""
    out = []
    for nr in sorted(PF.POMOCE, key=lambda x: (x.split(".")[0], int(x.split(".")[1]))):
        nazwa, przygotuj, kroki, wskazowka, opis_zdjecia = PF.POMOCE[nr]
        polecenia = {}
        for kod_w, wiek in DP.WERSJE:
            foto, audio = _media_pomocy(nr, kod_w)
            polecenia[kod_w] = {
                "wiek": wiek,
                "polecenie_dla_dziecka": PF.POLECENIA[(nr, kod_w)],
                "nagranie": audio,
            }
        foto, _ = _media_pomocy(nr, DP.WERSJE[0][0])
        out.append({
            "wskaznik": nr,
            "nazwa": nazwa,
            "co_przygotowac": list(przygotuj),
            "trzy_kroki_uzycia": list(kroki),
            "wskazowka_dla_doroslego": wskazowka,
            "zdjecie": foto,
            "opis_zdjecia": opis_zdjecia,
            "polecenia": polecenia,
        })
    return {
        "dokument": "EduPlaner 2026 · druk KC-4 · pomoce dydaktyczne do wskaźników FBA",
        "opis": ("Trzy kroki użycia czyta DOROSŁY, polecenie mówi się DZIECKU — "
                 "i to polecenie jest nagrane głosem autorki. Nagrania to dane "
                 "biometryczne: nie publikuj ich poza uzgodnionym zastosowaniem."),
        "liczba_pomocy": len(out),
        "liczba_nagran": len(PF.POLECENIA),
        "pomoce": out,
    }


def materialy_do_druku():
    """25 arkuszy A4 + mapowanie kart i pasków na bibliotekę symboli."""
    arkusze = []
    for nr in sorted(KF.RDZEN, key=lambda x: (x.split(".")[0], int(x.split(".")[1]))):
        a = KF.RDZEN[nr]["arkusz"]
        kody_kart = SF.KARTY.get(nr, [])
        kody_paska = SF.PASKI.get(nr, [])
        karty = []
        for i, k in enumerate(a.get("karty") or []):
            etykieta, opis = (k if isinstance(k, (list, tuple)) else (k, ""))
            kod = kody_kart[i] if i < len(kody_kart) else None
            karty.append({
                "etykieta_dla_dziecka": etykieta,
                "opis_dla_doroslego": opis,
                "symbol": kod or None,
                "plik_symbolu": _wzgledna(SF.plik(kod)) if kod and SF.plik(kod) else None,
            })
        pasek = []
        for i, krok in enumerate(a.get("pasek") or []):
            kod = kody_paska[i] if i < len(kody_paska) else None
            pasek.append({
                "etykieta_dla_dziecka": krok,
                "symbol": kod or None,
                "plik_symbolu": _wzgledna(SF.plik(kod)) if kod and SF.plik(kod) else None,
            })
        arkusze.append({
            "wskaznik": nr,
            "tytul": a.get("tytul", ""),
            "wstep_dla_doroslego": a.get("wstep", ""),
            "karty": karty,
            "pasek_kolejnosci": pasek,
        })
    przypisanych, z_obrazkiem, puste = SF.stan()
    return {
        "dokument": "EduPlaner 2026 · materiały A4 do wycięcia przy konspektach FBA",
        "opis": ("Etykiety kart i pasków widzi DZIECKO — pisane są prostym językiem. "
                 "Opisy pod polami i wstęp czyta dorosły. Symbole pochodzą "
                 "z biblioteki banku KPOF: ten sam obrazek musi być tu, na tablicy "
                 "AAC i w planie dnia."),
        "biblioteka_symboli": {
            "katalog": _wzgledna(SF.BIBLIOTEKA),
            "przypisanych": przypisanych,
            "z_obrazkiem": z_obrazkiem,
            "pol_celowo_pustych": puste,
        },
        "liczba_arkuszy": len(arkusze),
        "arkusze": arkusze,
    }


def wlasne_konspekty():
    """Kontrakt danych edytora własnych konspektów — dla aplikacji, nie dla druku."""
    return {
        "opis": ("Nauczycielka dopisuje własne scenariusze plusem przy celu. "
                 "W dokumencie HTML zapisują się w localStorage przeglądarki; "
                 "aplikacja powinna przejąć te dane, zachowując kształt rekordu."),
        "klucz_localstorage": MK.KLUCZ,
        "rekord": {
            "id": "mkf<losowy>", "wersja": "A|B|C", "nr": "I.1 … V.5",
            "poziom": "p3|p2|p1",
            "wskaznik": "treść wskaźnika (kopia informacyjna)",
            "funkcja": "I … V",
            "zastepcze": "zachowanie zastępcze — pole WYMAGANE",
            "tytul": "…", "podtytul": "…", "czas": "…", "forma": "…", "cykl": "…",
            "ter": "cel terapeutyczny", "kryt": "kryterium",
            "pomoce": ["…"], "metody": ["…"], "rodzaj": "…",
            "przebieg": [["czynność nauczyciela", "reakcja dziecka"]],
            "mod3": ["…"], "mod2": ["…"], "mod1": ["…"],
            "wskazowka": "…",
            "vii": "gotowa|wlasna|brak",
            "zArkuszem": True,
            "pomoc": {
                "nazwa": "…", "przygotuj": ["…"], "kroki": ["…"],
                "wskazowka": "…", "polecenie": "…",
                "foto": "data:image/jpeg;base64,… (900 px)",
                "audio": "data:audio/mpeg;base64,… (do 600 kB)",
            },
            "utworzono": "ISO 8601", "zmieniono": "ISO 8601",
        },
        "uwagi": [
            "Cel edukacyjny NIE jest w rekordzie — czyta się go na żywo z FBA-T.",
            "Klucz jest inny niż klucz banku KPOF; zbiory nie mogą się mieszać.",
            "Przy karcie 'gotowa' media nie są kopiowane — pochodzą z konspektu.",
        ],
    }


PLIKI = {
    "cele_fba_obserwacja.json": cele_obserwacja,
    "cele_fba_poziomy.json": cele_poziomy,
    "konspekty_fba.json": konspekty,
    "pomoce_fba.json": pomoce,
    "materialy_do_druku.json": materialy_do_druku,
    "wlasne_konspekty_kontrakt.json": wlasne_konspekty,
}


def main(cel):
    os.makedirs(cel, exist_ok=True)
    for nazwa, fn in PLIKI.items():
        sciezka = os.path.join(cel, nazwa)
        with open(sciezka, "w", encoding="utf-8") as f:
            json.dump(fn(), f, ensure_ascii=False, indent=2)
        print(f"  {nazwa:34} {os.path.getsize(sciezka)/1024:8.1f} kB")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(KORZEN, "eksport_json"))
