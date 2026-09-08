---
name: bank-celow-smart
description: 'Rozbudowa banku celów SMART KPOF dla przedszkola (EduPlaner 2026, PCTP Koszalin, autorka Mirosława Ewa Jurczyszyn) — dopisywanie konspektów zajęć, kart pomocy dydaktycznych z nagraniem jej głosem, arkuszy A4 do wydruku, symboli do biblioteki obrazkowej i historyjek obrazkowych, a potem przebudowa dokumentów i spakowanie kompletu dla programisty. Użyj ZAWSZE, gdy prosi o: „dopisz konspekt”, „dodaj cel SMART”, „brakuje materiałów do wydruku”, „uzupełnij pomoce dydaktyczne”, „dorysuj symbole”, „zrób historyjkę obrazkową”, „przebuduj bank”, „sprawdź, czy wszystko się drukuje”, „spakuj bank dla Arka”, a także przy hasłach: bank celów SMART, KPOF, druk KC-1, KC-3, KC-4, konspekt przedszkolny, karta pomocy, arkusz do wycięcia, biblioteka symboli, poziom wsparcia I/II/III, twierdzenie, podstawa 2026, wersja A/B/C/U. NIE używaj do dokumentów ucznia — WOPF, IPET, Bazę Uczniów i Raport Ucznia obsługują skille eduplaner-pctp oraz ipet-raport-pctp.'
---

# Bank celów SMART — rozbudowa

Bank to jeden plik HTML otwierany z dysku, bez serwera i bez konta: **178 konspektów,
534 cele SMART, 144 karty pomocy, 226 arkuszy A4, 163 symbole, trzy historyjki
obrazkowe.** Wszystko siedzi w środku jako `data:` URI, więc dokument działa
u nauczyciela bez internetu.

Ten skill prowadzi rozbudowę tak, żeby nowy element wszedł do dokumentu naprawdę,
a nie tylko do kodu. Bank ma jedną nieoczywistą cechę, wokół której kręci się
połowa poniższych zasad: **brak nie wysypuje budowania.** Karta bez zdjęcia dostaje
pole zastępcze, arkusz z nienarysowanym symbolem jest po cichu pomijany, dokument
składa się dalej i wygląda dobrze. Nauczyciel dowiaduje się o braku dopiero przy
drukarce, w sali, przy dziecku. Dlatego po każdej partii sprawdzamy pomiarem,
zamiast zakładać.

## Zanim cokolwiek dopiszesz

```bash
python3 .claude/skills/bank-celow-smart/scripts/sprawdz_bank.py
```

Wypisuje stan całości: konspekty per wersja, arkusze gotowe do złożenia, symbole
narysowane, karty bez zdjęcia albo bez nagrania, pokrycie podstawy. Kończy się
kodem 1, gdy znalazł brak. Uruchom to **przed** pracą (żeby wiedzieć, od czego
zaczynasz) i **po** (żeby wiedzieć, że nic nie zniknęło).

## Cztery zasady, których nie wolno złamać

**1. Nagrania tylko jej własnym, sklonowanym głosem.** `voice_id
jq4ZUryuBeDqmtkKtBZ4`, model `eleven_v3`. Materiał firmowany jej nazwiskiem ma
brzmieć nią. Gdy głos jest niedostępny — oddaj sam tekst polecenia i zatrzymaj
się; nie podstawiaj głosu premade „na próbę". Rejestr aktorski i zasady pisania
tekstu mówionego: `references/pomoce.md`.

**2. Twierdzenia KPOF i cele uzupełniające to dwa różne zbiory.** Wersje A, B i C
pochodzą z jej arkuszy KPOF. Wersja U to cele dopisane po to, by domknąć pokrycie
podstawy do 113/113. Wymyślonego celu nie wolno dopisać do wersji A, B ani C —
to nie jest kwestia porządku, tylko wiarygodności narzędzia diagnostycznego.

**3. Do dziecka mów prosto.** Każdy tekst, który usłyszy albo przeczyta
przedszkolak — polecenie na karcie pomocy, etykieta na arkuszu, narracja
historyjki — pisz **krótkimi, prostymi zdaniami i bez trudnych słów**.
Przedszkolak nie rozumie wyrazów typu *strategia*, *sygnał*, *instrukcja*,
*sekwencja*, *komunikat*, *procedura*, *technika*, *emocja* w roli terminu.
Zamiast nich pisz to, co dziecko widzi i robi: **sposób**, **kartka**,
**dzwonek**, **gwizdek**, **co ci pomaga**, **kiedy robi się trudno**.
Jedno zdanie = jedna czynność; dwa krótkie zdania są lepsze niż jedno długie.

