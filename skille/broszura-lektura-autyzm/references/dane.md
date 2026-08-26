# Format danych (JSON)

Kompletny działający plik: `assets/maly-ksiaze.json`. Najszybsza droga do nowej lektury to
skopiowanie go i podmiana treści — od razu widać oczekiwaną głębokość każdego pola.

Wszystkie teksty są zwykłym tekstem (bez HTML). Znaki `<`, `>`, `&` są bezpieczne — skrypt
je escapuje. W ćwiczeniach teorii umysłu `\n` w polu `tresc` oznacza nowy akapit.

## Szkielet

```json
{
  "meta": { ... },
  "wydawca": { ... },
  "postacie": [ ... ],
  "rozdzialy": [ ... ],
  "cwiczenia": [ ... ],
  "gra": { ... },
  "scenariusz": { ... },
  "zakonczenie": { ... }
}
```

## meta

| pole | opis |
|---|---|
| `tytul` | tytuł lektury, np. `"Mały Książę"` |
| `podtytul_okladki` | druga linia tytułu broszury, np. `"moim bohaterem"` |
| `haslo` | podtytuł pod tytułem, np. `"podróż emocjonalna"` |
| `nadtytul` | linia nad tytułem; domyślnie „Adaptacja lektury dla młodzieży ze spektrum autyzmu” |
| `zrodlo` | informacja o oryginale — tytuł, autor, rok |
| `okladka_svg` | nazwa funkcji z `svg.py` albo gotowy inline SVG (patrz `ilustracje.md`) |
| `na_okladce` | lista 5–7 haseł na okładkę |
| `odbiorcy` | dla kogo, np. `"uczniowie 12–19 lat ze spektrum autyzmu, klasy VII–VIII"` |
| `zastosowanie` | gdzie użyć, np. `"lekcje polskiego, rewalidacja, TUS, świetlica"` |
| `uwaga_trudne_tematy` | które rozdziały wymagają uprzedzenia i dlaczego (może być pusty) |

## wydawca

```json
"wydawca": {
  "organizacja": "Pomorskie Centrum Terapii Pedagogicznej",
  "autorka": "Mirosława Ewa Jurczyszyn",
  "mail": "kontakt@eduplaner2026",
  "skrot": "PCTP",
  "logo_svg": "logo_pctp"
}
```

`skrot` trafia do stopki każdej strony. `logo_svg` to nazwa funkcji z `svg.py`
(`logo_pctp`) albo inline SVG w kwadracie `viewBox="0 0 200 200"`.

## postacie

```json
{ "nazwa": "Lis", "ikona": "fox",
  "kim": "Zwierzę, które uczy najważniejszej rzeczy.",
  "zachowanie": "Spokojny, cierpliwy, mówi wprost i konkretnie. Podaje instrukcję krok po kroku.",
  "rola": "Jedyna postać, która tłumaczy zasady relacji tak, że da się je zastosować." }
```

## rozdzialy — pełny przykład

```json
{
  "nr": 7,
  "tytul": "Kłótnia o kolce",
  "miejsce": "Pustynia Sahara · 5. dzień",
  "ikona": "thorn",
  "ilustracja": null,
  "mysl": "Kiedy dwie osoby myślą o dwóch różnych sprawach, łatwo o kłótnię.",

  "streszczenie": [
    "Piątego dnia Mały Książę pyta, czy baranek zjada kwiaty z kolcami.",
    "Narrator naprawia silnik i jest zmęczony. Odpowiada byle jak."
  ],

  "slowka": [
    { "pojecie": "kolce",
      "wyjasnienie": "Ostre igły na łodydze róży. Chronią kwiat przed zwierzętami." },
    { "pojecie": "„poważne sprawy”",
      "wyjasnienie": "Tak dorośli nazywają swoje zajęcia. Mały Książę uważa, że one wcale nie są najważniejsze." }
  ],

  "emocje": [
    { "kto": "Narrator", "emocja": "zniecierpliwienie",
      "sygnal": "mówi „nie zawracaj mi głowy”", "poziom": 4 },
    { "kto": "Mały Książę", "emocja": "rozpacz",
      "sygnal": "płacze, nie może mówić", "poziom": 5 }
  ],

  "zaleznosci": "Pierwsza prawdziwa kłótnia. Każdy myśli o czym innym…",

  "wnioski": [
    { "przyczyna": "Narrator myślał tylko o silniku",
      "skutek": "odpowiedział krótko i lekceważąco" }
  ],

  "ocena": {
    "pytanie": "Kto zachował się źle w tej kłótni?",
    "odpowiedz": "ŻÓŁTE po obu stronach. Narrator odpowiedział lekceważąco… Obaj mieli powody i obaj mogli zrobić to lepiej."
  },

  "tom": {
    "etap": 4,
    "tytul": "Dwie głowy, dwie myśli",
    "tresc": "Narysuj albo napisz w dwóch chmurkach:\n\n① O czym MYŚLI narrator?\n② O czym MYŚLI Mały Książę?\n③ Czy narrator wie, o czym myśli chłopiec?"
  },

  "pytania_latwe":  ["O co pyta Mały Książę?", "Co robił narrator w tym czasie?"],
  "pytania_trudne": ["Dlaczego Mały Książę tak bardzo się rozzłościł o kolce?"]
}
```

