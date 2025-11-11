const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);

let result = '';
for (let i = 1; i <= N; i += 1) {
    if (i % 2 === 0 || i % 3 === 0) {
        result += `1 `;
    } else {
        result += `0 `;
    }
}
console.log(result);