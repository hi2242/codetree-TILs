const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const [N, M] = input.split(' ').map(Number);

let row = null;

for (let i = 0; i < N; i += 1) {
    row = '';
    for (let j = 0; j < M; j += 1) {
        row += '* ';
    }
    console.log(row);
}