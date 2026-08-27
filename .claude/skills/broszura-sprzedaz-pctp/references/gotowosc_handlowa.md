# Gotowość handlowa publikacji

Lista sprawdzana przed wystawieniem broszury na sprzedaż. Podzielona według tego,
co faktycznie blokuje sprzedaż, a co tylko podnosi jej wartość — bo to dwie różne
pilności i mylenie ich kosztuje czas.

---

## Blokujące — bez tego nie sprzedawaj

**Strona z prawami autorskimi.** Osobna strona, nie jedno zdanie na okładce.
Musi zawierać: znak `©` z rokiem i nazwiskiem, wydawcę, numer wydania, zakres
licencji (co wolno, czego nie wolno), informację o znaku wodnym oraz kontakt.
Szablon takiej strony jest w broszurze o echolalii — warto go skopiować.

**Dane sprzedawcy i regulamin.** Nazwa, NIP, adres, regulamin sprzedaży,
polityka prywatności. Przy treściach cyfrowych konieczna jest **zgoda kupującego
na natychmiastowe wykonanie umowy** — bez niej ma on 14 dni na odstąpienie
i zwrot pieniędzy mimo pobrania pliku.

**Kontakt do autorki.** Adres e-mail albo strona, widoczne w publikacji.
Brak kontaktu w płatnym materiale wygląda niepoważnie i uniemożliwia reklamacje.

**Źródła ilustracji.** Jeśli w publikacji są zdjęcia, musisz mieć do nich prawa:
własne, licencja komercyjna albo pisemna zgoda na wizerunek (przy dzieciach —
od rodzica lub opiekuna). Grafiki wektorowe rysowane kodem tego problemu nie mają
i dlatego są domyślnym wyborem.

---

## Podnoszące cenę

**Studium przypadku** — jedno dziecko od obserwacji do efektów po trzech
miesiącach. W materiałach dla pedagogów to element, który najmocniej przekonuje
do zakupu, bo pokazuje, że metoda działa u konkretnego ucznia, a nie w teorii.

**Recenzja specjalisty** — dwa zdania od neurologopedy albo pedagoga z tytułem,
umieszczone na stronie redakcyjnej.

**Załączniki do druku jako osobne pliki.** Arkusze i karty ukryte w środku
kilkudziesięciostronicowego PDF-u są nieużywane. Wyodrębnij je — robi to
`zbuduj_sprzedaz.py`.

**ISBN** — nadaje Biblioteka Narodowa bezpłatnie. Nie jest obowiązkowy przy
sprzedaży własnej, ale otwiera dystrybucję w księgarniach i podnosi wiarygodność.

---

## Techniczne

**Egzemplarz imienny.** Znak wodny z danymi nabywcy działa lepiej niż hasło:
nie utrudnia czytania ani druku, a pozwala ustalić źródło wycieku.
Skrypt `znak_wodny.py` generuje egzemplarz i numer do powiązania z zamówieniem.

**Próbka.** Kilka stron udostępnianych bezpłatnie — okładka, strona redakcyjna,
spis treści i jedna strona merytoryczna. Sprzedaje lepiej niż sam opis.

**Okładka jako obraz.** Do sklepu i mediów społecznościowych, minimum 1200 px
szerokości.

**Zakładki nawigacyjne w PDF.** Przy publikacji powyżej dwudziestu stron brak
zakładek jest odbierany jako niedbałość. Generuje je `zbuduj_sprzedaz.py`
na podstawie spisu treści.

---

## Ustalanie ceny

Punkty odniesienia z polskiego rynku materiałów dla pedagogów specjalnych
(stan na 2026): pojedyncze e-booki ze scenariuszami zajęć **20–22 zł**,
opracowania w księgarniach e-bookowych **39–50 zł**.

Sensowna struktura dla materiału obszernego, opartego na źródłach i zawierającego
gotowe druki:

| Licencja | Zakres | Orientacyjnie |
|---|---|---|
| Indywidualna | jedna osoba, użytek własny | 35–45 zł |
| Placówki | zespół do 15 osób, prawo do wydruku | 130–170 zł |
| Rozszerzona | licencja placówki plus konsultacja | 220–280 zł |

Cena premierowa niższa o 25–30 % przez pierwsze dwa–trzy tygodnie zbiera opinie,
które potem sprzedają. Poniżej 25 zł nie schodź — w tej kategorii zbyt niska cena
jest czytana jako niska jakość.

Licencja placówki ma zwykle największy potencjał: dyrektor kupuje raz dla całego
zespołu, a karta uzgodnień daje mu konkretny powód, żeby zdecydować o zakupie
zespołowym.
