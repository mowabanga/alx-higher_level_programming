#!/usr/bin/node
const args = process.argv.slice(2);
const number = Number.isInteger(+args[0]);
if (number !== true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args[0]; i++){
    let y = 0;
    let myVar = '';
    while (y < args) {
      myVar += 'X';
      y++;
    }
    console.log(myVar);
  }
}
