# Audiobook — „Rajmund i Arystoteles"

## Stan: czeka na Twój głos

W tym katalogu nie ma jeszcze plików MP3. To celowe.

Zasada skilla `dane-i-glos` brzmi: **tylko Twój głos**. Skill nie podstawia
cudzego lektora. Dlatego zamiast nagrania jest tu gotowy scenariusz —
37 plików tekstowych, po jednym na rozdział, w katalogu `scenariusz/`.
To dokładnie ten tekst, który ma zostać przeczytany.

## Czego brakuje

Jednej rzeczy: **1–2 minut Twojego nagrania** (MP3, WAV, M4A albo film MP4 —
skrypt sam wyciągnie z niego dźwięk). Może to być zwykłe czytanie na głos
dowolnego tekstu, byle spokojnie i bez hałasu w tle.

## Co zrobić — dwa polecenia

Z katalogu głównego repozytorium:

```bash
# 1. Raz w życiu: zapamiętanie Twojego głosu (klon w ElevenLabs)
python3 .claude/skills/dane-i-glos/scripts/skonfiguruj_glos.py nagranie.mp3 --nazwa "Ewa - narracja PL"

# 2. Nagranie całego audiobooka Twoim głosem — 37 plików MP3 + napisy SRT
bash opowiadania/skrypty/nagraj_audiobook.sh
```

Sprawdzenie, czy głos jest już zapamiętany:

```bash
python3 .claude/skills/dane-i-glos/scripts/skonfiguruj_glos.py --pokaz
```

## Co powstanie

* `rozdzial-01-rajmund.mp3` … `rozdzial-37-krotkie-powtorzenie.mp3` — po jednym pliku na rozdział,
  każdy na 1,5–2,5 minuty (razem około 50 minut),
* `rozdzial-NN-....srt` — napisy z czasami, gdyby Maksymilian wolał słuchać i czytać naraz.

Podział na rozdziały jest celowy: krótki plik łatwiej włączyć jeszcze raz,
można wrócić do jednego rozdziału i nie trzeba szukać miejsca w długim nagraniu.

## Uwaga o głosie

Jeśli kiedyś świadomie zdecydujesz się na innego lektora, `elevenlabs_tts.py`
ma przełącznik `--obcy-glos`, ale wymaga on podania konkretnego `--voice-id`
i Twojej wyraźnej decyzji za każdym razem. Domyślnie nic się nie nagra bez Twojego głosu.
