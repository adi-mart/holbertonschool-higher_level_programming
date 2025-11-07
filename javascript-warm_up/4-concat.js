#!/usr/bin/node
const { argv } = require('node:process');
let args1 = argv[2];
let args2 = argv[3];
if (args1 == null) {
  args1 = undefined;
}
if (args2 == null) {
  args2 = undefined;
}
console.log(args1, 'is', args2);
