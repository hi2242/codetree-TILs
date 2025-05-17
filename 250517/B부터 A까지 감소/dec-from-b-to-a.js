const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let [A, B] = input;

let result = [];

for (let i = B; i >= A; i--) {
    result.push(i);
}

console.log(result.join(" "));