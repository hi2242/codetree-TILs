const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);
const ft = 30.48;

console.log((N * ft).toFixed(1));