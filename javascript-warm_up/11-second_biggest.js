#!/usr/bin/node
const process = require('process');

if (process.argv.length >= 4) {
  const myArray = [];
  for (let i = 2; i < process.argv.length; i++) {
    myArray.push(Number(process.argv[i]));
  }
  const myMax = Math.max.apply(null, myArray);
  myArray.splice(myArray.indexOf(myMax), 1);
  console.log(Math.max.apply(null, myArray));
} else {
  console.log(0);
}
