import {Config} from '@remotion/cli/config';

Config.setVideoImageFormat('jpeg');
Config.setOverwriteOutput(true);
Config.setConcurrency(4);

// W tym środowisku Chromium jest już zainstalowany razem z Playwrightem —
// wskazujemy go, żeby Remotion nie pobierał własnej kopii.
const chromium = process.env.REMOTION_CHROMIUM;
if (chromium) {
  Config.setBrowserExecutable(chromium);
}
