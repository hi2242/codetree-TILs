const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const n = Number(input);

let result = '';
let i = n;
while (i >= 1) {
    result += `${i} `;
    i -= 1;
}
console.log(result);