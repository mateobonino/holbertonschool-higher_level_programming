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
  for (let i = 2; i < counter; i++) {
    console.log(process.argv[i]);
  }
}
