> ⚠️ **Dokument ŻYWY, ale częściowo rozjechany z kodem (sprawdzone 2026-07-29).**
> Cytuje go **5 miejsc w CSS powłoki** (`shared/layout/layout.css`, `shared/naglowek/header.css`,
> `shared/podnaglowek/submenu.css`) przez numery sekcji — dlatego zostaje w żywych dokumentach.
> **Ale nie każda wartość jest już prawdziwa:** podany niżej gradient sidebara
> `linear-gradient(180deg, #4b2d7a, #3d2566)` **nie występuje w `src/`**. Traktuj ten plik jako
> opis intencji i układu, a **konkretne wartości sprawdzaj w kodzie** — źródłem prawdy są
> `src/modules/shared/menu/sidebar.css` i tokeny `src/styles/foundation/`.
> Przy najbliższej pracy nad powłoką: albo zaktualizuj wartości tutaj, albo zdejmij cytowania z CSS.

> **Źródło:** dostarczone przez Arka 2026-07-08 (`eduplaner_ui_konwencje_v2.md`, zrzut ekranu UI),
> skopiowane 1:1 do repo jako trwałe źródło. Nie edytować
> treści poniżej ręcznie — to referencja wejściowa, interpretowana przy wdrożeniu.

# EduPlaner 2026 — konwencja UI na podstawie zrzutu ekranu

> Zakres: **bez treści kartki A4**. Opis dotyczy layoutu aplikacji, sidebaru, headera, subheadera, toolbaru i ogólnej konwencji wizualnej.
> 
> Priorytet: konwencja w stylu praktycznej specyfikacji UI dla wdrożenia frontendu.

---

## 1. Konwencja globalna

### Styl ogólny
- Interfejs ma charakter **panelu administracyjnego / dashboardu SaaS**.
- Układ jest dwukolumnowy:
  - **lewa kolumna**: sidebar nawigacyjny,
  - **prawa kolumna**: główny obszar aplikacji z headerem, subheaderem i podglądem dokumentu.
- Layout jest osadzony w dużym, jasnym mockupie z miękkim cieniem.
- Dominują:
  - **ciemne fiolety** w sidebarze,
  - **jasne neutralne tła** w części roboczej,
  - **pomarańczowy akcent** dla ważnych akcji i badge'y.

### Font
- Główny font interfejsu: **Mulish**
- Bazowy rozmiar fontu UI: **16px**

### Główne kolory
- **Sidebar gradient**: `linear-gradient(180deg, #4b2d7a, #3d2566)`
- **Akcent / CTA / badge**: `#e0522e`
- **Tło strony poza kartką**: `#eeeef3`
- **Tło nagłówków / pasków narzędzi**:
  - `#faf9fb`
  - `#f2f2f7`
- **Obwódki / separatory**:
  - `#ececf2`
  - `#dcdce6`
- **Kartka A4**: `#ffffff`

### Cienie i promienie
- **Kartka A4**:
  - `background: #fff`
  - `box-shadow: 0 2px 10px rgba(30,20,60,.06)`
  - `border-radius: 6px`
- **Cały panel / mockup**:
  - `box-shadow: 0 8px 30px rgba(30,20,60,.12)`
  - `border-radius: 10px`
- **Przyciski toolbaru**: `border-radius: 8px`
- **Badge / pigułki**: `border-radius: 8px`

---

## 2. Układ główny aplikacji

### Shell aplikacji
- Tło całej strony: **jasnoszare `#eeeef3`**.
- Główna ramka aplikacji jest osadzona centralnie i ma wygląd gotowego mockupu produktu.
- Główna struktura:
  1. **Sidebar po lewej**
  2. **Prawa część robocza** z:
     - headerem,
     - subheaderem / toolbar em,
     - obszarem podglądu.

### Panel / mockup
- Wygląda jak pojedynczy kontener UI obejmujący cały widok aplikacji.
- Styl:
  - `border-radius: 10px`
  - `box-shadow: 0 8px 30px rgba(30,20,60,.12)`
- Krawędzie są miękkie, bez agresywnych obramowań.

---

## 3. Sidebar

### Tło i rola
- Sidebar jest pełnowysokościowym pionowym panelem po lewej stronie.
- Tło sidebaru:
  - `linear-gradient(180deg, #4b2d7a, #3d2566)`
- Sidebar **nie ma jednolitego fillu** — bazuje wyłącznie na gradiencie.
- Elementy wewnętrzne sidebaru (nagłówek, sekcje menu, stopka) są **transparentne**, dzięki czemu widać gradient pod spodem.

