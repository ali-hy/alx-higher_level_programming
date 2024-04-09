#!/usr/bin/node

const Square = require('./5-square');

module.exports = class extends Square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let res = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        res += c;
      }
      if (i < this.height - 1) {
        res += '\n';
      }
    }
    console.log(res);
  }
};
