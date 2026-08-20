import React from 'react';
import {AbsoluteFill, Sequence} from 'remotion';
import {StoryScene} from './StoryScene';
import type {ProjectConfig} from './types';

type StoryVideoProps = {
  project: ProjectConfig;
};

export const StoryVideo: React.FC<StoryVideoProps> = ({project}) => {
  let from = 0;

  return (
    <AbsoluteFill style={{backgroundColor: project.canvas.background}}>
      {project.scenes.map((scene) => {
        const durationInFrames = Math.round(scene.durationSeconds * project.canvas.fps);
        const sequence = (
          <Sequence
            key={scene.id}
            from={from}
            durationInFrames={durationInFrames}
            premountFor={project.canvas.fps}
          >
            <StoryScene scene={scene} project={project} />
          </Sequence>
        );
        from += durationInFrames;
        return sequence;
      })}
    </AbsoluteFill>
  );
};

export const ScenePreview: React.FC<StoryVideoProps> = ({project}) => {
  const scene = project.scenes[0];
  return <StoryScene scene={scene} project={project} />;
};
