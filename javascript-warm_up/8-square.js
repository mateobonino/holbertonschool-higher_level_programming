#!/usr/bin/node
const process = require('process');

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2], 10); i++) {
    console.log('X'.repeat(parseInt(process.argv[2], 10)));
  }
}
