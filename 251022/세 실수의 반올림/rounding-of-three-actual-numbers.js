const fs = require('fs');

let input = fs.readFileSync(0).toString().trim().split('\n');

console.log(`${Number(input[0]).toFixed(3)}\n${Number(input[1]).toFixed(3)}\n${Number(input[2]).toFixed(3)}`)