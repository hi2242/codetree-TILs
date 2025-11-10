const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);
console.log(`Your score is ${N} point.`);