const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const [a, b, c] = input.split(' ').map(Number);
let result = 'NO';

for (let i = a; i <= b; i += 1) {
    if (i % c === 0) {
        result = 'YES';
        break;
    }
}

console.log(result);