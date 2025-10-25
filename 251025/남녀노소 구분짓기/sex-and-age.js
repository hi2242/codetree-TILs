const fs = require('fs');

let input = fs.readFileSync(0).toString().trim().split('\n');
let result = null;

let human = {
    gender : Number(input[0]),
    age : Number(input[1]),
};

if (human.gender === 0) {
    if (human.age >= 19) {
        result = 'MAN';
    } else {
        result = 'BOY';
    }
} else {
    if (human.age >= 19) {
        result = 'WOMAN';
    } else {
        result = 'GIRL';
    }
}

console.log(result);