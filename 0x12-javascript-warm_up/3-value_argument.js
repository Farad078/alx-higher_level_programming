#!/usr/bin/node

/* A script that prints the first argument passed to it */
const arg = process.argv;
let count = 0;
for (const element of arg) {
  count += 1;
}

if (count <= 2) {
  console.log('No argument');
} else {
  console.log(arg[2]);
}
