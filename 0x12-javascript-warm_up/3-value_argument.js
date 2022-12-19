#!/usr/bin/node
const args = process.argv.slice(2);
let length = 0;
for (let i of args) {
  length++;
}
if (length === 0) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
