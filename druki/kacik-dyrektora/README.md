# Kącik dyrektora · EduPlaner 2026 · PCTP

Druki dla dyrektora szkoły lub placówki, złożone w tym samym stylu co
**Dziennik Wsparcia · domena d2 ICF** (marka PCTP: fiolet `#2D1B69`, pomarańcz
`#E8450A`, Arial, A4, pola z kropkowanymi linijkami, tabele z fioletowym
nagłówkiem, plakietka i belka w nagłówku, stopka z numeracją stron).

## Druk D-1 — Sprawozdanie nauczyciela z pomocy psychologiczno-pedagogicznej

- `Kacik_Dyrektora_Sprawozdanie_Nauczyciela_PPP.html` — źródło do druku i edycji
- `Kacik_Dyrektora_Sprawozdanie_Nauczyciela_PPP.pdf` — wersja gotowa do wydruku (9 stron A4)

Zawartość druku:

Lista kontrolna „co musi zawierać sprawozdanie”, terminy złożenia i wskazówki
redakcyjne są w **panelu aplikacji** na górze pliku HTML — panel nie drukuje się
(`@media print { display:none }`).

| Strona | Sekcje |
|---|---|
| 1 | I. Osoba składająca sprawozdanie i dane (rola, kwalifikacje, formy pomocy, dokumentacja, okres) |
| 2 | § Podstawa prawna · II. Podstawa objęcia uczniów pomocą |
| 3 | III. Realizacja zaleceń z orzeczenia i opinii · IV. Zestawienie uczniów |
| 4 | V. Bilans realizacji godzin · VI. Cele SMART i stopień realizacji (skala 1–5) |
| 5 | VII. Metody, warunki prowadzenia zajęć i dostosowania |
| 6 | VIII. Efekty i ocena efektywności · IX. Trudności, bariery i działania zaradcze |
| 7 | X. Współpraca w realizacji pomocy · XI. Doskonalenie zawodowe i autoewaluacja |
| 8 | XII. Wnioski i rekomendacje · XIII. Załączniki · XIV. Zapoznanie rodziców i podpisy |
| 9 | XV. Ocena sprawozdania · XVI. Decyzja dyrektora · XVII. Wnioski do organizacji pomocy |

**Kto składa sprawozdanie:** każda osoba prowadząca z uczniem zajęcia w ramach
pomocy p-p (ocenia efektywność własnych zajęć); wychowawca klasy dodatkowo
w wersji zbiorczej dla swojej klasy; dla ucznia z orzeczeniem ocena trafia do
WOPFU. Dyrektor nie pisze sprawozdania — przyjmuje je i ocenia (sekcje XV–XVII).

### Wydruk

Otwórz plik HTML w przeglądarce i wybierz **Drukuj → A4 → marginesy: brak →
grafika tła: włączona**. Plik jest samowystarczalny (bez zewnętrznych zasobów).

Ponowne wygenerowanie PDF-a z wiersza poleceń:

```bash
chromium --headless --no-pdf-header-footer \
  --print-to-pdf=Kacik_Dyrektora_Sprawozdanie_Nauczyciela_PPP.pdf \
  Kacik_Dyrektora_Sprawozdanie_Nauczyciela_PPP.html
```

### Podstawa prawna druku

- Prawo oświatowe — art. 68 ust. 1 pkt 2 i 6 (nadzór pedagogiczny dyrektora)
- Rozp. MEN z 9.08.2017 r. o pomocy psychologiczno-pedagogicznej (Dz.U. 2017 poz. 1591, t.j. Dz.U. 2023 poz. 1798) — obowiązek oceny efektywności pomocy
- Rozp. MEN z 9.08.2017 r. o kształceniu specjalnym (Dz.U. 2017 poz. 1578, t.j. Dz.U. 2020 poz. 1309) — okresowa wielospecjalistyczna ocena (WOPFU) min. 2 razy w roku
- Rozp. MEN z 25.08.2017 r. o dokumentacji przebiegu nauczania (Dz.U. 2017 poz. 1646)
- Rozp. MEN z 25.08.2017 r. o nadzorze pedagogicznym (t.j. Dz.U. 2020 poz. 1551)
- Rozp. ME z 2.03.2026 r. o orzeczeniach i opiniach (Dz.U. 2026 poz. 428) — ocena funkcjonalna od 1.09.2026
- RODO (UE) 2016/679
