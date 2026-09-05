#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audyt banku celów i konspektów — sprawdza wszystko, nie próbkę.

    python3 narzedzia/audyt.py                 # wszystkie moduły
    python3 narzedzia/audyt.py mowa tom        # wybrane

Po co: „czy cele są dobrze dobrane" nie da się odpowiedzieć przez zajrzenie
w kilka rekordów. Ten skrypt przechodzi po wszystkich 225 celach i 75
konspektach każdego modułu i pyta o rzeczy, które da się sprawdzić maszynowo:
czy poziomy naprawdę się różnią, czy cel konspektu mówi o tym samym co cel
z tabeli, czy każde polecenie ma nagranie, a każda pomoc zdjęcie i karty.

Ocen „ciekawy" i „dynamiczny" maszyna nie postawi — ale policzy to, z czego
ciekawość wynika: czy czasownik jest obserwowalny, czy cel niesie warunek
sytuacji, czy trzy wersje wiekowe to trzy różne pomysły, czy jeden przepisany.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys
import unicodedata

KORZEN = pathlib.Path(__file__).resolve().parent.parent
MODULY = ["sens", "tom", "mowa", "fba"]

# Czasownik obserwowalny — taki, który da się policzyć z boku sali.
# „Rozumie", „zna", „potrafi" nie są obserwowalne: nie widać ich bez testu.
# Dopasowanie musi iść po całych słowach: pierwsza wersja szukała podciągu
# i „wie" znajdowało się w „powie", przez co 64 dobre cele MOWY wyszły jako
# złe. Raport, który krzyczy na zdrowe cele, jest gorszy niż brak raportu.
NIEOBSERWOWALNE = r"\b(rozumie|zna|wie|potrafi|umie|uswiadamia|chce)\b|\b(jest swiadom|orientuje sie|ma swiadomosc)"
# Wyrazy, których przedszkolak nie rozumie — lista ze skilla cele-fba-pbs.
# Wolno im stać w celu SMART i w metodach, gdzie czyta je dorosły; nie wolno
# w poleceniu, które dziecko usłyszy z nagrania, ani na etykiecie karty.
TRUDNE = ("strategi", "sygnał", "sekwencj", "komunikat", "instrukcj", "procedur",
          "technik", "regulacj", "identyfik", "alternatyw", "konsekwencj",
          "koncentr", "wizualiz", "termometr", "licznik")
DLUGIE_POLECENIE = 14   # słów; powyżej tego dziecko nie powtórzy polecenia

# Warunek sytuacji — cel bez niego mówi „co", ale nie mówi „kiedy i gdzie".
# Wystarczy jeden przyimek albo spójnik okolicznikowy; chodzi o to, żeby cel
# osadzał się w sytuacji, a nie żeby użył konkretnego słowa.
WARUNEK = r"\b(gdy|kiedy|podczas|po|przy|przed|bez|z|ze|w|we|na|do|od|dla|zanim|jesli|az)\b"


def bezogonkow(t: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", t.lower())
                   if unicodedata.category(c) != "Mn")


def rdzenie(t: str) -> set[str]:
    """Zbiór rdzeni słów dłuższych niż 4 znaki — do porównywania, czy dwa
    zdania mówią o tym samym. Ucinam końcówkę fleksyjną, bo „poprosi" i
    „prosi" to ta sama rzecz, a porównanie całych słów tego nie widzi."""
    return {s[:5] for s in re.findall(r"[a-z]{5,}", bezogonkow(t))}


