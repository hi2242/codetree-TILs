const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [A, B] = input.map(Number);

let result = '';
let i = A;
while (i <= B) {
    result += `${i} `;
    if (i % 2 !== 0) {
        i *= 2;
    } else {
        i += 3;
    }
}
console.log(result);