# Media modułu profilu sensorycznego

Wszystkie ścieżki w plikach JSON liczone są od tego katalogu — tak jak w module ABC/FBA.

```
eduplaner_sens/assets/audio_sens/     ai_1.mp3 … cvii_3.mp3   — 63 nagrania poleceń dla dziecka
eduplaner_sens/assets/pomoce_sens/    k_i_1.jpg … k_vii_3.jpg — 21 zdjęć pomocy dydaktycznych
eduplaner_sens/assets/arkusze/        pola drabin, skal i historyjek — bez tekstu
../../media_wspolne/eduplaner_przedszkole/assets/symbole/     — biblioteka WSPÓLNA z bankiem KPOF
```

Nazwa pliku nagrania: litera wersji wiekowej (a/b/c) + numer zmysłu rzymski małymi literami
+ numer sektora. `bvi_2.mp3` to polecenie do wskaźnika VI.2 w wersji B (5 lat).

**Nagrania to sklonowany głos autorki — dana biometryczna.** Nie publikuj tych plików
i nie używaj ich poza uzgodnionym zastosowaniem w aplikacji EduPlaner 2026. Pliki audio
i zdjęcia nie wchodzą do repozytorium (`.gitignore`); repozytorium trzyma teksty, manifest
i kod, który je odtwarza.

Symbole **nie są kopiowane** do tego modułu. Dziecko korzystające z komunikacji obrazkowej
musi widzieć ten sam obrazek na karcie z zajęć, na tablicy AAC i w planie dnia —
biblioteka symboli zostaje jedna, w `media_wspolne/` obok modułów. Buildy szukają pliku
najpierw tutaj, potem tam. Karta z `plik_symbolu: null` to pole celowo puste: miejsce na
własny symbol dziecka.

Rysunki w `assets/arkusze/` są **bez tekstu**. Polskie podpisy dokładają dokumenty z
`HISTORYJKI` w `dane_zrodlowe.py` — poprawka słowa nie wymaga wtedy przerysowywania
obrazka, a generator obrazu i tak nie postawiłby polskiego napisu poprawnie.

Nagrania odtwarza:

```bash
export ELEVENLABS_API_KEY="..."
export ELEVENLABS_VOICE_ID="<id klonu głosu autorki>"
python3 03_kod_zrodlowy/nagrania_glos.py --generuj
```