### Typografia sidebaru
- Główne etykiety menu:
  - rozmiar: **16px**
  - waga:
    - aktywne: **700**
    - nieaktywne: **500–600**
- Teksty w sidebarze:
  - aktywne: `#ffffff`
  - nieaktywne: `rgba(255,255,255,.75)` lub miejscami wizualnie bliżej `.92`

---

## 4. Sidebar — nagłówek z logo

### Układ
- Padding nagłówka z logo: **`22px 20px 18px`**
- Układ poziomy: logo po lewej, tekst po prawej.
- Odstęp logo ↔ tekst: **`12px`**

### Logo
- Rozmiar logo: **40x40px**
- `object-fit: contain`
- Kontener logo:
  - bez dodatkowego tła,
  - bez osobnej pigułki,
  - bez fillu pod spodem,
  - po prostu obraz PNG osadzony bezpośrednio na gradiencie.

### Teksty brandowe
- Nazwa: **EduPlaner 2026**
  - kolor: biały
  - rozmiar: ok. **16px**
  - waga: **700–800**
- Podpis: **PCTP · KOSZALIN**
  - kolor: półtransparentna biel
  - rozmiar: ok. **12px**
  - waga: **600–700**
  - litery wizualnie bardziej techniczne / drobniejsze od tytułu

### Divider pod logo
- Pod nagłówkiem z logo znajduje się cienka linia oddzielająca go od listy menu.
- Styl:
  - `border-bottom: 1px solid rgba(255,255,255,.1)`

---

## 5. Sidebar — sekcje główne menu

### Wygląd sekcji głównych
Przykłady widoczne na ekranie:
- Kartoteka
- Metryczka
- WOPF – ocena funkcjonalna
- IPET – program
- Ewaluacja
- Zespół
- Baza wiedzy
- Druki
- Ustawienia

### Styl elementu głównego
- Tło: **transparent**
- Padding: **`9px 10px`**
- `border-radius: 8px`
- Układ: jedna linia, flex poziomy
- Wyrównanie: ikonka po lewej, label, opcjonalnie strzałka po prawej

### Ikonka sekcji głównej
- Kontener ikonki:
  - `width: 18px`
  - `text-align: center`
  - `font-size: 15px`
  - `opacity: .85`
- Odstęp ikonka → tekst: **10px**
- Ikonka zawsze jest pierwsza, przed labelem.

### Label sekcji głównej
- Font-size: **16px**
- Waga: **600–700**
- Kolor:
  - aktywna / ważniejsza sekcja: `#fff`
  - nieaktywna: `rgba(255,255,255,.75)` do `.92`

### Strzałka rozwijania
- Dotyczy sekcji rozwijalnych, np. **Kartoteka**, **Metryczka**.
- Wyrównana do prawej.
- Optycznie odpychana przez label w układzie flex.
- Styl:
  - `opacity: .6`
  - `font-size: 12px`

---

## 6. Sidebar — podpozycje (children)

### Przykładowe podpozycje widoczne na ekranie
W rozwiniętej sekcji **Metryczka** widać m.in.:
- Metryczka ucznia
- Podstawa prawna
- Arkusz dostępności ucznia
- Warianty organizacyjne
- Wywiad z rodzicem
- Zgłoszenie potrzeby wsparcia
- Zgłoszenie ucznia
- Zgłoszenie rodzica
- Zgoda i klauzula RODO

W sekcji **Kartoteka** widoczna jest m.in. pozycja:
- Kartoteka uczniów

### Styl podpozycji
- Padding: **`8px 12px 8px 38px`**
- Wcięcie od lewej: **38px**
  - podpozycje są wyrównane względem tekstu sekcji nadrzędnej, a nie względem ikonki.
- `border-radius: 8px`
- Odstęp między podpozycjami: **`gap: 1px`**

### Podpozycja aktywna
Przykład: **Metryczka ucznia**
- Tło: `rgba(255,255,255,.14)`
- Tekst: `#fff`
- Font-weight: **700**
- Tło jest delikatne, półtransparentne, bez osobnej ramki.

### Podpozycja nieaktywna
- Tło: `transparent`
- Tekst: `rgba(255,255,255,.75)`
- Font-weight: **500**
- Nadal czytelna, ale wyraźnie mniej dominująca niż aktywna.

---

## 7. Sidebar — stopka użytkownika

### Położenie
- Stopka jest przyklejona do dołu sidebaru.
- Zawiera avatar oraz dane użytkownika.

### Styl stopki
- Tło: **transparent**
- Padding: **`16px 18px`**
- Separator od części menu:
  - `border-top: 1px solid rgba(255,255,255,.1)`
- Jest to symetryczne domknięcie sidebara, analogiczne do dividera pod logo.

