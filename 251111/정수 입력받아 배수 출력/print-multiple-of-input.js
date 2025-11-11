const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);

let result = '';
for (let i = N; i <= N * 5; i += N) {
    result += `${i} `;
}
console.log(result);