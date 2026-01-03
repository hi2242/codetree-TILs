const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
let N = Number(input);
let cnt = 0;

while (N < 1000) {
    if (N % 2 === 0) {
        N = 3 * N + 1;
    } else {
        N = 2 * N + 2;
    }
    cnt += 1;
}

console.log(cnt);