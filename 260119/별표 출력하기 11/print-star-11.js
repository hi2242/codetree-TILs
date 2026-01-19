const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);

let row = null;

for (let i = 1; i <= 3 + 2 * (N - 1); i += 1) {
    row = '';
    for (let j = 1; j <= 3 + 2 * (N - 1); j += 1) {
        if (i % 2 === 0 && j % 2 === 0) {
            row += '  ';
        } else {
            row += '* ';
        }
    }
    console.log(row);
}