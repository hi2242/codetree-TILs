const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);

let result = '';
for (let i = 1; i <= N; i += 1) {
    result += `${i} `;
}

console.log(result);