#!/usr/bin/node
const { argv } = require('node:process');
const num1 = parseInt(argv[2]);
if (isNaN(num1)) {
  console.log(1);
} else {
  console.log(fact(num1));
}

function fact (n) {
  if (n === 0 || n === 1) {
    return 1;
  }
  return n * fact(n - 1);
}
