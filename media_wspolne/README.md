# Biblioteka symboli — wspólna dla modułów EduPlaner

```
eduplaner_przedszkole/assets/symbole/   k_emocja_radosc.jpg … k_zabawa_ukladanka.jpg
```

Jedna kopia dla wszystkich modułów. Ten sam obrazek ma być na karcie pracy, na tablicy
AAC dziecka i w planie dnia — gdyby każdy moduł trzymał własną kopię, pierwsza poprawka
rysunku rozjechałaby te trzy miejsca.

Buildy szukają pliku najpierw w `04_media/` swojego modułu, dopiero potem tutaj. Dzięki
temu moduł może nadpisać pojedynczy symbol, nie ruszając biblioteki.

Nazwa pliku to `k_` + klucz symbolu z `arkusz.karty[].symbol` w `dane_zrodlowe.py`.
Klucz `null` oznacza pole celowo puste — miejsce na własny symbol dziecka z jego tablicy AAC.

Pliki nie wchodzą do repozytorium (`.gitignore`): repozytorium trzyma opisy i kod, obrazki
się odtwarza. Styl jest wspólny dla całej biblioteki: płaski wektor, gruby ciemny kontur,
fiolet i pomarańcz marki, białe tło, **żadnego tekstu na obrazku** — podpisy składa dokument.
