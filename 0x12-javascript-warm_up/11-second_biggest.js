#!/usr/bin/node
const process = require('process');

const nums = process.argv.slice(2).map(v => parseInt(v));
if (nums.length < 2) {
  console.log(0);
  process.exit();
}

console.log(nums)

let m1 = nums[0]; let m2 = nums[1];
for (let i = 1; i < nums.length; i++) {
  const n = nums[i];
  if (n > m1) {
    m2 = m1;
    m1 = n;
  } else if (n > m2) {
    m2 = n;
  }
}

console.log(m2);
