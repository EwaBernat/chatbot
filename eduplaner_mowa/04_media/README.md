# Media modułu rozwoju mowy

Wszystkie ścieżki w plikach JSON liczone są od tego katalogu — tak jak w module ABC/FBA,
w banku sensorycznym i w banku teorii umysłu.

```
eduplaner_mowa/assets/audio_mowa/     ai_1.mp3 … cv_5.mp3   — 75 nagrań poleceń dla dziecka
eduplaner_mowa/assets/pomoce_mowa/    k_i_1.jpg … k_v_5.jpg — 25 zdjęć pomocy dydaktycznych
eduplaner_mowa/assets/arkusze/        pola historyjek, listw i zestawów — bez tekstu
../../media_wspolne/eduplaner_przedszkole/assets/symbole/   — biblioteka WSPÓLNA z bankiem KPOF
```

Nazwa pliku nagrania: litera wersji wiekowej (a/b/c) + numer obszaru rzymski małymi
literami + numer pozycji. `biv_4.mp3` to polecenie do wskaźnika IV.4 w wersji B (5 lat).

**Nagrania to sklonowany głos autorki — dana biometryczna.** Nie publikuj tych plików
i nie używaj ich poza uzgodnionym zastosowaniem w aplikacji EduPlaner 2026. Pliki audio
i zdjęcia nie wchodzą do repozytorium (`.gitignore`); repozytorium trzyma teksty, manifest
i kod, który je odtwarza.

Symbole **nie są kopiowane** do tego modułu — biblioteka zostaje jedna, w `media_wspolne/`
obok modułów; buildy szukają pliku najpierw tutaj, potem tam. Karta z `plik_symbolu: null`
to pole celowo puste: miejsce na własny symbol dziecka.

Dziesięć symboli powstało na potrzeby tego modułu i trafiło do biblioteki wspólnej:
`mowa_pokaz`, `mowa_powtorz`, `mowa_kolej`, `mowa_opowiadam`, `pytanie_kto`, `pytanie_co`,
`pytanie_gdzie`, `rytm_klaskanie`, `sylaba_dziel`, `aac_tablica`.

Rysunki w `assets/arkusze/` są **bez tekstu**. Polskie podpisy dokładają dokumenty z
`HISTORYJKI` w `dane_zrodlowe.py` — poprawka słowa nie wymaga wtedy przerysowywania
obrazka, a generator obrazu i tak nie postawiłby polskiego napisu poprawnie.

Pięć arkuszy obrazkowych (25 pól):

| wskaźnik | rodzaj | co pokazuje |
|---|---|---|
| I.3 | listwa | trzy kroki polecenia dwuetapowego, do powieszenia przy stoliku |
| III.3 | zestaw | sześć słów od dwóch do czterech sylab, do klaskania |
| IV.2 | zestaw | sześć czynności — obrazek wymusza czasownik, nie nazwę rzeczy |
| V.2 | rozgałęzienie | dwie sytuacje, każda z zakończeniem „sygnał” i „płacz” |
| V.3 | historyjka | cztery obrazki jednego dnia, do ułożenia i opowiedzenia |

Nagrania odtwarza:

```bash
export ELEVENLABS_API_KEY="..."
export ELEVENLABS_VOICE_ID="<id klonu głosu autorki>"
python3 03_kod_zrodlowy/nagrania_glos.py --generuj
```
