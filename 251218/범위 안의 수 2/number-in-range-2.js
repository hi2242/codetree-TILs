const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const arr = input.split('\n').map(Number);
let sumVal = 0;
let index = 0;

arr.forEach(elem => {
    if (0 <= elem && elem <= 200) {
        sumVal += elem;
        index += 1;
    }
});

console.log(sumVal, (sumVal / index).toFixed(1));