const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [N, a] = input.map(Number);

let i = 1;
while (i <= N) {
    if (i % a === 0) {
        console.log(1);
    } else {
        console.log(0);
    }
    i += 1;
}