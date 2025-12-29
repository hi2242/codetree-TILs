const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const [A, B] = input.split(' ').map(Number);
let result = 1;

for (let i = 1; i <= B; i += 1) {
    if (i % A === 0) {
        result *= i;
    } else {
        continue;
    }
}

console.log(result);