const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [C, N] = input;

let result = '';
if (C === 'A') {
    for (let i = 1; i <= N; i += 1) {
        result += `${i} `;
    }
} else {
    for (let i = N; i >= 1; i -= 1) {
        result += `${i} `;
    }
}
console.log(result);