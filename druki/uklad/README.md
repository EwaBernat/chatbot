# EduPlaner 2026 — komplet przedszkola

**PCTP Koszalin · 58 druków w dwóch kącikach · 31 sierpnia 2026 r.**

Wszystko ułożone w jednej kolejności: **wykaz obowiązków → podział według terminów →
podział według rodzajów czynności → druki**. Ta sama kolejność obowiązuje w katalogach,
w menu aplikacji i na stronie kafelkowej.

## Od czego zacząć

| Plik | Dla kogo |
|---|---|
| **WDROZENIE_KACIKI_W_APLIKACJI.html** | dla Arka — jak wpiąć oba kąciki, podział na kafelki, paleta, trasy, reguły |
| **rejestr-kacikow.json** | dla Arka — cała struktura maszynowo, nic nie trzeba przepisywać |
| `kacik-*/03_PODZIAL_WG_RODZAJOW_CZYNNOSCI/PRZEWODNIK…` | dla Ewy — kolejność i kafelki na dwóch kartkach A4 |

## Układ każdego kącika

```
00_START/                              MANIFEST, README, wykaz poprawek, rejestr
01_WYKAZ_OBOWIAZKOW/                   krok 1 — lista czynności
02_PODZIAL_WG_TERMINOW/                krok 2 — kalendarz roku
03_PODZIAL_WG_RODZAJOW_CZYNNOSCI/      krok 3 — przewodnik po kafelkach
04_DRUKI/                              krok 4 — druki w kolejności kafelków
   01_…  02_…  …                       jeden katalog na kafel
   _CO_JEST_W_TYM_KAFLU.txt            co siedzi w kaflu i gdzie szukać reszty
05_GENERATOR_WORD/                     parsuj.py + gen.js — odtwarzanie .docx z HTML
```

## Numeracja

Numer druku jest **ciągły przez cały kącik** i nie zmienia się nigdy — ten sam numer stoi
w nazwie pliku, w rejestrze i na kaflu. Kącik dyrektora: **01–31**.
Kącik nauczyciela: **01–25**. Wykaz obowiązków i kalendarz stoją przed numeracją,
bo są mapą, nie drukiem do wypełnienia.

## Jeden plik, kilka druków

Część druków dzieli plik HTML — pięć druków nadzoru siedzi w jednym pliku, cztery druki rady w drugim.
Na dysku plik leży w kafelku swojego **pierwszego** druku, a `_CO_JEST_W_TYM_KAFLU.txt` mówi,
gdzie szukać pozostałych. W aplikacji trasa prowadzi wprost do druku — plik plus zakres stron —
więc użytkownik podziału na pliki nie widzi.

## Każdy druk w trzech formatach

| Format | Do czego |
|---|---|
| `.html` | wypełnianie w przeglądarce, autozapis; niebieskie znaczniki poprawek widoczne tylko na ekranie |
| `.pdf` | druk — bez warstwy interaktywnej i bez znaczników |
| `.docx` | edycja w Wordzie — te same treści i tabele |

## Kafelki

**Kącik dyrektora** (31 druków w 9 kafelkach)


| Nr | Kafel | Druki | Sygnatury |
|---:|---|---:|---|
| 01 | 🗺 Planowanie pracy przedszkola | 01–02 | DW-1 · PW-1 |
| 02 | 🔍 Nadzór pedagogiczny | 03–08 | DN-1 · DN-2 · DN-3 · DN-4 · DN-5 · EW-1 |
| 03 | 👥 Rada pedagogiczna | 09–12 | RP-1 · RP-2 · RP-3 · RP-4 |
| 04 | ⚙ Organizacja pracy | 13–16 | DO-1 · DO-2 · DO-3 · ZD-1 |
| 05 | 🤝 Pomoc psychologiczno-pedagogiczna | 17–21 | DP-1 · DP-2 · DP-3 · DP-4 · D-1 |
| 06 | ✉ Poradnia i rodzice | 22–24 | DR-1 · DR-2 · DR-3 |
| 07 | 🛡 Bezpieczeństwo | 25–27 | DB-1 · DB-2 · DB-3 |
| 08 | 📋 Rekrutacja | 28 | RE-1 |
| 09 | 📌 Zmiany 2026/2027 | 29–31 | DZ-1 · DZ-2 · DZ-3 |


**Kącik nauczyciela** (25 druków w 9 kafelkach)


| Nr | Kafel | Druki | Sygnatury |
|---:|---|---:|---|
| 01 | 👁 Obserwacja i diagnoza | 01–02 | O-1 · O-5 |
| 02 | 📝 Opinie o dziecku | 03–05 | O-2 · O-3 · O-4 |
| 03 | 🤝 Pomoc psychologiczno-pedagogiczna | 06–08 | P-1 · P-2 · P-3 |
| 04 | 🧩 Dostosowania | 09 | DS-1 |
| 05 | 🧠 Zajęcia rewalidacyjne i dziennik | 10–12 | Z-1 · Z-2 · Z-3 |
| 06 | 📐 Planowanie i realizacja zajęć | 13–17 | R-1 · R-2 · R-3 · R-4 · KON |
| 07 | 👪 Współpraca z rodzicami | 18–20 | W-1 · W-2 · W-3 |
| 08 | 🛡 Bezpieczeństwo i sytuacje szczególne | 21–24 | B-1 · B-2 · B-3 · B-4 |
| 09 | 💡 Materiały instruktażowe | 25 | I-1 |


## Paleta dla aplikacji

| Pozycja | Akcent | Pastel |
|---|---|---|
| Kącik dyrektora | `#3D2566` | `#EAE6F3` |
| Kącik nauczyciela | `#1F6F8B` | `#E4EFF4` |

Kafelki wewnątrz kącików **własnej palety nie mają** — dziedziczą akcent rodzica.
Dwie nowe pary wymagają wpisu w sekcji wyjątków u strażnika powłoki, z powodem i datą.

## Stan prawny

Oba kąciki przeszły przegląd prawny i merytoryczny 31 sierpnia 2026 r. — **225 poprawek**.
Zero nieaktualnych publikatorów, liczby kontrolne zgodne, wszystkie strony mieszczą się w A4.
Wykazy: `kacik-*/00_START/POPRAWKI_2026-08-31.md`.
Następny przegląd obowiązkowy rejestru przepisów: **1 września 2026 r.**
