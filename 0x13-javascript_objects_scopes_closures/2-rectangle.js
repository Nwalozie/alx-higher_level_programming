#!/usr/bin/node
/**
 * Represents a rectangle
 */
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {

    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
