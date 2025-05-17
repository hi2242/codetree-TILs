const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split("\n").map(Number);

let result_three = input.filter(elem => elem % 3 === 0);
let result_five = input.filter(elem => elem % 5 === 0);

console.log(result_three.length, result_five.length);