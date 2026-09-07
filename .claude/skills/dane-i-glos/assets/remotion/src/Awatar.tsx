import React from 'react';
import {OffthreadVideo, Sequence, staticFile, useVideoConfig} from 'remotion';
import type {Awatar as AwatarDef, UkladAwatara} from './typy';

/**
 * Postać Ewa PCTP w kompozycji (skill awatar-ewa-pctp).
 *
 * Klip musi mieć kanał alfa (WebM VP9 z wytnij_postac.py); `transparent`
 * każe Remotion wyciągać klatki z przezroczystością, więc Ewa stoi na tle
 * sceny, a nie w czarnym prostokącie. Układy odpowiadają wstaw_ewe.py:
 * pelny / rog / lewa / prawa — te same proporcje, żeby film z ffmpeg
 * i film z Remotion wyglądały tak samo.
 */
const SKALA: Record<UkladAwatara, number> = {pelny: 1.0, rog: 0.42, lewa: 0.9, prawa: 0.9};

const polozenie = (
  uklad: UkladAwatara,
  margines: number,
): React.CSSProperties => {
  switch (uklad) {
    case 'rog':
      return {right: margines, bottom: margines};
    case 'lewa':
      return {left: margines, bottom: 0};
    case 'prawa':
      return {right: margines, bottom: 0};
    default:
      return {left: 0, right: 0, bottom: 0, display: 'flex', justifyContent: 'center'};
  }
};

export const Awatar: React.FC<{awatar: AwatarDef; wyciszony?: boolean}> = ({awatar, wyciszony}) => {
  const {fps, height} = useVideoConfig();
  const uklad = awatar.uklad ?? 'pelny';
  const wysokosc = Math.round(height * (awatar.skala ?? SKALA[uklad]));
  const margines = awatar.margines ?? 48;
  const od = Math.round((awatar.odSek ?? 0) * fps);
  const trwanie = awatar.doSek != null ? Math.max(1, Math.round((awatar.doSek - (awatar.odSek ?? 0)) * fps)) : undefined;

  const klip = (
    <div style={{position: 'absolute', ...polozenie(uklad, margines)}}>
      <OffthreadVideo
        src={staticFile(awatar.plik)}
        transparent
        muted={wyciszony || awatar.dzwiek === false}
        style={{height: wysokosc, width: 'auto', display: 'block'}}
      />
    </div>
  );

  return trwanie ? (
    <Sequence from={od} durationInFrames={trwanie}>{klip}</Sequence>
  ) : (
    <Sequence from={od}>{klip}</Sequence>
  );
};
