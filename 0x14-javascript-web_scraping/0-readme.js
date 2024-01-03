#!/usr/bin/node
const fs = require('fs');
const args = process.argv[2]
const filePath = args

fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
        if (err.code === 'ENOENT'){
            console.error(err)
        } else {
            console.error(`Error reading the file: ${err.message}`)
        }
    } else {
        console.log(data)
    }
});
    