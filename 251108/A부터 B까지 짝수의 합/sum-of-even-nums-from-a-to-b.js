const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');

const [A, B] = input.map(Number);
let result = 0;
for (let i = A; i <= B; i += 1) {
    if (i % 2 === 0) {
        result += i;
    }
}

console.log(result);