# -*- coding: utf-8 -*-
"""
Strona sprzedażowa zeszytu „Kolorowy Świat Emocji" — do wklejenia
na www.eduplaner2026.pl.

Uruchom:  python3 sprzedaz/generuj_oferte.py
Powstanie: sprzedaz/oferta.html (samowystarczalna, ze zdjęciami w środku)

Ceny i warunki licencji zmieniasz w słowniku LICENCJE poniżej.
"""
import os
import sys
import html

BAZA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BAZA)
sys.path.insert(0, os.path.join(os.path.dirname(BAZA), "broszura"))
from fonty import CSS_FONTY         # noqa: E402

# ── zdjęcia ──────────────────────────────────────────────────────────────────
# Bierzemy je z katalogu broszury i osadzamy w pliku, żeby stronę dało się
# wysłać albo wgrać jednym plikiem. Plik pośredni budujemy, gdy go brakuje.
POTRZEBNE = ["okladka", "01-cialo", "02-cialo", "04-cialo", "05-cialo",
             "01-otwarcie", "wstep-poznaj", "koniec", "c2-zielony",
             "c2-pomaranczowy", "c2-fioletowy", "c2-bialy", "c2-brazowy",
             "c2-czarny"]


def _zbierz_zdjecia():
    import base64
    zrodlo = os.path.join(os.path.dirname(BAZA), "broszura", "zdjecia-gotowe")
    dane = {}
    for nazwa in POTRZEBNE:
        sciezka = os.path.join(zrodlo, nazwa + ".jpg")
        if os.path.exists(sciezka):
            with open(sciezka, "rb") as f:
                dane[nazwa] = ("data:image/jpeg;base64,"
                               + base64.b64encode(f.read()).decode("ascii"))
    with open(os.path.join(BAZA, "_zdjecia.py"), "w", encoding="utf-8") as f:
        f.write("# generowane automatycznie przez generuj_oferte.py\nZDJ = ")
        f.write(repr(dane))
    return dane


try:
    from _zdjecia import ZDJ       # noqa: E402
except ImportError:
    ZDJ = _zbierz_zdjecia()


def e(t):
    return html.escape(str(t), quote=False)


def foto(nazwa, alt="", klasa=""):
    if nazwa not in ZDJ:
        return ""
    return f'<img class="{klasa}" src="{ZDJ[nazwa]}" alt="{e(alt)}" decoding="async">'


FIRMA = {
    "nazwa": "Pomorskie Centrum Terapii Pedagogicznej",
    "skrot": "PCTP",
    "miasto": "Koszalin",
    "autorka": "Mirosława Ewa Jurczyszyn",
    "funkcja": "pedagog specjalny",
    "email": "kontakt@eduplaner2026.pl",
    "telefon": "[usunięto]",
    "www": "www.eduplaner2026.pl",
}

# ── Licencje — ceny uzupełnij przed publikacją ───────────────────────────────
LICENCJE = [
    {
        "nazwa": "Licencja indywidualna",
        "dla": "Dla jednego specjalisty",
        "cena": "[ cena ]",
        "zakres": [
            "Plik PDF do pobrania — 58 stron.",
            "Wydruk dla własnych uczniów i podopiecznych, bez limitu kopii.",
            "Praca indywidualna i w małej grupie.",
            "Dożywotni dostęp do zakupionego wydania.",
        ],
        "polecana": False,
    },
    {
        "nazwa": "Licencja placówkowa",
        "dla": "Dla całej szkoły, przedszkola lub poradni",
        "cena": "[ cena ]",
        "zakres": [
            "Wszystko z licencji indywidualnej.",
            "Korzystanie przez wszystkich specjalistów w jednej placówce.",
            "Wydruki dla wszystkich uczniów tej placówki.",
            "Plik w wewnętrznej sieci placówki.",
        ],
        "polecana": True,
    },
    {
        "nazwa": "Licencja szkoleniowa",
        "dla": "Dla prowadzących szkolenia i warsztaty",
        "cena": "[ cena ]",
        "zakres": [
            "Wszystko z licencji placówkowej.",
            "Pokazywanie stron zeszytu podczas szkoleń i webinarów.",
            "Materiały ćwiczeniowe dla uczestników szkolenia.",
            "Wymagane podanie autorki i wydawcy.",
        ],
        "polecana": False,
    },
]

