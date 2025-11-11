const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);

let i = 1;
while (i <= N) {
    console.log('*');
    i += 1;
}