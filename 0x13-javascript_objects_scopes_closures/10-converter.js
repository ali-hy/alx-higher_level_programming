#!/usr/bin/node
let counter = 0;

module.exports.converter = function (base) {
    return (number) => {
        return number.toString(base);
    }
}
