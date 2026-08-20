#!/usr/bin/env node

import {existsSync, mkdirSync, readFileSync, writeFileSync} from 'node:fs';
import {dirname, resolve} from 'node:path';

const args = process.argv.slice(2);
const projectArg = args[0];
const outputIndex = args.indexOf('--output');

if (!projectArg) {
  console.error('Usage: node generate-srt.mjs <project.json> [--output <subtitles.srt>]');
  process.exit(1);
}

const projectPath = resolve(projectArg);
if (!existsSync(projectPath)) {
  console.error(`Project file not found: ${projectPath}`);
  process.exit(1);
}

const projectDir = dirname(projectPath);
const outputPath = outputIndex >= 0 && args[outputIndex + 1]
  ? resolve(args[outputIndex + 1])
  : resolve(projectDir, 'outputs', 'final', 'subtitles.srt');

const project = JSON.parse(readFileSync(projectPath, 'utf8'));
const insetStart = Number(project.subtitles?.insetStartSeconds ?? 0.2);
const insetEnd = Number(project.subtitles?.insetEndSeconds ?? 0.1);

if (!Array.isArray(project.scenes) || project.scenes.length === 0) {
  console.error('project.json must contain at least one scene.');
  process.exit(1);
}

const pad = (value, length = 2) => String(value).padStart(length, '0');
const formatSrtTime = (seconds) => {
  const totalMilliseconds = Math.max(0, Math.round(seconds * 1000));
  const hours = Math.floor(totalMilliseconds / 3600000);
  const minutes = Math.floor((totalMilliseconds % 3600000) / 60000);
  const secs = Math.floor((totalMilliseconds % 60000) / 1000);
  const milliseconds = totalMilliseconds % 1000;
  return `${pad(hours)}:${pad(minutes)}:${pad(secs)},${pad(milliseconds, 3)}`;
};

let cursor = 0;
const cues = [];

for (const scene of project.scenes) {
  const duration = Number(scene.durationSeconds);
  if (!Number.isFinite(duration) || duration <= 0) {
    console.error(`Invalid durationSeconds for scene ${scene.id ?? '?'}.`);
    process.exit(1);
  }

  const lines = [scene.chinese, scene.english]
    .map((value) => typeof value === 'string' ? value.trim() : '')
    .filter(Boolean);

  if (lines.length === 0) {
    console.error(`Scene ${scene.id ?? '?'} has no subtitle content.`);
    process.exit(1);
  }

  const start = cursor + insetStart;
  const end = cursor + duration - insetEnd;
  if (end <= start) {
    console.error(`Subtitle inset is longer than scene ${scene.id ?? '?'} duration.`);
    process.exit(1);
  }

  cues.push({start, end, lines});
  cursor += duration;
}

const srt = cues
  .map((cue, index) => `${index + 1}\n${formatSrtTime(cue.start)} --> ${formatSrtTime(cue.end)}\n${cue.lines.join('\n')}`)
  .join('\n\n');

mkdirSync(dirname(outputPath), {recursive: true});
writeFileSync(outputPath, `${srt}\n`, 'utf8');
console.log(`Wrote ${cues.length} subtitle cues: ${outputPath}`);
console.log(`Subtitle timeline ends at ${formatSrtTime(cues.at(-1).end)}.`);
