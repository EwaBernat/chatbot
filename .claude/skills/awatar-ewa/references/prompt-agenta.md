# Prompt do Video Agenta HeyGen

Video Agent dostaje jedno polecenie i sam podejmuje wszystkie decyzje, których w nim nie ma:
kto mówi, w jakim języku, jak długo, co pokazuje tło. Dlatego prompt piszemy tak, żeby
zostawić agentowi realizację, a nie tożsamość mówiącego.

## Szkielet, od którego zaczynasz

```
Zrób film z moim awatarem w HeyGen.

AWATAR: użyj mojego awatara „Ewa" z mojego konta. Nie dobieraj postaci z galerii
        ani żadnego innego awatara.
GŁOS:   mój głos „Ewa - narracja PL" z konta. Język: polski.
DŁUGOŚĆ: około 60 sekund.
FORMAT: 1920×1080 (poziom) — na stronę i YouTube.
TŁO:    jednolite, ciemny fiolet #2D1B69.

TEKST DO WYPOWIEDZENIA (przeczytaj dokładnie ten tekst, nie rozwijaj go
i nie dopisuj własnych zdań):
---
<tu wklej gotowy scenariusz z etapu 2>
---

NA EKRANIE: żadnych plansz poza podpisem imienia i nazwiska w pierwszych 5 sekundach.
NAPISY: włącz napisy po polsku.
```

## Pięć rzeczy, które muszą się w nim znaleźć

1. **Awatar po nazwie i zakaz podmiany.** Bez tego agent wybiera postać z galerii, a film
   z obcą twarzą jest do wyrzucenia razem z kredytami.
2. **Język polski wprost.** Agent domyślnie ciągnie w stronę angielskiego, także wtedy, gdy
   prompt jest po polsku.
3. **Gotowy tekst zamiast tematu.** „Powiedz o zebraniu" da tekst agenta. Wklejony scenariusz
   z etapu 2 daje tekst, który ona zaakceptowała.
4. **Długość i format kadru** — inaczej dostaniesz domyślny poziom 16:9, nawet gdy materiał
   idzie na Reels.
5. **Granica dopisywania.** Zdanie „nie dopisuj własnych zdań" wycina najczęstszą
   niespodziankę: doklejone wezwanie do działania albo cudzy claim reklamowy.

## Warianty

**Pion na Reels / TikToka / Stories**

```
FORMAT: 1080×1920 (pion), awatar w kadrze do połowy klatki piersiowej.
NAPISY: duże, wypalone w obrazie — materiał będzie oglądany bez dźwięku.
DŁUGOŚĆ: maksymalnie 30 sekund.
```

**Awatar w rogu, treść na planszach**

```
UKŁAD: awatar w prawym dolnym rogu, w kółku, około 25% szerokości kadru.
PLANSZE: po jednej na akapit tekstu, tylko hasła — maksymalnie 6 słów na planszę.
         Bez pełnych zdań i bez tabel.
```

**Poprawka gotowego materiału**

```
Weź projekt „Zaproszenie na zebranie" z moich Projects i zmień w nim tylko jedno:
tekst od zdania „Spotykamy się..." zastąp poniższym. Awatar, głos, tło i format
zostają bez zmian.
```

## Czego nie wpisywać

- **Klucza API ani hasła** — złącze loguje się przez OAuth, sekret nie jest potrzebny.
- **Nazwisk i danych uczniów, pacjentów, klientów** — materiał zostaje na koncie HeyGen.
  Imiona zamień na „uczeń", „dziecko", „uczestnik", chyba że film jest imienny z założenia.
- **Nierealnych obietnic i cudzych cytatów** — awatar wygląda jak ona, więc wszystko, co
  powie, będzie odczytane jako jej słowa.

## Po wygenerowaniu

Agent zwraca odnośnik do projektu (app.heygen.com → Projects). Zanim oddasz materiał, obejrzyj
go i sprawdź to, czego prompt nie gwarantuje: czy mówi jej awatar, czy wymowa liczb i skrótów
jest poprawna i czy nic nie zostało dopisane do scenariusza. Poprawki zamawiaj wariantem
„poprawka gotowego materiału" — nowy render od zera zużywa kredyty drugi raz.
