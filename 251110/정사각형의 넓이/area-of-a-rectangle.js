const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);

console.log(N ** 2);
if (N < 5) {
    console.log('tiny');
}