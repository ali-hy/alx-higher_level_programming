#!/usr/bin/node
const fs = require('fs');

// Get the file paths from the command line arguments
const [file1, file2, destination] = process.argv.slice(2);

// Read the first file
fs.readFile(file1, 'utf8', (err, data1) => {
  if (err) throw err;

  // Read the second file
  fs.readFile(file2, 'utf8', (err, data2) => {
    if (err) throw err;

    // Concatenate the data from the two files
    const data = data1 + data2;

    // Write the concatenated data to the destination file
    fs.writeFile(destination, data, 'utf8', (err) => {
      if (err) throw err;
    });
  });
});
