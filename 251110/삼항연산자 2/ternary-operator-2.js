const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const a = Number(input);
const result = a === 1 ? 't' : 'f';

console.log(result);