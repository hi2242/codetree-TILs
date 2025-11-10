const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
let [a, b] = input.map(Number);

a += b;
b += a;

console.log(a, b);