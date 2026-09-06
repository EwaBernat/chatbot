# Film szkoleniowy dla szkoły podstawowej — EduPlaner 2026 · PCTP

Projekt Remotion, który zamienia **skrypt dla nauczycieli** w film: plansze, tabele,
zakreślenia, najazdy kamery i zrzuty prawdziwych druków z aplikacji EduPlaner —
z narracją **głosem autorki** (ElevenLabs, skill `glos-ewy`).

## Skąd bierze się treść

Narracja **nie jest pisana tutaj**. Jest wyciągana wprost z
[`../build_skrypt_szkola.py`](../build_skrypt_szkola.py), czyli z tego samego źródła,
z którego powstaje drukowany skrypt. Film mówi więc dokładnie to, co stoi w druku —
poprawka w skrypcie wchodzi do filmu po jednym uruchomieniu generatora.

W tym projekcie dokładamy tylko **warstwę obrazu**: jaki typ planszy, co zakreślamy
na pomarańczowo, którą tabelę pokazujemy, w który druk najeżdżamy kamerą.

```
build_skrypt_szkola.py ──► zbuduj_scenariusz.py ──► src/scenariusz.json ──► Remotion ──► MP4
       (narracja)              (plan scen)              (czasy z MP3)
```

## Jak to uruchomić

```bash
npm install
npm run studio                     # podgląd na żywo, przewijanie po ujęciach
npx remotion render S1 gotowe/SZKOLA_M1.mp4 \
    --browser-executable=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell
```

Render 1920×1080 · 30 kl./s · H.264. Tempo w kontenerze: około **2× dłużej niż film**
(16 minut filmu ≈ 23 minuty renderu).

## Typy plansz

| Typ | Do czego |
|---|---|
| `czolowka` | otwarcie całego szkolenia — znak PCTP, tytuł, spis siedmiu części |
| `tytulModulu` | karta tytułowa modułu z wielkim numerem |
| `punkty` | 2–4 tezy z numerkami; `**tekst**` dostaje pomarańczowy zakreślacz |
| `cytat` | przepis w ramce z paragrafem — do cytowania rozporządzeń |
| `tabela` | tabela budowana wiersz po wierszu, nagłówek na fiolecie |
| `druk` | zrzut z aplikacji albo strona skryptu z powolnym najazdem (Ken Burns) |
| `sciezki` | dwie kolumny obok siebie — np. kształcenie specjalne / pomoc p-p |
| `obieg` | oś z przystankami — obieg dokumentów |
| `domkniecie` | trzy zdania na koniec modułu |

Zakreślanie: w każdym tekście fragment ujęty w `**gwiazdki**` dostaje pomarańczowe tło,
które wjeżdża od lewej jak pociągnięcie markerem. Po jednym–dwóch na planszę.

## Skąd biorą się druki na ekranie

`public/druki/` — zrzuty z **działającej aplikacji EduPlaner 2026** w trybie szkoły
podstawowej (`npm run dev:szkolap` w repozytorium EduPlaner2026, przeglądarka 1600×1000,
dwukrotna gęstość pikseli). Widać na nich prawdziwe menu, prawdziwe druki i wybranego
ucznia z kartoteki demonstracyjnej.

`public/kartki/` — strony skryptu (PDF, 130 dpi) dla druków, których aplikacja jeszcze
nie ma w wersji szkolnej.

Odświeżenie zrzutów: uruchom aplikację w trybie `szkolap`, zaloguj się, wybierz ucznia
w wyszukiwarce u góry i zrób zrzuty tras z `public/druki/` ponownie.

## Głos

Narrację nagrywa skill [`glos-ewy`](../../.claude/skills/glos-ewy/SKILL.md) —
sklonowany głos autorki, model `eleven_v3`, jedna wskazówka aktorska na ujęcie,
głośność wyrównana do **−20,7 LUFS** (poziom narracji w modułach EduPlaner).

Pliki: `public/glos/<id ujęcia>.mp3`. Gdy plik istnieje, `zbuduj_scenariusz.py` bierze
**zmierzoną** długość nagrania jako długość sceny; gdy go nie ma — szacuje z tempa
107 słów na minutę, żeby dało się obejrzeć układ przed nagraniem.

## Dodanie kolejnego modułu

1. Dopisz `PLAN_<numer>` w `zbuduj_scenariusz.py` — lista `(id, [indeksy akapitów], scena)`.
   Indeksy wskazują akapity narracji z `czesc_<numer>` w skrypcie.
2. Dopisz plan do słownika `PLANY`.
3. `python3 zbuduj_scenariusz.py` → obejrzyj układ w `npm run studio` (bez głosu).
4. Nagraj głos skillem `glos-ewy`, wrzuć MP3 do `public/glos/`, wyrównaj głośność.
5. `python3 zbuduj_scenariusz.py` jeszcze raz — czasy scen wskoczą na zmierzone.
6. Render.

## Stan produkcji

| Moduł | Ujęć | Długość | Głos | Render |
|---|---:|---:|---|---|
| S1 · Podstawa prawna | 27 | 16:02 | **nagrany** | **gotowy** |
| S2 · Dlaczego zmieniamy | 20 | 14:24 | do nagrania | — |
| S3 · Obieg dokumentów | 15 | 8:35 | do nagrania | — |
| S4 · Metryczka i teczka ucznia | 14 | 7:45 | do nagrania | — |
| S5 · KSzOF | 20 | 13:12 | do nagrania | — |
| S6 · Obserwacja pogłębiona | 19 | 11:32 | do nagrania | — |
| S7 · WOPF-SP, IPET, PWES | 25 | 17:25 | do nagrania | — |

Razem **140 ujęć, około 89 minut**. Plansze wszystkich modułów są gotowe i można je
obejrzeć w `npm run studio` już teraz — czasy scen są wtedy szacowane z tempa
107 słów na minutę, a po nagraniu wskakują na zmierzone.

Koszt dogrania sześciu pozostałych modułów: **56 443 znaki ≈ 9,31 USD** w ElevenLabs.
Czas renderu: około **2,5 godziny** dla całej reszty.
