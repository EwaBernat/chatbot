# Druk FBA-C — cele SMART do obserwacji pogłębionej

Ciąg dalszy karty **ABC / FBA** (analiza funkcjonalna zachowania i pozytywne
wsparcie — PBS). Tamta kończy się pięcioma celami SMART, po jednym na funkcję
zachowania. Wyznaczają kierunek planu, ale na obserwację pogłębioną są za
szerokie: „skorzysta z ustalonej strategii wyciszenia” nie mówi, w której
z pięciu sytuacji napięcia liczymy postęp.

Ten druk rozpisuje tamte pięć celów na **25 celów szczegółowych** — po jednym
do każdego wskaźnika kwestionariusza funkcji. Każdy ma zachowanie, które widać,
liczbę, którą da się policzyć, i termin, w którym sprawdzamy. Osiem stron A4
pionowo: wprowadzenie · pięć stron z kartami celów · dwie strony tabeli ewaluacji.

## Składanie dokumentu

```bash
# formularz bez nazwiska (to jest wersja w repozytorium)
python3 src/build_cele_fba.py

# pod konkretnego ucznia — punktacja pięciu funkcji z kwestionariusza
python3 src/build_cele_fba.py --uczen "Imię Nazwisko" --klasa "III A" \
    --wyniki 7,8,13,7,13

# pomiar: czy każda strona mieści się na jednej kartce A4
node src/zmierz_strony.mjs Cele_SMART_FBA_obserwacja_poglebiona.html
```

Dokumenty z nazwiskiem nie wchodzą do repozytorium (`.gitignore`) — noszą dane
osobowe ucznia. Zostaje sam formularz.

## Druk FBA-T — tabela wiek × poziom wsparcia

Ten sam materiał ułożony tak, jak układa go bank celów SMART KPOF: zakładki
wersji wiekowych, wiersz na wskaźnik, trzy kolumny poziomów wsparcia.
**225 celów** (25 wskaźników × 3 poziomy × 3 wersje) — nauczyciel wybiera
komórkę, zamiast przepisywać cel pod dziecko.

```bash
python3 src/build_tabela.py     # Tabela_celow_FBA_wiek_poziom.html
node src/do_pdf.mjs             # oba druki do PDF: FBA-C pionowo, FBA-T poziomo
```

| wersja | wiek | czym się różni |
|---|---|---|
| A | 3–4 lata | symbol podany do ręki, krótkie czasy, proste zachowanie |
| B | 5 lat | karta na stoliku plus słowo, czasy średnie |
| C | 6 lat | słowo zamiast karty, nazywanie własnego stanu, planowanie |

Poziom wsparcia zmienia **warunki zadania**, nie funkcję zachowania: Poziom III —
podpora dorosłego, 3 z 5 sytuacji, 4 tygodnie; Poziom II — pomoc w zasięgu,
4 z 5, 8 tygodni; Poziom I — bez pomocy przedmiotowej i z trudniejszym
zachowaniem, 4 z 5, 12 tygodni. Kryterium na Poziomie I nie rośnie do 5 z 5:
„za każdym razem” to w przedszkolu cel nie do osiągnięcia i psuje ewaluację,
zamiast ją domykać.

Tabela drukuje się **poziomo** i drukuje się ta wersja wiekowa, która jest
otwarta — tak jak bank. Pas z nazwą wersji siedzi w `thead`, więc powtarza się
na każdej kartce; bez niego druga i trzecia strona nie mówiły, czyj to rocznik.

## Skąd kryterium i horyzont

Nie z podręcznika, tylko z punktacji funkcji u tego ucznia — tak samo jak
w banku celów SMART horyzont wynika z poziomu wsparcia:

| punktacja | ocena | kryterium | horyzont |
|---|---|---|---|
| 10–15 | dominująca | 8 z 10 sytuacji | 4 tygodnie |
| 5–9 | istotna | 7 z 10 sytuacji | 8 tygodni |
| 0–4 | słaba | 6 z 10 sytuacji | 12 tygodni |

Funkcja dominująca dostaje najkrótszy horyzont nie dlatego, że jest łatwiejsza,
tylko dlatego, że jest priorytetem planu — sprawdzamy ją najczęściej.

Horyzont trzymamy w trzech formach gramatycznych (`4 tygodni` · `4 tygodniach`
· `4 tygodnie`), bo wchodzi w trzy różne zdania. Jedna forma dawała
„weryfikacja po 4 tygodni” w druku, który idzie do rodzica.

## Co gdzie leży

```
src/dane_fba.py         25 celów SMART do obserwacji pogłębionej (druk FBA-C)
src/dane_poziomy.py     225 celów: wiek × poziom wsparcia (druk FBA-T)
src/build_cele_fba.py   składanie druku FBA-C
src/build_tabela.py     składanie druku FBA-T
src/zmierz_strony.mjs   pomiar, czy strony mieszczą się na A4
src/do_pdf.mjs          wydruk obu druków do PDF
```

Cele mówią o **zachowaniu zastępczym** — pełniącym tę samą funkcję co zachowanie
trudne, tylko akceptowalnym. Nie odbieramy uczniowi funkcji (ucieczki, uwagi,
regulacji), uczymy innej drogi do niej. To odróżnia plan PBS od karania reakcji
i o to samo trzeba dbać przy każdym dopisywanym celu.
