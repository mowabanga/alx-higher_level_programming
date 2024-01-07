#!/usr/bin/node
const request = require("request");
const url = process.argv[2];

request(url, (err, response, body) => {
    if (err) {
        console.error(err);
    } else if (response.statusCode !== 200) {
        console.log(response.statusCode);
    } else {
        try {
            const films = JSON.parse(body).results;
            console.log(films);
        }
        catch {
            console.log(parseError)
        }
    }
})