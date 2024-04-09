#!/usr/bin/node

module.exports.converter = function (base) {
  return (number) => {
    return number.toString(base);
  };
};
