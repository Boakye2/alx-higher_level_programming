#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonBody = JSON.parse(body);
    const dictTaskUser = {};
    for (const allTask of jsonBody) {
      if (allTask.completed) {
        if (dictTaskUser[allTask.userId]) {
          dictTaskUser[allTask.userId] += 1;
        } else {
          dictTaskUser[allTask.userId] = 1;
        }
      }
    }
    console.log(dictTaskUser);
  }
});
