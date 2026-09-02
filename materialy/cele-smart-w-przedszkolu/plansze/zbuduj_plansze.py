#!/usr/bin/env python3
"""Buduje plansze do filmu szkoleniowego "Cele SMART w przedszkolu".

Treść pochodzi wprost z broszury PCTP "Cele SMART w przedszkolu" (sygn. SMART-P1,
stan prawny 28 sierpnia 2026 r.). Plansze renderuje headless Chromium — bez sieci.

    python3 zbuduj_plansze.py            # HTML + PNG
    python3 zbuduj_plansze.py --tylko-html
"""
import subprocess, sys, pathlib

KAT = pathlib.Path(__file__).parent
CHROM = "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell"
ZNAK = ('<div class="znak"><b>PCTP KOSZALIN</b>EduPlaner 2026<br>'
        'Cele SMART w przedszkolu · SMART-P1</div>')

def slajd(nazwa, tytul, par, sub, tresc, styl="", klasa="", stopka_prawo="", a4=False):
    body_cls = " ".join(x for x in (["a4"] if a4 else []) + ([klasa] if klasa else []))
    gl = ""
    if tytul:
        gl = f'''<div class="gl"><div>
      {'<div class="par">'+par+'</div>' if par else ''}
      <h1>{tytul}</h1>
      {'<div class="sub">'+sub+'</div>' if sub else ''}
    </div>{ZNAK}</div>'''
    return f'''<!doctype html><html lang="pl"><head><meta charset="utf-8">
<title>{tytul or nazwa}</title><link rel="stylesheet" href="wspolne.css">
<style>{styl}</style></head><body class="{body_cls}">
<div class="pasek"></div>
<div class="ram">
  {gl}
  <div class="tresc">{tresc}</div>
  <div class="stopka"><span>EduPlaner 2026 · PCTP Koszalin — materiał szkoleniowy do broszury SMART-P1</span><span>{stopka_prawo}</span></div>
</div></body></html>'''

PLANSZE = []
def dodaj(nazwa, html, w=1920, h=1080):
    PLANSZE.append((nazwa, html, w, h))

# ---------------------------------------------------------------- 00 · TYTUŁ
dodaj("00_tytul", slajd("00_tytul", "", "", "", '''
<div class="tyt-ram">
  <div class="tyt-lewa">
    <div class="tyt-nad">Szkolenie dla nauczycieli przedszkola · PCTP Koszalin</div>
    <h1>Cele SMART<br>w przedszkolu</h1>
    <p class="tyt-lead">Jak napisać cel, który da się <b>zobaczyć</b>, <b>policzyć</b><br>i <b>obronić</b> przed zespołem, rodzicem i kuratorium.</p>
    <div class="tyt-chipy">
      <span>5 liter</span><span>6 kroków</span><span>1 formuła zdania</span>
      <span>9 obszarów podstawy</span><span>bank czasowników</span><span>podstawa prawna</span>
    </div>
    <div class="tyt-aut">Opracowanie: pedagog specjalny mgr Mirosława Ewa Jurczyszyn<br>
      <span>Na podstawie broszury „Cele SMART w przedszkolu”, sygn. SMART-P1 · stan prawny 28 sierpnia 2026 r.</span></div>
  </div>
  <div class="tyt-prawa">
    <div class="tyt-box zle">
      <div class="tyt-box-et">Tak zwykle brzmi cel</div>
      <p>„Dziecko będzie lepiej radziło sobie z emocjami i stanie się spokojniejsze.”</p>
      <div class="tyt-box-uw">Za pół roku nikt nie odpowie, czy się udało.</div>
    </div>
    <div class="tyt-strzalka">↓ po tym szkoleniu ↓</div>
    <div class="tyt-box ok">
      <div class="tyt-box-et">Tak brzmi cel, który działa</div>
      <p>„Dziecko rozpozna narastające napięcie i zastosuje oddech 4-4-4 w 4 na 5 sytuacji trudnych, do końca semestru.”</p>
      <div class="tyt-ptaszki"><span>✓ S</span><span>✓ M</span><span>✓ A</span><span>✓ R</span><span>✓ T</span><b>4/5</b></div>
    </div>
  </div>
</div>''', styl='''
.tyt-ram{display:grid;grid-template-columns:1fr 720px;gap:70px;height:100%;align-items:center;padding-bottom:20px}
.tyt-nad{font-size:16px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--pomarancz);margin-bottom:22px}
.tyt-lewa h1{font-size:104px;line-height:1;color:#fff;letter-spacing:-.03em}
.tyt-lead{font-size:28px;line-height:1.45;color:#D6CFEE;margin-top:28px}
.tyt-lead b{color:#fff}
.tyt-chipy{display:flex;flex-wrap:wrap;gap:11px;margin-top:34px;max-width:840px}
.tyt-chipy span{font-size:16px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:#fff;border:1px solid rgba(255,255,255,.35);border-radius:999px;padding:9px 17px}
.tyt-aut{margin-top:40px;font-size:19px;line-height:1.6;color:#C9C1E4}
.tyt-aut span{font-size:15px;color:#A79ECB}
.tyt-box{border-radius:18px;padding:26px 30px;background:#fff}
.tyt-box-et{font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;margin-bottom:12px}
.tyt-box p{font-size:26px;line-height:1.4;font-weight:700;color:var(--fiolet-cn)}
.tyt-box.zle{border-left:11px solid var(--czerwony)}
.tyt-box.zle .tyt-box-et{color:var(--czerwony)}
.tyt-box.ok{border-left:11px solid var(--zielony)}
.tyt-box.ok .tyt-box-et{color:var(--zielony)}
.tyt-box-uw{margin-top:12px;font-size:18px;color:var(--mute)}
.tyt-strzalka{text-align:center;font-size:15px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--pomarancz);padding:20px 0}
.tyt-ptaszki{display:flex;gap:16px;align-items:center;margin-top:16px;font-size:19px;font-weight:700;color:var(--zielony)}
.tyt-ptaszki b{margin-left:auto;background:var(--zielony);color:#fff;border-radius:8px;padding:5px 13px}
''', klasa="ciemny", stopka_prawo="Plansza 1 · Otwarcie"))

# ------------------------------------------------- 01 · §1 ŻYCZENIE / NARZĘDZIE
dodaj("01_zyczenie_narzedzie", slajd("01", "Cel-życzenie kontra cel-narzędzie", "§1 · Po co",
  "Cel ma trzech odbiorców: dziecko, rodzica i zespół, który dwa razy w roku ocenia, czy to zadziałało.", '''
<div class="dwie">
  <div class="zle-blok">
    <div class="et" style="color:var(--czerwony)">✕ Cel-życzenie</div>
    <p class="cytat" style="margin:14px 0 18px">„Dziecko będzie lepiej radziło sobie z emocjami i stanie się spokojniejsze.”</p>
    <p class="opis"><b>Czego tu brakuje:</b> nie wiadomo, co dokładnie dziecko ma zrobić, ile razy, w jakiej sytuacji ani do kiedy. Za pół roku nikt — łącznie z Tobą — nie odpowie, czy cel został osiągnięty. „Spokojniejsze” to interpretacja dorosłego, a nie zachowanie dziecka.</p>
  </div>
  <div class="ok-blok">
    <div class="et" style="color:var(--zielony)">✓ Cel-narzędzie</div>
    <p class="cytat" style="margin:14px 0 18px">„Dziecko rozpozna narastające napięcie i samodzielnie zastosuje wybraną strategię wyciszenia (oddech 4-4-4) w 4 na 5 sytuacji trudnych, do końca semestru.”</p>
    <p class="opis"><b>Każde słowo pracuje:</b> rozpozna / zastosuje — widać; 4 na 5 — policzysz; sytuacji trudnych — wiadomo, kiedy obserwować; do końca semestru — wiadomo, kiedy podsumować. Ten cel sam podpowiada, co masz robić w poniedziałek rano.</p>
  </div>
</div>
<div class="pom-blok" style="margin-top:26px">
  <div class="et" style="color:var(--pomarancz)">Zasada trzech osób — test przed wpisaniem celu</div>
  <p style="font-size:24px;line-height:1.5;margin-top:10px">Gdyby jutro zastąpiła Cię inna nauczycielka, czy z samego zapisu celu wiedziałaby, <b>co robić i co liczyć</b>? Jeśli tak — cel jest dobry. Jeśli musiałaby dopytywać — cel jest jeszcze życzeniem.</p>
</div>''', styl='''
.dwie{display:grid;grid-template-columns:1fr 1fr;gap:34px}
.opis{font-size:20px;line-height:1.55;color:var(--mute)}
.opis b{color:var(--fiolet)}
''', stopka_prawo="Plansza 2 · §1 Po co"))

