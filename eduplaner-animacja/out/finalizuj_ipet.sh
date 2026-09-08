#!/bin/bash
# Render filmu IPET: tsc → remotion → kompresja → web/media. Użycie: bash out/finalizuj_ipet.sh
set -e
cd /home/user/chatbot/eduplaner-animacja
FF=node_modules/@remotion/compositor-linux-x64-gnu/ffmpeg
npx remotion render IpetPromo out/eduplaner-ipet.mp4 --browser-executable=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell --log=error --concurrency=4 2>&1 | tail -2
$FF -y -loglevel error -i out/eduplaner-ipet.mp4 -c:v libx264 -crf 24 -preset medium -pix_fmt yuv420p -movflags +faststart -c:a aac -b:a 160k out/eduplaner-ipet-web.mp4
cp out/eduplaner-ipet-web.mp4 ../web/media/eduplaner-ipet.mp4
ls -la out/eduplaner-ipet-web.mp4
node_modules/@remotion/compositor-linux-x64-gnu/ffprobe -v error -show_entries format=duration:stream=codec_type -of default=nw=1 out/eduplaner-ipet-web.mp4
