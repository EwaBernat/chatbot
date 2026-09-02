> ⚠️ **Materiał wejściowy, nie strażnik — i nie jest kompletny (sprawdzone 2026-09-02).**
> Spis treści zapowiada 12 rozdziałów; dostarczony tekst urywa się na pierwszym zdaniu
> rozdziału 3 („Hierarchia przepływu danych"). Rozdziały 3–12 trzeba dosłać.
> Wartości i podstawy prawne z tego pliku wchodzą do `straznik-prawo` dopiero po weryfikacji
> w rejestrze `rejestr-przepisow.json`; w razie konfliktu rozstrzyga rejestr.

# EDUPLANER 2026 – KOMPENDIUM PRAWNO-MERYTORYCZNE I ARCHITEKTURA AGENTA AUDYTUJĄCEGO DOKUMENTACJĘ SZKOLNĄ I PRZEDSZKOLNĄ

## SPIS TREŚCI
1. Systemowe Ramy Prawne i Zasady Ogólne (RODO, Dane Medyczne, SOM, Bezpieczeństwo, Kwalifikacje)
2. Taryfikator i Prawne Normy Godzinowe Zajęć Rewalidacyjnych (Szkoły Ogólnodostępne, Integracyjne, Specjalne, SOSW, Przedszkola)
3. Hierarchia Przepływu Danych i Cykl Życia Dokumentacji w Placówce
4. Moduł I: Kartoteka Ucznia
5. Moduł II: Metryczka i Audyt Dokumentacji Wstępnej
6. Moduł III: Wielospecjalistyczna Ocena Poziomu Funkcjonowania (WOPF / WOPFU)
7. Moduł IV: Indywidualny Program Edukacyjno-Terapeutyczny (IPE)
8. Moduł V: Realizacja (Dzienniki, Zajęcia Rewalidacyjne i PPP, BHP i Atesty)
9. Moduł VI: Okresowa i Końcowa Ewaluacja (WOPF Okresowy, Modyfikacja IPE / Aneksy)
10. Moduł VII: Zespół ds. Kształcenia Specjalnego i Procedury Współpracy z Rodzicami (KPA / KRO)
11. Moduł VIII: Baza Wiedzy, Archiwizacja i Likwidacja Placówki
12. Matryca Blokad i Reguł Walidacji dla Strażnika Prawnego (Agenta Audytującego)

---

## 1. SYSTEMOWE RAMY PRAWNE I ZASADY OGÓLNE

Wszystkie procedury, formularze, widoki interfejsu oraz druki generowane przez system **EduPlaner 2026** muszą bezwzględnie odpowiadać powszechnie obowiązującym przepisom prawa rangi ustawowej i rozporządzeniowej.

### 1.1. Ochrona Danych Osobowych (RODO) i Zasada Minimalizacji
* **Podstawa prawna:**
  * **Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO)** – art. 5 ust. 1 lit. c (zasada minimalizacji danych), art. 6 ust. 1 lit. c i e (obowiązek prawny i realizacja zadań w interesie publicznym).
  * **Ustawa z dnia 10 maja 2018 r. o ochronie danych osobowych** (t.j. Dz.U. z 2019 r. poz. 1781).
  * **Ustawa z dnia 14 grudnia 2016 r. – Prawo oświatowe** (t.j. Dz.U. z 2024 r. poz. 737 z późn. zm.) – art. 10 ust. 1 pkt 1, art. 68 ust. 1 pkt 6.
* **Rygor systemowy i blokady:**
  * Dane osobowe są przetwarzane wyłącznie w zakresie niezbędnym do realizacji celów dydaktycznych, wychowawczych i opiekuńczych.
  * **Bezwzględna blokada numeru PESEL oraz dokładnego adresu zamieszkania na wydrukach i szablonach roboczych** (WOPF, IPE, karty obserwacji, arkusze rewalidacyjne, dzienniki robocze). Identyfikacja ucznia w bieżącej dokumentacji pedagogicznej odbywa się wyłącznie na podstawie: **imienia (imion), nazwiska, daty urodzenia oraz oznaczenia klasy/oddziału**.