LICENCJA_ZASADY = [
    ("Wolno", [
        "Drukować dowolną liczbę egzemplarzy w zakresie swojej licencji.",
        "Wypełniać, kopiować pojedyncze strony i karty do zajęć.",
        "Wycinać karty do gry i karty emocji.",
        "Pokazywać zeszyt rodzicom uczniów, z którymi pracujesz.",
    ]),
    ("Nie wolno", [
        "Odsprzedawać zeszytu ani jego fragmentów.",
        "Udostępniać pliku PDF poza swoją licencją.",
        "Publikować stron w internecie i w mediach społecznościowych.",
        "Usuwać oznaczeń autorki i wydawcy.",
    ]),
]

CO_W_SRODKU = [
    ("5 rozdziałów", "Radość, smutek, złość, wstyd i lęk — każdy w swoim kolorze "
                     "i zawsze w tym samym układzie ośmiu stron."),
    ("40 pytań do pracy", "Po osiem pytań do każdego opowiadania, z liniami "
                          "do zapisania odpowiedzi."),
    ("45 zadań", "Na trzech poziomach trudności — od pięciominutowych "
                 "po projekty na kilka dni."),
    ("Gra planszowa", "\u201eŚcieżka Kolorów\u201d dla 2\u20134 osób: plansza, "
                      "zasady i 24 karty do wycięcia."),
    ("Karty emocji", "Sześć kart z twarzami — pomoc komunikacyjna na chwile, "
                     "gdy trudno powiedzieć słowami."),
    ("Materiały dla dorosłego", "Instrukcja towarzyszenia, pytania na start "
                                "i wskazówki, kiedy szukać wsparcia specjalisty."),
]

GDZIE = [
    "Zajęcia rewalidacyjne",
    "Pomoc psychologiczno-pedagogiczna",
    "Terapia indywidualna",
    "Praca w małej grupie",
    "Praca w domu z rodzicem",
]

CZESC_2 = [
    ("c2-zielony", "Spokój", "zielony", "#3F8F5B", "#FFFFFF"),
    ("c2-pomaranczowy", "Ekscytacja", "pomarańczowy", "#E8721C", "#2B1400"),
    ("c2-fioletowy", "Duma", "fioletowy", "#6B4BA8", "#FFFFFF"),
    ("c2-bialy", "Ulga", "biały", "#F1EEE8", "#2B2B2E"),
    ("c2-brazowy", "Znudzenie", "brązowy", "#7A5A3A", "#FFFFFF"),
    ("c2-czarny", "Samotność", "czarny", "#2B2B2E", "#FFFFFF"),
]

KOLORY_1 = [
    ("01-cialo", "Radość", "żółty", "#F2B21A", "#3D2800"),
    ("02-cialo", "Smutek", "niebieski", "#2E6FB7", "#FFFFFF"),
    ("04-cialo", "Wstyd", "różowy", "#E0619B", "#3F0B25"),
    ("05-cialo", "Lęk", "szary", "#6E7681", "#FFFFFF"),
]

LOGO = (
    '<svg class="logo" viewBox="0 0 600 600" role="img" aria-label="PCTP">'
    '<circle cx="300" cy="300" r="298" fill="#3E2664"/>'
    '<circle cx="300" cy="300" r="288" fill="#CFC4E4"/>'
    '<circle cx="300" cy="300" r="274" fill="#3E2664"/>'
    '<circle cx="300" cy="300" r="268" fill="#4B3079"/>'
    '<g stroke="#C8A02A" stroke-width="10" stroke-linecap="round" fill="none">'
    '<path d="M300 276 L300 234"/>'
    '<path d="M300 272 C286 246 264 232 240 220"/>'
    '<path d="M300 272 C314 246 336 232 360 220"/></g>'
    '<ellipse cx="300" cy="166" rx="22" ry="47" fill="#A292CE" '
    'transform="rotate(-46 300 250)"/>'
    '<ellipse cx="300" cy="166" rx="22" ry="47" fill="#A292CE" '
    'transform="rotate(46 300 250)"/>'
    '<ellipse cx="300" cy="158" rx="23" ry="51" fill="#F0A97A" '
    'transform="rotate(-21 300 250)"/>'
    '<ellipse cx="300" cy="158" rx="23" ry="51" fill="#F0A97A" '
    'transform="rotate(21 300 250)"/>'
    '<ellipse cx="300" cy="150" rx="24" ry="55" fill="#E8722E"/>'
    '<circle cx="300" cy="178" r="13" fill="#FFFFFF"/></svg>'
)


