const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);

let result = '';
let i = 1;
while (i <= N) {
    result += `${i} `;
    i += 1;
}
console.log(result);