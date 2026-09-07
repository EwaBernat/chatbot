# Filmy szkoleniowe — EduPlaner 2026 · PCTP

Projekt Remotion, który zamienia **skrypty dla nauczycieli** w filmy: plansze, tabele,
zakreślenia, najazdy kamery i zrzuty prawdziwych druków z aplikacji EduPlaner —
z narracją **głosem autorki** (ElevenLabs, skill `glos-ewy`).

Dwa szkolenia dzielą tę samą oprawę i ten sam zestaw scen:

* **szkoła podstawowa** — moduły `S1`…`S7`, scenariusz `src/scenariusz.json`,
  budowany przez `zbuduj_scenariusz.py` ze skryptu `../build_skrypt_szkola.py`;
* **przedszkole** — moduły `P1`…`P6`, scenariusz `src/scenariusz-przedszkole.json`,
  budowany przez `zbuduj_scenariusz_przedszkole.py` wprost z pliku
  `../Skrypt_dla_nauczycieli_PRZEDSZKOLE_wydanie2_po_audycie.docx`.

Stopka filmu bierze nazwę placówki z numeru modułu, więc slajd `P…` sam podpisuje
się „przedszkole”, a `S…` — „szkoła podstawowa”.

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
| S2 · Dlaczego zmieniamy | 20 | 13:18 | **nagrany** | **gotowy** |
| S3 · Obieg dokumentów | 15 | 7:20 | **nagrany** | **gotowy** |
| S4 · Metryczka i teczka ucznia | 14 | 7:07 | **nagrany** | **gotowy** |
| S5 · KSzOF | 19 | 12:19 | **nagrany** | **gotowy** |
| S6 · Obserwacja pogłębiona | 19 | 11:21 | **nagrany** | **gotowy** |
| S7 · WOPF-SP, IPET, PWES | 25 | 17:24 | **nagrany** | **gotowy** |

Razem **139 ujęć, 1 godzina 25 minut**. Szkolenie jest kompletne: wszystkie moduły
mają narrację głosem Ewy wyrównaną do −20,7 LUFS i wyrenderowany film 1080p.

### Przedszkole

| Moduł | Ujęć | Długość | Głos | Render |
|---|---:|---:|---|---|
| P1 · Podstawa prawna | 22 | 10:15 | **nagrany** | **gotowy** |
| P2 · Obieg dokumentów | 12 | 5:37 | **nagrany** | **gotowy** |
| P3 · Metryczka dziecka | 13 | 5:50 | **nagrany** | **gotowy** |
| P4 · KPOF | 22 | 10:38 | **nagrany** | **gotowy** |
| P5 · Obserwacja pogłębiona | 24 | 9:41 | **nagrany** | **gotowy** |
| P6 · WOPF, IPET, ewaluacja | 30 | 13:40 | **nagrany** | **gotowy** |

Razem **123 ujęcia, 55 minut 40 sekund**. Szkolenie przedszkolne jest kompletne:
wszystkie ujęcia mają narrację wyrównaną do −20,7 LUFS i wyrenderowany film 1080p.

Zrzuty druków przedszkolnych leżą w `public/druki-przedszkole/` i pochodzą z trybu
`przedszkole` aplikacji (`npx vite --mode przedszkole`). W tym trybie aplikacja ma
komplet druków: KPOF w trzech wersjach wiekowych, profil ICF, ABC, FBA, profil
sensoryczny, mowę, teorię umysłu, WOPF, IPET, ewaluację i opinię do poradni.

Gotowe pliki leżą w `gotowe/` i **nie są w repozytorium** — kontener jest ulotny,
więc po jego wygaśnięciu trzeba je odtworzyć poleceniem `npx remotion render S<n>`
(scenariusz i nagrania są w repo, więc render odtworzy dokładnie te same filmy).
Obok pełnych plików powstają wersje `_lekki.mp4` (CRF 33, dźwięk 56 kb/s mono),
bo przez czat da się przesłać najwyżej 30 MB.

Do dokrętki zostaje tylko awatar HeyGen — patrz `HEYGEN.md`. Miejsce na obraz
awatara jest już w kodzie (`OkienkoAwatara`), wystarczy wrzucić klipy do
`public/awatar/` i dopisać `awatar` do ujęcia w `scenariusz.json`.