# ------------------------------------------------------- 02 · §2 PIĘĆ LITER
LITERY = [
 ("S","Skonkretyzowany","SPECIFIC · CO DOKŁADNIE WIDZĘ",
  "Czy to zachowanie da się zobaczyć albo usłyszeć? Czy dwie różne osoby opiszą je tak samo?",
  "„rozpozna narastające napięcie i zastosuje oddech 4-4-4”",
  "„będzie spokojniejsze”, „poprawi zachowanie” — to Twoja ocena, nie czynność dziecka."),
 ("M","Mierzalny","MEASURABLE · ILE I NA ILE PRÓB",
  "Ile razy? Na ile okazji? Czym to policzę — kartą obserwacji, żetonami, listą?",
  "„w 4 na 5 sytuacji trudnych”, „w 8 na 10 prób”",
  "„często”, „zazwyczaj”, „znacząco częściej” — nie da się tego policzyć."),
 ("A","Osiągalny","ACHIEVABLE · NASTĘPNY KROK, NIE SKOK",
  "Czy to jeden krok dalej niż to, co dziecko potrafi dziś? Czy mieści się w przyznanym poziomie wsparcia (I / II / III)?",
  "wskazuje kolor na planszy → połączy kolor ze strategią wyciszenia",
  "Cel trzy piętra nad punktem wyjścia. Dziecko przez pół roku nie doświadcza sukcesu."),
 ("R","Istotny","RELEVANT · ZMIENIA CODZIENNOŚĆ",
  "Czy osiągnięcie tego celu realnie ułatwi dziecku dzień w przedszkolu? Czy wynika z WOPF i z orzeczenia?",
  "samoregulacja = warunek udziału w zabawie, w posiłku, w wyjściu do ogrodu",
  "Cel skopiowany z internetu albo z zeszłorocznego IPET-u innego dziecka."),
 ("T","Określony w czasie","TIME-BOUND · TERMIN I PUNKT KONTROLNY",
  "Do kiedy? I kiedy zajrzę do celu po drodze, żeby zdążyć go zmodyfikować?",
  "„do końca I semestru”, z przeglądem po 8 tygodniach",
  "„w ciągu roku szkolnego” bez punktu kontrolnego — w maju okazuje się, że nic się nie działo."),
]
karty = "".join(f'''<div class="k">
  <div class="lit">{l}</div><div class="naz">{n}</div><div class="ang">{a}</div>
  <div class="rzad"><span class="klucz">Pytanie</span><p>{p}</p></div>
  <div class="frag">{w}</div>
  <div class="pul"><span class="klucz">Pułapka</span><p>{u}</p></div>
</div>''' for l,n,a,p,w,u in LITERY)
dodaj("02_piec_liter", slajd("02", "Pięć liter, pięć pytań kontrolnych", "§2 · Anatomia",
  "SMART to nie ozdobnik w tabelce — to pięć filtrów, przez które przepuszczasz jedno zdanie.",
  f'<div class="karty">{karty}</div>', styl='''
.karty{display:grid;grid-template-columns:repeat(5,1fr);gap:18px;height:100%}
.k{background:#fff;border:1px solid var(--linia);border-top:9px solid var(--pomarancz);border-radius:16px;padding:30px 26px;display:flex;flex-direction:column}
.lit{font-size:96px;font-weight:700;color:var(--pomarancz);line-height:.85;letter-spacing:-.04em}
.naz{font-size:28px;font-weight:700;color:var(--fiolet);margin:16px 0 4px;line-height:1.1}
.ang{font-size:12px;font-weight:700;letter-spacing:.09em;color:var(--faint);margin-bottom:24px}
.klucz{display:block;font-size:11px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--mute);margin-bottom:6px}
.rzad p{font-size:20px;line-height:1.45;color:var(--atrament)}
.frag{margin:22px 0;background:#F1F8F4;border-left:6px solid var(--zielony);border-radius:0 9px 9px 0;padding:15px 15px;font-size:19px;line-height:1.4;font-weight:700;color:var(--fiolet-cn)}
.pul{margin-top:auto}
.pul p{font-size:18.5px;line-height:1.42;color:var(--czerwony)}
''', stopka_prawo="Plansza 3 · §2 Anatomia"))

# ----------------------------------------------------- 03 · §3 SZEŚĆ KROKÓW
KROKI = [
 ("1","Zobacz i nazwij zachowanie","Przez ok. dwa tygodnie zapisuj, co dokładnie się dzieje — bez ocen i bez przyczyn. Zbierz też sytuacje, w których dziecku się udaje.",
  "Gdybym nagrała to kamerą, co dokładnie widać na nagraniu?","„Zaciska pięści, oddycha szybciej, odwraca się od stołu” — zamiast „złości się”."),
 ("2","Zmierz punkt wyjścia","Policz, jak jest teraz. Bez tej liczby nie ustawisz sensownego kryterium ani nie wykażesz postępu.",
  "Na 5 trudnych sytuacji — w ilu dziecko poradziło sobie dziś?","Punkt wyjścia = 1 na 5 sytuacji, i to tylko z podpowiedzią dorosłego."),
 ("3","Wybierz czasownik, który widać","Serce celu. Wskaże, nazwie, poprosi, zastosuje, poda, wybierze — tak. „Zrozumie”, „poczuje”, „będzie wiedziało” — nie.",
  "Czy mogę postawić kreskę w chwili, gdy to się stanie?",""),
 ("4","Dopisz miarę i kryterium","Liczba + z ilu prób + w jakim okresie. Kryterium ustaw o jeden–dwa punkty powyżej punktu wyjścia, nie na maksimum.",
  "Punkt wyjścia 1/5 → realne kryterium to 3–4 na 5, nie 5 na 5.","„w 4 na 5 obserwowanych sytuacji, zapis w karcie obserwacji”."),
 ("5","Ustal warunki i poziom wsparcia","Napisz wprost: samodzielnie / po jednej podpowiedzi słownej / z pomocą gestu. Dodaj, gdzie i kiedy: w sali, w ogrodzie, przy posiłku.",
  "Ile pomocy wolno dorosłemu dać, żeby to nadal liczyło się jako sukces dziecka?",""),
 ("6","Wyznacz termin i sposób sprawdzenia","Data końcowa plus punkt kontrolny w połowie drogi. Termin celu nie może wykraczać poza okres, na jaki opracowano program.",
  "Kiedy siadam z tym celem po raz pierwszy, a kiedy ostatni?","Przegląd po 8 tygodniach, podsumowanie na koniec semestru, WOPF dwa razy w roku."),
]
kr = "".join(f'''<div class="kr">
  <div class="nr">{n}</div>
  <div class="tre"><h3>{t}</h3><p>{o}</p>
    <div class="mysl"><span>Powiedz sobie</span>{m}</div>
    {'<div class="prz">Przykład: '+p+'</div>' if p else ''}
  </div></div>''' for n,t,o,m,p in KROKI)
dodaj("03_szesc_krokow", slajd("03", "Sześć kroków od obserwacji do zapisu", "§3 · Skrypt",
  "Cel nie powstaje przy biurku, tylko na dywanie. Najpierw patrzysz i liczysz, dopiero potem piszesz.",
  f'<div class="kroki">{kr}</div>', styl='''
.kroki{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr 1fr;gap:16px 30px;height:100%}
.kr{display:flex;gap:18px;align-items:flex-start;background:#fff;border:1px solid var(--linia);border-radius:14px;padding:18px 22px}
.nr{flex:0 0 50px;height:50px;border-radius:50%;background:var(--fiolet);color:#fff;display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:700}
.tre h3{font-size:25px;color:var(--fiolet-cn);margin-bottom:6px}
.tre p{font-size:19px;line-height:1.45;color:var(--mute)}
.mysl{margin-top:11px;background:var(--papier-lt);border:1px dashed var(--linia);border-radius:9px;padding:10px 14px;font-size:18.5px;font-style:italic;color:var(--fiolet)}
.mysl span{display:block;font-style:normal;font-size:10.5px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--faint);margin-bottom:3px}
.prz{margin-top:9px;font-size:18px;color:var(--pomarancz);line-height:1.4}
''', stopka_prawo="Plansza 4 · §3 Skrypt"))

# ---------------------------------------------------------- 04 · §4 FORMUŁA
POLA = [("1 · Kto","Dziecko / imię","Dziecko"),
        ("2 · W jakiej sytuacji","gdzie i kiedy to obserwujesz","w sytuacjach trudnych w sali i w ogrodzie"),
        ("3 · Z jakim wsparciem","samodzielnie / z podpowiedzią","samodzielnie, bez podpowiedzi słownej dorosłego"),
        ("4 · Co zrobi","czasownik, który widać + co konkretnie","rozpozna narastające napięcie na termometrze i zastosuje oddech 4-4-4"),
        ("5 · Miara","ile na ile prób","w 4 na 5 obserwowanych sytuacji"),
        ("6 · Termin","do kiedy","do końca I semestru"),
        ("7 · Sprawdzenie","czym to potwierdzisz","zapis w karcie obserwacji")]
pola_html = "".join(f'''<div class="pole"><label>{a}</label><div class="hint">{b}</div><div class="v">{c}</div></div>''' for a,b,c in POLA)
dodaj("04_formula_zdania", slajd("04", "Jedno zdanie, siedem miejsc do wypełnienia", "§4 · Formuła",
  "Tak wygląda wpisywanie celu: wypełniasz siedem pól po kolei i czytasz całość na głos.",
  f'''<div class="ukl">
  <div class="formularz">
    <div class="et" style="margin-bottom:14px">Formularz celu · EduPlaner 2026 → konspekt i sekcja III IPET</div>
    {pola_html}
  </div>
  <div class="prawa">
    <div class="ok-blok">
      <div class="et" style="color:var(--zielony)">✓ Formuła wypełniona — cel z konspektu „Termometr napięcia”</div>
      <p class="cytat" style="margin-top:14px">„Dziecko <u>w sytuacjach trudnych w sali i w ogrodzie</u> <u>samodzielnie, bez podpowiedzi słownej dorosłego</u>, <u>rozpozna narastające napięcie na termometrze i zastosuje strategię wyciszenia (oddech 4-4-4)</u> <u>w 4 na 5 obserwowanych sytuacji</u>, <u>do końca I semestru</u>, co potwierdzi <u>zapis w karcie obserwacji</u>.”</p>
    </div>
    <div class="pom-blok" style="margin-top:22px">
      <div class="et" style="color:var(--pomarancz)">Test głośnego czytania</div>
      <p style="font-size:21px;line-height:1.5;margin-top:9px">Przeczytaj cel rodzicowi i zapytaj: „co konkretnie zobaczy Pani u dziecka w grudniu, jeśli nam się uda?”. Jeśli rodzic odpowie jednym zdaniem — cel jest zrozumiały. Jeśli milknie — wróć do kroku 3.</p>
    </div>
    <div class="zrodlo">Ten sam układ pól — <b>zachowanie · warunki · kryterium</b> — opisał R. F. Mager (1962), a amerykańskie prawo oświatowe (IDEA, 34 CFR § 300.320) wymaga w celu IEP dokładnie czterech elementów: terminu, warunków, zachowania i kryterium.</div>
  </div>
</div>''', styl='''
.ukl{display:grid;grid-template-columns:790px 1fr;gap:44px;height:100%}
.formularz{background:#fff;border:1px solid var(--linia);border-radius:18px;padding:24px 26px;box-shadow:0 30px 70px -45px rgba(45,27,105,.5)}
.pole{border:1px solid var(--linia);border-radius:11px;padding:10px 15px;margin-bottom:9px;background:var(--papier-lt)}
.pole:last-child{border:2px solid var(--pomarancz);background:#FFF6F2;margin-bottom:0}
.pole label{display:block;font-size:11px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--fiolet);margin-bottom:2px}
.pole .hint{font-size:13px;color:var(--faint);margin-bottom:5px}
.pole .v{font-size:19px;font-weight:700;color:var(--fiolet-cn);line-height:1.3}
.cytat u{text-decoration:none;background:linear-gradient(transparent 62%,#FFD9C7 62%)}
.zrodlo{margin-top:22px;font-size:16px;line-height:1.55;color:var(--mute);border-left:4px solid var(--linia);padding-left:16px}
.zrodlo b{color:var(--fiolet)}
''', stopka_prawo="Plansza 5 · §4 Formuła zdania"))

# ------------------------------------------------------- 05 · §5 CZASOWNIKI
DOBRE = ["wskaże","nazwie","poda","powtórzy","zastosuje","wybierze","ułoży","poprosi o…","zgłosi",
         "podejdzie","odłoży","poczeka","przekaże","pokaże na obrazku","policzy","wykona","zapyta","odpowie"]
