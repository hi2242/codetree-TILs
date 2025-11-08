const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = Number(input[0]);
let [a, b] = [null, null];
let result = null;
for (let i = 1; i <= N; i += 1) {
    [a, b] = input[i].split(' ').map(Number);
    result = 0;
    for (let j = a; j <= b; j += 1) {
        if (j % 2 === 0) result += j;
    }
    console.log(result);
}