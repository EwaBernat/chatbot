#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audyt konspektów zajęć — 288 scenariuszy, każdy sprawdzony osobno.

    python3 narzedzia/audyt_konspektow.py            # wszystkie moduły
    python3 narzedzia/audyt_konspektow.py mowa fba   # wybrane
    python3 narzedzia/audyt_konspektow.py --pokaz    # z przykładami do wglądu

Audyt banku (narzedzia/audyt.py) pyta o cele. Ten pyta o konspekt jako scenariusz
zajęć: czy pasuje do swojego wskaźnika, czy przebieg naprawdę gdzieś prowadzi,
czy trzy wersje wiekowe to trzy różne zajęcia, czy wsparcie maleje z poziomu na
poziom i czy to, co konspekt zapowiada w sekcji VII, faktycznie istnieje jako
plik na dysku.

Czego maszyna nie oceni: czy zajęcia są ciekawe dla pięciolatka. Policzy za to
to, z czego ciekawość wynika — czy pięć kroków przebiegu to pięć różnych
czynności, czy dziecko w każdym kroku coś robi, czy nauczyciel stopniowo się
wycofuje, i czy pomoce wymienione w konspekcie to te same rzeczy, które
nauczycielka wytnie z arkusza.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys
import unicodedata
from collections import Counter, defaultdict

KORZEN = pathlib.Path(__file__).resolve().parent.parent
MODULY = ["sens", "tom", "mowa", "fba"]

POLE_ZASADY = {"sens": "strategia_sensoryczna", "tom": "krok_mentalizacji",
               "mowa": "krok_komunikacyjny", "fba": "zachowanie_zastepcze"}

# Czasownik, który w kroku przebiegu nic nie opisuje. „N — wspiera dziecko”
# nie mówi nauczycielce, co ma zrobić w poniedziałek o dziewiątej.
PUSTE_CZASOWNIKI = r"\b(wspiera|dba|zapewnia|umozliwia|stwarza|buduje|rozwija|ksztaltuje|"\
                   r"motywuje|zacheca|monitoruje)\b"


def bez(t: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", str(t).lower())
                   if unicodedata.category(c) != "Mn")


def rdzenie(t: str) -> set[str]:
    """Rdzenie czterozn., bo polska odmiana rozjeżdża dłuższe ucięcie.

    „słowo”, „słowem” i „słowa” przy pięciu znakach dają trzy różne ciągi
    i porównanie mówi, że konspekt o proszeniu słowem nie ma nic wspólnego
    ze wskaźnikiem o wypowiadaniu słów. Przy czterech wszystkie dają „slow”."""
    return {s[:4] for s in re.findall(r"[a-z]{5,}", bez(t))}


