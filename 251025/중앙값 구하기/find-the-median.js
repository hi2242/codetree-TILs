const fs = require('fs');

let input = fs.readFileSync(0).toString().trim().split(' ');
let result = null;
let [a, b, c] = [Number(input[0]), Number(input[1]), Number(input[2])];

if (a > b) {
    if (b > c) {
        result = b;
    } else if (a > c) {
        result = c;
    } else {
        result = a;
    }
} else {
    if (a > c) {
        result = a;
    } else if (b > c) {
        result = c;
    } else {
        result = b;
    }
}

console.log(result);