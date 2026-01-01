function printGrid(grid) {
    grid.forEach(row => {
        console.log(...row);
    })
}

const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const rows = input.split('\n');
const grid = [];
let index = 0;
rows.forEach(row => {
    grid.push(row.split(' '));
})

index = 0;
while (true) {
    console.log(Number(grid[index][0]) * Number(grid[index][1]));
    if (grid[index][2] === 'C') {
        break;
    }
    index += 1;
}