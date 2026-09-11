import {Config} from '@remotion/cli/config';

Config.setVideoImageFormat('jpeg');
Config.setOverwriteOutput(true);
Config.setConcurrency(2);
// Film w iframie liczy klatkę deterministycznie (window.__film.seek), więc nie trzeba spowalniać renderu.
// W kontenerze bez własnej przeglądarki:
//   npx remotion render OcenaFunkcjonalna ../out/film.mp4 --browser-executable=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell
