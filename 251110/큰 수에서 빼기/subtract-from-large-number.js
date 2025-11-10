const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [A, B] = input.map(Number);

let result = null;
if (A > B) {
    result = A - B;
} else {
    result = B - A;
}

console.log(result);