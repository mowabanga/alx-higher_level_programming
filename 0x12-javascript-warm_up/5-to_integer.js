#!/usr/bin/node
const args = process.argv.slice(2);
const check = Number.isInteger(+args[0]);
if (check === true) {
  console.log('My number:', args[0]);
} else {
  console.log('Not a number');
}
