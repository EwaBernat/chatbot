---
name: awatar-ewy
description: |
  Dobiera właściwą postać awatara HeyGen Mirosławy Ewy Jurczyszyn (PCTP Koszalin), jej głos
  z ElevenLabs i stopkę z danymi firmy — po jednej komendzie, bez pytania o identyfikatory.
  Sześć postaci: trzy szkoleniowe (Wykład, Warsztat, Konsultacja), Zajęcia z Maksem,
  Spot reklamowy i Herbatka z Ewą.
  Użyj ZAWSZE, gdy prosi o nagranie „mną", „moim awatarem", „moją twarzą" albo wymienia
  którąkolwiek postać po nazwie: „wykład", „warsztat", „konsultacja", „zajęcia z Maksem",
  „spot", „wersja spotowa", „Herbatka z Ewą", „herbatka".
  Wyzwalaj także przy: „nagraj to mną", „film ze mną", „powiedz to moim głosem i twarzą",
  „zrób z tego szkolenie", „wersja dla dzieci", „odcinek herbatki", „przebierz awatara",
  „inny strój", „ten sam tekst, inna postać", a także gdy prosi o materiał wideo dla
  dyrektorów, nauczycieli, rodziców albo dzieci i sama ma w nim wystąpić.
  NIE używaj do: filmów bez jej udziału, samej analizy danych, dokumentów WOPF/IPET
  (skille eduplaner-pctp, ipet-raport-pctp) ani do klonowania głosu od zera
  (skill dane-i-glos, etap 0).
allowed-tools: Bash, Read, Write, Edit, mcp__heygen__*, mcp__ElevenLabs__*
---

# Awatar Ewy — jedna komenda, właściwa postać

Ten skill zdejmuje z użytkowniczki obowiązek pamiętania identyfikatorów, strojów, ustawień
głosu i danych do stopki. Ona mówi, **co** ma powstać i **dla kogo**; skill dobiera **jak**.

## Zasada nadrzędna: to zawsze jej twarz i jej głos

Materiał firmowany jej nazwiskiem musi być nią. Dlatego:

- **Nigdy nie generuj postaci z opisu** jako zamiennika. Awatar z promptu to obca osoba
  podpisana jej danymi — to nie pomyłka techniczna, tylko wprowadzenie widza w błąd.
- **Nigdy nie podstawiaj cudzego głosu.** Bez jej klonu z ElevenLabs oddaj sam scenariusz
  i zatrzymaj się — dokładnie tak, jak robi to skill `dane-i-glos`.
- **Nie wymyślaj `avatar_id` ani `voice_id`.** Biorą się wyłącznie z `AVATAR-EWA.md`,
  z odpowiedzi narzędzia albo od niej.
- Zgodę na wizerunek nagrywa ona sama, przez link z HeyGena. Tego kroku nie da się obejść
  i **dobrze, że tak jest** — właśnie ten mechanizm chroni jej twarz przed cudzym użyciem.

## Krok 1 — rozpoznaj postać

Postać wynika z **odbiorcy i sytuacji**, nie z tego, czy padła jej nazwa. Jeśli komenda
nazywa postać wprost — użyj jej. Jeśli nie, wybierz po odbiorcy:

| Komenda mówi o… | Postać | Klucz |
|---|---|---|
| szkoleniu, radzie pedagogicznej, wykładzie, webinarze | **Szkolenie · Wykład** | `wyklad` |
| ćwiczeniach, pracy w grupach, instruktażu krok po kroku | **Szkolenie · Warsztat** | `warsztat` |
| rozmowie 1:1, odpowiedzi na pytanie, wsparciu dla jednej osoby | **Szkolenie · Konsultacja** | `konsultacja` |
| dziecku, uczniu, zajęciach, Maksie | **Zajęcia z Maksem** | `maks` |
| reklamie, promocji, EduPlanerze dla dyrektorów, social mediach | **Spot reklamowy** | `spot` |
| odcinku, rozmowie z widzami, kulisach, luźnym temacie | **Herbatka z Ewą** | `herbatka` |

