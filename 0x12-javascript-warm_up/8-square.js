#!/usr/bin/node

const arg = process.argv[2];
const x = parseFloat(arg);
if (isNaN(x)) { console.log('Missing size'); } else {
  let res = '';
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      res += 'X';
    }
    if (i < x - 1) {
      res += '\n';
    }
  }
  console.log(res);
}
