const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);
let result = 'P';

for (let i = 2; i <= N - 1; i += 1) {
    if (N % i === 0) {
        result = 'C';
        break;
    }
}

console.log(result);