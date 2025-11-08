const fs = require('fs');

const input = Number(fs.readFileSync(0).toString().trim());
let result = 0;
for (let i = 0; i <= input; i += 1) {
    if (i % 2 === 0) continue;
    if (i % 3 === 0) continue;
    if (i % 5 === 0) continue;
    result += 1;
}

console.log(result);