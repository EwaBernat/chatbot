# Komponenty szablonu — gotowe do wklejenia

Spis: [Siatki](#siatki) · [Nagłówki slajdu](#naglowki-slajdu) · [Karty](#karty) ·
[Pasy podsumowania](#pasy-podsumowania) · [Boxy semantyczne](#boxy-semantyczne) ·
[Listy](#listy) · [Tabela](#tabela-porownawcza) · [Zamiast → powiedz](#zamiast--powiedz) ·
[Etapy wiekowe](#etapy-wiekowe) · [Procedura krok po kroku](#procedura-krok-po-kroku) ·
[Komiks](#komiks-svg) · [Dymki mowy i myśli](#dymki-mowy-i-mysli) ·
[Skala / termometr](#skala--termometr) · [Wykres obciążenia](#wykres-obciazenia) ·
[Okładka z grafiką](#okladka-z-grafika) · [Przypis](#przypis) · [Gęstość](#gestosc-slajdu)

Zasada nadrzędna: te klasy istnieją po to, żeby wszystkie slajdy wyglądały jak
jeden materiał. Nowy komponent twórz tylko wtedy, gdy żaden z poniższych nie
oddaje treści — a wtedy zbuduj go z istniejących tokenów (`var(--green)`,
`var(--line)`, `var(--ink-2)`), nie z nowych kolorów.

## Siatki
```html
<div class="cols c2">…</div>   <!-- 1:1 -->
<div class="cols c3">…</div>   <!-- trzy równe -->
<div class="cols c4">…</div>   <!-- cztery równe: moduły, etapy, tygodnie -->
<div class="cols c5">…</div>   <!-- pięć: oś etapów rozwojowych -->
<div class="cols c-73">…</div> <!-- szeroka lewa + wąska prawa (treść + panel) -->
<div class="cols c-37">…</div> <!-- wąska lewa + szeroka prawa -->
<div class="stack">…</div>     <!-- pionowo, równe odstępy -->
```

## Nagłówki slajdu
```html
<p class="eyebrow">Moduł II · Rozpoznanie</p>
<h2>Teza slajdu w jednym zdaniu</h2>
<p class="lead">Zdanie rozwijające, większe od treści kart.</p>
…
<div class="tag">Etykieta modułu</div><div class="num">09 / 25</div>
```
`eyebrow` sam dorysowuje linię do prawej krawędzi. `tag` i `num` są pozycjonowane
w stopce slajdu — wpisz je na końcu każdej sekcji.

## Karty
```html
<div class="card"><h3>Nagłówek</h3><p>Treść.</p></div>
<div class="card top"><span class="chip">Etykieta</span><h3 style="margin-top:11px">Nagłówek</h3><p>Treść.</p></div>
<div class="card soft"><p class="small">Wariant bez ramki, na szarym tle.</p></div>
```
`chip` ma warianty: `chip a` (bursztyn), `chip t` (zieleń), `chip s` (błękit),
`chip r` (czerwień). Używaj ich zgodnie ze znaczeniem, nie dla urozmaicenia.

## Pasy podsumowania
Ciemny pas to miejsce na zdanie, które uczestnik ma zapamiętać. Jeden na slajd.
```html
<div class="dark" style="display:flex;align-items:center;gap:24px">
  <span class="n" style="font-size:44px;color:var(--green-3)">&rarr;</span>
  <p class="lead" style="margin:0">Zdanie do zapamiętania. <strong>Wyróżnienie</strong>.</p>
</div>
```

## Boxy semantyczne
```html
<div class="two">
  <div class="box bad"><h3>✕ &nbsp;Unikaj</h3><ul class="dots">…</ul></div>
  <div class="box good"><h3>✓ &nbsp;Stosuj</h3><ul class="dots">…</ul></div>
</div>
<div class="box warn"><h3>Uwaga</h3><p>Ostrzeżenie, próg, ryzyko.</p></div>
```

## Listy
```html
<ul class="dots"><li>punkt z kropką</li></ul>
<ul class="ticks"><li>pozycja z kwadratem do odhaczenia — do checklist</li></ul>
```
`ticks` sygnalizuje, że slajd nadaje się do wydruku i wypełnienia.

## Tabela porównawcza
Najlepsze narzędzie do przesunięcia perspektywy: sytuacja / co widzi dorosły /
co dzieje się w dziecku / co działa.
```html
<table class="grid">
  <thead><tr><th style="width:20%">Sytuacja</th><th>Co widzi nauczyciel</th><th>Co dzieje się w dziecku</th><th>Co działa</th></tr></thead>
  <tbody><tr><td><b>Rozbita wieża</b></td><td>…</td><td>…</td><td>…</td></tr></tbody>
</table>
```

## Zamiast → powiedz
Najczęściej cytowany slajd każdego szkolenia. Po lewej zdanie odruchowe, po
prawej gotowe zdanie do wypowiedzenia.
```html
<div class="swap">
  <span class="no">„Przeproś Kubę.”</span><span class="ar">→</span>
  <span class="yes">„Kuba <strong>myślał</strong>, że wieża zostanie. Teraz jest smutny.”</span>
</div>
```

## Etapy wiekowe
```html
<div class="card top"><span class="age">4–6<span>LAT</span></span>
  <h3 style="margin-top:12px">Fałszywe przekonania</h3><p>…</p></div>
```
Etap bieżący wyróżnij bursztynem (`style="background:var(--amber)"` na `age`,
`border-top-color:var(--amber)` na karcie), etapy poza zakresem szkolenia
przygaś (`style="opacity:.72"`).

## Procedura krok po kroku
```html
<div class="steps">
  <div class="step"><div class="k"><span class="circ">1</span><h3 style="margin:0">Nazwa etapu</h3></div>
    <p>Co się dzieje.</p><p class="small" style="margin-top:9px;color:var(--green)"><strong style="color:var(--green)">ok. 5 min</strong></p></div>
  …
</div>
```

## Komiks SVG
Trzy panele w rzędzie tłumaczą test albo scenkę szybciej niż akapit. Figury
buduj z koła (głowa) i wycinka (tułów) — na 350 px szerokości panelu twarze i
tak się nie przeczytają, więc liczy się czytelny układ i podpisy.
```html
<div class="comic">
  <div class="panel">
    <svg viewBox="0 8 240 140" aria-label="Panel 1">
      <rect width="240" height="152" fill="#EFF4ED"/>
      <line x1="0" y1="124" x2="240" y2="124" stroke="#B7CCB2" stroke-width="2"/>
      <circle cx="52" cy="66" r="14" fill="#3E7B4F"/>
      <path d="M36 124 q0 -31 16 -31 q16 0 16 31 z" fill="#3E7B4F"/>
      <text x="30" y="145" font-family="Source Sans 3,sans-serif" font-size="12" font-weight="700" fill="#3E7B4F">ANNA</text>
    </svg>
    <div class="cap"><b>1.</b> Podpis panelu.</div>
  </div>
</div>
```
Ostatni panel — ten z pytaniem — wyróżnij tłem `#FBEEDC` i podpisem wersalikami.

## Dymki mowy i myśli
```html
<div class="bub say">Co ktoś <strong>mówi</strong><span class="tail"></span></div>
<div class="bub think">Co ktoś <strong>myśli</strong><span class="dots"><i></i><i></i></span></div>
```
Biały z ogonkiem = mowa, błękitny z kółeczkami = myśl. Kody kolorów muszą być
stałe w całym materiale, bo dziecko uczy się właśnie tej różnicy.

## Skala / termometr
```html
<div class="therm">
  <div class="lvl" style="background:#E4EEE1"><b>1</b><span>spokój</span></div>
  <div class="lvl" style="background:var(--amber-soft)"><b>3</b><span>umiarkowane — skracamy zadanie</span></div>
  <div class="lvl" style="background:var(--red-soft)"><b>5</b><span>bardzo silne — tylko regulacja</span></div>
</div>
```
Kolejność w kodzie jest odwrócona (`column-reverse`), więc 1 wpisz najpierw.

## Wykres obciążenia
Trzy paski pokazujące, ile zasobu zjadają bodźce, emocje i ile zostaje na
myślenie. Działa lepiej niż zdanie o „przeciążeniu".
```html
<div style="display:flex;justify-content:space-between;font-size:13px;color:var(--ink-2);margin-bottom:5px">
  <span>Hałas, tłok, światło</span><span style="color:var(--amber-ink);font-weight:700">obciążenie sensoryczne</span></div>
<div style="height:22px;background:var(--sage-2);border-radius:4px;overflow:hidden">
  <div style="width:62%;height:100%;background:var(--amber)"></div></div>
```

## Okładka z grafiką
Slajd tytułowy ma klasę `cover`; grafikę wstaw jako `<svg class="art">`. Lewą
krawędź grafiki wygasza maska, więc rysunek nie kończy się widoczną krawędzią.
Rysuj metaforę materiału (most, tory, pociąg), nie abstrakcyjne kształty.
```html
<svg class="art" viewBox="0 0 760 430" aria-hidden="true">
  <defs><radialGradient id="sun"><stop offset="0" stop-color="#84BE92" stop-opacity=".7"/>
    <stop offset="1" stop-color="#84BE92" stop-opacity="0"/></radialGradient></defs>
  <circle cx="466" cy="168" r="168" fill="url(#sun)"/>
  <!-- most: łuki + przęsło + filary -->
  <g stroke="#9CC4A6" stroke-width="7" fill="none"><path d="M250 250 A105 95 0 0 1 460 250"/></g>
  <rect x="90" y="238" width="580" height="13" fill="#E4EEE1"/>
</svg>
```

## Przypis
Gdy krótka nota koliduje z etykietą modułu w stopce, ustaw ją bezwzględnie po
prawej, zostawiając miejsce na numer slajdu:
```html
<p class="small" style="position:absolute;right:112px;bottom:20px;left:400px;text-align:right;margin:0;font-size:13px;color:var(--red)">
  <strong style="color:var(--red)">Uwaga:</strong> …</p>
```

## Gęstość slajdu
Slajd z zapasem miejsca (skrypt pomiarowy pokaże „pusto") powiększ klasą `big`
na sekcji: `<section class="slide big" …>` — rośnie typografia, odstępy i
padding kart, bez zmiany układu.

## Pas toru
Poziomy separator w motywie kolejowym — dobry zamiast zwykłej linii:
```html
<div class="track" style="margin:26px 0 22px"></div>
```