CSS = """
:root{
  --fiolet:#2D1B69; --fiolet-ciemny:#1a0f42; --fiolet-jasny:#EFEBF8;
  --pomarancz:#E8450A; --pomarancz-cieply:#F0A97A;
  --papier:#FFFFFF; --tlo:#F7F5F1;
  --atrament:#241F2E; --atrament-2:#57506A; --atrament-3:#8B8399;
  --wlos:#E5E0EA;
  --font-h:"Nunito","Trebuchet MS",sans-serif;
  --font-t:"Atkinson Hyperlegible","Verdana",sans-serif;
  --maks:1120px;
}
*{box-sizing:border-box}
body{margin:0;background:var(--papier);color:var(--atrament);
  font-family:var(--font-t);font-size:17px;line-height:1.65;
  -webkit-font-smoothing:antialiased}
img{max-width:100%;display:block}
p{margin:0}
h1,h2,h3{font-family:var(--font-h);margin:0;text-wrap:balance}
a{color:inherit}

.wrap{max-width:var(--maks);margin:0 auto;padding:0 24px}
section{padding:64px 0}
.tlo{background:var(--tlo)}
.eyebrow{font-family:var(--font-h);font-weight:800;font-size:13px;
  letter-spacing:.18em;text-transform:uppercase;color:var(--pomarancz)}
h2{font-weight:900;font-size:clamp(28px,4vw,40px);line-height:1.12;
  letter-spacing:-.01em;margin:10px 0 0}
.lead{font-size:clamp(17px,2vw,20px);line-height:1.6;color:var(--atrament-2);
  max-width:62ch;margin-top:14px}

/* ── hero ─────────────────────────────────────────── */
.hero{background:linear-gradient(160deg,var(--fiolet) 0%,var(--fiolet-ciemny) 100%);
  color:#fff;padding:56px 0 64px}
.hero-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:48px;align-items:center}
.seria{display:inline-flex;align-items:center;gap:12px;
  font-family:var(--font-h);font-weight:900;font-size:12px;letter-spacing:.2em;
  text-transform:uppercase;border:2px solid #8B6FD0;padding:7px 15px}
.seria i{font-style:normal;background:var(--pomarancz-cieply);color:#1B1030;
  padding:2px 9px;letter-spacing:.14em}
.hero h1{font-weight:900;font-size:clamp(38px,6vw,60px);line-height:.98;
  letter-spacing:-.02em;margin:20px 0 0}
.hero-sub{font-size:clamp(18px,2.4vw,23px);color:#D9CDF5;margin-top:16px;max-width:30ch}
.hero-przezn{color:#B9A6E6;margin-top:18px;font-size:16px;max-width:44ch}
.hero-foto{border:1px solid rgba(255,255,255,.18)}
.chipy{display:flex;flex-wrap:wrap;gap:8px;margin-top:26px}
.chip{font-family:var(--font-h);font-weight:800;font-size:13px;padding:7px 13px;
  color:#1B1030}
.hero-cta{display:flex;flex-wrap:wrap;gap:14px;align-items:center;margin-top:30px}
.btn{display:inline-block;font-family:var(--font-h);font-weight:900;font-size:16px;
  letter-spacing:.02em;padding:15px 28px;background:var(--pomarancz);color:#fff;
  text-decoration:none;border:2px solid var(--pomarancz)}
.btn:hover{background:#c93a08;border-color:#c93a08}
.btn-obrys{background:transparent;color:#fff;border-color:#8B6FD0}
.btn-obrys:hover{background:rgba(255,255,255,.08);border-color:#fff}
.btn:focus-visible,a:focus-visible{outline:3px solid var(--pomarancz-cieply);
  outline-offset:3px}

/* ── liczby ───────────────────────────────────────── */
.liczby{display:grid;grid-template-columns:repeat(4,1fr);gap:2px;
  background:var(--wlos);border:1px solid var(--wlos)}
.liczba{background:var(--papier);padding:26px 20px;text-align:center}
.liczba b{display:block;font-family:var(--font-h);font-weight:900;
  font-size:clamp(30px,4.4vw,44px);line-height:1;color:var(--fiolet)}
.liczba span{display:block;font-size:14px;color:var(--atrament-2);margin-top:8px}

/* ── siatki ───────────────────────────────────────── */
.trzy{display:grid;grid-template-columns:repeat(3,1fr);gap:26px;margin-top:36px}
.dwa{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}
.karta{background:var(--papier);border:1px solid var(--wlos);padding:26px}
.karta h3{font-weight:900;font-size:20px;color:var(--fiolet)}
.karta p{margin-top:9px;font-size:15.5px;line-height:1.6;color:var(--atrament-2)}

/* ── kolory ───────────────────────────────────────── */
.kolory{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:36px}
.kolor{overflow:hidden;border:1px solid var(--wlos)}
.kolor img{height:190px;object-fit:cover;width:100%}
.kolor-pas{background:var(--c);color:var(--txt);padding:12px 16px}
.kolor-pas b{display:block;font-family:var(--font-h);font-weight:900;font-size:19px}
.kolor-pas span{font-size:13px;letter-spacing:.08em;opacity:.85}

/* ── gdzie ────────────────────────────────────────── */
.gdzie{display:flex;flex-wrap:wrap;gap:10px;margin-top:28px}
.gdzie span{font-family:var(--font-h);font-weight:800;font-size:15px;
  background:var(--fiolet-jasny);color:var(--fiolet);padding:10px 18px}

/* ── licencje ─────────────────────────────────────── */
.licencje{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;
  margin-top:38px;align-items:start}
.lic{background:var(--papier);border:1px solid var(--wlos);display:flex;
  flex-direction:column;height:100%}
.lic-polecana{border:2px solid var(--fiolet);box-shadow:0 12px 32px rgba(45,27,105,.13)}
.lic-tag{background:var(--fiolet);color:#fff;font-family:var(--font-h);
  font-weight:900;font-size:12px;letter-spacing:.16em;text-transform:uppercase;
  padding:8px 20px;text-align:center}
.lic-body{padding:26px 24px 28px;display:flex;flex-direction:column;gap:14px;flex:1}
.lic h3{font-weight:900;font-size:22px;color:var(--fiolet)}
.lic-dla{font-size:14.5px;color:var(--atrament-3)}
.lic-cena{font-family:var(--font-h);font-weight:900;font-size:30px;
  color:var(--atrament);border-top:1px solid var(--wlos);padding-top:16px}
.lic ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;
  gap:10px;flex:1}
.lic li{position:relative;padding-left:26px;font-size:15.5px;line-height:1.55;
  color:var(--atrament-2)}
.lic li::before{content:"";position:absolute;left:2px;top:8px;width:11px;height:6px;
  border-left:2.5px solid var(--pomarancz);border-bottom:2.5px solid var(--pomarancz);
  transform:rotate(-45deg)}

.zasady{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:34px}
.zasada{background:var(--papier);border:1px solid var(--wlos);padding:24px 26px}
.zasada h3{font-weight:900;font-size:19px}
.zasada.tak h3{color:#1F7A46}
.zasada.nie h3{color:#B3261E}
.zasada ul{list-style:none;margin:14px 0 0;padding:0;display:flex;
  flex-direction:column;gap:9px}
.zasada li{position:relative;padding-left:24px;font-size:15.5px;line-height:1.55;
  color:var(--atrament-2)}
.zasada.tak li::before{content:"";position:absolute;left:2px;top:8px;width:10px;
  height:5px;border-left:2.5px solid #1F7A46;border-bottom:2.5px solid #1F7A46;
  transform:rotate(-45deg)}
.zasada.nie li::before{content:"×";position:absolute;left:3px;top:-2px;
  font-family:var(--font-h);font-weight:900;font-size:19px;color:#B3261E}

/* ── autorka i zapowiedź ──────────────────────────── */
.autorka{display:grid;grid-template-columns:280px 1fr;gap:36px;align-items:center}
.autorka img{border:1px solid var(--wlos)}
.autor-podpis{font-family:var(--font-h);font-weight:800;font-size:17px;
  color:var(--pomarancz);margin-top:10px;letter-spacing:.01em}
.zapowiedz{background:var(--fiolet);color:#fff}
.zapowiedz .eyebrow{color:var(--pomarancz-cieply)}
.zapowiedz .lead{color:#C9B6F2}
.zap-siatka{display:grid;grid-template-columns:repeat(6,1fr);gap:12px;margin-top:34px}
.zap img{height:130px;object-fit:cover;width:100%}
.zap-pas{background:var(--c);color:var(--txt);padding:10px 12px}
.zap-pas b{display:block;font-family:var(--font-h);font-weight:900;font-size:15px}
.zap-pas span{font-size:11.5px;letter-spacing:.06em;opacity:.85}

/* ── kontakt i stopka ─────────────────────────────── */
.kontakt{background:var(--fiolet-jasny)}
.kontakt-grid{display:grid;grid-template-columns:1fr auto;gap:40px;align-items:center}
.dane{display:flex;flex-wrap:wrap;gap:10px 34px;margin-top:20px;
  font-family:var(--font-h);font-weight:800;font-size:17px;color:var(--fiolet)}
.dane a{text-decoration:none}
.dane a:hover{text-decoration:underline}
footer{background:var(--atrament);color:#B9B2C4;padding:34px 0;font-size:14px}
.stopka{display:flex;align-items:center;gap:16px;flex-wrap:wrap}
.logo{width:48px;height:48px;flex:0 0 auto}
.stopka b{font-family:var(--font-h);font-weight:900;color:#fff;letter-spacing:.06em}
.stopka-prawa{margin-left:auto;text-align:right;line-height:1.5}

@media (max-width:900px){
  .hero-grid,.dwa,.autorka,.kontakt-grid{grid-template-columns:1fr}
  .trzy,.licencje,.zasady,.kolory{grid-template-columns:1fr 1fr}
  .liczby{grid-template-columns:1fr 1fr}
  .zap-siatka{grid-template-columns:repeat(3,1fr)}
  .stopka-prawa{margin-left:0;text-align:left}
}
@media (max-width:560px){
  .trzy,.licencje,.zasady,.kolory,.liczby{grid-template-columns:1fr}
  .zap-siatka{grid-template-columns:repeat(2,1fr)}
  section{padding:48px 0}
}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
@media print{.btn{display:none}}
"""


