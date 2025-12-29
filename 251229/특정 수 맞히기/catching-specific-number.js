const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const numberInput = input.split('\n').map(Number);
let i = 0;

while (true) {
    if (numberInput[i] < 25) {
        console.log('Higher');
    } else if (numberInput[i] > 25) {
        console.log('Lower');
    } else {
        console.log('Good');
        break;
    }
    i += 1;
}