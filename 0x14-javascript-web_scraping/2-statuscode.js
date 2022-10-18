#!/usr/bin/nodejs
// Script that display the status code of a GET request
const request = require('request');
request(process.argv[2], function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
