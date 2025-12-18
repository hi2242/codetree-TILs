const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const arr = input.split('\n').map(Number);
let sumVal = 0;

for (let i = 0; i < arr.length; i += 1) {
    if (arr[i] % 2 !== 0 && arr[i] % 3 === 0) {
        sumVal += arr[i];
    }
}

console.log(sumVal);