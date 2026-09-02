# Strażnicy

Jeden folder, **jeden plik na strażnika**. Siedmiu. Każdy pilnuje jednej rzeczy i mówi wprost, czego
**nie** pilnuje — dzięki temu wiadomo, do kogo iść z pytaniem.

Strażnik ma trzy warstwy: **podstawę** (ten dokument), **sondę** (automat) i **procedurę**
(skill `straznik`). Reguła bez sondy jest życzeniem — dlatego przy każdym stoi, czym dziś jest pilnowany.

| Strażnik | Pilnuje | Sonda |
|---|---|---|
| <!-- straznik:ignoruj --> [`straznik-prawo`](./straznik-prawo.md) | przepisy istnieją, obowiązują, mają jedno brzmienie; zmiana prawa daje listę druków | **brak** — po `E18` |
| <!-- straznik:ignoruj --> [`straznik-danych`](./straznik-danych.md) | wszystko, co widać na kartce, jest zapisywane | jedna |
| <!-- straznik:ignoruj --> [`straznik-synchronizacji`](./straznik-synchronizacji.md) | wartość wpisana raz nie wraca; automat nie kasuje pracy człowieka | trzy — bez kontroli kierunku |
| [`straznik-wygladu-druku`](./straznik-wygladu-druku.md) | rama, typografia, dualizm, zapełnienie kartki | dwie — bez kontroli zapełnienia |
| <!-- straznik:ignoruj --> [`straznik-powloki`](./straznik-powloki.md) | aplikacja: menu, kafle, paleta, typografia ekranu | sześć |
| <!-- straznik:ignoruj --> [`straznik-merytoryki`](./straznik-merytoryki.md) | druk mówi to, co ma; szkoła odpowiada przedszkolu | częściowa i taka zostanie |
| <!-- straznik:ignoruj --> [`straznik-dokumentacji`](./straznik-dokumentacji.md) | dokument nie wskazuje na plik, którego nie ma | **jedyna w pełni działająca** |

## Stan folderu — 2026-09-02

⚠️ **Do repozytorium trafiło dziś tylko to, co dostarczono; sześciu strażników jeszcze tu nie ma.**
Wskazania na brakujące pliki w tabeli wyżej niosą `<!-- straznik:ignoruj -->`, żeby sonda
dokumentacji nie liczyła ich jako naruszeń — znacznik schodzi w dniu, w którym plik powstaje.

| Plik | Stan |
|---|---|
| `straznik-wygladu-druku.md` | **jest** — sprawdzony 2026-08-22 |
| `KANON-UI.md` | **jest** — materiał historyczny, sprawdzony 2026-07-29 |
| `straznik-prawo/rejestr-przepisow.json` | **jest** — 26 aktów, wygenerowany 2026-08-21 |
| `straznik-prawo/kompendium-prawno-merytoryczne.md` | **jest, ale urwany** — spis treści zapowiada 12 rozdziałów, tekst kończy się na pierwszym zdaniu rozdziału 3 |
| `straznik-prawo.md` | brak |
| `straznik-danych.md` | brak |
| `straznik-synchronizacji.md` | brak |
| `straznik-powloki.md` | brak |
| `straznik-merytoryki.md` | brak |
| `straznik-dokumentacji.md` | brak |
| `scripts/straznik-dokumentacji.mjs` | brak — narzędzie wspólne nie zostało jeszcze przeniesione |

⚠️ **Prostowanie:** sekcja „Co jeszcze leży w folderze" mówi o **24 aktach** w rejestrze;
plik zawiera **26 wpisów o unikalnych identyfikatorach** (policzone 2026-09-02).

## Zakres

**Sześć modułów: metryczka, wopf, ipet, ewaluacja, realizacja, zespół** — 78 druków.
Nic poza nimi nie podlega strażnikom.

**Tryby szkolne** są dziś zamknięte flagą; strażnicy obejmą je, gdy się otworzą — i to jest główny
powód, dla którego powstali.

## Trzy wyniki

| Wynik | Znaczenie | Co dalej |
|---|---|---|
| **ZGODNE** | reguła spełniona | nic |
| **NARUSZENIE** | reguła złamana bez uzasadnienia | poprawka albo zadanie |
| **WYJĄTEK** | świadome odstępstwo z zapisanym powodem | wpis w sekcji „Wyjątki", z datą i autorem |

Wyjątek bez powodu jest naruszeniem. Wyjątek „bo tak było" — też.

## Narzędzie wspólne

`scripts/straznik-dokumentacji.mjs` pilnuje reguły nadrzędnej dla wszystkich sześciu:
**dokument nie wskazuje na plik, którego nie ma.** Stan na 2026-08-21: **ZGODNE**, 281 wskazań
sprawdzonych, 0 naruszeń.

Wskazanie celowe (zdanie o skasowanym pliku) oznacza się `<!-- straznik:ignoruj -->` w linii
albo `<!-- straznik:ignoruj-sekcje -->` pod nagłówkiem — inaczej sonda liczy je jako naruszenie.

## Zasada utrzymania

**Dokument ma zgadzać się ze stanem faktycznym, nie z intencją sprzed pół roku.** Każdy niesie datę
sprawdzenia i ⚠️ przy każdym zapisie, który przestał być prawdą.

Przy pierwszym pisaniu (2026-08-21) prostowanie było potrzebne **cztery razy** — i to jest najlepszy
argument za istnieniem strażników: nikt tych rozjazdów nie zauważył przez pół roku, bo nic ich
nie sprawdzało.

**Dokumenty mają być krótkie.** To materiał do weryfikacji, nie podręcznik: reguła, pomiar, granica.
Uzasadnienia idą do zadań, nie tutaj.

## Co jeszcze leży w folderze

- [`KANON-UI.md`](./KANON-UI.md) — **materiał historyczny, nie źródło prawdy.** Opis zrzutu ekranu
  z lipca 2026, częściowo rozjechany z kodem, cytowany z pięciu miejsc w CSS powłoki przez numery
  sekcji. **Konflikt z kodem rozstrzyga kod.** Jego los czeka na decyzję Arka.
- [`straznik-prawo/rejestr-przepisow.json`](./straznik-prawo/rejestr-przepisow.json) — 24 akty
  ze skanu 559 plików; pola prawne wypełnia `E18`. ⚠️ Wpisów jest dziś **26** — patrz „Stan folderu".
- [`straznik-prawo/kompendium-prawno-merytoryczne.md`](./straznik-prawo/kompendium-prawno-merytoryczne.md)
  — materiał wejściowy dla `straznik-prawo`: ramy RODO, dane medyczne, SOM, taryfikator godzin
  rewalidacji. **Nie jest strażnikiem i nie jest kompletny** — tekst urywa się na rozdziale 3 z 12.

## Skąd się wzięli

Projekt `D07`, wdrożenie `Z34`, kanon druku i procedura `Z35` — w `docs/e-zadania/`.
Wcześniej reguły żyły w sześciu plikach `KANON-*.md`; pięć zastąpili strażnicy.
