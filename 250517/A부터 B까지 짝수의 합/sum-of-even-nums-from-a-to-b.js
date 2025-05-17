const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let [A, B] = input;

let result = 0;
for (let i = A; i <= B; i++) {
    if (i % 2 === 0) {
        result += i;
    }
}

console.log(result);