#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Druk SENS-T — tabela 189 celów SMART z pomocami, poleceniami i konspektami.

    python3 03_kod_zrodlowy/build_tabela.py

Czyta WYŁĄCZNIE pliki z 01_dane_json/ — to one są źródłem. Zapisuje
02_gotowe_dokumenty/sens_tabela_SENS-T.html (otwiera się z dysku, bez serwera).
"""
from __future__ import annotations

import html
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import wspolne_html as wh  # noqa: E402

KORZEN = pathlib.Path(__file__).resolve().parent.parent
DANE = KORZEN / "01_dane_json"
WYJSCIE = KORZEN / "02_gotowe_dokumenty" / "sens_tabela_SENS-T.html"


def e(t) -> str:
    return html.escape(str(t))


def wczytaj(nazwa: str) -> dict:
    p = DANE / nazwa
    if not p.exists():
        raise SystemExit(f"Brak {p}. Uruchom najpierw: python3 03_kod_zrodlowy/eksport_json.py")
    return json.loads(p.read_text(encoding="utf-8"))


def pasek_filtrow(zmysly: dict) -> str:
    opcje = "".join(f'<option value="{k}">{e(v["rzymska"])} · {e(v["nazwa"])}</option>'
                    for k, v in zmysly.items())
    return f"""<div class="filtry">
  <label>Zmysł <select id="f-zmysl"><option value="">wszystkie</option>{opcje}</select></label>
  <label>Poziom <select id="f-poziom"><option value="">wszystkie</option>
    <option value="III">III — wsparcie intensywne</option>
    <option value="II">II — wsparcie umiarkowane</option>
    <option value="I">I — wsparcie podstawowe</option></select></label>
  <label>Wiek <select id="f-wiek"><option value="">wszystkie</option>
    <option value="3-4">3–4 lata</option><option value="5">5 lat</option>
    <option value="6">6 lat</option></select></label>
  <span class="licz" id="licznik"></span>
</div>
<script>
const wiersze = () => document.querySelectorAll('tr[data-zmysl]');
function filtruj(){{
  const z = f_zmysl.value, p = f_poziom.value, w = f_wiek.value;
  let widoczne = 0;
  wiersze().forEach(tr => {{
    const ok = (!z || tr.dataset.zmysl === z) && (!p || tr.dataset.poziom === p)
            && (!w || tr.dataset.wiek === w);
    tr.hidden = !ok; if (ok) widoczne++;
  }});
  document.querySelectorAll('.sheet[data-zmysl]').forEach(s => {{
    s.hidden = !!z && s.dataset.zmysl !== z;
  }});
  licznik.textContent = widoczne + ' z ' + wiersze().length + ' celów';
}}
['f-zmysl','f-poziom','f-wiek'].forEach(id =>
  document.getElementById(id).addEventListener('change', filtruj));
window.addEventListener('DOMContentLoaded', filtruj);
</script>"""


def arkusz_wskaznika(w_id: str, cele: list[dict], pomoc: dict, polecenia: list[dict],
                     konspekty: list[dict], arkusz: dict, numer: int, ile: int) -> str:
    c0 = cele[0]
    zmysl, sektor = c0["zmysl"], c0["sektor"]
    wiersze = []
    for c in cele:
        p = c["poziom_wsparcia"]["kod"]
        wiersze.append(
            f'<tr data-zmysl="{zmysl["klucz"]}" data-poziom="{p}" data-wiek="{c["wersja_wiekowa"]["kod"]}">'
            f'<td><span class="lvl {p}">Poziom {p}</span><br><span class="audio">{e(c["id"])}</span></td>'
            f'<td><b>{e(c["wersja_wiekowa"]["nazwa"])}</b></td>'
            f'<td>{e(c["cel"])}</td>'
            f'<td><b>{e(c["kryterium"])}</b><br>{e(c["horyzont"]["mianownik"])}</td>'
            f'<td>{e(c["wskaznik_obserwacji"])}</td></tr>'
        )
    pol = "".join(
        f'<div class="dziecko"><span class="lvl {p["poziom_wsparcia"]["kod"]}">'
        f'Poziom {p["poziom_wsparcia"]["kod"]}</span> „{e(p["polecenie_dla_dziecka"])}”<br>'
        f'<span class="audio">{e(p["nagranie"])}</span></div>'
        f'<div class="doroslego"><b>Instrukcja słowna dorosłego:</b> {e(p["instrukcja_slowna_doroslego"])}</div>'
        for p in polecenia
    )
    kon = "".join(
        f'<tr><td><span class="lvl {k["poziom_wsparcia"]["kod"]}">Poziom {k["poziom_wsparcia"]["kod"]}</span></td>'
        f'<td><b>{e(k["temat"])}</b><br>{e(k["czas_trwania_min"])} min · {e(k["forma"])}</td>'
        f'<td>{e(k["przebieg"]["czesc_glowna"]["czynnosci"])}</td>'
        f'<td>{e(k["ewaluacja"]["co_liczymy"])}<br><i>{e(k["ewaluacja"]["uwaga_autorki"])}</i><br>'
        f'<span class="audio">cel: {e(k["cel_edukacyjny_zrodlo"]["wzor_id"])}</span></td></tr>'
        for k in konspekty
    )
    return f"""<div class="sheet" data-zmysl="{zmysl['klucz']}">
{wh.naglowek(f'Bank celów SMART · profil sensoryczny · {e(zmysl["nazwa"])}', 'SENS-T', 'WOPF · SI · SMART')}
<div class="sec"><div class="n">{e(zmysl['rzymska'])}</div><h2>{e(zmysl['nazwa'])} · {e(sektor['nazwa'])}</h2><div class="line"></div>
  <span class="lvl I">{e(c0['icf'])}</span></div>
