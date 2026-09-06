# Skille

## broszura-lektura-autyzm

Generator broszury-adaptacji lektury szkolnej dla uczniów ze spektrum autyzmu.
Powstał z broszury „Mały Książę moim bohaterem — podróż emocjonalna”
(`broszury/maly-ksiaze/`), uogólnionej tak, by obsłużyć dowolną lekturę.

### Instalacja

Plik `broszura-lektura-autyzm.skill` można wgrać do Claude (przycisk **Save skill**
na karcie pliku) albo rozpakować katalog `broszura-lektura-autyzm/` do `~/.claude/skills/`.

### Użycie bez Claude

```bash
python3 broszura-lektura-autyzm/scripts/zloz_broszure.py dane.json --out broszura.html --skala 1.15
python3 broszura-lektura-autyzm/scripts/sprawdz_sklad.py broszura.html \
        --dopasuj-linie linie.json --pdf broszura.pdf
python3 broszura-lektura-autyzm/scripts/zloz_broszure.py dane.json --out broszura.html \
        --skala 1.15 --linie linie.json
```

`assets/maly-ksiaze.json` to kompletny, działający przykład (27 rozdziałów → 107 stron A4).
Najszybsza droga do nowej lektury: skopiować go i podmienić treść.

### Powiększony druk

`--skala 1.15` powiększa stopień pisma o 15% (tekst główny 13,1 pt zamiast 11,4 pt).
Skalowane są tylko wartości w punktach — siatka i marginesy zostają w milimetrach,
więc proporcje strony A4 się nie zmieniają. Po zmianie skali trzeba przeliczyć linie
na notatki (`--dopasuj-linie`), bo inaczej dolne partie stron się rozjadą.

### Co jest sprawdzane automatycznie

`sprawdz_sklad.py` wykrywa trzy rzeczy, których nie widać w przeglądarce, a które psują druk:
niedomknięty HTML, sekcję przekraczającą 297 mm oraz niezgodność liczby stron PDF
z liczbą sekcji (czyli puste albo rozlane strony).

### Weryfikacja

| Lektura | Rozdziałów | Skala pisma | Sekcji | Stron PDF | Najwyższa strona |
|---|---|---|---|---|---|
| Mały Książę | 27 | 1,15 (powiększony) | 115 | 115 | 291,1 mm |

Skrypt `sprawdz_sklad.py` sprawdza wysokość z zapasem 292 mm zamiast pełnych 297 mm —
silnik druku zaokrągla wysokości i strona ocierająca się o krawędź arkusza i tak się rozlewa.
