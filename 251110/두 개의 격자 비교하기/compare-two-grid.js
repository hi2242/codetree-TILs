const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const firstGrid = input.slice(1, N + 1).map(row => row.split(' ').map(Number));
const secondGrid = input.slice(N + 1).map(row => row.split(' ').map(Number));

const resultGrid = [];
for (let i = 0; i < N; i += 1) {
    let row = [];
    for (let j = 0; j < M; j += 1) {
        if (firstGrid[i][j] === secondGrid[i][j]) {
            row.push(0);
        } else {
            row.push(1);
        }
    }
    resultGrid.push(row);
}

resultGrid.forEach(row => console.log(row.join(' ')));