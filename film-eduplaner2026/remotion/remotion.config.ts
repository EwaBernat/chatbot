import { Config } from '@remotion/cli/config';

Config.setVideoImageFormat('jpeg');
Config.setOverwriteOutput(true);
Config.setConcurrency(2);

// Render w kontenerze bez własnej przeglądarki — wskaż ją jawnie:
//   npx remotion render Film out/film.mp4 --browser-executable=/opt/pw-browsers/chromium
