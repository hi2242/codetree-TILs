const fs = require('fs');

let input = fs.readFileSync(0).toString().trim().split(' ');

let [a, b] = [Number(input[0]), Number(input[1])];

let result1 = null;
let result2 = null;

if (a < b) {
    result1 = 1;
} else {
    result1 = 0;
}

if (a === b) {
    result2 = 1;
} else {
    result2 = 0;
}

console.log(result1, result2);