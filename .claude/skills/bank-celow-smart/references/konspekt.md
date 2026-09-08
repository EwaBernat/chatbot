# Konspekt zajęć — struktura i wzór

Konspekt to druk **KC-3**: jedna karta A4, ta sama dla wszystkich 178 scenariuszy.
Nauczyciel czyta je seriami, więc identyczna kolejność sekcji jest tu ważniejsza
niż pomysłowość układu — oko wie, gdzie szukać przebiegu, nie czytając nagłówków.

## Gdzie dopisać

Moduł na wersję i obszar: `src/konspekty_<wersja>_d<obszar>.py`, np.
`konspekty_5_d3.py` to wersja B (5 lat), obszar III. Klucz w słowniku to para
`(kod_wersji, numer_twierdzenia)` — ta sama para wiąże konspekt z celem w banku,
kartą pomocy i arkuszem do wydruku. Literówka w kluczu nie wysypuje budowania,
tylko cicho gubi konspekt; `sprawdz_bank.py` to wyłapuje.

Numer konspektu (`nr`) ma postać `<litera><obszar>-<numer>`: `D1-01` dla wersji A
(historyczne „D”), `B1-01`, `C7-32`, `U6-30`.

## Wzór

```python
 ("B", 12): dict(
  nr="B3-12", tytul="Kronika dnia",
  podtytul="Opowiadanie o tym, co się wydarzyło, w kolejności zdarzeń",
  sfera="III POROZUMIEWANIE SIĘ · Opowiadanie (ICF d330–d335 · PP 3.7·3.9)",
  czas="20 min", forma="mała grupa (4–6 dzieci)", cykl="3× w tygodniu",
  ter="Dziecko opowie trzy zdarzenia z dnia w kolejności, korzystając z kart "
      "planu dnia, w 3 z 5 prób, w ciągu 8 tygodni.",
  ter_smart=[
    ("S", "Opowiada zdarzenia w kolejności: najpierw, potem, na końcu."),
    ("M", "3 zdarzenia; 3 z 5 prób."),
    ("A", "Karty planu dnia zdejmują z dziecka pamiętanie kolejności."),
    ("R", "Opowiadanie o przeszłości to podstawa relacji z wydarzeń w szkole."),
    ("T", "Weryfikacja po 8 tygodniach."),
  ],
  ter_kryt="Rejestr wypowiedzi · 5 prób w tygodniu.",
  pomoce=["karty planu dnia", "kronika grupy — zeszyt formatu A3", "…"],
  metody=["opowiadanie z podporą obrazkową", "pytania o kolejność", "…"],
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne",
  przebieg=[
    ("N — rozkłada karty planu dnia w kolejności.", "D — wskazuje, co było pierwsze."),
    ("N — pyta: „co robiliśmy potem?”.", "D — opowiada drugie zdarzenie."),
    # 5 kroków to dobra długość: mieści się na stronie i wystarcza na 20 minut
  ],
  mod3=["dwa zdarzenia zamiast trzech", "opowiadanie przez wskazanie karty"],
  mod2=["trzy zdarzenia po podpowiedzi pierwszego słowa"],
  mod1=["cztery zdarzenia z uzasadnieniem „bo”", "opowiedzenie bez kart"],
  wskazowka="Nie poprawiaj kolejności w trakcie — zapisz, co powiedziało, "
            "i wróć do tego z kartami po opowiadaniu."),
```

## Jak pisać cel terapeutyczny

Cel edukacyjny bierze się z banku (jest już napisany, przy każdym poziomie
wsparcia). Ty piszesz **cel terapeutyczny**: co dziecko zrobi, w ilu próbach,
w jakim czasie. Jedno zdanie, obserwowalne zachowanie, liczba i horyzont.

* **dobrze:** „Poczeka na swoją kolej 2 minuty w zabawie z regułą, korzystając
  z wizualnej kolejki — w 3 z 5 sytuacji, w ciągu 8 tygodni.”
* **źle:** „Poprawa umiejętności czekania na swoją kolej.” — nie da się tego
  zaobserwować ani policzyć, więc nie da się z tego zrobić ewaluacji.

Horyzont wynika z poziomu wsparcia: Poziom III — 4 tygodnie, II — 8 tygodni,
I — 12 tygodni. Rozpisanie SMART (`ter_smart`) tłumaczy każdą literę na to
konkretne zadanie, a nie na definicję z podręcznika.

## Przebieg

Pary „czynność nauczyciela (N) / oczekiwana reakcja dziecka (D)”. Pisz je jako
konkretne czynności, nie jako cele: **„N — uderza w bębenek i podaje polecenie”**,
nie „N — wprowadza sygnał dźwiękowy”. Nauczyciel ma to wykonać, nie zinterpretować.

Pięć kroków to sprawdzona długość. Przy siedmiu konspekt zaczyna wychodzić poza
stronę — sprawdź wtedy pomiarem (`zmierz_a4.mjs`).

## Modyfikacje

Trzy listy, po jednej na poziom: `mod3` (czerwona — brak progresu), `mod2` (żółta),
`mod1` (zielona — rozszerzenie przy pełnym sukcesie). Modyfikacja ma zmieniać
**warunki zadania**, nie cel: mniej elementów, dłuższy czas, podpowiedź, inna
forma odpowiedzi. Cel zostaje ten sam, bo to on jest wpisany w IPET.

## Po dopisaniu

Konspekt bez materiału do wydruku jest niekompletny — każdy z istniejących 178 ma
przynajmniej jeden arkusz. Jeśli dopisujesz konspekt, dopisz też arkusz
(`references/arkusze.md`), a gdy konspekt opiera się na konkretnym przedmiocie —
także kartę pomocy (`references/pomoce.md`).
