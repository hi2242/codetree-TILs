const fs = require('fs');

let [a, b] = fs.readFileSync(0).toString().trim().split(' ');

console.log(`${Number(b)} ${Number(a)}`)