const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [A, B] = input.map(Number);

let result = '';
if (A < B) {
    result += '1 ';
} else {
    result += '0 ';
}

if (A === B) {
    result += '1 ';
} else {
    result += '0 ';
}

console.log(result);