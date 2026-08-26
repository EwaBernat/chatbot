import {Config} from '@remotion/cli/config';

Config.setVideoImageFormat('jpeg');
Config.setOverwriteOutput(true);
// Przy renderze w kontenerze bez własnej przeglądarki wskaż ją jawnie:
//   npx remotion render RaportWideo out/film.mp4 --browser-executable=/opt/pw-browsers/chromium
