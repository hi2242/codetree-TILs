const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const [A, B] = input.split(' ').map(Number);
let index = 0;
let sumVal = 0;

for (let i = A; i <= B; i += 1) {
    if (i % 5 === 0 || i % 7 === 0) {
        sumVal += i;
        index += 1;
    }
}

console.log(sumVal, (sumVal / index).toFixed(1));