const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const grid = input.map(row => row.split(' ').map(Number));

let result = 0;
for (let i = 0; i < grid.length; i += 1) {
    for (let j = 0; j <= i; j += 1) {
        result += grid[i][j];
    }
}
console.log(result);