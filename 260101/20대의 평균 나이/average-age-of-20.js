const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const arr = input.split('\n').map(Number);
let acc = 0;
let index = 0;
let temp = 0;

while (true) {
    temp = arr[index];
    if (temp >= 20 && temp < 30) {
        acc += temp;
    } else {
        break;
    }
    index += 1;
}

console.log((acc / index).toFixed(2));