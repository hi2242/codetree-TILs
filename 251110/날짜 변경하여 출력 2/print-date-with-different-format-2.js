const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('-');
const [m, d, y] = input;

console.log(`${y}.${m}.${d}`);