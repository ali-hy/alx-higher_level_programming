#!/usr/bin/node
const process = require('process');

if (process.argv[2]) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
