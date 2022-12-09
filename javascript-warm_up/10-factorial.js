#!/usr/bin/node
const process = require('process');
function factorial (num) {
  if (num < 0) {
    return -1;
  }
  if (num === 0) {
    return 1;
  }
  return (num * factorial(num - 1));
}

if (process.argv[2] === undefined) {
  console.log(factorial(1));
} else {
  console.log(factorial(parseInt(process.argv[2], 10)));
}
