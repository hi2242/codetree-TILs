const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [a, b] = input.map(Number);

console.log(a * b);