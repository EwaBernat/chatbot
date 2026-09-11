# Raport Oceny Funkcjonalnej · EduPlaner 2026

Wzór opinii przedszkola/szkoły o funkcjonowaniu dziecka w obszarach ICF, przygotowany
dla rodzica i zespołu orzekającego poradni (Rozp. MEN z 2 marca 2026 r., Dz. U. 2026 poz. 428, § 7 ust. 6–7).

Styl graficzny wg wzoru IPET EduPlaner 2026: biały papier, lawendowe pola `#EFE9F9`, cienkie linie `#D9D0F0`, fiolet `#2D1B69` tylko w akcentach, pomarańczowe plakietki `#E74509`, tytuł wyśrodkowany. A4, czcionka treści min. 12 pt, druk ciągły z numeracją stron w marginesie; ok. 33 stron PDF / 46 stron Word, w tym załącznik „Opinia o funkcjonowaniu dziecka / ucznia” dla poradni: Część I (okładka · metryczka i procedura · narzędzia) oraz Część II (funkcjonowanie w placówce · wyniki liczbowe KPOF/KSzOF w 9 domenach ICF · analiza jakościowa d1–d9 i zalecenia do IPE · wyniki arkuszy ABC, sensorycznego, biopsychospołecznego, mowy i ToM · podjęte działania · zalecenia z poradni: A) rewalidacja, B) pomoc psychologiczno-pedagogiczna z wymiarem godzin, C) pozostałe zalecenia i sposoby realizacji · podpisy). Część II zawiera przykładowe wyniki do nadpisania.

| Plik | Przeznaczenie |
|---|---|
| `Raport_Oceny_Funkcjonalnej.html` | wersja do aplikacji EduPlaner 2026 (ekran + druk A4, responsywna na telefon) |
| `Raport_Oceny_Funkcjonalnej.pdf` | gotowy wydruk / wysyłka dla rodzica |
| `Raport_Oceny_Funkcjonalnej.docx` | wersja edytowalna Word (Arial, nagłówek i stopka z paginacją) |
| `Opinia_dla_poradni.docx` | sama opinia dla zespołu orzekającego (5 stron, czysty druk bez brandowania) – `node generate_raport_docx.js --opinia Opinia_dla_poradni.docx` |
| `raport_data.json` | **jedno źródło treści** sekcji 4–16 (przykładowe dane do nadpisania) |
| `build_html.py` | buduje HTML z `styles.css` + `part1_pages.html` + JSON (`python3 build_html.py`) |
| `generate_raport_docx.js` | generator Worda z tego samego JSON (`npm i docx@9 && node generate_raport_docx.js Raport_Oceny_Funkcjonalnej.docx`) |

PDF powstaje z HTML przez Chromium:

```
chrome --headless --no-pdf-header-footer --print-to-pdf=Raport_Oceny_Funkcjonalnej.pdf Raport_Oceny_Funkcjonalnej.html
```

## Zasady: KPOF / KSzOF i steny

- Przedszkole = **KPOF**, szkoła = **KSzOF**. W HTML sekcja 5 ma przełącznik narzędzia (zapamiętywany w przeglądarce).
- **Steny tylko dla KSzOF (szkoła).** Po wyborze KPOF kolumna „Sten” jest ukryta; w Wordzie zostawia się ją pustą.
- **Średniej nigdy nie opisuje się stenem** – kafelek „Średnia” pokazuje tylko wartość w skali 0–5.
- Analiza jakościowa obejmuje wszystkie 9 domen ICF (d1–d9).

## Struktura (16 sekcji)

Część I: 1 metryczka · 2 obserwacja wstępna · 3 narzędzia. Część II: 4 funkcjonowanie · 5 wyniki liczbowe · 6 arkusze · 7 Mój głos · 8 działania podjęte · 9 analiza 9 domen · 10 decyzja Zespołu o poziomie wsparcia. Część III: 11 dostosowanie programu, organizacji i technologii · 12 zintegrowane działania · 13 zajęcia (rewalidacja, PPP szczegółowo, mapa zaleceń poradni) · 14 dodatkowa osoba · 15 rodzice i poradnia · 16 terminy oceny efektywności i podpisy.

## Opinia dla poradni (załącznik) – wg § 7 ust. 6–7 rozp. ME z 2.03.2026 (Dz. U. 2026 poz. 428)

1 data wydania i dane dziecka · 2 podstawa opinii (obserwacje i działania diagnostyczne w placówce) · 3 informacja o funkcjonowaniu – trudności, mocne strony, uzdolnienia w obszarach ICF (A przedszkole 5, B uczeń 7) · 4 trudności w realizacji programu · 5 załączniki (WOPF / okresowa ocena) · 6 działania, formy i zakres pomocy, okres, efekty · 7 wnioski do dalszej pracy · 8 fakultatywnie: informacje dla oceny zespołu (§ 8: funkcje ciała, bariery i ułatwienia, głos dziecka i rodziców, stanowisko placówki) · 9 podpisy i potwierdzenie kopii dla rodziców. Nagłówki bez reklamy – tylko nazwa placówki.
