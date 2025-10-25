const fs = require('fs');

let input = fs.readFileSync(0).toString().trim().split('\n');

let firstLine = Number(input[0]);
// let secondLine = input[1].split(' ').map(num => Number(num) ** 2);

// console.log(secondLine.join(' '));

let result = [];
let secondLine = input[1].split(' ').map(Number);

for (let i = 0; i < firstLine; i++) {
    result.push(secondLine[i] * secondLine[i]);
}

console.log(result.join(' '));
