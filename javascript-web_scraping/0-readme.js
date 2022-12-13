#!/usr/bin/node
const fs = require('fs');
const process = require('process');

fs.readFile(process.argv[2], 'utf8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
