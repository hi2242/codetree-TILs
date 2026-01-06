const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);
let row = null;

for (let i = N; i > 0; i -= 1) {
    row = '';
    for (let j = 0; j < i; j += 1) {
        row += '* ';
    }
    console.log(row);
}