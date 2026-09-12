import React, {useEffect, useRef, useState} from 'react';
import {
  AbsoluteFill,
  Audio,
  OffthreadVideo,
  Sequence,
  continueRender,
  delayRender,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';

export type Props = {
  audio: string | null;   // narracja.mp3 – Twój głos z ElevenLabs
  awatar: string | null;  // awatar.mp4 – Twój awatar z HeyGen (usta do tego samego MP3)
  srt: string | null;     // napisy.srt – sceny dosuwają się do prawdziwych zdań
  sekundy: number;        // długość filmu
};

type FilmOkno = Window & {
  __filmReadyPromise?: Promise<boolean>;
  __film?: {seek: (t: number) => void; awatarPos: () => {ax: number; ay: number; ad: number; p: number}};
};

/**
 * Film HTML (oryginalny druk + silnik animacji) liczy każdą klatkę deterministycznie
 * z czasu: window.__film.seek(t). Remotion tylko ustawia czas, dokłada dźwięk i awatar.
 */
const INTRO = 13.0;

export const Film: React.FC<Props> = ({audio, awatar, srt, sekundy}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const t = frame / fps;
  const ref = useRef<HTMLIFrameElement>(null);
  const [gotowy, setGotowy] = useState(false);
  const [pos, setPos] = useState({ax: 1560, ay: 224, ad: 260, p: 0});
  const [handle] = useState(() => delayRender('film html'));

  const q = new URLSearchParams({remotion: '1', dur: String(sekundy)});
  if (srt) q.set('srt', staticFile(srt));
  const src = staticFile('ocena_funkcjonalna_film.html') + '?' + q.toString();

  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const onLoad = () => {
      const w = el.contentWindow as FilmOkno | null;
      if (!w) return;
      (w.__filmReadyPromise ?? Promise.resolve(true)).then(() => {
        setGotowy(true);
        continueRender(handle);
      });
    };
    el.addEventListener('load', onLoad);
    return () => el.removeEventListener('load', onLoad);
  }, [handle]);

  useEffect(() => {
    if (!gotowy) return;
    const w = ref.current?.contentWindow as FilmOkno | null;
    if (!w?.__film) return;
    const h = delayRender('klatka ' + frame);
    w.__film.seek(t);
    setPos(w.__film.awatarPos());
    // jedna klatka na przemalowanie iframe'u
    requestAnimationFrame(() => continueRender(h));
  }, [gotowy, t, frame]);

  return (
    <AbsoluteFill style={{background: '#15102B'}}>
      <iframe
        ref={ref}
        src={src}
        title="Ocena Funkcjonalna – film"
        style={{width: 1920, height: 1080, border: 0, display: 'block'}}
      />
      {/* intro Ewy PCTP: jej twarz i jej głos z klipu ze skilla, przez pierwsze 13 s */}
      <Sequence from={0} durationInFrames={Math.round(INTRO * fps)}>
        <div style={{position: 'absolute', left: pos.ax - pos.ad / 2, top: pos.ay - pos.ad / 2, width: pos.ad, height: pos.ad, borderRadius: '50%', overflow: 'hidden', clipPath: 'circle(50% at 50% 50%)'}}>
          <OffthreadVideo src={staticFile('awatar/ewa_pctp_intro.webm')} transparent style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: '50% 0', transform: 'scale(1.55)', transformOrigin: '50% 18%'}} />
        </div>
      </Sequence>
      {audio ? (
        <Sequence from={Math.round(INTRO * fps)}>
          <Audio src={staticFile(audio)} />
        </Sequence>
      ) : null}
      {awatar ? (
        <div
          style={{
            position: 'absolute',
            left: pos.ax - pos.ad / 2,
            top: pos.ay - pos.ad / 2,
            width: pos.ad,
            height: pos.ad,
            borderRadius: '50%',
            overflow: 'hidden',
            boxShadow: '0 20px 60px rgba(0,0,0,.5)',
          }}
        >
          <Sequence from={Math.round(INTRO * fps)} layout="none">
            <OffthreadVideo
              src={staticFile(awatar)}
              muted
              style={{width: '100%', height: '100%', objectFit: 'cover'}}
            />
          </Sequence>
        </div>
      ) : null}
    </AbsoluteFill>
  );
};
