const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = Number(input[0]);
const arr = input.slice(1, N + 1).map(Number);
const sumVal = arr.reduce((acc, curr) => acc + curr, 0);

console.log(sumVal, (sumVal / N).toFixed(1));