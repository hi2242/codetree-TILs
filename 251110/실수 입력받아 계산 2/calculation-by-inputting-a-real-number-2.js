const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
let a = Number(input);
a += 1.5;

console.log(a.toFixed(2));