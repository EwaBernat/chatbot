# Cele SMART do wskaźników FBA

Dwa druki, jedna treść w dwóch układach. **Nie da się dopisać celu tylko do
jednego** — nauczycielka czyta oba i rozjazd między nimi jest gorszy niż brak.

## Skąd się biorą wskaźniki

Kwestionariusz funkcji zachowania ma pięć funkcji po pięć wskaźników. Numeracja
jest **per funkcja**: `I.1`–`I.5`, `II.1`–`II.5`, aż do `V.5`. To 25 wskaźników.

| nr | funkcja | co dziecko tym załatwia |
|---|---|---|
| I | Ucieczka / unikanie | wyjście z trudnego lub nielubianego zadania |
| II | Sensoryczne / autostymulacja | regulację pobudzenia, bodziec, którego brakuje |
| III | Uwaga dorosłego | kontakt, spojrzenie, obecność |
| IV | Dostęp do rzeczy | przedmiot, aktywność, przywilej |
| V | Regulacja / zmiana | przewidywalność, wyjście z przeciążenia |

Funkcja to **nie** ocena dziecka, tylko odpowiedź na pytanie „po co". Cel uczy
innej drogi do tej samej odpowiedzi.

## Druk FBA-C — obserwacja pogłębiona

`src/dane_fba.py`, składanie `src/build_cele_fba.py`. Osiem stron A4 pionowo:
jedna strona na funkcję, potem tabela ewaluacji rozbita na dwie kartki.

Struktura danych: `FUNKCJE[rzym]` niesie nazwę funkcji i pięć wskaźników, każdy
z celem rozpisanym na SMART. `PROGI` to krotki `(prog, nazwa, proba, dop, msc,
mian, opis)`, a `ocena(wynik)` zwraca komplet pól dla danej punktacji.

Trzy formy gramatyczne horyzontu (`dop` „4 tygodni", `msc` „4 tygodniach",
`mian` „4 tygodnie") nie są nadmiarem — wchodzą w trzy różne zdania druku. Jedna
forma dawała „weryfikacja po 4 tygodni" w dokumencie dla rodzica.

Strony funkcji i tabela ewaluacji były kiedyś za wysokie (1146–1584 px przy
budżecie 1054). Zagęszczenie typograficzne i podział ewaluacji na dwie kartki to
rozwiązanie, które przeszło pomiar — nie cofaj go, dopisując „luźniejszy" układ.

## Druk FBA-T — wiek × poziom wsparcia

`src/dane_poziomy.py`, składanie `src/build_tabela.py`. Ten sam układ co bank
KPOF: zakładki wersji wiekowych, wiersz na wskaźnik, trzy kolumny poziomów.

```python
CELE["I"]["wskazniki"][0] = {
    "wskaznik": "Zachowanie pojawia się, gdy dziecko ma wykonać trudne zadanie.",
    "zastepcze": "rozpoczęcie zadania",
    "A": ("cel dla Poziomu III", "cel dla Poziomu II", "cel dla Poziomu I"),
    "B": (...), "C": (...),
}
```

Kolejność kolumn zostaje **III, II, I** — od największego wsparcia do
najmniejszego, tak jak w banku. Nauczyciel czyta oba dokumenty tym samym ruchem
oka: w dół do swojego wskaźnika, w bok do swojego poziomu.

Poziom zmienia **warunki zadania, nie funkcję**. Na każdym poziomie dziecko uczy
się tej samej drogi do tej samej potrzeby, tylko z inną ilością podpory. Cel,
który na Poziomie I załatwia inną potrzebę niż na III, jest błędem, nie
progresją.

`zastepcze` to jedno–trzy słowa nazywające zachowanie zastępcze wiersza. Wchodzi
do tabeli, do wykazu konspektów i do edytora własnych konspektów jako podpowiedź.

## Kolor

Kolor poziomów (czerwony · żółty · zielony) jest **tylko w legendzie na górze**.
W samej tabeli koloru nie ma: 75 kolorowych komórek przestaje cokolwiek
wyróżniać. Jeśli prosi o „więcej koloru", zaproponuj wyróżnienie jednego wiersza
albo jednej kolumny, nie pomalowanie tabeli.

## Po zmianie treści

```bash
python3 src/build_tabela.py && python3 src/build_cele_fba.py
python3 ../.claude/skills/cele-fba-pbs/scripts/sprawdz_fba.py
```

Cel edukacyjny konspektów i edytora czyta się **na żywo z tabeli**, nie z kopii —
poprawka w `dane_poziomy.py` przechodzi do konspektów sama. Nie dopisuj celu
drugi raz do modułu konspektów; to właśnie ta kopia rozjeżdżała się z bankiem.
