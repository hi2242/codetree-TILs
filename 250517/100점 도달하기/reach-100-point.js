const fs = require("fs");

let N = Number(fs.readFileSync(0).toString().trim());

let result = [];

for (let i = N; i <= 100; i++) {
    result.push(i >= 90 ? "A" : i >= 80 ? "B" : i >= 70 ? "C" : i >= 60 ? "D" : "F");
}

console.log(...result);