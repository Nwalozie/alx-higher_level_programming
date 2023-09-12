#!/usr/bin/node
const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  charPrint (c = 'X') {
    const row = c.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

module.exports = Square;