Trudne słowa zostają tam, gdzie czyta je **dorosły** — w celu SMART, w opisie
metod, w trzech krokach użycia pomocy i we wskazówce dla prowadzącego. Sprawdź
to przed nagraniem, bo poprawka po nagraniu kosztuje drugie nagranie:

```bash
python3 - <<'EOF'
import sys, re, importlib; sys.path.insert(0, 'src')
TRUDNE = ['strategi','sygnał','sekwencj','komunikat','instrukcj','procedur','technik',
          'regulacj','identyfik','alternatyw','konsekwencj','koncentr','analiz','wizualiz']
for mod in ('pomoce_a','pomoce_b','pomoce_c','pomoce_u'):
    m = importlib.import_module(mod)
    for kod, poz in m.POMOCE.items():
        tekst = str(poz[4])
        trafienia = [w for w in TRUDNE if w in tekst.lower()]
        dlugie = [z for z in re.split(r'[.!?]', tekst) if len(z.split()) > 14]
        if trafienia or dlugie:
            print(mod, kod, trafienia, f'{len(dlugie)} długich zdań')
EOF
```

**4. Jeden symbol = jeden plik, używany wszędzie tak samo.** Dziecko korzystające
z komunikacji obrazkowej musi widzieć **ten sam** obrazek na tablicy AAC, w planie
dnia i na breloku. Symbol, który zmienia wygląd między materiałami, przestaje być
słowem. Nigdy nie rysuj drugiego „podobnego" symbolu pod jeden konspekt — dopisz
istniejący albo dołóż nowy do wspólnej biblioteki.

## Co gdzie leży

```
eduplaner_przedszkole/
  src/dane_34|5|6|uzup.py      twierdzenia i cele SMART — treść banku
  src/konspekty_<wersja>_d<n>.py   konspekty, moduł na wersję i obszar
  src/pomoce_a|b|c|u.py        karty pomocy dydaktycznych
  src/karty_druk.py            arkusze A4 przy konspektach (7 rodzajów)
  src/symbole.py               biblioteka symboli: kod → podpis + opis rysunku
  src/zalacznik_c1.py          historyjka „Jak rośnie kwiatek”
  src/zalaczniki_hist.py       historyjki „Zgubiony klucz” i „Wieża Zosi”
  src/moje_konspekty.py        edytor własnych konspektów w przeglądarce
  src/build.py                 bank (KC-1) · build_konspekty.py (KC-3) · build_pomoce.py (KC-4)
  src/kompresuj_media.py       PNG → k_*.jpg, MP3 → 40 kbps mono
  src/eksport_json.py          cała treść banku do JSON, dla aplikacji
  assets/                      symbole, zdjęcia pomocy, nagrania, kadry historyjek
```

## Ścieżki rozbudowy

Wybierz to, o co prosi, i przeczytaj odpowiedni plik z `references/` **zanim**
zaczniesz pisać treść — każdy z nich niesie wzór, ograniczenia i pułapki, które
w tym projekcie już raz kosztowały przebudowę.

| Prośba | Przeczytaj | Potem |
|---|---|---|
| „dopisz konspekt do celu X" | `references/konspekt.md` | przebuduj + sprawdź |
| „brakuje pomocy dydaktycznej" | `references/pomoce.md` | zdjęcie + nagranie jej głosem |
| „brakuje materiałów do wydruku" | `references/arkusze.md` | arkusz + ewentualnie nowe symbole |
| „dorysuj brakujące symbole" | `references/arkusze.md` (sekcja o rysowaniu) | kompresja + kontakt |
| „zrób historyjkę obrazkową" | `references/historyjki.md` | 5 scen + narracja + trzy karty A4 |
| „nie drukuje się dobrze" | `references/druk.md` | pomiar `zmierz_a4.mjs` |
| „spakuj to dla programisty" | niżej, sekcja *Paczka* | `spakuj_dla_programisty.py` |

## Pętla robocza

Ta sama dla każdej ścieżki:

```bash
# 1. treść — dopisz w odpowiednim module w src/
# 2. media — jeśli doszły nowe obrazki albo nagrania:
python3 src/kompresuj_media.py
# 3. przebuduj dokumenty (z katalogu eduplaner_przedszkole)
python3 src/build.py && python3 src/build_konspekty.py && python3 src/build_pomoce.py
# 4. sprawdź spójność
python3 ../.claude/skills/bank-celow-smart/scripts/sprawdz_bank.py
# 5. sprawdź druk — czy każdy arkusz mieści się na jednej stronie A4
node ../.claude/skills/bank-celow-smart/scripts/zmierz_a4.mjs
```

Kroku 5 nie da się zastąpić oglądaniem. Arkusz, który wyjdzie poza stronę, nie
zgłasza błędu — po prostu drukuje się na dwóch kartkach, z kaflami rozciętymi
w pół. `kompresuj_media.py` **pomija pliki już przetworzone**: po poprawieniu
obrazka skasuj stary `k_*.jpg`, inaczej dokument dalej pokaże poprzednią wersję.

## Kiedy pytać, a kiedy działać

Rozbudowa treści merytorycznej to jej dziedzina, nie twoja. Sam dopisuj to, co
wynika wprost z tego, co już jest: brakujący arkusz do istniejącego konspektu,
brakujący symbol do istniejącego arkusza, kartę pomocy według wzoru sąsiednich.
Zapytaj, zanim: dopiszesz nowe twierdzenie albo cel SMART, zmienisz treść
istniejącego celu, przypiszesz konspekt do innego punktu podstawy.

Gdy znajdziesz brak, o który nie pytała — powiedz o nim i **uzupełnij**, zamiast
tylko raportować. W tym projekcie brakujące elementy nie zgłaszają się same.

## Sprawdzanie efektu oczami

Dokumenty są wizualne, a Playwright jest w obrazie. Po większej zmianie zrób zrzut
i **obejrzyj go**, zanim powiesz, że gotowe:

```js
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const p = await b.newPage({ viewport: { width: 1250, height: 900 } });
await p.route('**://fonts.*/**', r => r.abort());   // pomiar bez internetu
await p.goto('file:///.../Bank_celow_SMART_KPOF.html', { waitUntil: 'domcontentloaded' });
```

Obrazki wklejone w odpowiedź **nie docierają do użytkowniczki** — pliki wysyłaj
narzędziem do wysyłania plików, nie linkiem w treści.

## Paczka dla programisty

Gdy prosi o komplet dla kogoś, kto wpina bank w aplikację:

```bash
python3 ../.claude/skills/bank-celow-smart/scripts/spakuj_dla_programisty.py \
  --cel /gdzie/zapisac --limit 28
```

Skrypt eksportuje świeży JSON, zbiera dokumenty, kod i te wersje mediów, które
naprawdę wchodzą do dokumentów, po czym dzieli całość na ponumerowane archiwa
mieszczące się w limicie przesyłki. Każda część niesie kartkę „część N z M"
z nazwami wszystkich pozostałych — gdyby któraś zaginęła, od razu widać, czego
brakuje.

Dołóż `--czytaj <plik.md>` z opisem dla odbiorcy. Najważniejsze, co ma tam być:
**dane z JSON są tym, co się wpina, a HTML jest wzorcem docelowym.** Programista,
który zacznie przepisywać treść z HTML-a, zrobi to raz i już nigdy nie zsynchronizuje.

Paczka zawiera jej nagrania głosowe — to dane biometryczne. Powiedz jej o tym,
kiedy oddajesz paczkę, żeby wiedziała, co przekazuje.

## Materiały pomocnicze

* `references/konspekt.md` — struktura konspektu, wzór modułu, jak pisać cel SMART
* `references/pomoce.md` — karty pomocy: treść, zdjęcie, nagranie jej głosem
* `references/arkusze.md` — siedem rodzajów arkusza, budżet strony, rysowanie symboli
* `references/historyjki.md` — historyjka obrazkowa: sceny, prompty, narracja, prefiksy
* `references/druk.md` — reguły druku, o które łatwo się potknąć
* `scripts/sprawdz_bank.py` — kontrola spójności całości
* `scripts/zmierz_a4.mjs` — pomiar, czy wszystko mieści się na A4
* `scripts/spakuj_dla_programisty.py` — paczka podzielona na ponumerowane części