def sekcja_hero():
    chipy = "".join(
        f'<span class="chip" style="background:{hx};color:{tx}">{e(em)}</span>'
        for _, em, _, hx, tx in KOLORY_1
    ) + '<span class="chip" style="background:#D33B2C;color:#fff">Złość</span>'
    return f"""
<header class="hero"><div class="wrap"><div class="hero-grid">
<div>
  <span class="seria">Świat Kolorów <i>Część 1</i></span>
  <h1>Kolorowy Świat Emocji</h1>
  <p class="hero-sub">Pięć kolorów. Pięć emocji. Jeden Ty.</p>
  <p class="hero-przezn">Zeszyt do zajęć rozwijających kompetencje emocjonalne
    i społeczne, dostosowany do potrzeb młodzieży ze spektrum autyzmu.</p>
  <div class="chipy">{chipy}</div>
  <div class="hero-cta">
    <a class="btn" href="#licencje">Zobacz licencje</a>
    <a class="btn btn-obrys" href="#srodek">Co jest w środku?</a>
  </div>
</div>
<div>{foto("okladka", "Okładka zeszytu Kolorowy Świat Emocji", "hero-foto")}</div>
</div></div></header>"""


def sekcja_liczby():
    dane = [("58", "stron A4"), ("5", "emocji i kolorów"),
            ("85", "pytań i zadań"), ("30", "kart do wycięcia")]
    poz = "".join(f'<div class="liczba"><b>{b}</b><span>{e(s)}</span></div>'
                  for b, s in dane)
    return f'<section class="tlo"><div class="wrap"><div class="liczby">{poz}</div></div></section>'


