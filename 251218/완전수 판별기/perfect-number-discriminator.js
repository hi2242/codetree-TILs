const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);
let sumVal = 0;
let result = null;

for (let i = 1; i < N; i += 1) {
    if (N % i === 0) {
        sumVal += i;
    }
}

if (N === sumVal) {
    result = 'P';
} else {
    result = 'N';
}

console.log(result);