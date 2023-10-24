#!/usr/bin/node

const request = require('request');
const fs = require('fs');

if (process.argv.length < 4) {
  console.error('Usage: node fetchAndStore.js <URL> <file_path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Request failed with status code: ${response.statusCode}`);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (writeError) => {
      if (writeError) {
        console.error(writeError);
      } else {
        console.log(`Webpage contents saved to ${filePath}`);
      }
    });
  }
});
