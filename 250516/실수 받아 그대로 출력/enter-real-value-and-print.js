fs = require("fs");

N = Number(fs.readFileSync(0).toString().trim())

console.log(N.toFixed(2))