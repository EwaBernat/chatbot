# Głos prowadzącej — od nagrania do gotowego filmu

Nagranie powstaje **raz, w jednym ciągu**: autorka czyta cały scenariusz od
początku do końca, bez zatrzymywania się na plikach. Cała reszta — cięcie na
slajdy, wyrzucanie nieudanych podejść, wyrównanie głośności, synchronizacja
napisów — dzieje się automatycznie.

## Skąd wziąć transkrypcję z czasem

Potrzebny jest plik SRT: tekst z zegarem. Najprostsza droga to Descript
(konto autorki), bo rozpoznaje polski i zwraca czas z dokładnością do setnych:

1. `import_media` z `project_id` i wpisem `{"content_type": "audio/mp4",
   "file_size": <bajty>, "language": "pl"}`; odpowiedź zawiera `upload_url`,
   pod który wysyła się plik metodą PUT (`Content-Type: application/octet-stream`).
2. `wait_for_job` do zakończenia importu.
3. `prompt_project_agent`: „utwórz nową kompozycję z zaimportowanego pliku,
   bez cięć i bez usuwania pauz”.
4. `export_transcript` z `format: "srt"` i `composition_id` tej kompozycji.

Wynik zapisz jako `glos/<czesc>.srt`.

## Korekta transkrypcji przed cięciem

To moment na poprawienie tego, co w napisach ma wyglądać porządnie, mimo że w
nagraniu padło inaczej. Napisy biorą tekst **z SRT**, więc poprawki wprowadza
się właśnie tutaj:

- oczywiste przejęzyczenia i powtórzenia („wzrok, wzrok opiekuna”),
- nazwiska i terminy przekręcone przy czytaniu,
- interpunkcja — kropka zamiast przecinka tam, gdzie zdanie się kończy,
  bo po niej scalają się napisy,
- **nie ruszaj czasu** — on musi zostać taki, jak w nagraniu.

Poprawki, które zmieniają sens merytoryczny (zła nazwa metody, złe słowo w
definicji), zgłoś autorce do dogrania — napis można naprawić, głosu nie.

## Cięcie i czyszczenie

```bash
python3 scripts/dopasuj-glos.py \
  --dane src/dane/czesc1.json \
  --srt  glos/czesc1.srt \
  --audio nagranie.m4a \
  --wyjscie public/audio/czesc1
```

Skrypt:

1. rozkłada transkrypcję na strumień słów z czasem,
2. dla każdej kwestii szuka jej początku po pierwszych słowach scenariusza,
   a końca — po ostatnich; przy kilku podejściach wygrywa **ostatnie**,
   więc nieudane starty wypadają z materiału same,
3. dosuwa cięcia do najbliższej ciszy (`silencedetect`), żeby nie uciąć słowa,
4. czyści dźwięk: `highpass=85` (dudnienie pomieszczenia), `afftdn`
   (szum tła), `acompressor` (wyrównanie dynamiki), `loudnorm=I=-16:TP=-1.5`
   (jednakowa głośność w całym filmie i w każdym odtwarzaczu),
5. dopisuje do pliku danych napisy z **prawdziwym** czasem — w filmie tekst
   pojawia się dokładnie ze słowem, które pada.

Gdy któraś kwestia nie znajdzie się w nagraniu, skrypt wypisze ostrzeżenie i ją
pominie; film zrenderuje się dalej, a ten slajd przejdzie w ciszy.

## Dogrywki

Pojedynczą poprawioną kwestię wystarczy nagrać osobno i zapisać pod właściwym
numerem (`18.mp3`) w katalogu części — nadpisze poprzednią. Potem
`node scripts/oblicz-czas.mjs` i render. Nic więcej nie trzeba synchronizować.

## Czego pilnować przy nagraniu

- jedno pomieszczenie i jedno ustawienie mikrofonu dla całej części — inaczej
  słychać przeskok barwy między slajdami,
- pauza po każdej kwestii (2–3 sekundy ciszy) — to ona daje skryptowi punkty
  cięcia,
- pomyłkę powtarza się **od początku całej kwestii**, nie od słowa,
- telefon 20–30 cm od ust, lekko z boku.
