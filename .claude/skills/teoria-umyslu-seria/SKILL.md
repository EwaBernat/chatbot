---
name: teoria-umyslu-seria
description: >-
  Generator kolejnych części serii broszur „Teoria umysłu" autorstwa Mirosławy Ewy Jurczyszyn (PCTP
  Koszalin) — wielostronicowe poradniki A4 (23–31 stron) dla nauczycieli i rodziców dzieci oraz uczniów w spektrum
  autyzmu. Użyj ZAWSZE, gdy użytkowniczka prosi o: „część 2/3/4 serii teoria umysłu", „kolejną
  broszurę z serii", „broszurę o TUE/TUK/TUS", „poradnik o emocjach/przekonaniach/umiejętnościach
  społecznych", „nową część o teorii umysłu", a także gdy prosi o poprawki, dodanie strony, nowe
  ćwiczenia lub aktualizację którejkolwiek części serii. Wyzwalaj też przy hasłach: broszura teoria
  umysłu, ToM w szkole, zajęcia emocjonalno-społeczne, fałszywe przekonanie, mentalizowanie, karta
  obserwacji ToM, seria Teoria umysłu. Produkt: jeden samodzielny plik HTML (strony A4 gotowe do
  druku, osadzone kroje pisma i logo PCTP, pastelowa paleta) plus PDF. NIE używaj do WOPFU, IPET, Bazy
  Uczniów ani Raportu Ucznia — te obsługują skille eduplaner-pctp oraz ipet-raport-pctp.
---

# Seria broszur „Teoria umysłu"

## Czym jest ta seria

Cykl poradników dla nauczycieli, nauczycieli współorganizujących, terapeutów i rodziców
pracujących z dziećmi i uczniami w spektrum autyzmu. Autorka: **Mirosława Ewa Jurczyszyn**,
PCTP Koszalin, kontakt **kontakt@eduplaner2026.pl**.

