const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const rows = input.split('\n');
const grid = rows.map(row => row.split(' ').map(Number));

const newGrid = grid.map(row => row.map(element => element * 3));

newGrid.forEach(row => console.log(row.join(' ')));