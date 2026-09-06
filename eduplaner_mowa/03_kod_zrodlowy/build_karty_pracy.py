#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Karty pracy — arkusze A4 do wycięcia, po jednym na wskaźnik.

    python3 03_kod_zrodlowy/build_karty_pracy.py

Każda strona to jeden arkusz z `materialy_do_druku.json`: cztery karty
w prawdziwym rozmiarze 9 × 9 cm z liniami cięcia, pasek kolejności i — dla
nauczyciela — polecenia dla dziecka w trzech wersjach wiekowych.

Etykiety na kartach widzi DZIECKO, więc są krótkie i duże. Opisy pól i wstęp
czyta DOROSŁY i stoją poza obszarem cięcia. Puste pole symbolu zostaje puste
celowo: wkleja się w nie symbol z biblioteki banku KPOF — ten sam, którego
dziecko używa na tablicy AAC i w planie dnia.
"""
from __future__ import annotations

import argparse
import base64
import html
import json
import pathlib
import re

KORZEN = pathlib.Path(__file__).resolve().parent.parent
DANE = KORZEN / "01_dane_json"
MEDIA = KORZEN / "04_media"
WSPOLNE = KORZEN.parent / "media_wspolne"   # biblioteka symboli, jedna dla wszystkich modułów
WYJSCIE = KORZEN / "02_gotowe_dokumenty" / "Karty_pracy_MOWA.html"
MODUL = {"kod": "MOWA", "nazwa": "Rozwój mowy i komunikacja", "plik_celow": "cele_mowa_poziomy.json",
         "plik_pomocy": "pomoce_mowa.json", "grupa": "obszary"}


def sciezka_w_opisie(p: pathlib.Path) -> str:
    """Skrót ścieżki w komunikacie — względem modułu, gdy plik w nim leży."""
    try:
        return str(p.relative_to(KORZEN))
    except ValueError:
        return str(p)


def bez_numeru(etykieta: str) -> str:
    """Etykieta bez wiodącego „1 · ”, gdy autorka wpisała numer w treść.

    Dopasowanie jest zakotwiczone na cyfrze z przodu, bo w środku etykiety
    kropka środkowa bywa częścią tekstu i nie wolno po niej ciąć.
    """
    return re.sub(r"^\s*\d+\s*·\s*", "", str(etykieta))


def logo_pctp() -> str:
    """Znak PCTP wklejony w dokument jako data: URI.

    W nagłówku stał do tej pory fioletowy krążek z napisem „PCTP” zrobiony
    w CSS. To był znacznik zastępczy, nie logo — materiał firmowany jej
    nazwiskiem ma nosić ten sam znak, co reszta ekosystemu EduPlaner.
    Plik leży raz, w media_wspolne/, i idzie do środka dokumentu, żeby
    ten działał z dysku, bez internetu.
    """
    p = KORZEN.parent / "media_wspolne" / "logo_pctp.png"
    if not p.exists():
        return ""
    return "data:image/png;base64," + base64.b64encode(p.read_bytes()).decode()


def e(t) -> str:
    return html.escape(str(t if t is not None else ""))


def wczytaj(nazwa: str) -> dict:
    p = DANE / nazwa
    if not p.exists():
        raise SystemExit(f"Brak {p}. Uruchom najpierw: python3 03_kod_zrodlowy/eksport_json.py")
    return json.loads(p.read_text(encoding="utf-8"))


def obraz_base64(sciezka_wzgledna: str) -> str | None:
    """Zdjęcia i symbole wklejamy do dokumentu, żeby otwierał się z dysku bez
    katalogu mediów. Gdy pliku nie ma, zostaje pole opisane nazwą."""
    if not sciezka_wzgledna:
        return None
    p = MEDIA / sciezka_wzgledna
    if not p.exists():
        p = WSPOLNE / sciezka_wzgledna
    if not p.exists():
        return None
    typ = "jpeg" if p.suffix.lower() in (".jpg", ".jpeg") else p.suffix.lstrip(".")
    return f"data:image/{typ};base64," + base64.b64encode(p.read_bytes()).decode("ascii")


STYL = """
:root{--fiolet:#2D1B69;--fiolet-2:#5a4a94;--fiolet-tlo:#efeaf9;--fiolet-linia:#d9d0f0;
  --pomarancz:#E8450A;--pomarancz-tlo:#fdece4;--pomarancz-linia:#f3cdbd;
  --ink:#2b2733;--szary:#6f6a7d;--linia:#e4e1ec;--zebra:#faf7f2}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{background:#e9e7ef;color:var(--ink);font-family:'Mulish','Segoe UI',Candara,Arial,sans-serif}
.strona{width:210mm;min-height:297mm;margin:12px auto;background:#fff;padding:10mm 12mm 8mm;
  box-shadow:0 6px 30px rgba(45,27,105,.16);display:flex;flex-direction:column}
.head{display:flex;align-items:center;gap:12px}
.mark{width:36px;height:36px;border-radius:50%;background:var(--fiolet);border:2px solid #cfc4ea;color:#fff;
  display:flex;align-items:center;justify-content:center;font-size:8px;font-weight:800;flex:0 0 auto}
/* Znak wchodzi jako tło kółka; gdy pliku nie ma, zostaje sam fiolet
   i dokument nadal się składa — brak nie ma wysypywać budowania. */
.mark{background:center/cover no-repeat var(--fiolet);background-image:var(--logo)}
.mark::after{content:""}
.head h1{font-size:15px;margin:0;color:var(--fiolet)}
.head .sub{font-size:8px;color:var(--szary);letter-spacing:.6px;text-transform:uppercase;font-weight:700;margin-top:2px}
.head .prawa{margin-left:auto;text-align:right}
.head .prawa b{display:inline-block;background:var(--pomarancz);color:#fff;font-size:10px;padding:4px 12px;border-radius:20px}
.head .prawa span{display:block;font-size:7.5px;color:var(--szary);letter-spacing:.9px;margin-top:3px;text-transform:uppercase}
.kreska{height:3px;border-radius:3px;margin:8px 0 10px;
  background:linear-gradient(90deg,var(--fiolet) 0%,var(--fiolet) 55%,var(--pomarancz) 55%,var(--pomarancz) 100%)}
.tyt{display:flex;align-items:flex-start;gap:10px;margin-bottom:6px}
.tyt .nr{background:var(--fiolet);color:#fff;font-size:11px;font-weight:800;padding:3px 10px;border-radius:12px;flex:0 0 auto}
.tyt h2{margin:0;font-size:15px;color:var(--fiolet)}
.tyt .kon{font-size:9px;color:var(--szary);margin-top:2px}
/* Zdjęcie gotowej pomocy szło wcześniej w kolumnie 62 mm i było przycinane
   (object-fit:cover), więc na wydruku nie dało się rozpoznać, co na nim leży.
   Teraz zajmuje pełną szerokość kolumny tekstu i pokazuje się w całości. */
.foto{margin:0 0 6px;border:1px solid var(--fiolet-linia);border-radius:8px;overflow:hidden;
  background:#fbfaff;break-inside:avoid}
.foto img{display:block;width:100%;height:auto;object-fit:contain}
.foto figcaption{padding:5px 9px;font-size:8.5px;line-height:1.45;color:var(--szary)}
.foto figcaption b{display:block;color:var(--fiolet);font-size:9.5px;margin-bottom:1px}
.foto.pusta{border-style:dashed;padding:10mm;font-size:9px;color:var(--szary);text-align:center;line-height:1.5}
/* Dwie kolumny: po lewej co przygotować, po prawej jak użyć i co znaczy która karta.
   Wcześniej wszystko szło jedną kolumną przez całą szerokość i dolna połowa
   kartki zostawała pusta, a zdjęcie musiało być małe, żeby się obok zmieściło. */
.dwie{display:grid;grid-template-columns:1fr 1fr;gap:6mm;align-items:start}
.dwie > div{min-width:0}
.wstep{background:var(--zebra);border-radius:8px;padding:8px 11px;font-size:9.5px;line-height:1.55}
.wstep b{color:var(--fiolet)}
.wstep h5{margin:7px 0 3px;font-size:8px;letter-spacing:.6px;text-transform:uppercase;color:var(--fiolet)}
.wstep ul{margin:0;padding-left:15px;font-size:9px;line-height:1.5}
.blk{display:flex;align-items:center;gap:7px;font-size:9px;font-weight:800;letter-spacing:.6px;
  color:var(--fiolet);text-transform:uppercase;margin:10px 0 6px}
.blk::before{content:"";width:9px;height:9px;border-radius:2px;background:var(--pomarancz)}
.blk .info{margin-left:auto;font-weight:600;letter-spacing:0;text-transform:none;color:var(--szary);font-size:8.5px}
.karty{display:grid;grid-template-columns:repeat(2,90mm);gap:6mm;justify-content:center}
.karta{width:90mm;height:90mm;border:1.5px dashed var(--fiolet-linia);border-radius:4mm;padding:5mm;
  display:flex;flex-direction:column;align-items:center;justify-content:space-between;text-align:center;
  break-inside:avoid;position:relative;background:#fff}
.karta .pole{width:100%;flex:1;border:1px solid var(--linia);border-radius:3mm;background:#fff;
  display:flex;align-items:center;justify-content:center;overflow:hidden;margin-bottom:4mm}
.karta .pole img{max-width:100%;max-height:100%;object-fit:contain}
.karta .pole .puste{font-size:8px;color:var(--szary);line-height:1.5;padding:6mm}
.karta .pole .puste b{display:block;color:var(--fiolet);font-size:8.5px;margin-bottom:2px}
.karta .et{font-size:17px;font-weight:800;color:var(--fiolet);letter-spacing:.2px;line-height:1.2}
.karta .rog{position:absolute;top:2mm;right:3mm;font-size:7px;color:var(--szary);letter-spacing:.5px}
.pasek{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;margin-top:4mm}
.pole-k{border:1.5px dashed var(--fiolet-linia);border-radius:3mm;padding:4mm 3mm;text-align:center;
  background:var(--fiolet-tlo);break-inside:avoid}
.pole-k .num{font-size:8px;font-weight:800;color:var(--pomarancz);letter-spacing:.6px}
.pole-k .et{font-size:12px;font-weight:800;color:var(--fiolet);margin-top:2px}
.pole-k .sym{font-size:7px;color:var(--szary);margin-top:3px}
.legenda{margin-top:8px;border-top:1px solid var(--linia);padding-top:7px}
.legenda h4{margin:0 0 4px;font-size:8.5px;letter-spacing:.6px;text-transform:uppercase;color:var(--fiolet)}
.legenda ul{margin:0;padding-left:15px;font-size:8.5px;line-height:1.5;color:var(--szary)}
.legenda b{color:var(--ink)}
.polecenia{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin-top:8px}
.pol{background:var(--pomarancz-tlo);border:1px solid var(--pomarancz-linia);border-radius:7px;padding:6px 9px;
  font-size:9px;line-height:1.45}
.pol .wiek{display:block;font-size:7.5px;font-weight:800;letter-spacing:.6px;text-transform:uppercase;
  color:var(--pomarancz);margin-bottom:2px}
.pol .audio{display:block;font-family:ui-monospace,Consolas,monospace;font-size:7px;color:var(--szary);margin-top:3px}
.graj{display:block;margin-top:4px;border:1px solid var(--pomarancz-linia);background:#fff;color:var(--pomarancz);
  border-radius:999px;padding:3px 9px;font:700 8px/1 inherit;cursor:pointer}
/* ——— strona instrukcji ———
   Wszystko, czego nie tnie się nożyczkami: zdjęcie gotowej pomocy, trzy kroki,
   znaczenie kart i teksty poleceń. Osobna kartka, bo razem z arkuszem do cięcia
   treść urastała do 370 mm i drukarka dzieliła ją w przypadkowym miejscu. */
.kroki{margin:2mm 0 0;padding-left:6mm;font-size:10px;line-height:1.6;color:var(--ink)}
.kroki li{margin-bottom:1mm}
.opisy{margin:2mm 0 0;padding-left:5mm;font-size:9.5px;line-height:1.6;color:var(--szary)}
.opisy b{color:var(--fiolet)}
.wskaz{margin-top:3mm;border-left:3px solid var(--fiolet);background:var(--fiolet-tlo);
  border-radius:0 2mm 2mm 0;padding:3mm 4mm;font-size:9.5px;line-height:1.55;color:var(--ink)}
.pole-k img{width:100%;height:26mm;object-fit:contain;background:#fff;margin:1.5mm 0}

/* ——— arkusz historyjki obrazkowej ———
   Osobna strona A4, bo pola tnie sie i uklada na stole, a karty z poprzedniej
   strony zostaja na tablicy. Drabina idzie od dolu do gory: najnizszy szczebel
   jest najlatwiejszy, wiec dziecko wchodzi na karte od dolu. */
.hpola{display:grid;grid-template-columns:repeat(auto-fill,minmax(46mm,1fr));
  gap:5mm;margin-top:3mm}
.hkafel{border:1.5px dashed var(--fiolet-linia);border-radius:3mm;
  padding:3mm;background:#fff;display:flex;flex-direction:column;gap:2mm;break-inside:avoid}
.hkafel img{width:100%;aspect-ratio:4/3;object-fit:contain;background:#fff}
.hkafel .hp{font-size:13px;font-weight:800;color:var(--fiolet);line-height:1.2}
.hkafel .hnr{display:inline-block;min-width:5mm;height:5mm;line-height:5mm;text-align:center;
  border-radius:50%;background:var(--fiolet);color:#fff;font-size:9px;font-weight:800;margin-right:1.5mm}
.hkafel .hq{font-size:9px;color:var(--szary);font-style:italic;line-height:1.4}
.drabina .hpola{display:flex;flex-direction:column-reverse;gap:3mm}
.drabina .hkafel{flex-direction:row;align-items:center;gap:4mm}
.drabina .hkafel img{width:38mm;flex:none}
.hpo{border:1px solid var(--linia);border-radius:2mm;background:var(--fiolet-tlo);padding:3mm;
  font-size:10px;line-height:1.55;margin-top:2mm}
.hpo b{color:var(--fiolet)}
.hwiersz{border-top:1px dashed var(--linia);padding-top:3mm;margin-top:3mm}
.hwiersz:first-of-type{border-top:none;margin-top:0;padding-top:0}
.hwiersz>.hnazwa{font-size:9px;letter-spacing:.6px;text-transform:uppercase;color:var(--szary)}
.stopka{margin-top:auto;padding-top:7px;border-top:1px solid var(--linia);display:flex;
  justify-content:space-between;font-size:8px;color:var(--szary);gap:10px}
@media print{
  *{-webkit-print-color-adjust:exact;print-color-adjust:exact}
  body{background:#fff}
  .strona{box-shadow:none;margin:0;page-break-after:always}
  @page{size:A4 portrait;margin:0}
  .karta,.pole-k,.foto,.hkafel,.hwiersz{break-inside:avoid}
  .graj{display:none !important}
}
"""


def karta(k: dict) -> str:
    obraz = obraz_base64(k.get("plik_symbolu"))
    if obraz:
        pole = f'<div class="pole"><img src="{obraz}" alt=""></div>'
    elif k.get("plik_symbolu"):
        nazwa = k["plik_symbolu"].rsplit("/", 1)[-1]
        pole = (f'<div class="pole"><span class="puste"><b>miejsce na symbol</b>{e(nazwa)}<br>'
                f'z biblioteki banku KPOF</span></div>')
    else:
        pole = ('<div class="pole"><span class="puste"><b>pole celowo puste</b>'
                'wklej symbol, którego dziecko używa<br>na tablicy AAC i w planie dnia</span></div>')
    return (f'<div class="karta"><span class="rog">wytnij wzdłuż linii</span>{pole}'
            f'<div class="et">{e(k["etykieta_dla_dziecka"])}</div></div>')


WKLEJ_GLOS = False   # ustawiane przez --z-glosem


def zrodlo_audio(sciezka_wzgledna: str) -> str | None:
    """Nagranie polecenia, wklejone w dokument. Karty pracy drukuje się na papierze,
    ale ten sam plik otwiera się też na tablicy w sali — wtedy przycisk odtwarza
    polecenie głosem autorki, bez katalogu mediów obok."""
    plik = MEDIA / sciezka_wzgledna
    if not WKLEJ_GLOS or not plik.exists():
        return None
    return "data:audio/mpeg;base64," + base64.b64encode(plik.read_bytes()).decode("ascii")


SKRYPT = """
// Jeden odtwarzacz na cały dokument: kliknięcie w inny przycisk przerywa poprzednie
// polecenie, żeby dwa głosy nigdy nie nachodziły na siebie w sali.
(function(){
  var gra = null;
  document.addEventListener('click', function(ev){
    var b = ev.target.closest('.graj'); if(!b) return;
    if(gra){ gra.pause(); gra = null; }
    gra = new Audio(b.dataset.audio); gra.play();
  });
})();
"""


def foto_pomocy(pomoc: dict) -> str:
    """Zdjęcie gotowej pomocy — nauczycielka widzi na jednej stronie i karty do
    wycięcia, i to, jak całość ma wyglądać w sali. Plik jest wklejony w dokument,
    więc drukuje się razem z kartami."""
    obraz = obraz_base64(pomoc.get("zdjecie"))
    if not obraz:
        return (f'<figure class="foto pusta">zdjęcie pomocy<br>'
                f'{e(pomoc.get("zdjecie") or "—")}</figure>')
    return (f'<figure class="foto"><img src="{obraz}" alt="{e(pomoc["opis_zdjecia"])}">'
            f'<figcaption><b>Tak wygląda gotowa pomoc</b>{e(pomoc["opis_zdjecia"])}</figcaption></figure>')


def naglowek(podtytul: str, arkusz: dict, pomoc: dict, konspekt_tytul: str,
             tytul: str, dopisek: str = "") -> str:
    """Wspólna głowa każdej strony A4 — ta sama marka, ten sam numer wskaźnika."""
    return f"""<div class="head"><span class="mark" role="img" aria-label="Logo PCTP"></span>
  <div><h1>EduPlaner 2026</h1><div class="sub">{e(MODUL['nazwa'])} · {podtytul}</div></div>
  <div class="prawa"><b>{e(MODUL['kod'])} · KC-4</b><span>arkusz A4{dopisek}</span></div></div>
<div class="kreska"></div>
<div class="tyt"><span class="nr">{e(arkusz['wskaznik'])}</span>
  <div><h2>{tytul}</h2>
    <div class="kon">do konspektu „{e(konspekt_tytul)}” · pomoc: {e(pomoc['nazwa'])}</div></div></div>"""


def stopka(arkusz: dict, nr_strony: int, ile: int) -> str:
    return (f'<div class="stopka"><span>EduPlaner 2026 · PCTP · pedagog specjalny '
            f'<b>mgr Mirosława Ewa Jurczyszyn</b></span>'
            f'<span>Karta pracy {nr_strony} z {ile} · wskaźnik {e(arkusz["wskaznik"])}</span></div>')


def strona_instrukcji(arkusz: dict, pomoc: dict, konspekt_tytul: str,
                      nr_strony: int, ile: int) -> str:
    """Strona dla dorosłego: zdjęcie gotowej pomocy, co przygotować, co znaczy która
    karta i teksty poleceń. Nie idzie pod nożyczki, więc zostaje w całości —
    wcześniej dzieliła kartkę z arkuszem do cięcia i obie rzeczy się nie mieściły."""
    opisy = "".join(f'<li><b>{e(k["etykieta_dla_dziecka"])}</b> — {e(k["opis_dla_doroslego"])}</li>'
                    for k in arkusz["karty"])

    def polecenie(w, p) -> str:
        # Przycisk służy do klikania na tablicy w sali; na papierze nie ma czego kliknąć,
        # więc znika w druku, a nazwa nagrania zostaje — i mówi, którego pliku szukać.
        # Wcześniej stało tu „brak nagrania”, co na wydruku było po prostu nieprawdą:
        # nagranie istnieje, tylko nie jest wklejone w tę wersję dokumentu.
        dane = zrodlo_audio(p["nagranie"])
        przycisk = (f'<button type="button" class="graj" data-audio="{dane}">▶ głos autorki</button>'
                    if dane else "")
        return (f'<div class="pol"><span class="wiek">Wersja {w} · {e(p["wiek"])}</span>'
                f'„{e(p["polecenie_dla_dziecka"])}”{przycisk}'
                f'<span class="audio">nagranie: {e(p["nagranie"].rsplit("/", 1)[-1])}</span></div>')

    polecenia = "".join(polecenie(w, p) for w, p in pomoc["polecenia"].items())
    return f"""<section class="strona instrukcja">
{naglowek("instrukcja do kart pracy", arkusz, pomoc, konspekt_tytul,
          e(arkusz['tytul']), " · dla dorosłego")}
{foto_pomocy(pomoc)}
<div class="dwie">
  <div>
    <div class="blk">Co przygotować</div>
    <div class="wstep"><b>Dla dorosłego.</b> {e(arkusz['wstep_dla_doroslego'])}
      <ul>{''.join(f'<li>{e(x)}</li>' for x in pomoc['co_przygotowac'])}</ul></div>
  </div>
  <div>
    <div class="blk">Jak użyć — trzy kroki</div>
    <ol class="kroki">{''.join(f'<li>{e(x)}</li>' for x in pomoc['trzy_kroki_uzycia'])}</ol>
    <div class="blk">Co znaczy która karta</div>
    <ul class="opisy">{opisy}</ul>
  </div>
</div>

<div class="blk">Polecenie dla dziecka <span class="info">to jest tekst nagrany głosem autorki</span></div>
<div class="polecenia">{polecenia}</div>

<div class="wskaz">{e(pomoc['wskazowka_dla_doroslego'])}</div>
{stopka(arkusz, nr_strony, ile)}
</section>"""


def strona_ciecia(arkusz: dict, pomoc: dict, konspekt_tytul: str,
                  nr_strony: int, ile: int) -> str:
    """Strona pod nożyczki: cztery karty 90 × 90 mm i pasek kolejności. Nic więcej,
    bo wszystko, co tu jeszcze stało, zostawało przecięte razem z kartami."""
    karty = "".join(karta(k) for k in arkusz["karty"])

    def pole_paska(i, p) -> str:
        obraz = obraz_base64(p.get("plik_symbolu"))
        rysunek = (f'<img src="{obraz}" alt="">' if obraz
                   else '<div class="sym">pole na własny symbol</div>')
        return (f'<div class="pole-k"><div class="num">{i}</div>{rysunek}'
                f'<div class="et">{e(bez_numeru(p["etykieta_dla_dziecka"]))}</div></div>')

    pasek = "".join(pole_paska(i, p) for i, p in enumerate(arkusz["pasek_kolejnosci"], start=1))
    return f"""<section class="strona ciecie">
{naglowek("karty pracy do wycięcia", arkusz, pomoc, konspekt_tytul,
          e(arkusz['tytul']), " · do wycięcia")}
<div class="blk">Karty dla dziecka <span class="info">rozmiar docelowy 90 × 90 mm · wytnij wzdłuż linii przerywanej</span></div>
<div class="karty">{karty}</div>

<div class="blk">Pasek kolejności <span class="info">wytnij w całości i powieś w miejscu, którego dotyczy</span></div>
<div class="pasek">{pasek}</div>
{stopka(arkusz, nr_strony, ile)}
</section>"""


def strona_historyjki(arkusz: dict, pomoc: dict, konspekt_tytul: str,
                      nr_strony: int, ile: int) -> str:
    """Druga strona A4 dla wskaźników, których pomoc wymaga obrazków: historyjki,
    drabiny albo skali. Rysunki przychodzą bez tekstu — polskie podpisy dokładamy
    tutaj, więc poprawka słowa nie oznacza przerysowywania obrazka."""
    h = arkusz["historyjka"]

    def kafel(p, nr=None) -> str:
        obraz = obraz_base64(p["plik"])
        numer = f'<span class="hnr">{nr}</span>' if nr else ""
        pytanie = f'<div class="hq">{e(p["pytanie"])}</div>' if p.get("pytanie") else ""
        rysunek = (f'<img src="{obraz}" alt="{e(p["podpis"])}">' if obraz
                   else f'<div class="hq">brak pliku {e(p["plik"].rsplit("/", 1)[-1])}</div>')
        return (f'<div class="hkafel">{rysunek}'
                f'<div class="hp">{numer}{e(p["podpis"])}</div>{pytanie}</div>')

    if h["rodzaj"] == "rozgalezienie":
        srodek = "".join(
            f'<div class="hwiersz"><div class="hnazwa">{e(w["nazwa"])}</div>'
            f'<div class="hpola">{kafel(w["poczatek"])}'
            f'{"".join(kafel(z) for z in w["zakonczenia"])}</div></div>'
            for w in h["wiersze"])
    else:
        numeruj = h["rodzaj"] in ("historyjka", "listwa", "drabina")
        srodek = ('<div class="hpola">'
                  + "".join(kafel(p, i if numeruj else None)
                            for i, p in enumerate(h["pola"], 1))
                  + "</div>")

    nazwy = {"historyjka": "historyjka obrazkowa", "drabina": "drabina do powieszenia",
             "listwa": "listwa scenariusza", "skala": "skala do wskazywania",
             "zestaw": "zestaw obrazków", "rozgalezienie": "historyjki w dwóch zakończeniach"}
    return f"""<section class="strona {e(h['rodzaj'])}">
<div class="head"><span class="mark" role="img" aria-label="Logo PCTP"></span>
  <div><h1>EduPlaner 2026</h1><div class="sub">{e(MODUL['nazwa'])} · {nazwy[h['rodzaj']]}</div></div>
  <div class="prawa"><b>{e(MODUL['kod'])} · KC-4</b><span>arkusz A4 · do wycięcia</span></div></div>
<div class="kreska"></div>
<div class="tyt"><span class="nr">{e(arkusz['wskaznik'])}</span>
  <div><h2>{e(h['tytul'])}</h2>
    <div class="kon">do konspektu „{e(konspekt_tytul)}” · pomoc: {e(pomoc['nazwa'])}</div></div></div>
<div class="hpo"><b>Po co to jest.</b> {e(h['po_co_dla_doroslego'])}<br>
  <b>Jak użyć.</b> {e(h['jak_uzyc_dla_doroslego'])}</div>
{srodek}
<div class="stopka"><span>EduPlaner 2026 · PCTP · pedagog specjalny <b>mgr Mirosława Ewa Jurczyszyn</b></span>
  <span>Karta pracy {nr_strony} z {ile} · wskaźnik {e(arkusz['wskaznik'])}</span></div>
</section>"""


def main() -> int:
    ap = argparse.ArgumentParser(description=f"Karty pracy — arkusze A4 modułu {MODUL['kod']}")
    ap.add_argument("--wyjscie", default=str(WYJSCIE), help="plik docelowy")
    ap.add_argument("--z-glosem", action="store_true", dest="z_glosem",
                    help="wklej nagrania w dokument (dana biometryczna — plik tylko do użytku "
                         "własnego autorki, nie do repozytorium)")
    args = ap.parse_args()
    # Wersja z głosem MUSI iść poza 02_gotowe_dokumenty: ten katalog trafia do
    # repozytorium, a nagranie to sklonowany głos autorki.
    if args.z_glosem and pathlib.Path(args.wyjscie).resolve() == WYJSCIE.resolve():
        raise SystemExit("--z-glosem wymaga --wyjscie poza 02_gotowe_dokumenty: "
                         "ten katalog trafia do repozytorium, a nagrania to dane biometryczne.")
    globals()["WKLEJ_GLOS"] = args.z_glosem

    materialy = wczytaj("materialy_do_druku.json")
    pomoce = {p["wskaznik"]: p for p in wczytaj(MODUL["plik_pomocy"])["pomoce"]}
    cele = wczytaj(MODUL["plik_celow"])
    wskazniki = {w["nr"]: w for g in cele[MODUL["grupa"]] for w in g["wskazniki"]}
    konspekty = {k["wskaznik"]: k["tytul"] for k in wczytaj(f"konspekty_{MODUL['kod'].lower()}.json")["konspekty"]}

    arkusze = materialy["arkusze"]
    # Wskaźnik z historyjką dostaje drugą stronę, więc liczbę stron znamy dopiero
    # po przejściu listy — stopka ma pokazywać prawdziwe „x z y”.
    # Każdy wskaźnik to dwie strony: instrukcja dla dorosłego i arkusz pod nożyczki.
    # Razem nie mieściły się na A4 — kartka rosła do 370 mm i drukarka tnęła ją
    # w przypadkowym miejscu, więc wydruk nie wyglądał jak podgląd na ekranie.
    ile = 2 * len(arkusze) + sum(1 for a in arkusze if a.get("historyjka"))
    strony, nr = [], 1
    for a in arkusze:
        p, tyt = pomoce[a["wskaznik"]], konspekty[a["wskaznik"]]
        strony.append(strona_instrukcji(a, p, tyt, nr, ile)); nr += 1
        strony.append(strona_ciecia(a, p, tyt, nr, ile)); nr += 1
        if a.get("historyjka"):
            strony.append(strona_historyjki(a, p, tyt, nr, ile)); nr += 1

    wyjscie = pathlib.Path(args.wyjscie)
    wyjscie.parent.mkdir(parents=True, exist_ok=True)
    wyjscie.write_text(
        '<!DOCTYPE html>\n<html lang="pl">\n<head>\n<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        f'<title>Karty pracy · {e(MODUL["nazwa"])} — EduPlaner 2026 · PCTP</title>\n'
        f'<style>:root{{--logo:url({logo_pctp()})}}{STYL}</style>\n</head>\n<body>\n' + "\n".join(strony) +
        '\n<script>' + SKRYPT + '</script>\n</body>\n</html>\n',
        encoding="utf-8")
    print(f"zapisano {sciezka_w_opisie(wyjscie)} "
          f"({wyjscie.stat().st_size // 1024} KB · {len(strony)} kart pracy A4)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
