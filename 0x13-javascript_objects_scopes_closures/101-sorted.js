#!/usr/bin/node

const dict = require('./101-data').dict;

const res = {}
Object.entries(dict).forEach((e) => {
    if (!(e[1] in res))
        res[e[1]] = [];
    res[e[1]].push(e[0]);
})
console.log(res);
