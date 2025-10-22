const fs = require('fs');

let input = fs.readFileSync(0).toString().trim().split(' ');

let [a, b, c] = [Number(input[0]), Number(input[1]), Number(input[2])];

let [sum, average] = [a + b + c, (a + b + c) / 3];

console.log(`${sum}\n${average}\n${sum - average}`)