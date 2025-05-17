const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split(" ");

console.log(input[0].length > input[1].length ?
     `${input[0]} ${input[0].length}` : input[1].length > input[0].length ? 
     `${input[1]} ${input[1].length}` : "same")