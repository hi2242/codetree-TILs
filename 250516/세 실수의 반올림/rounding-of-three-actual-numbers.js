fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split("\n");

console.log(input.map(x => Number(x).toFixed(3)).join("\n"));