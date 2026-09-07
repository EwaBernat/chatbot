---
name: awatar-ewa-pctp
description: Postać „Ewa PCTP" — filmowy awatar użytkowniczki (autorki EduPlaner 2026, PCTP Koszalin) do wywoływania w filmach i prezentacjach, zawsze z jej własnym głosem. Skill trzyma kartę postaci (wygląd, kadr, strój, ton), gotową wyciętą postać (PNG i klip WebM z przezroczystym tłem) oraz skrypty, które wycinają Ewę z dowolnego klipu HeyGen, nakładają ją na plansze, ekrany aplikacji i filmy, wstawiają do prezentacji PPTX i do kompozycji Remotion (na żądanie, przełącznikiem --awatar) i pamiętają jej awatara HeyGen. Użyj ZAWSZE, gdy prosi o: „wstaw Ewę", „dodaj awatara do filmu/prezentacji", „Ewa niech to powie", „nagraj z moją postacią", „Ewa PCTP", „Agent Ewa", „postać Ewy", „awatar w rogu", „pobierz samą postać", „wytnij mnie z tła", „Ewa na planszy", „intro z Ewą", „mój awatar do filmów", „Ewa w Remotion", „awatar w filmie z wykresami", a także gdy wgrywa film z awatarem HeyGen i chce z niego korzystać dalej. Wyzwalaj przy hasłach: awatar, postać, HeyGen, Remotion, przezroczyste tło, alfa, WebM, PNG postaci, prezentacja z awatarem, film z Ewą. Głos i dane liczbowe obsługuje skill dane-i-glos — ten skill dodaje do nich twarz.
---

# Awatar „Ewa PCTP"

Jedna postać, jeden wygląd, jeden głos. Ewa PCTP to filmowe wcielenie użytkowniczki:
awatar HeyGen z jej twarzą, mówiący jej sklonowanym głosem z ElevenLabs. Ten skill
sprawia, że Ewę da się **wywołać** w dowolnym materiale — filmie, planszy, prezentacji —
bez ustalania za każdym razem, jak ma wyglądać i skąd wziąć jej klip.

Karta postaci (wygląd, kadr, strój, gest, ton): `references/postac.md`. Przeczytaj ją,
zanim opiszesz Ewę w scenariuszu albo zlecisz jej nową scenę.

## Zasady nadrzędne

1. **Tylko jej głos.** Ewa mówi wyłącznie klonem głosu użytkowniczki z ElevenLabs
   (zasada ze skilla `dane-i-glos`). Bez zapamiętanego głosu: napisz scenariusz,
   przygotuj plansze, ale **nie renderuj** mówiącej Ewy i nie proponuj głosu zastępczego.
