const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [gender, age] = input.map(Number);

let result = null;
if (gender === 0) {
    if (age >= 19) {
        result = 'MAN';
    } else {
        result = 'BOY';
    }
} else {
    if (age >= 19) {
        result = 'WOMAN';
    } else {
        result = 'GIRL';
    }
}

console.log(result);