### Avatar
- Rozmiar: **34x34px**
- `border-radius: 50%`
- Bez dodatkowego tła pod spodem.
- To po prostu zdjęcie użytkownika przycięte do koła.

### Dane użytkownika
- Imię i nazwisko: **Arkadiusz Pielechowski**
  - kolor: biały
  - rozmiar: ok. **14px**
  - waga: **700**
- Rola: **Programista**
  - kolor: `rgba(255,255,255,.75)`
  - rozmiar: ok. **12px**
  - waga: **500–600**

---

## 8. Header główny

### Funkcja
Header to górny pasek prawej części aplikacji. Zawiera:
- mały label trybu,
- tytuł widoku,
- wyszukiwarkę,
- chip z aktualnie wybraną osobą,
- główny przycisk akcji.

### Tło i obramowanie
- Tło: bardzo jasne, w praktyce zbliżone do `#faf9fb` / bieli
- Dół odcięty delikatnym separatorem w kolorze z grupy:
  - `#ececf2`
  - `#dcdce6`

### Zawartość od lewej do prawej
1. **PODGLĄD**
2. **Metryczka ucznia**
3. Pole wyszukiwania
4. Chip z uczniem
5. Przycisk **Powitanie**

### Label „PODGLĄD"
- Rozmiar: ok. **12px**
- Waga: **700–800**
- Kolor: stonowany szarofioletowy
- Zapis uppercase

### Tytuł „Metryczka ucznia"
- Rozmiar: **16px**
- Waga: **700–800**
- Kolor: ciemny granatowo-fioletowy
- To główny tekst nawigacyjny w headerze.

---

## 9. Wyszukiwarka w headerze

### Styl pola
- Tło: `#f2f2f7`
- Kształt: zaokrąglony prostokąt
- `border-radius: 8px`
- Bez mocnej widocznej ramki
- Ikona lupy po lewej

### Typografia
- Placeholder: **„Szukaj kartoteki ucznia (imię, nazwisko, klasa...)"**
- Rozmiar fontu: **16px**
- Kolor placeholdera: stonowany, jasnoszary / szarofioletowy
- Waga: **500**

### Wysokość
- Optycznie około **34–36px**

---

## 10. Chip wybranego ucznia w headerze

### Zawartość
- Imię i nazwisko: **Magdalena Kowalska**
- Meta: **kl. III A**
- Ikona zamknięcia: **X** po prawej

### Styl
- Tło: `#f2f2f7`
- `border-radius: 8px`
- Układ inline-flex
- Optycznie ta sama wysokość, co pole wyszukiwania i przyciski w headerze.

### Typografia
- Imię i nazwisko:
  - rozmiar: **16px**
  - waga: **700**
  - kolor: ciemny
- Meta „kl. III A":
  - rozmiar: ok. **14px**
  - waga: **600**
  - kolor: bardziej stonowany
- Ikona X:
  - mała,
  - subtelna,
  - kolor szarawy / szarofioletowy

---

## 11. Przycisk główny w headerze — „Powitanie"

### Styl
- Typ: główny CTA
- Tło: `#e0522e`
- Tekst: biały
- `border-radius: 8px`
- Bez mocnego obrysu

### Typografia
- Rozmiar fontu: **16px**
- Waga: **700**

### Wysokość
- Optycznie ok. **34–36px**

---

## 12. Subheader / pasek pod headerem

### Funkcja
Subheader jest drugim poziomem nawigacji i toolbaru. Zawiera:
- nawigację wsteczną / breadcrumb,
- narzędzia kontekstowe,
- kontrolki zoomu,
- akcje na formularzu / podglądzie.

### Tło
- Jasne, lekko odcięte od headera:
  - `#faf9fb`
  - elementy wewnętrzne często osadzone na `#ffffff` lub `#f2f2f7`

### Separator
- Delikatne dolne obramowanie w tonacji:
  - `#ececf2`
  - `#dcdce6`

---

## 13. Breadcrumb / nawigacja w subheaderze

### Widoczne elementy
- `‹ Wróć: Kartoteka`
- separator pionowy
- `Spis druków`

### Styl
- Teksty mają charakter linków.
- Kolor: fiolet / granatowy fiolet spójny z brandingiem.
- Rozmiar fontu: **16px**
- Waga: **600–700**

### Separator pionowy
- Delikatny, cienki, jasny.
- Ma funkcję rozdzielenia sąsiadujących linków.

---

## 14. Kontrolka zoomu / sterowanie widokiem

### Widoczne elementy
- ikona lupy
- `150%`
- druga ikona lupy
- mała ikona odświeżenia / resetu

