---
name: dane-i-glos
description: Zamienia dane (CSV, XLSX, JSON, tabela w czacie) w gotowe nagranie lektorskie po polsku — najpierw rzetelna analiza liczb, potem scenariusz narracji, na końcu plik MP3 z ElevenLabs plus napisy SRT. Użyj ZAWSZE, gdy użytkowniczka prosi o: „udźwiękowij te dane", „przeczytaj mi ten raport", „zrób lektora do tych wyników", „narracja z tabeli", „podcast z danych", „audio podsumowanie", „wersja do słuchania", „głos do prezentacji/filmu", „scenariusz lektorski z Excela", „przegadaj mi ten arkusz", a także przy hasłach: ElevenLabs, TTS, text-to-speech, lektor, narracja, voice-over, mp3 z danych, napisy SRT do narracji. Wyzwalaj też, gdy użytkowniczka wgrywa plik z danymi i mówi „z głosem", „na głos", „do posłuchania" albo prosi o ścieżkę dźwiękową do materiału EduPlaner / raportu / statystyk. NIE używaj do samej analizy danych bez audio ani do samego czytania tekstu, który nie pochodzi z danych.
---

# Dane i głos

Skill prowadzi jedną drogę: **dane → liczby → scenariusz → głos**. Każdy etap opiera się na
poprzednim, więc narracja nigdy nie zawiera liczby, której nie ma w pliku źródłowym.

## Kiedy co uruchomić

| Prośba | Etapy |
|---|---|
| „Zrób audio z tych danych" | 1 → 2 → 3 → 4 → 5 |
| „Napisz scenariusz lektorski, głos zrobię sama" | 1 → 2 → 3 |
| „Przeczytaj ten gotowy tekst" | 4 → 5 (pomiń analizę) |
| „Dodaj napisy do nagrania" | 4 z `--srt` |

## Etap 1 — Wczytaj dane i policz, zanim cokolwiek napiszesz

Nigdy nie opisuj danych z pamięci ani „na oko" z podglądu pliku. Uruchom profiler:

```bash
python3 .claude/skills/dane-i-glos/scripts/dane_do_narracji.py <plik> --profil
```

Skrypt przyjmuje `.csv`, `.tsv`, `.xlsx`, `.json`, `.jsonl` i zwraca w Markdown:
liczbę wierszy i kolumn, typ każdej kolumny, braki danych, sumy/średnie/min/maks dla liczb,
najczęstsze wartości dla kategorii oraz zakres dat. To jest **jedyne źródło liczb** dla narracji.

Przydatne przełączniki:

- `--kolumny nazwa,druga` — zawęź profil do wybranych kolumn
- `--grupuj klasa --agreguj wynik` — przekrój (średnia i liczebność w grupach)
- `--arkusz "Nazwa"` — konkretny arkusz z XLSX (domyślnie pierwszy)
- `--json` — profil jako JSON, gdy potrzebujesz go dalej przetworzyć

Jeśli plik jest pusty, ma same nagłówki albo kolumna liczbowa okazuje się tekstem —
powiedz to wprost użytkowniczce i zapytaj, zanim zbudujesz narrację na wątpliwych danych.

## Etap 2 — Wybierz historię, nie wszystkie liczby

Nagranie to nie arkusz odczytany na głos. Z profilu wybierz **3–5 faktów**, które niosą sens:
największa zmiana, wartość odstająca, wynik zbiorczy, wyraźny trend, coś zaskakującego.
Resztę pomiń — zostaje w pliku, do którego słuchacz zawsze może zajrzeć.

Zapytaj o odbiorcę, jeśli nie wynika z rozmowy: **dyrekcja, rodzice, zespół, sama autorka**?
Ten wybór zmienia ton, długość i to, które liczby są ważne.

## Etap 3 — Napisz scenariusz lektorski

Pełne zasady stylu: `references/narracja.md` — przeczytaj przed pisaniem pierwszego zdania.
Skrót najważniejszych reguł:

- **Tempo**: ok. 150 słów na minutę po polsku. 60 s ≈ 150 słów, 90 s ≈ 225 słów.
- **Liczby zapisuj słowami tak, jak się je czyta**: `87,5%` → „osiemdziesiąt siedem i pół procent",
  `2026` → „dwa tysiące dwudziesty szósty". Silnik TTS czyta cyfry po polsku niepewnie.
- **Jedno zdanie = jedna myśl.** Maksymalnie 20 słów. Bez wtrąceń w nawiasach.
- **Bez elementów wizualnych**: żadnego „jak widać w tabeli", „poniższy wykres".
- **Struktura**: haczyk (1 zdanie) → kontekst (2–3) → kluczowe liczby (3–5) → wniosek (1–2).

Zapisz scenariusz do pliku `.txt` (np. `narracja.txt`) i **pokaż go użytkowniczce do akceptacji
przed generowaniem audio** — poprawka w tekście kosztuje sekundę, przegenerowanie nagrania kosztuje
znaki z limitu ElevenLabs.

Pauzy zaznaczaj nową linią lub `<break time="0.7s" />` (obsługiwane przez modele `eleven_v3`
i `eleven_multilingual_v2`).

## Etap 4 — Wygeneruj głos

**Najpierw sprawdź, czy w sesji są narzędzia ElevenLabs (`mcp__ElevenLabs__*`)** — jeśli tak,
użyj ich. Jeśli nie ma, użyj skryptu REST, który wymaga tylko klucza w zmiennej środowiskowej:

```bash
export ELEVENLABS_API_KEY="..."          # klucz z elevenlabs.io → Profile → API Keys
python3 .claude/skills/dane-i-glos/scripts/elevenlabs_tts.py narracja.txt -o raport.mp3
```

Najczęstsze przełączniki:

- `--glosy` — wypisz dostępne głosy z konta i ich `voice_id` (uruchom to jako pierwsze)
- `--voice-id <id>` — konkretny głos; domyślnie `ELEVENLABS_VOICE_ID` lub Rachel
- `--model eleven_multilingual_v2` — domyślny, najlepszy dla polszczyzny
- `--srt napisy.srt` — dodatkowo napisy z rzeczywistymi znacznikami czasu z ElevenLabs
- `--stability 0.5 --similarity 0.75 --speed 1.0` — barwa i tempo
- `--suchy-bieg` — policz znaki i koszt bez wywołania API

Skrypt sam dzieli długi tekst na fragmenty poniżej limitu znaków, zachowuje ciągłość brzmienia
(`previous_text`/`next_text`) i skleja wynik w jeden plik MP3.

Klucza API **nigdy** nie wpisuj do pliku w repozytorium ani do treści rozmowy — tylko zmienna
środowiskowa. Szczegóły API, modele, limity i kody błędów: `references/elevenlabs.md`.

## Etap 5 — Oddaj komplet

Dostarcz użytkowniczce trzy rzeczy i wymień je jawnie:

1. **plik audio** (`.mp3`) — wyślij go, nie tylko wspomnij ścieżkę,
2. **tekst narracji** (`.txt`) — żeby mogła poprawić i przegenerować,
3. **napisy** (`.srt`) — jeśli nagranie pójdzie pod wideo.

Podaj czas trwania nagrania i liczbę zużytych znaków. Jeśli któryś etap się nie udał —
powiedz który i dlaczego, zamiast oddawać niekompletny zestaw po cichu.

## Materiały

- `references/narracja.md` — zasady pisania pod polskiego lektora, wzorce zdań, przykłady
- `references/elevenlabs.md` — API, modele, limity, głosy, rozwiązywanie błędów
- `assets/przyklad_dane.csv` — dane testowe do sprawdzenia całej ścieżki
