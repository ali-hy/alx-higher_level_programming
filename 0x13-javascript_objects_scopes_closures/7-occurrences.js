#!/usr/bin/node

module.exports.nbOccurences = function (list, searchElement) {
  return list.reduce(
    (count = 0, curr) => {
      if (curr === searchElement) {
        count++;
      }
      return count;
    },
    0);
};
