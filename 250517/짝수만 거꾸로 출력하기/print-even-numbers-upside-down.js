const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split("\n");

let N = Number(input[0]), arr = input[1].split(" ").map(Number);

let result = arr.filter(elem => elem % 2 === 0)

console.log(...result.reverse())