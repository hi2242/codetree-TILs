const fs = require("fs");

let N = Number(fs.readFileSync(0).toString().trim());

let result = [];
for (let i = N; i < N * 6; i += N) {
    result.push(i);
}

console.log(result.join(" "));