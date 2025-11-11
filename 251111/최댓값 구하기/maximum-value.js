const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [a, b, c] = input.map(Number);

let result = null;
if (a >= b && a >= c) {
    result = a;
} else if (b >= a && b >= c) {
    result = b;
} else {
    result = c;
}

console.log(result);