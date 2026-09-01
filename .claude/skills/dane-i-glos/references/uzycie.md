# Gdzie i jak wstawiać dane autorki

Wszystko pochodzi z `assets/dane.json` — jedno źródło prawdy. Nigdy nie
przepisuj adresu ani telefonu z pamięci; wczytaj plik i użyj pól.

## Stopka dokumentu Word / PDF

Pod ostatnią sekcją, mniejszym stopniem pisma, kolorem `marka.fiolet`:

```
Opracowanie: Mirosława Ewa Jurczyszyn · Pomorskie Centrum Terapii Pedagogicznej w Koszalinie
kontakt@eduplaner2026.pl · [telefon — plik prywatny]
```

W dokumentach z podpisami (WOPF, IPET) obowiązuje konwencja PCTP: **linia NAD
etykietą** — miejsce na odręczny podpis jest wyżej, opis roli niżej.

## Podpis odręczny na dokumencie

Cztery gotowe wersje w `assets/`, wszystkie jako krzywe (żaden font nie musi
być zainstalowany, polskie znaki są w środku):

| Plik | Charakter | Dobre do |
|---|---|---|
| `podpis-odreczny.svg` | żywy, pisany długopisem | przedmowy, listy, materiały dla nauczycieli |
| `podpis-kaligraficzny.svg` | ozdobny, pełny zamach | certyfikaty, dyplomy, strony tytułowe |
| `podpis-klasyczny.svg` | wąski, klasyczny | stopki dokumentów, wizytówki |
| `podpis-lekki.svg` | cienki, oszczędny | tam, gdzie podpis ma nie dominować |

W dokumencie wstaw go **nad** linią podpisu, w wysokości 14–18 mm. W materiale
ekranowym: 120–180 px wysokości. Kolor zmienia się jednym atrybutem `fill`
w pliku SVG — domyślnie ciemna zieleń `#243F2C`, do dokumentów EduPlaner
podmień na fiolet `#2D1B69`.

## Plansza końcowa filmu

```
Mirosława Ewa Jurczyszyn
Pomorskie Centrum Terapii Pedagogicznej · Koszalin
kontakt@eduplaner2026.pl · [telefon — plik prywatny]
```

Nazwisko krojem nagłówkowym (Figtree 800, 40 px), reszta mniejszym, w kolorze
przygaszonym. Nad tekstem — podpis odręczny, jeśli plansza ma być osobista.

## Stopka prezentacji HTML

Na okładce i na ostatnim slajdzie, w pasku dolnym:
`Opracowanie: Mirosława Ewa Jurczyszyn · PCTP Koszalin`

## Stopka e-maila

```
Mirosława Ewa Jurczyszyn
pedagog specjalny · Pomorskie Centrum Terapii Pedagogicznej
tel. [telefon — plik prywatny] · kontakt@eduplaner2026.pl
```

## Logo

Do czasu wgrania pliku (`assets/logo/`) materiały używają samego podpisu i nazwy.
Gdy logo się pojawi: na dokumentach w prawym górnym rogu strony tytułowej
(wysokość 12–16 mm), w filmach na planszy końcowej obok nazwiska, w prezentacji
na okładce, przy dolnej krawędzi.

## Czego pilnować

- **„Pomorskie Centrum Terapii Pedagogicznej”** — pełna nazwa przy pierwszym
  wystąpieniu w dokumencie, potem można skracać do PCTP.
- Telefon zapisujemy z odstępami: `[telefon — plik prywatny]`.
- Nazwisko zawsze w pełnej formie: **Mirosława Ewa Jurczyszyn** — bez inicjałów.
- Materiały dla placówek kończymy formułą praw z `formuly.prawa`.
