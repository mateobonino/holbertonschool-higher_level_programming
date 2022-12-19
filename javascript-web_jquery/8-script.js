#!/usr/bin/node
const request = require('request');
const movieList = document.getElementById('list_movies');
request('https://swapi-api.hbtn.io/api/films/?format=json', function (error, response, body) {
  if (error) {
    console.log(error);
  }
  data = JSON.parse(body);
  for (const i of data.results) {
    movieList.innerHTML += i.title;
  }
});