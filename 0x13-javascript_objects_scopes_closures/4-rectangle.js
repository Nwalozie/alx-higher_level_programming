#!/usr/bin/node
/**
 * Represents a rectangle
 */
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      /* returns an empty list object */
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (!this.width || !this.height) {
      console.log('Empty Rectangle');
      return;
    }

    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    if (this.width && this.height) {
      [this.width, this.height] = [this.height, this.width];
    }
  }

  double () {
    if (this.width && this.height) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}
module.exports = Rectangle;
