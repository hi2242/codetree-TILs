const fs = require("fs");

let N = Number(fs.readFileSync(0).toString().trim())

let result = 0
for (let i = 1; i <= N; i++) {
    if (i % 2 === 0 || i % 3 === 0 || i % 5 === 0) {
        continue;
    }
    result++
}

console.log(result)