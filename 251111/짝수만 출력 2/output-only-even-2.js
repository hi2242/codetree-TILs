const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [A, B] = input.map(Number);

let result = '';
let i = A;

while (i >= B) {
    result += `${i} `;
    i -= 2;
}
console.log(result);