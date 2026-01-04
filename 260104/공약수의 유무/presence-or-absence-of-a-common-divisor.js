const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const [A, B] = input.split(' ').map(Number);
let result = 0;

for (let i = A; i <= B; i += 1) {
    if (1920 % i === 0 && 2880 % i === 0) {
        result = 1;
        break;
    }
}

console.log(result);