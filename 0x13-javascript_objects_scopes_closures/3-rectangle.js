#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined || w <= 0 || h <= 0) { return; }
    this.width = w;
    this.height = h;
  }

  print () {
    let res = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        res += 'X';
      }
      if (i < this.height - 1) {
        res += '\n';
      }
    }
    console.log(res);
  }
}

module.exports = Rectangle;
