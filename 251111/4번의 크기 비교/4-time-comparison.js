const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const A = Number(input[0]);
const [B, C, D, E] = input[1].split(' ').map(Number);

console.log(`${Number(A > B)}
${Number(A > C)}
${Number(A > D)}
${Number(A > E)}`);