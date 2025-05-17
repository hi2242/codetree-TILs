const fs = require("fs");

let N = Number(fs.readFileSync(0).toString().trim());

function solve() {
    let temp = 0;
    for (let i = 1; i <= 100; i++) {
        temp += i;
        if (temp >= N) {
            return i;
        }
    }
}

console.log(solve());