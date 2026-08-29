---
name: dane-firmy-pctp
description: Jedyne źródło prawdy o danych firmowych PCTP Koszalin i EduPlaner 2026 — logo (plik SVG), pełna nazwa placówki, autorka, telefon, e-mail, adres www, kolory marki, typografia, hasła i ton głosu. Użyj ZAWSZE, gdy tworzysz cokolwiek firmowanego marką: broszurę, ulotkę, plakat, prezentację, planszę, post, dokument Word, arkusz, aplikację HTML, stronę, film lub materiał reklamowy — także wtedy, gdy użytkowniczka nie prosi o to wprost, a jedynie mówi „zrób to w moich kolorach", „dodaj logo", „wstaw moje dane", „dane firmy", „stopka z kontaktem", „podpisz to mną", „marka PCTP", „identyfikacja wizualna". Wyzwalaj też, gdy trzeba sprawdzić lub poprawić dane kontaktowe albo podpis autorki w istniejącym materiale. NIE używaj do treści merytorycznej dokumentów (WOPF, IPET, Raport Ucznia, Baza Uczniów) — te obsługują skille eduplaner-pctp oraz ipet-raport-pctp; ten skill dostarcza wyłącznie warstwę firmową.
---

# Dane firmy · PCTP Koszalin i EduPlaner 2026

Ten plik jest jedynym źródłem prawdy o danych firmowych. **Nie zmyślaj danych spoza niego** —
telefonu, adresu, NIP-u ani nazwiska współpracownika. Jeśli czegoś tu nie ma, a materiał tego
wymaga, zapytaj użytkowniczkę zamiast zgadywać. Zły numer telefonu na wydrukowanej ulotce
kosztuje nakład, a nie poprawkę.

## Dane podstawowe

| Pole | Wartość |
|---|---|
| Placówka | **PCTP Koszalin** — Pomorskie Centrum Terapii Pedagogicznej |
| Produkt | **EduPlaner 2026** — cyfrowa aplikacja z dokumentacją placówki |
| Ekosystem dokumentów | **EduPlaner2026‑MJ‑PCTP** |
| Autorka / opracowanie | **pedagog specjalny mgr Mirosława Ewa Jurczyszyn** |

Podpis autorki zapisuj dokładnie w tej kolejności — **tytuł zawodowy przed nazwiskiem**:
„pedagog specjalny mgr Mirosława Ewa Jurczyszyn". Tak podpisuje swoje materiały.

## Kontakt

| Kanał | Wartość |
|---|---|
| Strona | **www.eduplaner2026.pl** |
| E‑mail | **kontakt@eduplaner2026.pl** |
| Telefon | **[usunięto]** |

W materiałach cyfrowych rób te dane klikalnymi (`https://`, `mailto:`, `tel:+48[usunięto]`) —
z ulotki oglądanej na telefonie użytkownik dzwoni jednym dotknięciem.

## Logo

Pliki: **`assets/logo-pctp.svg`** (sam znak) oraz **`assets/logotyp.html`**
(gotowy do wklejenia blok `<symbol>` + logotyp + CSS — nie buduj go od nowa).

Znak: — okrągła odznaka: fioletowy krążek z jasną obwódką,
kwiat o pięciu płatkach (dwa jasnofioletowe na zewnątrz, dwa brzoskwiniowe, pomarańczowy
w środku, biała kropka, złote łodygi) i napis **PCTP** szeryfową antykwą.

> **Uwaga o pochodzeniu pliku.** Ten SVG to **rekonstrukcja** odrysowana z obrazu przesłanego
> przez autorkę — plik źródłowy nie był dostępny. Jest bardzo bliski oryginałowi, ale nie jest
> jego kopią. Gdy pojawi się plik źródłowy (SVG lub PNG w wysokiej rozdzielczości), podmień
> `assets/logo-pctp.svg` i usuń tę uwagę. Do druku wielkoformatowego poproś o oryginał.

### Jak używać

Odznaka jest okrągła i **niesie własne fioletowe tło**, więc czyta się zarówno na jasnym
papierze, jak i na ciemnym fiolecie marki — jasna obwódka daje jej oddech. Nie umieszczaj jej
na tle pomarańczowym ani na zdjęciu bez przyciemnienia.

- **Minimalny rozmiar: 64 px** (ok. 17 mm w druku). Poniżej napis „PCTP" przestaje być czytelny —
  jeśli potrzebujesz mniejszego znaku, użyj samego kwiatu bez napisu.
