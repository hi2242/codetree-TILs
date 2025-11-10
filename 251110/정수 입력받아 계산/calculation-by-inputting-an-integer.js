const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
let a = Number(input);
a = a * 2 + 3;
console.log(a);