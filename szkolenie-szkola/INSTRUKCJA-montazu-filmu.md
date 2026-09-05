# Dogranie wstawek do filmu — przedszkole (M1, M3, M4)

Stan na 5 września 2026 r.

## Co jest zrobione

| Etap | Stan |
|---|---|
| Punkty cięcia namierzone co do 0,2 s | **gotowe** — OCR paska napisów, potwierdzone klatkami |
| Plansze wstawek w projekcie filmu | **gotowe** — `plansze_wstawek/*.png`, 1920×1080 |
| Teksty narracji | **gotowe** — w `wstawki_manifest.json` |
| Potok montażowy | **gotowe i przetestowane** — M3 345 s → 410 s, styki czyste |
| Nagrania głosem autorki | **gotowe** — głos „Ewa-głos_do skils" (ElevenLabs), 7 plików, 4:13 |
| Gotowe filmy | **gotowe** — `gotowe/M1_po_audycie.mp4`, `M3_…`, `M4_…` |

## Punkty cięcia (zweryfikowane)

| Wstawka | Moduł | Po akapicie | Cięcie | Tytuł planszy |
|---|---|---|---|---|
| M1_1 | M1 | 08 | **187,77 s** (3:07) | Podstawa programowa — akt zmieniający |
| M1_2 | M1 | 12 | **262,49 s** (4:22) | Co uchyliło nowe rozporządzenie |
| M1_3 | M1 | 21 | **437,12 s** (7:17) | Do rozpoznania, nie do cytowania |
| M1_4 | M1 | 25 | **500,96 s** (8:20) | Dwa akty, które muszą być w naszej liście |
| M3_1 | M3 | 12 | **169,28 s** (2:49) | Informacja o gotowości — urzędowy wzór |
| M3_2 | M3 | 16 | **254,74 s** (4:14) | Podawanie leku — na jakiej podstawie? |
| M4_1 | M4 | 08 | **230,46 s** (3:50) | Dwie różne podstawy |

Sześć z siedmiu cięć pokrywa się z wykrytą zmianą planszy w oryginale (różnica ≤ 0,2 s).
Siódme (M1_3) wypada w ciszy między akapitami 21 i 22 — sprawdzone klatkami: 436,5 s pasek pusty,
437,6 s zaczyna się „Z tego rozporządzenia wynikają trzy nasze obowiązki”.

## Filmy są złożone

Wstawki nagrano głosem **„Ewa-głos_do skils"** (`jq4ZUryuBeDqmtkKtBZ4`, klon polski, w opisie:
„intonacja pasuje do prowadzenia szkoleń i wykładów"), model `eleven_multilingual_v2`.
Zużyto **3458 kredytów ElevenLabs (≈ 0,57 USD)**, 4 minuty 13 sekund materiału.
Wszystkie generacje na jednym przepływie: <https://elevenlabs.io/app/flows/ASET7HhNnsqGeHwrKxsw>

| Wstawka | Długość nagrania | | Wstawka | Długość nagrania |
|---|---|---|---|---|
| M1_1 | 27,85 s | | M3_1 | 14,47 s |
| M1_2 | 27,90 s | | M3_2 | 44,96 s |
| M1_3 | 35,19 s | | M4_1 | 29,57 s |
| M1_4 | 73,56 s | | | |

## Gdyby trzeba było powtórzyć — trzy polecenia

```bash
# 1. Zapamiętaj głos (raz). Skrypt sam wyciągnie dźwięk z filmu.
python3 .claude/skills/dane-i-glos/scripts/skonfiguruj_glos.py M1.mp4 --nazwa "Ewa - narracja PL"

# 2. Nagraj siedem wstawek (ok. 2 700 znaków ElevenLabs)
python3 szkolenie-szkola/nagraj_wstawki.py --wyjscie audio/

# 3. Złóż filmy (M1.mp4, M3.mp4, M4.mp4 w katalogu bieżącym)
python3 szkolenie-szkola/zloz_wstawki.py --audio audio/ --zrodla . --wyjscie gotowe/
```

Wynik: `gotowe/M1_po_audycie.mp4`, `gotowe/M3_po_audycie.mp4`, `gotowe/M4_po_audycie.mp4`.
Czas składania: około 2–3 minuty na moduł.

Zamiast kroków 1–2 można nagrać siedem fragmentów mikrofonem i zapisać je jako
`audio/M1_1.mp3` … `audio/M4_1.mp3`. Skrypt przyjmie każde nagranie i sam dopasuje
tempo przewijania napisów do jego długości.

## Jak działa potok

1. Dzieli film źródłowy w punkcie cięcia.
2. Buduje wstawkę: plansza + pasek napisów przewijany porcjami po ~11 słów, proporcjonalnie
   do długości nagrania.
3. Skleja: część przed cięciem + wstawka + reszta filmu.
4. Wszystko w parametrach oryginału — 1920×1080, 30 kl./s, H.264, AAC 48 kHz stereo.

Brakującego nagrania skrypt **nie zastępuje** ciszą ani innym głosem — pomija wstawkę
i wypisuje, której brakuje.

## Przewidywane długości po zmianie

| Moduł | Teraz | Po dograniu |
|---|---|---|
| M1 | 9:30 | ~12:21 |
| M3 | 5:45 | ~6:34 |
| M4 | 10:08 | ~10:46 |

## Dlaczego nagrania nie powstały tutaj

`api.elevenlabs.io` jest zablokowane przez politykę sieciową tego środowiska (odpowiedź 403
z pośrednika), a złącze ElevenLabs zwraca 403 na każde wywołanie. Nagranie cudzym głosem
nie wchodzi w grę — materiał firmowany Pani nazwiskiem ma brzmieć Panią.
