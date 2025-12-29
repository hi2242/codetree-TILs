const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);
let result = 1;

for (let i = 1; i <= 10; i += 1) {
    result *= i;
    if (result >= N) {
        console.log(i);
        break;
    }
}