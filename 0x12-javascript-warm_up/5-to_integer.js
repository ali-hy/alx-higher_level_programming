#!/usr/bin/node
const process = require('process');

const arg = process.argv[2];
const num = parseFloat(arg);
if (isNaN(num)) { console.log('Not a number'); } else { console.log(`My number: ${num}`); }
