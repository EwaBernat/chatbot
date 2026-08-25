# Plik z treścią — opis pól

Jeden plik JSON, kodowanie UTF-8. Kompletny przykład: `assets/tresc-arystoteles.json`.
Pusty szkielet: `assets/tresc-szablon.json`.

W polach tekstowych wolno używać `<strong>`, `<em>` i `<br>`. Reszta HTML-a nie jest
potrzebna i łatwo nią zepsuć skład.

## meta

| Pole | Co to | Przykład |
|---|---|---|
| `seria` | nazwa serii, w żywej paginie | `"Mała Filozofia"` |
| `tom` | numer, na stronie redakcyjnej | `1` |
| `tom_slownie` | na okładce i stronie tytułowej | `"Tom pierwszy"` |
| `tytul` | tytuł z `<br>` do łamania na okładce | `"Spotkanie<br>z Arystotelesem"` |
| `tytul_plaski` | ten sam bez `<br>` — pagina, PDF, metryka | `"Spotkanie z Arystotelesem"` |
| `podtytul` | jedno zdanie, bez kropki na końcu | |
| `bohater` | podpis pod portretem na stronie 5 | `"Arystoteles ze Stagiry"` |
| `lata` | daty życia, tam samo | `"384–322 p.n.e."` |
| `odbiorca` | zdanie na stronie tytułowej i redakcyjnej | |
| `wydawca_skrot` | przy znaku wydawcy | `"PCTP"` |
| `wydawca_opis` | tekst pola do uzupełnienia | |

## wstep

```json
"wstep": {
  "tytul": "Ta książeczka czyta się powoli",
  "zdania": ["…", "…"],          // dokładnie 6
  "zasady": ["…"]                // dokładnie 5, zdania zaczynające się od "Możesz…"
}
```

## os_czasu

```json
"os_czasu": {
  "tytul": "Życie Arystotelesa w ośmiu punktach",
  "lead": "…", "podpis": "…", "stopka": "…",
  "punkty": [
    {"rok":"384", "jednostka":"p.n.e.", "opis":["Rodzi się","w Stagirze"],
     "kolor":"szafran", "duzy": true}
  ],
  "karty": [{"tytul":"Skąd pochodził", "opis":"…"}]     // dokładnie 4
}
```

`punkty` — najlepiej 8, przy 6–10 też się rozłoży. `opis` maksymalnie dwie linie,
każda do jakichś 18 znaków, bo rysowane jest jako tekst w SVG i nie zawija się samo.
`kolor`: `morze`, `szafran`, `oliwka` albo `glina`. `duzy` powiększa kropkę —
używaj dla narodzin i śmierci.

## termometr

```json
"termometr": {"podpis": "zdanie wiążące skalę 0–10 z myślą filozofa"}
```

Sama skala jest wspólna dla całej serii i nie podlega zmianie.

## rozdzialy — dwanaście obiektów

```json
{
  "nr": 1,
  "emocja_label": "Ciekawość",              // do paginy i spisu treści
  "tytul": "Chłopiec w domu lekarza",
  "svg": "<svg viewBox=\"0 0 640 190\" …>", // ilustracja sceny
  "fig_etykieta": null,                     // "Infografika 3 · złoty środek" gdy to infografika
  "fig_caption": null,                      // podpis pod rysunkiem
  "scena":  ["…"],                          // 14 zdań
  "cytat": "Wszyscy ludzie z natury dążą do poznania.",
  "cytat_zrodlo": "Arystoteles, „Metafizyka”, księga I",
  "mysl":   ["…"],                          // 10 zdań
  "emocja_nazwa": "Ciekawość",              // duża plakietka w sekcji 3
  "emocja": ["…"],                          // 7 zdań
  "zycie":  ["…"],                          // 6 zdań
  "pytania": [["1", "treść pytania"]],      // 5 par [numer, treść]
  "tabela": null                            // opcjonalna <table>, trafia na stronę C
}
```

`fig_etykieta` decyduje o układzie: gdy jest, rysunek dostaje pełną szerokość kolumny
(dla infografik z drobnym tekstem); gdy jej nie ma, rysunek jest wyśrodkowaną winietą
i pod sekcją „Scena" pojawia się ozdobnik z listków.

`pytania` — numery jako napisy, ciągiem 1–60 przez całą broszurę. Rozdział 1 dostaje
1–5, rozdział 2 → 6–10 i tak dalej.

`tabela` — surowy `<table>` z `<thead>` i `<tbody>`. Skład bierze pierwsze trzy wiersze,
bo tyle mieści się na stronie C obok pytań.

## hasla

Dwanaście tablic czteroelementowych: `[numer, "emocja", "cytat bez cudzysłowów", "zdanie po ludzku"]`.
Cudzysłowy dokłada skład.

## slownik

Lista par `["Słowo", "Wyjaśnienie jednym–dwoma zdaniami."]`. Kolejność dowolna,
najlepiej w kolejności pojawiania się w tekście. 10–14 pozycji mieści się na stronie.

## nota

Cztery pary `["Nagłówek grupy", "Treść."]`: cytaty z dzieł, myśli przypisywane,
status scen, wskazówka do dalszej lektury.

## gra

```json
"gra": {
  "tytul": "Emocje według Arystotelesa",
  "lead": "…",
  "kostka_miary_lead": "zdanie wiążące kostkę z nauką filozofa o właściwej mierze",
  "kostka_emocji": [["ciekawość","chcę sprawdzić"]],       // dokładnie 6 par
  "karty": [[1, "ciekawość", "Opowiedz o…", 9]],           // dokładnie 12
  "plansza_emocje": ["ciekawość", "…"]                     // dokładnie 12, w kolejności rozdziałów
}
```

Czwarta wartość w karcie to numer strony rozdziału: 9, 12, 15, 18, 21, 24, 27, 30,
33, 36, 39, 42. Przy niezmienionej paginacji zawsze taka sama.

`plansza_emocje` to krótkie nazwy na pola planszy — mieszczą się dwa wiersze po
dwanaście znaków, więc „smutek i wdzięczność" skróć do „wdzięczność".

## tyl_okladki

```json
"tyl_okladki": {
  "lead": "akapit-zajawka, 3 zdania",
  "punkty": ["…"],                 // 4–5 wypunktowań
  "cytat": "bez cudzysłowów",
  "cytat_zrodlo": "…"
}
```

## svg

```json
"svg": {"okladka": "<svg viewBox=\"0 0 800 470\" …>"}
```

Portret bohatera. Pojawia się dwa razy: na okładce w pełnej wielkości i na stronie 5
jako mniejszy frontispis z podpisem `bohater · lata`.
