#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/people/5/?format=json', function (error, response, body) {
  if (error) {
    console.log(error);
  }
  data = JSON.parse(body);
  document.getElementById('character').innerHTML = data['name'];
});
