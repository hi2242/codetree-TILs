const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [A, B] = input.map(Number);

let result = '';
for (let i = B; i >= A; i -= 1) {
    result += `${i} `;
}
console.log(result);