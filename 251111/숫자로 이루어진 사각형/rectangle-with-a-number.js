const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = Number(input[0]);
// Please write your code here.

function printRect(n) {
    let temp = 1;
    for (let i = 0; i < n; i += 1) {
        for (let j = 0; j < n; j += 1) {
            process.stdout.write(`${temp} `);
            if (temp === 9) {
                temp = 1;
            } else {
                temp += 1;
            }
        }
        process.stdout.write('\n');
    }
}

printRect(N);