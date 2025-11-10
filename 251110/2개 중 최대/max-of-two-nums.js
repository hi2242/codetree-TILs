const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [A, B] = input.map(Number);

const result = A > B ? A : B;

console.log(result);