Gdy komenda pasuje do dwóch postaci (np. „szkolenie dla rodziców o Maksie"), zapytaj
**jednym krótkim zdaniem**, która ma być — i podaj swoją propozycję, żeby wystarczyło
potwierdzić.

📖 **Pełne definicje — strój, kadr, tło, ton, tempo, znaczniki głosu, długość:
[`references/postacie.md`](references/postacie.md).** Wczytaj sekcję wybranej postaci
przed pisaniem scenariusza; ton i tempo różnią się między nimi bardziej niż wygląd.

## Krok 2 — sprawdź, czym dysponujesz

Przeczytaj `AVATAR-EWA.md` z katalogu głównego repozytorium. To jedyne źródło
identyfikatorów.

| Stan | Co zrób |
|---|---|
| `Group ID` wypełnione | rozwiąż aktualne looki (`list_avatar_looks`) i pracuj normalnie |
| `Group ID` puste | **nie generuj awatara po cichu.** Napisz jednym zdaniem, że awatar czeka na utworzenie, i oddaj scenariusz + gotowy tekst narracji. Reszta pipeline'u zadziała, gdy identyfikator się pojawi |
| brak połączenia z HeyGenem | to samo — plus wskaż `HEYGEN-START.md`, sekcja „Krok 1" |

Niedokończony materiał z uczciwą informacją jest wart więcej niż film z obcą twarzą.

## Krok 3 — napisz scenariusz pod postać

Treść merytoryczną bierz z właściwego źródła (dane, `eduplaner-reklama/references/marka.md`,
dokumenty), ale **rytm i słownictwo dobierz do postaci**. Różnica między „Wykładem"
a „Zajęciami z Maksem" to nie kosmetyka — to inne zdania, inna długość, inny poziom
abstrakcji.

Zawsze powstają **dwa pliki tekstowe**:

- `narracja.txt` — czysty tekst, bez znaczników. Dla modeli, które ich nie obsługują.
- `narracja-v3.txt` — ten sam tekst ze znacznikami reżyserii dla `eleven_v3`.

⚠️ `eleven_multilingual_v2` przeczytałby `[warmly]` na głos. Dlatego dwa pliki, nie jeden.

## Krok 4 — głos

Domyślnie klon **„Ewa-głos_do skils"** (`jq4ZUryuBeDqmtkKtBZ4`), model `eleven_v3`.
Ustawienia różnią się między postaciami — tabela w `references/postacie.md`.

Zasady rytmu, które przesądzają o tym, czy głos brzmi ciepło czy jak katarynka —
jedno zdanie w akapicie, wyliczenia po kropce, `--stability` niżej niż domyślne —
są w `.claude/skills/dane-i-glos/references/rytm_i_pauzy.md`. **Przeczytaj je przed
pierwszym nagraniem**; były ustalane odsłuchem, nie z dokumentacji.

Generuj **2–3 ujęcia i wybierz najkrótsze**. Ten sam tekst i głos potrafią dać rozrzut
siedmiu sekund — to tańsze niż skracanie treści.

## Krok 5 — film

Jeśli jest połączenie z HeyGenem i `Group ID`:

1. ElevenLabs robi MP3 (krok 4).
2. `create_video` z tym MP3 jako ścieżką audio — HeyGen animuje usta do gotowego nagrania,
   nie czyta tekstu sam. Dzięki temu w filmie jest **jej** głos, nie katalogowy.
3. Kadr, tło i format według postaci.

Bez połączenia: `dane-i-glos/scripts/heygen_awatar.py --audio <mp3> --avatar-id <id>`.

## Krok 6 — stopka

Każdy materiał kończy się planszą z danymi. Bierz je z
[`references/marka-firmy.md`](references/marka-firmy.md) — jedno miejsce, żeby nie
rozjeżdżały się między filmami. Skład stopki różni się per postać: „Herbatka" ma lżejszą
niż „Wykład". Szczegóły w `postacie.md`.

Jeśli w `marka-firmy.md` brakuje pozycji (są oznaczone `<do uzupełnienia>`) — **nie zmyślaj
ani nie pomijaj po cichu**. Wstaw widoczne miejsce i powiedz jej, czego brakuje. Zły adres
strony w filmie, który pójdzie do dyrektorów, kosztuje więcej niż jedno pytanie.

## Zapamiętywanie nowych ustaleń

Gdy podczas pracy ustali coś trwałego — nowy strój, poprawione ustawienie głosu, wybrany
`look_id` dla postaci — **dopisz to do `references/postacie.md` albo `AVATAR-EWA.md`**
i powiedz jej w jednym zdaniu, że zapisałeś. Sens tego skilla polega na tym, że każda
decyzja podejmowana jest raz.

## Czego ten skill nie robi

- Nie tworzy awatara od zera — to `heygen-avatar` plus jej zgoda na wizerunek.
- Nie klonuje głosu — to `dane-i-glos`, etap 0.
- Nie pisze dokumentów WOPF/IPET — to `eduplaner-pctp` i `ipet-raport-pctp`.
- Nie robi filmów, w których ona nie występuje.

## Materiały

- `references/komendy.md` — **gotowe komendy do skopiowania**, jedna na każdą postać
- `references/postacie.md` — sześć postaci: wygląd, kadr, ton, tempo, głos, stopka, format
- `references/marka-firmy.md` — nazwa, e-mail, logo, strona, kolory, podpis autorki
- `AVATAR-EWA.md` (katalog główny) — identyfikatory HeyGen i ElevenLabs
- `.claude/skills/dane-i-glos/references/rytm_i_pauzy.md` — pauzy, tempo, ciepło głosu
- `HEYGEN-START.md` (katalog główny) — połączenie z HeyGenem, klucze, bezpieczeństwo
