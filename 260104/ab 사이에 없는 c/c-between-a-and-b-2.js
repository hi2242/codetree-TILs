const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const [a, b, c] = input.split(' ').map(Number);
let result = 'YES';

for (let i = a; i <= b; i += 1) {
    if (i % c === 0) {
        result = 'NO';
        break;
    }
}

console.log(result);