const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const realInput = input.split('\n').map(Number);
let i = 0;

while (true) {
    if (realInput[i] === 0) {
        break;
    }
    console.log(realInput[i]);
    i += 1;
}