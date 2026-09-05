#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Druk TOM-T — tabela 225 celów SMART, z której wchodzi się w konspekty.

    python3 03_kod_zrodlowy/build_tabela.py

Układ jest ten sam co w druku FBA-T: zakładki wersji wiekowych, jedna tabela
wszystkich celów (wiersz = wskaźnik, kolumna = poziom wsparcia), a kliknięcie
w cel otwiera konspekt zajęć z wyróżnionym tym poziomem. Cel edukacyjny
w konspekcie czytany jest NA ŻYWO z komórki tabeli — nigdy kopiowany.

Czyta wyłącznie pliki z 01_dane_json/. Zapisuje jeden samodzielny plik HTML.
"""
from __future__ import annotations

import argparse
import base64
import html
import json
import pathlib
import sys

KORZEN = pathlib.Path(__file__).resolve().parent.parent
DANE = KORZEN / "01_dane_json"
WYJSCIE = KORZEN / "02_gotowe_dokumenty" / "Tabela_celow_TOM_wiek_poziom.html"
MEDIA = "../04_media"          # ścieżki mediów liczone od 02_gotowe_dokumenty/
MEDIA_KAT = KORZEN / "04_media"   # ten sam katalog na dysku — do wklejania plików w dokument
WSPOLNE = KORZEN.parent / "media_wspolne"   # biblioteka symboli, jedna dla wszystkich modułów


def sciezka_w_opisie(p: pathlib.Path) -> str:
    """Skrót ścieżki w komunikacie — względem modułu, gdy plik w nim leży."""
    try:
        return str(p.relative_to(KORZEN))
    except ValueError:
        return str(p)


def e(t) -> str:
    return html.escape(str(t if t is not None else ""))


def obraz_base64(sciezka_wzgledna: str | None) -> str | None:
    """Zdjęcie pomocy wklejamy w dokument, a nie linkujemy. Dzięki temu konspekt
    drukuje się ze zdjęciem także wtedy, gdy nauczycielka otworzy sam plik HTML,
    bez katalogu 04_media. Gdy pliku nie ma, zostaje opis słowny."""
    if not sciezka_wzgledna:
        return None
    p = MEDIA_KAT / sciezka_wzgledna
    if not p.exists():
        p = WSPOLNE / sciezka_wzgledna
    if not p.exists():
        return None
    typ = "jpeg" if p.suffix.lower() in (".jpg", ".jpeg") else p.suffix.lstrip(".")
    return f"data:image/{typ};base64," + base64.b64encode(p.read_bytes()).decode("ascii")


def wczytaj(nazwa: str) -> dict:
    p = DANE / nazwa
    if not p.exists():
        raise SystemExit(f"Brak {p}. Uruchom najpierw: python3 03_kod_zrodlowy/eksport_json.py")
    return json.loads(p.read_text(encoding="utf-8"))


STYL = """
:root{
  --fiolet:#2D1B69; --fiolet-2:#5a4a94; --fiolet-tlo:#efeaf9; --fiolet-linia:#d9d0f0;
  --pomarancz:#E8450A; --pomarancz-tlo:#fdece4; --pomarancz-linia:#f3cdbd;
  --ink:#2b2733; --szary:#6f6a7d; --paper:#fff; --linia:#e4e1ec; --zebra:#faf7f2;
  --p1:#1f8a5b; --p1-tlo:#eaf6f0; --p1-linia:#bfe3d1;
  --p2:#c8811b; --p2-tlo:#fbf3e3; --p2-linia:#eed6a8;
  --p3:#c0392b; --p3-tlo:#fbebe9; --p3-linia:#f0c3bd;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{background:#e9e7ef;color:var(--ink);padding:18px 12px;
     font-family:'Mulish','Segoe UI',Candara,Arial,sans-serif;-webkit-font-smoothing:antialiased}
.ark{max-width:1180px;margin:0 auto;background:var(--paper);border-radius:14px;padding:22px 26px 18px;
     box-shadow:0 8px 34px rgba(45,27,105,.15)}
.head{display:flex;align-items:center;gap:13px;margin-bottom:14px}
.mark{width:40px;height:40px;border-radius:50%;background:var(--fiolet);border:2px solid #cfc4ea;
      display:flex;align-items:center;justify-content:center;color:#fff;font-size:9px;font-weight:800;
      letter-spacing:.4px;flex:0 0 auto}
.mark::after{content:"PCTP"}
.head h1{font-size:19px;margin:0;color:var(--fiolet);letter-spacing:.2px}
.head .sub{font-size:9.5px;color:var(--szary);letter-spacing:.6px;text-transform:uppercase;
           font-weight:700;margin-top:2px}
.head .prawa{margin-left:auto;text-align:right}
.head .prawa b{display:inline-block;background:var(--pomarancz);color:#fff;font-size:11px;
               padding:5px 13px;border-radius:20px}
.head .prawa span{display:block;font-size:8.5px;color:var(--szary);letter-spacing:.9px;margin-top:4px;
                  text-transform:uppercase}
.kreska{height:3px;border-radius:3px;margin-bottom:14px;
        background:linear-gradient(90deg,var(--fiolet) 0%,var(--fiolet) 55%,var(--pomarancz) 55%,var(--pomarancz) 100%)}
.tyt{margin-bottom:14px}
.pigula{display:inline-block;background:var(--fiolet);color:#fff;font-size:12px;font-weight:800;
        padding:6px 15px;border-radius:20px}
