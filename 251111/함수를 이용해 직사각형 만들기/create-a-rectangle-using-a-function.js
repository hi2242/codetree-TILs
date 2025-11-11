const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split("\n");
let [n, m] = input[0].split(" ").map(Number);

// Please Write your code here.

function printRect(width, height) {
    for (let i = 0; i < width; i += 1) {
        for (let j = 0; j < height; j += 1) {
            process.stdout.write('1');
        }
        process.stdout.write('\n');
    }
}

printRect(n, m);