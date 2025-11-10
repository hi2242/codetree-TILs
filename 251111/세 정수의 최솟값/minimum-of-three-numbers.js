const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [a, b, c] = input.map(Number);

if ((a > b && b > c) || (b > a && a > c)) {
    console.log(c);
} else if ((a > c && c > b) || (c > a && a > b)) {
    console.log(b);
} else {
    console.log(a);
}