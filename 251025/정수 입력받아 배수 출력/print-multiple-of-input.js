const fs = require('fs');

let input = Number(fs.readFileSync(0).toString().trim());
let result = '';

for (let i = input; i <= input * 5; i += input) {
    result += `${i} `;
}

console.log(result);