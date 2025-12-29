const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const numberInput = input.split('\n').map(Number);
let i = 0;

while (true) {
    if (numberInput[i] === 1) {
        console.log('John');
    } else if (numberInput[i] === 2) {
        console.log('Tom');
    } else if (numberInput[i] === 3) {
        console.log('Paul');
    } else if (numberInput[i] === 4) {
        console.log('Sam');
    } else {
        console.log('Vacancy');
        break;
    }
    i += 1;
}