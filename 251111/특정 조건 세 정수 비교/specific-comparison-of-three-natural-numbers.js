const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [a, b, c] = input.map(Number);

let result = '';
if (a === Math.min(a, b, c)) {
    result += '1 ';
} else {
    result += '0 ';
}

if (a === b && b === c) {
    result += '1 ';
} else {
    result += '0 ';
}

console.log(result);