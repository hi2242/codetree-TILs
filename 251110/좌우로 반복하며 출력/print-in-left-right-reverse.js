const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);

for (let i = 0; i < N; i += 1) {
    let row = [];
    for (let j = 1; j <= N; j += 1) {
        if (i % 2 === 0) {
            row.push(j);
        } else {
            row.push(N - j + 1);
        }
    }
    console.log(row.join(''));
}