`ocena.odpowiedz` **musi zaczynać się** od `ZIELONE`, `ŻÓŁTE` albo `CZERWONE` — po tym słowie
dobierany jest kolor i znak bloku. `tom.etap` to liczba 1–5.

## cwiczenia

```json
{ "nr": 1, "tytul": "Karty emocji", "cel": "Rozpoznawanie i nazywanie emocji",
  "czas": "15 min", "forma": "indywidualnie lub w parach",
  "opis": "Przygotuj 12 kartoników…",
  "kroki": ["Uczeń losuje kartonik…", "Szuka w broszurze rozdziału…"],
  "dostosowanie": "Uczniom niemówiącym daj karty z gotowymi zdaniami do wskazania…" }
```

Skrypt układa po dwa ćwiczenia na stronę, więc ich liczba może być dowolna.

## gra

```json
"gra": {
  "nazwa": "Podróż Małego Księcia",
  "wstep": "Gra planszowa na 30 pól…",
  "zasady": ["Gramy 2–5 osób…", "NIKT NIE WYPADA Z GRY…"],
  "talie": [
    { "nazwa": "EMOCJE",         "kolor": "#6FC5A0", "karty": ["…", "…"] },
    { "nazwa": "WNIOSKI",        "kolor": "#E3B23C", "karty": ["…"] },
    { "nazwa": "OCENA SYTUACJI", "kolor": "#1F8A63", "karty": ["…"] },
    { "nazwa": "CO MYŚLI?",      "kolor": "#D96D8B", "karty": ["…"] }
  ],
  "pola_specjalne": [ { "pole": "Pole 21 — Lis", "opis": "Wybierz gracza i powiedz mu…" } ]
}
```

Cztery talie i te cztery kolory są związane z kolorami pól na planszy — nie zmieniaj ich,
bo plansza rysuje się z tej samej palety.

## scenariusz

```json
"scenariusz": {
  "tytul": "Mały Książę — podróż emocjonalna",
  "info": { "czas": "ok. 25–30 minut", "obsada": "od 12 do 30 osób (role skalowalne)",
            "proby": "8 prób po 45 minut", "muzyka": "spokojna, instrumentalna, stała głośność" },
  "obsada": [ { "rola": "Chór Gwiazd (4–8 osób)",
                "opis": "rola bez tekstu indywidualnego: wspólne zdania chórem" } ],
  "uwaga_obsada": "Klasa mniejsza — jedna osoba gra dwie role…",
  "zasady":    ["Każdy uczeń ma rolę, ale nikt nie musi mówić…"],
  "rekwizyty": ["Duży karton pomalowany na zielono — planeta"],
  "proby":     [ { "nazwa": "Próba 1", "opis": "Czytanie całości przy stole. Nikt nie wstaje." } ],
  "sceny": [
    { "nr": 1, "tytul": "Rysunek numer jeden",
      "miejsce": "Przed kurtyną. Światło ciepłe.",
      "osoby": "Narrator I, Narrator II",
      "kwestie": [ { "kto": "NARRATOR I", "tekst": "Kiedy miałem sześć lat, narysowałem węża." } ],
      "wskazowka": "Narratorzy stoją nieruchomo, mówią do publiczności." }
  ]
}
```

Sceny 1 i 2 trafiają na wspólną stronę, każda następna dostaje własną — dłuższe sceny nie
mieszczą się parami na A4.

## zalaczniki

Materiały do wycięcia na końcu broszury. Klucze `plansza`, `termometr`, `sygnalizator`
przyjmują `true`/`false`; `karty` to lista miejsc z lektury (po 4 na stronę).

```json
"zalaczniki": {
  "plansza": true, "termometr": true, "sygnalizator": true,
  "karty": [
    { "nazwa": "Planeta Króla", "ikona": "crown", "kto": "Król bez poddanych",
      "opis": "Król rządzi wszystkim, także gwiazdami. Wydaje tylko takie rozkazy, które i tak by się wykonały.",
      "pytanie": "Czym różni się prośba od rozkazu?" }
  ]
}
```

## zakonczenie

```json
"zakonczenie": {
  "cytat": "Dobrze widzi się tylko sercem. Najważniejsze jest niewidoczne dla oczu.",
  "cytat_zrodlo": "Lis, rozdział 21",
  "akapity": ["Ta broszura powstała po to, żeby…", "Niczego tu nie uproszczono…"]
}
```

## Ile stron wyjdzie

```
7  strony wstępne (okładka, spis ×2, jak korzystać ×2, narzędzia ×2)
+  3 × liczba rozdziałów
+  ceil(liczba ćwiczeń / 2)
+  ceil(liczba postaci / 4)   (karty postaci)
+  3  gra
+  4  scenariusz: tytuł i obsada, zasady, program, rekwizyty i próby
+  liczba scen           (każda scena na osobnej stronie)
+  załączniki: 1 plansza + 1 termometr + 1 krążki + ceil(karty / 4)
+  1  zakończenie
```

27 rozdziałów, 8 ćwiczeń, 8 scen, 8 kart miejsc → **115 stron**.
