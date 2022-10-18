#!/usr/bin/nodejs
/**
 * Script that prints the number of movies where
 * the character “Wedge Antilles” is present.
 */
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const result = JSON.parse(body).results;
    let counter = 0;
    for (const film of result) {
      for (const character of film.characters) {
        if (character.endsWith('/18/')) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
