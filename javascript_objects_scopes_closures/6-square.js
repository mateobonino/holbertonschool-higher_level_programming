#!/usr/bin/node
const MySquare = require('./5-square');

class Square extends MySquare {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Square;
