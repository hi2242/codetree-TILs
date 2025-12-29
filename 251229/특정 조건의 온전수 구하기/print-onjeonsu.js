const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);
let result = [];

for (let i = 1; i <= N; i += 1) {
    if (i % 2 === 0) {
        continue;
    } else if (i % 10 === 5) {
        continue;
    } else if (i % 3 === 0 && i % 9 !== 0) {
        continue;
    } else {
        result.push(i);
    }
}

console.log(...result);