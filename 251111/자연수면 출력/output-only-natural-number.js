const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [A, B] = input.map(Number);

let result = '';
if (A > 0) {
    for (let i = 0; i < B; i += 1) {
        result += `${A}`;
    }
} else {
    result = 0;
}
console.log(result);