- Zachowaj **pole ochronne** równe połowie średnicy znaku.
- Nie rozciągaj, nie obracaj, nie zmieniaj kolorów płatków, nie dokładaj cienia ani poświaty.
- W dokumencie HTML wstaw znak raz jako `<symbol>` i użyj `<use>` w każdym miejscu —
  plik nie puchnie, a znak zostaje wektorowy i ostry w druku.

### Logotyp (lockup)

Standardowe zestawienie to odznaka + nazwa produktu + pełna nazwa placówki:

```
[odznaka]   EduPlaner 2026
            PCTP KOSZALIN · POMORSKIE CENTRUM TERAPII PEDAGOGICZNEJ
```

W „EduPlaner 2026" rok składaj pomarańczem, resztę bielą (na ciemnym tle) lub fioletem
(na jasnym). Podpis pod spodem: wersaliki, spacjowanie ok. 0,15 em, mniejszy stopień.

## Kolory

Te wartości są zgodne ze stałą `BRAND` w `ipet_data.js` — używaj ich, nie dobieraj własnych.

| Rola | HEX | Zastosowanie |
|---|---|---|
| Fiolet (główny) | `#2D1B69` | tła, nagłówki, okładki |
| Fiolet ciemny | `#1F1148` | gradienty, cieniowanie okładek |
| Pomarańcz (akcent) | `#E8450A` | akcenty, CTA, wyróżnienia |
| Zieleń | `#0D7D5C` | cele osiągnięte, sukces, „tak" |
| Czerwień | `#B8350D` | trudności, interwencja, „nie" |
| Bursztyn | `#C47A10` | uwagi, podstawa prawna, stan pośredni |
| Turkus | `#2B6E6E` | sensoryka |
| Tekst główny | `#1A1A2E` | treść |
| Tekst pomocniczy | `#5B5B72` | opisy, podpisy |
| Tło jasne fioletowe | `#F4F2FA` | tła sekcji, syntezy |
| Tło jasne pomarańczowe | `#FDF1EC` | ramki ABC, uwagi |
| Linie tabel | `#D9D5E8` | delikatne linie i obramowania |

Zieleń, bursztyn i czerwień to **kolory znaczeniowe** (sukces / częściowo / brak) — nie używaj
ich dekoracyjnie, bo w dokumentach PCTP niosą informację o poziomie realizacji celu.

## Typografia

- **Dokumenty Word i PDF do druku urzędowego:** Arial (w środowisku bez Arial użyj DejaVu Sans —
  poprawnie renderuje polskie znaki).
- **Materiały HTML i publikacje:** Sofia Sans Condensed na nagłówki, Lato na tekst ciągły,
  IBM Plex Mono na dane i liczby. Wszystkie mają pełny zestaw polskich znaków.
- Materiały, które mają działać bez internetu (wysyłane mailem, na pendrive), potrzebują
  fontów **osadzonych jako data URI** — link do Google Fonts nie zadziała offline i druk wyjdzie
  innym krojem, niż widziała autorka.
- Format dokumentów: **A4**, marginesy 1440×1080×1440×1080 DXA.

## Hasła i ton głosu

Hasła‑klamry (używaj oszczędnie, jedno na materiał):

- **Mniej dokumentów. Więcej edukacji.**
- Cyfrowa szafa dla Twojej placówki
- Odzyskaj czas dla dziecka i dla siebie
- Otwarty projekt — współtwórz go z nami

Ton: ciepły, spokojny, profesjonalny, wspólnotowy — jak do zaprzyjaźnionego, zapracowanego
profesjonalisty. Zaczynaj od ulgi, nie od straszenia papierologią. Obietnicę podpieraj konkretem.
**Nigdy nie stosuj presji sprzedażowej** („ostatnia szansa", „promocja kończy się") — kontakt
proponuj po wartości, jako „chętnie porozmawiamy, bez zobowiązań".

Odbiorca: dyrektorzy oraz nauczyciele i specjaliści przedszkoli i szkół.

## Sygnatury materiałów

Materiały szkoleniowe podpisuj sygnaturą w stopce, żeby dało się je rozróżnić w obiegu:

```
EduPlaner 2026 · PCTP Koszalin
Sygnatura: <KOD> · ekosystem EduPlaner2026-MJ-PCTP
Stan prawny: <data>
```

Kody w użyciu: **SMART‑P1** — broszura „Cele SMART w przedszkolu"; **TUE‑1** — konspekt
„Termometr napięcia". Nadając nowy kod, trzymaj się schematu `<TEMAT>-<POZIOM/NR>` i dopisz go tutaj.

Materiały odwołujące się do przepisów zawsze opatruj datą stanu prawnego — teksty jednolite
zmieniają pozycje częściej niż same przepisy, a bez daty czytelnik nie wie, czy materiał jest aktualny.
