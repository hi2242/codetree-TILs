const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split("\n");

let [N, M] = input[0].split(" ").map(Number);

let grid_first = input.slice(1, N + 1).map(row => row.split(" ").map(Number));
let grid_second = input.slice(N + 1, N * 2 + 1).map(row => row.split(" ").map(Number));

let result = Array(N).fill(0).map(() => Array(M).fill(0));

for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
        result[i][j] = grid_first[i][j] === grid_second[i][j] ? 0 : 1
    }
}

console.log(result.map(row => row.join(" ")).join("\n"))
