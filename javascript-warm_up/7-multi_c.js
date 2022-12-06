#!/usr/bin/node
const process = require('process');

if (process.argv[2] !== undefined && parseInt(process.argv[2], 10) > 0) {
  for (let i = 0; i < parseInt(process.argv[2], 10); i++) {
    console.log('C is fun');
  }
}
if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
}
