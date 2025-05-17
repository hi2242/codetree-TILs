const fs = require("fs");

let input = fs.readFileSync(0).toString().trim()

let result = input.split("");

result.splice(1, 1, "a")
result.splice(-2, 1, "a")
console.log(result.join(""))