ZLE = ["zrozumie","będzie wiedziało","poczuje","uświadomi sobie","polubi","zainteresuje się",
       "będzie chciało","nauczy się","poprawi","wzmocni","rozwinie","będzie lepiej…"]
dodaj("05_bank_czasownikow", slajd("05", "Bank czasowników", "§5 · Słownik",
  "Najszybsza droga do dobrego celu prowadzi przez dobry czasownik.",
  f'''<div class="dwie">
  <div class="ok-blok">
    <div class="et" style="color:var(--zielony)">✓ Czasowniki, które widać — przy tych postawisz kreskę</div>
    <div class="chmura">{"".join(f'<span>{w}</span>' for w in DOBRE)}</div>
  </div>
  <div class="zle-blok">
    <div class="et" style="color:var(--czerwony)">✕ Czasowniki-pułapki — dzieją się w głowie dziecka</div>
    <div class="chmura zla">{"".join(f'<span>{w}</span>' for w in ZLE)}</div>
  </div>
</div>
<div class="pom-blok" style="margin-top:24px">
  <div class="et" style="color:var(--pomarancz)">Jak naprawić czasownik-pułapkę — zapytaj: „po czym poznam, że dziecko to zrozumiało?”</div>
  <div class="napraw">
    <div><span class="zl">„zrozumie zasadę”</span><b>→</b><span class="db">„poda zasadę własnymi słowami lub wskaże ją na obrazku”</span></div>
    <div><span class="zl">„rozpozna emocje”</span><b>→</b><span class="db">„wskaże na planszy kolor odpowiadający swojemu napięciu”</span></div>
    <div><span class="zl">„poprosi o pomoc, gdy poczuje złość”</span><b>→</b><span class="db">„użyje umówionego gestu lub zdania «potrzebuję przerwy»”</span></div>
  </div>
</div>''', styl='''
.dwie{display:grid;grid-template-columns:1fr 1fr;gap:34px}
.chmura{display:flex;flex-wrap:wrap;gap:11px;margin-top:18px}
.chmura span{font-size:23px;font-weight:700;color:var(--zielony);background:#fff;border:1px solid #A9D8C4;border-radius:999px;padding:9px 19px}
.chmura.zla span{color:var(--czerwony);border-color:#E9BDB0;text-decoration:line-through;text-decoration-thickness:2px}
.napraw{margin-top:14px;display:grid;gap:9px}
.napraw div{display:flex;align-items:center;gap:16px;font-size:20px}
.napraw .zl{color:var(--czerwony);flex:0 0 380px}
.napraw b{color:var(--pomarancz);font-size:24px}
.napraw .db{color:var(--zielony);font-weight:700}
''', stopka_prawo="Plansza 6 · §5 Bank czasowników"))

# ------------------------------------------------------- 06 · §6 TERMOMETR
FILTRY = [("S","Skonkretyzowany","Dwie obserwowalne czynności: <b>rozpozna</b> (wskazuje poziom na termometrze) i <b>zastosuje</b> (wykonuje oddech 4-4-4). Obie widać z drugiego końca sali."),
 ("M","Mierzalny","4 na 5 sytuacji trudnych, liczone w karcie obserwacji. Jedna kreska = jedna sytuacja. Podsumowanie ilościowe na koniec semestru."),
 ("A","Osiągalny","Cel opisany dla poziomu I, z gotową modyfikacją dla poziomu II i III. Skala 1–6 opiera się na kolorze i sygnale z ciała, a nie na nazywaniu emocji."),
 ("R","Istotny","Sfera integracji społeczno-emocjonalnej i samoregulacji <span class='icf'>(ICF b1521 — regulacja emocji)</span>. Strefa żółta to moment, w którym strategia jeszcze działa."),
 ("T","Określony w czasie","Do końca semestru, przy pracy ciągłej w ciągu dnia. Termometr wraca w realnych sytuacjach — dane zbierają się same.")]
fil = "".join(f'<div class="f"><div class="lit">{l}</div><div><b>{n}</b><p>{o}</p></div></div>' for l,n,o in FILTRY)
dodaj("06_termometr_rozbior", slajd("06", "Rozbiór celu wzorcowego: „Termometr napięcia”", "§6 · Wzorzec",
  "Cel z konspektu TUE-1 przepuszczony przez pięć filtrów. Narzędzie pomiaru jest tu jednocześnie pomocą dydaktyczną.",
  f'''<div class="ukl">
  <div>
    <div class="pom-blok" style="margin-bottom:20px">
      <div class="et" style="color:var(--pomarancz)">Cel</div>
      <p class="cytat" style="margin-top:10px">„Dziecko rozpozna narastające napięcie i samodzielnie zastosuje wybraną strategię wyciszenia (np. oddech 4-4-4) w 4 na 5 sytuacji trudnych, do końca semestru.”</p>
    </div>
    {fil}
  </div>
  <div class="prawa">
    <div class="term-karta">
      <div class="et" style="text-align:center;margin-bottom:16px">Termometr napięcia 1–6</div>
      <div class="term">
        <div class="strefa czerw"><div class="num">6<br>5</div><div class="opis"><b>Czerwona</b>za późno na naukę — tylko bezpieczeństwo</div></div>
        <div class="strefa zolt"><div class="num">4<br>3</div><div class="opis"><b>Żółta</b>tu działa strategia — to jest Twój moment</div></div>
        <div class="strefa ziel"><div class="num">2<br>1</div><div class="opis"><b>Zielona</b>spokój, gotowość do uczenia się</div></div>
      </div>
    </div>
    <div class="karta-obs">
      <div class="et">Karta obserwacji — tak wygląda „4 na 5”</div>
      <p>Pięć kolejnych sytuacji trudnych w tygodniu. Zaznaczasz tylko jedno: czy dziecko <b>samodzielnie</b> rozpoznało poziom i użyło strategii.</p>
      <div class="kreski"><span class="p">✓</span><span class="p">✓</span><span class="m">–</span><span class="p">✓</span><span class="p">✓</span>
        <b>4 / 5 → kryterium spełnione</b></div>
    </div>
  </div>
</div>''', styl='''
.ukl{display:grid;grid-template-columns:1fr 620px;gap:40px;height:100%}
.f{display:flex;gap:15px;margin-bottom:11px;align-items:flex-start}
.f .lit{flex:0 0 40px;height:40px;border-radius:10px;background:var(--fiolet);color:#fff;display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:700}
.f b{font-size:17px;color:var(--fiolet);letter-spacing:.05em;text-transform:uppercase;display:block;margin-bottom:2px}
.f p{font-size:17px;line-height:1.45;color:var(--mute)}
.f p b{display:inline;font-size:17px;text-transform:none;letter-spacing:0;color:var(--fiolet-cn)}
.term-karta{background:#fff;border:1px solid var(--linia);border-radius:18px;padding:22px}
.term{display:flex;flex-direction:column;gap:8px}
.strefa{display:flex;align-items:center;gap:18px;border-radius:12px;padding:14px 18px;color:#fff}
.strefa .num{font-size:26px;font-weight:700;line-height:1.05;flex:0 0 46px;text-align:center}
.strefa .opis{font-size:17px;line-height:1.35}
.strefa .opis b{display:block;font-size:19px;letter-spacing:.06em;text-transform:uppercase}
.czerw{background:var(--czerwony)} .zolt{background:var(--zolty)} .ziel{background:var(--zielony)}
.karta-obs{margin-top:18px;background:#fff;border:1px solid var(--linia);border-radius:18px;padding:22px 24px}
.karta-obs p{font-size:17px;line-height:1.5;color:var(--mute);margin-top:9px}
.karta-obs p b{color:var(--fiolet)}
.kreski{display:flex;align-items:center;gap:12px;margin-top:16px}
.kreski span{width:52px;height:52px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:700;border:2px solid var(--linia)}
.kreski .p{color:var(--zielony);border-color:#A9D8C4;background:#F1F8F4}
.kreski .m{color:var(--faint)}
.kreski b{margin-left:10px;font-size:19px;color:var(--zielony)}
''', stopka_prawo="Plansza 7 · §6 Wzorzec"))

# --------------------------------------------------- 07 · §7 DZIEWIĘĆ OBSZARÓW
OBSZARY = [
 ("Społeczny","relacje · współpraca · przynależność","Wchodzi do zabawy, zabierając zabawkę; o pozwolenie pyta w 1 na 5 sytuacji.","„Dziecko dołączy do zabawy rówieśników, używając umówionego zwrotu («Mogę się z wami bawić?»), samodzielnie, w 4 na 5 obserwowanych sytuacji zabawy swobodnej, do końca I semestru.”","Karta obserwacji zabawy swobodnej — pięć sytuacji w tygodniu."),
 ("Osobisty","tożsamość · emocje · granice","Po przegranej wychodzi z zabawy albo płacze — w 4 na 5 gier.","„Dziecko po przegranej w grze planszowej zostanie przy stole i dokończy rundę, po jednej podpowiedzi słownej, w 3 na 5 gier, do 15 grudnia.”","Wpis w dzienniku po każdej grze; przegląd po 8 tygodniach."),
 ("Językowy","mowa · komunikacja · droga do czytania","Opowiada zdaniami dwu- i trzywyrazowymi, gubi kolejność zdarzeń.","„Dziecko opowie treść historyjki z trzech obrazków, zachowując kolejność zdarzeń, samodzielnie, w 4 na 5 prób, do końca semestru.”","Arkusz zliczeń — jedna historyjka tygodniowo."),
 ("Matematyczny","orientacja · rytmy · intuicja","Kontynuuje rytm dwuelementowy, ale tylko z podpowiedzią.","„Dziecko ułoży dalszy ciąg rytmu trzyelementowego (np. czerwony–niebieski–żółty) samodzielnie, w 8 na 10 prób, do końca lutego.”","Karta zliczeń prób przy kąciku matematycznym."),
 ("Przyrodniczy","obserwacja · przyroda z bliska","Nazywa dwa zwierzęta spotykane w ogrodzie przedszkolnym.","„Dziecko wskaże i nazwie trzy oznaki zmiany pory roku zaobserwowane w ogrodzie, samodzielnie, w 4 na 5 wyjść, do końca listopada.”","Kalendarz obserwacji prowadzony po każdym wyjściu."),
 ("Techniczny","praca rąk · narzędzia · konstruowanie","Łączy elementy tylko wtedy, gdy dorosły przytrzyma materiał.","„Dziecko połączy dwa elementy konstrukcji, samodzielnie wybierając sposób łączenia (taśma, sznurek, klej), bez pomocy fizycznej dorosłego, w 4 na 5 zajęć majsterkowania, do końca semestru.”","Karta obserwacji kącika majsterkowania."),
 ("Cyfrowy","rozumienie techniki · higiena cyfrowa","Rozpoznaje telefon i tablet, nie potrafi powiedzieć, do czego służą.","„Dziecko wskaże na obrazkach trzy urządzenia i powie własnymi słowami, do czego każde służy (np. telefon — do rozmowy), samodzielnie, w 4 na 5 prób, do końca marca.”","Arkusz zliczeń; zestaw obrazków urządzeń."),
 ("Artystyczny","proces twórczy · ekspresja emocji","Przerywa pracę plastyczną w połowie; nie komentuje tego, co zrobiło.","„Dziecko dokończy pracę plastyczną i powie, co przedstawia oraz jaki nastrój chciało pokazać, samodzielnie, w 4 na 5 zajęć, do końca semestru.”","Teczka prac z krótką notatką przy każdej."),
 ("Ruchowy","motoryka · postawa · bezpieczeństwo","Utrzymuje równowagę na jednej nodze przez ok. 2 sekundy.","„Dziecko utrzyma równowagę, stojąc na jednej nodze przez 5 sekund, samodzielnie, w 4 na 5 prób, do końca kwietnia.”","Pomiar stoperem raz w tygodniu, zapis w karcie."),
]
ob = "".join(f'''<div class="o"><div class="naz">{n}<span>{p}</span></div>
  <div class="wyj"><span class="klucz">Punkt wyjścia</span>{w}</div>
  <div class="cel">{c}</div>
  <div class="mia"><span class="klucz">Czym mierzysz</span>{m}</div></div>''' for n,p,w,c,m in OBSZARY)
