const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const rows = input.split('\n');

const fristGrid = rows.slice(0, 3).map(row => row.split(' ').map(Number));
const secondGrid = rows.slice(4, 8).map(row => row.split(' ').map(Number));

let resultGrid = [];
for (let i = 0; i < fristGrid.length; i += 1) {
    let row = [];
    for (let j = 0; j < fristGrid[i].length; j += 1) {
        row.push(fristGrid[i][j] * secondGrid[i][j]);
    }
    resultGrid.push(row);
}

resultGrid.forEach(row => console.log(row.join(' ')));