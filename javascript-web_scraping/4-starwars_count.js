#!/usr/bin/node
const request = require('request');
const process = require('process');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  
});