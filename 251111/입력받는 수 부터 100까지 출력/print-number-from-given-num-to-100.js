const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const n = Number(input);

let result = '';
for (let i = n; i <= 100; i += 1) {
    result += `${i} `;
}
console.log(result);