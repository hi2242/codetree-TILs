const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);
let result = 0;

for (let i = 0; i <= 100; i += 1) {
    result += i;
    if (result >= N) {
        console.log(i);
        break;
    }
}