### Styl
- Układ inline, bez wyraźnego kontenera.
- Rozmiar tekstu: **16px**
- Waga: **700**
- Ikony są małe, lekkie, w kolorystyce niebiesko-fioletowo-szarej.

---

## 15. Przyciski toolbaru

### Widoczne przyciski
- Wczytaj dane
- Wersje (7)
- Wyczyść
- Zapisz kopię
- Drukuj

### Styl ogólny przycisków wtórnych
Dotyczy: **Wczytaj dane**, **Wersje (7)**, **Wyczyść**, **Zapisz kopię**
- Tło: białe lub bardzo jasne
- Obramowanie: cienkie, w kolorze `#ececf2` / `#dcdce6`
- `border-radius: 8px`
- Układ: ikonka po lewej, tekst po prawej
- Bez ciężkich cieni

### Typografia przycisków
- Rozmiar fontu: **16px**
- Waga: **700**
- Tekst ciemny, czytelny

### Ikony w przyciskach
- Małe, osadzone po lewej stronie labela.
- Część ikon ma kolor akcentowy lub neutralny szarofioletowy.
- W przycisku **Wyczyść** ikonka jest bardziej pomarańczowa, co wzmacnia znaczenie akcji.

### Przycisk „Drukuj"
- Typ: wyróżniony CTA na toolbarze
- Tło: `#e0522e`
- Tekst: biały
- Ikona: biała lub bardzo jasna
- `border-radius: 8px`
- Font-size: **16px**
- Font-weight: **700**

---

## 16. Badge / pigułka „Metryczka"

### Styl
- Tło: `#e0522e`
- Tekst: biały
- `border-radius: 8px`
- Kształt krótkiej, zaokrąglonej pigułki

### Typografia
- Rozmiar fontu: ok. **14–16px**
- Waga: **700**

---

## 17. Kartka A4 jako kontener podglądu

> Bez opisywania treści dokumentu — tylko jako element UI.

### Styl kartki
- Tło: `#ffffff`
- `border-radius: 6px`
- `box-shadow: 0 2px 10px rgba(30,20,60,.06)`
- Kartka jest osadzona na jaśniejszym tle całej części roboczej.
- Sprawia wrażenie realistycznego podglądu dokumentu w aplikacji.

### Otoczenie kartki
- Tło wokół kartki: `#eeeef3`
- Dzięki temu kartka mocno odcina się od reszty interfejsu.

---

## 18. Tła poszczególnych elementów sidebaru — podsumowanie

### Cały sidebar
- `linear-gradient(180deg, #4b2d7a, #3d2566)`

### Nagłówek z logo
- `transparent`

### Sekcja główna menu
- `transparent`

### Podpozycja aktywna
- `rgba(255,255,255,.14)`

### Podpozycja nieaktywna
- `transparent`

### Stopka użytkownika
- `transparent`

### Logo w kółku / kontener 40px
- brak tła, sam obrazek PNG

### Avatar autora 34px
- samo zdjęcie, `border-radius: 50%`, bez dodatkowego tła

---

## 19. Szybkie podsumowanie wdrożeniowe

Jeśli przepisać ten widok 1:1 jako konwencję komponentów, to najważniejsze założenia są następujące:

1. **Mulish 16px jako baza UI**.
2. **Sidebar na fioletowym gradiencie** bez dodatkowych teł w sekcjach.
3. **Aktywność zaznaczana półtransparentną bielą `rgba(255,255,255,.14)`**.
4. **Pomarańcz `#e0522e` jako kolor akcji głównej**.
5. **Jasne, miękkie tła `#faf9fb`, `#f2f2f7`, `#eeeef3`** dla części roboczej.
6. **Miękkie promienie**:
   - panel: `10px`
   - kartka: `6px`
   - przyciski / chipy / badge: `8px`
7. **Delikatne obwódki i separatory** zamiast ciężkich ramek.
8. **Całość ma wyglądać nowocześnie, spokojnie i „produktowo"**, bez agresywnego kontrastu poza pomarańczowymi CTA.

---

## 20. Drobne obserwacje dodatkowe ze zrzutu

- Header i subheader są wizualnie **bardzo lekkie**, prawie „papierowe".
- Przyciski są zwarte, ale nie ciasne — mają wygodny klik target.
- Tekst w całym UI jest dość czytelny i raczej **semi-bold / bold** niż ultra-light.
- Sidebar ma klimat „aplikacji produkcyjnej", a nie marketingowej.
- Prawa część aplikacji jest maksymalnie neutralna, żeby fokus był na podglądzie treści.
- Spacing jest spójny: dużo zaokrągleń, miękkich pudełek i czytelnych marginesów.
