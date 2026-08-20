import React from 'react';
import {
  AbsoluteFill,
  Img,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import type {ProjectConfig, ProjectScene} from './types';

const clamp = (value: number) => Math.max(0, Math.min(1, value));

const revealMask = (progress: number, featherPercent: number): string => {
  const p = clamp(progress);
  const feather = Math.max(0, Math.min(30, featherPercent));

  if (p <= 0) return 'linear-gradient(to right, transparent 0%, transparent 100%)';
  if (p >= 1) return 'linear-gradient(to right, #000 0%, #000 100%)';

  const movingEdge = p * (100 + feather);
  const solidUntil = Math.max(0, Math.min(100, movingEdge - feather));
  const transparentFrom = Math.max(0, Math.min(100, movingEdge));

  return `linear-gradient(to right, #000 0%, #000 ${solidUntil}%, transparent ${transparentFrom}%, transparent 100%)`;
};

type StorySceneProps = {
  scene: ProjectScene;
  project: ProjectConfig;
};

export const StoryScene: React.FC<StorySceneProps> = ({scene, project}) => {
  const frame = useCurrentFrame();
  const {fps, durationInFrames} = useVideoConfig();
  const t = frame / fps;
  const {reveal, canvas} = project;

  const grayscaleProgress = interpolate(
    t,
    [reveal.blankSeconds, reveal.grayscaleEndSeconds],
    [0, 1],
    {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'},
  );
  const colorProgress = interpolate(
    t,
    [reveal.grayscaleEndSeconds, reveal.colorEndSeconds],
    [0, 1],
    {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'},
  );
  const scale = interpolate(
    frame,
    [0, Math.max(1, durationInFrames - 1)],
    [1, reveal.zoomEnd],
    {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'},
  );

  const commonImageStyle: React.CSSProperties = {
    position: 'absolute',
    inset: 0,
    width: '100%',
    height: '100%',
    objectFit: scene.imageFit,
    objectPosition: scene.imagePosition,
    transform: `scale(${scale})`,
    transformOrigin: 'center center',
  };

  return (
    <AbsoluteFill style={{backgroundColor: canvas.background, overflow: 'hidden'}}>
      <Img
        src={staticFile(scene.image)}
        style={{
          ...commonImageStyle,
          filter: 'grayscale(1) saturate(0) brightness(1.03) contrast(0.98)',
          WebkitMaskImage: revealMask(grayscaleProgress, reveal.featherPercent),
          maskImage: revealMask(grayscaleProgress, reveal.featherPercent),
        }}
      />
      <Img
        src={staticFile(scene.image)}
        style={{
          ...commonImageStyle,
          WebkitMaskImage: revealMask(colorProgress, reveal.featherPercent),
          maskImage: revealMask(colorProgress, reveal.featherPercent),
        }}
      />
    </AbsoluteFill>
  );
};
