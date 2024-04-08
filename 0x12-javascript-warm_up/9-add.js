#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

const a = parseFloat(process.argv[2]); const b = parseFloat(process.argv[3]);
console.log(add(a, b));