class AudytKonspektow:
    def __init__(self, modul: str):
        self.m = modul
        self.kat = KORZEN / f"eduplaner_{modul}"
        self.dane = self.kat / "01_dane_json"
        self.media = self.kat / "04_media"
        self.wspolne = KORZEN / "media_wspolne"
        self.uwagi: list[tuple[str, str, str]] = []
        self.liczby: dict[str, int] = {}

    def wczytaj(self, nazwa):
        f = self.dane / nazwa
        return json.loads(f.read_text(encoding="utf-8")) if f.exists() else None

    def zle(self, g, c):   self.uwagi.append(("BŁĄD", g, c))
    def slabe(self, g, c): self.uwagi.append(("słabe", g, c))

    def plik_jest(self, sciezka) -> bool:
        """Media leżą w dwóch miejscach i trzeba sprawdzić oba.

        Zdjęcia pomocy i nagrania są w 04_media modułu. Symbole na kartach idą
        ze wspólnej biblioteki banku KPOF — ten sam obrazek ma być u dziecka na
        tablicy AAC, w planie dnia i na wyciętej karcie, więc leży raz, w
        media_wspolne/, pod tą samą ścieżką co w JSON-ie. FBA przyszedł
        z własną kopią w 04_media i dlatego działa w obu układach."""
        if not sciezka:
            return False
        wzgledna = pathlib.Path(sciezka)
        return ((self.media / wzgledna).exists()
                or (self.wspolne / wzgledna).exists()
                or (self.wspolne / wzgledna.name).exists())

    # ——————————————————————————————————————————————————————————————————
    def uruchom(self) -> bool:
        if not self.dane.exists():
            print(f"\n### {self.m.upper()} — modułu nie ma w repozytorium\n")
            return False
        poziomy = self.wczytaj(f"cele_{self.m}_poziomy.json") or {}
        grupy = next((v for v in poziomy.values()
                      if isinstance(v, list) and v and isinstance(v[0], dict)
                      and "wskazniki" in v[0]), [])
        wsk = {w["nr"]: w for g in grupy for w in g["wskazniki"]}
        kons = (self.wczytaj(f"konspekty_{self.m}.json") or {}).get("konspekty", [])
        pom = {p["wskaznik"]: p for p in (self.wczytaj(f"pomoce_{self.m}.json") or {}).get("pomoce", [])}
        ark = {a["wskaznik"]: a for a in (self.wczytaj("materialy_do_druku.json") or {}).get("arkusze", [])}

        self.liczby["konspekty"] = len(kons)
        self.liczby["wskaźniki"] = len(wsk)
        pole = POLE_ZASADY[self.m]

        po_wskazniku = defaultdict(dict)
        for k in kons:
            po_wskazniku[k["wskaznik"]][k["wersja_wiekowa"]] = k

        for k in kons:
            self.jeden(k, wsk.get(k["wskaznik"]), pom.get(k["wskaznik"]),
                       ark.get(k["wskaznik"]), pole)
        for nr, wersje in po_wskazniku.items():
            self.trzy_wersje(nr, wersje)
        self.miedzy_wskaznikami(kons)
        self.profil(kons, pom, ark)
        return True

    def profil(self, kons, pom, ark):
        """Liczby, które opisują przebieg, zamiast go oceniać.

        Nie ma tu progu „dobrze / źle”. Są po to, żeby dało się porównać moduły
        między sobą i zobaczyć po zmianie, czy konspekty nie zrobiły się uboższe:
        ile różnych czynności ma przebieg, ile razy dziecko coś robi, ile rzeczy
        nauczycielka musi przygotować."""
        if not kons:
            return
        krokow = [len(k.get("przebieg", [])) for k in kons]
        rozne = [len({bez(p.get("nauczyciel", "")) for p in k.get("przebieg", [])}) for k in kons]
        slowa_d = [len(p.get("dziecko", "").split())
                   for k in kons for p in k.get("przebieg", [])]
        pomocy = [len(k.get("pomoce", [])) for k in kons]
        metod = [len(k.get("metody", [])) for k in kons]
        mod = [sum(len(k.get("modyfikacje", {}).get(x, {}).get("kroki", []))
                   for x in ("p3", "p2", "p1")) for k in kons]
        sr = lambda a: sum(a) / len(a)
        self.liczby["kroków w przebiegu"] = f"{min(krokow)}–{max(krokow)}"
        self.liczby["z tego różnych"] = f"{sr(rozne):.1f}"
        self.liczby["słów na reakcję dziecka"] = f"{sr(slowa_d):.1f}"
        self.liczby["pomocy"] = f"{sr(pomocy):.1f}"
        self.liczby["metod"] = f"{sr(metod):.1f}"
        self.liczby["kroków modyfikacji"] = f"{sr(mod):.1f}"

    # ——— jeden konspekt ————————————————————————————————————————————
    def jeden(self, k, w, pomoc, arkusz, pole):
        g = f"{k['wersja_wiekowa']}-{k['wskaznik']}"

        # 1. czy konspekt dotyczy swojego wskaźnika
        if w:
            konsp = rdzenie(" ".join([k["tytul"], k.get("podtytul", ""),
                                      k["cel_terapeutyczny"]["tresc"],
                                      " ".join(k.get("metody", [])),
                                      " ".join(p.get("nauczyciel", "") for p in k.get("przebieg", []))]))
            # Zasada modułu jest ważniejsza niż samo brzmienie wskaźnika: to ona
            # mówi, czego konspekt ma uczyć. Wystarczy, że konspekt odzywa się
            # do niej — dopiero cisza po obu stronach jest błędem.
            z_zasada = rdzenie(w.get(pole, "")) & konsp
            z_wskaznikiem = rdzenie(w["wskaznik"]) & konsp
            if not z_zasada and len(z_wskaznikiem) < 2:
                self.zle(g, "konspekt nie spotyka się ani ze swoim wskaźnikiem, "
                            "ani z zasadą modułu")

        # 2. przebieg: pięć różnych czynności, w każdym kroku dziecko coś robi
        przeb = k.get("przebieg", [])
        if len(przeb) < 5:
            self.slabe(g, f"przebieg ma {len(przeb)} kroków zamiast pięciu")
        czynnosci = [bez(p.get("nauczyciel", "")) for p in przeb]
        if len(set(czynnosci)) < len(czynnosci):
            self.zle(g, "dwa kroki przebiegu są takie same")
        for i, p in enumerate(przeb, 1):
            n, d = p.get("nauczyciel", ""), p.get("dziecko", "")
            if not n or not d:
                self.zle(g, f"krok {i} bez pary N/D"); continue
            if re.search(PUSTE_CZASOWNIKI, bez(n)):
                self.slabe(g, f"krok {i}: czasownik, który nic nie opisuje — „{n[:55]}…”")

        # Czego tu nie ma i dlaczego: sprawdzania, czy podpora słabnie z kroku
        # na krok. Próbowałam tego trzy razy — po czasowniku nauczyciela, po
        # słowach wycofania w ostatnich krokach, po długości opisu — i za każdym
        # razem wychodziły same fałszywe trafienia. „N — mówi” pięć razy pod rząd
        # jest w A-I.2 zaletą, bo za każdym razem ubywa podpowiedzi. „D — milczy”
        # to jedno słowo i cała treść kroku w konspekcie o poprawianiu zdań.
        # Ostatni krok, w którym dziecko ocenia własny wybór, wygląda dla wyrażenia
        # regularnego tak samo jak ten, w którym nauczyciel prowadzi za rękę.
        # Maszyna tego nie rozstrzygnie po słowach. Liczby niżej opisują przebieg;
        # ocenę „czy to są dobre zajęcia” wystawia człowiek, który je przeczyta.

        # 3. modyfikacje: wsparcie ma maleć z poziomu na poziom
        mod = k.get("modyfikacje", {})
        if set(mod) != {"p3", "p2", "p1"}:
            self.zle(g, f"modyfikacje niepełne: {sorted(mod)}")
        else:
            zest = {p: tuple(mod[p].get("kroki", [])) for p in ("p3", "p2", "p1")}
            if len(set(zest.values())) < 3:
                self.zle(g, "dwa poziomy wsparcia mają tę samą modyfikację")
            dlugosci = {p: len(" ".join(z)) for p, z in zest.items()}
            for p in ("p3", "p2", "p1"):
                if len(zest[p]) < 2:
                    self.slabe(g, f"modyfikacja {p} ma {len(zest[p])} krok(i) — za mało, "
                                  "żeby powiedzieć, czym ten poziom się różni")

        # 4. pomoce konspektu a pomoc dydaktyczna i arkusz — jedna rzecz, nie trzy
        if pomoc:
            wspolne = rdzenie(" ".join(k.get("pomoce", []))) & rdzenie(
                " ".join(pomoc.get("co_przygotowac", [])) + " " + pomoc.get("nazwa", ""))
            if len(wspolne) < 2:
                self.slabe(g, "pomoce z konspektu nie pokrywają się z kartą pomocy KC-4 — "
                              "nauczycielka przygotuje co innego, niż mówi scenariusz")
        else:
            self.zle(g, "konspekt bez karty pomocy dydaktycznej")

        # 5. media zapowiedziane w sekcji VII: nagranie tej wersji, zdjęcie, karty
        if pomoc:
            pol = pomoc.get("polecenia", {}).get(k["wersja_wiekowa"])
            if not pol:
                self.zle(g, f"brak polecenia dla wersji {k['wersja_wiekowa']}")
            else:
                if not self.plik_jest(pol.get("nagranie")):
                    self.zle(g, f"zapowiedziane nagranie nie istnieje: {pol.get('nagranie')}")
                if not pol.get("polecenie_dla_dziecka"):
                    self.zle(g, "puste polecenie dla dziecka")
            if not self.plik_jest(pomoc.get("zdjecie")):
                self.zle(g, f"zapowiedziane zdjęcie pomocy nie istnieje: {pomoc.get('zdjecie')}")
        if arkusz:
            karty = arkusz.get("karty", [])
            if len(karty) != 4:
                self.zle(g, f"arkusz do wycięcia ma {len(karty)} kart zamiast czterech")
            bez_obrazka = [x for x in karty
                           if x.get("plik_symbolu") and not self.plik_jest(x["plik_symbolu"])]
            if bez_obrazka:
                self.zle(g, f"{len(bez_obrazka)} kart czeka na nienarysowany symbol")
            if len(arkusz.get("pasek_kolejnosci", [])) != 3:
                self.slabe(g, "pasek kolejności nie ma trzech pól")
        else:
            self.zle(g, "konspekt zapowiada materiał do wycięcia, którego nie ma")

        # 6. metryka zajęć
        for p in ("czas", "forma", "cykl", "rodzaj_zajec"):
            if not k.get(p):
                self.zle(g, f"brak pola „{p}”")

    # ——— trzy wersje wiekowe tego samego wskaźnika ————————————————————
    def trzy_wersje(self, nr, wersje):
        if set(wersje) != {"A", "B", "C"}:
            self.zle(nr, f"wskaźnik ma konspekty tylko dla {sorted(wersje)}")
            return
        for pole, opis in (("tytul", "tytuł"), ("podtytul", "podtytuł")):
            war = {w: k.get(pole, "") for w, k in wersje.items()}
            if len(set(war.values())) < 3 and pole == "podtytul":
                self.slabe(nr, "dwie wersje wiekowe mają ten sam podtytuł")
        przeb = {w: tuple(bez(p.get("nauczyciel", "")) for p in k.get("przebieg", []))
                 for w, k in wersje.items()}
        if len(set(przeb.values())) < 3:
            self.zle(nr, "dwie wersje wiekowe mają identyczny przebieg zajęć — "
                         "trzylatek dostaje to samo, co sześciolatek")
        cele = {w: k["cel_terapeutyczny"]["tresc"] for w, k in wersje.items()}
        if len(set(cele.values())) < 3:
            self.zle(nr, "dwie wersje wiekowe mają ten sam cel terapeutyczny")

    # ——— czy konspekty nie powtarzają się między wskaźnikami ——————————
    def miedzy_wskaznikami(self, kons):
        for pole, nazwa in (("tytul", "tytuł"),):
            widziane = {}
            for k in kons:
                if k["wersja_wiekowa"] != "B":
                    continue
                t = bez(k.get(pole, ""))
                if t in widziane:
                    self.zle(k["wskaznik"], f"{nazwa} konspektu taki sam jak w {widziane[t]}")
                widziane[t] = k["wskaznik"]
        tresci = {}
        for k in kons:
            t = bez(k["cel_terapeutyczny"]["tresc"])
            g = f"{k['wersja_wiekowa']}-{k['wskaznik']}"
            if t in tresci:
                self.zle(g, f"cel terapeutyczny identyczny jak w {tresci[t]}")
            tresci[t] = g

    # ——————————————————————————————————————————————————————————————————
    def raport(self, pokaz=False):
        bledy = [u for u in self.uwagi if u[0] == "BŁĄD"]
        slabe = [u for u in self.uwagi if u[0] == "słabe"]
        print(f"\n### {self.m.upper()}")
        licz = self.liczby
        print(f"  konspekty: {licz.pop('konspekty', 0)} · wskaźniki: {licz.pop('wskaźniki', 0)}"
              f" · błędy: {len(bledy)} · do poprawy: {len(slabe)}")
        print("  profil przebiegu: " + " · ".join(f"{k} {v}" for k, v in licz.items()))
        for waga, lista in (("BŁĄD", bledy), ("do poprawy", slabe)):
            if not lista:
                continue
            rodz = defaultdict(list)
            for _, gdzie, co in lista:
                rodz[re.sub(r"[„”][^„”]*[„”]?", "…", co)[:78]].append(gdzie)
            print(f"  — {waga}:")
            for co, gdzie in sorted(rodz.items(), key=lambda x: -len(x[1]))[:10]:
                miejsca = ", ".join(gdzie[:4]) + ("…" if len(gdzie) > 4 else "")
                print(f"      {len(gdzie):>4}× {co}")
                print(f"           {miejsca}")
        return len(bledy), len(slabe)


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    pokaz = "--pokaz" in sys.argv
    print("AUDYT KONSPEKTÓW ZAJĘĆ — EduPlaner 2026")
    b = s = 0
    for m in args or MODULY:
        a = AudytKonspektow(m)
        if a.uruchom():
            x, y = a.raport(pokaz); b += x; s += y
    print(f"\nRAZEM: {b} błędów · {s} rzeczy do poprawy")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
