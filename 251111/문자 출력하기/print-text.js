const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();

let result = '';
for (let i = 0; i < 8; i += 1) {
    result += input;
}
console.log(result);