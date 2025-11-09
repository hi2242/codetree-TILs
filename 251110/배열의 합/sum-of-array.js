const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const grid = input.map(row => row.split(' ').map(Number));

let lineSum = null;
for (let i = 0; i < grid.length; i += 1) {
    lineSum = 0;
    for (let j = 0; j < grid[i].length; j += 1) {
        lineSum += grid[i][j];
    }
    console.log(lineSum);
}