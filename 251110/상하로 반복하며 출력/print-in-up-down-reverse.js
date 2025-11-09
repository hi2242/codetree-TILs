const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);

for (let i = 0; i < N; i += 1) {
    let row = [];
    for (let j = 0; j < N; j += 1) {
        if (j % 2 === 0) {
            row.push(i + 1);
        } else {
            row.push(N - i);
        }
    }
    console.log(row.join(''));
}
