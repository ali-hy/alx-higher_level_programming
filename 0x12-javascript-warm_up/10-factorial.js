#!/usr/bin/node
const process = require('process');

function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return (1);
  }

  return (n * factorial(n - 1));
}

const a = process.argv[2];
console.log(factorial(a));