Część 1 („Ogólna") jest opublikowana i stanowi **wzorzec wizualny i redakcyjny dla całej serii**.
Kolejne części mają wyglądać tak, jakby wyszły z tej samej drukarni tego samego dnia —
czytelniczka ma trzymać w ręku serię, nie zbiór luźnych materiałów.

Rejestr części, mapa treści części 1 i propozycje kolejnych: **`references/seria.md`**.

## Zanim zaczniesz pisać

Ustal z użytkowniczką trzy rzeczy — reszta wynika z wzorca:

1. **Numer i nazwa części** (np. „Część 2 — Emocje"). Trafia na okładkę, na stronę końcową
   i do nadtytułu spisu treści.
2. **Zakres merytoryczny** — co ta część obejmuje i czego świadomie *nie* obejmuje,
   żeby części się nie dublowały. Sprawdź w `references/seria.md`, co już jest w części 1.
3. **Liczba gotowych materiałów** — ile ćwiczeń, czy jest karta do druku, czy jest program zajęć.
   To decyduje o objętości: część 1 ma 23 strony przy 18 ćwiczeniach, programie i karcie.

Jeśli użytkowniczka podaje tylko temat („zrób część o emocjach"), zaproponuj zakres i strukturę
stron **zanim** zaczniesz pisać HTML — łatwiej poprawić plan niż gotowe 23 strony.

## Jak zbudować część

### 1. Zacznij od szablonu, nie od zera

Skopiuj `assets/szablon.html` do katalogu roboczego. Zawiera **kompletny arkusz stylów,
osadzone kroje pisma (Fraunces + Nunito Sans w base64) i logo PCTP jako SVG**, a także
szkielet okładki i strony treściowej.

To najważniejsza decyzja techniczna w tym skillu: plik jest **samodzielny**. Nie odwołuje się
do internetu, więc drukuje się identycznie na każdym komputerze w szkole, także bez sieci.
Nigdy nie zastępuj osadzonych fontów linkiem do Google Fonts — złamiesz tę własność.

Nie zmieniaj wartości w bloku `:root` ani nazw klas. Jeśli czegoś brakuje, dopisz nową regułę
na końcu arkusza, nadając jej nazwę spoza istniejącej przestrzeni (patrz ostrzeżenie o kolizjach
klas w `references/system-wizualny.md`).

### 1a. Stopień pisma jest nienaruszalny — zawsze duży

Autorka zgłosiła przy części 2B, że wcześniejszy skład był **za drobny i trudno się go czyta**.
Szablon niesie już podniesioną skalę (tekst ciągły **11 pt**, tabele 9,5 pt, minimum 7,7 pt)
i **to jest wartość docelowa dla każdej kolejnej części**.

Zasada, od której nie ma wyjątków:

> Gdy treść nie mieści się na stronie, **dodajesz stronę albo przenosisz blok** —
> nigdy nie zmniejszasz stopnia pisma.

Kolejność sięgania po miejsce, gdy strona się nie mieści:

1. Usuń powtórzenie — sprawdź, czy tej treści nie ma już w zestawieniu zbiorczym gdzie indziej.
2. Skróć lead o jedną linijkę albo przeredaguj akapit tak, żeby zszedł o wiersz.
3. Oznacz stronę klasą `.page--zw` — zagęszcza odstępy i wyściółki, **nie rusza pisma**.
4. Przenieś blok na sąsiednią stronę z zapasem.
5. Dodaj nową stronę i rozłóż na niej treść z dwóch przepełnionych.

Zmniejszenie `font-size` nie występuje na tej liście i nie jest dopuszczalnym rozwiązaniem.
Pełna tabela wielkości: `references/system-wizualny.md`, sekcja „Skala pisma".

### 2. Pisz treść według zasad redakcyjnych

`references/zasady-redakcyjne.md` — język, znaki zapytania w tytułach, obowiązkowe zastrzeżenia
przy testach i przepisach, sposób oznaczania wykresów poglądowych, terminologia TUE/TUK/TUS.
Przeczytaj przed pisaniem: te zasady są tym, co odróżnia rzetelny materiał metodyczny
od ładnie złożonego zbioru porad.

### 3. Składaj strony z gotowych komponentów

`references/anatomia-stron.md` — katalog sprawdzonych układów: karta ćwiczenia, tabela norm
wiekowych, tabela „zamiast → powiedz", ramka prawna, wykres słupkowy, kołowy i skumulowany,
karta obserwacji jako formularz, spis treści, stopka wydawnicza. Każdy z gotowym kodem.

Wykresy generuj skryptem `scripts/wykresy.py` — ma funkcje na słupki, słupki skumulowane
i pierścień, z poprawnymi zaokrągleniami końców, odstępami między segmentami i etykietami
na pierścieniu. Ręczne liczenie `stroke-dasharray` kończy się przesuniętymi etykietami.

### 4. Sprawdź, czy strony się mieszczą — to nie jest opcjonalne

Strona A4 nie rozciąga się. Treść, która nie mieści się w `.page`, zostaje **ucięta przy druku**,
i to bez żadnego ostrzeżenia — dlatego mierzenie jest obowiązkowym krokiem, nie kontrolą jakości
na koniec.

```bash
python3 scripts/sprawdz_strony.py broszura.html
```

Skrypt otwiera plik w headless Chromium i dla każdej strony podaje zapas w pikselach.
Wartość ujemna = przepełnienie. Dwie pułapki, które kosztują najwięcej czasu:

- **Mierz przy szerokości okna ≥ 1400 px.** Poniżej 820 px włącza się układ mobilny
  (jedna kolumna) i wyniki są bezużyteczne. Skrypt robi to sam — nie zmieniaj tego.
- **W układzie dwukolumnowym o wysokości wiersza decyduje wyższa kolumna.** Skracanie tekstu
  w niższej nie daje nic. Najpierw sprawdź, która kolumna jest wyższa.

Gdy strona przepełnia się o więcej niż ~250 px, nie tnij tekstu — **przenieś blok na stronę
z zapasem albo podziel stronę na dwie**. Materiał metodyczny traci wartość, gdy się go okroi
do rozmiaru arkusza; lepiej mieć 24 strony niż 23 okrojone.

Gdy strona ma **ponad ~350 px zapasu**, wygląda na niedokończoną. Dołóż blok, który realnie
pomaga czytelnikowi (przykład ucznia, lista kontrolna, gotowa formuła zapisu) — nie powiększaj
odstępów.

### 5. Wygeneruj PDF i dostarcz

```bash
bash scripts/zrob_pdf.sh broszura.html broszura.pdf
```

Sprawdź, czy liczba stron w PDF zgadza się z liczbą sekcji `.page`. Rozjazd oznacza,
że coś przepełnia arkusz.

Dostarcz **oba pliki** — PDF do druku i HTML do dalszej edycji — a broszurę opublikuj
dodatkowo jako artefakt, żeby użytkowniczka mogła podesłać link zespołowi.

### 6. Numeracja i spis treści na końcu

Numery stron i spis treści uzupełnij **po** ustaleniu ostatecznego układu — inaczej każde
przeniesienie bloku wymaga ręcznej korekty kilkunastu liczb:

```bash
python3 scripts/sprawdz_strony.py broszura.html --numeruj
```

Przypisuje numery kolejnym stopkom (okładka = 1, bez stopki) i wypisuje mapę stron do spisu treści.
Na koniec przejrzyj odsyłacze w treści („karta obserwacji ze s. 22") — skrypt ich nie poprawia.

## Kontrola przed oddaniem

Przejdź te punkty — każdy z nich był realnym błędem przy części 1:

- Wszystkie strony mieszczą się na A4 (skrypt nie zgłasza wartości ujemnych).
- **Stopień pisma nie został nigdzie obniżony, żeby coś zmieścić** — tekst ciągły ma 11 pt,
  najdrobniejszy tekst w dokumencie nie schodzi poniżej 7,7 pt.
- Podpisy wewnątrz SVG mają realny rozmiar: `viewBox` odpowiada szerokości renderowania
  (patrz „Pułapka skali" w `references/system-wizualny.md`).
- Liczba stron w PDF = liczba sekcji `.page`.
- Polskie znaki wyświetlają się poprawnie (brak `Ĺ`, `Ă`, `â€`) — plik zaczyna się od `<meta charset="utf-8">`.
- Tytuły i etykiety w formie pytającej mają znak zapytania.
- Każdy wykres bez źródła w literaturze jest podpisany jako **model poglądowy**.
- Przy testach stoi zastrzeżenie o granicy kompetencji nauczyciela i psychologa.
- Przy przepisach stoi przypomnienie o sprawdzeniu tekstu jednolitego w ISAP.
- Nowe klasy CSS nie kolidują z istniejącymi (najczęstsza pułapka: krótkie nazwy jak `ex`, `it`, `nm`).
- Na okładce i stronie końcowej zgadza się numer części, autorka i adres kontaktowy.