def sekcja_srodek():
    karty = "".join(
        f'<div class="karta"><h3>{e(t)}</h3><p>{e(o)}</p></div>'
        for t, o in CO_W_SRODKU
    )
    kolory = "".join(
        f'<div class="kolor" style="--c:{hx};--txt:{tx}">{foto(p, em)}'
        f'<div class="kolor-pas"><b>{e(em)}</b><span>{e(kol)}</span></div></div>'
        for p, em, kol, hx, tx in KOLORY_1
    )
    return f"""
<section id="srodek"><div class="wrap">
  <span class="eyebrow">Co jest w środku</span>
  <h2>Gotowy materiał na cały rok pracy</h2>
  <p class="lead">Każdy rozdział ma ten sam układ ośmiu stron. Przewidywalność
    jest tu elementem terapeutycznym, nie ozdobnikiem — nastolatek wie,
    czego się spodziewać na następnej stronie.</p>
  <div class="trzy">{karty}</div>
  <div class="kolory">{kolory}</div>
</div></section>"""


def sekcja_gdzie():
    poz = "".join(f"<span>{e(g)}</span>" for g in GDZIE)
    return f"""
<section class="tlo"><div class="wrap"><div class="dwa">
<div>
  <span class="eyebrow">Dla kogo</span>
  <h2>Sprawdzi się tam, gdzie pracujesz</h2>
  <p class="lead">Zeszyt powstał do pracy z nastolatkiem w spektrum autyzmu,
    ale działa wszędzie tam, gdzie trzeba nazwać emocje: krótkie zdania,
    czytelny krój pisma, brak przebodźcowania, stały rytm stron.</p>
  <div class="gdzie">{poz}</div>
</div>
<div>{foto("wstep-poznaj", "Strona z zeszytu")}</div>
</div></div></section>"""