class Audyt:
    def __init__(self, modul: str):
        self.m = modul
        self.kat = KORZEN / f"eduplaner_{modul}"
        self.dane = self.kat / "01_dane_json"
        self.uwagi: list[tuple[str, str, str]] = []   # (waga, gdzie, co)
        self.liczby: dict[str, int] = {}

    def wczytaj(self, nazwa: str):
        f = self.dane / nazwa
        return json.loads(f.read_text(encoding="utf-8")) if f.exists() else None

    def zle(self, gdzie, co):   self.uwagi.append(("BŁĄD", gdzie, co))
    def slabe(self, gdzie, co): self.uwagi.append(("słabe", gdzie, co))

    # ——— 1. cele z tabeli ———————————————————————————————————————————
    def cele(self):
        d = (self.wczytaj(f"cele_{self.m}_poziomy.json") or {})
        # Grupa wskaźników nazywa się inaczej w każdym module: obszary w MOWIE,
        # komponenty w ToM, zmysły w SENS, funkcje w FBA. Szukam po kształcie,
        # nie po nazwie — inaczej nowy moduł cicho wypada z audytu, tak jak
        # wypadł ToM przy pierwszym uruchomieniu.
        grupy = next((v for v in d.values()
                      if isinstance(v, list) and v and isinstance(v[0], dict)
                      and "wskazniki" in v[0]), [])
        wsk = [w for g in grupy for w in g["wskazniki"]]
        self.liczby["wskaźniki"] = len(wsk)
        self.liczby["cele"] = sum(len(w["cele"]) * 3 for w in wsk)
        widziane: dict[str, str] = {}

        for w in wsk:
            nr = w["nr"]
            for wersja, poz in w["cele"].items():
                tresci = [poz.get(p, "") for p in ("p3", "p2", "p1")]
                if len(set(tresci)) < 3:
                    self.zle(f"{nr}·{wersja}", "dwa poziomy wsparcia mają ten sam cel — "
                             "poziom przestaje cokolwiek znaczyć")
                for p, t in zip(("p3", "p2", "p1"), tresci):
                    g = f"{nr}·{wersja}·{p}"
                    if not t:
                        self.zle(g, "pusty cel"); continue
                    low = bezogonkow(t)
                    if re.search(NIEOBSERWOWALNE, low):
                        self.slabe(g, f"czasownik nieobserwowalny: „{t[:60]}…”")
                    if not re.search(WARUNEK, low) and len(t.split()) < 8:
                        self.slabe(g, f"cel krótki i bez osadzenia w sytuacji — nie wiadomo, "
                                   f"kiedy go zaliczyć: „{t}”")
                    if len(t.split()) > 22:
                        self.slabe(g, f"cel na {len(t.split())} słów — za długi, "
                                   "nie zmieści się w komórce tabeli")
                    klucz = bezogonkow(t)
                    if klucz in widziane and widziane[klucz] != g:
                        self.zle(g, f"cel identyczny jak {widziane[klucz]}")
                    widziane[klucz] = g
            # trzy wersje wiekowe mają być trzema pomysłami, nie jednym przepisanym
            for p in ("p3", "p2", "p1"):
                war = {v: w["cele"][v].get(p, "") for v in w["cele"]}
                if len(set(war.values())) < len(war):
                    self.zle(f"{nr}·{p}", "wersje wiekowe nie różnią się na tym poziomie")
        self.szablony(wsk)
        return {w["nr"]: w for w in wsk}

    def szablony(self, wsk):
        """Czy kolumna tabeli nie zapadła się w jedno zdanie z wymienioną nazwą.

        To jest właściwe pytanie o konkretność celu. Pojedynczy cel może wyglądać
        poprawnie, a cała kolumna i tak nic nie mówić, jeżeli dwadzieścia celów
        kończy się tą samą frazą i różni się jednym słowem. Nauczycielka czyta
        kolumnę, nie pojedynczą komórkę."""
        from collections import Counter
        for wersja in ("A", "B", "C"):
            for p in ("p3", "p2", "p1"):
                kol = [w["cele"].get(wersja, {}).get(p, "") for w in wsk]
                kol = [c for c in kol if c]
                if len(kol) < 5:
                    continue
                ogony = Counter(" ".join(c.split()[-3:]).lower() for c in kol)
                fraza, ile = ogony.most_common(1)[0]
                if ile > len(kol) / 3:
                    self.zle(f"kolumna {wersja}·{p}",
                             f"{ile} z {len(kol)} celów kończy się tak samo („…{fraza}”) "
                             "— kolumna jest szablonem, nie zestawem celów")
                krotkie = sum(1 for c in kol if len(c.split()) < 7)
                if krotkie > len(kol) / 2:
                    self.slabe(f"kolumna {wersja}·{p}",
                               f"{krotkie} z {len(kol)} celów krótszych niż siedem słów "
                               "— za mało konkretu, żeby dało się je obserwować")

    # ——— 2. konspekty ——————————————————————————————————————————————
    def konspekty(self, wskazniki):
        d = self.wczytaj(f"konspekty_{self.m}.json") or {}
        kons = d.get("konspekty", [])
        self.liczby["konspekty"] = len(kons)
        pole = {"sens": "strategia_sensoryczna", "tom": "krok_mentalizacji",
                "mowa": "krok_komunikacyjny", "fba": "zachowanie_zastepcze"}[self.m]

        for k in kons:
            g = f"{k['wersja_wiekowa']}-{k['wskaznik']}"
            ct = k.get("cel_terapeutyczny", {})
            tresc = ct.get("tresc", "")
            if not tresc:
                self.zle(g, "konspekt bez celu terapeutycznego"); continue

            # cel konspektu ma mówić o tym samym, co cel z tabeli
            w = wskazniki.get(k["wskaznik"])
            if w:
                z_tabeli = " ".join(w["cele"].get(k["wersja_wiekowa"], {}).values())
                wspolne = rdzenie(tresc) & rdzenie(z_tabeli)
                if len(wspolne) < 2:
                    self.zle(g, "cel terapeutyczny konspektu nie spotyka się z celem "
                             f"z tabeli (wspólnych pojęć: {len(wspolne)})")
                # zasada modułu ma być widoczna w konspekcie
                if w.get(pole):
                    caly = " ".join([tresc, k.get("podtytul", ""), k.get("tytul", ""),
                                     " ".join(k.get("metody", [])),
                                     " ".join(s_["tresc"] for s_ in ct.get("smart", []))])
                    if not rdzenie(w[pole]) & rdzenie(caly):
                        self.slabe(g, f"zasada modułu („{w[pole][:40]}…”) nie odzywa się "
                                   "nigdzie w konspekcie")

            smart = {s["litera"]: s["tresc"] for s in ct.get("smart", [])}
            if set(smart) != set("SMART"):
                self.zle(g, f"SMART niepełny: {sorted(smart)}")
            elif len(set(smart.values())) < 5:
                self.zle(g, "dwie litery SMART mają tę samą treść")
            if not ct.get("kryterium"):
                self.zle(g, "brak kryterium ewaluacji")

            przeb = k.get("przebieg", [])
            if len(przeb) < 5:
                self.slabe(g, f"przebieg ma {len(przeb)} kroków zamiast pięciu")
            for i, kr in enumerate(przeb, 1):
                if not kr.get("nauczyciel") or not kr.get("dziecko"):
                    self.zle(g, f"krok {i} bez pary N/D")
            if len(przeb) != len({p.get("nauczyciel") for p in przeb}):
                self.zle(g, "dwa kroki przebiegu są identyczne")

            mod = k.get("modyfikacje", {})
            if set(mod) != {"p3", "p2", "p1"}:
                self.zle(g, f"modyfikacje niepełne: {sorted(mod)}")
            else:
                zestawy = [tuple(mod[p].get("kroki", [])) for p in ("p3", "p2", "p1")]
                if len(set(zestawy)) < 3:
                    self.zle(g, "dwa poziomy mają tę samą modyfikację")
                for p, z in zip(("p3", "p2", "p1"), zestawy):
                    if len(z) < 2:
                        self.slabe(g, f"modyfikacja {p} ma {len(z)} krok(i)")

            for pole_l, ile in (("pomoce", 4), ("metody", 4)):
                if len(k.get(pole_l, [])) < ile:
                    self.slabe(g, f"{pole_l}: {len(k.get(pole_l, []))} pozycji, mniej niż {ile}")
            if not k.get("wskazowka"):
                self.slabe(g, "brak wskazówki dla prowadzącego")
        return kons

    # ——— 3. pomoce, nagrania, obrazki, karty ————————————————————————
    def pomoce(self):
        d = self.wczytaj(f"pomoce_{self.m}.json") or {}
        pom = d.get("pomoce", [])
        self.liczby["pomoce"] = len(pom)
        media = self.kat / "04_media"
        brak_mp3 = brak_jpg = 0
        nagran = 0

        for p in pom:
            g = p["wskaznik"]
            zdj = p.get("zdjecie")
            if not zdj:
                self.zle(g, "pomoc bez zdjęcia")
            elif not (media / zdj).exists():
                brak_jpg += 1; self.zle(g, f"brak pliku zdjęcia: {zdj}")
            for wersja, pol in p.get("polecenia", {}).items():
                nagran += 1
                gg = f"{g}·{wersja}"
                nag = pol.get("nagranie")
                if not nag:
                    self.zle(gg, "polecenie bez nagrania")
                elif not (media / nag).exists():
                    brak_mp3 += 1; self.zle(gg, f"brak pliku nagrania: {nag}")
                tekst = pol.get("polecenie_dla_dziecka", "")
                if not tekst:
                    self.zle(gg, "puste polecenie dla dziecka")
                elif len(tekst.split()) > DLUGIE_POLECENIE:
                    self.slabe(gg, f"polecenie na {len(tekst.split())} słów — dziecko "
                               "tego nie powtórzy")
                for t in TRUDNE:
                    if t in tekst.lower():
                        self.zle(gg, f"słowo dorosłego w poleceniu dla dziecka: „{t}…”")
            if len(p.get("trzy_kroki_uzycia", [])) != 3:
                self.slabe(g, "„jak użyć” nie ma trzech kroków")
            if len(p.get("co_przygotowac", [])) < 3:
                self.slabe(g, "krótka lista „co przygotować”")
        self.liczby["nagrania"] = nagran
        self.liczby["brak mp3"] = brak_mp3
        self.liczby["brak jpg"] = brak_jpg
        return pom

    def arkusze(self):
        d = self.wczytaj("materialy_do_druku.json") or {}
        ark = d.get("arkusze", [])
        self.liczby["arkusze A4"] = len(ark)
        hist = 0
        for a in ark:
            g = a["wskaznik"]
            if len(a.get("karty", [])) != 4:
                self.zle(g, f"arkusz ma {len(a.get('karty', []))} kart zamiast czterech")
            for k in a.get("karty", []):
                et = k.get("etykieta_dla_dziecka", "")
                if len(et.split()) > 4:
                    self.slabe(g, f"etykieta karty na {len(et.split())} słów: „{et}”")
                for t in TRUDNE:
                    if t in et.lower():
                        self.zle(g, f"słowo dorosłego na karcie dziecka: „{et}”")
            if len(a.get("pasek_kolejnosci", [])) != 3:
                self.slabe(g, "pasek kolejności nie ma trzech pól")
            if a.get("historyjka"):
                hist += 1
        self.liczby["historyjki"] = hist
        return ark

    def uruchom(self):
        if not self.dane.exists():
            print(f"\n### {self.m.upper()} — modułu nie ma w repozytorium\n"); return False
        w = self.cele()
        self.konspekty(w)
        self.pomoce()
        self.arkusze()
        return True

    def raport(self):
        bledy = [u for u in self.uwagi if u[0] == "BŁĄD"]
        slabe = [u for u in self.uwagi if u[0] == "słabe"]
        print(f"\n### {self.m.upper()}")
        print("  " + " · ".join(f"{k}: {v}" for k, v in self.liczby.items()))
        print(f"  błędy: {len(bledy)} · do poprawy: {len(slabe)}")
        for waga, lista in (("BŁĄD", bledy), ("słabe", slabe)):
            from collections import Counter
            if not lista: continue
            rodz = Counter(re.sub(r"[„”][^„”]*[„”]?", "…", c)[:70] for _, _, c in lista)
            print(f"  — {waga}:")
            for co, ile in rodz.most_common(12):
                przyklad = next(g for wg, g, c in lista if re.sub(r"[„”][^„”]*[„”]?", "…", c)[:70] == co)
                print(f"      {ile:>4}× {co}   (np. {przyklad})")
        return len(bledy), len(slabe)


def main() -> int:
    wybrane = sys.argv[1:] or MODULY
    razem_b = razem_s = 0
    print("AUDYT BANKU CELÓW I KONSPEKTÓW — EduPlaner 2026")
    for m in wybrane:
        a = Audyt(m)
        if a.uruchom():
            b, s = a.raport(); razem_b += b; razem_s += s
    print(f"\nRAZEM: {razem_b} błędów · {razem_s} rzeczy do poprawy")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
