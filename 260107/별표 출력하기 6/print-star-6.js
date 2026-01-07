const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);
let row = null;

for (let i = 0; i < N; i += 1) {
    row = '';
    for (let j = 0; j < i; j += 1) {
        row += '  ';
    }

    for (let j = 0; j < 2 * (N - i) - 1; j += 1) {
        row += '* ';
    }
    console.log(row);
}

for (let i = 1; i < N; i += 1) {
    row = '';
    for (let j = 0; j < N - i - 1; j += 1) {
        row += '  ';
    }
    for (let j = 0; j < 2 * i + 1; j += 1) {
        row += '* ';
    }
    console.log(row);
}
