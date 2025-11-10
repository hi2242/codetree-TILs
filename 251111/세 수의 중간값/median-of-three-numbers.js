const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [A, B, C] = input.map(Number);

console.log(Number(B > A && B < C));