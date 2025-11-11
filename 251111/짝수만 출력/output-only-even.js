const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [A, B] = input.map(Number);

let i = A;
let result = '';
while (i <= B) {
    result += `${i} `;
    i += 2;
}
console.log(result);