const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);
let row = null;

for (let i = 1; i <= N; i += 1) {
    row = '';
    if (i % 2 !== 0) {
        row += '* ';
        console.log(row);
        continue;
    } 
    for (let j = 0; j < i; j += 1) {
        row += '* ';
    }
    console.log(row);
}