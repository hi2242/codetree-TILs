const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [a, b, c] = input.map(Number);
const sumAll = a + b + c;
const avg = sumAll / 3;

console.log(`${sumAll}
${avg}
${sumAll - avg}`);