dodaj("07_dziewiec_obszarow", slajd("07", "Dziewięć obszarów nowej podstawy — gotowe cele", "§7 · Bank celów",
  "Od 1 września 2026 r. osiągnięcia dziecka opisuje się w dziewięciu obszarach zamiast czterech. Po jednym gotowym celu na każdy obszar — z punktem wyjścia i narzędziem pomiaru.",
  f'<div class="obszary">{ob}</div>', styl='''
.obszary{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;height:100%}
.o{background:#fff;border:1px solid var(--linia);border-left:6px solid var(--pomarancz);border-radius:12px;padding:14px 16px;display:flex;flex-direction:column}
.naz{font-size:20px;font-weight:700;color:var(--fiolet);line-height:1.15}
.naz span{display:block;font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--faint);margin-top:3px}
.klucz{display:block;font-size:9.5px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--faint);margin-bottom:2px}
.wyj{margin:9px 0;font-size:14px;line-height:1.35;color:var(--mute)}
.cel{background:#F1F8F4;border-radius:8px;padding:10px 12px;font-size:15px;line-height:1.38;font-weight:700;color:var(--fiolet-cn)}
.mia{margin-top:auto;padding-top:9px;font-size:13.5px;line-height:1.35;color:var(--teal)}
''', stopka_prawo="Plansza 8 · §7 Bank celów"))

# ------------------------------------------------------- 08 · §8 EWALUACJA
dodaj("08_ewaluacja", slajd("08", "Zielony, żółty, czerwony — co zrobić z celem", "§8 · Ewaluacja",
  "Cel, który nie działa, nie jest porażką dziecka — jest informacją dla zespołu.",
  '''<div class="swiatla">
  <div class="s ziel"><div class="lampa"></div><h3>Zielony</h3><div class="zakres">4–5 na 5 sytuacji</div>
    <ul><li>Cel osiągnięty — zapisz to konkretnie, <b>z liczbą</b>.</li>
        <li>Podnieś poprzeczkę w stronę generalizacji: inne miejsce, inna osoba dorosła, większa grupa.</li>
        <li>Nowy cel buduj od tego, co dziecko już robi — nie zaczynaj od zera.</li></ul></div>
  <div class="s zolt"><div class="lampa"></div><h3>Żółty</h3><div class="zakres">2–3 na 5 sytuacji</div>
    <ul><li><b>Cel zostaje — zmieniasz drogę do niego.</b></li>
        <li>Zmniejsz krok i tempo, dołóż podpowiedź (wzór, gest, początek odpowiedzi), wydłuż czas.</li>
        <li>Zwiększ liczbę prób i dodaj wzmocnienie; pracuj na bliższych, konkretnych przykładach.</li></ul></div>
  <div class="s czerw"><div class="lampa"></div><h3>Czerwony</h3><div class="zakres">0–1 na 5 sytuacji</div>
    <ul><li>Cofnij cel o etap, do poziomu, na którym dziecko <b>odnosi sukces</b>.</li>
        <li>Uprość zadanie (mniej elementów, praca 1:1), zmień kanał — obraz lub gest zamiast słowa.</li>
        <li>Zweryfikuj poziom wsparcia (I / II / III) i sam zapis celu; rozważ konsultację zespołu.</li></ul></div>
</div>
<div class="pom-blok" style="margin-top:26px">
  <div class="et" style="color:var(--pomarancz)">Jak zapisać ewaluację, żeby broniła się sama — trzy zdania</div>
  <div class="trzy">
    <div><b>1 · Liczba</b>„w okresie IX–I odnotowano 4 na 5 sytuacji”</div>
    <div><b>2 · Warunki</b>„samodzielnie, bez podpowiedzi, w sali i w ogrodzie”</div>
    <div><b>3 · Wniosek i decyzja</b>„cel osiągnięty, przechodzimy do generalizacji na wyjścia poza teren przedszkola”</div>
  </div>
  <p style="margin-top:14px;font-size:18px;color:var(--mute)">Taki zapis jest zarazem <b>oceną efektywności udzielanej pomocy</b> i materiałem do <b>wielospecjalistycznej oceny poziomu funkcjonowania</b>.</p>
</div>''', styl='''
.swiatla{display:grid;grid-template-columns:repeat(3,1fr);gap:26px}
.s{background:#fff;border:1px solid var(--linia);border-radius:16px;padding:22px 24px}
.lampa{width:34px;height:34px;border-radius:50%;margin-bottom:14px}
.ziel .lampa{background:var(--zielony)} .zolt .lampa{background:var(--zolty)} .czerw .lampa{background:var(--czerwony)}
.s h3{font-size:28px;color:var(--fiolet)}
.zakres{font-size:16px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--mute);margin:4px 0 14px}
.s ul{list-style:none}
.s li{font-size:18px;line-height:1.45;padding-left:22px;position:relative;margin-bottom:9px;color:var(--atrament)}
.s li::before{content:"→";position:absolute;left:0;color:var(--pomarancz);font-weight:700}
.s li b{color:var(--fiolet)}
.trzy{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:12px}
.trzy div{background:#fff;border-radius:10px;padding:13px 16px;font-size:19px;line-height:1.4;color:var(--fiolet-cn);font-style:italic}
.trzy b{display:block;font-style:normal;font-size:11px;letter-spacing:.13em;text-transform:uppercase;color:var(--pomarancz);margin-bottom:6px}
''', stopka_prawo="Plansza 9 · §8 Ewaluacja"))

# ------------------------------------------------------- 09 · §9 CHECKLISTA
CHECK = ["Cel opisuje czynność dziecka, a nie działanie nauczyciela ani stan emocjonalny.",
 "Czasownik pochodzi z listy „które widać” (§5).",
 "Jest liczba: ile razy, na ile prób.",
 "Znam punkt wyjścia i kryterium jest od niego wyższe o jeden–dwa kroki, nie o pięć.",
 "Napisane jest, ile wsparcia dziecko może dostać (samodzielnie / z podpowiedzią).",
 "Wiadomo, gdzie i kiedy obserwuję (sala, ogród, posiłek, szatnia).",
 "Jest termin i punkt kontrolny w połowie okresu.",
 "Wpisane jest narzędzie pomiaru (karta obserwacji, arkusz zliczeń).",
 "Cel wynika z WOPF i orzeczenia, a nie z gotowego wzoru.",
 "Inna nauczycielka, czytając sam cel, wie, co robić w poniedziałek."]
PARY = [("„Dziecko będzie chętniej uczestniczyć w zajęciach grupowych.”","„Dziecko dołączy do zabawy w kole i pozostanie w niej przez co najmniej 5 minut, w 3 na 5 zajęć w tygodniu, do końca I semestru.”"),
 ("„Nauczyciel będzie wspierał dziecko w rozpoznawaniu emocji.”","„Dziecko wskaże na planszy kolor odpowiadający swojemu napięciu, w 4 na 5 sytuacji trudnych.” <i>(cel opisuje dziecko, nie dorosłego)</i>"),
 ("„Dziecko zrozumie zasady panujące w grupie.”","„Dziecko poda własnymi słowami lub wskaże na obrazku dwie zasady obowiązujące w sali, w 4 na 5 prób.”"),
 ("„Dziecko poprawi komunikację z rówieśnikami.”","„Dziecko poprosi rówieśnika o zabawkę umówionym zdaniem, zamiast ją zabierać, w 3 na 5 obserwowanych sytuacji.”"),
 ("„Dziecko osiągnie samodzielność w samoobsłudze w ciągu roku.”","„Dziecko samodzielnie założy buty na rzepy (dopuszczalna jedna podpowiedź słowna) w 4 na 5 wyjść do ogrodu, do 15 grudnia; przegląd po 8 tygodniach.”")]
ch = "".join(f'<li>{t}</li>' for t in CHECK)
pr = "".join(f'<tr><td class="zl">{a}</td><td class="ar">→</td><td class="db">{b}</td></tr>' for a,b in PARY)
dodaj("09_checklista", slajd("09", "Checklista przed wpisaniem celu do dokumentu", "§9 · Kontrola",
  "Dziesięć pytań. Jeśli na któreś odpowiadasz „nie” — wróć do odpowiedniego kroku ze §3.",
  f'''<div class="ukl">
  <div class="karta"><div class="et" style="margin-bottom:14px">Dziesięć pytań kontrolnych</div><ol class="ch">{ch}</ol></div>
  <div class="karta"><div class="et" style="margin-bottom:14px">Pięć najczęstszych poprawek</div>
    <table class="pary"><tr><th>Zapis, który się nie obroni</th><th></th><th>Ten sam zamiar, zapisany dobrze</th></tr>{pr}</table></div>
</div>''', styl='''
.ukl{display:grid;grid-template-columns:640px 1fr;gap:34px;height:100%}
ol.ch{list-style:none;counter-reset:c}
ol.ch li{counter-increment:c;font-size:18px;line-height:1.42;padding-left:44px;position:relative;margin-bottom:13px}
ol.ch li::before{content:"□";position:absolute;left:0;top:-3px;font-size:26px;color:var(--pomarancz)}
ol.ch li::after{content:counter(c);position:absolute;left:8.5px;top:2px;font-size:12px;font-weight:700;color:var(--pomarancz)}
table.pary{width:100%;border-collapse:collapse}
table.pary th{text-align:left;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--mute);padding:0 12px 10px;border-bottom:2px solid var(--linia)}
table.pary td{padding:12px;vertical-align:top;border-bottom:1px solid var(--linia);font-size:17px;line-height:1.4}
td.zl{color:var(--czerwony);width:38%}
td.ar{color:var(--pomarancz);font-size:22px;font-weight:700;width:34px;text-align:center}
td.db{color:var(--fiolet-cn);font-weight:700}
td.db i{font-weight:400;color:var(--mute)}
''', stopka_prawo="Plansza 10 · §9 Kontrola"))

