const fs = require('fs');
const input = Number(fs.readFileSync(0).toString().trim());
let temp = 0;
let result = null;
for (let i = 1; i <= 100; i += 1) {
    if (temp + i >= input) {
        result = i;
        break;
    }
    temp += i;
}

console.log(result);