#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log('code:', response.statusCode);
  }
  console.log('code:', response.statusCode);
});
