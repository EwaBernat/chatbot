# Media modułu profilu sensorycznego

Wszystkie ścieżki w plikach JSON liczone są od tego katalogu.

```
eduplaner_sens/assets/audio_sens/    as_<nr>_<poziom>.mp3   — 63 nagrania poleceń dla dziecka
eduplaner_sens/assets/pomoce_sens/   p_<nr>.jpg             — 21 zdjęć pomocy dydaktycznych
eduplaner_sens/assets/arkusze/       a_<nr>.pdf             — 21 arkuszy A4 do wycięcia
eduplaner_przedszkole/assets/symbole/                       — biblioteka WSPÓLNA z bankiem KPOF
```

**Nagrania to sklonowany głos autorki — dana biometryczna.** Nie publikuj tych plików
i nie używaj ich poza uzgodnionym zastosowaniem w aplikacji EduPlaner 2026. Pliki audio,
zdjęcia i arkusze PDF nie wchodzą do repozytorium (`.gitignore`); repozytorium trzyma
teksty, manifest i kod, który je odtwarza.

Symbole **nie są kopiowane** do tego modułu. Dziecko korzystające z komunikacji
obrazkowej musi widzieć ten sam obrazek na karcie z zajęć, na tablicy AAC i w planie dnia —
biblioteka symboli zostaje jedna, w katalogu banku KPOF.

Nagrania odtwarza:

```bash
export ELEVENLABS_API_KEY="..."
export ELEVENLABS_VOICE_ID="<id klonu głosu autorki>"
python3 03_kod_zrodlowy/nagrania_glos.py --generuj
```