.tyt p{margin:8px 0 0;font-size:12px;line-height:1.6;max-width:78ch;color:#413c4d}
.zakladki{display:flex;gap:8px;margin:14px 0 12px;flex-wrap:wrap}
.tab{border:1px solid var(--fiolet-linia);background:var(--paper);color:var(--ink);border-radius:999px;
     padding:8px 18px;font:600 12px/1.25 inherit;cursor:pointer;text-align:left}
.tab .w{display:block;font-size:8.5px;letter-spacing:.8px;text-transform:uppercase;color:var(--szary);
        font-weight:800}
.tab[aria-selected="true"]{background:var(--fiolet);border-color:var(--fiolet);color:#fff}
.tab[aria-selected="true"] .w{color:#cfc4ea}
.legenda{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:12px}
.leg{border-radius:10px;padding:9px 12px;font-size:10.5px;line-height:1.45;border:1px solid}
.leg b{display:flex;align-items:center;gap:6px;font-size:11px;margin-bottom:3px}
.leg b i{width:10px;height:10px;border-radius:3px;display:inline-block}
.leg .kryt{font-size:9.5px;color:var(--szary);margin-top:3px}
.leg.l3{background:var(--p3-tlo);border-color:var(--p3-linia);color:var(--p3)}
.leg.l2{background:var(--p2-tlo);border-color:var(--p2-linia);color:var(--p2)}
.leg.l1{background:var(--p1-tlo);border-color:var(--p1-linia);color:var(--p1)}
.leg.l3 b i{background:var(--p3)} .leg.l2 b i{background:var(--p2)} .leg.l1 b i{background:var(--p1)}
.uwaga{background:var(--pomarancz-tlo);border:1px solid var(--pomarancz-linia);border-radius:10px;
       padding:10px 14px;font-size:11px;line-height:1.6;margin-bottom:14px}
.uwaga b{color:var(--fiolet)}
.kspis{margin-bottom:12px;border:1px solid var(--fiolet-linia);border-radius:10px;background:#fbfaff}
.kspis summary{cursor:pointer;padding:9px 14px;font-size:11.5px;font-weight:700;color:var(--fiolet)}
.kspis-tresc{padding:0 14px 12px}
.kspis-info{font-size:10px;color:var(--szary);margin:0 0 9px;display:flex;gap:10px;align-items:center;
            flex-wrap:wrap}
.kgrupa{margin-bottom:10px}
.kgrupa h4{font-size:10px;letter-spacing:.7px;text-transform:uppercase;color:var(--fiolet);margin:0 0 5px}
.ksiatka{display:grid;grid-template-columns:repeat(auto-fill,minmax(215px,1fr));gap:6px}
.kbtn{text-align:left;border:1px solid var(--linia);background:#fff;border-radius:8px;padding:6px 9px;
      cursor:pointer;font:inherit;font-size:10px;line-height:1.35}
.kbtn:hover{border-color:var(--pomarancz);background:var(--pomarancz-tlo)}
.kbtn .knr{display:inline-block;background:var(--fiolet);color:#fff;font-size:8px;font-weight:800;
           padding:1px 6px;border-radius:9px;margin-right:5px}
.kbtn b{display:block;margin-top:3px}
.kbtn .kzast{color:var(--szary);font-size:9px}
.chipbtn{border:1px solid var(--fiolet-linia);background:#fff;color:var(--fiolet);border-radius:999px;
         padding:4px 11px;font:700 9.5px/1 inherit;cursor:pointer}
.chipbtn.mocny{background:var(--fiolet);color:#fff;border-color:var(--fiolet)}
table{width:100%;border-collapse:collapse;font-size:10.5px}
caption.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
thead th{background:var(--fiolet);color:#fff;font-size:9px;letter-spacing:.6px;text-transform:uppercase;
         padding:7px 8px;text-align:left;font-weight:800;border-right:1px solid rgba(255,255,255,.18)}
thead th.p3{background:var(--p3)} thead th.p2{background:var(--p2)} thead th.p1{background:var(--p1)}
tr.wband th{background:var(--fiolet-2);font-size:9.5px;text-transform:none;letter-spacing:.3px}
tr.pas td{background:var(--fiolet-tlo);color:var(--fiolet);font-weight:800;font-size:10.5px;
          padding:6px 9px;border-top:2px solid var(--fiolet-linia)}
tr.pas .li{font-weight:600;color:var(--szary);font-size:9px;margin-left:8px}
td{border-bottom:1px solid var(--linia);padding:7px 9px;vertical-align:top;line-height:1.45}
td.nr{font-weight:800;color:var(--fiolet);font-size:10px}
td.wsk b{display:block;font-weight:700;margin-bottom:3px}
td.wsk span{display:block;color:var(--szary);font-size:9.5px}
td.wsk .kzn{color:var(--pomarancz);font-weight:700;margin-top:3px}
td.g{position:relative;cursor:pointer}
td.g:hover{background:var(--pomarancz-tlo)}
td.g .tresc{display:block;padding-right:16px}
td.g .ram{display:inline-block;margin-top:5px;font-size:8.5px;font-weight:700;padding:2px 7px;
          border-radius:9px;border:1px solid}
td.g[data-lvl="p3"] .ram{background:var(--p3-tlo);color:var(--p3);border-color:var(--p3-linia)}
td.g[data-lvl="p2"] .ram{background:var(--p2-tlo);color:var(--p2);border-color:var(--p2-linia)}
td.g[data-lvl="p1"] .ram{background:var(--p1-tlo);color:var(--p1);border-color:var(--p1-linia)}
.mkt-add{position:absolute;top:5px;right:5px;width:17px;height:17px;border-radius:50%;border:1px solid
         var(--fiolet-linia);background:#fff;color:var(--fiolet);font:800 11px/1 inherit;cursor:pointer;
         opacity:0;transition:opacity .12s}
td.g:hover .mkt-add,.mkt-add:focus{opacity:1}
.stopka{margin-top:16px;padding-top:10px;border-top:1px solid var(--linia);display:flex;
        justify-content:space-between;font-size:9px;color:var(--szary);gap:10px;flex-wrap:wrap}
/* ——— konspekt ——— */
.kmodal{display:none;position:fixed;inset:0;background:rgba(30,22,55,.55);z-index:50;overflow:auto;
        padding:22px 12px}
.kmodal.open{display:block}
.kcard{max-width:900px;margin:0 auto;background:#fff;border-radius:12px;padding:24px 28px;position:relative}
.kclose{position:absolute;top:12px;right:14px;width:28px;height:28px;border-radius:50%;
        border:1px solid var(--linia);background:#fff;cursor:pointer;font-size:14px;color:var(--szary)}
.khead{display:flex;align-items:center;gap:12px;margin-bottom:12px}
.khead .kw{font-size:16px;font-weight:800;color:var(--fiolet)}
.khead .ks{font-size:9.5px;color:var(--szary);margin-top:2px;letter-spacing:.4px}
.kpill{margin-left:auto;background:var(--pomarancz);color:#fff;font-size:9.5px;font-weight:700;
       padding:5px 12px;border-radius:20px;white-space:nowrap}
.kmeta{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:10px 0}
.kmeta .field{background:var(--fiolet-tlo);border:1px solid var(--fiolet-linia);border-radius:8px;
              padding:5px 10px;font-size:10px}
.kmeta .field b{display:block;font-size:7.5px;letter-spacing:.7px;text-transform:uppercase;
                color:var(--fiolet);margin-bottom:2px}
.kmeta .dots{display:block;border-bottom:1.5px dotted #b7add6;height:12px}
.ktitle{margin:12px 0 6px}
.kp{display:inline-block;background:var(--fiolet);color:#fff;font-size:8.5px;font-weight:700;
    letter-spacing:.8px;text-transform:uppercase;padding:3px 10px;border-radius:12px}
.ksfera{font-size:9px;color:var(--szary);margin-top:6px;letter-spacing:.3px;text-transform:uppercase;
        font-weight:700}
.ktitle h3{margin:4px 0 2px;font-size:18px;color:var(--fiolet)}
.kpod{font-size:11px;color:var(--szary)}
.kkrok{background:var(--pomarancz-tlo);border:1px solid var(--pomarancz-linia);border-radius:9px;
            padding:8px 12px;font-size:10.5px;margin:8px 0}
.kkrok b{color:var(--fiolet)}
.kkrok span{display:block;color:var(--szary);font-size:9.5px;margin-top:2px}
.ksec{display:flex;align-items:center;gap:8px;margin:14px 0 5px}
.ksec .sq{min-width:20px;height:20px;padding:0 5px;border-radius:5px;background:var(--pomarancz);color:#fff;
          display:flex;align-items:center;justify-content:center;font-weight:800;font-size:10px}
.ksec h4{margin:0;font-size:11px;letter-spacing:.7px;text-transform:uppercase;color:var(--fiolet)}
.ksec .line{flex:1;height:1px;background:var(--linia)}
.kcele{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.kcel{border:1px solid var(--linia);border-radius:9px;padding:9px 12px;font-size:10px}
.kcel.edu{background:#fbfaff}
.kchead{font-size:8.5px;font-weight:800;letter-spacing:.6px;text-transform:uppercase;
        color:var(--fiolet);margin-bottom:5px}
.kvar{padding:5px 0;border-top:1px dashed var(--linia)}
.kvar:first-of-type{border-top:0}
.kvar.wyb{background:var(--pomarancz-tlo);border-radius:7px;padding:5px 8px;margin:3px -8px}
.kvlvl{display:inline-block;font-size:8px;font-weight:800;padding:1px 7px;border-radius:9px}
.kvlvl.p3{background:var(--p3-tlo);color:var(--p3)} .kvlvl.p2{background:var(--p2-tlo);color:var(--p2)}
.kvlvl.p1{background:var(--p1-tlo);color:var(--p1)}
.ktresc{margin-top:3px;line-height:1.45}
.kkryt{font-size:9px;color:var(--szary);margin-top:3px}
.ksmart{list-style:none;margin:6px 0 0;padding:0}
.ksmart li{display:flex;gap:7px;margin-bottom:3px;font-size:9.5px;line-height:1.4}
.ksmart b{background:var(--fiolet);color:#fff;width:15px;height:15px;border-radius:4px;display:flex;
          align-items:center;justify-content:center;font-size:8.5px;flex:0 0 auto}
.kdwie{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.klista{margin:0;padding-left:16px;font-size:10px;line-height:1.5}
.krodzaj{font-size:10.5px;background:var(--fiolet-tlo);border-radius:8px;padding:7px 11px}
.kkurs{font-size:9.5px;color:var(--szary);font-style:italic;margin:6px 0}
table.ktab{margin-top:4px;font-size:10px}
table.ktab thead th{background:var(--fiolet-2)}
table.ktab td.lp{font-weight:800;color:var(--fiolet);text-align:center}
.kmods{display:grid;grid-template-columns:repeat(3,1fr);gap:9px;margin-top:5px}
.kmod{border-radius:9px;padding:8px 10px;font-size:9.5px;border:1px solid}
.kmod b{display:block;margin-bottom:4px;font-size:10px}
.kmod.m3{background:var(--p3-tlo);border-color:var(--p3-linia);color:var(--p3)}
.kmod.m2{background:var(--p2-tlo);border-color:var(--p2-linia);color:var(--p2)}
.kmod.m1{background:var(--p1-tlo);border-color:var(--p1-linia);color:var(--p1)}
.kmod .klista{color:var(--ink)}
.kmod.wyb{outline:2px solid var(--fiolet);outline-offset:2px}
.kwsk{background:var(--fiolet-tlo);border-left:3px solid var(--fiolet);border-radius:0 8px 8px 0;
      padding:8px 12px;font-size:10px;line-height:1.55;margin-top:9px}
.pom{border:1px solid var(--linia);border-radius:10px;overflow:hidden;margin-top:6px}
.pom-head{background:var(--fiolet-tlo);padding:8px 12px;display:flex;align-items:center;gap:9px}
.pom-head h5{margin:0;font-size:12px;color:var(--fiolet)}
.pom-head .wiek{margin-left:auto;font-size:9px;color:var(--szary);font-weight:700}
.pom-cialo{display:grid;grid-template-columns:200px 1fr;gap:12px;padding:12px}
.pom-foto{margin:0;border:1px solid var(--fiolet-linia);border-radius:9px;background:#fbfaff;
          overflow:hidden;display:flex;flex-direction:column}
.pom-foto .kadr{flex:1;width:100%;min-height:126px;background-size:cover;background-position:center}
.pom-foto figcaption{padding:5px 7px;font-size:8px;line-height:1.35;color:var(--szary);text-align:center}
.pom-foto.pusta{border-style:dashed;min-height:150px;align-items:center;justify-content:center;
          padding:10px;font-size:8.5px;color:var(--szary);text-align:center;line-height:1.45}
.pom-tresc h6{margin:0 0 3px;font-size:9px;letter-spacing:.6px;text-transform:uppercase;color:var(--fiolet)}
.pom-tresc ul,.pom-tresc ol{margin:0 0 8px;padding-left:16px;font-size:10px;line-height:1.5}
.pom-dziecko{background:var(--pomarancz-tlo);border-left:3px solid var(--pomarancz);border-radius:0 8px 8px 0;
             padding:7px 11px;font-size:11px;margin-top:6px}
.pom-dziecko .lab{display:block;font-size:8px;letter-spacing:.6px;text-transform:uppercase;
                  color:var(--pomarancz);font-weight:800;margin-bottom:2px}
.pom-play{border:1px solid var(--pomarancz-linia);background:#fff;color:var(--pomarancz);border-radius:999px;
          padding:3px 10px;font:700 9px/1 inherit;cursor:pointer;margin-top:5px}
.pom-play small{font-weight:400;color:var(--szary)}
.pom-plik{display:block;font-family:ui-monospace,Consolas,monospace;font-size:7.5px;color:var(--szary);margin-top:3px}
.karty{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:6px}
.karta{border:1px dashed var(--fiolet-linia);border-radius:9px;padding:8px;text-align:center;font-size:9px}
.karta .pole{height:52px;border-radius:7px;background:#fbfaff;border:1px solid var(--linia);margin-bottom:5px;
             display:flex;align-items:center;justify-content:center;color:var(--szary);font-size:7.5px;
             padding:4px;line-height:1.3;background-size:cover;background-position:center}
.karta .et{font-weight:800;color:var(--fiolet);font-size:10px}
.karta .op{color:var(--szary);margin-top:2px;line-height:1.35}
.pasek{display:flex;gap:8px;margin-top:8px}
.pasek .pole-k{flex:1;border:1px solid var(--fiolet-linia);border-radius:8px;padding:6px;text-align:center;
               font-size:9px;font-weight:700;color:var(--fiolet);background:var(--fiolet-tlo)}
.formularz{display:grid;gap:8px;font-size:11px}
.formularz label{display:grid;gap:3px;font-size:9.5px;font-weight:700;color:var(--fiolet)}
.formularz input,.formularz textarea,.formularz select{font:inherit;font-size:11px;font-weight:400;
  color:var(--ink);border:1px solid var(--fiolet-linia);border-radius:7px;padding:6px 9px;width:100%}
.formularz textarea{min-height:64px;resize:vertical}
.fdwie{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.ftrzy{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.fprzyciski{display:flex;gap:8px;justify-content:flex-end;margin-top:10px;flex-wrap:wrap}
.fbtn{border-radius:999px;padding:7px 16px;font:700 11px/1 inherit;cursor:pointer;border:1px solid var(--fiolet-linia);background:#fff;color:var(--fiolet)}
.fbtn.mocny{background:var(--fiolet);color:#fff;border-color:var(--fiolet)}
.fbtn.usun{color:var(--p3);border-color:var(--p3-linia)}
.komunikat{font-size:10px;color:var(--szary);margin-right:auto;align-self:center}
@media (max-width:900px){
  .legenda,.kcele,.kdwie,.kmods,.karty{grid-template-columns:1fr}
  .kmeta{grid-template-columns:1fr 1fr}
  .pom-cialo{grid-template-columns:1fr}
  table{font-size:10px}
}
/* ——— historyjki obrazkowe, drabiny i skale ———
   Rysunek przychodzi bez tekstu, podpis polski stoi pod nim — dzięki temu
   poprawka słowa nie wymaga przerysowywania obrazka. Drabina idzie od dołu
   do góry, bo tak dziecko czyta wysiłek: najniższy szczebel jest najłatwiejszy. */
.hist{margin:10px 0 4px;border:1px solid var(--linia);border-radius:8px;background:#fbfaff;padding:10px}
.hist>h6{font-size:9px;letter-spacing:.6px;text-transform:uppercase;color:var(--fiolet);margin:0 0 4px}
.hist .hopis{font-size:9.5px;line-height:1.5;color:var(--szary);margin:0 0 8px}
.hist .hopis b{color:var(--tekst)}
.hist .hpola{display:grid;grid-template-columns:repeat(auto-fill,minmax(105px,1fr));gap:8px}
.hist figure{margin:0;min-width:0}
.hist img{width:100%;aspect-ratio:4/3;object-fit:contain;border:1px solid var(--linia);
  border-radius:6px;background:#fff;display:block}
.hist .hnr{display:inline-block;min-width:15px;height:15px;line-height:15px;text-align:center;
  border-radius:50%;background:var(--fiolet);color:#fff;font-size:8.5px;font-weight:800;margin-right:4px}
.hist .hp{font-size:10px;font-weight:700;color:var(--fiolet);margin-top:4px;line-height:1.3}
.hist .hq{display:block;font-size:9px;color:var(--szary);font-style:italic;line-height:1.4;margin-top:1px}
.hist.drabina .hpola{display:flex;flex-direction:column-reverse;gap:6px}
.hist.drabina figure{display:grid;grid-template-columns:86px 1fr;gap:9px;align-items:center}
.hist.drabina .hp{margin-top:0}
.hist .hwiersz{display:grid;grid-template-columns:1fr auto 2fr;gap:8px;align-items:center;
  padding:6px 0;border-top:1px dashed var(--linia)}
.hist .hwiersz:first-of-type{border-top:none}
.hist .hstrzalka{font-size:16px;color:var(--pomarancz);font-weight:800}
.hist .hkonce{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.hist .hnazwa{grid-column:1/-1;font-size:9px;letter-spacing:.5px;text-transform:uppercase;
  color:var(--szary);margin-bottom:-2px}

.ob{width:100%;background-size:contain;background-position:center;background-repeat:no-repeat;
  background-color:#fff}

@media print{
  *{-webkit-print-color-adjust:exact;print-color-adjust:exact}
  @page{size:A4 landscape;margin:9mm}
  @page kon{size:A4 portrait;margin:10mm}
  body{background:#fff;padding:0}
  .ark{max-width:none;box-shadow:none;border-radius:0;padding:0}
  .zakladki,.kspis,.mkt-add,.pom-play,.chipbtn,.fprzyciski{display:none !important}
  thead{display:table-header-group}
  tr,.uwaga,.leg{break-inside:avoid}
  .kmodal{display:none !important}
  html.druk-konspektu .ark{display:none !important}
  html.druk-konspektu .kmodal.open{display:block !important;position:static;background:none;
    padding:0;overflow:visible}
  html.druk-konspektu .kcard{box-shadow:none;max-width:none;padding:0;border-radius:0;page:kon;zoom:.95}
  html.druk-konspektu .kclose{display:none}
  .pom,.kmod,.karta,.pom-foto,.hist figure,.hist .hwiersz{break-inside:avoid}
  .pom-cialo{grid-template-columns:170px 1fr}
}
"""

def naglowek(liczba_celow: int) -> str:
    return f"""<div class="head">
  <span class="mark" role="img" aria-label="Logo PCTP"></span>
  <div><h1>EduPlaner 2026</h1>
    <div class="sub">Teoria umysłu (ToM) · tabela celów SMART · wiek i poziom wsparcia</div></div>
  <div class="prawa"><b>ToM · WOPF</b><span>narzędzie · druk TOM-T</span></div>
</div>
<div class="kreska"></div>
<div class="tyt">
  <span class="pigula">{liczba_celow} celów SMART</span>
  <p>25 wskaźników karty obserwacji ToM — pięć komponentów po pięć pozycji — × trzy wersje
     wiekowe × trzy poziomy wsparcia. Wiersz mówi, <b>co dziecko robi albo mówi, po czym widać,
     że uwzględniło cudzą perspektywę</b>; kolumna — ile przy tym dostaje podpory. Kliknięcie w cel otwiera konspekt
     zajęć z wyróżnionym tym poziomem.</p>
</div>"""


def zakladki(wersje: list[dict]) -> str:
    p = "".join(
        f'<button type="button" class="tab" role="tab" data-wersja="{w["klucz"]}" '
        f'aria-selected="{"true" if i == 0 else "false"}">'
        f'<span class="w">wersja {w["klucz"]}</span>{e(w["wiek"])}</button>'
        for i, w in enumerate(wersje))
    return f'<div class="zakladki" role="tablist" aria-label="Wersje wiekowe">{p}</div>'


def legenda(poziomy: list[dict]) -> str:
    p = "".join(
        f'<div class="leg l{poz["rzym"].count("I")}"><b><i aria-hidden="true"></i>{e(poz["nazwa"])}</b>'
        f'{e(poz["warunki"])}<div class="kryt">kryterium {e(poz["kryterium"])} sytuacji · '
        f'weryfikacja po {e(poz["horyzont"]).replace("tygodni", "tygodniach")}</div></div>'
        for poz in poziomy)
    return f'<div class="legenda">{p}</div>'


def uwaga(opis_modulu: str) -> str:
    return f"""<div class="uwaga"><b>Poziom zmienia warunki, nie krok mentalizacji.</b>
  Na każdym poziomie dziecko wykonuje ten sam krok — nazwanie, wskazanie, uzgodnienie —
  tylko z inną ilością podpory. Cel przepisujemy do IPET-u w brzmieniu z komórki i dokładamy
  kryterium oraz horyzont z nagłówka kolumny. Kryterium na Poziomie I zostaje <b>4 z 5</b>,
  a nie rośnie do 5 z 5: rośnie trudność samego zachowania, nie liczba prób — „za każdym razem”
  to w przedszkolu cel nie do osiągnięcia i psuje ewaluację, zamiast ją domykać.
  <br><br>{e(opis_modulu)}</div>"""


def wykaz_konspektow(wersja: str, komponenty: list[dict], konspekty_wg: dict) -> str:
    grupy = []
    for z in komponenty:
        karty = "".join(
            f'<button type="button" class="kbtn" data-kon="{konspekty_wg[(w["nr"], wersja)]["id"]}" '
            f'data-wersja="{wersja}" data-wsk="{e(w["nr"])}" data-lvl="p2">'
            f'<span class="knr">{e(w["nr"])}</span>'
            f'<b>{e(konspekty_wg[(w["nr"], wersja)]["tytul"])}</b>'
            f'<span class="kzast">{e(w["krok_mentalizacji"])}</span></button>'
            for w in z["wskazniki"])
        grupy.append(f'<div class="kgrupa"><h4>Komponent {e(z["nr"])} · {e(z["nazwa"])} '
                     f'<span style="font-weight:600;color:var(--szary)">{e(z["icf"])}</span></h4>'
                     f'<div class="ksiatka">{karty}</div></div>')
    return f"""<details class="kspis"><summary>Wykaz konspektów · 25 scenariuszy zajęć do tej wersji wiekowej</summary>
  <div class="kspis-tresc">
    <p class="kspis-info">Konspekt otwiera też kliknięcie celu w tabeli — otwarty scenariusz ma
      wtedy wyróżniony ten poziom wsparcia, w który kliknięto.
      <button type="button" class="chipbtn mocny" data-zeszyt="{wersja}">Drukuj wszystkie 25 konspektów (A4)</button>
      <button type="button" class="chipbtn" data-moje="{wersja}">Moje konspekty</button></p>
    {''.join(grupy)}
    <div class="kgrupa" data-mkt-lista="{wersja}"></div>
  </div></details>"""


def tabela_wersji(wersja: str, wiek: str, komponenty: list[dict], poziomy: list[dict],
                  konspekty_wg: dict) -> str:
    wiersze = []
    for z in komponenty:
        wiersze.append(f'<tr class="pas"><td colspan="5">Komponent {e(z["nr"])} · {e(z["nazwa"])}'
                       f'<span class="li">pięć pozycji karty · {e(z["icf"])} · {e(z["pp"])}</span></td></tr>')
        for w in z["wskazniki"]:
            kon = konspekty_wg[(w["nr"], wersja)]
            komorki = []
            for poz in poziomy:
                k = poz["klucz"]
                komorki.append(
                    f'<td class="g" data-kon="{kon["id"]}" data-lvl="{k}" data-wersja="{wersja}" '
                    f'data-wsk="{e(w["nr"])}" tabindex="0" role="button" '
                    f'title="Otwórz konspekt zajęć do tego celu">'
                    f'<span class="tresc">{e(w["cele"][wersja][k])}</span>'
                    f'<span class="ram">{e(poz["kryterium"])} sytuacji · {e(poz["horyzont"])}</span>'
                    f'<button class="mkt-add" type="button" title="Dodaj własny konspekt do tego celu" '
                    f'aria-label="Dodaj własny konspekt do tego celu">+</button></td>')
            wiersze.append(
                f'<tr data-wsk="{e(w["nr"])}" data-komponent="{e(z["nr"])}" '
                f'data-krok="{e(w["krok_mentalizacji"])}">'
                f'<td class="nr">{e(w["nr"])}</td>'
                f'<td class="wsk"><b>{e(w["wskaznik"])}</b>'
                f'<span>krok mentalizacji: {e(w["krok_mentalizacji"])}</span>'
                f'<span>pozycja karty obserwacji: {e(w["pozycja"])} · skala 0–2</span>'
                f'<span class="kzn">konspekt: {e(kon["tytul"])}</span></td>'
                + "".join(komorki) + "</tr>")
    naglowki = "".join(f'<th class="{p["klucz"]}">{e(p["nazwa"])}</th>' for p in poziomy)
    return f"""<section class="wersja" id="w-{wersja}" data-wersja="{wersja}">
  {wykaz_konspektow(wersja, komponenty, konspekty_wg)}
  <table>
    <colgroup><col style="width:6%"><col style="width:31%">
      <col style="width:21%"><col style="width:21%"><col style="width:21%"></colgroup>
    <caption class="sr-only">Cele SMART · wersja {wersja} · {e(wiek)}</caption>
    <thead>
      <tr class="wband"><th colspan="5">EduPlaner 2026 · druk TOM-T · cele SMART do wskaźników
        teorii umysłu <b>wersja {wersja} · {e(wiek)}</b></th></tr>
      <tr><th>Nr</th><th>Wskaźnik z karty obserwacji ToM</th>{naglowki}</tr>
    </thead>
    <tbody>{''.join(wiersze)}</tbody>
  </table>
</section>"""

WKLEJ_GLOS = False   # ustawiane przez --z-glosem; patrz uwaga niżej


def zrodlo_audio(sciezka_wzgledna: str) -> str:
    """Nagranie polecenia.

    GŁOS JEST DANĄ BIOMETRYCZNĄ. Domyślnie dokument tylko LINKUJE plik z 04_media
    — dzięki temu wersja w repozytorium nie zawiera sklonowanego głosu autorki.
    Z opcją --z-glosem nagranie zostaje wklejone w plik (base64) i dokument gra
    z pendrive'a, bez katalogu mediów. Taki plik jest do użytku własnego autorki
    i nie trafia do repozytorium (patrz .gitignore)."""
    plik = MEDIA_KAT / sciezka_wzgledna
    if WKLEJ_GLOS and plik.exists():
        return "data:audio/mpeg;base64," + base64.b64encode(plik.read_bytes()).decode("ascii")
    return f"{MEDIA}/{sciezka_wzgledna}"


def klasa_zdjecia(pomoc: dict) -> str:
    """Nazwa klasy CSS zdjęcia — z nazwy pliku, np. k_i_1.jpg → foto-k-i-1."""
    return "foto-" + pathlib.Path(pomoc["zdjecie"]).stem.replace("_", "-")



def klasa_obrazka(sciezka: str) -> str:
    """Nazwa klasy CSS obrazka — z nazwy pliku, np. iv_4_p1.jpg → o-iv-4-p1."""
    return "o-" + pathlib.Path(sciezka).stem.replace("_", "-")


def styl_obrazkow(pomoce: list[dict], arkusze: list[dict]) -> str:
    """Symbole i pola historyjek wklejamy tak samo jak zdjęcia pomocy: raz na plik,
    jako regułę CSS. Ten sam symbol wraca w kilku wskaźnikach i w każdym z trzech
    konspektów — wklejony w miejscu użycia rozdąłby dokument kilkunastokrotnie."""
    sciezki = set()
    for a in arkusze:
        sciezki |= {k["plik_symbolu"] for k in a["karty"] + a["pasek_kolejnosci"] if k["plik_symbolu"]}
    for p in pomoce:
        h = p.get("historyjka")
        if not h:
            continue
        pola = h.get("pola") or [x for w in h["wiersze"] for x in [w["poczatek"]] + w["zakonczenia"]]
        sciezki |= {x["plik"] for x in pola}
    reguly = []
    for sciezka in sorted(sciezki):
        dane = obraz_base64(sciezka)
        if dane:
            reguly.append(f'.{klasa_obrazka(sciezka)}{{background-image:url("{dane}")}}')
    return "\n".join(reguly)


def styl_zdjec(pomoce: list[dict]) -> str:
    """Każde zdjęcie pomocy wklejamy w dokument RAZ, jako regułę CSS. Ten sam
    wskaźnik ma trzy konspekty (A, B, C), więc gdyby zdjęcie siedziało w każdym
    z nich osobno, plik urósłby trzykrotnie bez żadnego zysku."""
    reguly = []
    for sciezka in sorted({p["zdjecie"] for p in pomoce}):
        dane = obraz_base64(sciezka)
        if not dane:
            continue
        klasa = "foto-" + pathlib.Path(sciezka).stem.replace("_", "-")
        reguly.append(f'.{klasa} .kadr{{background-image:url("{dane}")}}')
    return "\n".join(reguly)


def pole_zdjecia(pomoc: dict) -> str:
    """Zdjęcie pomocy w konspekcie. Plik jest wklejony w dokument, więc konspekt
    drukuje się ze zdjęciem także wtedy, gdy nauczycielka otworzy sam HTML, bez
    katalogu 04_media. Gdy zdjęcia nie ma, zostaje opis słowny."""
    if not obraz_base64(pomoc.get("zdjecie")):
        return (f'<figure class="pom-foto pusta"><span>zdjęcie pomocy<br>'
                f'{e(pomoc["zdjecie"])}</span></figure>')
    return (f'<figure class="pom-foto {klasa_zdjecia(pomoc)}">'
            f'<div class="kadr" role="img" aria-label="{e(pomoc["nazwa"])}"></div>'
            f'<figcaption>{e(pomoc["nazwa"])}</figcaption></figure>')



def blok_historyjki(h: dict | None) -> str:
    """Historyjka obrazkowa, drabina albo skala — tam, gdzie pomoc ich wymaga.
    Kolejność pól niesie znaczenie, więc numerujemy je i nie pozwalamy im się
    przemieszać: historyjka czyta się w prawo, drabina w górę."""
    if not h:
        return ""

    def figura(p, nr=None) -> str:
        numer = f'<span class="hnr">{nr}</span>' if nr else ""
        pytanie = f'<span class="hq">{e(p["pytanie"])}</span>' if p.get("pytanie") else ""
        return (f'<figure><div class="ob {klasa_obrazka(p["plik"])}" role="img" '
                f'aria-label="{e(p["podpis"])}"></div>'
                f'<figcaption class="hp">{numer}{e(p["podpis"])}{pytanie}</figcaption></figure>')

    if h["rodzaj"] == "rozgalezienie":
        srodek = "".join(
            f'<div class="hwiersz"><span class="hnazwa">{e(w["nazwa"])}</span>'
            f'{figura(w["poczatek"])}<span class="hstrzalka">→</span>'
            f'<div class="hkonce">{"".join(figura(z) for z in w["zakonczenia"])}</div></div>'
            for w in h["wiersze"])
    else:
        numeruj = h["rodzaj"] in ("historyjka", "listwa", "drabina")
        srodek = ('<div class="hpola">'
                  + "".join(figura(p, i if numeruj else None)
                            for i, p in enumerate(h["pola"], 1))
                  + "</div>")
    return (f'<div class="hist {e(h["rodzaj"])}"><h6>{e(h["tytul"])}</h6>'
            f'<p class="hopis"><b>Po co:</b> {e(h["po_co_dla_doroslego"])} '
            f'<b>Jak użyć:</b> {e(h["jak_uzyc_dla_doroslego"])}</p>{srodek}</div>')


def karta_pomocy(kon: dict, pomoc: dict, arkusz: dict) -> str:
    pol = pomoc["polecenia"][kon["wersja_wiekowa"]]
    def pole_symbolu(k) -> str:
        """Symbole leżą w bibliotece banku KPOF. Gdy pliku nie ma pod ręką, karta
        pokazuje jego nazwę — nauczycielka wie wtedy, co wkleić w puste pole."""
        if not k["plik_symbolu"]:
            return '<div class="pole">pole na własny symbol z tablicy AAC</div>'
        return (f'<div class="pole"><div class="ob {klasa_obrazka(k["plik_symbolu"])}" '
                f'role="img" aria-label="{e(k["etykieta_dla_dziecka"])}" '
                f'style="height:100%"></div></div>')

    karty = "".join(
        f'<div class="karta">{pole_symbolu(k)}'
        f'<div class="et">{e(k["etykieta_dla_dziecka"])}</div>'
        f'<div class="op">{e(k["opis_dla_doroslego"])}</div></div>'
        for k in arkusz["karty"])
    pasek = "".join(f'<div class="pole-k">{e(p["etykieta_dla_dziecka"])}</div>'
                    for p in arkusz["pasek_kolejnosci"])
    return f"""<section class="pom">
  <div class="pom-head"><span class="kp">Pomoc dydaktyczna · druk KC-4</span>
    <h5>{e(pomoc['nazwa'])}</h5><span class="wiek">{e(kon['wiek'])}</span></div>
  <div class="pom-cialo">
    {pole_zdjecia(pomoc)}
    <div class="pom-tresc">
      <h6>Co przygotować</h6>
      <ul>{''.join(f'<li>{e(x)}</li>' for x in pomoc['co_przygotowac'])}</ul>
      <h6>Jak użyć — trzy kroki</h6>
      <ol>{''.join(f'<li>{e(x)}</li>' for x in pomoc['trzy_kroki_uzycia'])}</ol>
      <h6>Wskazówka dla dorosłego</h6>
      <p style="font-size:10px;line-height:1.5;margin:0">{e(pomoc['wskazowka_dla_doroslego'])}</p>
      <div class="pom-dziecko"><span class="lab">Polecenie dla dziecka · {e(pol['wiek'])}</span>
        „{e(pol['polecenie_dla_dziecka'])}”
        <button type="button" class="pom-play" data-audio="{e(zrodlo_audio(pol['nagranie']))}">
          ▶ posłuchaj głosem autorki</button>
        <span class="pom-plik">nagranie: {e(pol['nagranie'].rsplit('/', 1)[-1])}</span></div>
    </div>
  </div>
  <div style="padding:0 12px 12px">
    <h6 style="font-size:9px;letter-spacing:.6px;text-transform:uppercase;color:var(--fiolet);margin:4px 0 2px">
      Arkusz A4 do wycięcia · {e(arkusz['tytul'])}</h6>
    <p class="kkurs" style="margin:2px 0 6px">{e(arkusz['wstep_dla_doroslego'])}</p>
    {blok_historyjki(pomoc.get('historyjka'))}
    <div class="karty">{karty}</div>
    <div class="pasek">{pasek}</div>
  </div>
</section>"""


def modal_konspektu(kon: dict, pomoc: dict, arkusz: dict, wskaznik: dict, poziomy: list[dict]) -> str:
    warianty = "".join(
        f'<div class="kvar" data-lvl="{p["klucz"]}"><span class="kvlvl {p["klucz"]}">{e(p["nazwa"])}</span>'
        f'<div class="ktresc kon-cel"></div>'
        f'<div class="kkryt"><b>Kryterium:</b> <span class="kon-kryt"></span></div></div>'
        for p in poziomy)
    smart = "".join(f'<li><b>{e(s["litera"])}</b><span>{e(s["tresc"])}</span></li>'
                    for s in kon["cel_terapeutyczny"]["smart"])
    przebieg = "".join(f'<tr><td class="lp">{p["lp"]}</td><td>{e(p["nauczyciel"])}</td>'
                       f'<td>{e(p["dziecko"])}</td></tr>' for p in kon["przebieg"])
    mody = "".join(
        f'<div class="kmod m{p["rzym"].count("I")}" data-mod="{p["klucz"]}">'
        f'<b>{e(p["nazwa"])} · {e(p["kolor_oceny"]).capitalize()}</b><ul class="klista">'
        + "".join(f'<li>{e(x)}</li>' for x in kon["modyfikacje"][p["klucz"]]["kroki"]) + "</ul></div>"
        for p in poziomy)
    return f"""<div class="kmodal" id="{kon['id']}" data-wersja="{kon['wersja_wiekowa']}"
  data-wsk="{e(kon['wskaznik'])}" role="dialog" aria-modal="true"
  aria-label="Konspekt zajęć: {e(kon['tytul'])}">
  <div class="kcard">
    <button class="kclose" data-zamknij aria-label="Zamknij konspekt" title="Zamknij (Esc)">✕</button>
    <div class="khead"><span class="mark" role="img" aria-label="Logo PCTP"></span>
      <div><div class="kw">EduPlaner 2026</div>
        <div class="ks">Konspekt · komponent {e(kon['komponent'])} · pozycja {e(kon['pozycja'])} · wersja
          {e(kon['wersja_wiekowa'])} · {e(kon['wiek'])} · wskaźnik {e(kon['wskaznik'])}</div></div>
      <span class="kpill">Konspekt ToM {e(kon['wersja_wiekowa'])}-{e(kon['wskaznik'])}</span></div>
    <div class="kmeta" style="grid-template-columns:1.6fr 1fr 1fr">
      <div class="field"><b>Dotyczy dziecka</b><span class="dots"></span></div>
      <div class="field"><b>Grupa</b><span class="dots"></span></div>
      <div class="field"><b>Data</b><span class="dots"></span></div></div>
    <div class="ktitle"><span class="kp">Konspekt zajęć · druk KC-3</span>
      <div class="ksfera">{e(kon['sfera'])}</div>
      <h3>{e(kon['tytul'])}</h3><div class="kpod">{e(kon['podtytul'])}</div></div>
    <div class="kmeta">
      <div class="field"><b>Czas</b>{e(kon['czas'])}</div>
      <div class="field"><b>Forma</b>{e(kon['forma'])}</div>
      <div class="field"><b>Cykl</b>{e(kon['cykl'])}</div>
      <div class="field"><b>Poziom wsparcia</b><span class="kon-poz">wszystkie trzy</span></div></div>
    <div class="kkrok"><b>Krok mentalizacji:</b> {e(wskaznik['krok_mentalizacji'])}
      <span>{e(wskaznik['opis_kroku'])}</span></div>

    <div class="ksec"><span class="sq">I</span><h4>Cel SMART</h4><span class="line"></span></div>
    <div class="kcele">
      <div class="kcel edu"><div class="kchead">Cel edukacyjny — z tabeli TOM-T, wg klikniętego poziomu</div>
        {warianty}</div>
      <div class="kcel ter"><div class="kchead">Cel terapeutyczny</div>
        <div class="ktresc">{e(kon['cel_terapeutyczny']['tresc'])}</div>
        <ul class="ksmart">{smart}</ul>
        <div class="kkryt"><b>Kryterium:</b> {e(kon['cel_terapeutyczny']['kryterium'])}</div></div>
    </div>

    <div class="kdwie">
      <div><div class="ksec"><span class="sq">II</span><h4>Pomoce dydaktyczne</h4><span class="line"></span></div>
        <ul class="klista">{''.join(f'<li>{e(x)}</li>' for x in kon['pomoce'])}</ul></div>
      <div><div class="ksec"><span class="sq">III</span><h4>Metody i formy działań</h4><span class="line"></span></div>
        <ul class="klista">{''.join(f'<li>{e(x)}</li>' for x in kon['metody'])}</ul></div>
    </div>
    <div class="kdwie" style="align-items:end">
      <div><div class="ksec"><span class="sq">IV</span><h4>Sposób realizacji</h4><span class="line"></span></div>
        <div class="krodzaj" style="font-style:italic">Tabela poniżej ↓</div></div>
      <div><div class="ksec"><span class="sq">V</span><h4>Rodzaj zajęć</h4><span class="line"></span></div>
        <div class="krodzaj">{e(kon['rodzaj_zajec'])}</div></div>
    </div>
    <p class="kkurs">Konkretne czynności nauczyciela (N) i odpowiadające im oczekiwane reakcje
      i umiejętności dziecka (D).</p>
    <table class="ktab">
      <thead><tr><th style="width:26px">Lp.</th><th style="width:47%">Czynności nauczyciela (N)</th>
        <th>Oczekiwane reakcje i umiejętności dziecka (D)</th></tr></thead>
      <tbody>{przebieg}</tbody></table>

    <div class="ksec"><span class="sq">VI</span><h4>Modyfikacja według poziomu wsparcia</h4>
      <span class="line"></span></div>
    <p class="kkurs">Poziom zmienia warunki, nie przebieg zajęć. Modyfikację stosuje się, gdy brak
      progresu w dwóch kolejnych sesjach; przy pełnym sukcesie przechodzi się o poziom wyżej.
      Kliknięty poziom jest wyróżniony.</p>
    <div class="kmods">{mody}</div>
    <div class="kwsk"><b>Wskazówka dla prowadzącego:</b> {e(kon['wskazowka'])}</div>
    <div class="kwsk" style="border-left-color:var(--pomarancz);background:var(--pomarancz-tlo)">
      <b>Bezpieczeństwo:</b> {e(kon['bezpieczenstwo'])}</div>

    <div class="ksec"><span class="sq">VII</span><h4>Materiały do wydruku</h4><span class="line"></span></div>
    <p class="kkurs">Karta pomocy z poleceniem nagranym głosem autorki, a pod nią materiał
      do wycięcia — cztery karty i pasek kolejności, A4 pionowo.</p>
    {karta_pomocy(kon, pomoc, arkusz)}
    <div class="fprzyciski">
      <span class="komunikat">Cel edukacyjny czyta się na żywo z tabeli — po poprawce autorki
        konspekt pokazuje nową treść bez przebudowy.</span>
      <button type="button" class="fbtn" data-drukuj-konspekt>Drukuj konspekt (A4)</button>
      <button type="button" class="fbtn mocny" data-zamknij>Zamknij</button></div>
  </div>
</div>"""

SKRYPT = """
/* ——— zakładki wersji wiekowych ———
   Widoczna jest jedna wersja: nauczycielowi potrzebna jest zwykle jedna,
   a trzy naraz to dziewięć kartek poziomych zamiast trzech. */
document.querySelectorAll('.tab').forEach(t => t.addEventListener('click', () => {
  const w = t.dataset.wersja;
  document.querySelectorAll('.tab').forEach(x =>
    x.setAttribute('aria-selected', String(x.dataset.wersja === w)));
  document.querySelectorAll('.wersja').forEach(s => { s.hidden = s.dataset.wersja !== w; });
}));
document.querySelectorAll('.wersja').forEach((s, i) => { s.hidden = i !== 0; });

/* ——— konspekt otwierany z tabeli ———
   Cel edukacyjny czytamy NA ŻYWO z komórki tabeli, nigdy z kopii w konspekcie:
   po poprawce w `dane_zrodlowe.py` konspekt pokazuje nową treść bez przebudowy. */
function zTabeli(wersja, nr, poziom){
  const td = document.querySelector('#w-' + wersja + ' tr[data-wsk="' + CSS.escape(nr) +
    '"] td.g[data-lvl="' + poziom + '"]');
  if(!td) return {cel:'', ram:''};
  return {cel:(td.querySelector('.tresc')||{}).textContent||'',
          ram:(td.querySelector('.ram')||{}).textContent||''};
}
function otworz(idKon, poziom){
  const m = document.getElementById(idKon);
  if(!m) return;
  const wersja = m.dataset.wersja, nr = m.dataset.wsk;
  m.querySelectorAll('.kvar').forEach(v => {
    const lvl = v.dataset.lvl, t = zTabeli(wersja, nr, lvl);
    v.querySelector('.kon-cel').textContent = t.cel;
    v.querySelector('.kon-kryt').textContent = t.ram;
    v.classList.toggle('wyb', !!poziom && lvl === poziom);
  });
  m.querySelectorAll('.kmod').forEach(k => k.classList.toggle('wyb', k.dataset.mod === poziom));
  const poz = m.querySelector('.kon-poz');
  if(poz) poz.textContent = poziom ? ({p3:'Poziom III', p2:'Poziom II', p1:'Poziom I'})[poziom]
                                   : 'wszystkie trzy';
  m.classList.add('open');
  document.body.style.overflow = 'hidden';
  m.querySelector('.kclose').focus();
}
function zamknij(){
  document.querySelectorAll('.kmodal.open').forEach(m => m.classList.remove('open'));
  document.body.style.overflow = '';
}
document.addEventListener('click', ev => {
  const dodaj = ev.target.closest('.mkt-add');
  if(dodaj){ ev.stopPropagation(); formularz(kontekst(dodaj.closest('td.g'))); return; }
  const td = ev.target.closest('td.g');
  if(td){ otworz(td.dataset.kon, td.dataset.lvl); return; }
  const kb = ev.target.closest('.kbtn');
  if(kb){ kb.dataset.mks ? pokazWlasny(kb.dataset.mks) : otworz(kb.dataset.kon, null); return; }
  if(ev.target.closest('[data-zamknij]') || ev.target.classList.contains('kmodal')){ zamknij(); return; }
  const dk = ev.target.closest('[data-drukuj-konspekt]');
  if(dk){ drukujKonspekt(); return; }
  const zesz = ev.target.closest('[data-zeszyt]');
  if(zesz){ drukujZeszyt(zesz.dataset.zeszyt); return; }
  const moje = ev.target.closest('[data-moje]');
  if(moje){ rysujListe(moje.dataset.moje); return; }
  const play = ev.target.closest('.pom-play');
  if(play){ odtworz(play); return; }
});
document.addEventListener('keydown', ev => {
  if(ev.key === 'Escape') zamknij();
  if(ev.key === 'Enter' && ev.target.matches('td.g')) otworz(ev.target.dataset.kon, ev.target.dataset.lvl);
});

/* ——— druk ——— */
function drukujKonspekt(){
  document.documentElement.classList.add('druk-konspektu');
  window.print();
  setTimeout(() => document.documentElement.classList.remove('druk-konspektu'), 400);
}
function drukujZeszyt(wersja){
  const modale = [...document.querySelectorAll('.kmodal[data-wersja="' + wersja + '"]')];
  modale.forEach(m => {
    m.classList.add('open');
    m.querySelectorAll('.kvar').forEach(v => {
      const t = zTabeli(wersja, m.dataset.wsk, v.dataset.lvl);
      v.querySelector('.kon-cel').textContent = t.cel;
      v.querySelector('.kon-kryt').textContent = t.ram;
    });
  });
  document.documentElement.classList.add('druk-konspektu');
  window.print();
  setTimeout(() => { document.documentElement.classList.remove('druk-konspektu'); zamknij(); }, 400);
}

/* ——— nagranie polecenia ———
   Pliki audio to sklonowany głos autorki — dana biometryczna. Nie ma ich
   w repozytorium; odtwarza je `nagrania_glos.py --generuj` do 04_media/. */
function odtworz(btn){
  /* Ten plik może linkować nagranie z 04_media albo mieć je w sobie (build --z-glosem).
     Gdy dokument wyjechał bez katalogu mediów, nagranie się nie wczyta — komunikat ma
     mówić nauczycielce, co z tym zrobić, a nie którą komendę uruchomić. */
  const a = new Audio(btn.dataset.audio);
  a.play().catch(() => {
    btn.innerHTML = btn.dataset.audio.startsWith('data:')
      ? 'nagranie jest w pliku, ale przeglądarka go nie odtworzyła — kliknij jeszcze raz'
      : 'ten plik tylko linkuje nagrania — otwórz wersję <b>…_Z_GLOSEM.html</b>, która gra sama';
    btn.disabled = true;
  });
}

/* ——— własne konspekty nauczycielki ———
   Zapisywane w pamięci przeglądarki, w kształcie z `wlasne_konspekty_kontrakt.json`.
   Cel edukacyjny i tu czytany jest z tabeli — rekord go nie przechowuje. */
const KLUCZ = 'eduplaner2026.moje-konspekty-tom.v1';
const POZIOMY_JS = __POZIOMY__;
const KOMPONENTY_JS = __KOMPONENTY__;
const WERSJE_JS = __WERSJE__;
const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g,
  c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const linie = s => String(s || '').split('\\n').map(x => x.trim()).filter(Boolean);
let pamiec = null, edytowany = null;

function magazynDziala(){
  try { localStorage.setItem('__mkt__', '1'); localStorage.removeItem('__mkt__'); return true; }
  catch(e){ return false; }
}
const MAGAZYN = magazynDziala();
function wczytaj(){
  if(!MAGAZYN) return pamiec || (pamiec = []);
  try { const s = localStorage.getItem(KLUCZ); const t = s ? JSON.parse(s) : []; return Array.isArray(t) ? t : []; }
  catch(e){ return []; }
}
/* Zwraca 'ok', 'pamiec' (magazyn zablokowany) albo 'brak-miejsca' — komunikat
   „nie udało się zapisać" bez powodu nie mówi nauczycielce, co ma zrobić. */
function zapisz(lista){
  if(!MAGAZYN){ pamiec = lista; return 'pamiec'; }
  try { localStorage.setItem(KLUCZ, JSON.stringify(lista)); return 'ok'; }
  catch(e){ pamiec = lista; return (e && (e.name === 'QuotaExceededError' || e.code === 22))
    ? 'brak-miejsca' : 'blad'; }
}
function kontekst(td){
  const tr = td.closest('tr');
  return {wersja: td.dataset.wersja, nr: td.dataset.wsk, poziom: td.dataset.lvl,
          komponent: tr.dataset.komponent, krok: tr.dataset.krok,
          wskaznik: (tr.querySelector('td.wsk b') || {}).textContent || ''};
}
function modal(id, tresc){
  let m = document.getElementById(id);
  if(!m){ m = document.createElement('div'); m.className = 'kmodal'; m.id = id; document.body.appendChild(m); }
  m.innerHTML = '<div class="kcard">' + tresc + '</div>';
  m.classList.add('open');
  document.body.style.overflow = 'hidden';
  return m;
}
function formularz(k, rekord){
  edytowany = rekord || null;
  const r = rekord || {};
  const poz = POZIOMY_JS[k.poziom] || POZIOMY_JS.p2;
  const t = zTabeli(k.wersja, k.nr, k.poziom);
  const pola = (nazwa, etykieta, wartosc, wiersze) => wiersze
    ? '<label>' + etykieta + '<textarea name="' + nazwa + '">' + esc(wartosc || '') + '</textarea></label>'
    : '<label>' + etykieta + '<input name="' + nazwa + '" value="' + esc(wartosc || '') + '"></label>';
  const m = modal('mkt-form', `
    <button class="kclose" data-zamknij aria-label="Zamknij">✕</button>
    <div class="khead"><span class="mark" role="img" aria-label="Logo PCTP"></span>
      <div><div class="kw">EduPlaner 2026</div>
        <div class="ks">Mój konspekt · komponent ${esc(k.komponent)} · ${esc(KOMPONENTY_JS[k.komponent] || '')}
          · wersja ${esc(k.wersja)} · ${esc(WERSJE_JS[k.wersja] || '')} · wskaźnik ${esc(k.nr)}</div></div>
      <span class="kpill">${rekord ? 'Edycja' : 'Nowy konspekt'}</span></div>
    <div class="kkrok"><b>Cel z tabeli (${esc(poz.nazwa)}):</b> ${esc(t.cel)}
      <span>${esc(t.ram)} · krok mentalizacji: ${esc(k.krok)}</span></div>
    <form class="formularz" id="mkt-formularz">
      ${pola('tytul', 'Temat zajęć', r.tytul)}
      ${pola('podtytul', 'Podtytuł', r.podtytul)}
      <div class="ftrzy">${pola('czas', 'Czas', r.czas || WERSJE_JS[k.wersja + '_czas'])}
        ${pola('forma', 'Forma', r.forma || WERSJE_JS[k.wersja + '_forma'])}
        ${pola('cykl', 'Cykl', r.cykl || WERSJE_JS[k.wersja + '_cykl'])}</div>
      ${pola('ter', 'Cel terapeutyczny', r.ter, true)}
      ${pola('kryt', 'Kryterium obserwacji', r.kryt)}
      <div class="fdwie">${pola('pomoce', 'Pomoce (jedna w wierszu)', (r.pomoce || []).join('\\n'), true)}
        ${pola('metody', 'Metody (jedna w wierszu)', (r.metody || []).join('\\n'), true)}</div>
      ${pola('rodzaj', 'Rodzaj zajęć', r.rodzaj)}
      ${pola('przebieg', 'Przebieg — wiersz: czynność nauczyciela | reakcja dziecka',
        (r.przebieg || []).map(p => p.join(' | ')).join('\\n'), true)}
      <div class="ftrzy">${pola('m3', 'Modyfikacja · Poziom III', (r.mody && r.mody.p3 || []).join('\\n'), true)}
        ${pola('m2', 'Modyfikacja · Poziom II', (r.mody && r.mody.p2 || []).join('\\n'), true)}
        ${pola('m1', 'Modyfikacja · Poziom I', (r.mody && r.mody.p1 || []).join('\\n'), true)}</div>
      ${pola('wskazowka', 'Wskazówka dla prowadzącego', r.wskazowka, true)}
      <div class="fprzyciski">
        <span class="komunikat">${MAGAZYN ? 'Zapis w pamięci tej przeglądarki.'
          : 'Magazyn przeglądarki jest zablokowany — konspekt zniknie po zamknięciu karty.'}</span>
        ${rekord ? '<button type="button" class="fbtn usun" id="mkt-usun">Usuń</button>' : ''}
        <button type="button" class="fbtn" data-zamknij>Anuluj</button>
        <button type="submit" class="fbtn mocny">Zapisz konspekt</button></div>
    </form>`);
  m.querySelector('#mkt-formularz').addEventListener('submit', ev => {
    ev.preventDefault();
    const f = new FormData(ev.target), g = n => (f.get(n) || '').trim();
    if(!g('tytul')){ alert('Temat zajęć jest potrzebny — po nim odnajdziesz konspekt w wykazie.'); return; }
    const lista = wczytaj();
    const rek = {
      id: (edytowany && edytowany.id) || 'mkt' + Date.now().toString(36),
      nr: k.nr, wersja: k.wersja, poziom: k.poziom, komponent: k.komponent, krok: k.krok,
      tytul: g('tytul'), podtytul: g('podtytul'), czas: g('czas'), forma: g('forma'), cykl: g('cykl'),
      ter: g('ter'), kryt: g('kryt'), pomoce: linie(g('pomoce')), metody: linie(g('metody')),
      rodzaj: g('rodzaj'),
      przebieg: linie(g('przebieg')).map(w => { const c = w.split('|'); return [(c[0]||'').trim(), (c[1]||'').trim()]; }),
      mody: {p3: linie(g('m3')), p2: linie(g('m2')), p1: linie(g('m1'))},
      wskazowka: g('wskazowka'), data: new Date().toISOString().slice(0, 10)
    };
    const i = lista.findIndex(x => x.id === rek.id);
    if(i >= 0) lista[i] = rek; else lista.push(rek);
    const stan = zapisz(lista);
    if(stan === 'brak-miejsca'){
      alert('W pamięci przeglądarki nie ma już miejsca. Usuń starsze własne konspekty, żeby zapisać ten.');
      return;
    }
    zamknij(); rysujListe(k.wersja); pokazWlasny(rek.id);
  });
  const usun = m.querySelector('#mkt-usun');
  if(usun) usun.addEventListener('click', () => {
    if(!confirm('Usunąć ten konspekt na stałe?')) return;
    zapisz(wczytaj().filter(x => x.id !== edytowany.id));
    zamknij(); rysujListe(k.wersja);
  });
}
function pokazWlasny(id){
  const r = wczytaj().find(x => x.id === id);
  if(!r) return;
  const t = zTabeli(r.wersja, r.nr, r.poziom), poz = POZIOMY_JS[r.poziom] || POZIOMY_JS.p2;
  const li = a => (a && a.length ? a : ['— nie wypełniono']).map(x => '<li>' + esc(x) + '</li>').join('');
  const prz = (r.przebieg || []).map((p, i) => '<tr><td class="lp">' + (i + 1) + '</td><td>' +
    esc(p[0]) + '</td><td>' + esc(p[1]) + '</td></tr>').join('');
  const mod = k => '<div class="kmod m' + (k === 'p3' ? 3 : k === 'p2' ? 2 : 1) +
    (r.poziom === k ? ' wyb' : '') + '"><b>' + esc(POZIOMY_JS[k].nazwa) + '</b><ul class="klista">' +
    li(r.mody && r.mody[k]) + '</ul></div>';
  modal('mkt-widok', `
    <button class="kclose" data-zamknij aria-label="Zamknij">✕</button>
    <div class="khead"><span class="mark" role="img" aria-label="Logo PCTP"></span>
      <div><div class="kw">EduPlaner 2026</div>
        <div class="ks">Konspekt własny · komponent ${esc(r.komponent)} · ${esc(KOMPONENTY_JS[r.komponent] || '')}
          · wersja ${esc(r.wersja)} · ${esc(WERSJE_JS[r.wersja] || '')} · wskaźnik ${esc(r.nr)}</div></div>
      <span class="kpill">Mój konspekt</span></div>
    <div class="kmeta" style="grid-template-columns:1.6fr 1fr 1fr">
      <div class="field"><b>Dotyczy dziecka</b><span class="dots"></span></div>
      <div class="field"><b>Grupa</b><span class="dots"></span></div>
      <div class="field"><b>Data</b><span class="dots"></span></div></div>
    <div class="ktitle"><span class="kp">Konspekt zajęć · druk KC-3 · opracowanie własne</span>
      <div class="ksfera">Wskaźnik ${esc(r.nr)} · krok mentalizacji: ${esc(r.krok)}</div>
      <h3>${esc(r.tytul)}</h3><div class="kpod">${esc(r.podtytul)}</div></div>
    <div class="kmeta">
      <div class="field"><b>Czas</b>${esc(r.czas || '—')}</div>
      <div class="field"><b>Forma</b>${esc(r.forma || '—')}</div>
      <div class="field"><b>Cykl</b>${esc(r.cykl || '—')}</div>
      <div class="field"><b>Poziom wsparcia</b>${esc(poz.nazwa)}</div></div>
    <div class="ksec"><span class="sq">I</span><h4>Cel SMART</h4><span class="line"></span></div>
    <div class="kcele">
      <div class="kcel edu"><div class="kchead">Cel edukacyjny — z tabeli TOM-T · ${esc(poz.nazwa)}</div>
        <div class="kvar wyb"><div class="ktresc">${esc(t.cel)}</div>
          <div class="kkryt"><b>Kryterium:</b> ${esc(t.ram)}</div></div></div>
      <div class="kcel ter"><div class="kchead">Cel terapeutyczny</div>
        <div class="ktresc">${esc(r.ter || '—')}</div>
        <div class="kkryt"><b>Kryterium:</b> ${esc(r.kryt || '—')}</div></div></div>
    <div class="kdwie">
      <div><div class="ksec"><span class="sq">II</span><h4>Pomoce dydaktyczne</h4><span class="line"></span></div>
        <ul class="klista">${li(r.pomoce)}</ul></div>
      <div><div class="ksec"><span class="sq">III</span><h4>Metody i formy działań</h4><span class="line"></span></div>
        <ul class="klista">${li(r.metody)}</ul></div></div>
    <div class="kdwie" style="align-items:end">
      <div><div class="ksec"><span class="sq">IV</span><h4>Sposób realizacji</h4><span class="line"></span></div>
        <div class="krodzaj" style="font-style:italic">Tabela poniżej ↓</div></div>
      <div><div class="ksec"><span class="sq">V</span><h4>Rodzaj zajęć</h4><span class="line"></span></div>
        <div class="krodzaj">${esc(r.rodzaj || '—')}</div></div></div>
    <table class="ktab">
      <thead><tr><th style="width:26px">Lp.</th><th style="width:47%">Czynności nauczyciela (N)</th>
        <th>Oczekiwane reakcje i umiejętności dziecka (D)</th></tr></thead>
      <tbody>${prz || '<tr><td class="lp">1</td><td>—</td><td>—</td></tr>'}</tbody></table>
    <div class="ksec"><span class="sq">VI</span><h4>Modyfikacja według poziomu wsparcia</h4>
      <span class="line"></span></div>
    <div class="kmods">${mod('p3')}${mod('p2')}${mod('p1')}</div>
    <div class="kwsk"><b>Wskazówka dla prowadzącego:</b> ${esc(r.wskazowka || '—')}</div>
    <div class="fprzyciski">
      <span class="komunikat">Zapisano ${esc(r.data)} · w pamięci tej przeglądarki</span>
      <button type="button" class="fbtn" id="mkt-edytuj">Edytuj</button>
      <button type="button" class="fbtn" data-drukuj-konspekt>Drukuj konspekt (A4)</button>
      <button type="button" class="fbtn mocny" data-zamknij>Zamknij</button></div>`);
  document.getElementById('mkt-edytuj').addEventListener('click', () => {
    zamknij();
    formularz({wersja: r.wersja, nr: r.nr, poziom: r.poziom, komponent: r.komponent,
               krok: r.krok, wskaznik: ''}, r);
  });
}
function rysujListe(wersja){
  const cel = document.querySelector('[data-mkt-lista="' + wersja + '"]');
  if(!cel) return;
  const moje = wczytaj().filter(r => r.wersja === wersja);
  if(!moje.length){ cel.innerHTML = ''; return; }
  cel.innerHTML = '<h4>Moje konspekty · ' + moje.length + '</h4><div class="ksiatka">' +
    moje.map(r => '<button type="button" class="kbtn" data-mkt="' + r.id + '">' +
      '<span class="knr">' + esc(r.nr) + '</span><b>' + esc(r.tytul) + '</b>' +
      '<span class="kzast">' + esc(POZIOMY_JS[r.poziom].nazwa) + ' · ' + esc(r.data) + '</span></button>').join('') +
    '</div>';
}
['A', 'B', 'C'].forEach(rysujListe);
"""


def main() -> int:
    cele = wczytaj("cele_tom_poziomy.json")
    konspekty = wczytaj("konspekty_tom.json")
    pomoce = wczytaj("pomoce_tom.json")
    materialy = wczytaj("materialy_do_druku.json")

    poziomy, wersje, komponenty = cele["poziomy_wsparcia"], cele["wersje_wiekowe"], cele["komponenty"]
    konspekty_wg = {(k["wskaznik"], k["wersja_wiekowa"]): k for k in konspekty["konspekty"]}
    pomoc_wg = {p["wskaznik"]: p for p in pomoce["pomoce"]}
    arkusz_wg = {a["wskaznik"]: a for a in materialy["arkusze"]}
    wskaznik_wg = {w["nr"]: w for z in komponenty for w in z["wskazniki"]}

    sekcje = "".join(tabela_wersji(w["klucz"], w["wiek"], komponenty, poziomy, konspekty_wg) for w in wersje)
    modale = "".join(
        modal_konspektu(k, pomoc_wg[k["wskaznik"]], arkusz_wg[k["wskaznik"]],
                        wskaznik_wg[k["wskaznik"]], poziomy)
        for k in konspekty["konspekty"])

    skrypt = (SKRYPT
              .replace("__POZIOMY__", json.dumps({p["klucz"]: {"nazwa": p["nazwa"], "rzym": p["rzym"],
                                                               "kryt": p["kryterium"],
                                                               "hor": p["horyzont"]} for p in poziomy},
                                                 ensure_ascii=False))
              .replace("__KOMPONENTY__", json.dumps({z["nr"]: z["nazwa"] for z in komponenty}, ensure_ascii=False))
              .replace("__WERSJE__", json.dumps(
                  {**{w["klucz"]: w["wiek"] for w in wersje},
                   **{w["klucz"] + "_czas": w["czas"] for w in wersje},
                   **{w["klucz"] + "_forma": w["forma"] for w in wersje},
                   **{w["klucz"] + "_cykl": w["cykl"] for w in wersje}}, ensure_ascii=False)))

    doc = f"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tabela celów SMART · teoria umysłu (przedszkole) — EduPlaner 2026 · PCTP</title>
<style>{STYL}
{styl_zdjec(pomoce["pomoce"])}
{styl_obrazkow(pomoce["pomoce"], materialy["arkusze"])}</style>
</head>
<body>
<div class="ark">
{naglowek(cele['liczba_celow'])}
{zakladki(wersje)}
{legenda(poziomy)}
{uwaga(cele['modul']['zasada_modulu'])}
{sekcje}
  <div class="stopka">
    <span>EduPlaner 2026 · PCTP · pedagog specjalny <b>mgr Mirosława Ewa Jurczyszyn</b></span>
    <span>druk TOM-T · tabela drukuje się poziomo · {cele['liczba_celow']} celów ·
      {konspekty['liczba']} konspektów</span>
  </div>
</div>
{modale}
<script>{skrypt}</script>
</body>
</html>
"""
    wyjscie = pathlib.Path(globals().get("CEL", WYJSCIE))
    wyjscie.parent.mkdir(parents=True, exist_ok=True)
    wyjscie.write_text(doc, encoding="utf-8")
    print(f"zapisano {sciezka_w_opisie(wyjscie)} ({wyjscie.stat().st_size // 1024} KB · "
          f"{cele['liczba_celow']} celów · {konspekty['liczba']} konspektów)")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Tabela celów TOM z konspektami")
    ap.add_argument("--wyjscie", default=str(WYJSCIE), help="plik docelowy")
    ap.add_argument("--z-glosem", action="store_true", dest="z_glosem",
                    help="wklej nagrania w dokument (dana biometryczna — plik tylko do "
                         "użytku własnego autorki, nie do repozytorium)")
    args = ap.parse_args()
    # Wersja z głosem MUSI iść poza 02_gotowe_dokumenty: ten katalog jest w
    # repozytorium, a nagranie to sklonowany głos autorki. Zamiast liczyć na
    # pamięć wywołującego, pilnuje tego program.
    if args.z_glosem and pathlib.Path(args.wyjscie).resolve() == WYJSCIE.resolve():
        raise SystemExit("--z-glosem wymaga --wyjscie poza 02_gotowe_dokumenty: "
                         "ten katalog trafia do repozytorium, a nagrania to dane biometryczne.")
    globals()["WKLEJ_GLOS"] = args.z_glosem
    globals()["CEL"] = args.wyjscie
    raise SystemExit(main())
