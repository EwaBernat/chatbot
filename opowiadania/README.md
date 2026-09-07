# Rajmund i Arystoteles — pakiet dla Maksymiliana

| Plik | Co to jest |
|---|---|
| `Rajmund-i-Arystoteles-do-druku.pdf` | **Wersja do druku.** A4, 52 strony, duża czcionka, 6 ilustracji, każdy rozdział na nowej stronie. |
| `rajmund-i-arystoteles.md` | Tekst źródłowy (37 rozdziałów, słowniczek 41 pojęć, 45 pytań). |
| `rajmund-i-arystoteles.html` | Wersja HTML, z której powstaje PDF. |
| `obrazy/` | Sześć ilustracji (JPG, 1280×720). |
| `audio/scenariusz/` | 37 plików tekstowych — scenariusz do nagrania, po jednym na rozdział. |
| `audio/README.md` | Jak nagrać audiobook **Twoim głosem** (czego brakuje i dwa polecenia). |
| `skrypty/zbuduj_pdf.py` | Buduje PDF na nowo po każdej zmianie tekstu. |
| `skrypty/nagraj_audiobook.sh` | Nagrywa 37 plików MP3 + napisy SRT Twoim głosem. |

## Druk

Plik PDF jest gotowy do wydruku na A4. Marginesy 20–22 mm, czcionka 12,5 pkt,
interlinia 1,75, tekst wyrównany do lewej (bez justowania — łatwiej czytać).
Do zszycia albo wpięcia w segregator: druk jednostronny, wtedy pusta połowa
strony przy krótkich rozdziałach zostaje na notatki.

## Przebudowa PDF po zmianie tekstu

```bash
python3 opowiadania/skrypty/zbuduj_pdf.py
```

## Audiobook

Zobacz `audio/README.md`. Nagranie czeka na próbkę Twojego głosu —
skill nie tworzy nagrań cudzym głosem.