### 1.2. Przetwarzanie Danych Medycznych i Chorób Przewlekłych
* **Podstawa prawna:**
  * **RODO** – art. 9 ust. 2 lit. a, b, h (przetwarzanie danych szczególnej kategorii: stan zdrowia, leki).
  * **Ustawa z dnia 12 kwietnia 2019 r. o opiece zdrowotnej nad uczniami** (Dz.U. z 2019 r. poz. 1078) – art. 7 (zbieranie informacji o stanie zdrowia za zgodą rodziców), art. 20–21 (warunki sprawowania opieki nad dziećmi przewlekle chorymi).
  * **Ustawa – Prawo oświatowe** – art. 68 ust. 1 pkt 6 w zw. z art. 10 ust. 1 pkt 1 (zapewnienie bezpiecznych i higienicznych warunków).
  * **Wspólne stanowisko MZ i MEN** w sprawie procedur sprawowania opieki nad uczniami przewlekle chorymi i podawania leków w placówkach oświatowych.
* **Rygor systemowy i blokady:**
  * Informacje o chorobach przewlekłych (astma, cukrzyca, epilepsja, hemofilia, alergie zagrażające życiu) oraz o stale przyjmowanych lekach (w tym preparatach psychotropowych) zbierane są **wyłącznie za dobrowolną, pisemną zgodą rodziców/opiekunów prawnych**.
  * Podawanie leków w placówce wymaga: pisemnego wniosku rodzica, zlecenia/zaświadczenia lekarskiego oraz pisemnej zgody pracownika przyjmującego to zadanie.
  * **Separacja uprawnień:** Karta medyczno-interwencyjna stanowi odrębny zbiór danych. Dostęp do niej posiadają wyłącznie: wychowawca, wyznaczeni nauczyciele/terapeuci oraz osoba przeszkolona w zakresie udzielania pierwszej pomocy. Informacje medyczne nie mogą być automatycznie scalane ani kopiowane do ogólnodostępnych druków WOPF/IPE.

### 1.3. Ochrona Małoletnich, Ustawa Kamilkowa i Procedura „Niebieskiej Karty”
* **Podstawa prawna:**
  * **Ustawa z dnia 28 lipca 2023 r. o zmianie ustawy – Kodeks rodzinny i opiekuńczy oraz niektórych innych ustaw (tzw. Ustawa Kamilkowa)** (Dz.U. z 2023 r. poz. 1606).
  * **Ustawa z dnia 13 maja 2016 r. o przeciwdziałaniu zagrożeniom przestępczością na tle seksualnym i ochronie małoletnich** (t.j. Dz.U. z 2024 r. poz. 560) – art. 22b i 22c (Standardy Ochrony Małoletnich – SOM).
  * **Ustawa z dnia 29 lipca 2005 r. o przeciwdziałaniu przemocy domowej** (t.j. Dz.U. z 2024 r. poz. 424 z późn. zm.).
  * **Rozporządzenie Rady Ministrów z dnia 6 września 2023 r. w sprawie procedury „Niebieskie Karty” oraz wzorów formularzy „Niebieska Karta”** (Dz.U. z 2023 r. poz. 1870).
* **Rygor systemowy i blokady:**
  * **Standardy Ochrony Małoletnich (SOM):** Wdrożenie procedur bezpiecznych relacji personel–dziecko oraz zasad interwencji.
  * **Weryfikacja personelu:** Obowiązkowe odnotowanie sprawdzenia w **Rejestrze Sprawców Przestępstw na Tle Seksualnym (RSPTS)** oraz pobrania zaświadczenia z **Krajowego Rejestru Karnego (KRK)** przed dopuszczeniem pracownika do pracy z dziećmi.
  * **Procedura Niebieskiej Karty:** Wszczęcie procedury następuje przez wypełnienie formularza **NK-A** i przekazanie go do właściwego Zespołu Interdyscyplinarnego w nieprzekraczalnym terminie **do 5 dni roboczych**. Formularze NK podlegają ścisłej poufności i nie mogą być łączone z teczką pomocową ucznia.

