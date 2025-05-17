const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split(" ");

let [a, b, c] = input.map(Number);

let sum = [a, b, c].reduce((a, b) => (a + b), 0)
let avg = sum / 3

console.log(sum)
console.log(avg)
console.log(sum - avg)