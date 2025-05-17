const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let [A, N] = input;

for (let i = 0; i < N; i++) {
    A += N
    console.log(A)
}