#!/usr/bin/node

const fs = require('fs');
const file_path = process.argv[2];
const string = process.argv[3];

fs.writeFile(file_path, string, 'utf-8', function (err) {
  if (err) console.log(err);
});
