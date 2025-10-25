const fs = require('fs');

let input = fs.readFileSync(0).toString().trim().split(' ');

let result = input.map(Number);

for (let i = 2; i < 10; i++) {
    result.push((result[i - 2] + result[i - 1]) % 10);
}

console.log(result.join(' '));