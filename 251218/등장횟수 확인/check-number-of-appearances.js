const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const arr = input.split('\n').map(Number);
let count = 0;

for (let i = 0; i < arr.length; i += 1) {
    if (arr[i] % 2 === 0) {
        count += 1;
    }
}

console.log(count);