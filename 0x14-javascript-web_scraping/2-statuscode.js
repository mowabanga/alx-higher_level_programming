#!/usr/bin/node
const { error } = require("console");
const url = process.argv[2];

fetch(url)
    .then(response => {
        if (response.ok) {
            console.log(`${response.status}`);
        } else {
            console.log(`${response.status} - ${response.statusText}`);
        }
    })
    .catch(error => {
        console.error(error);
    })