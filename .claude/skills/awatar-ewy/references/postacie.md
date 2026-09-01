# Sześć postaci awatara

Jedna twarz, jeden głos, sześć sposobów bycia. Postać zmienia **ton, tempo i długość
zdania** bardziej niż strój — widz rozpoznaje ją uchem, zanim zauważy marynarkę.

Wygląd bierze się z jednego awatara HeyGen (`Group ID` w `AVATAR-EWA.md`); poszczególne
stroje to **looki** w tej samej grupie. Nowy look dodaje się trybem z `avatar_group_id` —
wtedy powstaje wariant tej samej osoby, a nie nowa postać.

## Co już istnieje na koncie

Na dziś jest **jeden look**: „Ewa - szkolenia-niebieska" (strój niebieski), grupa
`4fceb4c254a349eab302734b740edbdd`.

Dopóki nie powstaną kolejne, **wszystkie postacie korzystają z tego looka** — a różnicę
niesie ton, tempo, kadr i tło, nie strój. To działa: widz rozpoznaje wykład po rytmie
i po tym, jak z nim rozmawiasz, zanim zauważy marynarkę. Nowe stroje dokładasz wtedy,
gdy sama uznasz, że warto — nie są warunkiem ruszenia z materiałami.

## Skrót

| Klucz | Postać | Odbiorca | Kadr | Tempo |
|---|---|---|---|---|
| `wyklad` | Szkolenie · Wykład | dyrektorzy, rada pedagogiczna | popiersie | spokojne |
| `warsztat` | Szkolenie · Warsztat | nauczyciele przy pracy | półpostać | rzeczowe |
| `konsultacja` | Szkolenie · Konsultacja | jedna osoba | zbliżenie | wolne |
| `maks` | Zajęcia z Maksem | dziecko | popiersie | bardzo wolne |
| `spot` | Spot reklamowy | dyrektorzy, social media | popiersie | spokojne |
| `herbatka` | Herbatka z Ewą | stali odbiorcy | popiersie luźne | swobodne |

## Ustawienia głosu

