# PWES — Plan Wsparcia Edukacyjnego

Dokument wynikowy **ścieżki B** (uczeń **bez orzeczenia** o potrzebie
kształcenia specjalnego) — odpowiednik IPET dla ścieżki A. Dotąd istniał
tylko jako nazwa/pole wyboru wewnątrz trzech druków WOPF (`WOPF_SP_arkusz_zespolowy`,
`WOPF_SP_bez_poglebionej`, `WOPF_karta_oceny`), z zastrzeżeniem wprost w
tekście: „Nie oznaczaj tej ścieżki jako formalnej WOPFU ani IPET" — czyli
żaden z tych druków nie jest, ani nie miał być, samym PWES. Ten folder
dodaje brakujący, samodzielny dokument.

## Dlaczego to inny dokument niż WOPF-SP

WOPF-SP (i jego 9-obszarowy aparat KSzOF/ICF/sten) to narzędzie dla ścieżki A
— wymóg wynika z § 6 rozporządzenia o kształceniu specjalnym (Dz.U. 2020
poz. 1309), które dotyczy wyłącznie uczniów **z orzeczeniem**. Dla ucznia
**bez orzeczenia** korzystającego z pomocy psychologiczno-pedagogicznej
obowiązuje inny, lżejszy przepis — rozporządzenie o zasadach organizacji i
udzielania pomocy psychologiczno-pedagogicznej (Dz.U. 2017 poz. 1591; tekst
jednolity: Dz.U. 2023 poz. 1798) — które nie wymaga pełnej wielospecjalistycznej
oceny w 9 obszarach, tylko: rozpoznania indywidualnych potrzeb, ustalonych
form/wymiaru/okresu pomocy, poinformowania rodziców i okresowej oceny
efektywności. Dlatego PWES **celowo nie ma** KSzOF, sten, kart obszarów ani
sekcji rewalidacji (rewalidacja jest zarezerwowana dla ścieżki A) — to nie
skrót WOPF-SP, tylko osobny dokument dopasowany do innej podstawy prawnej.

## Struktura (4 strony)

1. **Dane ucznia i podstawa objęcia pomocą** — kto zgłosił potrzebę, powód
   (pełny katalog z rozporządzenia: trudności w uczeniu się/specyficzne,
   zaburzenia zachowania, uzdolnienia, choroba przewlekła, sytuacja
   kryzysowa, zaniedbania środowiskowe, trudności adaptacyjne, deficyty
   językowe...), rodzaj oceny, współpraca z poradnią.
2. **Zespół**, **rozpoznanie potrzeb** (mocne strony / trudności, źródła
   rozpoznania) i **wpływ trudności na funkcjonowanie** — w tym mała
   tabelka „Napotykane trudności w zakresie włączenia ucznia w zajęcia
   realizowane wspólnie z oddziałem szkolnym oraz efekty działań" (ten
   sam element, który jest w WOPF-SP).
3. **Ustalone formy pomocy pp** (11 kategorii z rozporządzenia, bez
   rewalidacji) z tabelą prowadzący/wymiar/okres i notą o limitach
   liczebności grup, **dostosowania metod pracy** i **cele planu
   wsparcia**.
4. **Informowanie rodziców**, **ocena efektywności i decyzja zespołu**
   (kontynuacja / modyfikacja / zakończenie / skierowanie do poradni z
   możliwością przejścia na ścieżkę A), podpisy, podstawa prawna, RODO.

Ta sama marka PCTP (fiolet `#2D1B69` + pomarańcz `#E8450A`, Mulish/Lora,
`.page`/`.phead`/`.pmeta`/`.pbody`/`.pfoot`, wspólny `base_css.html`) co
cała rodzina WOPF — inna treść, ten sam system wizualny.

## Gęstość stron

Pierwsza wersja miała 7 stron ze 185–645px pustego miejsca na stronę —
za dużo jak na ilość treści (rozpoznanie merytoryczne dla ścieżki B jest z
natury krótsze niż pełne WOPFU). Scalona do **4 stron**, 46–185px marginesu
— gęsto wypełnione, bez przelewania.

Zweryfikowane: programowy pomiar marginesu na każdej stronie (wszystkie
dodatnie), skan poziomego przelewania (0 elementów), edytowalność pól
sprawdzona programowo.

## Odtworzenie PDF

Źródło: generator Python (`build_pwes.py`, poza repozytorium — w
scratchpadzie sesji), analogiczny do `WOPF/` — reużywa te same funkcje
pomocnicze (`page`, `sec_header`, `checkbox_grid`, `ttable`, `note_p`...) i
ten sam `base_css.html`. PDF renderowany przez headless Chromium
(Playwright `page.pdf()`, A4).
