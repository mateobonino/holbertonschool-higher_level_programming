#!/usr/bin/node
const request = require('request');
const process = require('process');
const string = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(string, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(body).title);
});
