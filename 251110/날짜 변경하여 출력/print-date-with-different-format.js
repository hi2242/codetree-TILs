const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('.');
const [y, m, d] = input;

console.log(`${m}-${d}-${y}`);