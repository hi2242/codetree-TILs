const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);
const result = N === 100 ? 'pass' : 'failure';

console.log(result);