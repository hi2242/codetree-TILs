const fs = require("fs");

let words = ["apple", "banana", "grape", "blueberry", "orange"];
let input = fs.readFileSync(0).toString().trim();

let result = words.filter(elem => elem[2] === input || elem[3] === input);

if (result.length !== 0) {
    console.log(result.join("\n"));
}
console.log(result.length)