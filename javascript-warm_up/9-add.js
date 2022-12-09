#!/usr/bin/node
const process = require('process');
function add (a, b) {
  console.log(a + b);
}

if (process.argv.length < 4) {
  console.log(NaN);
} else {
  add(parseInt(process.argv[2], 10), parseInt(process.argv[3], 10));
}
