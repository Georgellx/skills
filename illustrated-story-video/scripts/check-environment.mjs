#!/usr/bin/env node

import {spawnSync} from 'node:child_process';
import {existsSync} from 'node:fs';
import {dirname, join} from 'node:path';

const npmCli = join(dirname(process.execPath), 'node_modules', 'npm', 'bin', 'npm-cli.js');
const npmCheck = existsSync(npmCli)
  ? {command: process.execPath, args: [npmCli, '--version']}
  : {command: 'npm', args: ['--version']};

const checks = [
  {name: 'node', command: process.execPath, args: ['--version'], required: true},
  {name: 'npm', ...npmCheck, required: true},
  {name: 'ffmpeg', command: 'ffmpeg', args: ['-version'], required: true},
  {name: 'ffprobe', command: 'ffprobe', args: ['-version'], required: true},
];

let failed = false;

for (const check of checks) {
  const result = spawnSync(check.command, check.args, {encoding: 'utf8'});
  if (result.status !== 0) {
    console.error(`[MISSING] ${check.name}`);
    if (check.required) failed = true;
    continue;
  }

  const firstLine = `${result.stdout || result.stderr}`.trim().split(/\r?\n/)[0];
  console.log(`[OK] ${check.name}: ${firstLine}`);
}

if (failed) {
  console.error('Environment check failed. Install the missing required tools before rendering.');
  process.exit(1);
}

console.log('Environment check passed.');
