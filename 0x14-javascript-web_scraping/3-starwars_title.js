#!/usr/bin/node
const request = require("request");
const argv = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${argv}`;

request(url, (error, response, body) => {
    if (error) {
        console.error(error);
    } else if (response.statusCode !== 200) {
        console.log(response.statusCode);
    } else {
        try {
            const film = JSON.parse(body);
            console.log(film['title']);
        } catch {
            console.error(parseError);
        }
    }
});