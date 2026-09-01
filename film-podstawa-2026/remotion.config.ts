import { Config } from '@remotion/cli/config';

Config.setVideoImageFormat('jpeg');
Config.setOverwriteOutput(true);
// Film jest długi (ok. 9,5 min) — bez współbieżności render ciągnie się godzinami.
Config.setConcurrency(null);
