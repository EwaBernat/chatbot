#!/usr/bin/env python3
"""Buduje edytor broszury: szablon + panel treści, tryb ręcznej edycji,
łapka do przenoszenia elementów i druk do PDF.

Wejście:  szablon-broszury-A4-druk.html  (z osadzonym fontem Mulish)
Wyjście:  edytor-broszury.html
"""
import pathlib, re

katalog = pathlib.Path(__file__).resolve().parent.parent
zrodlo = (katalog / 'szablon-broszury-A4-druk.html').read_text(encoding='utf-8')

STYL = r'''
<style>
/* ====== WARSTWA EDYTORA (nie drukuje się) ====== */
:root{ --ed-tlo:#1B1E27; --ed-panel:#242833; --ed-linia:#3A4050; --ed-akcent:#C8963E;
       --ed-akcent-2:#6E8F7D; --ed-tekst:#E8EAF0; --ed-tekst-mig:#98A0B0; }

.ed-pasek{
  position:fixed; inset:0 0 auto 0; z-index:60; display:flex; align-items:center;
  gap:8px; padding:10px 16px; background:var(--ed-tlo); color:var(--ed-tekst);
  border-bottom:1px solid var(--ed-linia); font-family:'Mulish',system-ui,sans-serif;
  box-shadow:0 2px 18px rgba(0,0,0,.35);
}
.ed-pasek .ed-marka{ font-weight:900; letter-spacing:.02em; margin-right:6px; font-size:14px; }
.ed-pasek .ed-marka em{ color:var(--ed-akcent); font-style:normal; }
.ed-rozpychacz{ flex:1; }

.ed-btn{
  font:600 13px/1 'Mulish',system-ui,sans-serif; color:var(--ed-tekst);
  background:var(--ed-panel); border:1px solid var(--ed-linia); border-radius:8px;
  padding:9px 13px; cursor:pointer; display:inline-flex; align-items:center; gap:7px;
  transition:background .15s, border-color .15s, color .15s;
}
.ed-btn:hover{ background:#2E3340; border-color:#4A5265; }
.ed-btn:focus-visible{ outline:2px solid var(--ed-akcent); outline-offset:2px; }
.ed-btn[aria-pressed="true"]{ background:var(--ed-akcent); border-color:var(--ed-akcent); color:#1B1E27; }
.ed-btn--glowny{ background:var(--ed-akcent); border-color:var(--ed-akcent); color:#1B1E27; font-weight:800; }
.ed-btn--glowny:hover{ background:#D9A84E; border-color:#D9A84E; }
.ed-btn svg{ width:15px; height:15px; flex:0 0 15px; }

/* ---- panel treści ---- */
.ed-panel{
  position:fixed; top:57px; bottom:0; left:0; width:370px; z-index:55;
  background:var(--ed-panel); color:var(--ed-tekst); border-right:1px solid var(--ed-linia);
  display:flex; flex-direction:column; font-family:'Mulish',system-ui,sans-serif;
  transform:translateX(-100%); transition:transform .22s ease; box-shadow:6px 0 28px rgba(0,0,0,.3);
}
.ed-panel[data-otwarty="tak"]{ transform:none; }
.ed-zakladki{ display:flex; border-bottom:1px solid var(--ed-linia); flex:0 0 auto; }
.ed-zakladka{
  flex:1; padding:13px 10px; background:none; border:0; border-bottom:2px solid transparent;
  color:var(--ed-tekst-mig); font:700 12.5px/1 'Mulish',sans-serif; cursor:pointer;
  letter-spacing:.04em; text-transform:uppercase;
}
.ed-zakladka[aria-selected="true"]{ color:var(--ed-akcent); border-bottom-color:var(--ed-akcent); }
.ed-karta{ display:none; padding:18px; overflow-y:auto; flex:1; }
.ed-karta[data-aktywna="tak"]{ display:block; }
.ed-karta h3{ font-size:13px; font-weight:800; letter-spacing:.1em; text-transform:uppercase;
  color:var(--ed-akcent); margin:0 0 4px; }
.ed-karta .ed-opis{ font-size:12.5px; line-height:1.55; color:var(--ed-tekst-mig); margin:0 0 16px; }
.ed-pole{ display:block; margin-bottom:13px; }
.ed-pole span{ display:block; font-size:11.5px; font-weight:700; letter-spacing:.05em;
  text-transform:uppercase; color:var(--ed-tekst-mig); margin-bottom:5px; }
.ed-pole input, .ed-pole textarea{
  width:100%; background:#1B1E27; border:1px solid var(--ed-linia); border-radius:7px;
  color:var(--ed-tekst); font:400 13.5px/1.5 'Mulish',system-ui,sans-serif; padding:9px 11px;
}
.ed-pole input:focus, .ed-pole textarea:focus{ outline:2px solid var(--ed-akcent); outline-offset:-1px; border-color:transparent; }
.ed-pole textarea{ min-height:230px; resize:vertical; }
.ed-grupa{ border-top:1px solid var(--ed-linia); margin-top:18px; padding-top:16px; }
.ed-panel .ed-stopa{ padding:14px 18px; border-top:1px solid var(--ed-linia); display:flex; gap:8px; flex:0 0 auto; }
.ed-panel .ed-stopa .ed-btn{ flex:1; justify-content:center; }
.ed-info{ font-size:12px; line-height:1.5; color:var(--ed-tekst-mig); background:#1B1E27;
  border-left:3px solid var(--ed-akcent-2); border-radius:0 6px 6px 0; padding:10px 12px; margin-bottom:14px; }
.ed-info code{ color:var(--ed-akcent); }

/* ---- płótno ---- */
body{ padding-top:57px; }
body[data-panel="tak"]{ padding-left:370px; }
.pasek-info{ display:none !important; }

/* ---- tryb ręcznej edycji ---- */
body[data-edycja="tak"] [contenteditable="true"]{
  outline:1px dashed rgba(200,150,62,.55); outline-offset:2px; border-radius:2px; cursor:text;
}
body[data-edycja="tak"] [contenteditable="true"]:hover{ outline-color:rgba(200,150,62,.95); background:rgba(200,150,62,.06); }
body[data-edycja="tak"] [contenteditable="true"]:focus{
  outline:2px solid var(--ed-akcent); background:rgba(200,150,62,.10);
}

/* ---- tryb przenoszenia ---- */
.ed-lapka{
  position:absolute; z-index:50; display:none; align-items:center; gap:5px;
  background:var(--ed-akcent); color:#1B1E27; border:0; border-radius:6px;
  padding:4px 8px; font:800 10.5px/1 'Mulish',sans-serif; letter-spacing:.06em;
  text-transform:uppercase; cursor:grab; box-shadow:0 3px 10px rgba(0,0,0,.28);
}
.ed-lapka:active{ cursor:grabbing; }
.ed-lapka svg{ width:12px; height:12px; }
body[data-przenoszenie="tak"] .ed-lapka[data-widoczna="tak"]{ display:inline-flex; }
body[data-przenoszenie="tak"] .ed-ruchomy{ outline:1px dashed rgba(110,143,125,.6); outline-offset:3px; }
body[data-przenoszenie="tak"] .ed-ruchomy:hover{ outline-color:var(--ed-akcent-2); }
.ed-ruchomy.ed-unosi{ opacity:.35; }
.ed-wstawka{ height:0; border-top:2.5px solid var(--ed-akcent); margin:2px 0; border-radius:2px; }

/* ---- komunikat ---- */
.ed-toast{
  position:fixed; left:50%; bottom:26px; transform:translate(-50%,14px); z-index:70;
  background:var(--ed-tlo); color:var(--ed-tekst); border:1px solid var(--ed-linia);
  border-left:3px solid var(--ed-akcent); border-radius:9px; padding:11px 17px;
  font:600 13px/1.4 'Mulish',sans-serif; opacity:0; pointer-events:none;
  transition:opacity .2s, transform .2s; box-shadow:0 8px 30px rgba(0,0,0,.4);
}
.ed-toast[data-widoczny="tak"]{ opacity:1; transform:translate(-50%,0); }

@media (max-width:900px){
  .ed-panel{ width:100%; }
  body[data-panel="tak"]{ padding-left:0; }
  .ed-pasek .ed-etykieta{ display:none; }
}
@media (prefers-reduced-motion:reduce){ .ed-panel,.ed-toast{ transition:none; } }

@media print{
  .ed-pasek,.ed-panel,.ed-lapka,.ed-toast,.ed-wstawka{ display:none !important; }
  body{ padding:0 !important; }
  [contenteditable]{ outline:none !important; background:none !important; }
  .ed-ruchomy{ outline:none !important; }
}

/* ====== WSTAWIANIE ZDJĘĆ ====== */
.zdjecie-ramka{ cursor:pointer; }
.zdjecie-ramka:hover{ border-color:var(--ed-akcent); }
.zdjecie-ramka.ed-cel{ border-style:solid; border-color:var(--ed-akcent); box-shadow:0 0 0 3px rgba(200,150,62,.25); }
.zdjecie-ramka.ed-nad{ border-style:solid; border-color:var(--ed-akcent-2); background:rgba(110,143,125,.12); }
.zdjecie-ramka > img{
  position:absolute; inset:0; width:100%; height:100%; object-fit:cover;
  border-radius:1.2mm; display:block;
}
.zdjecie-ramka.ed-ma-zdjecie{ background:none; border-style:solid; border-color:rgba(200,150,62,.35); }
.zdjecie-ramka.ed-ma-zdjecie::after{ display:none; }
.zdjecie-ramka.ed-ma-zdjecie > :not(img){ display:none; }

.ed-okno{
  position:fixed; inset:0; z-index:80; display:none; align-items:center; justify-content:center;
  background:rgba(12,14,20,.62); padding:20px; font-family:'Mulish',system-ui,sans-serif;
}
.ed-okno[data-otwarte="tak"]{ display:flex; }
.ed-okno-tresc{
  background:var(--ed-panel); color:var(--ed-tekst); border:1px solid var(--ed-linia);
  border-radius:14px; width:min(560px,100%); max-height:88vh; overflow-y:auto;
  padding:24px; box-shadow:0 24px 70px rgba(0,0,0,.5);
}
.ed-okno h2{ font-size:17px; font-weight:900; margin:0 0 6px; color:var(--ed-tekst); }
.ed-okno .ed-opis{ margin:0 0 18px; }
.ed-zrodla{ display:grid; gap:10px; margin-bottom:18px; }
.ed-zrodlo{
  display:flex; align-items:flex-start; gap:12px; text-align:left; width:100%;
  background:#1B1E27; border:1px solid var(--ed-linia); border-radius:10px;
  padding:13px 15px; cursor:pointer; color:var(--ed-tekst); font-family:inherit;
  transition:border-color .15s, background .15s;
}
.ed-zrodlo:hover{ border-color:var(--ed-akcent); background:#20242F; }
.ed-zrodlo:focus-visible{ outline:2px solid var(--ed-akcent); outline-offset:2px; }
.ed-zrodlo .ed-glif{
  flex:0 0 34px; height:34px; border-radius:9px; background:rgba(200,150,62,.16);
  color:var(--ed-akcent); display:flex; align-items:center; justify-content:center;
}
.ed-zrodlo .ed-glif svg{ width:17px; height:17px; }
.ed-zrodlo b{ display:block; font-size:13.5px; font-weight:800; margin-bottom:2px; }
.ed-zrodlo small{ display:block; font-size:11.8px; line-height:1.45; color:var(--ed-tekst-mig); }
.ed-banki{ display:flex; flex-wrap:wrap; gap:7px; margin-top:8px; }
.ed-bank{
  font:700 11.5px/1 'Mulish',sans-serif; color:var(--ed-tekst); text-decoration:none;
  background:#1B1E27; border:1px solid var(--ed-linia); border-radius:20px; padding:7px 12px;
}
.ed-bank:hover{ border-color:var(--ed-akcent-2); color:#fff; }
.ed-okno-stopa{ display:flex; gap:9px; justify-content:flex-end; border-top:1px solid var(--ed-linia); padding-top:16px; }
@media print{ .ed-okno{ display:none !important; } }
</style>
'''

