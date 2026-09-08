import {Config} from '@remotion/cli/config';

Config.setVideoImageFormat('jpeg');
Config.setOverwriteOutput(true);
// W kontenerze bez własnej przeglądarki:
//   npx remotion render EduPlanerPromo out/eduplaner-promo.mp4 \
//     --browser-executable=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell
