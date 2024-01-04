#!/usr/bin/node

const reqs = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
reqs.get(url + id, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const dd = data.characters;
  for (const i of dd) {
    reqs.get(i, function (error, response, body1) {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
