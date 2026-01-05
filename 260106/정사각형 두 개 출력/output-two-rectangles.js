const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);
let row = null;

for (let i = 0; i <= 2 * N; i += 1) {
    row = '';
    for (let j = 0; j < N; j += 1) {
        row += '*'
    }
    if (i === N) {
        console.log();
    } else {
        console.log(row);
    }
}