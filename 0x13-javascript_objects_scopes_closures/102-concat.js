#!/usr/bin/node
const fs = require('fs');

const [file1, file2, destination] = process.argv.slice(2);

fs.readFile(file1, 'utf8', (err, data1) => {
  if (err) throw err;

  fs.readFile(file2, 'utf8', (err, data2) => {
    if (err) throw err;

    const data = data1 + data2;
    fs.writeFile(destination, data, 'utf8', (err) => {
      if (err) throw err;
    });
  });
});