def sekcja_licencje():
    karty = ""
    for lic in LICENCJE:
        zakres = "".join(f"<li>{e(z)}</li>" for z in lic["zakres"])
        tag = '<div class="lic-tag">Najczęściej wybierana</div>' if lic["polecana"] else ""
        klasa = "lic lic-polecana" if lic["polecana"] else "lic"
        karty += f"""<div class="{klasa}">{tag}<div class="lic-body">
          <h3>{e(lic["nazwa"])}</h3>
          <p class="lic-dla">{e(lic["dla"])}</p>
          <ul>{zakres}</ul>
          <p class="lic-cena">{e(lic["cena"])}</p></div></div>"""
    zasady = "".join(
        f'<div class="zasada {"tak" if t == "Wolno" else "nie"}"><h3>{e(t)}</h3>'
        f'<ul>{"".join(f"<li>{e(p)}</li>" for p in poz)}</ul></div>'
        for t, poz in LICENCJA_ZASADY
    )
    return f"""
<section id="licencje"><div class="wrap">
  <span class="eyebrow">Licencje</span>
  <h2>Wybierz zakres, którego naprawdę potrzebujesz</h2>
  <p class="lead">Zeszyt sprzedajemy jako plik PDF do samodzielnego wydruku.
    Kupujesz raz, drukujesz tyle egzemplarzy, ilu masz uczniów.</p>
  <div class="licencje">{karty}</div>
  <div class="zasady">{zasady}</div>
</div></section>"""


