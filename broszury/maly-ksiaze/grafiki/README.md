# Grafiki do broszury

Wrzuć tu pliki graficzne (PNG, JPEG, WebP). Nazwy bez polskich znaków i spacji,
np. `okladka.png`, `rozdzial-21-lis.jpg`.

Najprościej przez przeglądarkę — nie trzeba niczego instalować:
**https://github.com/EwaBernat/chatbot/upload/claude/maly-ksiaze-autyzm-broszura-o9x00t/broszury/maly-ksiaze/grafiki**
przeciągnij pliki, potem zielony przycisk **Commit changes** na dole.

## Jak podpiąć grafikę do broszury

W pliku `skille/broszura-lektura-autyzm/assets/maly-ksiaze.json`:

```json
"meta": { "okladka_obraz": "grafiki/okladka.png" }
```

a przy wybranym rozdziale:

```json
{ "nr": 21, "obraz": "grafiki/rozdzial-21-lis.jpg" }
```

Potem skład:

```bash
python3 skille/broszura-lektura-autyzm/scripts/zloz_broszure.py \
        skille/broszura-lektura-autyzm/assets/maly-ksiaze.json \
        --out broszury/maly-ksiaze/maly-ksiaze-broszura.html \
        --skala 1.15 --grafiki broszury/maly-ksiaze \
        --linie skille/broszura-lektura-autyzm/assets/maly-ksiaze-linie.json
```

## Rozmiar

Grafiki są wklejane do środka pliku HTML, żeby broszura pozostała jednym dokumentem.
Plik rośnie o mniej więcej jedną trzecią rozmiaru zdjęć — przed wgraniem warto je zmniejszyć
do szerokości ok. 1600 px (okładka 2000 px).
