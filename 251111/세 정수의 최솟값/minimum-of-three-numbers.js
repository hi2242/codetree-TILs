const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [a, b, c] = input.map(Number);

if (a >= c && b >= c) {
    console.log(c);
} else if (a >= b && c >= b) {
    console.log(b);
} else {
    console.log(a);
}