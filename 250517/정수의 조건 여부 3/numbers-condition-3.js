const fs = require("fs");

let a = Number(fs.readFileSync(0).toString().trim());

console.log(a % 13 === 0 || a % 19 === 0 ? "True" : "False");