# ------------------------------------------------- 10 · §10 PODSTAWA PRAWNA
AKTY = [("Ustawa z dnia 14 grudnia 2016 r. — Prawo oświatowe","t.j. Dz.U. z 2025 r. poz. 1043",
  "Podstawa całego systemu: przedszkole ma dostosowywać treści, metody i organizację nauczania do możliwości psychofizycznych dziecka oraz zapewniać pomoc psychologiczno-pedagogiczną (m.in. art. 1 i art. 47 ust. 1 pkt 5, art. 127). Dostosowanie musi być opisane konkretnie — stąd wymóg mierzalnego celu."),
 ("Rozporządzenie MEN z dnia 9 sierpnia 2017 r. w sprawie zasad organizacji i udzielania pomocy psychologiczno-pedagogicznej","t.j. Dz.U. z 2023 r. poz. 1798",
  "Obowiązek obserwacji pedagogicznej nastawionej na wczesne rozpoznanie dysharmonii rozwojowych, rozpoznawania potrzeb i barier oraz <b>oceny efektywności udzielanej pomocy</b> wraz z wnioskami (m.in. § 20). Określa formy pomocy w przedszkolu (§ 6). Bez liczby w celu nie da się tej oceny sporządzić."),
 ("Rozporządzenie MEN z dnia 9 sierpnia 2017 r. w sprawie warunków organizowania kształcenia dzieci i młodzieży niepełnosprawnych…","t.j. Dz.U. z 2020 r. poz. 1309",
  "To „konstytucja IPET-u” (§ 6). Zespół <b>co najmniej dwa razy w roku szkolnym</b> dokonuje okresowej wielospecjalistycznej oceny poziomu funkcjonowania, uwzględniając ocenę efektywności programu, i w miarę potrzeb go modyfikuje. Cel SMART jest tym, co w ogóle daje się ocenić po pół roku."),
 ("Rozporządzenie MEN z dnia 24 sierpnia 2017 r. w sprawie organizowania wczesnego wspomagania rozwoju dzieci","Dz.U. z 2017 r. poz. 1635",
  "Dotyczy dzieci objętych WWRD. Zespół opracowuje indywidualny program wczesnego wspomagania i analizuje jego skuteczność, wprowadzając zmiany stosownie do potrzeb dziecka i rodziny. Ta sama logika: cel → działanie → sprawdzenie → modyfikacja."),
 ("Rozporządzenie Ministra Edukacji z dnia 11 marca 2026 r. w sprawie podstawy programowej wychowania przedszkolnego…","Dz.U. z 2026 r. poz. 378 — obowiązuje od 1 września 2026 r.",
  "Porządkuje osiągnięcia dziecka w <b>dziewięciu obszarach</b> w miejsce dotychczasowych czterech. Każdy cel indywidualny musi wskazywać obszar i konkretne osiągnięcie: cel jest uszczegółowieniem wymagania z podstawy, nie bytem osobnym. Zastępuje rozporządzenie z 14 lutego 2017 r. (Dz.U. poz. 356).")]
akt = "".join(f'<tr><td class="a"><b>{n}</b><span>{s}</span></td><td class="w">{o}</td></tr>' for n,s,o in AKTY)
dodaj("10_podstawa_prawna", slajd("10", "Podstawa prawna — pięć aktów", "§10 · Prawo",
  "Cel SMART nie jest wymysłem metodyków. To praktyczna odpowiedź na to, czego przepisy wymagają od dokumentacji: rozpoznania potrzeb, zaplanowania działań i oceny ich efektywności.",
  f'''<table class="akty"><tr><th style="width:520px">Akt prawny</th><th>Co z tego wynika dla Twojego zapisu celu</th></tr>{akt}</table>
<div class="pom-blok" style="margin-top:20px">
  <div class="et" style="color:var(--pomarancz)">Jak powołać się na przepis w dokumencie — wystarczy jedna linia</div>
  <p style="font-size:19px;line-height:1.55;margin-top:9px"><span class="pp">§ 6 rozporządzenia MEN z 9.08.2017 r. (t.j. Dz.U. 2020 poz. 1309)</span> — przy celach i ewaluacji IPET, oraz <span class="pp">§ 20 rozporządzenia MEN z 9.08.2017 r. (t.j. Dz.U. 2023 poz. 1798)</span> — przy obserwacji pedagogicznej i ocenie efektywności pomocy. Przed oddaniem dokumentacji sprawdź aktualny tekst jednolity w ISAP — pozycje tekstów jednolitych zmieniają się częściej niż same przepisy.</p>
</div>''', styl='''
table.akty{width:100%;border-collapse:collapse}
table.akty th{text-align:left;font-size:11px;letter-spacing:.13em;text-transform:uppercase;color:var(--mute);padding:0 16px 10px;border-bottom:2px solid var(--fiolet)}
table.akty td{padding:12px 16px;vertical-align:top;border-bottom:1px solid var(--linia)}
td.a b{display:block;font-size:16.5px;line-height:1.35;color:var(--fiolet);margin-bottom:4px}
td.a span{font-size:14.5px;color:var(--bursztyn);font-weight:700}
td.w{font-size:16.5px;line-height:1.45;color:var(--atrament)}
td.w b{color:var(--fiolet-cn)}
''', stopka_prawo="Plansza 11 · §10 Podstawa prawna"))

# ------------------------------------------- 10b · CZY SMART JEST OBOWIĄZKOWY
dodaj("10b_czy_obowiazkowe", slajd("10b", "Czy cel SMART jest obowiązkowy?", "§10 · Prawo — pytanie z sali",
  "Sama formuła — nie. Mierzalność celu — w praktyce tak. Różnica jest ważna i warto ją znać przed rozmową z dyrektorem albo kontrolą.",
  '''<div class="dwie">
  <div class="zle-blok">
    <div class="et" style="color:var(--czerwony)">✕ Czego przepisy NIE nakazują</div>
    <ul class="pkt" style="margin-top:14px">
      <li>Słowo <b>„SMART”</b> nie pada w rozporządzeniach regulujących IPET i pomoc psychologiczno-pedagogiczną.</li>
      <li>Żaden przepis nie narzuca formuły zdania ani kolejności siedmiu pól.</li>
      <li>W katalogu z <span class="pp">§ 6 ust. 1</span> rozporządzenia o kształceniu specjalnym
          <b>„cele” nie są wymienione</b> jako odrębny element programu. Katalog obejmuje m.in.:
          zakres i sposób dostosowania programu i wymagań, zintegrowane działania nauczycieli i specjalistów,
          formy i okres pomocy wraz z wymiarem godzin, działania wspierające rodziców, zajęcia rewalidacyjne
          oraz rodzaj i sposób dostosowania warunków organizacji kształcenia.</li>
    </ul>
    <p class="wniosek">Nikt nie zakwestionuje Twojego celu dlatego, że nie ma w nim akronimu.</p>
  </div>
  <div class="ok-blok">
    <div class="et" style="color:var(--zielony)">✓ Co przepisy nakazują — i co z tego wynika</div>
    <ul class="pkt ptaszki" style="margin-top:14px">
      <li><b>Ocena efektywności pomocy.</b> Nauczyciele i specjaliści udzielający pomocy
          <b>oceniają jej efektywność i formułują wnioski</b> dotyczące dalszych działań
          — <span class="pp">§ 20 ust. 9</span> rozp. MEN z 9.08.2017 r. (t.j. Dz.U. 2023 poz. 1798).</li>
      <li><b>Okresowa ocena poziomu funkcjonowania.</b> Zespół <b>co najmniej dwa razy w roku szkolnym</b>
          dokonuje jej, <b>uwzględniając ocenę efektywności programu</b>, i w miarę potrzeb program modyfikuje
          — <span class="pp">§ 6 ust. 9</span> rozp. MEN z 9.08.2017 r. (t.j. Dz.U. 2020 poz. 1309).</li>
      <li><b>Rozpoznanie potrzeb.</b> W przedszkolu — obserwacja pedagogiczna, a w roku poprzedzającym szkołę
          zakończona analizą i oceną gotowości dziecka (diagnoza przedszkolna)
          — <span class="pp">§ 20 ust. 1</span> tego samego rozporządzenia.</li>
      <li><b>Obszar i osiągnięcie.</b> Cel jest uszczegółowieniem wymagania z podstawy programowej
          — <span class="pp">Dz.U. 2026 poz. 378</span>, obowiązuje od 1.09.2026 r.</li>
    </ul>
  </div>
</div>
<div class="pom-blok" style="margin-top:24px">
  <div class="et" style="color:var(--pomarancz)">Sedno — i zdanie, którym można to wyjaśnić dyrektorowi albo wizytatorowi</div>
  <p class="sedno">Przepis nie mówi „napisz cel SMART”. Przepis mówi <b>„oceń efektywność”</b>.
  Efektywności celu bez miary nie da się ocenić — więc miara jest wymuszona <b>funkcjonalnie</b>, choć nie literalnie.
  SMART to nie dodatkowy obowiązek nałożony na Ciebie, tylko najprostsza znana technika wykonania obowiązku, który i tak masz.</p>
</div>''', styl='''
.dwie{display:grid;grid-template-columns:1fr 1fr;gap:34px}
.dwie ul.pkt li{font-size:18px;line-height:1.5;margin-bottom:12px}
.dwie ul.pkt li b{color:var(--fiolet-cn)}
.wniosek{margin-top:14px;padding-top:12px;border-top:1px dashed #E9BDB0;font-size:19px;font-style:italic;color:var(--czerwony)}
.sedno{font-size:23px;line-height:1.5;margin-top:10px;color:var(--atrament)}
.sedno b{color:var(--pomarancz)}
''', stopka_prawo="Plansza 12 · §10 Czy to obowiązkowe"))

