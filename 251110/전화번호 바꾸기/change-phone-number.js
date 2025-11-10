const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('-');
const [a, b, c] = input;

console.log(`${a}-${c}-${b}`);