def sekcja_autorka():
    return f"""
<section class="tlo"><div class="wrap"><div class="autorka">
<div>{foto("koniec", "Paleta pięciu kolorów emocji")}</div>
<div>
  <span class="eyebrow">Kto to napisał</span>
  <h2>{e(FIRMA["nazwa"])}</h2>
  <p class="autor-podpis">{e(FIRMA["autorka"])} — {e(FIRMA["funkcja"])}</p>
  <p class="lead">Zeszyt wyrósł z codziennej pracy terapeutycznej
    w {e(FIRMA["miasto"])}ie — z pytania, jak rozmawiać o emocjach
    z nastolatkiem, dla którego słowa bywają za trudne, a kolory już nie.
    Autorka prowadzi też ekosystem dokumentów EduPlaner 2026.</p>
</div>
</div></div></section>"""


def sekcja_zapowiedz():
    kafle = "".join(
        f'<div class="zap" style="--c:{hx};--txt:{tx}">{foto(p, em)}'
        f'<div class="zap-pas"><b>{e(em)}</b><span>{e(kol)}</span></div></div>'
        for p, em, kol, hx, tx in CZESC_2
    )
    return f"""
<section class="zapowiedz"><div class="wrap">
  <span class="eyebrow">Wkrótce</span>
  <h2>Świat Kolorów — część 2</h2>
  <p class="lead">Sześć nowych kolorów i sześć emocji, które też warto umieć
    nazwać. Ten sam bohater, ta sama droga przez osiem stron.</p>
  <div class="zap-siatka">{kafle}</div>
</div></section>"""


def sekcja_kontakt():
    return f"""
<section class="kontakt"><div class="wrap"><div class="kontakt-grid">
<div>
  <span class="eyebrow">Zamówienie</span>
  <h2>Chętnie porozmawiamy — bez zobowiązań</h2>
  <p class="lead">Napisz albo zadzwoń. Jeśli nie masz pewności, która licencja
    pasuje do Twojej placówki, pomożemy wybrać.</p>
  <div class="dane">
    <a href="mailto:{FIRMA["email"]}">{e(FIRMA["email"])}</a>
    <a href="tel:+48{FIRMA["telefon"].replace(" ", "")}">{e(FIRMA["telefon"])}</a>
  </div>
</div>
<div><a class="btn" href="mailto:{FIRMA["email"]}?subject=Kolorowy%20Świat%20Emocji%20—%20zamówienie">
  Napisz do nas</a></div>
</div></div></section>"""


def stopka():
    return f"""
<footer><div class="wrap"><div class="stopka">
  {LOGO}
  <div><b>{e(FIRMA["skrot"])}</b> {e(FIRMA["nazwa"])} · {e(FIRMA["miasto"])}</div>
  <div class="stopka-prawa">
    {e(FIRMA["www"])}<br>
    Kolorowy Świat Emocji · wydanie pierwsze, 2026<br>
    © {e(FIRMA["autorka"])}. Wszelkie prawa zastrzeżone.
  </div>
</div></div></footer>"""


def zbuduj():
    tytul = "Kolorowy Świat Emocji"
    glowa = (
        f"<title>{tytul}</title>\n"
        '<meta name="description" content="Zeszyt do zajęć rozwijających '
        'kompetencje emocjonalne i społeczne dla młodzieży ze spektrum autyzmu. '
        '58 stron A4, gra planszowa, karty emocji. PCTP Koszalin.">\n'
        f"<style>{CSS_FONTY}\n{CSS}</style>"
    )
    cialo = "\n".join([
        sekcja_hero(), sekcja_liczby(), sekcja_srodek(), sekcja_gdzie(),
        sekcja_licencje(), sekcja_autorka(), sekcja_zapowiedz(),
        sekcja_kontakt(), stopka(),
    ])
    pelny = ('<!doctype html>\n<html lang="pl">\n<head>\n<meta charset="utf-8">\n'
             '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
             f"{glowa}\n</head>\n<body>\n{cialo}\n</body>\n</html>\n")
    with open(os.path.join(BAZA, "oferta.html"), "w", encoding="utf-8") as f:
        f.write(pelny)
    with open(os.path.join(BAZA, "oferta-artefakt.html"), "w", encoding="utf-8") as f:
        f.write(f"{glowa}\n{cialo}\n")
    return len(pelny)


if __name__ == "__main__":
    print(f"Gotowe. Strona sprzedażowa: {zbuduj() // 1024} KB")