# ------------------------------------------ 10c · STARE I NOWE ROZPORZĄDZENIE
dodaj("10c_stare_nowe", slajd("10c", "Stare i nowe rozporządzenie — co się zmieniło 1 września", "§10 · Prawo — zmiana podstawy",
  "Zmienił się adres obszaru, a nie obowiązek mierzalności. To rozróżnienie oszczędza mnóstwo niepotrzebnego przepisywania.",
  '''<div class="dwie" id="porownanie">
  <div class="akt stare">
    <div class="naglowek"><span class="tag">Do 31 sierpnia 2026 r.</span>
      <h3>Rozporządzenie MEN<br>z 14 lutego 2017 r.</h3>
      <div class="dzu">Dz.U. 2017 poz. 356</div></div>
    <div class="et2">Cztery obszary rozwoju</div>
    <div class="chipy stare-chipy"><span>fizyczny</span><span>emocjonalny</span><span>społeczny</span><span>poznawczy</span></div>
    <ul class="pkt">
      <li>Cel odnosił się do <b>obszaru rozwoju dziecka</b>.</li>
      <li>W zakresie wychowania przedszkolnego <b>zastąpione</b> od 1 września 2026 r.</li>
    </ul>
  </div>
  <div class="akt nowe">
    <div class="naglowek"><span class="tag tag-on">Od 1 września 2026 r.</span>
      <h3>Rozporządzenie<br>Ministra Edukacji z 11 marca 2026 r.</h3>
      <div class="dzu">Dz.U. 2026 poz. 378</div></div>
    <div class="et2">Dziewięć obszarów</div>
    <div class="chipy nowe-chipy"><span>społeczny</span><span>osobisty</span><span>językowy</span><span>matematyczny</span><span>przyrodniczy</span><span>techniczny</span><span>cyfrowy</span><span>artystyczny</span><span>ruchowy</span></div>
    <ul class="pkt ptaszki">
      <li>W dokumentacji wskazuj <b>obszar oraz numer osiągnięcia</b> z załącznika.</li>
      <li>To numer osiągnięcia obroni cel przed zespołem i organem nadzoru.</li>
    </ul>
  </div>
</div>
<div class="bez-zmian" id="bezzmian">
  <div class="et2" style="color:var(--zielony)">Czego zmiana NIE ruszyła — to te przepisy, a nie podstawa programowa, wymagają mierzalności</div>
  <div class="trzy">
    <div><b>§ 6</b><span>Rozp. MEN z 9.08.2017 r. o kształceniu specjalnym <i>(t.j. Dz.U. 2020 poz. 1309)</i> — treść IPET oraz okresowa wielospecjalistyczna ocena poziomu funkcjonowania co najmniej dwa razy w roku szkolnym.</span></div>
    <div><b>§ 20 ust. 9</b><span>Rozp. MEN z 9.08.2017 r. o pomocy psychologiczno-pedagogicznej <i>(t.j. Dz.U. 2023 poz. 1798)</i> — ocena efektywności udzielonej pomocy i wnioski do dalszej pracy.</span></div>
    <div class="wniosek-blok"><b>Wniosek</b><span>Nowa podstawa <b>nie ruszyła obowiązku mierzalności</b> — on płynie z tych dwóch rozporządzeń. Zmienił się <b>adres obszaru</b>, do którego cel przypisujesz: z czterech na dziewięć.</span></div>
  </div>
  <p class="ostrzezenie">Numery tekstów jednolitych sprawdź w ISAP przed zacytowaniem — rozporządzenia bywają nowelizowane częściej, niż zmienia się ich treść merytoryczna.</p>
</div>''', styl='''
.dwie{display:grid;grid-template-columns:1fr 1fr;gap:30px}
.akt{background:#fff;border:1px solid var(--linia);border-radius:16px;padding:24px 26px}
.akt.stare{border-top:8px solid var(--faint);opacity:.96}
.akt.nowe{border-top:8px solid var(--pomarancz)}
.naglowek{display:flex;flex-direction:column;gap:8px;margin-bottom:16px}
.tag{align-self:flex-start;font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;
 background:#EFECF6;color:var(--mute);border-radius:999px;padding:6px 14px}
.tag-on{background:#FFE4D8;color:var(--pomarancz)}
.akt h3{font-size:26px;line-height:1.2;color:var(--fiolet)}
.dzu{font-size:17px;font-weight:700;color:var(--bursztyn)}
.et2{font-size:11.5px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--mute);margin:14px 0 9px}
.chipy{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:14px}
.chipy span{font-size:17px;font-weight:700;border-radius:999px;padding:7px 15px}
.stare-chipy span{background:#F1EFF7;color:var(--mute);border:1px solid var(--linia)}
.nowe-chipy span{background:#FFF6F2;color:var(--pomarancz);border:1px solid #F3C9B6}
.dwie ul.pkt li{font-size:17.5px;line-height:1.45;margin-bottom:7px}
.dwie ul.pkt li b{color:var(--fiolet-cn)}
.ostrzezenie{margin-top:13px;padding-top:11px;border-top:1px dashed #A9D8C4;font-size:15.5px;line-height:1.45;color:var(--mute)}
.bez-zmian{margin-top:26px;background:#F1F8F4;border:2px solid #A9D8C4;border-left:10px solid var(--zielony);
 border-radius:14px;padding:20px 26px}
.trzy{display:grid;grid-template-columns:1fr 1fr 1fr;gap:22px;margin-top:6px}
.trzy div b{display:block;font-size:24px;color:var(--zielony);margin-bottom:6px}
.trzy div span{font-size:16.5px;line-height:1.45;color:var(--atrament)}
.trzy div span i{color:var(--bursztyn);font-style:normal;font-weight:700}
.wniosek-blok b{color:var(--pomarancz)!important}
.wniosek-blok span b{display:inline;font-size:inherit;color:var(--fiolet-cn)!important}
''', stopka_prawo="Plansza 12b · §10 Stare i nowe rozporządzenie"))

# ---------------------------------------------- 11 · SKĄD SIĘ WZIĄŁ TEN POMYSŁ
ZR = [("1981","G. T. Doran","„There's a S.M.A.R.T. way to write management's goals and objectives”, <i>Management Review</i> 70(11), s. 35–36",
   "Pierwsze użycie skrótu SMART. U Dorana <b>A</b> = <i>assignable</i> (przypisany komuś), <b>R</b> = <i>realistic</i> (realny przy danych zasobach). Doran od razu zastrzegł, że nie każdy cel musi spełniać wszystkie pięć kryteriów — SMART to lista kontrolna, nie gorset."),
 ("1962","R. F. Mager","<i>Preparing Instructional Objectives</i>, Fearon, Palo Alto",
   "Źródło pedagogiczne formuły. Mager pokazał, że cel dydaktyczny musi mieć trzy części: <b>zachowanie</b> (co uczący się zrobi), <b>warunki</b> i <b>kryterium</b>. To dokładnie pola 3, 4, 5 i 7 formuły z §4."),
 ("1968","T. Kiresuk, R. Sherman","„Goal Attainment Scaling”, <i>Community Mental Health Journal</i> 4, s. 443–453",
   "Skalowanie osiągania celu: dla każdego celu ustala się <b>z góry</b> skalę wyników, zanim zacznie się praca. Stąd bierze się logika „zielony – żółty – czerwony” z §8: próg sukcesu ustalasz przed startem, nie po fakcie."),
 ("2002","E. Locke, G. Latham","„Building a Practically Useful Theory of Goal Setting and Task Motivation”, <i>American Psychologist</i> 57(9), s. 705–717",
   "Podsumowanie 35 lat badań: cele <b>konkretne i trudne</b> dają wyraźnie lepsze wyniki niż zachęta „postaraj się najlepiej, jak umiesz”. To empiryczna odpowiedź na pytanie, dlaczego „będzie spokojniejsze” nie działa."),
 ("2007","WHO","<i>ICF-CY — Międzynarodowa Klasyfikacja Funkcjonowania, Niepełnosprawności i Zdrowia: wersja dla dzieci i młodzieży</i>",
   "Wspólny język opisu funkcjonowania. Kod <span class='icf'>b1521</span> to <b>regulacja emocji</b> — dlatego cel „Termometru napięcia” da się jednoznacznie przypisać do sfery, którą rozumie logopeda, psycholog i lekarz."),
 ("2004→","IDEA, USA","<i>Individuals with Disabilities Education Act</i>, 34 CFR § 300.320(a)(2)–(3)",
   "Amerykański odpowiednik IPET-u wymaga w programie <b>mierzalnych celów rocznych</b> oraz opisu, <b>jak</b> postęp będzie mierzony i kiedy raportowany. Cel uznaje się za mierzalny, gdy ma cztery elementy: termin, warunki, zachowanie i kryterium — ten sam zestaw, co w naszej formule.")]
zr = "".join(f'''<div class="z"><div class="rok">{r}</div><div class="tre"><b>{a}</b><div class="tyt">{t}</div><p>{o}</p></div></div>''' for r,a,t,o in ZR)
dodaj("11_zrodla", slajd("11", "Skąd się wzięły te cele — i skąd ten pomysł", "Źródła · Zaplecze merytoryczne",
  "SMART w przedszkolu nie spadło z nieba. Ma cztery korzenie: zarządzanie, dydaktykę, psychologię motywacji i klasyfikację funkcjonowania.",
  f'<div class="zrodla">{zr}</div>', styl='''
.zrodla{display:grid;grid-template-columns:1fr 1fr;gap:18px 30px;height:100%}
.z{display:flex;gap:20px;align-items:flex-start;background:#fff;border:1px solid var(--linia);border-left:6px solid var(--pomarancz);border-radius:14px;padding:20px 24px}
.rok{flex:0 0 96px;font-size:32px;font-weight:700;color:var(--pomarancz);letter-spacing:-.02em;padding-top:1px}
.tre>b{font-size:23px;color:var(--fiolet)}
.tyt{font-size:17px;line-height:1.4;color:var(--mute);margin:3px 0 9px}
.tre p{font-size:18.5px;line-height:1.48;color:var(--atrament)}
.tre p b{font-size:inherit;color:var(--fiolet-cn)}
''', stopka_prawo="Plansza 13 · Zaplecze merytoryczne"))

