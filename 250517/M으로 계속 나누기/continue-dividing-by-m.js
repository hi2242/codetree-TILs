const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let [N, M] = input;

while (N != 0) {
    console.log(N)
    N = ~~(N / M)
}