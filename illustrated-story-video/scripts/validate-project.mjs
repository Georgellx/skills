#!/usr/bin/env node

import {spawnSync} from 'node:child_process';
import {existsSync, readFileSync} from 'node:fs';
import {dirname, resolve} from 'node:path';

const args = process.argv.slice(2);
const projectArg = args[0];
const videoIndex = args.indexOf('--video');
const previewMode = args.includes('--preview');

if (!projectArg) {
  console.error('Usage: node validate-project.mjs <project.json> [--video <final.mp4>] [--preview]');
  process.exit(1);
}

const projectPath = resolve(projectArg);
const projectDir = dirname(projectPath);
const errors = [];
const warnings = [];

if (!existsSync(projectPath)) {
  console.error(`Project file not found: ${projectPath}`);
  process.exit(1);
}

let project;
try {
  project = JSON.parse(readFileSync(projectPath, 'utf8'));
} catch (error) {
  console.error(`Invalid JSON: ${error.message}`);
  process.exit(1);
}

const positiveNumber = (value) => Number.isFinite(Number(value)) && Number(value) > 0;

if (!project.title || typeof project.title !== 'string' || !project.title.trim()) {
  errors.push('title must be filled before production.');
}

for (const key of ['width', 'height', 'fps']) {
  if (!positiveNumber(project.canvas?.[key])) errors.push(`canvas.${key} must be a positive number.`);
}

for (const key of ['blankSeconds', 'grayscaleEndSeconds', 'colorEndSeconds', 'featherPercent', 'zoomEnd']) {
  if (!positiveNumber(project.reveal?.[key])) errors.push(`reveal.${key} must be a positive number.`);
}

if (positiveNumber(project.reveal?.grayscaleEndSeconds) && positiveNumber(project.reveal?.colorEndSeconds)) {
  if (Number(project.reveal.grayscaleEndSeconds) >= Number(project.reveal.colorEndSeconds)) {
    errors.push('reveal.grayscaleEndSeconds must be earlier than reveal.colorEndSeconds.');
  }
}

if (!Array.isArray(project.scenes) || project.scenes.length === 0) {
  errors.push('At least one scene is required.');
} else {
  if (project.scenes.length !== 1 && (project.scenes.length < 4 || project.scenes.length > 8)) {
    warnings.push(`Scene count is ${project.scenes.length}; the supported production range is 4-8, while one scene is allowed for preview.`);
  }

  const ids = new Set();
  for (const [index, scene] of project.scenes.entries()) {
    const label = scene.id ?? String(index + 1);
    if (!scene.id) errors.push(`Scene ${index + 1} is missing id.`);
    if (ids.has(scene.id)) errors.push(`Duplicate scene id: ${scene.id}`);
    ids.add(scene.id);

    if (!positiveNumber(scene.durationSeconds)) {
      errors.push(`Scene ${label} durationSeconds must be positive.`);
    } else if (positiveNumber(project.reveal?.colorEndSeconds) && Number(scene.durationSeconds) <= Number(project.reveal.colorEndSeconds) + 0.3) {
      errors.push(`Scene ${label} is too short for the reveal and full-color hold.`);
    }

    if (!scene.image || typeof scene.image !== 'string') {
      errors.push(`Scene ${label} is missing image.`);
    } else {
      const imagePath = resolve(projectDir, 'remotion', 'public', scene.image);
      if (!existsSync(imagePath)) errors.push(`Scene ${label} image not found: ${imagePath}`);
    }

    if (!['contain', 'cover'].includes(scene.imageFit)) errors.push(`Scene ${label} imageFit must be contain or cover.`);
    if (!scene.imagePosition || typeof scene.imagePosition !== 'string') errors.push(`Scene ${label} is missing imagePosition.`);

    const subtitleLines = [scene.chinese, scene.english]
      .map((value) => typeof value === 'string' ? value.trim() : '')
      .filter(Boolean);
    if (subtitleLines.length === 0) errors.push(`Scene ${label} has no subtitle content.`);
  }
}

const totalDuration = Array.isArray(project.scenes)
  ? project.scenes.reduce((sum, scene) => sum + (Number(scene.durationSeconds) || 0), 0)
  : 0;
const expectedVideoDuration = previewMode && Array.isArray(project.scenes) && project.scenes[0]
  ? Number(project.scenes[0].durationSeconds) || 0
  : totalDuration;

if (videoIndex >= 0) {
  const videoArg = args[videoIndex + 1];
  if (!videoArg) {
    errors.push('--video requires a file path.');
  } else {
    const videoPath = resolve(videoArg);
    if (!existsSync(videoPath)) {
      errors.push(`Video not found: ${videoPath}`);
    } else {
      const probe = spawnSync('ffprobe', [
        '-v', 'error',
        '-show_entries', 'format=duration:stream=index,codec_type,codec_name,width,height,r_frame_rate,nb_frames',
        '-of', 'json',
        videoPath,
      ], {encoding: 'utf8'});

      if (probe.status !== 0) {
        errors.push(`ffprobe failed: ${(probe.stderr || '').trim() || 'unknown error'}`);
      } else {
        const data = JSON.parse(probe.stdout);
        const streams = Array.isArray(data.streams) ? data.streams : [];
        const videoStream = streams.find((stream) => stream.codec_type === 'video');
        const audioStreams = streams.filter((stream) => stream.codec_type === 'audio');

        if (!videoStream) errors.push('Final file has no video stream.');
        if (audioStreams.length > 0) errors.push(`Silent handoff contains ${audioStreams.length} audio stream(s).`);

        if (videoStream) {
          if (Number(videoStream.width) !== Number(project.canvas?.width)) errors.push(`Video width ${videoStream.width} does not match project ${project.canvas?.width}.`);
          if (Number(videoStream.height) !== Number(project.canvas?.height)) errors.push(`Video height ${videoStream.height} does not match project ${project.canvas?.height}.`);
          if (videoStream.codec_name !== 'h264') warnings.push(`Video codec is ${videoStream.codec_name}, expected h264.`);
        }

        const actualDuration = Number(data.format?.duration);
        const frameTolerance = 1 / Number(project.canvas?.fps || 30) + 0.02;
        if (Number.isFinite(actualDuration) && Math.abs(actualDuration - expectedVideoDuration) > frameTolerance) {
          errors.push(`Video duration ${actualDuration.toFixed(3)}s does not match expected ${expectedVideoDuration.toFixed(3)}s.`);
        }
      }
    }
  }
}

for (const warning of warnings) console.warn(`[WARN] ${warning}`);
for (const error of errors) console.error(`[ERROR] ${error}`);

console.log(`Scenes: ${Array.isArray(project.scenes) ? project.scenes.length : 0}`);
console.log(`Configured duration: ${totalDuration.toFixed(3)}s`);
if (previewMode) console.log(`Preview duration: ${expectedVideoDuration.toFixed(3)}s`);

if (errors.length > 0) {
  console.error(`Validation failed with ${errors.length} error(s).`);
  process.exit(1);
}

console.log('Validation passed.');