IKONY = {
 'olowek':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg>',
 'lapka':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 9V5.5a1.5 1.5 0 0 1 3 0V9"/><path d="M8 9V4a1.5 1.5 0 0 1 3 0v5"/><path d="M11 9V4.5a1.5 1.5 0 0 1 3 0V10"/><path d="M14 10V7a1.5 1.5 0 0 1 3 0v6a7 7 0 0 1-7 7h-1a6 6 0 0 1-6-6v-2a1.5 1.5 0 0 1 3 0"/></svg>',
 'tekst':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h16M4 12h10M4 18h13"/></svg>',
 'drukarka':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9V3h12v6"/><path d="M6 18H4a2 2 0 0 1-2-2v-4a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2h-2"/><path d="M6 14h12v7H6z"/></svg>',
 'zapis':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2Z"/><path d="M17 21v-8H7v8M7 3v5h8"/></svg>',
 'cofnij':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/></svg>',
}

POLA = [
 ('sela', None, None),
]

PANEL = '''
<div class="ed-pasek ed-chrome">
  <span class="ed-marka">Broszura <em>PCTP</em></span>
  <button class="ed-btn" id="ed-pokaz-panel" aria-pressed="false">{tekst}<span class="ed-etykieta">Treść</span></button>
  <button class="ed-btn" id="ed-tryb-edycji" aria-pressed="false">{olowek}<span class="ed-etykieta">Edytuj tekst</span></button>
  <button class="ed-btn" id="ed-tryb-przenoszenia" aria-pressed="false">{lapka}<span class="ed-etykieta">Przenoś elementy</span></button>
  <span class="ed-rozpychacz"></span>
  <button class="ed-btn" id="ed-zapisz">{zapis}<span class="ed-etykieta">Zapisz</span></button>
  <button class="ed-btn" id="ed-przywroc">{cofnij}<span class="ed-etykieta">Przywróć wzór</span></button>
  <button class="ed-btn ed-btn--glowny" id="ed-drukuj">{drukarka}Drukuj / PDF</button>
</div>

<aside class="ed-panel ed-chrome" id="ed-panel" data-otwarty="nie" aria-label="Panel treści">
  <div class="ed-zakladki" role="tablist">
    <button class="ed-zakladka" role="tab" aria-selected="true"  data-karta="formularz">Formularz</button>
    <button class="ed-zakladka" role="tab" aria-selected="false" data-karta="wklej">Wklej tekst</button>
  </div>

  <div class="ed-karta" data-karta="formularz" data-aktywna="tak">
    <h3>Dane broszury</h3>
    <p class="ed-opis">Wpisz treść — zmiana pojawia się w broszurze od razu, w trakcie pisania.</p>
    <label class="ed-pole"><span>Seria / nadtytuł</span><input type="text" data-cel="seria"></label>
    <label class="ed-pole"><span>Tytuł broszury</span><input type="text" data-cel="tytul"></label>
    <label class="ed-pole"><span>Podtytuł</span><textarea data-cel="podtytul" style="min-height:64px"></textarea></label>
    <label class="ed-pole"><span>Autor</span><input type="text" data-cel="autor"></label>

    <div class="ed-grupa">
      <h3>Tytuły stron</h3>
      <label class="ed-pole"><span>Przedmowa</span><input type="text" data-cel="tytul-przedmowa"></label>
      <label class="ed-pole"><span>Wstęp</span><input type="text" data-cel="tytul-wstep"></label>
      <label class="ed-pole"><span>Zdanie otwierające wstęp</span><textarea data-cel="lead-wstep" style="min-height:64px"></textarea></label>
      <label class="ed-pole"><span>Rozdział 02</span><input type="text" data-cel="tytul-r02"></label>
      <label class="ed-pole"><span>Rozdział 03</span><input type="text" data-cel="tytul-r03"></label>
      <label class="ed-pole"><span>Rozdział 04</span><input type="text" data-cel="tytul-r04"></label>
      <label class="ed-pole"><span>Zakończenie</span><input type="text" data-cel="tytul-autor"></label>
    </div>

    <div class="ed-grupa">
      <h3>Stopka</h3>
      <p class="ed-opis">Podmienia dane na wszystkich stronach naraz.</p>
      <label class="ed-pole"><span>Instytucja</span><input type="text" id="ed-instytucja"></label>
      <label class="ed-pole"><span>E-mail</span><input type="text" id="ed-email"></label>
      <label class="ed-pole"><span>Rok wydania</span><input type="text" id="ed-rok"></label>
      <button class="ed-btn" id="ed-zastosuj-stopke" style="width:100%;justify-content:center">Zastosuj w całej broszurze</button>
    </div>
  </div>

  <div class="ed-karta" data-karta="wklej">
    <h3>Wklej gotowy tekst</h3>
    <p class="ed-opis">Wklej całą treść naraz — rozłoży się po kolei na akapity broszury.</p>
    <div class="ed-info">
      Oddzielaj akapity <strong>pustą linią</strong>. Linia zaczynająca się od <code>#</code>
      trafia w tytuł broszury, a od <code>##</code> — w tytuł kolejnego rozdziału.
      Pozostałe akapity wypełniają kolejne miejsca na tekst, strona po stronie.
    </div>
    <label class="ed-pole"><span>Treść</span><textarea id="ed-wklejka" placeholder="# Tytuł broszury&#10;&#10;Pierwszy akapit przedmowy…&#10;&#10;Drugi akapit…&#10;&#10;## Podstawy, które warto znać&#10;&#10;Akapit rozdziału…"></textarea></label>
    <button class="ed-btn ed-btn--glowny" id="ed-rozloz" style="width:100%;justify-content:center">Rozłóż tekst w broszurze</button>
  </div>

  <div class="ed-stopa">
    <button class="ed-btn" id="ed-zamknij-panel">Zamknij panel</button>
  </div>
</aside>

<div class="ed-toast ed-chrome" id="ed-toast" role="status" aria-live="polite"></div>
<button class="ed-lapka ed-chrome" id="ed-lapka" type="button" aria-label="Przenieś element">{lapka}Przenieś</button>

<div class="ed-okno ed-chrome" id="ed-okno-zdjec" role="dialog" aria-modal="true" aria-labelledby="ed-okno-tytul">
  <div class="ed-okno-tresc">
    <h2 id="ed-okno-tytul">Wstaw zdjęcie</h2>
    <p class="ed-opis">Wybrane zdjęcie wskoczy w tę ramkę i zostanie zapisane w pliku broszury.</p>

    <div class="ed-zrodla">
      <button class="ed-zrodlo" id="ed-zrodlo-dysk">
        <span class="ed-glif"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="M7 10l5-5 5 5"/><path d="M12 5v13"/></svg></span>
        <span><b>Z dysku</b><small>Wybierz plik JPG lub PNG z komputera. Zdjęcie zostaje wewnątrz broszury — działa też bez internetu.</small></span>
      </button>

      <button class="ed-zrodlo" id="ed-zrodlo-schowek">
        <span class="ed-glif"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="8" y="8" width="13" height="13" rx="2"/><path d="M5 16H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v1"/></svg></span>
        <span><b>Ze schowka — Canva, Gamma i inne</b><small>Skopiuj grafikę w Canvie lub Gammie (Ctrl+C), wróć tutaj i naciśnij Ctrl+V. To najprostsza droga z dowolnego programu.</small></span>
      </button>

      <button class="ed-zrodlo" id="ed-zrodlo-adres">
        <span class="ed-glif"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1"/><path d="M14 11a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/></svg></span>
        <span><b>Z adresu internetowego</b><small>Wklej bezpośredni link do pliku ze zdjęciem. Wymaga połączenia z siecią przy druku.</small></span>
      </button>
    </div>

    <h3 style="font-size:12px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--ed-akcent);margin:0">
      Banki zdjęć na darmowej licencji
    </h3>
    <p class="ed-opis" style="margin:6px 0 0">
      Otwórz w nowej karcie, pobierz zdjęcie i wróć tutaj. Zawsze sprawdź warunki licencji przy konkretnym pliku.
    </p>
    <div class="ed-banki">
      <a class="ed-bank" href="https://unsplash.com/pl" target="_blank" rel="noopener noreferrer">Unsplash</a>
      <a class="ed-bank" href="https://www.pexels.com/pl-pl/" target="_blank" rel="noopener noreferrer">Pexels</a>
      <a class="ed-bank" href="https://pixabay.com/pl/" target="_blank" rel="noopener noreferrer">Pixabay</a>
      <a class="ed-bank" href="https://openverse.org/" target="_blank" rel="noopener noreferrer">Openverse</a>
      <a class="ed-bank" href="https://commons.wikimedia.org/" target="_blank" rel="noopener noreferrer">Wikimedia Commons</a>
    </div>

    <div class="ed-okno-stopa" style="margin-top:20px">
      <button class="ed-btn" id="ed-usun-zdjecie">Usuń zdjęcie z ramki</button>
      <button class="ed-btn" id="ed-zamknij-okno">Zamknij</button>
    </div>
  </div>
</div>
<input type="file" id="ed-plik" accept="image/*" hidden>

'''.format(tekst=IKONY['tekst'], olowek=IKONY['olowek'], lapka=IKONY['lapka'],
           zapis=IKONY['zapis'], cofnij=IKONY['cofnij'], drukarka=IKONY['drukarka'])

