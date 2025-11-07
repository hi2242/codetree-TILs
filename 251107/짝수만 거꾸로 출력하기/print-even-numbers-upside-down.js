const fs = require('fs');

let input = fs.readFileSync(0).toString().trim().split('\n');

let [N, num] = [Number(input[0]), input[1].split(' ').map(Number)];
let result = [];

for (let i = N - 1; i >= 0; i -= 1) {
    if (num[i] % 2 === 0) result.push(num[i]);
}

console.log(result.join(' '));