# -*- coding: utf-8 -*-
"""
Generuje nagrania siedmiu wstawek głosem autorki (ElevenLabs) na podstawie
wstawki_manifest.json. Uruchamiać TAM, gdzie sieć przepuszcza api.elevenlabs.io
— w kontenerze Claude Code na stronie jest to zablokowane.

    # raz: zapamiętaj głos z własnego nagrania (skrypt sam wyciągnie dźwięk z filmu)
    python3 ../.claude/skills/dane-i-glos/scripts/skonfiguruj_glos.py M1.mp4 --nazwa "Ewa - narracja PL"

    # potem:
    python3 nagraj_wstawki.py --wyjscie audio/

Bez zapamiętanego głosu elevenlabs_tts.py odmawia i kończy się kodem 4 —
i tak ma być. Żadnej wstawki nie wolno nagrać cudzym głosem.
"""
import argparse, json, os, subprocess, sys

SKRYPT_TTS = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          '..', '.claude', 'skills', 'dane-i-glos', 'scripts', 'elevenlabs_tts.py')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--manifest', default=os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                       'wstawki_manifest.json'))
    ap.add_argument('--wyjscie', default='audio')
    ap.add_argument('--tts', default=SKRYPT_TTS)
    ap.add_argument('--srt', action='store_true', help='dodatkowo zapisz napisy .srt')
    a = ap.parse_args()

    man = json.load(open(a.manifest, encoding='utf-8'))
    os.makedirs(a.wyjscie, exist_ok=True)
    znaki = 0
    for w in man['wstawki']:
        txt = os.path.join(a.wyjscie, f'{w["id"]}.txt')
        mp3 = os.path.join(a.wyjscie, f'{w["id"]}.mp3')
        with open(txt, 'w', encoding='utf-8') as f:
            f.write(w['narracja'] + '\n')
        znaki += len(w['narracja'])
        cmd = [sys.executable, a.tts, txt, '-o', mp3]
        if a.srt:
            cmd += ['--srt', os.path.join(a.wyjscie, f'{w["id"]}.srt')]
        print(f'--- {w["id"]} ({len(w["narracja"])} znaków) ---', flush=True)
        r = subprocess.run(cmd)
        if r.returncode == 4:
            print('\nPRZERWANE: skill nie ma zapamiętanego głosu autorki.')
            print('Uruchom najpierw: skonfiguruj_glos.py <nagranie lub film> --nazwa "Ewa - narracja PL"')
            sys.exit(4)
        if r.returncode != 0:
            print(f'Błąd generowania {w["id"]} (kod {r.returncode})'); sys.exit(r.returncode)
    print(f'\nGotowe: {len(man["wstawki"])} nagrań w {a.wyjscie}. '
          f'Zużyto około {znaki} znaków ElevenLabs.')


if __name__ == '__main__':
    main()
