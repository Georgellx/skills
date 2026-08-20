#!/usr/bin/env node

import {copyFileSync, existsSync, mkdirSync, readdirSync, statSync, writeFileSync} from 'node:fs';
import {dirname, join, resolve} from 'node:path';
import {fileURLToPath} from 'node:url';

const outputArg = process.argv[2];

if (!outputArg) {
  console.error('Usage: node init-project.mjs <output-project-directory>');
  process.exit(1);
}

const outputDir = resolve(outputArg);
if (existsSync(outputDir)) {
  console.error(`Refusing to overwrite existing path: ${outputDir}`);
  process.exit(1);
}

const scriptDir = dirname(fileURLToPath(import.meta.url));
const templateDir = resolve(scriptDir, '..', 'assets', 'remotion-template');

const copyTree = (source, destination) => {
  if (statSync(source).isDirectory()) {
    mkdirSync(destination, {recursive: true});
    for (const entry of readdirSync(source)) {
      copyTree(join(source, entry), join(destination, entry));
    }
    return;
  }

  copyFileSync(source, destination);
};

if (!existsSync(templateDir)) {
  console.error(`Missing Remotion template: ${templateDir}`);
  process.exit(1);
}

for (const directory of [
  outputDir,
  join(outputDir, 'input'),
  join(outputDir, 'content'),
  join(outputDir, 'outputs', 'videos'),
  join(outputDir, 'outputs', 'final'),
  join(outputDir, 'outputs', 'checks'),
]) {
  mkdirSync(directory, {recursive: true});
}

const remotionDir = join(outputDir, 'remotion');
mkdirSync(remotionDir, {recursive: true});
for (const entry of readdirSync(templateDir)) {
  copyTree(join(templateDir, entry), join(remotionDir, entry));
}
mkdirSync(join(remotionDir, 'public', 'images'), {recursive: true});

const scenes = Array.from({length: 6}, (_, index) => {
  const number = String(index + 1).padStart(2, '0');
  return {
    id: number,
    image: `images/scene-${number}.png`,
    durationSeconds: 6.4,
    imageFit: 'contain',
    imagePosition: 'center center',
    chinese: '',
    english: '',
  };
});

const project = {
  title: '',
  canvas: {
    width: 1080,
    height: 1920,
    fps: 30,
    background: '#f8f3e9',
  },
  reveal: {
    blankSeconds: 0.2,
    grayscaleEndSeconds: 1.65,
    colorEndSeconds: 2.85,
    featherPercent: 10,
    zoomEnd: 1.022,
  },
  subtitles: {
    insetStartSeconds: 0.2,
    insetEndSeconds: 0.1,
  },
  scenes,
};

writeFileSync(join(outputDir, 'project.json'), `${JSON.stringify(project, null, 2)}\n`, 'utf8');

const scenePlan = `# Approved scene plan

Do not start image production until this table and subtitle wording are approved.

| Scene | Visible event | Narrative function | Emotional/information change | Chinese subtitle | English adaptation | Essential because |
| --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |
| 6 |  |  |  |  |  |  |

Content route approved: no
Scene plan approved: no
Chinese subtitles approved: no
English adaptation approved/not required: no
Unresolved content risks: not reviewed
`;

writeFileSync(join(outputDir, 'content', 'scene-plan.md'), scenePlan, 'utf8');

console.log(`Created illustrated story video project: ${outputDir}`);
console.log('Next: approve content/scene-plan.md, replace project.json text, and add images under remotion/public/images/.');
