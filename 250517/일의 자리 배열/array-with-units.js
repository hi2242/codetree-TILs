const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let result = [];

result.splice(0, 0, ...input);

for (let i = 2; i < 10; i++) {
    result.push((result[i - 2] + result[i - 1]) % 10);
}


console.log(...result);