# ------------------------------------------------------- 12 · DLACZEGO TERAZ
dodaj("12_dlaczego_teraz", slajd("12", "Dlaczego akurat teraz", "Uzasadnienie · Wrzesień 2026",
  "Trzy rzeczy zbiegły się w jednym miesiącu — i wszystkie trzy dotyczą zapisu celu.",
  '''<div class="powody">
  <div class="p"><div class="ikona">1</div><h3>Nowa podstawa weszła w życie 1 września 2026 r.</h3>
    <p>Osiągnięcia dziecka opisuje się teraz w <b>dziewięciu obszarach</b> zamiast czterech (Dz.U. 2026 poz. 378). Cele napisane w starym układzie nie wskażą właściwego obszaru ani numeru osiągnięcia — a to on obroni cel przed zespołem i organem nadzoru.</p></div>
  <div class="p"><div class="ikona">2</div><h3>Wrzesień to miesiąc, w którym zapada zapis na cały rok</h3>
    <p>Programy dla dzieci z orzeczeniami powstają na początku roku szkolnego, a obserwacja wstępna trwa właśnie teraz. <b>Cel wpisany źle we wrześniu jest kopiowany przez dwanaście miesięcy</b> — do arkuszy, do dziennika, do rozmów z rodzicami.</p></div>
  <div class="p"><div class="ikona">3</div><h3>Ocena efektywności to obowiązek, nie dobra wola</h3>
    <p>Zespół <b>co najmniej dwa razy w roku</b> ocenia poziom funkcjonowania i skuteczność programu. Pierwszy przegląd wypadnie w styczniu. Do stycznia zdąży policzyć się tylko to, co ma miarę wpisaną dziś.</p></div>
</div>
<div class="dwa-doly">
  <div class="ok-blok"><div class="et" style="color:var(--zielony)">Co zyskujesz, pisząc cel z miarą</div>
    <ul class="pkt ptaszki" style="margin-top:12px">
      <li>Wiesz, co robić w poniedziałek rano — cel sam podpowiada działanie.</li>
      <li>Rodzic słyszy konkret zamiast „pracujemy nad emocjami”.</li>
      <li>Ewaluacja pisze się sama: liczba, warunki, wniosek.</li>
      <li>Zastępstwo nie oznacza przerwy w terapii.</li></ul></div>
  <div class="zle-blok"><div class="et" style="color:var(--czerwony)">Co kosztuje cel bez miary</div>
    <ul class="pkt" style="margin-top:12px">
      <li>W styczniu nie ma czego ocenić — wpisujesz „częściowo osiągnięty”.</li>
      <li>Kontrola pyta o dowód, a dowodu nie ma.</li>
      <li>Dziecko przez pół roku pracuje nad czymś, czego nikt nie zmierzył.</li>
      <li>Ten sam cel wraca w kolejnym IPET-cie, bo nie wiadomo, czy zadziałał.</li></ul></div>
</div>''', styl='''
.powody{display:grid;grid-template-columns:repeat(3,1fr);gap:26px;margin-bottom:26px}
.p{background:#fff;border:1px solid var(--linia);border-top:7px solid var(--pomarancz);border-radius:16px;padding:22px 24px}
.ikona{width:46px;height:46px;border-radius:12px;background:var(--fiolet);color:#fff;display:flex;align-items:center;justify-content:center;font-size:23px;font-weight:700;margin-bottom:14px}
.p h3{font-size:23px;line-height:1.25;color:var(--fiolet);margin-bottom:10px}
.p p{font-size:18px;line-height:1.5;color:var(--mute)}
.p p b{color:var(--fiolet-cn)}
.dwa-doly{display:grid;grid-template-columns:1fr 1fr;gap:26px}
.dwa-doly ul.pkt li{font-size:18px;margin-bottom:6px}
''', stopka_prawo="Plansza 14 · Uzasadnienie"))

# ------------------------------------------------------------- 13 · FINAŁ
dodaj("13_final", slajd("13", "", "", "", '''
<div class="fin">
  <div>
    <div class="fin-nad">EduPlaner 2026 · PCTP Koszalin</div>
    <h1 class="fin-h">Mniej dokumentów.<br>Więcej edukacji.</h1>
    <p class="fin-lead">Jedno zdanie z miarą zastępuje pół strony ogólników — i jako jedyne przechodzi przez ewaluację.</p>
    <div class="fin-kroki">
      <div><b>Dziś</b>weź jeden cel z bieżącej dokumentacji i przepisz go formułą z §4.</div>
      <div><b>Do piątku</b>zmierz punkt wyjścia u jednego dziecka — pięć sytuacji, pięć kresek.</div>
      <div><b>Za 8 tygodni</b>usiądź z kartą obserwacji i sprawdź: zielony, żółty czy czerwony.</div>
    </div>
  </div>
  <div class="fin-kontakt">
    <div class="et" style="color:var(--pomarancz)">Baza celów SMART w aplikacji</div>
    <p class="fin-op">W EduPlanerze 2026 powstaje biblioteka gotowych celów SMART — uporządkowanych według sfer rozwoju, poziomów wsparcia i kodów ICF. Wybierasz cel, dopasowujesz miarę i termin. Baza rośnie razem ze społecznością — Twoje sprawdzone cele też mogą do niej trafić.</p>
    <div class="fin-dane">
      <div><span>Strona</span>www.eduplaner2026.pl</div>
      <div><span>E-mail</span>kontakt@eduplaner2026.pl</div>
      <div><span>Telefon</span>662 888 403</div>
      <div><span>Opracowanie</span>pedagog specjalny<br>mgr Mirosława Ewa Jurczyszyn</div>
    </div>
    <div class="fin-sygn">Materiał szkoleniowy do broszury „Cele SMART w przedszkolu”, sygn. SMART-P1 · przykład przewodni: konspekt TUE-1 „Termometr napięcia”, ICF b1521 · stan prawny 28 sierpnia 2026 r.</div>
  </div>
</div>''', styl='''
.fin{display:grid;grid-template-columns:1fr 700px;gap:70px;height:100%;align-items:center;padding-bottom:20px}
.fin-nad{font-size:16px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--pomarancz);margin-bottom:22px}
.fin-h{font-size:82px;line-height:1.03;color:#fff;letter-spacing:-.03em}
.fin-lead{font-size:26px;line-height:1.45;color:#D6CFEE;margin-top:26px;max-width:860px}
.fin-kroki{margin-top:38px;display:grid;gap:14px;max-width:880px}
.fin-kroki div{background:rgba(255,255,255,.09);border-left:5px solid var(--pomarancz);border-radius:0 12px 12px 0;padding:15px 20px;font-size:21px;color:#fff}
.fin-kroki b{display:block;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--pomarancz);margin-bottom:5px}
.fin-kontakt{background:#fff;border-radius:20px;padding:32px 36px}
.fin-op{font-size:18px;line-height:1.55;color:var(--mute);margin-top:12px}
.fin-dane{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:24px}
.fin-dane div{font-size:20px;font-weight:700;color:var(--fiolet);line-height:1.35}
.fin-dane span{display:block;font-size:10.5px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--faint);margin-bottom:4px}
.fin-sygn{margin-top:26px;padding-top:16px;border-top:1px solid var(--linia);font-size:14px;line-height:1.55;color:var(--faint)}
''', klasa="ciemny", stopka_prawo="Plansza 15 · Finał"))