<div class="note">{e(c0['kod'])} · {e(c0['nazwa'])} — kierunek: {e(sektor['kierunek'])}</div>

<div class="box"><b>Strategia sensoryczna (to jest sedno celu):</b> {e(c0['strategia_sensoryczna'])}<br>
<b>Sygnał dziecka:</b> {e(c0['sygnal_dziecka'])} &nbsp;·&nbsp; <b>Co liczymy:</b> {e(c0['wskaznik_obserwacji'])}</div>

<div class="blk">Cele SMART — 3 poziomy wsparcia × 3 wersje wiekowe</div>
<table class="tbl"><thead><tr><th style="width:13%">Poziom</th><th style="width:9%">Wiek</th>
<th style="width:46%">Cel</th><th style="width:11%">Kryterium</th><th>Wskaźnik</th></tr></thead>
<tbody>{''.join(wiersze)}</tbody></table>

<div class="blk">Pomoc dydaktyczna i instrukcje słowne</div>
<div class="box o"><b>{e(pomoc['nazwa'])}</b><br>{e(pomoc['opis_dla_doroslego'])}<br>
<b>Trzy kroki użycia:</b> 1. {e(pomoc['trzy_kroki_uzycia'][0])} 2. {e(pomoc['trzy_kroki_uzycia'][1])}
3. {e(pomoc['trzy_kroki_uzycia'][2])}<br><b>Wskazówka:</b> {e(pomoc['wskazowka_dla_doroslego'])}</div>
<div class="note">Tekst w ramce pomarańczowej mówi się <b>dziecku</b> (to on jest nagrany głosem autorki);
tekst w ramce fioletowej czyta <b>nauczyciel</b>. Nie wolno zamienić ich miejscami.</div>
{pol}

<div class="blk">Konspekty zajęć (KC-3) i arkusz do wycięcia</div>
<table class="tbl"><thead><tr><th style="width:13%">Poziom</th><th style="width:24%">Temat</th>
<th style="width:40%">Część główna</th><th>Ewaluacja</th></tr></thead><tbody>{kon}</tbody></table>
<div class="box"><b>Arkusz A4:</b> {e(arkusz['tytul'])} — {e('; '.join(arkusz['elementy_do_wyciecia']))}<br>
<b>Bezpieczeństwo:</b> {e(c0['ryzyko'])}</div>

