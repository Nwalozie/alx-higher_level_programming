#!/usr/bin/node

exports.esrever = function (list) {
  const temp = [];
  let count = 1;

  for (let i = 0; i < list.length; i++) {
    temp.push(list[(list.length - count)]);
    count++;
  }
  return temp;
};
