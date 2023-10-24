#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Request failed with status code: ${response.statusCode}`);
  } else {
    try {
      const filmsData = JSON.parse(body);
      const wedgeAntillesFilms = filmsData.results.filter(film =>
        film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
      );
      console.log(`${wedgeAntillesFilms.length}`);
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
