const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let [A, B, C] = input;

console.log((A > B && B > C) || (C > B && B > A) ? B : (B > A && A > C) || (C > A && A > B) ? A : C)