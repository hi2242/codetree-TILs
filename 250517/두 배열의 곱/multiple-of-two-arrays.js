const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split("\n");

let grid_first = input.slice(0, 3).map(row => row.split(" ").map(Number));
let grid_second = input.slice(4, 7).map(row => row.split(" ").map(Number));

let result = Array.from({length : 3}, () => Array(3).fill(0));

for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
        result[i][j] = grid_first[i][j] * grid_second[i][j];
    }
}

console.log(result.map(row => row.join(" ")).join("\n"));