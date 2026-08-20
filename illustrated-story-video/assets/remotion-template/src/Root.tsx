import React from 'react';
import {Composition} from 'remotion';
import projectJson from '../../project.json';
import {ScenePreview, StoryVideo} from './StoryVideo';
import type {ProjectConfig} from './types';

const project = projectJson as ProjectConfig;
const totalFrames = project.scenes.reduce(
  (sum, scene) => sum + Math.round(scene.durationSeconds * project.canvas.fps),
  0,
);
const previewFrames = Math.round(project.scenes[0].durationSeconds * project.canvas.fps);

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="ScenePreview"
        component={ScenePreview}
        defaultProps={{project}}
        durationInFrames={previewFrames}
        fps={project.canvas.fps}
        width={project.canvas.width}
        height={project.canvas.height}
      />
      <Composition
        id="StoryVideo"
        component={StoryVideo}
        defaultProps={{project}}
        durationInFrames={totalFrames}
        fps={project.canvas.fps}
        width={project.canvas.width}
        height={project.canvas.height}
      />
    </>
  );
};
