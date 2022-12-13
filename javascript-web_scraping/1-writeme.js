#!/usr/bin/node
const fs = require('fs');
const process = require('process');

let string = process.argv[3];

if (process.argv[3] === undefined || process.argv[3] === '') {
  string = '';
}

fs.writeFile(process.argv[2], string, function (error, data) {
  if (error) {
    console.log(error);
  }
});
