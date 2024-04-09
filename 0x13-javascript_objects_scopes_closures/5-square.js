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

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

class Square extends Rectangle {
    constructor (size) {
        super(size, size);
    }
}

module.exports = Square;