2. **Tylko jej awatar.** Ewa powstaje wyłącznie z awatara, który użytkowniczka sama
   utworzyła w HeyGen (zgoda na wizerunek). Nigdy nie generuj jej twarzy ani sylwetki
   innym narzędziem (generatory obrazu i wideo, „podobna postać", stockowa modelka).
3. **Jeden wygląd.** Zawsze ten sam strój, fryzura, okulary i kadr z karty postaci.
   Nie „odświeżaj" wyglądu, nie zmieniaj koloru marynarki pod tło, nie kadruj inaczej,
   niż opisuje karta — rozpoznawalność jest ważniejsza niż urozmaicenie.
4. **Marka.** Tła i plansze w kolorach EduPlaner / PCTP: fiolet `#2D1B69`, pomarańcz
   `#E8450A`, Arial. Marynarka Ewy jest w odcieniu fioletu marki, więc na fiolecie
   marki postać zlewa się dołem — dawaj jej jasny akcent (pasek, plansza, obraz) albo
   układ z Ewą na jasnym polu.

## Co skill ma od ręki (bez żadnego API)

| Plik | Co to jest | Do czego |
|---|---|---|
| `assets/ewa_pctp.png` | wycięta postać, 772×1026 px, przezroczyste tło | slajdy, plansze, miniatury, strona |
| `assets/ewa_pctp_intro.webm` | intro (13 s) z kanałem alfa, z oryginalnym dźwiękiem | wstawka wideo, test układów, czołówka |
| `assets/intro_tekst.txt` | tekst intro („Dzień dobry. Mam na imię Ewa…") | wzorzec rejestru, gotowa czołówka szkolenia |
| `assets/ewa_kadr.jpg` | kadr wzorcowy 1280 px | wzorzec wyglądu i kadru |
| `assets/ewa_gesty.jpg` | cztery klatki gestów | wzorzec ruchu rąk i mimiki |

Gdy użytkowniczka prosi „daj mi samą postać" — wyślij `assets/ewa_pctp.png`
(i `assets/ewa_pctp_intro.webm`, jeśli chce ruch) przez `SendUserFile`. Nic nie trzeba
renderować.

## Kiedy co uruchomić

| Prośba | Droga |
|---|---|
| „Pobierz / daj mi samą postać" | wyślij `assets/ewa_pctp.png` (+ `.webm`) |
| „Wytnij Ewę z tego filmu" | `wytnij_postac.py film.mp4` → `ewa.webm` + `ewa.png` |
| „Ewa niech powie ten tekst" (nowa scena) | **A** scenariusz → głos (dane-i-glos 4a) → HeyGen `--audio --tlo "#00FF00"` → `wytnij_postac.py --tlo "#00FF00"` |
| „Wstaw Ewę do filmu / na planszę / na ekran aplikacji" | **B** `wstaw_ewe.py` |
| „Ewa w rogu prezentacji", „awatar na slajdach" | **C** `ewa_do_prezentacji.py` |
| „Intro z Ewą" | `assets/ewa_pctp_intro.webm` → `wstaw_ewe.py --tlo plansza.png` |
| „Ewa w Remotion", „awatar w filmie z wykresami" | **D** `przygotuj_remotion.py --awatar ewa.webm` |
| „Zapamiętaj mojego awatara" | `zapamietaj_awatara.py --avatar-id <id>` |

Zależności skryptów (jednorazowo): `pip install -r .claude/skills/awatar-ewa-pctp/requirements.txt`.
Systemowego ffmpeg nie trzeba — `imageio-ffmpeg` przynosi własny.

## Droga A — nowa scena z Ewą (jej głos + jej twarz)

Ewa mówi coś nowego. Cały łańcuch to skill `dane-i-glos` plus dwa kroki na końcu:

```
scenariusz (references/narracja.md w dane-i-glos)
  → elevenlabs_tts.py narracja.txt -o glos.mp3 --srt napisy.srt      # jej klon głosu
  → heygen_awatar.py --audio glos.mp3 --tlo "#00FF00" --czekaj -o ewa_zielona.mp4
  → wytnij_postac.py ewa_zielona.mp4 --tlo "#00FF00" --webm ewa.webm --png ewa.png
  → droga B albo C
```

Dlaczego zielone tło, a nie fiolet marki: marynarka Ewy jest fioletowo-granatowa,
klucz na fiolecie wyciąłby ją razem z tłem. Zielony `#00FF00` nie występuje w postaci.
Jeśli użytkowniczka eksportuje z aplikacji HeyGen, niech wybierze **WebM z przezroczystym
tłem** — wtedy `wytnij_postac.py` tylko przepakowuje, bez kluczowania.

`heygen_awatar.py` bierze awatara z pamięci skilla (`zapamietaj_awatara.py`), więc nie
pytaj o `avatar_id` przy każdej scenie. Jeśli pamięć jest pusta, zapytaj raz i zapamiętaj.

Uwaga na sieć: w środowisku zdalnym polityka sieciowa może blokować ElevenLabs i HeyGen
(`403` z proxy). Wtedy wszystko, co nie wymaga API, i tak zrób — scenariusz, plansze,
kompozycję z gotowym klipem — a render głosu i awatara zostaw na komputer użytkowniczki
albo złącze MCP ElevenLabs, jeśli jest w sesji. Szczegóły w `dane-i-glos/SKILL.md`.

## Droga B — Ewa w filmie (plansza, ekran aplikacji, kolor marki)

```bash
python3 .../wstaw_ewe.py ewa.webm --sprawdz                                  # czy klip ma alfę
python3 .../wstaw_ewe.py ewa.webm -o film.mp4                                # pełny kadr, fiolet marki
python3 .../wstaw_ewe.py ewa.webm --tlo plansza.png --uklad rog -o film.mp4   # Ewa mała w rogu
python3 .../wstaw_ewe.py ewa.webm --tlo plansza.png --uklad rog --kolo        # ...w kółku (webinar)
python3 .../wstaw_ewe.py ewa.webm --tlo ekran_aplikacji.mp4 --uklad lewa      # Ewa z lewej, treść z prawej
python3 .../wstaw_ewe.py ewa.webm --pion --uklad pelny                        # 1080×1920 pod Reels
python3 .../wstaw_ewe.py ewa.webm --audio glos.mp3 --napisy napisy.srt        # własny dźwięk + napisy
```

Układy: `pelny` (cała wysokość, środek), `rog` (42 % wysokości, prawy dolny róg),
`lewa` / `prawa` (90 % wysokości, przy krawędzi, druga połowa ekranu na treść).
`--skala`, `--margines`, `--x`, `--y` zmieniają domyślne pozycje. Bez alfy w klipie
podaj `--klucz "#00FF00"`. `--suchy-bieg` pokazuje polecenie ffmpeg bez renderu.

Przy scenach powitania i pożegnania Ewa jest **duża** (`pelny`, `lewa`, `prawa`);
przy omawianiu ekranów aplikacji **mała** (`rog`), żeby nie zasłaniać treści — tak jak
w storyboardach ze skilla `eduplaner-reklama`.

Plansze tła rób w kolorach marki (skill `eduplaner-reklama`, `scripts/build_slides.py`)
albo z Remotion (`dane-i-glos/assets/remotion`). Remotion i HyperFrames czytają WebM
z alfą bezpośrednio (`<OffthreadVideo transparent>` / `<video>`), więc Ewę można też
wstawić w kodzie kompozycji zamiast przez ffmpeg.

## Droga C — Ewa w prezentacji (PPTX)

```bash
# nieruchoma Ewa na wybranych slajdach (przezroczyste tło, wtapia się w każdy slajd)
python3 .../ewa_do_prezentacji.py szkolenie.pptx --obraz assets/ewa_pctp.png --slajdy 1,8 --pozycja prawa

# mówiąca Ewa: klip MP4 na tle w kolorze slajdu (PowerPoint nie odtwarza wideo z alfą)
python3 .../wstaw_ewe.py ewa.webm --tlo "#2D1B69" -o ewa_wstep.mp4
python3 .../ewa_do_prezentacji.py szkolenie.pptx --klip 1=ewa_wstep.mp4 --klip 9=ewa_finał.mp4 --pozycja srodek
```

Pozycje: `rog` (6 cm, prawy dolny), `lewa` / `prawa` (11 cm, przy krawędzi), `srodek`
(14 cm, dół slajdu). `--wysokosc-cm` zmienia rozmiar. Klip startuje po kliknięciu;
automatyczny start ustawia się w PowerPoint (Odtwarzanie → Start: Automatycznie) —
powiedz to użytkowniczce przy oddawaniu pliku.

Do prezentacji budowanych od zera (skill `pptx`) wstaw `assets/ewa_pctp.png` jak zwykły
obraz — to najprostsza droga, gdy Ewa ma tylko „być", a nie mówić. Głos do slajdów robi
`dane-i-glos` (MP3 z jej klonem); klip z mówiącą Ewą powstaje drogą A.

## Droga D — Ewa w Remotion (na żądanie)

Szablon filmu z danych (`dane-i-glos/assets/remotion`) ma wbudowany komponent `Awatar`.
Ewa **nie pojawia się sama** — tylko gdy użytkowniczka o nią poprosi; wtedy dodaj
przełącznik `--awatar` do składania projektu:

```bash
python3 .claude/skills/dane-i-glos/scripts/przygotuj_remotion.py ~/moj-film \
        --profil profil.json --narracja narracja.txt --audio glos.mp3 --napisy napisy.srt \
        --awatar ewa.webm --awatar-uklad rog            # albo pelny / lewa / prawa
        # --awatar-od 0 --awatar-do 13 --awatar-skala 0.5
cd ~/moj-film && npm install && npx remotion render RaportWideo out/film.mp4
```

Skrypt kopiuje klip do `public/` i dopisuje do `film.json` wpis `awatar` (`plik`,
`uklad`, `odSek`, opcjonalnie `doSek`, `skala`, `margines`, `dzwiek`). Kilka odcinków
z Ewą to lista `awatar: [...]` w `film.json` — np. powitanie w układzie `pelny` od zera
do trzynastej sekundy i pożegnanie w rogu od pięćdziesiątej. Długość filmu sama
uwzględnia koniec klipu Ewy.

Zasady, których pilnuje szablon:

- klip musi być **WebM z alfą** (`wytnij_postac.py --webm`); `OffthreadVideo transparent`
  odczytuje przezroczystość, więc Ewa stoi na tle sceny, nie w prostokącie,
- gdy film ma `audio` (narracja z ElevenLabs), klip Ewy jest **wyciszony** — inaczej
  głos byłby podwójny; bez `audio` Ewa mówi własną ścieżką z klipu,
- układy i proporcje są te same co w `wstaw_ewe.py`, więc ffmpeg i Remotion dają
  ten sam kadr.

Przezroczysty render jest wolniejszy (Remotion wyciąga klatki jako PNG); 13 s Ewy
w 1080p to kilka dodatkowych minut. W kontenerze bez przeglądarki dodaj
`--browser-executable` wskazujący `headless_shell` (patrz `dane-i-glos/assets/remotion/README.md`).

## Pamięć awatara

Identyfikator awatara HeyGen leży w tej samej pamięci co głos ElevenLabs
(`~/.config/dane-i-glos/konfiguracja.json`, poza repozytorium, bez kluczy API):

```bash
python3 .../zapamietaj_awatara.py --pokaz
python3 .../zapamietaj_awatara.py --szukaj Ewa                 # wymaga HEYGEN_API_KEY
python3 .../zapamietaj_awatara.py --avatar-id <id> --nazwa "Ewa PCTP"
```

Od tej chwili `heygen_awatar.py` z `dane-i-glos` używa Ewy bez `--avatar-id`.

## Oddawanie pracy

Wyślij pliki przez `SendUserFile`, nie tylko ścieżki: film MP4 albo prezentację PPTX,
a przy wycinaniu — `ewa.png` i `ewa.webm`. Podaj czas trwania, układ i to, co zużyło
kredyty (znaki ElevenLabs, minuty HeyGen). Materiał, w którym Ewa mówi cudzym głosem,
nie istnieje — nie oddawaj go.

## Materiały

- `references/postac.md` — karta postaci: wygląd, strój, kadr, gest, ton, parametry techniczne
- `references/produkcja.md` — eksport z HeyGen, kluczowanie, alfa w różnych formatach, Remotion, kody błędów
- `assets/` — gotowa postać (PNG, WebM z alfą) i kadry wzorcowe
- `scripts/wytnij_postac.py` — sama postać z klipu (szachownica / kolor / alfa → WebM, MOV, PNG, sekwencja)
- `scripts/wstaw_ewe.py` — Ewa na tle, planszy albo filmie (układy, kółko, napisy, pion)
- `scripts/ewa_do_prezentacji.py` — Ewa na slajdach PPTX (obraz albo klip)
- `scripts/zapamietaj_awatara.py` — pamięć awatara HeyGen
