const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const A = Number(input);
let result = [];

for (let i = 1; i <= A; i += 1) {
    if (i % 2 === 0 && i % 4 !== 0) {
        continue;
    } else if (parseInt(i / 8) % 2 === 0) {
        continue;
    } else if (i % 7 < 4) {
        continue;
    } else {
        result.push(i);
    }
}

console.log(...result);