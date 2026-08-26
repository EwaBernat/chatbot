# Katalog komponentów

Sprawdzone układy z części 1. Kopiuj i wypełniaj treścią — dzięki temu kolejne części
składają się z tych samych klocków i wyglądają jak jedna seria.

## Spis treści

Cztery części, każda z własnym kolorem, pozycje z opisem i kropkowanym wiodącym.

```html
<div class="spis">
  <div style="--rail:var(--tue)">
    <div class="czesc__h"><span class="czesc__n">I</span><span class="czesc__t">Zrozumieć</span><span class="czesc__s">podstawy</span></div>
    <div class="poz"><span class="poz__t"><b>Czym jest teoria umysłu</b> <span>— definicja, od której wszystko się zaczyna</span></span><i></i><span class="poz__p">3</span></div>
  </div>
</div>
```

Kolory części po kolei: `--tue`, `--gold`, `--tuk`, `--tus`.
Pod spisem: karta ze skrótami (`.skroty`, dwie kolumny) i ramka „Jak korzystać z broszury?".

## Karta ćwiczenia

```html
<div class="ex ex--tue">
  <div class="ex__head"><span class="ex__no">01</span><h3>Lustro emocji</h3><span class="tag tag--tue">TUE</span></div>
  <div class="ex__body">
    <p><b>Cel</b>Rozpoznanie emocji na własnej twarzy i w ciele.</p>
    <p><b>Materiały</b>Lusterko dla każdego dziecka, 4 karty emocji.</p>
    <p><b>Przebieg</b>1. Pokazujesz kartę i nazywasz emocję. 2. Dzieci robią minę do lusterka. …</p>
    <p><b>Kryterium</b>Dziecko trafnie robi i nazywa 4 miny w 4 z 5 prób.</p>
    <p><b>Wersja łatwiejsza</b>2 emocje, model dorosłego obok lustra.</p>
  </div>
</div>
```

Warianty: `ex--tue`, `ex--tuk`, `ex--tus`. `<b>` w `.ex__body` renderuje się jako
mała etykieta wersalikowa nad tekstem — dlatego treść idzie **zaraz po** znaczniku, bez spacji.

**Sześć kart w `.grid.g2` wypełnia stronę A4** (trzy wiersze po dwie) i zostaje ok. 100 px zapasu.

## Tabela norm wiekowych

```html
<div class="tbl-wrap">
<table>
  <thead><tr><th style="width:17mm">Wiek</th><th style="width:44mm">Co się rozwija? (norma)</th><th>Jak to wygląda w praktyce?</th><th style="width:48mm">Częsty obraz w autyzmie</th></tr></thead>
  <tbody>
    <tr><td class="age">9–14 mies.</td><td><strong>Wspólne pole uwagi</strong></td><td>…</td><td>…</td></tr>
    <tr style="background:var(--tuk-soft)"><td class="age">4–5 lat</td><td><strong>FAŁSZYWE PRZEKONANIE</strong></td><td>…</td><td>…</td></tr>
  </tbody>
</table>
</div>
```

`td.age` daje pogrubiony wiek z cyframi tabelarycznymi. Kamień milowy wyróżniaj
tłem wiersza w kolorze filaru, nie pogrubieniem całego tekstu.

## Tabela „zamiast → powiedz"

```html
<table class="swap">
  <thead><tr><th style="width:50%">Zamiast tego ⟶</th><th>Powiedz to</th></tr></thead>
  <tbody><tr><td>„Zachowuj się!"</td><td>„Usiądź na krześle. Ręce połóż na stole."</td></tr></tbody>
</table>
```

`.swap` koloruje pierwszą kolumnę na różowo, drugą na zielono — czytelniczka widzi kierunek
zmiany bez czytania nagłówka.

## Ramki

```html
<div class="callout callout--warn">   <!-- złota: uwaga, pułapka, ostrzeżenie -->
  <span class="kicker" style="color:var(--gold)">Uwaga na skrót</span>
  <p style="font-size:9.00pt">…</p>
</div>

<div class="callout callout--law">    <!-- fioletowa: podstawa prawna, kompetencje -->
  <span class="kicker" style="color:var(--tuk)">Kto to robi w szkole?</span>
  <p style="font-size:9.00pt">…</p>
</div>
```

Karty: `.card` z wariantami `card--tue`, `card--tuk`, `card--tus`, `card--gold`, `card--plain`.

## Schemat kroków (stepper)

