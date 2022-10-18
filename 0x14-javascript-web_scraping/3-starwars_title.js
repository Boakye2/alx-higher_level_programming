#!/usr/bin/nodejs
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/:id';
const id = process.argv[2];

request(url + id, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