<div class="blk">Notatka nauczyciela</div>
<div class="edit" contenteditable="true">kliknij i wpisz własne obserwacje dziecka…</div>
{wh.stopka(numer, ile, 'SENS-T · bank celów SMART')}
</div>"""


def main() -> int:
    cele = wczytaj("cele_sens_poziomy.json")
    pomoce = wczytaj("pomoce_sens.json")
    konspekty = wczytaj("konspekty_sens.json")
    materialy = wczytaj("materialy_do_druku.json")
    obserwacja = wczytaj("cele_sens_obserwacja.json")

    wg_wskaznika: dict[str, list[dict]] = {}
    for c in cele["cele"]:
        wg_wskaznika.setdefault(c["wskaznik_id"], []).append(c)
    pomoc_wg = {p["wskaznik_id"]: p for p in pomoce["pomoce"]}
    polecenia_wg: dict[str, list[dict]] = {}
    for p in pomoce["polecenia_dla_dziecka"]:
        polecenia_wg.setdefault(p["wskaznik_id"], []).append(p)
    konspekty_wg: dict[str, list[dict]] = {}
    for k in konspekty["konspekty"]:
        konspekty_wg.setdefault(k["wskaznik_id"], []).append(k)
    arkusz_wg = {a["wskaznik_id"]: a for a in materialy["arkusze"]}

    ile = len(wg_wskaznika) + 1
    arkusze = [strona_tytulowa(cele, obserwacja, ile)]
    for i, (w_id, lista) in enumerate(wg_wskaznika.items(), start=2):
        arkusze.append(arkusz_wskaznika(w_id, lista, pomoc_wg[w_id], polecenia_wg[w_id],
                                        konspekty_wg[w_id], arkusz_wg[w_id], i, ile))

    WYJSCIE.parent.mkdir(parents=True, exist_ok=True)
    WYJSCIE.write_text(
        wh.dokument("Bank celów SMART · profil sensoryczny (przedszkole) — EduPlaner 2026 · PCTP",
                    arkusze, pasek_filtrow(cele["cele"][0] and
                                           {c["zmysl"]["klucz"]: c["zmysl"] for c in cele["cele"]})),
        encoding="utf-8")
    print(f"zapisano {WYJSCIE.relative_to(KORZEN)} "
          f"({WYJSCIE.stat().st_size // 1024} KB · {len(arkusze)} stron · {cele['liczba_celow']} celów)")
    return 0


def strona_tytulowa(cele: dict, obserwacja: dict, ile: int) -> str:
    poziomy = "".join(
        f'<tr><td><span class="lvl {k}">Poziom {k}</span></td><td>{e(v["nazwa"])}</td>'
        f'<td>{e(v["wsparcie"])}</td><td><b>{e(cele["kryteria_poziomow"][k]["proba"])}</b> · '
        f'{e(cele["kryteria_poziomow"][k]["horyzont"]["mianownik"])}</td>'
        f'<td>{e(cele["kryteria_poziomow"][k]["uzasadnienie"])}</td></tr>'
        for k, v in cele["poziomy_wsparcia"].items())
    progi = "".join(
        f'<tr><td><b>{p["zakres_sumy"][0]}–{p["zakres_sumy"][1]}</b></td><td>{e(p["natezenie"])}</td>'
        f'<td>{e(p["pasmo"])}</td><td><b>{e(p["proba"])}</b> · {e(p["horyzont"]["mianownik"])}</td>'
        f'<td>{e(p["decyzja"])}</td></tr>' for p in obserwacja["progi"])
    return f"""<div class="sheet">
{wh.naglowek('Bank celów SMART · profil sensoryczny · przedszkole', 'SENS-T', 'WOPF · SI · SMART')}
<div class="sec"><div class="n p">I</div><h2>O banku — co tu jest i jak z tego korzystać</h2><div class="line"></div></div>
<div class="box"><b>Zasada modułu.</b> {e(cele['modul']['zasada_modulu'])}</div>
<p style="font-size:9.5px">
<b>{cele['liczba_celow']} celów SMART</b> = 21 wskaźników (7 zmysłów × 3 sektory objawów)
× 3 poziomy wsparcia × 3 wersje wiekowe. Do tego <b>63 konspekty</b> zajęć (KC-3),
<b>21 pomocy</b> dydaktycznych z <b>63 poleceniami</b> dla dziecka i nagraniami,
<b>21 arkuszy A4</b> do wycięcia oraz <b>21 celów</b> do obserwacji pogłębionej (druk SENS-C).</p>

<div class="sec"><div class="n">II</div><h2>Poziomy wsparcia — skąd kryterium i horyzont</h2><div class="line"></div></div>
<div class="note">{e(cele['jak_liczyc_kryterium'])}</div>
<table class="tbl"><thead><tr><th style="width:9%">Poziom</th><th style="width:20%">Nazwa</th>
<th style="width:32%">Wsparcie</th><th style="width:13%">Kryterium</th><th>Dlaczego tyle</th></tr></thead>
<tbody>{poziomy}</tbody></table>

<div class="sec"><div class="n">III</div><h2>Progi druku SENS-C — kryterium z punktacji zmysłu</h2><div class="line"></div></div>
<div class="note">{e(obserwacja['przelicznik_natezenia'])} — suma zmysłu bierze się z druku obserwacji (0–24).</div>
<table class="tbl"><thead><tr><th style="width:11%">Suma 0–24</th><th style="width:11%">Natężenie</th>
<th style="width:26%">Pasmo</th><th style="width:16%">Kryterium</th><th>Decyzja</th></tr></thead>
<tbody>{progi}</tbody></table>

<div class="sec"><div class="n">IV</div><h2>Podstawa</h2><div class="line"></div></div>
<div class="box">{e(cele['modul']['podstawa_merytoryczna'])}<br><br>
{'<br>'.join(e(x) for x in cele['modul']['podstawa_prawna'])}</div>
{wh.stopka(1, ile, 'SENS-T · bank celów SMART')}
</div>"""


if __name__ == "__main__":
    raise SystemExit(main())
