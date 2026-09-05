# Media modułu teorii umysłu

Wszystkie ścieżki w plikach JSON liczone są od tego katalogu — tak jak w module ABC/FBA
i w banku sensorycznym.

```
eduplaner_tom/assets/audio_tom/       ai_1.mp3 … cv_5.mp3   — 75 nagrań poleceń dla dziecka
eduplaner_tom/assets/pomoce_tom/      k_i_1.jpg … k_v_5.jpg — 25 zdjęć pomocy dydaktycznych
eduplaner_tom/assets/arkusze/          pola historyjek, drabin i skal — bez tekstu
../../media_wspolne/eduplaner_przedszkole/assets/symbole/   — biblioteka WSPÓLNA z bankiem KPOF
```

Nazwa pliku nagrania: litera wersji wiekowej (a/b/c) + numer komponentu rzymski małymi
literami + numer pozycji. `biv_4.mp3` to polecenie do wskaźnika IV.4 w wersji B (5 lat).

**Nagrania to sklonowany głos autorki — dana biometryczna.** Nie publikuj tych plików
i nie używaj ich poza uzgodnionym zastosowaniem w aplikacji EduPlaner 2026. Pliki audio
i zdjęcia nie wchodzą do repozytorium (`.gitignore`); repozytorium trzyma teksty, manifest
i kod, który je odtwarza.

Symbole **nie są kopiowane** do tego modułu — biblioteka zostaje jedna, w `media_wspolne/`
obok modułów; buildy szukają pliku najpierw tutaj, potem tam. Karta z `plik_symbolu: null`
to pole celowo puste: miejsce na własny symbol dziecka.

Rysunki w `assets/arkusze/` są **bez tekstu**. Polskie podpisy dokładają dokumenty z
`HISTORYJKI` w `dane_zrodlowe.py` — poprawka słowa nie wymaga wtedy przerysowywania
obrazka, a generator obrazu i tak nie postawiłby polskiego napisu poprawnie.

Nagrania odtwarza:

```bash
export ELEVENLABS_API_KEY="..."
export ELEVENLABS_VOICE_ID="<id klonu głosu autorki>"
python3 03_kod_zrodlowy/nagrania_glos.py --generuj
```
