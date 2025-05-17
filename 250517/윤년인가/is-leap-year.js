const fs = require("fs");

let Y = Number(fs.readFileSync(0).toString().trim());

console.log(Y % 100 === 0 && Y % 400 !== 0 ? "false" : Y % 4 === 0 ? "true" : "false");