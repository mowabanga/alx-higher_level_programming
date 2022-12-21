#!/usr/bin/node
const args = process.argv.slice(2);
const number = Number.isInteger(+args[0]);
if (number !== true) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < args; i++) {
    console.log('C is fun');
  }
}
