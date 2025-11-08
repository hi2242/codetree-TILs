const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const num = Number(input);

let line = null;
for (let i = 1; i <= num; i += 1) {
    line = [];
    for (let j = 1; j <= num; j += 1) {
        line.push(`${i} * ${j} = ${i * j}`);
    }
    console.log(line.join(', '));
}