const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');

const nums = input.map(Number);
let [countA, countB] = [0, 0];

nums.forEach(num => {
    if (num % 3 === 0) countA += 1;
    if (num % 5 === 0) countB += 1;
})

console.log(`${countA} ${countB}`);