### 1.4. Trudne Zachowania Behawioralne i Podstawy Prawne Wobec Rodziców
* **Podstawa prawna:**
  * **Ustawa z dnia 25 lutego 1964 r. – Kodeks rodzinny i opiekuńczy (KRO)** (t.j. Dz.U. z 2023 r. poz. 2809 z późn. zm.) – art. 95 § 1, art. 96, art. 109.
  * **Ustawa z dnia 9 czerwca 2022 r. o wspieraniu i resocjalizacji nieletnich** (Dz.U. z 2022 r. poz. 1700 z późn. zm.) – art. 4, art. 5.
  * **Ustawa z dnia 14 czerwca 1960 r. – Kodeks postępowania administracyjnego (KPA)** (t.j. Dz.U. z 2024 r. poz. 572) – art. 39–44.
* **Rygor systemowy i ścieżka procedowania:**
  * **Notatka faktograficzna:** Obowiązek sporządzenia notatki opartej na faktach (data, godzina, miejsce, opis zachowania bez ocen subiektywnych, podjęte środki bezpieczeństwa, świadkowie).
  * **Ścieżka eskalacji:** Działania wewnątrzszkolne $\rightarrow$ wezwanie rodziców (ZPO / tryb KPA) $\rightarrow$ w razie braku współpracy i bezpośredniego zagrożenia dobra dziecka – wniosek dyrektora do Sądu Rejonowego (Wydział Rodzinny i Nieletnich) w trybie **art. 109 KRO** (wgląd w sytuację rodziny).

### 1.5. Bezpieczeństwo Lokalowe, Sanepid, BHP i Kwalifikacje Kadry
* **Podstawa prawna:**
  * **Rozporządzenie MENiS z dnia 31 grudnia 2002 r. w sprawie bezpieczeństwa i higieny w publicznych i niepublicznych szkołach i placówkach** (t.j. Dz.U. z 2020 r. poz. 1604 z późn. zm.).
  * **Rozporządzenie MEiN z dnia 14 września 2023 r. w sprawie szczegółowych kwalifikacji wymaganych od nauczycieli** (Dz.U. z 2023 r. poz. 2102).
  * Normy bezpieczeństwa: **PN-EN 1729-1/2:2016** (meble i stanowiska uczniowskie), **PN-EN 71** i **CE** (bezpieczeństwo zabawek i pomocy dydaktycznych), **PN-EN 1176/1177** (place zabaw).
* **Rygor systemowy:**
  * Kontrola parametrów lokalu: powierzchnia min. **2,5 m² na dziecko** w przedszkolu, temperatura w salach min. **18°C**, atestowane wyposażenie.
  * Obowiązkowe szkolenie z zakresu udzielania pierwszej pomocy dla wszystkich pracowników pedagogicznych (§ 21 rozporządzenia BHP).
  * Weryfikacja kwalifikacji: blokada możliwości przypisania nauczyciela/terapeuty do zajęć rewalidacyjnych lub PPP bez zarejestrowanych w systemie uprawnień kierunkowych (np. oligofrenopedagogika, autyzm, terapia pedagogiczna, logopedia).

---

## 2. TARYFIKATOR I PRAWNE NORMY GODZINOWE ZAJĘĆ REWALIDACYJNYCH

Wymiar godzin zajęć rewalidacyjnych dla uczniów z orzeczeniem o potrzebie kształcenia specjalnego wynika bezpośrednio z przepisów ramowych planów nauczania oraz rozporządzenia o kształceniu specjalnym.

