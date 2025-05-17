const fs = require("fs");

let point = Number(fs.readFileSync(0).toString().trim())

console.log(point >= 90 ? "A" : point >= 80 ? "B" : point >= 70 ? "C" : point >= 60 ? "D" : "F")