#!/usr/bin/nodejs
/**
 * Script that reads and prints the content of a file
 */
const fs = require('fs');
const file = process.argv[2];
// Asynchronous version of fs.readFile. Returns the contents of the filename
fs.readFile(file, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else console.log(data);
});
