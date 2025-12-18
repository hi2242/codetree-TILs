const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = Number(input[0])
const arr = input.slice(1, N + 1).map(Number);
let sumVal = 0;

for (let i = 0; i < N; i += 1) {
    if (arr[i] % 2 !== 0 && arr[i] % 3 === 0) {
        sumVal += arr[i];
    }
}

console.log(sumVal);