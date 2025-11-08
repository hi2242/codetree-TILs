const fs = require('fs');
const input = Number(fs.readFileSync(0).toString().trim());
let result = 0;
for (let i = 1; i <= 100; i += 1) {
    if (result + i >= input) {
        break;
    }
    result += i;
}

console.log(result);