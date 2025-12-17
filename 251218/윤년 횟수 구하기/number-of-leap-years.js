const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);
let count = 0;

for (let i = 1; i < N; i += 1) {
    if (i % 100 === 0 && i % 400 !== 0) {
        continue;
    } else if (i % 4 === 0) {
        count += 1;
    } else {
        continue;
    }
}

console.log(count);