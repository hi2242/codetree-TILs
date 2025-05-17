fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split(" ");

let [A, B] = input.map(Number);

console.log(A, B, A + B);