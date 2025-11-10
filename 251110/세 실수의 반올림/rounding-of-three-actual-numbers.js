const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [a, b, c] = input.map(Number);

console.log(`${a.toFixed(3)}
${b.toFixed(3)}
${c.toFixed(3)}`);