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
python3 broszura-lektura-autyzm/scripts/zloz_broszure.py dane.json --out broszura.html
python3 broszura-lektura-autyzm/scripts/sprawdz_sklad.py broszura.html \
        --dopasuj-linie linie.json --pdf broszura.pdf
python3 broszura-lektura-autyzm/scripts/zloz_broszure.py dane.json --out broszura.html \
        --linie linie.json
```

`assets/maly-ksiaze.json` to kompletny, działający przykład (27 rozdziałów → 107 stron A4).
Najszybsza droga do nowej lektury: skopiować go i podmienić treść.

### Co jest sprawdzane automatycznie

`sprawdz_sklad.py` wykrywa trzy rzeczy, których nie widać w przeglądarce, a które psują druk:
niedomknięty HTML, sekcję przekraczającą 297 mm oraz niezgodność liczby stron PDF
z liczbą sekcji (czyli puste albo rozlane strony).

### Weryfikacja

| Lektura | Rozdziałów | Sekcji | Stron PDF | Najwyższa strona |
|---|---|---|---|---|
| Mały Książę | 27 | 107 | 107 | 296,1 mm |
| Opowieść wigilijna (test) | 5 | 34 | 34 | 294,8 mm |