```html
<div class="kroki">
  <div class="krok" style="--kolor:var(--tue)">
    <span class="krok__n">1</span>
    <div><h5>Obserwuj i zapisuj</h5><p>Trzy sytuacje, trzy różne dni…</p></div>
  </div>
</div>
```

Kółka łączy pionowa linia. Dobre do procedur: od obserwacji do IPET, od zgłoszenia do poradni.

## Makieta dokumentu

Do pokazania wzoru zapisu (fragment WOPFU, cel do IPET) — wygląda jak wydruk, więc czytelniczka
od razu widzi, że to do skopiowania:

```html
<div class="dok">
  <div class="dok__bar"><span>WOPFU · fragment</span><span>wzór do skopiowania</span></div>
  <div class="dok__body"><div><b>Mocne strony:</b> …</div><div><b>Trudności:</b> …</div></div>
  <div class="dok__note"><strong>Cel do IPET z kryterium:</strong> „…"</div>
</div>
```

## Wykresy

Generuj przez `scripts/wykresy.py`:

```bash
python3 scripts/wykresy.py slupki  "2;6=20,3;0=30,4;0=57,5;0=78" --prog 50 > w.svg
python3 scripts/wykresy.py pierscien "TUE=50,TUK=30,TUS=20" > w.svg
python3 scripts/wykresy.py skumulowany "Poziom I=70/20/10;Poziom II=50/30/20" > w.svg
```

Osadzaj w `<figure>` z tytułem, legendą i podpisem:

```html
<figure>
  <span class="fig-title">Kiedy dzieci zaczynają rozumieć fałszywe przekonanie?</span>
  <!-- svg -->
  <div class="legend"><span><i class="sw" style="background:#C4547A"></i>TUE — emocje 50%</span></div>
  <figcaption>Wartości orientacyjne wg metaanalizy Wellman, Cross, Watson (2001).</figcaption>
</figure>
```

Zasady, które trzymają wykresy czytelnymi: etykiety procentów **na pierścieniu** (białe,
pogrubione), nie obok niego — obok kolidują z legendą; przy dwóch i więcej seriach zawsze
legenda; jedna seria legendy nie potrzebuje, bo nazywa ją tytuł.

## Karta obserwacji jako formularz

Kluczowa różnica wobec zwykłej tabeli: to ma być **wypełnialne po wydrukowaniu**.
Każdy wiersz ma kratki `<span class="box">` w kolumnach `sc`, kropkowaną linię na notatkę
w kolumnie `nt` i numer w kolumnie `lp`. Pozycje pogrupowane wierszami `.grp` z paskiem
w kolorze filaru i polem sumy.

```html
<tr class="grp g-tue">
  <td class="lp"></td><td class="nm"><span class="tag tag--tue">TUE</span> <b>Emocje — co on czuje?</b></td>
  <td class="sc sc--a sc--z och" colspan="4">0 – 3</td>
  <td class="nt"><span class="suma">razem <em></em> / 18</span></td></tr>
<tr class="it g-tue"><td class="lp">1</td><td class="nm">Nazywa 4 emocje podstawowe u siebie</td>
  <td class="sc sc--a"><span class="box"></span></td><td class="sc"><span class="box"></span></td>
  <td class="sc"><span class="box"></span></td><td class="sc sc--z"><span class="box"></span></td>
  <td class="nt"><i></i></td></tr>
```

Wiersze parzyste dostają klasę `alt` (delikatny pas prowadzący wzrok przez szeroki wiersz).
Pod tabelą: pola sum `.wynik-box` dla każdego filaru, pole ustalonego poziomu, miejsce
na wniosek i trzy linie na podpisy.

## Buźki i termometr emocji

`scripts/buzki.py` rysuje dwa zestawy twarzy jako SVG — bez plików graficznych, więc drukują się ostro
w każdym rozmiarze i nie powiększają pliku:

```bash
python3 scripts/buzki.py radosc "#C4547A"     # radosc, smutek, zlosc, strach, zdziwienie
python3 -c "import sys;sys.path.insert(0,'scripts');from buzki import intensywnosc;print(intensywnosc(4,'#C4547A'))"
```

- `twarz(emocja, kolor)` — pięć emocji do kart pracy i tablicy emocji.
- `intensywnosc(n, kolor)` — pięć min pokazujących **natężenie** odczucia (1 spokój → 5 bardzo mocno).
  Termometr mierzy siłę, nie rodzaj emocji, dlatego wymaga osobnego zestawu.

