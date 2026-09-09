# Audiobook — „Rajmund i Arystoteles"

## Stan: czeka na Twój głos

W tym katalogu nie ma jeszcze plików MP3. To celowe.

Zasada skilla `dane-i-glos` brzmi: **tylko Twój głos**. Skill nie podstawia
cudzego lektora. Dlatego zamiast nagrania jest tu gotowy scenariusz:

* `scenariusz/` — 37 plików, część pierwsza,
* `scenariusz-czesc-2/` — 31 plików, część druga.

To dokładnie ten tekst, który ma zostać przeczytany, po jednym pliku na rozdział.

## Czego brakuje

Jednej rzeczy: **1–2 minut Twojego nagrania** (MP3, WAV, M4A albo film MP4 —
skrypt sam wyciągnie z niego dźwięk). Może to być zwykłe czytanie na głos
dowolnego tekstu, byle spokojnie i bez hałasu w tle.

## Co zrobić — dwa polecenia

Z katalogu głównego repozytorium:

```bash
# 1. Raz w życiu: zapamiętanie Twojego głosu (klon w ElevenLabs)
python3 .claude/skills/dane-i-glos/scripts/skonfiguruj_glos.py nagranie.mp3 --nazwa "Ewa - narracja PL"

# 2. Nagranie audiobooka Twoim głosem — MP3 + napisy SRT
bash opowiadania/skrypty/nagraj_audiobook.sh        # obie części
bash opowiadania/skrypty/nagraj_audiobook.sh 2      # tylko część druga
```

Sprawdzenie, czy głos jest już zapamiętany:

```bash
python3 .claude/skills/dane-i-glos/scripts/skonfiguruj_glos.py --pokaz
```

## Co powstanie

* `czesc-1/rozdzial-01-rajmund.mp3` … — 37 plików, po jednym na rozdział (razem około 50 minut),
* `czesc-2/rozdzial-01-rok-pozniej.mp3` … — 31 plików części drugiej (razem około 45 minut),
* `rozdzial-NN-....srt` — napisy z czasami, gdyby Maksymilian wolał słuchać i czytać naraz.

Podział na rozdziały jest celowy: krótki plik łatwiej włączyć jeszcze raz,
można wrócić do jednego rozdziału i nie trzeba szukać miejsca w długim nagraniu.

## Uwaga o głosie

Jeśli kiedyś świadomie zdecydujesz się na innego lektora, `elevenlabs_tts.py`
ma przełącznik `--obcy-glos`, ale wymaga on podania konkretnego `--voice-id`
i Twojej wyraźnej decyzji za każdym razem. Domyślnie nic się nie nagra bez Twojego głosu.
