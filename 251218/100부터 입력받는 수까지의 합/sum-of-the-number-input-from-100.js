const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);
let sumVal = 0;

for (let i = N; i <= 100; i += 1) {
    sumVal += i;
}

console.log(sumVal);