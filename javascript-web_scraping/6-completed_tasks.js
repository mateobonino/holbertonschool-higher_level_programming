#!/usr/bin/node
const process = require('process');
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const count = {};
  for (const i of data) {
    if (i.completed) {
      if (count[i.userId]) {
        count[i.userId]++;
      } else {
        count[i.userId] = 1;
      }
    }
  }
  console.log(count);
});
