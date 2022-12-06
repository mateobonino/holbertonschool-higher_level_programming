#!/usr/bin/node
const process = require('process');
let counter = 0;
const args = process.argv;
args.forEach((value, index) => {
  counter++;
});
if (counter <= 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2])
}