# --------------------------------------- 14 · KONSPEKT TUE-1 (A4, „zdjęcie”)
KONSPEKT = '''<!doctype html><html lang="pl"><head><meta charset="utf-8">
<title>Konspekt TUE-1 Termometr napięcia</title><link rel="stylesheet" href="wspolne.css">
<style>
body.a4{background:#fff}
.ark{padding:44px 56px 30px}
.gl{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:3px solid var(--fiolet);padding-bottom:13px;margin-bottom:20px}
.gl h1{font-size:29px;color:var(--fiolet);letter-spacing:-.01em}
.gl .sub{font-size:13.5px;color:var(--mute);margin-top:5px}
.gl .znak{text-align:right;font-size:11.5px;color:var(--mute);line-height:1.5}
.gl .znak b{color:var(--pomarancz);font-size:13.5px;display:block;letter-spacing:.09em}
.meta{display:grid;grid-template-columns:repeat(4,1fr);border:1px solid var(--linia);border-radius:10px;overflow:hidden;margin-bottom:18px}
.meta div{padding:10px 13px;border-right:1px solid var(--linia);background:var(--papier-lt)}
.meta div:last-child{border-right:none}
.meta label{display:block;font-size:9.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--mute);margin-bottom:3px}
.meta span{font-size:14px;font-weight:700;color:var(--fiolet)}
h2.sek{font-size:12px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--fiolet);margin:18px 0 8px;display:flex;align-items:center;gap:9px}
h2.sek::before{content:"";width:15px;height:3px;background:var(--pomarancz)}
.cel{border:2px solid var(--pomarancz);border-left:10px solid var(--pomarancz);border-radius:11px;background:#FFF6F2;padding:15px 19px}
.cel .nag{font-size:10px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--pomarancz);margin-bottom:7px}
.cel p{font-size:17.5px;line-height:1.45;font-weight:700;color:var(--fiolet-cn)}
.cel .rozbior{display:grid;grid-template-columns:repeat(5,1fr);gap:7px;margin-top:12px}
.cel .rozbior div{background:#fff;border:1px solid #F3C9B6;border-radius:7px;padding:7px 8px}
.cel .rozbior b{display:block;font-size:15px;color:var(--pomarancz);line-height:1}
.cel .rozbior span{font-size:9.5px;color:var(--mute);line-height:1.35;display:block;margin-top:3px}
ul.pkt2{list-style:none}
ul.pkt2 li{font-size:13.5px;line-height:1.55;padding-left:19px;position:relative;margin-bottom:2px}
ul.pkt2 li::before{content:"▸";position:absolute;left:0;color:var(--pomarancz);font-weight:700}
ul.pkt2.zi li::before{content:"✓";color:var(--zielony)}
.kol2{display:grid;grid-template-columns:1fr 1fr;gap:24px}
.kol3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}
table.t{width:100%;border-collapse:collapse;font-size:12.5px}
table.t th{background:var(--fiolet);color:#fff;text-align:left;padding:8px 11px;font-size:10px;letter-spacing:.08em;text-transform:uppercase}
table.t td{border:1px solid var(--linia);padding:8px 11px;vertical-align:top;line-height:1.45}
table.t.karta td{height:26px}
table.t.karta tr:nth-child(even) td{background:#fff}
table.t.karta tr td:not(.et2){background:var(--papier-lt)}
table.t tr:nth-child(even) td{background:var(--papier-lt)}
table.t td.et2{font-weight:700;color:var(--fiolet);white-space:nowrap}
.pozLvl{border:1px solid var(--linia);border-radius:9px;padding:10px 12px;background:var(--papier-lt)}
.pozLvl b{display:block;font-size:11px;letter-spacing:.09em;text-transform:uppercase;color:var(--pomarancz);margin-bottom:4px}
.pozLvl span{font-size:12.5px;line-height:1.45;color:var(--atrament)}
.wsk{border:1px solid var(--linia);border-left:7px solid var(--zielony);border-radius:9px;background:#F1F8F4;padding:12px 16px;font-size:13.5px;line-height:1.6}
.wsk b{color:var(--zielony)}
.kreski{display:flex;align-items:center;gap:8px;margin-top:8px}
.kreski span{width:34px;height:34px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:17px;font-weight:700;border:2px solid var(--linia);background:#fff}
.kreski .p{color:var(--zielony);border-color:#A9D8C4}
.kreski .m{color:var(--faint)}
.kreski b{margin-left:6px;font-size:13.5px;color:var(--zielony)}
.ppb{margin-top:16px;border-top:1px solid var(--linia);padding-top:11px;font-size:10.5px;line-height:1.7;color:var(--mute)}
.ppb b{color:var(--bursztyn)}
.stopka2{margin-top:14px;border-top:1px solid var(--linia);padding-top:9px;display:flex;justify-content:space-between;font-size:10.5px;color:var(--faint)}
</style></head><body class="a4">
<div class="pasek"></div>
<div class="ark">
  <div class="gl">
    <div><h1>Konspekt zajęć · TUE-1 „Termometr napięcia”</h1>
      <div class="sub">Załącznik do IPET · sfera integracji społeczno-emocjonalnej i samoregulacji</div></div>
    <div class="znak"><b>PCTP KOSZALIN</b>EduPlaner 2026 · SMART-P1<br>Cele SMART w przedszkolu</div>
  </div>
  <div class="meta">
    <div><label>Grupa</label><span>„Motylki” · 5-latki</span></div>
    <div><label>Data zajęć</label><span>14.10.2026 r.</span></div>
    <div><label>Czas</label><span>30 minut + praca ciągła</span></div>
    <div><label>Prowadząca</label><span>mgr A. Nowak</span></div>
  </div>

  <h2 class="sek">Obszar podstawy programowej i kod ICF</h2>
  <ul class="pkt2"><li><b>Obszar osobisty</b> — tożsamość, emocje, granice (podstawa programowa wychowania przedszkolnego obowiązująca od 1.09.2026 r.). Sfera integracji społeczno-emocjonalnej i samoregulacji. <span class="icf">ICF: b1521 — regulacja emocji</span></li></ul>

  <h2 class="sek">Cel zajęć zapisany formułą SMART</h2>
  <div class="cel">
    <div class="nag">Cel · ten sam zapis w konspekcie, w karcie obserwacji i w sekcji III IPET</div>
    <p>Dziecko w sytuacjach trudnych w sali i w ogrodzie samodzielnie, bez podpowiedzi słownej dorosłego, rozpozna narastające napięcie na termometrze i zastosuje strategię wyciszenia (oddech 4-4-4) w 4 na 5 obserwowanych sytuacji, do końca I semestru, co potwierdzi zapis w karcie obserwacji.</p>
    <div class="rozbior">
      <div><b>S</b><span>rozpozna na termometrze · zastosuje oddech — obie czynności widać</span></div>
      <div><b>M</b><span>4 na 5 sytuacji trudnych, jedna kreska = jedna sytuacja</span></div>
      <div><b>A</b><span>punkt wyjścia 1/5 z podpowiedzią → kryterium 4/5</span></div>
      <div><b>R</b><span>samoregulacja = warunek udziału w zabawie i posiłku</span></div>
      <div><b>T</b><span>koniec I semestru, przegląd po 8 tygodniach</span></div>
    </div>
  </div>

  <div class="kol2" style="margin-top:18px">
    <div>
      <h2 class="sek">Cele operacyjne — dziecko:</h2>
      <ul class="pkt2 zi">
        <li>wskaże na termometrze poziom odpowiadający swojemu napięciu,</li>
        <li>nazwie strefę kolorem (zielona / żółta / czerwona),</li>
        <li>wykona oddech 4-4-4 według wzoru z planszy,</li>
        <li>zgłosi potrzebę przerwy umówionym zdaniem, zanim wejdzie w strefę czerwoną.</li>
      </ul>
      <h2 class="sek">Metody i formy</h2>
      <ul class="pkt2">
        <li>plansza termometru jako pomoc i jednocześnie narzędzie pomiaru,</li>
        <li>modelowanie oddechu przez dorosłego, próba z podpowiedzią, próba samodzielna,</li>
        <li>formy: indywidualna → w parze z dorosłym → w sytuacji naturalnej w grupie.</li>
      </ul>
    </div>
    <div>
      <h2 class="sek">Modyfikacja dla poziomów wsparcia</h2>
      <div class="kol3">
        <div class="pozLvl"><b>Poziom I</b><span>Zapis bazowy: samodzielnie, 4 na 5 sytuacji.</span></div>
        <div class="pozLvl"><b>Poziom II</b><span>Dopuszczalna jedna podpowiedź gestem; kryterium 3 na 5.</span></div>
        <div class="pozLvl"><b>Poziom III</b><span>Wspólne wskazanie z dorosłym; kryterium 2 na 5, praca 1:1.</span></div>
      </div>
      <h2 class="sek">Środki dydaktyczne</h2>
      <ul class="pkt2"><li>plansza „Termometr napięcia 1–6”, karta obserwacji, karta „Potrzebuję przerwy”, plansza oddechu 4-4-4.</li></ul>
    </div>
  </div>

  <h2 class="sek">Przebieg zajęć</h2>
  <table class="t">
    <tr><th style="width:145px">Etap</th><th style="width:66px">Czas</th><th>Czynności nauczyciela i dzieci</th></tr>
    <tr><td class="et2">Wprowadzenie</td><td>5 min</td><td>Zabawa „Jak dziś świeci mój termometr?” — każde dziecko wskazuje poziom. Nauczyciel nazywa strefy kolorem, bez oceniania.</td></tr>
    <tr><td class="et2">Część główna</td><td>20 min</td><td>Modelowanie oddechu 4-4-4. Scenki sytuacji trudnych (przegrana, hałas, czekanie na swoją kolej) — dziecko wskazuje poziom i wybiera strategię. Nauczyciel stawia kreskę na karcie obserwacji przy próbach samodzielnych.</td></tr>
    <tr><td class="et2">Zakończenie</td><td>5 min</td><td>Termometr zostaje na ścianie na wysokości oczu dzieci. Umowa: wracamy do niego w realnych sytuacjach przez cały dzień — dlatego dane zbierają się same.</td></tr>
  </table>

  <div class="kol2" style="margin-top:16px">
    <div>
      <h2 class="sek">Jak sprawdzę, czy cel został osiągnięty</h2>
      <div class="wsk">
        <b>Wskaźnik:</b> w ilu z 5 kolejnych sytuacji trudnych w tygodniu dziecko samodzielnie rozpoznało poziom i użyło strategii.<br>
        <b>Narzędzie:</b> karta obserwacji — jedna kreska = jedna sytuacja.<br>
        <b>Punkt kontrolny:</b> po 8 tygodniach · <b>Podsumowanie:</b> koniec I semestru.
        <div class="kreski"><span class="p">✓</span><span class="p">✓</span><span class="m">–</span><span class="p">✓</span><span class="p">✓</span><b>4 / 5 → kryterium spełnione</b></div>
      </div>
    </div>
    <div>
      <h2 class="sek">Decyzja po punkcie kontrolnym (§8 broszury)</h2>
      <table class="t">
        <tr><th style="width:96px">Wynik</th><th>Co robię z celem</th></tr>
        <tr><td class="et2" style="color:var(--zielony)">4–5 / 5</td><td>Cel osiągnięty — zapisuję z liczbą, przechodzę do generalizacji (inne miejsce, inna osoba dorosła).</td></tr>
        <tr><td class="et2" style="color:var(--zolty)">2–3 / 5</td><td>Cel zostaje — zmieniam drogę: mniejszy krok, podpowiedź, więcej prób.</td></tr>
        <tr><td class="et2" style="color:var(--czerwony)">0–1 / 5</td><td>Cofam cel o etap, upraszczam zadanie, weryfikuję poziom wsparcia i sam zapis celu.</td></tr>
      </table>
    </div>
  </div>


  <h2 class="sek">Karta obserwacji do wydruku — jedna kreska = jedna sytuacja trudna</h2>
  <table class="t karta">
    <tr><th style="width:150px">Tydzień</th><th>Sytuacja 1</th><th>Sytuacja 2</th><th>Sytuacja 3</th><th>Sytuacja 4</th><th>Sytuacja 5</th><th style="width:96px">Wynik</th><th style="width:150px">Uwagi</th></tr>
    <tr><td class="et2">1 (14–18.10)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td class="et2">2 (21–25.10)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td class="et2">3 (28.10–01.11)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td class="et2">4 (04–08.11)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td class="et2">…</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td class="et2">8 — punkt kontrolny</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  </table>
  <p style="font-size:11.5px;color:var(--mute);margin-top:7px">Zaznaczasz tylko jedno: czy dziecko <b>samodzielnie</b> rozpoznało poziom na termometrze i użyło strategii (✓), czy nie (–). Sumę z tygodnia wpisujesz w kolumnie „Wynik” jako <b>x / 5</b>.</p>

  <div class="ppb">
    <b>Podstawa prawna:</b> § 6 rozporządzenia MEN z 9.08.2017 r. w sprawie warunków organizowania kształcenia, wychowania i opieki dla dzieci i młodzieży niepełnosprawnych… (t.j. Dz.U. 2020 poz. 1309) — cele IPET, zintegrowane działania, okresowa wielospecjalistyczna ocena poziomu funkcjonowania co najmniej dwa razy w roku szkolnym · § 6 i § 20 rozporządzenia MEN z 9.08.2017 r. w sprawie zasad organizacji i udzielania pomocy psychologiczno-pedagogicznej (t.j. Dz.U. 2023 poz. 1798) — obserwacja pedagogiczna i ocena efektywności udzielanej pomocy · rozporządzenie Ministra Edukacji z 11.03.2026 r. w sprawie podstawy programowej wychowania przedszkolnego (Dz.U. 2026 poz. 378), obowiązujące od 1.09.2026 r. — obszar osobisty.
  </div>
  <div class="stopka2"><span>EduPlaner 2026 · PCTP Koszalin · materiał szkoleniowy do broszury SMART-P1</span><span>Plansza 16 · Konspekt TUE-1 (format A4)</span></div>
</div></body></html>'''
dodaj("14_konspekt_tue1", KONSPEKT, 1240, 1754)

# ------------------------------------------------------------------ RENDER
def main():
    tylko_html = "--tylko-html" in sys.argv
    for nazwa, html, w, h in PLANSZE:
        (KAT / f"{nazwa}.html").write_text(html, encoding="utf-8")
        if tylko_html:
            print(f"HTML  {nazwa}.html"); continue
        subprocess.run([CHROM, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
                        f"--window-size={w},{h}", f"--screenshot={KAT / (nazwa + '.png')}",
                        f"file://{KAT / (nazwa + '.html')}"],
                       check=True, capture_output=True)
        print(f"PNG   {nazwa}.png  ({w}×{h})")
    print(f"\nGotowe: {len(PLANSZE)} plansz w {KAT}")

if __name__ == "__main__":
    main()
