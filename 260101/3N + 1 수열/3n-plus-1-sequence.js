const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
let N = Number(input);
let count = 0;

while (true) {
    if (N === 1) {
        console.log(count);
        break;
    }
    if (N % 2 === 0) {
        N /= 2;
    } else {
        N = N * 3 + 1;
    }
    count += 1;
}