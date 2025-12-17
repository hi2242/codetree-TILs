const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const arr = input.split('\n').map(Number);

let [countA, countB] = [0, 0];

for (let i = 0; i < arr.length; i += 1) {
    if (arr[i] % 3 == 0) {
        countA += 1;
    }

    if (arr[i] % 5 == 0) {
        countB += 1;
    }
}

console.log(countA, countB);