const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');

const [A, B] = input.map(Number);
let temp = A;
let result = [];

while (true) {
    if (temp > B) break;
    result.push(temp);
    if (temp % 2 !== 0) temp *= 2;
    else temp += 3;
}
console.log(result.join(' '));