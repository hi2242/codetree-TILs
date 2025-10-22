const fs = require("fs");
let point = Number(fs.readFileSync(0).toString().trim());

console.log(`Your score is ${point} point.`);