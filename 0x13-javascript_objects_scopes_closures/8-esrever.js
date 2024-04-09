#!/usr/bin/node

module.exports.esrever = function (list) {
  const res = new Array(list.length);
  for (let i = 0; i < res.length; i++) {
    res[i] = list[res.length - (i + 1)];
  }
  return res;
};
