const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split("\n");

let [A_math, A_eng] = input[0].split(" ").map(Number);
let [B_math, B_eng] = input[1].split(" ").map(Number);

console.log(A_math > B_math && A_eng > B_eng ? 1 : 0)