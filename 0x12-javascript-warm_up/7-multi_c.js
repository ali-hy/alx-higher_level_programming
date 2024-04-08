#!/usr/bin/node

const arg = process.argv[2];
const x = parseFloat(arg);
if (isNaN(x)) { console.log('Missing number of occurrences'); }
for (let i = 0; i < x; i++) {
  console.log('C is fun');
}