### 2.1. Podstawy Prawne Taryfikatora
* **Rozporządzenie MEN z dnia 3 kwietnia 2019 r. w sprawie ramowych planów nauczania dla publicznych szkół** (t.j. Dz.U. z 2024 r. poz. 815 z późn. zm.).
* **Rozporządzenie MEN z dnia 9 sierpnia 2017 r. w sprawie warunków organizowania kształcenia, wychowania i opieki dla dzieci i młodzieży niepełnosprawnych, niedostosowanych społecznie i zagrożonych niedostosowaniem społecznym** (t.j. Dz.U. z 2020 r. poz. 1309 z późn. zm.).

### 2.2. Ustawowa Tabela Przydziału Godzin Rewalidacji w EduPlaner 2026

| Typ placówki i forma oddziału | Podstawa prawna z ramowego planu | Tygodniowy wymiar godzin rewalidacji | Sposób naliczania i przydziału |
| :--- | :--- | :--- | :--- |
| **Szkoła Ogólnodostępna** (dla każdego ucznia z orzeczeniem) | Załączniki nr 1–7 do Dz.U. z 2024 r. poz. 815 | **2 godziny tygodniowo** | **Indywidualnie na każdego ucznia** |
| **Oddział Integracyjny w szkole ogólnodostępnej** | Załączniki nr 1–7 do Dz.U. z 2024 r. poz. 815 | **2 godziny tygodniowo** | **Indywidualnie na każdego ucznia** |
| **Szkoła Specjalna / Oddział Specjalny** (uczniowie niewidomi, słabowidzący, niesłyszący, słabosłyszący, z autyzmem w tym z Zespołem Aspergera, z niepełnosprawnością ruchową, z niepełnosprawnościami sprzężonymi) | Załączniki dla szkół podstawowych specjalnych do Dz.U. z 2024 r. poz. 815 | **12 godzin tygodniowo** | **Pula na cały oddział** (do podziału na grupy lub zajęcia indywidualne) |
| **Szkoła Specjalna / Oddział Specjalny** (uczniowie z niepełnosprawnością intelektualną w stopniu umiarkowanym lub znacznym) | Załącznik dla SP specjalnej do Dz.U. z 2024 r. poz. 815 | **10 godzin tygodniowo** | **Pula na cały oddział** |
| **Szkoła Specjalna Przysposabiająca do Pracy** | Załącznik do ramowego planu nauczania dla szkoły przysposabiającej | **10 godzin tygodniowo** | **Pula na cały oddział** |
| **Branżowa Szkoła Specjalna / Technikum Specjalne** | Załączniki dla ponadpodstawowych szkół specjalnych | **12 godzin tygodniowo** | **Pula na cały oddział** |
| **Przedszkole** (ogólnodostępne, integracyjne, specjalne) | Rozporządzenie MEN z 9 sierpnia 2017 r. (Dz.U. z 2020 r. poz. 1309) | Wymiar ustala organ prowadzący w arkuszu organizacji przedszkola | Zgodnie z zaleceniami orzeczenia i arkuszem organizacji |

### 2.3. Logika Algorytmu Agenta ds. Rewalidacji:
1. Pobranie z Metryczki: **Typ placówki**, **Rodzaj oddziału** oraz **Diagnoza orzeczenia**.
2. W oddziałach **ogólnodostępnych i integracyjnych**: agent wymusza przypisanie minimum **2h/tydzień** dla danego ucznia (brak tej wartości blokuje zatwierdzenie IPE).
3. W oddziałach **specjalnych**: agent kontroluje sumaryczną pulę oddziału (**10h** lub **12h** tygodniowo) oraz weryfikuje podział tych godzin pomiędzy uczniów w planie pracy rewalidacyjnej oddziału.

---

## 3. HIERARCHIA PRZEPŁYWU DANYCH I CYKL ŻYCIA DOKUMENTACJI

System EduPlaner 2026 realizuje ścisły, sekwencyjny obieg danych: