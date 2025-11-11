const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);

let i = 3;
let result = '';
while (i <= N) {
    result += `${i} `;
    i += 3;
}
console.log(result);