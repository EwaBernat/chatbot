# Sala, która uczy każde dziecko

Broszura A4 (49 stron) łącząca organizację sali przedszkolnej według nowej podstawy programowej
z dostępnością i dostosowaniami dla dzieci ze zróżnicowanymi potrzebami.

## Pliki

- `sala_ktora_uczy_kazde_dziecko.html` — wersja źródłowa (jeden plik, zdjęcia i fonty osadzone)
- `sala_ktora_uczy_kazde_dziecko.pdf` — wersja do druku, A4, bez marginesów
- `zrodla/build.py` — generator broszury
- `zrodla/base_css.txt` — arkusz stylów z osadzonymi fontami (Quicksand, Nunito, Caveat)
- `zrodla/img/`, `zrodla/new/` — zdjęcia użyte w broszurze

## Struktura

| Strony | Zawartość |
|---|---|
| 01–03 | Okładka i spis treści |
| 04–19 | Organizacja sali według nowej podstawy programowej — pięć stref |
| 20–29 | Trzy poziomy wsparcia, projektowanie uniwersalne, matryca strefa × poziom |
| 30–40 | Dostosowania według deficytów + gotowe zapisy do WOPFU / IPET |
| 41–48 | Monitoring sali: dwa arkusze, karta obserwacji, plan naprawczy, plan wdrożenia |
| 49 | Podsumowanie i kontakt |

## Ponowne wygenerowanie

```bash
cd zrodla && python3 build.py
```

Skrypt zapisuje plik HTML obok siebie; PDF powstaje przez wydruk strony do A4
z włączonym tłem i zerowymi marginesami.