Wszystkie na klonie `jq4ZUryuBeDqmtkKtBZ4` („Ewa-głos_do skils"), model `eleven_v3`.

| Postać | stability | style | speed | Dlaczego |
|---|---|---|---|---|
| `wyklad` | 0.40 | 0.40 | 0.95 | równiej, bo treść jest gęsta — wahania męczą przy dłuższym słuchaniu |
| `warsztat` | 0.35 | 0.45 | 1.00 | naturalne tempo pracy, ma nadążać za czyimś robieniem |
| `konsultacja` | 0.30 | 0.50 | 0.92 | najbliżej rozmowy; niżej niż 0.30 głos zaczyna „pływać" |
| `maks` | 0.30 | 0.55 | 0.88 | dziecko potrzebuje czasu na przetworzenie każdego zdania |
| `spot` | 0.35 | 0.45 | 0.95 | ustawienie zatwierdzone odsłuchem przy spocie EduPlaner |
| `herbatka` | 0.28 | 0.55 | 1.00 | najszerszy zakres emocji — tu wolno się zaśmiać |

Zasady rytmu (akapit = pauza, wyliczenia po kropce) obowiązują wszędzie:
`.claude/skills/dane-i-glos/references/rytm_i_pauzy.md`.

---

## `wyklad` — Szkolenie · Wykład

**Kiedy:** rada pedagogiczna, webinar, szkolenie dla dyrektorów, wprowadzenie do tematu.
Wszędzie tam, gdzie mówisz do sali i musisz mieć autorytet od pierwszego zdania.

**Wygląd:** **strój niebieski** — look „Ewa - szkolenia-niebieska", jedyny istniejący
na koncie HeyGen. To on jest twarzą wszystkich trzech postaci szkoleniowych, dopóki nie
powstaną osobne looki dla warsztatu i konsultacji.
**Kadr:** popiersie, wzrok w obiektyw, awatar w lewej lub prawej trzeciej, resztę zajmuje treść.
**Tło:** fiolet marki `#2D1B69`, gładkie. Bez rozpraszaczy — konkurują z wykresem.

**Ton:** rzeczowy, ciepły, bez sprzedażowego nacisku. Mówisz do zapracowanego profesjonalisty,
który zna się na rzeczy — nie tłumacz oczywistości, ale nie zakładaj, że zna Twoje skróty.

**Zdania:** średniej długości, jedna myśl na zdanie. Termin fachowy wprowadzaj raz, z krótkim
rozwinięciem („WOPF, czyli wielospecjalistyczna ocena poziomu funkcjonowania"), potem używaj
skrótu swobodnie.

**Znaczniki:** `[calm]` domyślnie, `[sincerely]` przy wnioskach, `[slowly]` przy pointach.
**Długość:** 3–12 minut. Powyżej — dziel na odcinki, uwaga sali siada po kwadransie.
**Format:** 16:9. **Stopka:** pełna — nazwa firmy, podpis, e-mail, strona.

---

## `warsztat` — Szkolenie · Warsztat

**Kiedy:** instruktaż krok po kroku, ćwiczenie do wykonania, praca w grupach, „teraz Państwo
spróbują". Widz ma coś **robić**, nie tylko słuchać.

**Wygląd:** docelowo marynarka rozpięta albo zdjęta — mniej dystansu, ta sama osoba.
Do czasu utworzenia osobnego looka: strój niebieski, a dystans zdejmuje ton i kadr.
**Kadr:** półpostać, żeby było widać gest. Awatar mniejszy, obok duży kadr z ekranem aplikacji.
**Tło:** jaśniejszy wariant fioletu albo zrzut z aplikacji.

**Ton:** koleżeński, konkretny. Prowadzisz kogoś za rękę przez czynność.

**Zdania:** krótkie, w trybie rozkazującym, jedna czynność na zdanie. Numeruj kroki głosem
(„po pierwsze", „teraz"), żeby dało się słuchać bez patrzenia. **Zostawiaj ciszę** po każdym
kroku — widz musi zdążyć kliknąć. Buduj ją osobnym akapitem, nie wielokropkiem.

**Znaczniki:** `[calm]` przy krokach, `[encouraging]` przy zachęcie do próby.
**Długość:** 2–6 minut na jedno ćwiczenie. **Format:** 16:9.
**Stopka:** skrócona — podpis i e-mail. Po warsztacie widz wraca do pracy, nie do kontaktu.

---

## `konsultacja` — Szkolenie · Konsultacja

**Kiedy:** odpowiedź na konkretne pytanie, wsparcie dla jednej osoby, trudny temat
wymagający taktu. Nagranie, które ktoś ogląda sam, często z niepokojem.

**Wygląd:** docelowo jak w warsztacie, spokojniej; na razie strój niebieski.
**Kadr:** zbliżenie — twarz wypełnia kadr,
bez plansz obok. Rozmawiasz z jedną osobą; wykres by ją tu wyprowadził.
**Tło:** ciemny fiolet, mocno rozmyty.

**Ton:** ciepły, uważny, **bez pośpiechu**. Nazywasz trudność wprost, zanim podasz rozwiązanie —
człowiek z problemem najpierw chce usłyszeć, że problem jest prawdziwy.

**Zdania:** krótkie. Pauzy dłuższe niż gdziekolwiek indziej. Zwracaj się przez „Pani/Pan"
albo bezosobowo, zależnie od tego, jak przyszło pytanie.

**Znaczniki:** `[sincerely]` domyślnie, `[warmly]` na otwarcie i zamknięcie, `[slowly]`
przy najtrudniejszym zdaniu.
**Długość:** 1–4 minuty. **Format:** 16:9 lub 1:1.
**Stopka:** minimalna — sam e-mail. Konsultacja kończy się zaproszeniem do rozmowy, nie reklamą.

---

## `maks` — Zajęcia z Maksem

**Kiedy:** materiał dla dziecka albo do wspólnego oglądania z dzieckiem. Maks jest tu
imieniem odbiorcy — wstaw imię konkretnego dziecka, jeśli nagranie jest dla niego.

**To najbardziej wymagająca postać.** Dziecko nie wybaczy pośpiechu ani żargonu, a materiał
dla dzieci ze specjalnymi potrzebami tym bardziej.

**Wygląd:** bez marynarki, kolorowa bluzka, ciepło. **Kadr:** popiersie, twarz wyraźnie widoczna —
mimika jest tu połową przekazu. **Tło:** jasne, ciepłe, spokojne. Bez wzorów i ruchu.

**Ton:** ciepły, pogodny, **bardzo wolny**. Mówisz do dziecka, nie o dziecku.

**Zdania:** krótkie, proste, jedno polecenie na zdanie. Zero żargonu — żadnego „ewaluacji"
ani „funkcjonowania". Powtarzaj kluczowe słowo zamiast szukać synonimu; dla dziecka
synonim to nowe słowo do nauczenia, nie ozdoba.

**Pauzy po każdym zdaniu.** Osobny akapit za każdym razem, bez wyjątku.

**Znaczniki:** `[warmly]` i `[slowly]` na przemian. **Długość:** 1–3 minuty, nie więcej.
**Format:** 16:9. **Stopka:** żadnej. Dziecko nie jest odbiorcą kontaktu firmowego —
dane dla dorosłego umieść w opisie pliku, nie w kadrze.

---

## `spot` — Spot reklamowy

**Kiedy:** promocja EduPlaner 2026, materiał na stronę, Facebooka, Instagram, mail do dyrektora.

**Wygląd — strój spotowy, ten kanoniczny:** granatowa marynarka, biała bluzka, perły,
włosy upięte. To wygląd z portretu firmowego; trzymaj go bez zmian, żeby marka była
rozpoznawalna między materiałami.

**Kadr:** popiersie na pełnym kadrze w scenach mówionych, awatar w prawym dolnym rogu przy
planszach. **Tło:** fiolet `#2D1B69` z delikatnym gradientem.

**Ton:** ciepły, spokojny, przekonujący — bez presji. Nigdy „ostatnia szansa" ani „promocja
kończy się". Obietnicę podpieraj konkretem, kontakt pokazuj **po** wartości.

**Zdania:** krótkie, rytmiczne. Wyliczenia po kropce, nigdy po przecinku.
**Znaczniki:** `[warmly]` otwarcie i osobiste zdania, `[calm]` wyliczenia, `[sincerely]`
serce spotu, `[slowly]` pointy, `[encouraging]` wezwanie do działania.

**Długość:** 30–60 s. **Format:** 16:9 i 9:16 z tego samego nagrania.
**Stopka:** pełna, z miejscem na QR do formularza analizy potrzeb.

**Wzorzec do naśladowania:** `reklama/scenariusz-60s.md` — pięć scen z czasami, sprawdzone
w praktyce. Nowy spot buduj na tym łuku, zmieniając treść, nie strukturę.

---

## `herbatka` — Herbatka z Ewą

**Kiedy:** odcinek cyklu, kulisy, luźniejszy temat, odpowiedź na komentarze, „co u nas słychać".
Postać budująca **relację**, nie sprzedaż i nie wykład.

**Wygląd:** najbardziej swobodny — miękki sweter albo bluzka w cieplejszym kolorze,
włosy mniej formalnie. Kubek w kadrze jest mile widziany; to znak rozpoznawczy cyklu.
**Kadr:** popiersie, lekko z boku, mniej „prezenterski". **Tło:** ciepłe, domowe,
z delikatną głębią ostrości. Jedyna postać, w której tło może być nieformalne.

**Ton:** rozmowa przy stole. Możesz się zaśmiać, zawahać, zacząć od anegdoty. To jedyna
postać, w której **dygresja jest zaletą** — buduje wrażenie, że ktoś naprawdę mówi.

**Zdania:** naturalne, różnej długości. Zwracaj się bezpośrednio: „pewnie znasz to uczucie",
„piszecie mi, że…". Zaczynaj od konkretu z życia, nie od tezy.

**Znaczniki:** `[warmly]` przeważa, `[sincerely]` przy osobistym wątku,
`[encouraging]` na pożegnanie.
**Długość:** 3–8 minut. **Format:** 16:9, wersja 9:16 na zapowiedź.
**Stopka:** lekka — podpis i strona, bez telefonu i bez QR. To nie jest materiał sprzedażowy.

---

## Dodawanie nowej postaci

Nowa postać to nowy look w **tej samej grupie** awatara — nigdy nowa grupa:

```bash
heygen avatar looks list --group-id <group_id>     # co już jest
```

W aplikacji albo prosząc agenta: „dodaj mojemu awatarowi wersję w swetrze". Potem dopisz
tutaj sekcję według tego samego szablonu (kiedy · wygląd · kadr · tło · ton · zdania ·
znaczniki · długość · format · stopka) i wpisz `look_id` do `AVATAR-EWA.md`.

Bez opisu tonu nowa postać będzie tylko innym ubraniem — a różnica ma być słyszalna.
