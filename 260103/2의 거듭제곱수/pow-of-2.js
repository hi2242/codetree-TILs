const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
let N = Number(input);
let x = 0;

while (true) {
    if (N % 2 !== 0) {
        console.log(x);
        break;
    }
    if (N % 2 === 0) {
        N /= 2;
        x += 1;
    }
}