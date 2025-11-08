const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [start, end] = input.map(Number);

let count = null;
let result = 0;
for (let i = start; i <= end; i += 1) {
    count = 0;
    for (let j = 1; j <= i; j += 1) {
        if (i % j === 0) count += 1;
    }
    if (count === 3) result += 1;
}

console.log(result);