const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);

let line = null;
let start = 1;
for (let i = 1; i <= N; i += 1) {
    line = '';
    for (let j = 0; j < i; j += 1) {
        line += `${start} `;
        start += 1;
    }
    console.log(line);
}