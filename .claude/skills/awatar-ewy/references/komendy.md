# Komendy — czym wywołać awatara

Ściąga do skopiowania. Skill wyzwala się sam, gdy w zdaniu jest **postać albo odbiorca**
plus **prośba o nagranie**. Nie trzeba podawać identyfikatorów, stroju ani ustawień głosu —
od tego jest ten skill.

## Najkrótsza wersja, która działa

```
Nagraj mnie: <o czym>
```

To wystarczy. Skill dobierze postać po odbiorcy, wczytają się ustawienia głosu, stopka
złoży się sama. Wszystko poniżej to doprecyzowanie, nie wymóg.

## Sześć postaci — komenda na każdą

| Postać | Komenda do skopiowania |
|---|---|
| `wyklad` | `Nagraj wykład dla dyrektorów o <temat>. Trzy minuty.` |
| `warsztat` | `Zrób warsztat dla nauczycieli: jak krok po kroku <czynność>.` |
| `konsultacja` | `Odpowiedz mną na pytanie: <pytanie>. Konsultacja, jedna osoba.` |
| `maks` | `Zajęcia z Maksem — wytłumacz dziecku <temat>. Krótko i wolno.` |
| `spot` | `Zrób spot reklamowy EduPlaner 2026 dla dyrektorów, 60 sekund.` |
| `herbatka` | `Odcinek Herbatki z Ewą dla rodziców o <temat>.` |

## Co dopisać, gdy ma być inaczej niż domyślnie

Dokładaj tylko to, co odbiega od definicji postaci w `postacie.md`:

| Chcesz | Dopisz |
|---|---|
| inną długość | `Dwie minuty.` / `Maksymalnie 45 sekund.` |
| pion na Reels/TikTok | `Wersja pionowa.` |
| oba formaty | `Poziom i pion.` |
| inny strój | `W lawendowej bluzce.` |
| ten sam tekst, inna postać | `To samo jako Herbatka z Ewą.` |
| bez stopki z kontaktem | `Bez stopki.` |
| sam tekst, bez nagrania | `Na razie tylko scenariusz.` |

## Pełna komenda — gdy chcesz mieć kontrolę

```
Nagraj mnie jako <postać>.
Temat: <o czym>.
Dla kogo: <odbiorca>.
Długość: <ile>.
Format: <poziom / pion / oba>.
```

Przykład, który przejdzie przez cały pipeline bez jednego pytania:

```
Nagraj mnie jako Wykład.
Temat: po co przedszkolu wielospecjalistyczna ocena poziomu funkcjonowania.
Dla kogo: dyrektorzy przedszkoli.
Długość: dwie minuty.
Format: poziom.
```

## Czego NIE trzeba pisać

Skill bierze to z plików, więc podawanie tego niczego nie poprawia, a bywa,
że wprowadza rozbieżność między materiałami:

- `avatar_id`, `group_id`, `look_id` → `AVATAR-EWA.md`
- `voice_id`, model, `stability`, `style`, `speed` → `postacie.md`, tabela ustawień głosu
- nazwa firmy, e-mail, telefon, logo, kolory → `marka-firmy.md`
- kadr, tło, ton, tempo → `postacie.md`, sekcja postaci

## Czego skill NIE zrobi po tej komendzie

Powie o tym wprost, zamiast podstawić zamiennik:

- **Nie ma połączenia z HeyGenem** → dostaniesz scenariusz i MP3 jej głosem
  z ElevenLabs, bez filmu. Film dorobi się jednym poleceniem, gdy połączenie wróci.
- **`Group ID` puste** → to samo; nigdy nie generuje awatara z opisu na zastępstwo.
- **Brak jej klonu głosu** → oddaje sam scenariusz. Cudzy głos pod jej nazwiskiem
  nie wchodzi w grę.

## Komendy do samego awatara, bez robienia filmu

```
Pokaż moje postacie awatara.
Jakie mam looki w HeyGenie?
Przypisz look <nazwa> do postaci <klucz>.
Zapisz nowy strój: <opis> dla <klucz>.
```

Ostatnia zapisuje decyzję na stałe — do `postacie.md` albo `AVATAR-EWA.md`.
Sens tego skilla polega na tym, że każdą decyzję podejmujesz raz.
