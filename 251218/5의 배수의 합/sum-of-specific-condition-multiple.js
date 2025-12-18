const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const [A, B] = input.split(' ').map(Number);
let sumVal = 0;

for (let i = Math.min(A, B); i <= Math.max(A, B); i += 1) {
    if (i % 5 === 0) {
        sumVal += i;
    }
}

console.log(sumVal);