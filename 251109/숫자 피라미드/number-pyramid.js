const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const num = Number(input);

let line = null;
for (let i = 1; i <= num; i += 1) {
    line = '';
    for (let j = 0; j < i; j += 1) {
        line += `${i} `;
    }
    console.log(line);
}