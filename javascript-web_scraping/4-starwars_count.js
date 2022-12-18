#!/usr/bin/node
const request = require('request');
const process = require('process');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  let count = 0;
  for (const i of data.results) {
    for (const j of i.characters) {
      if (j.includes('people/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});