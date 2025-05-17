const fs = require("fs");

let input = fs.readFileSync(0).toString().trim();

let grid = input.split("\n").map(row => row.split(" ").map(Number));

let result = grid.map(row => row.map(elem => elem * 3));

console.log(result.map(row => row.join(" ")).join("\n"));