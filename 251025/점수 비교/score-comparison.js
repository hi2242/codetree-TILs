const fs = require('fs');

let input = fs.readFileSync(0).toString().trim().split('\n');
let result = null;
let [a, b] = [input[0].split(' '), input[1].split(' ')];

let info_a = {
    math : Number(a[0]),
    english : Number(a[1]),
}

let info_b = {
    math : Number(b[0]),
    english : Number(b[1]),
}

if (info_a.math > info_b.math && info_a.english > info_b.english) {
    result = 1;
} else {
    result = 0;
}

console.log(result);