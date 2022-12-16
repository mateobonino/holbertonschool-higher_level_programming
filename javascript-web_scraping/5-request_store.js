#!/usr/bin/node
const request = require('request');
const process = require('process');
const fs = require('fs');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(process.argv[3], body, function (error, data) {
    if (error) {
      console.log(error);
    }
  });
});
