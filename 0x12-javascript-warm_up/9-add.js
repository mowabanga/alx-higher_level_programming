#!/usr/bin/node
const args = process.argv.slice(2);
const a = args[0];
const b = args[1];
function add(a, b) {
  sum = a + b;
  return (sum);
}
console.log(add(parseInt(a), parseInt(b)));
