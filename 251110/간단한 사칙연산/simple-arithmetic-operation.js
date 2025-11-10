const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [A, B] = input.map(Number);

console.log(`${A + B}
${A - B}
${parseInt(A / B)}
${A % B}`);