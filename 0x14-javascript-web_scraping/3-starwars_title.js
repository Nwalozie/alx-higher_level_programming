#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: node starwars.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Request failed with status code: ${response.statusCode}`);
  } else {
    try {
      const movie = JSON.parse(body);
      console.log(`${movie.title}`);
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
