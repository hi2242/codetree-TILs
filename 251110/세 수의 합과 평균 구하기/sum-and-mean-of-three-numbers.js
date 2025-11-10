const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [A, B, C] = input.map(Number);

console.log(`${A + B + C}
${Math.floor((A + B + C) / 3)}`);