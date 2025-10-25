const fs = require('fs');

let input = fs.readFileSync(0).toString().trim().split(' ');
let result = input.reverse();

console.log(result.join(''));