SKRYPT = r'''
<script>
(function(){
  'use strict';
  var body = document.body;
  var KLUCZ = 'broszura-pctp-v1';

  /* elementy, które da się edytować ręcznie */
  var EDYTOWALNE = 'h1,h2,h3,h4,p,li,td,th,cite,.nadtytul,.spis-tytul,.spis-opis,'
                 + '.spis-strona,.spis-nr,.stat .liczba,.stat .opis,.podpis-opis,'
                 + '.stopka span,.okladka-stopka span,.podpis-linia,.etykieta,.wymiar,.logo-blok .nazwa';
  /* bloki, które da się przenosić łapką */
  var RUCHOME = '.ramka,.zdjecie,.cytat,.statystyki,.galeria,.notatki,.tabela,'
              + '.kroki,.ozdobnik-linia,.kropki,.spis';

  var wzorcowy = null;   // kopia oryginału do przywrócenia
  var scena = document.querySelector('.pasek-info') ? document.body : document.body;

  /* ---------- komunikaty ---------- */
  var toast = document.getElementById('ed-toast'), licznikToast;
  function powiedz(tekst){
    toast.textContent = tekst;
    toast.setAttribute('data-widoczny','tak');
    clearTimeout(licznikToast);
    licznikToast = setTimeout(function(){ toast.removeAttribute('data-widoczny'); }, 2600);
  }

  /* ---------- oznaczanie elementów ---------- */
  function oznacz(){
    document.querySelectorAll('.strona ' + RUCHOME).forEach(function(el){
      if (!el.closest('.ed-panel')) el.classList.add('ed-ruchomy');
    });
    document.querySelectorAll('.strona').forEach(function(str){
      str.querySelectorAll(EDYTOWALNE).forEach(function(el){
        if (el.querySelector(EDYTOWALNE)) return;         // tylko liście
        el.setAttribute('data-edytowalny','tak');
      });
    });
  }

  /* ---------- tryb ręcznej edycji ---------- */
  var trybEdycji = document.getElementById('ed-tryb-edycji');
  function ustawEdycje(wl){
    body.setAttribute('data-edycja', wl ? 'tak' : 'nie');
    trybEdycji.setAttribute('aria-pressed', wl ? 'true' : 'false');
    document.querySelectorAll('[data-edytowalny]').forEach(function(el){
      if (wl) el.setAttribute('contenteditable','true');
      else    el.removeAttribute('contenteditable');
    });
    if (wl) powiedz('Tryb edycji: kliknij dowolny tekst i pisz.');
  }
  trybEdycji.addEventListener('click', function(){
    ustawEdycje(body.getAttribute('data-edycja') !== 'tak');
  });

  /* ---------- łapka: przenoszenie elementów ---------- */
  var lapka = document.getElementById('ed-lapka');
  var trybPrzen = document.getElementById('ed-tryb-przenoszenia');
  var celLapki = null, niesiony = null, wstawka = null;

  function ustawPrzenoszenie(wl){
    body.setAttribute('data-przenoszenie', wl ? 'tak' : 'nie');
    trybPrzen.setAttribute('aria-pressed', wl ? 'true' : 'false');
    if (!wl) lapka.removeAttribute('data-widoczna');
    else powiedz('Najedź na element, złap łapkę i przeciągnij w nowe miejsce.');
  }
  trybPrzen.addEventListener('click', function(){
    ustawPrzenoszenie(body.getAttribute('data-przenoszenie') !== 'tak');
  });

  document.addEventListener('mouseover', function(e){
    if (body.getAttribute('data-przenoszenie') !== 'tak' || niesiony) return;
    var el = e.target.closest ? e.target.closest('.ed-ruchomy') : null;
    if (!el || el === celLapki) return;
    celLapki = el;
    var p = el.getBoundingClientRect();
    lapka.style.top  = (window.scrollY + p.top - 11) + 'px';
    lapka.style.left = (window.scrollX + p.left) + 'px';
    lapka.setAttribute('data-widoczna','tak');
  });

  lapka.addEventListener('pointerdown', function(e){
    if (!celLapki) return;
    e.preventDefault();
    niesiony = celLapki;
    niesiony.classList.add('ed-unosi');
    wstawka = document.createElement('div');
    wstawka.className = 'ed-wstawka';
    lapka.setPointerCapture(e.pointerId);
  });

  lapka.addEventListener('pointermove', function(e){
    if (!niesiony) return;
    niesiony.style.pointerEvents = 'none';
    var pod = document.elementFromPoint(e.clientX, e.clientY);
    niesiony.style.pointerEvents = '';
    if (!pod || !pod.closest) return;
    var sasiad = pod.closest('.ed-ruchomy');
    if (!sasiad || sasiad === niesiony || sasiad === wstawka) return;
    var p = sasiad.getBoundingClientRect();
    if (e.clientY < p.top + p.height / 2) sasiad.parentNode.insertBefore(wstawka, sasiad);
    else sasiad.parentNode.insertBefore(wstawka, sasiad.nextSibling);
  });

  function upusc(){
    if (!niesiony) return;
    if (wstawka && wstawka.parentNode) wstawka.parentNode.replaceChild(niesiony, wstawka);
    else if (wstawka) wstawka.remove();
    niesiony.classList.remove('ed-unosi');
    niesiony = null; wstawka = null; celLapki = null;
    lapka.removeAttribute('data-widoczna');
    powiedz('Element przeniesiony.');
  }
  lapka.addEventListener('pointerup', upusc);
  lapka.addEventListener('pointercancel', upusc);

  /* ---------- panel treści ---------- */
  var panel = document.getElementById('ed-panel');
  function ustawPanel(wl){
    panel.setAttribute('data-otwarty', wl ? 'tak' : 'nie');
    body.setAttribute('data-panel', wl ? 'tak' : 'nie');
    document.getElementById('ed-pokaz-panel').setAttribute('aria-pressed', wl ? 'true' : 'false');
  }
  document.getElementById('ed-pokaz-panel').addEventListener('click', function(){
    ustawPanel(panel.getAttribute('data-otwarty') !== 'tak');
  });
  document.getElementById('ed-zamknij-panel').addEventListener('click', function(){ ustawPanel(false); });

  document.querySelectorAll('.ed-zakladka').forEach(function(z){
    z.addEventListener('click', function(){
      document.querySelectorAll('.ed-zakladka').forEach(function(i){ i.setAttribute('aria-selected','false'); });
      z.setAttribute('aria-selected','true');
      document.querySelectorAll('.ed-karta').forEach(function(k){
        k.setAttribute('data-aktywna', k.dataset.karta === z.dataset.karta ? 'tak' : 'nie');
      });
    });
  });

  /* ---------- formularz -> broszura ---------- */
  function polaFormularza(){
    document.querySelectorAll('[data-cel]').forEach(function(wejscie){
      var cel = document.querySelector('[data-pole="' + wejscie.dataset.cel + '"]');
      if (!cel) return;
      wejscie.value = cel.textContent.trim().replace(/\s+/g,' ');
      wejscie.addEventListener('input', function(){
        var kolor = cel.querySelector('span[style]');           // druga część tytułu w złocie
        if (kolor){ cel.textContent = wejscie.value; }
        else cel.textContent = wejscie.value;
      });
    });
  }

  /* ---------- dane stopki w całej broszurze ---------- */
  function podmienTekst(stary, nowy){
    if (!stary || stary === nowy) return;
    var chodzik = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
      acceptNode: function(n){
        return n.parentElement.closest('.ed-panel,.ed-pasek,script,style')
          ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT;
      }
    });
    var n;
    while ((n = chodzik.nextNode())){
      if (n.nodeValue.indexOf(stary) !== -1) n.nodeValue = n.nodeValue.split(stary).join(nowy);
    }
  }
  var stopka = { instytucja:'Pomorskie Centrum Terapii Pedagogicznej',
                 email:'kontakt@eduplaner2026.pl', rok:'2026' };
  document.getElementById('ed-instytucja').value = stopka.instytucja;
  document.getElementById('ed-email').value      = stopka.email;
  document.getElementById('ed-rok').value        = stopka.rok;
  document.getElementById('ed-zastosuj-stopke').addEventListener('click', function(){
    var nowe = { instytucja:document.getElementById('ed-instytucja').value.trim(),
                 email:document.getElementById('ed-email').value.trim(),
                 rok:document.getElementById('ed-rok').value.trim() };
    podmienTekst(stopka.instytucja, nowe.instytucja);
    podmienTekst(stopka.email, nowe.email);
    podmienTekst(stopka.rok, nowe.rok);
    stopka = nowe;
    powiedz('Dane stopki zaktualizowane na wszystkich stronach.');
  });

  /* ---------- automatyczne rozłożenie wklejonego tekstu ---------- */
  document.getElementById('ed-rozloz').addEventListener('click', function(){
    var surowy = document.getElementById('ed-wklejka').value.trim();
    if (!surowy){ powiedz('Najpierw wklej tekst w pole powyżej.'); return; }

    var bloki = surowy.split(/\n\s*\n/).map(function(b){ return b.trim(); }).filter(Boolean);
    var naglowki = document.querySelectorAll('.strona h2[data-pole]');
    var iNaglowka = 0;

    /* miejsca na akapity: zwykłe <p> w treści stron, bez leadów i podpisów */
    var akapity = [].slice.call(document.querySelectorAll('.strona .tresc p'))
      .filter(function(p){
        return !p.closest('.ed-panel') && !p.classList.contains('mikro')
            && !p.closest('.zdjecie-ramka') && p.textContent.trim().length > 40;
      });
    var iAkapitu = 0, wstawione = 0;

    bloki.forEach(function(blok){
      if (/^#\s+/.test(blok)){
        var t = document.querySelector('[data-pole="tytul"]');
        if (t){ t.textContent = blok.replace(/^#\s+/, ''); wstawione++; }
      } else if (/^##\s+/.test(blok)){
        if (iNaglowka < naglowki.length){
          naglowki[iNaglowka++].textContent = blok.replace(/^##\s+/, '');
          wstawione++;
        }
      } else if (iAkapitu < akapity.length){
        akapity[iAkapitu++].textContent = blok.replace(/\s*\n\s*/g, ' ');
        wstawione++;
      }
    });
    powiedz('Rozłożono ' + wstawione + ' fragment(ów). Resztę dopiszesz ręcznie.');
  });

  /* ---------- zapis / przywracanie ---------- */
  function zapisz(){
    try{
      var strony = [].map.call(document.querySelectorAll('.strona'), function(s){ return s.outerHTML; });
      localStorage.setItem(KLUCZ, JSON.stringify(strony));
      powiedz('Zapisano w tej przeglądarce.');
    }catch(e){ powiedz('Nie udało się zapisać — przeglądarka blokuje pamięć stron.'); }
  }
  function wczytaj(){
    try{
      var dane = localStorage.getItem(KLUCZ);
      if (!dane) return false;
      var strony = JSON.parse(dane);
      var obecne = document.querySelectorAll('.strona');
      if (strony.length !== obecne.length) return false;
      obecne.forEach(function(s, i){ s.outerHTML = strony[i]; });
      return true;
    }catch(e){ return false; }
  }
  document.getElementById('ed-zapisz').addEventListener('click', zapisz);
  document.getElementById('ed-przywroc').addEventListener('click', function(){
    if (!confirm('Przywrócić pierwotny wzór? Wszystkie zmiany zostaną utracone.')) return;
    try{ localStorage.removeItem(KLUCZ); }catch(e){}
    document.querySelectorAll('.strona').forEach(function(s, i){ s.outerHTML = wzorcowy[i]; });
    start(true);
    powiedz('Przywrócono pierwotny wzór.');
  });

  /* ---------- druk ---------- */
  document.getElementById('ed-drukuj').addEventListener('click', function(){
    ustawEdycje(false); ustawPrzenoszenie(false); ustawPanel(false);
    setTimeout(function(){ window.print(); }, 120);
  });

  /* ---------- start ---------- */
  function start(poPrzywroceniu){
    oznacz();
    polaFormularza();
    if (body.getAttribute('data-edycja') === 'tak') ustawEdycje(true);
  }
  wzorcowy = [].map.call(document.querySelectorAll('.strona'), function(s){ return s.outerHTML; });
  if (wczytaj()) powiedz('Wczytano Twoją poprzednią wersję.');
  start();
  ustawEdycje(false);
  ustawPrzenoszenie(false);
})();
</script>
'''

