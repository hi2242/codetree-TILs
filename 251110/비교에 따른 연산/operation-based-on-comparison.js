const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [a, b] = input.map(Number);

let result = null;
if (a > b) {
    result = a * b;
} else {
    result = parseInt(b / a);
}

console.log(result);