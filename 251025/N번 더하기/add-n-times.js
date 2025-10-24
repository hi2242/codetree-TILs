const fs = require('fs');

let input = fs.readFileSync(0).toString().trim().split(' ');

let [A, N] = [Number(input[0]), Number(input[1])];

let result = A;
for (let i = 0; i < N; i++) {
    result += N;
    console.log(result);
}