const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);
let row = null;

for (let i = 1; i <= N; i += 1) {
    row = '';
    if (i % 2 !== 0) {
        for (let j = 0; j < i / 2; j += 1) {
            row += '* ';
        }
    } else {
        for (let j = 0; j < N - (i / 2) + 1; j += 1) {
            row += '* ';
        }
    }
    console.log(row);
}

for (let i = N; i > 0; i -= 1) {
    row = '';
    if (i % 2 !== 0) {
        for (let j = 0; j < i / 2; j += 1) {
            row += '* ';
        }
    } else {
        for (let j = 0; j < N - (i / 2) + 1; j += 1) {
            row += '* ';
        }
    }
    console.log(row);
}