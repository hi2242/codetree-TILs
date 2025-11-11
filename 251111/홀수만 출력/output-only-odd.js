const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [A, B] = input.map(Number);

let result = '';
for (let i = A; i <= B; i += 2) {
    result += `${i} `;
}
console.log(result);