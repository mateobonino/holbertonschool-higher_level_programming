#!/usr/bin/node
const request = require('request');
const helloTag = document.getElementById('hello');
request('https://stefanbohacek.com/hellosalut/?lang=fr', function (error, response, body) {
  if (error) {
    console.log(error);
  }
  data = JSON.parse(body);
  helloTag.innerHTML = data['hello'];
});
