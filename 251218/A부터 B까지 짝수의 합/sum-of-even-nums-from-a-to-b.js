const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
let [A, B] = input.split(' ').map(Number);
let sumVal = 0;

for (let i = A; i <= B; i += 1) {
    if (i % 2 === 0) {
        sumVal += i;
    }
}

console.log(sumVal);