Termometr emocji buduj jako **jeden SVG** z rurką, bańką, polami w rampie jednego odcienia
(jasny → nasycony), twarzami natężenia po prawej i kratkami do zaznaczenia. Trzymanie wszystkiego
w jednym SVG rozwiązuje problem, który przy układzie z osobnych elementów HTML wraca zawsze:
twarze i kratki rozjeżdżają się z podziałką przy każdej zmianie szerokości kolumny.
Zagnieżdżone `<svg x= y= width= height=>` pozwala wstawić gotową twarz w wyliczonym miejscu.

Na jasnych polach rampy rysuj twarze kolorem `--ink2`, nie kolorem pola — inaczej znikają.

## Stopka wydawnicza (ostatnia strona)

Blok z logo PCTP, autorką, adresem, tytułem broszury, nadtytułem serii i plakietką numeru części,
a pod nim jedno zdanie: „Materiał ma charakter informacyjno-metodyczny. Nie zastępuje diagnozy
specjalistycznej ani wykładni przepisów prawa oświatowego."

## Strona załącznika (plansza na całą kartkę)

Narzędzie, które dziecko realnie obsługuje — koło ze strzałką, plansza z pionkami,
karty do trzymania w ręku — dostaje **własną stronę na końcu broszury**, obok wersji
opisowej w środku. W środku zostaje instrukcja i tabela „kiedy czego używać";
w załączniku sama plansza, tak duża, jak pozwala arkusz.

```html
<section class="page page--zal">
  <div class="page__body">
    <div>
      <div class="eyebrow">Załącznik 1 · do wydrukowania w powiększeniu</div>
      <h2 class="h-sec">Koło emocji w rozmiarze A4</h2>
      <p class="lead" style="margin-top:3px">To samo koło co na s. 15…</p>
    </div>
    <div class="zal-plansza">
      <!-- SVG planszy -->
    </div>
  </div>
  <div class="page__foot">…<span class="num">30</span></div>
</section>
```

```css
.page--zal .page__body{gap:6px}
.zal-plansza{flex:1; display:flex; align-items:center; justify-content:center;
  border:1.4px dashed var(--tuk-mid); border-radius:14px; background:#FFFDFB; padding:8px}
.zal-plansza > svg{width:100%; height:auto; max-height:100%}
```

Trzy rzeczy, na których łatwo się przewrócić:

1. **Selektor `>` jest konieczny.** `.zal-plansza svg` łapie także zagnieżdżone `<svg class="buzka">`
   wewnątrz planszy i rozdmuchuje je do szerokości strony. Rysunek rozpada się w sposób,
   który na pierwszy rzut oka wygląda jak błąd generatora, a nie jak kolizja CSS.
2. **Kopiując SVG, zmień identyfikatory.** `href="#luk0"` odsyła zawsze do pierwszego elementu
   o tym `id` w całym dokumencie — kopia koła bez zmiany `id` pobiera łuki oryginału
   i podpisy lądują poza tarczą. Prefiksuj: `luk0` → `zluk0`.
3. **Wycinając SVG z pliku, licz zagnieżdżenia.** Pierwsze `</svg>` po otwarciu tagu zamyka
   zagnieżdżoną buźkę, nie całą planszę. Szukaj domknięcia przez zliczanie `<svg` i `</svg>`.

Budżet pionowy strony załącznika: pole treści ≈ 1048 px, z tego nagłówek z leadem ≈ 90 px
i stopka ≈ 34 px. Na samą planszę zostaje **ok. 900 px** — przy pełnej szerokości 703 px
oznacza to proporcję nie wyższą niż 1,28. Plansza pionowa wyższa niż to nie zmieści się,
choćby skrypt pomiarowy pokazywał tylko kilkanaście pikseli przepełnienia.

Karty do wycinania w załączniku: siatka `repeat(3,1fr)`, `min-height:55mm` na kartę,
buźka 16 mm, numer 19 pt, tekst 12 pt i dwie linie do zapisania odpowiedzi.
Dwanaście kart wypełnia wtedy dokładnie jedną stronę.

Ramka karty do wycinania jest **grubsza niż ramka karty w środku broszury**: `2.4px dashed`
w nasyconym kolorze rodziny emocji plus delikatny cień. Przerywana linia ma być linią cięcia,
a nie ozdobą — przy 1,4 px gubi się przy druku i trudno po niej trafić nożyczkami.