SKRYPT_ZDJEC = r'''
<script>
(function(){
  'use strict';
  var okno   = document.getElementById('ed-okno-zdjec');
  var wejscie= document.getElementById('ed-plik');
  var ramka  = null;                       // ramka, którą właśnie wypełniamy
  var toast  = document.getElementById('ed-toast'), licznik;

  function powiedz(t){
    toast.textContent = t; toast.setAttribute('data-widoczny','tak');
    clearTimeout(licznik); licznik = setTimeout(function(){ toast.removeAttribute('data-widoczny'); }, 3000);
  }

  /* --- zmniejszenie zdjęcia, żeby plik broszury nie spuchł --- */
  function przeskaluj(zrodlo, gotowe){
    var obraz = new Image();
    obraz.onload = function(){
      var max = 1800, w = obraz.width, h = obraz.height;
      if (Math.max(w, h) > max){ var s = max / Math.max(w, h); w = Math.round(w*s); h = Math.round(h*s); }
      var plotno = document.createElement('canvas');
      plotno.width = w; plotno.height = h;
      plotno.getContext('2d').drawImage(obraz, 0, 0, w, h);
      try{ gotowe(plotno.toDataURL('image/jpeg', 0.86)); }
      catch(e){ gotowe(zrodlo); }          // np. obraz z innej domeny
    };
    obraz.onerror = function(){ gotowe(zrodlo); };
    obraz.crossOrigin = 'anonymous';
    obraz.src = zrodlo;
  }

  function wstaw(cel, zrodlo){
    if (!cel) return;
    przeskaluj(zrodlo, function(gotowy){
      var img = cel.querySelector('img');
      if (!img){ img = document.createElement('img'); cel.appendChild(img); }
      img.src = gotowy;
      img.alt = 'Zdjęcie w broszurze';
      cel.classList.add('ed-ma-zdjecie');
      powiedz('Zdjęcie wstawione.');
    });
  }

  function zPliku(plik, cel){
    if (!plik || !/^image\//.test(plik.type)){ powiedz('To nie jest plik ze zdjęciem.'); return; }
    var czyt = new FileReader();
    czyt.onload = function(){ wstaw(cel, czyt.result); };
    czyt.readAsDataURL(plik);
  }

  /* --- kliknięcie w ramkę otwiera okno wyboru --- */
  document.addEventListener('click', function(e){
    if (document.body.getAttribute('data-przenoszenie') === 'tak') return;
    var cel = e.target.closest ? e.target.closest('.zdjecie-ramka') : null;
    if (!cel || cel.closest('.ed-panel')) return;
    e.preventDefault();
    document.querySelectorAll('.ed-cel').forEach(function(r){ r.classList.remove('ed-cel'); });
    ramka = cel; ramka.classList.add('ed-cel');
    okno.setAttribute('data-otwarte','tak');
  });

  function zamknij(){
    okno.removeAttribute('data-otwarte');
    if (ramka) ramka.classList.remove('ed-cel');
  }
  document.getElementById('ed-zamknij-okno').addEventListener('click', zamknij);
  okno.addEventListener('click', function(e){ if (e.target === okno) zamknij(); });
  document.addEventListener('keydown', function(e){ if (e.key === 'Escape') zamknij(); });

  /* --- z dysku --- */
  document.getElementById('ed-zrodlo-dysk').addEventListener('click', function(){ wejscie.click(); });
  wejscie.addEventListener('change', function(){
    zPliku(wejscie.files[0], ramka); wejscie.value = ''; zamknij();
  });

  /* --- ze schowka (Canva, Gamma, dowolny program) --- */
  document.getElementById('ed-zrodlo-schowek').addEventListener('click', function(){
    if (navigator.clipboard && navigator.clipboard.read){
      navigator.clipboard.read().then(function(rzeczy){
        for (var i = 0; i < rzeczy.length; i++){
          var typ = rzeczy[i].types.filter(function(t){ return /^image\//.test(t); })[0];
          if (typ){
            rzeczy[i].getType(typ).then(function(plik){
              var czyt = new FileReader();
              czyt.onload = function(){ wstaw(ramka, czyt.result); zamknij(); };
              czyt.readAsDataURL(plik);
            });
            return;
          }
        }
        powiedz('W schowku nie ma grafiki. Skopiuj ją i naciśnij tutaj Ctrl+V.');
      }).catch(function(){
        powiedz('Naciśnij teraz Ctrl+V, żeby wkleić grafikę ze schowka.');
      });
    } else {
      powiedz('Naciśnij teraz Ctrl+V, żeby wkleić grafikę ze schowka.');
    }
  });

  document.addEventListener('paste', function(e){
    var rzeczy = (e.clipboardData || {}).items || [];
    for (var i = 0; i < rzeczy.length; i++){
      if (/^image\//.test(rzeczy[i].type)){
        e.preventDefault();
        zPliku(rzeczy[i].getAsFile(), ramka || document.querySelector('.zdjecie-ramka'));
        zamknij();
        return;
      }
    }
  });

  /* --- z adresu --- */
  document.getElementById('ed-zrodlo-adres').addEventListener('click', function(){
    var adres = prompt('Wklej bezpośredni adres zdjęcia (musi kończyć się np. na .jpg lub .png):');
    if (adres && adres.trim()){ wstaw(ramka, adres.trim()); zamknij(); }
  });

  /* --- usunięcie zdjęcia --- */
  document.getElementById('ed-usun-zdjecie').addEventListener('click', function(){
    if (!ramka) return;
    var img = ramka.querySelector('img');
    if (img) img.remove();
    ramka.classList.remove('ed-ma-zdjecie');
    powiedz('Zdjęcie usunięte — wróciła ramka zastępcza.');
    zamknij();
  });

  /* --- przeciągnij i upuść plik wprost na ramkę --- */
  document.addEventListener('dragover', function(e){
    var cel = e.target.closest ? e.target.closest('.zdjecie-ramka') : null;
    if (!cel) return;
    e.preventDefault(); cel.classList.add('ed-nad');
  });
  document.addEventListener('dragleave', function(e){
    var cel = e.target.closest ? e.target.closest('.zdjecie-ramka') : null;
    if (cel) cel.classList.remove('ed-nad');
  });
  document.addEventListener('drop', function(e){
    var cel = e.target.closest ? e.target.closest('.zdjecie-ramka') : null;
    if (!cel) return;
    e.preventDefault(); cel.classList.remove('ed-nad');
    var dane = e.dataTransfer;
    if (dane.files && dane.files[0]) zPliku(dane.files[0], cel);
    else {
      var adres = dane.getData('text/uri-list') || dane.getData('text/plain');
      if (adres) wstaw(cel, adres.trim());
    }
  });
})();
</script>
'''

# --- złożenie pliku ---
wynik = zrodlo.replace('</head>', STYL + '</head>', 1)
wynik = wynik.replace('<body>', '<body data-edycja="nie" data-przenoszenie="nie" data-panel="nie">\n' + PANEL, 1)
wynik = wynik.replace('</body>', SKRYPT + SKRYPT_ZDJEC + '</body>', 1)
wynik = wynik.replace('<title>Szablon broszury A4 — wersja do druku (fonty osadzone)</title>',
                      '<title>Edytor broszury PCTP</title>', 1)

(katalog / 'edytor-broszury.html').write_text(wynik, encoding='utf-8')
print('Zapisano: edytor-broszury.html', round(len(wynik)/1024), 'KB')
