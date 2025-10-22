const FS = require('fs');

let input = FS.readFileSync(0).toString().trim().split(' ');

let [A, B] = [Number(input[0]), Number(input[1])];

console.log(A, B, A + B)