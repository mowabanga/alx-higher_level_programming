#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2)
const filePath = args
fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
        if (err.code === 'ENOENT'){
            console.error('Error: File does not exist')
        } else {
            console.error(`Error reading the file: ${err.message}`)
        }
    } else {
        console.log(data)
    }
})