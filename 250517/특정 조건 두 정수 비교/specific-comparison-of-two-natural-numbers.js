const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let [a, b] = input;

process.stdout.write(a < b ? "1" : "0");
process.stdout.write(" ");
process.stdout.write(a === b ? "1" : "0");