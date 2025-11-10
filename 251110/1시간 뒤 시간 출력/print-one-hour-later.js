const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(':');
const [h, m] = input.map(Number);

console.log(`${h + 1}:${m}`);