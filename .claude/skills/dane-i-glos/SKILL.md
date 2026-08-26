---
name: dane-i-glos
description: >-
  Dane autorki, jej podpis odręczny, logo i głos — wszystko, czym podpisuje się
  materiał. Użyj ZAWSZE, gdy autorka prosi o: „podpisz to”, „dodaj moje dane”,
  „wstaw mój podpis”, „dodaj stopkę z kontaktem”, „plansza końcowa z moim
  nazwiskiem”, „wstaw logo”, „dopisz mój e-mail i telefon”, „wizytówka”,
  „stopka do maila”, a także przy każdym materiale firmowanym przez PCTP:
  prezentacji, filmie, dokumencie Word, broszurze, certyfikacie, ulotce.
  Wyzwalaj też na hasła: dane i głos, same dane bez głosu, podpis EduPlaner,
  Mirosława Ewa Jurczyszyn, Pomorskie Centrum Terapii Pedagogicznej, PCTP
  Koszalin, kontakt@eduplaner2026.pl. Skill działa w dwóch trybach: SAME DANE
  (podpis, nazwa, kontakt, logo, kolory marki) albo DANE I GŁOS — wtedy razem
  ze skillem glos-i-awatar podkłada również nagranie lektorskie autorki.
---

# Dane i głos autorki

Jedno miejsce, z którego biorą się: nazwisko, funkcja, nazwa firmy, kontakt,
kolory marki, podpis odręczny, logo — i wskazanie na głos.

## Źródło prawdy

`assets/dane.json`. Wczytaj ten plik i użyj pól; nigdy nie przepisuj adresu
ani numeru z pamięci, bo literówka w kontakcie kosztuje więcej niż wszystko inne
w materiale.

```
autorka.pelne     Mirosława Ewa Jurczyszyn
autorka.funkcja   pedagog specjalny
firma.pelna       Pomorskie Centrum Terapii Pedagogicznej
firma.podpis_krotki   PCTP Koszalin
kontakt.email     kontakt@eduplaner2026.pl
kontakt.telefon   [usunięto]
marka.fiolet      #2D1B69      (ekosystem EduPlaner)
marka.pomarancz   #E8450A
marka.zielen      #3E7B4F      (cykl Budowanie mostów społecznych)
```

Gotowe formuły — stopka krótka, stopka pełna, plansza końcowa, nota o prawach —
leżą w `formuly`. Używaj ich zamiast układać zdanie od nowa: dzięki temu
wszystkie materiały brzmią tak samo.

## Dwa tryby

**Same dane** (domyślnie) — podpisujesz materiał: stopka, plansza końcowa,
podpis odręczny, logo, kolory. Nic więcej nie jest potrzebne.

**Dane i głos** — materiał ma też ścieżkę lektorską albo awatara. Wtedy dane
stąd, a całą obsługę nagrania bierze skill **`glos-i-awatar`**: cięcie jednego
długiego nagrania na slajdy, czyszczenie dźwięku, napisy w rytm głosu, układy
kadru z awatarem.

## Podpis odręczny

Cztery wersje w `assets/`, wszystkie jako krzywe — działają bez instalowania
fontów i mają poprawne polskie znaki. Domyślny jest **`podpis-odreczny.svg`**
(żywy, pisany długopisem); do certyfikatów lepszy `podpis-kaligraficzny.svg`.
Rozmiary, kolory i miejsce w dokumencie: `references/uzycie.md`.

Podpis wstawiamy tam, gdzie materiał ma charakter osobisty — przedmowa, list do
rodziców, certyfikat, plansza końcowa filmu. Na dokumentach urzędowych (WOPF,
IPET) zostaje **pusta linia na odręczny podpis**, zgodnie z konwencją PCTP:
linia nad etykietą roli.

## Logo

Slot czeka w `assets/logo/`. Dopóki plik nie zostanie wgrany, materiały
podpisujemy samym nazwiskiem i nazwą — i tak wygląda to porządnie. Po wgraniu:
prawy górny róg strony tytułowej, plansza końcowa filmu, okładka prezentacji.

## Zasada

Każdy materiał wychodzący z tej pracowni ma **nazwisko autorki i nazwę PCTP**.
Kontakt dokładamy tam, gdzie materiał trafia poza placówkę: filmy, broszury,
ulotki, certyfikaty. W materiałach wewnętrznych wystarczy stopka krótka.
