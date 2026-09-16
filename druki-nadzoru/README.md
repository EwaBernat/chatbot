# Druki z nadzoru pedagogicznego · PCTP Koszalin

Komplet 14 druków (.docx, A4) obsługujących roczny cykl nadzoru pedagogicznego
dyrektora szkoły specjalnej: planowanie → obserwacje → kontrola → ewaluacja →
wspomaganie → sprawozdanie. Marka EduPlaner2026-MJ-PCTP: fiolet `#2D1B69`,
pomarańcz `#E8450A`, Arial, nagłówek i stopka z paginacją na każdej stronie.

Gotowe pliki leżą w `out/`. Każdy druk ma kod (NP-01 … NP-14) widoczny w nagłówku
strony, dzięki czemu druki odwołują się do siebie nawzajem.

## Spis druków

| Kod | Druk | Kiedy używasz |
|---|---|---|
| NP-01 | Plan nadzoru pedagogicznego | wrzesień — przedstawienie radzie pedagogicznej |
| NP-02 | Sprawozdanie z nadzoru pedagogicznego | podsumowanie półroczne i roczne |
| NP-03 | Arkusz obserwacji zajęć dydaktycznych | obserwacja zajęć edukacyjnych |
| NP-04 | Arkusz obserwacji zajęć rewalidacyjnych i specjalistycznych | rewalidacja, logopedia, TUS, SI, WWR |
| NP-05 | Arkusz obserwacji diagnozującej | sprawdzenie efektu: co uczniowie potrafią |
| NP-06 | Karta pohospitacyjna | rozmowa z nauczycielem po obserwacji |
| NP-07 | Arkusz kontroli dokumentacji przebiegu nauczania | dzienniki, teczki uczniów, arkusze ocen |
| NP-08 | Arkusz kontroli realizacji IPET i WOPF | kontrola dokumentacji ucznia z orzeczeniem |
| NP-09 | Ewaluacja wewnętrzna — projekt i harmonogram | zaprojektowanie badania |
| NP-10 | Ewaluacja wewnętrzna — kwestionariusz ankiety | narzędzie badawcze (+ wersja uproszczona dla uczniów) |
| NP-11 | Raport z ewaluacji wewnętrznej | wyniki, wnioski, rekomendacje |
| NP-12 | Karta wspomagania i doskonalenia nauczyciela | diagnoza potrzeb i plan rozwoju |
| NP-13 | Protokół rady pedagogicznej — wyniki nadzoru | posiedzenie rady + lista obecności |
| NP-14 | Karta oceny pracy nauczyciela | arkusz roboczy dyrektora |

## Jak z tego korzystać

Druki są przygotowane do wypełnienia: pola opisowe mają kropkowane linie,
listy — kratki `□` do zaznaczenia, tabele — puste wiersze. Wypełniasz je
w Wordzie albo po wydrukowaniu, odręcznie. Wiersze oznaczone w tekście jako
propozycje (np. tematyka kontroli w NP-01) skreślasz lub zastępujesz własnymi.

## Regeneracja i zmiany

```bash
cd druki-nadzoru
npm install                 # jednorazowo, biblioteka docx
node generuj.js             # wszystkie druki do out/
node generuj.js out NP-03   # tylko wybrane
python3 sprawdz_uklad.py    # kontrola szerokości tabel
```

Treść każdego druku jest w osobnym pliku w `druki/`. Styl (kolory, nagłówki,
kratki, podpisy) jest wspólny w `styl.js`, a powtarzalne bloki — podstawa prawna,
metryczka, tabele kontrolne, skala ocen — w `wspolne.js`. Żeby dodać pozycję do
arkusza, dopisujesz jedną linię tekstu w odpowiedniej tablicy.

## Stan prawny

Druki przywołują: Prawo oświatowe (art. 55–60, art. 68 ust. 1 pkt 2, art. 69
ust. 7), rozporządzenie w sprawie nadzoru pedagogicznego, rozporządzenia
o kształceniu specjalnym i pomocy psychologiczno-pedagogicznej z 9 sierpnia
2017 r., rozporządzenie o dokumentacji przebiegu nauczania, Kartę Nauczyciela
i rozporządzenie o ocenie pracy nauczycieli oraz RODO.

Akty podano bez numerów Dz.U., z adnotacją „ze zm.", bo teksty jednolite bywają
aktualizowane. **Przed wdrożeniem druków zweryfikuj aktualne brzmienie
przywołanych przepisów** — dotyczy to zwłaszcza NP-14 (liczba i treść kryteriów
oceny pracy zależą od stopnia awansu zawodowego) oraz terminów w NP-01 i NP-02.

## Ochrona danych

NP-03 … NP-08, NP-12 i NP-14 zawierają dane osobowe, a NP-08 także dane o stanie
zdrowia ucznia. Każdy z tych druków ma klauzulę przypominającą o zasadach
przechowywania. Przechowuj je w dokumentacji nadzoru pedagogicznego prowadzonej
przez dyrektora, udostępniaj wyłącznie osobom upoważnionym.
