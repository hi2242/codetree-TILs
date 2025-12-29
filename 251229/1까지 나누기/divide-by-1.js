const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
let N = Number(input);
let count = 0;
let index = 1;

while (true) {
    N = parseInt(N / index);
    index += 1;
    count += 1;
    if (N <= 1) {
        break;
    }
}

console.log(count);