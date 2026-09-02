# -*- coding: utf-8 -*-
"""Karty do wycięcia → symbole ze wspólnej biblioteki EduPlaner.

Karty w konspektach FBA miały puste pola z podpisem „miejsce na symbol".
To było uczciwe, ale niepełne: nauczyciel dostawał ramkę do wypełnienia,
a nie gotowy materiał. Teraz każda karta bierze obrazek **z biblioteki
`eduplaner_przedszkole/src/symbole.py`** — tej samej, z której korzysta bank
celów SMART.

Dlaczego stamtąd, a nie z nowych rysunków pod te konspekty: dziecko korzystające
z komunikacji obrazkowej musi widzieć TEN SAM symbol na tablicy AAC, w planie
dnia i na karcie z konspektu. Symbol dorysowany pod jeden materiał przestaje
być słowem. Symbole, których w bibliotece nie było (gniotek, taśma, koc
obciążeniowy, czerwona karta), zostały **dopisane do biblioteki**, a nie
narysowane obok niej.

Karta bez przypisanego symbolu zostaje polem do wypełnienia — tak jest
w kilku miejscach celowo: „Mój znak" i „Sygnał 1" dziecko rysuje razem
z nauczycielem, bo to mają być jego znaki, nie obrazki z zestawu.
"""

from pathlib import Path

BIBLIOTEKA = (Path(__file__).resolve().parent.parent.parent
              / "eduplaner_przedszkole" / "assets" / "symbole")

# (wskaźnik, numer karty 0–3) → kod symbolu z biblioteki; None = pole do rysowania
KARTY = {
 "I.1":  ["postawa_stolik", "dzien_zabawa", "polecenie_wez", "strategia_przerwa"],
 "I.2":  ["gest_slucham", "polecenie_wez", "gest_brawo", "strategia_przerwa"],
 "I.3":  ["strategia_przerwa", "gest_chodz", "strategia_czesci", "gest_brawo"],
 "I.4":  ["zabawa_ukladanka", "zabawa_klocki", None, "emocja_duma"],
 "I.5":  ["strategia_przerwa", "prosze_odpoczynek", "prosze_ruch", "gest_chodz"],
 "II.1": ["sensor_gniotek", "sensor_tasma", "sensor_faktura", "polecenie_poloz"],
 "II.2": ["prosze_ruch", "sensor_ucisk", "prosze_cisza", "emocja_radosc"],
 "II.3": ["dzien_sniadanie", "dzien_zajecia", "dzien_obiad", "postawa_stolik"],
 "II.4": ["zabawa_ukladanka", "zabawa_rysowanie", "zabawa_ksiazki", "dzien_sprzatanie"],
 "II.5": ["gest_stop", "sensor_zamiana", "prosze_ruch", "instrument_dzwonki"],
 "III.1": ["prosze_pomoc", "gest_czekam", "zabawa_ukladanka", "gest_chodz"],
 "III.2": ["strategia_pomoc", "gest_skinienie", "gest_czekam", "zeton_diament"],
 "III.3": ["gest_mowie", "gest_slucham", "gest_czekam", "gest_brawo"],
 "III.4": ["gest_mowie", "gest_czekam", "postawa_stolik", "dzien_zajecia"],
 "III.5": [None, "gest_skinienie", "emocja_duma", "gest_czekam"],
 "IV.1": ["gest_stop", "zabawa_klocki", "zabawa_rysowanie", "emocja_spokoj"],
 "IV.2": ["gest_czekam", "gest_stop", "polecenie_poloz", "dzien_powrot"],
 "IV.3": ["polecenie_daj", "zabawa_auta", "zabawa_ksiazki", "gest_dziekuje"],
 "IV.4": ["polecenie_daj", "gest_czekam", "zabawa_ukladanka", "emocja_duma"],
 "IV.5": ["gest_czekam", "zabawa_rysowanie", "zabawa_ukladanka", "zeton_diament"],
 "V.1":  ["plan_zmiana", "gest_czekam", "dzien_zajecia", "emocja_spokoj"],
 "V.2":  ["emocja_spokoj", "emocja_zmeczenie", "emocja_zlosc", "strategia_oddech"],
 "V.3":  ["strategia_przerwa", "strategia_oddech", "sensor_ucisk", "prosze_cisza"],
 "V.4":  ["gest_chodz", "postawa_stolik", "gest_brawo", "umiem_pomagam"],
 "V.5":  ["karta_czerwona", "sygnal_ciala", None, "prosze_pomoc"],
}

# Pasek kolejności — trzy pola pod spodem karty.
PASKI = {
 "I.1":  ["polecenie_wez", "polecenie_poloz", "gest_brawo"],
 "I.2":  ["strategia_czesci", "strategia_czesci", "gest_brawo"],
 "I.3":  ["strategia_przerwa", "gest_czekam", "gest_chodz"],
 "I.4":  ["zabawa_ukladanka", "zabawa_klocki", "strategia_czesci"],
 "I.5":  ["strategia_przerwa", "prosze_odpoczynek", "gest_chodz"],
 "II.1": ["polecenie_wez", "postawa_stolik", "polecenie_poloz"],
 "II.2": ["gest_mowie", "prosze_ruch", "emocja_radosc"],
 "II.3": ["instrument_dzwonki", "gest_chodz", "gest_brawo"],
 "II.4": ["gest_brawo", "zabawa_ukladanka", "postawa_stolik"],
 "II.5": ["gest_stop", "gest_stop", "sensor_zamiana"],
 "III.1": ["prosze_pomoc", "gest_czekam", "gest_skinienie"],
 "III.2": ["strategia_pomoc", "gest_skinienie", "gest_mowie"],
 "III.3": ["gest_slucham", "gest_mowie", "gest_slucham"],
 "III.4": ["gest_mowie", "instrument_dzwonki", "postawa_stolik"],
 "III.5": ["strategia_pomoc", "gest_skinienie", "postawa_stolik"],
 "IV.1": ["gest_stop", "zabawa_klocki", "postawa_stolik"],
 "IV.2": ["zabawa_auta", "gest_czekam", "polecenie_poloz"],
 "IV.3": ["polecenie_daj", "gest_czekam", "gest_dziekuje"],
 "IV.4": ["polecenie_daj", "gest_czekam", "gest_brawo"],
 "IV.5": ["gest_czekam", "zabawa_ukladanka", "gest_brawo"],
 "V.1":  ["plan_zmiana", "gest_czekam", "gest_chodz"],
 "V.2":  ["emocja_spokoj", "gest_mowie", "strategia_oddech"],
 "V.3":  ["gest_chodz", "strategia_oddech", "gest_brawo"],
 "V.4":  ["strategia_oddech", "gest_chodz", "gest_brawo"],
 "V.5":  ["sygnal_ciala", "karta_czerwona", "prosze_pomoc"],
}


def plik(kod):
    """Ścieżka do obrazka symbolu albo None, gdy jeszcze nie narysowany."""
    if not kod:
        return None
    p = BIBLIOTEKA / f"k_{kod}.jpg"
    return p if p.exists() else None


def stan():
    """(przypisanych, z obrazkiem, pól do rysowania) — kontrola kompletności."""
    wszystkie = [k for lista in list(KARTY.values()) + list(PASKI.values()) for k in lista]
    przypisane = [k for k in wszystkie if k]
    return len(przypisane), sum(1 for k in przypisane if plik(k)), len(wszystkie) - len(przypisane)
