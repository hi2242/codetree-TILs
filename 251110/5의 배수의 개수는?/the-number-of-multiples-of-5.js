const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const grid = input.map(row => row.split(' ').map(Number));

let result = 0;
grid.forEach(row => row.forEach(element => {
    if (element % 5 === 0) {
        result += 1;
    }
}));

console.log(result);